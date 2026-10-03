"""Read products, prices, fees, FBA inventory and sales (read only)."""
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from .client import MARKETPLACE_ID, call, get

SALES_TZ = "America/Los_Angeles"  # Seller Central US uses Pacific time


def get_fba_inventory():
    """All FBA items: asin, sku, title, stock numbers."""
    items, next_token = [], None
    while True:
        params = {
            "details": "true",
            "granularityType": "Marketplace",
            "granularityId": MARKETPLACE_ID,
            "marketplaceIds": MARKETPLACE_ID,
        }
        if next_token:
            params["nextToken"] = next_token
        data = get("/fba/inventory/v1/summaries", **params)
        for s in data.get("payload", {}).get("inventorySummaries", []):
            d = s.get("inventoryDetails") or {}
            reserved = (d.get("reservedQuantity") or {}).get("totalReservedQuantity", 0)
            inbound = sum(d.get(k, 0) or 0 for k in (
                "inboundWorkingQuantity", "inboundShippedQuantity", "inboundReceivingQuantity"))
            items.append({
                "asin": s.get("asin"),
                "sku": s.get("sellerSku"),
                "title": s.get("productName"),
                "fba_available": d.get("fulfillableQuantity", 0),
                "fba_reserved": reserved,
                "fba_inbound": inbound,
                "fba_total": s.get("totalQuantity", 0),
            })
        next_token = (data.get("pagination") or {}).get("nextToken")
        if not next_token:
            return items


def get_catalog_item(asin):
    """Title, brand and best seller rank for one ASIN."""
    data = get(f"/catalog/2022-04-01/items/{asin}",
               marketplaceIds=MARKETPLACE_ID, includedData="summaries,salesRanks")
    summary = next(iter(data.get("summaries") or []), {})
    ranks = next(iter(data.get("salesRanks") or []), {})
    top = next(iter(ranks.get("displayGroupRanks") or []), {})
    return {
        "asin": asin,
        "title": summary.get("itemName"),
        "brand": summary.get("brand"),
        "sales_rank": top.get("rank"),
        "sales_rank_group": top.get("title"),
    }


def get_my_prices(skus):
    """Your own current price per SKU. Returns {sku: price}."""
    prices = {}
    skus = [s for s in skus if s]
    for i in range(0, len(skus), 20):  # max 20 per call
        data = get("/products/pricing/v0/price", MarketplaceId=MARKETPLACE_ID,
                   ItemType="Sku", Skus=",".join(skus[i:i + 20]))
        for row in data.get("payload", []):
            offers = (row.get("Product") or {}).get("Offers") or []
            if offers:
                buying = offers[0].get("BuyingPrice") or {}
                listing = (buying.get("ListingPrice") or {}).get("Amount")
                prices[row.get("SellerSKU")] = listing
        time.sleep(2)  # this endpoint is slow (0.5 calls per second)
    return prices


def get_fees(asin, price):
    """Amazon fees per unit (referral + FBA) at this price. Only an estimate - changes nothing."""
    body = {"FeesEstimateRequest": {
        "MarketplaceId": MARKETPLACE_ID,
        "IsAmazonFulfilled": True,
        "PriceToEstimateFees": {"ListingPrice": {"CurrencyCode": "USD", "Amount": price}},
        "Identifier": f"fee-{asin}",
    }}
    data = call("POST", f"/products/fees/v0/items/{asin}/feesEstimate", body=body)
    result = data.get("payload", {}).get("FeesEstimateResult", {})
    estimate = result.get("FeesEstimate") or {}
    details = {f.get("FeeType"): (f.get("FinalFee") or {}).get("Amount")
               for f in estimate.get("FeeDetailList") or []}
    return {
        "total_fees": (estimate.get("TotalFeesEstimate") or {}).get("Amount"),
        "referral_fee": details.get("ReferralFee"),
        "fba_fee": details.get("FBAFees"),
        "status": result.get("Status"),
    }


def _interval(days, end=None):
    tz = ZoneInfo(SALES_TZ)
    end = end or datetime.now(tz).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=days)
    return f"{start.isoformat()}--{end.isoformat()}"


def get_sales(days=60, asin=None, granularity="Total"):
    """Units, orders and sales from the Sales API.

    granularity="Total" gives one row; "Day" gives one row per day.
    The period ends at midnight today (Pacific time), so today is not included.
    """
    params = {
        "marketplaceIds": MARKETPLACE_ID,
        "interval": _interval(days),
        "granularity": granularity,
        "granularityTimeZone": SALES_TZ,
    }
    if asin:
        params["asin"] = asin
    data = get("/sales/v1/orderMetrics", **params)
    rows = []
    for m in data.get("payload", []):
        rows.append({
            "interval": m.get("interval"),
            "units": m.get("unitCount", 0),
            "orders": m.get("orderCount", 0),
            "sales": float((m.get("totalSales") or {}).get("amount") or 0),
        })
    return rows
