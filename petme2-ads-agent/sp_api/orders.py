"""Read orders (read only). No buyer personal data is requested."""
from datetime import datetime, timedelta, timezone

from .client import MARKETPLACE_ID, get


def list_orders(days=60):
    """All orders created in the last `days` days (summary fields only)."""
    created_after = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    orders, next_token = [], None
    while True:
        if next_token:
            data = get("/orders/v0/orders", MarketplaceIds=MARKETPLACE_ID, NextToken=next_token)
        else:
            data = get("/orders/v0/orders", MarketplaceIds=MARKETPLACE_ID, CreatedAfter=created_after)
        payload = data.get("payload", {})
        for o in payload.get("Orders", []):
            orders.append({
                "order_id": o.get("AmazonOrderId"),
                "purchase_date": o.get("PurchaseDate"),
                "status": o.get("OrderStatus"),
                "channel": o.get("FulfillmentChannel"),
                "total": (o.get("OrderTotal") or {}).get("Amount"),
                "items_shipped": o.get("NumberOfItemsShipped"),
                "items_unshipped": o.get("NumberOfItemsUnshipped"),
            })
        next_token = payload.get("NextToken")
        if not next_token:
            return orders


def get_order_items(order_id):
    """ASIN, SKU, quantity and price for one order."""
    data = get(f"/orders/v0/orders/{order_id}/orderItems")
    return [{
        "asin": i.get("ASIN"),
        "sku": i.get("SellerSKU"),
        "quantity": i.get("QuantityOrdered"),
        "item_price": (i.get("ItemPrice") or {}).get("Amount"),
    } for i in data.get("payload", {}).get("OrderItems", [])]
