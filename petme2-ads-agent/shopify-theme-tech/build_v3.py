"""V3 conversion layer: runs after build.py, build_v2.py and build_pages.py.
Adds the welcome popup (header group), trust badges (product + cart) and the
30-day money-back guarantee band (homepage + product page)."""
import json
from pathlib import Path

HERE = Path(__file__).parent
load = lambda p: json.loads((HERE / p).read_text())
save = lambda p, o: (HERE / p).write_text(json.dumps(o, indent=2, ensure_ascii=False) + "\n")

BADGES = {"b1": {"type": "badge", "settings": {"icon": "truck", "text": "Free U.S. shipping"}},
          "b2": {"type": "badge", "settings": {"icon": "money_back", "text": "30-day money-back guarantee"}},
          "b3": {"type": "badge", "settings": {"icon": "lock", "text": "Secure checkout"}},
          "b4": {"type": "badge", "settings": {"icon": "box", "text": "Fulfilled by Amazon"}}}


def insert_after(tpl, after, key, section):
    tpl["sections"][key] = section
    if key in tpl["order"]:
        tpl["order"].remove(key)
    tpl["order"].insert(tpl["order"].index(after) + 1, key)


H = load("sections/header-group.json")
H["sections"]["pm2-popup"] = {"type": "pm2-popup", "settings": {
    "enabled": True, "code": "WELCOME10", "delay_seconds": 12, "scroll_percent": 40, "desktop_delay_seconds": 20,
    "cap_days": 14, "show_on_mobile": True, "auto_apply": True, "show_code_without_email": False, "color_scheme": "scheme-3"}}
if "pm2-popup" not in H["order"]:
    H["order"].append("pm2-popup")
save("sections/header-group.json", H)

P = load("templates/product.json")
insert_after(P, "main", "trust_badges", {"type": "pm2-trust-badges", "blocks": BADGES, "block_order": list(BADGES),
    "settings": {"product_position": "under_buy_buttons", "style": "card", "show_savings": True, "show_low_stock": True,
                 "low_stock_threshold": 5, "delivery_note": "Ships fast from Amazon's U.S. network", "color_scheme": "scheme-3",
                 "padding_top": 0, "padding_bottom": 0}})
insert_after(P, "extras", "guarantee", {"type": "pm2-guarantee", "settings": {
    "style": "card", "icon": "shield", "color_scheme": "scheme-4", "padding_top": 24, "padding_bottom": 24}})
save("templates/product.json", P)

I = load("templates/index.json")
insert_after(I, "cmp_fountains", "guarantee", {"type": "pm2-guarantee", "settings": {
    "style": "card", "icon": "shield", "color_scheme": "scheme-4", "padding_top": 36, "padding_bottom": 36}})
save("templates/index.json", I)

C = load("templates/cart.json")
insert_after(C, "cart-footer", "trust_badges", {"type": "pm2-trust-badges", "blocks": BADGES, "block_order": list(BADGES),
    "settings": {"style": "plain", "show_savings": False, "show_low_stock": False, "delivery_note": "",
                 "color_scheme": "scheme-3", "padding_top": 8, "padding_bottom": 24}})
save("templates/cart.json", C)
print("index:", I["order"]); print("product:", P["order"]); print("cart:", C["order"]); print("header:", H["order"])
