"""Daily product snapshot (read only).

Run: python -m sp_api.snapshot [--days 60] [--no-fees]
Writes data/YYYY-MM-DD/products.json and products.csv and prints a table:
ASIN, title, price, FBA stock, units sold.
"""
import argparse
import csv
import json
import sys
import time
from datetime import date
from pathlib import Path

from .auth import PROJECT_ROOT, MissingKeysError
from .products import get_catalog_item, get_fba_inventory, get_fees, get_my_prices, get_sales


def build(days=60, with_fees=True, log=print):
    log("Reading FBA inventory ...")
    items = get_fba_inventory()
    log(f"  {len(items)} items found.")

    log("Reading your prices ...")
    prices = get_my_prices([i["sku"] for i in items])

    rows = []
    for n, item in enumerate(items, 1):
        asin = item["asin"]
        log(f"Reading sales for {asin} ({n}/{len(items)}) ...")
        row = dict(item)
        row["price"] = prices.get(item["sku"])
        if not row.get("title"):
            row["title"] = get_catalog_item(asin).get("title")
        total = get_sales(days=days, asin=asin)
        row[f"units_{days}d"] = total[0]["units"] if total else 0
        row[f"sales_{days}d"] = total[0]["sales"] if total else 0.0
        row["units_per_day"] = round(row[f"units_{days}d"] / days, 2)
        row["stock_days"] = (round(row["fba_available"] / row["units_per_day"], 1)
                             if row["units_per_day"] else None)
        if with_fees and row["price"]:
            fees = get_fees(asin, row["price"])
            row["amazon_fees"] = fees["total_fees"]
            row["referral_fee"] = fees["referral_fee"]
            row["fba_fee"] = fees["fba_fee"]
        rows.append(row)
        time.sleep(2)  # Sales API allows ~0.5 calls per second
    return rows


def save(rows, day=None):
    folder = PROJECT_ROOT / "data" / (day or date.today().isoformat())
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "products.json").write_text(json.dumps(rows, indent=2))
    if rows:
        fields = list(dict.fromkeys(k for r in rows for k in r))
        with open(folder / "products.csv", "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)
    return folder


def print_table(rows, days=60):
    def cut(s, n):
        s = str(s or "")
        return s if len(s) <= n else s[:n - 1] + "…"

    print(f"\n| ASIN | Title | Price | FBA stock | Units sold ({days} days) |")
    print("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: -(r.get(f"units_{days}d") or 0)):
        price = f"${r['price']:.2f}" if r.get("price") else "-"
        print(f"| {r['asin']} | {cut(r.get('title'), 50)} | {price} | "
              f"{r.get('fba_available', 0)} | {r.get(f'units_{days}d', 0)} |")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=60)
    ap.add_argument("--no-fees", action="store_true")
    args = ap.parse_args()
    try:
        rows = build(days=args.days, with_fees=not args.no_fees)
    except MissingKeysError as e:
        print(f"Not ready: {e}")
        return 1
    folder = save(rows)
    print_table(rows, args.days)
    print(f"\nSaved to {Path(folder).relative_to(PROJECT_ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
