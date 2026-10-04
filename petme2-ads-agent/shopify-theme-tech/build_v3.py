"""V3 conversion layer: runs after build.py, build_v2.py and build_pages.py.
Adds the welcome popup (header group), trust badges (product + cart) and the
30-day money-back guarantee band (homepage + product page),
the product story (pm2-product-story) and the real-life highlights strip that replaces reviews."""
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
    "settings": {"product_position": "under_buy_buttons", "style": "card", "show_savings": True, "show_low_stock": False,
                 "low_stock_threshold": 5, "delivery_note": "Orders are fulfilled by Amazon", "color_scheme": "scheme-3",
                 "padding_top": 0, "padding_bottom": 0}})
insert_after(P, "extras", "guarantee", {"type": "pm2-guarantee", "settings": {
    "style": "card", "icon": "shield", "color_scheme": "scheme-4", "padding_top": 24, "padding_bottom": 24}})
# Story-telling product page: product photos as story chapters (metafield custom.story), then an honest
# "Made for real life" day strip in place of the reviews app block (no ratings, no quotes).
P["sections"].pop("reviews", None)
if "reviews" in P["order"]:
    P["order"].remove("reviews")
insert_after(P, "specs", "story", {"type": "pm2-product-story", "settings": {
    "eyebrow": "See it in action", "heading": "What it does for you",
    "subheading": "Scroll through the photos. One idea at a time.", "max_chapters": 6,
    "show_cta": True, "cta_label": "Add to cart", "cta_note": "Free U.S. shipping. 30-day money-back guarantee.",
    "color_scheme": "scheme-3", "padding_top": 40, "padding_bottom": 56}})
insert_after(P, "story", "highlights", {"type": "pm2-product-highlights", "settings": {
    "eyebrow": "Made for real life", "heading": "A normal day, made easier",
    "feeder_moments": "Morning :: Breakfast, on time :: The feeder serves the meal times and portions you set in the app.\n"
                      "At work :: Change plans from your phone :: Running late? Edit the meal schedule in the app.\n"
                      "Evening :: Dinner, even when you are out :: Meals keep coming on the schedule you set.\n"
                      "Once in a while :: Refill and wipe :: Top up the dry food. Stainless steel wipes clean.",
    "fountain_moments": "Morning :: Fresh, moving water :: The pump keeps the water moving all day.\n"
                        "All day :: Calm at home :: A quiet pump, made for use inside the home.\n"
                        "Night :: Quiet enough for bedtime :: Low noise, day and night.\n"
                        "Cleaning day :: Comes apart to clean :: Take it apart, rinse, put it back together.",
    "color_scheme": "scheme-4", "padding_top": 48, "padding_bottom": 48}})
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
