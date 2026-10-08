"""Ask buyers for a review with Amazon's official "Request a Review" (Solicitations API).

Owner asked for this on 2026-10-04 ("have an agent that asks for reviews, always").
This is the ONLY write action in sp_api/. It can do exactly one thing: send Amazon's
standard review + seller-feedback request for one order. Amazon writes the message,
allows it once per order, only 5-30 days after delivery, and refuses it otherwise.

Run:  python3 -m sp_api.reviews            -> dry run: list eligible orders, send nothing
      python3 -m sp_api.reviews --send     -> send to every eligible order not sent before
Log:  reviews-sent.csv (order id, date, result). Orders in the log are never sent again.
"""
import argparse
import csv
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import requests

from .auth import PROJECT_ROOT, get_access_token
from .client import ENDPOINT, MARKETPLACE_ID, SpApiError, get
from .orders import list_orders

LOG = PROJECT_ROOT / "reviews-sent.csv"
ACTION = "productReviewAndSellerFeedback"


def _done():
    if not LOG.exists():
        return set()
    with open(LOG, newline="") as f:
        return {r["order_id"] for r in csv.DictReader(f) if r["result"] in ("sent", "not_eligible_final")}


def _log(order_id, result, note=""):
    new = not LOG.exists()
    with open(LOG, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["order_id", "date", "result", "note"])
        w.writerow([order_id, date.today().isoformat(), result, note])


def eligible(order_id):
    d = get(f"/solicitations/v1/orders/{order_id}", marketplaceIds=MARKETPLACE_ID)
    return any(a.get("name") == ACTION for a in (d.get("_links", {}).get("actions") or []))


def send(order_id):
    path = f"/solicitations/v1/orders/{order_id}/solicitations/{ACTION}"
    for attempt in range(6):
        r = requests.post(ENDPOINT + path, params={"marketplaceIds": MARKETPLACE_ID},
                          headers={"x-amz-access-token": get_access_token(),
                                   "user-agent": "petme2-ads-agent/1.0 (Language=Python)"},
                          timeout=60)
        if r.status_code == 429 or r.status_code >= 500:
            time.sleep(min(2 ** attempt, 30))
            continue
        if r.status_code >= 400:
            raise SpApiError(f"HTTP {r.status_code}: {r.text[:300]}")
        return
    raise SpApiError("Amazon kept saying 'too many requests'.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--send", action="store_true", help="really send (default: dry run)")
    ap.add_argument("--days", type=int, default=35)
    args = ap.parse_args()
    done = _done()
    now = datetime.now(timezone.utc)
    orders = [o for o in list_orders(days=args.days)
              if o["status"] == "Shipped" and o["order_id"] not in done
              and (now - datetime.fromisoformat(o["purchase_date"].replace("Z", "+00:00"))).days >= 5]
    sent = skipped = errors = 0
    for o in orders:
        oid = o["order_id"]
        try:
            ok = eligible(oid)
            time.sleep(1.1)
            if not ok:
                skipped += 1
                age = (now - datetime.fromisoformat(o["purchase_date"].replace("Z", "+00:00"))).days
                if args.send and age > 30:
                    _log(oid, "not_eligible_final", f"{age} days old")
                continue
            if args.send:
                send(oid)
                _log(oid, "sent")
                time.sleep(1.1)
            sent += 1
        except SpApiError as e:
            errors += 1
            if args.send:
                _log(oid, "error", str(e)[:120])
    word = "Sent" if args.send else "Would send"
    print(f"{word}: {sent} review requests. Not eligible now: {skipped}. Errors: {errors}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
