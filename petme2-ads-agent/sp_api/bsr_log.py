"""Append today's BSR for every PETME2 ASIN to reports/rank-history.csv (read only).

Run: python -m sp_api.bsr_log
"""
import csv
import time
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .auth import PROJECT_ROOT
from .client import get

OUT = PROJECT_ROOT / "reports" / "rank-history.csv"


def main():
    products = yaml.safe_load(open(PROJECT_ROOT / "products.yaml"))["products"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    rows = []
    for p in products:
        r = get(f"/catalog/2022-04-01/items/{p['asin']}", marketplaceIds="ATVPDKIKX0DER",
                includedData="salesRanks")
        for sr in r.get("salesRanks", []):
            for c in sr.get("classificationRanks", []):
                rows.append([now, p["asin"], p["title"], c["title"], c["rank"]])
            for d in sr.get("displayGroupRanks", []):
                rows.append([now, p["asin"], p["title"], d["title"] + " (main)", d["rank"]])
        time.sleep(0.6)
    new = not OUT.exists()
    with open(OUT, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["utc_time", "asin", "product", "category", "rank"])
        w.writerows(rows)
    for r in rows:
        if "(main)" not in r[3]:
            print(f"{r[2]:<28} #{r[4]:<6} {r[3]}")


if __name__ == "__main__":
    main()
