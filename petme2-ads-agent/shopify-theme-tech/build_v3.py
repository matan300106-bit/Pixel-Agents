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

# Shorter buy box: the long product description no longer sits open under the buy buttons.
# It moves into a closed "Full product details" drop-down (owner: "long large text ... stressing").
P = load("templates/product.json")
main = P["sections"]["main"]
if "description" in main["blocks"]:
    i = main["block_order"].index("description")
    main["block_order"][i] = "details"
    del main["blocks"]["description"]
    main["blocks"]["details"] = {"type": "custom_liquid", "settings": {"custom_liquid": (
        '<details class="pm2-details"><summary>Full product details</summary>'
        '<div class="pm2-details__body rte">{{ product.description }}</div></details>'
        '<style>.pm2-details{border-top:1px solid rgba(var(--color-foreground),.12);border-bottom:1px solid rgba(var(--color-foreground),.12)}'
        '.pm2-details summary{cursor:pointer;list-style:none;padding:16px 0;min-height:44px;font-weight:600;display:flex;justify-content:space-between;align-items:center}'
        '.pm2-details summary::-webkit-details-marker{display:none}.pm2-details summary::after{content:"+";font-size:22px;font-weight:300}'
        '.pm2-details[open] summary::after{content:"\\2013"}.pm2-details__body{padding:0 0 18px;font-size:15px;line-height:1.6}</style>')}}
    save("templates/product.json", P)
print("product main blocks:", P["sections"]["main"]["block_order"])

# Dual Bowl feeder comes in 2 colors, sold as 2 linked products (black / white).
# Show a "Color" swatch picker under the price on both pages; the other color links to its page.
P = load("templates/product.json")
main = P["sections"]["main"]
main["blocks"]["colors"] = {"type": "custom_liquid", "settings": {"custom_liquid": (
    "{%- assign pm2_black = '2-in-1-smart-feeder' -%}{%- assign pm2_white = '2-in-1-smart-feeder-white' -%}"
    "{%- if product.handle == pm2_black or product.handle == pm2_white -%}"
    "<div class=\"pm2-colors\" role=\"group\" aria-label=\"Color\">"
    "<p class=\"pm2-colors__label\">Color: <strong>{% if product.handle == pm2_black %}Black{% else %}White{% endif %}</strong></p>"
    "<div class=\"pm2-colors__row\">"
    "<a href=\"{{ routes.root_url | append: 'products/' | replace: '//', '/' }}{{ pm2_black }}\" class=\"pm2-colors__swatch{% if product.handle == pm2_black %} is-active{% endif %}\" "
    "{% if product.handle == pm2_black %}aria-current=\"true\"{% endif %} aria-label=\"Black\"><span style=\"background:#1d1f24\"></span>Black</a>"
    "<a href=\"{{ routes.root_url | append: 'products/' | replace: '//', '/' }}{{ pm2_white }}\" class=\"pm2-colors__swatch{% if product.handle == pm2_white %} is-active{% endif %}\" "
    "{% if product.handle == pm2_white %}aria-current=\"true\"{% endif %} aria-label=\"White\"><span style=\"background:#f4f4f2\"></span>White</a>"
    "</div></div>"
    "<style>.pm2-colors__label{margin:0 0 10px;font-size:15px}"
    ".pm2-colors__row{display:flex;gap:10px;flex-wrap:wrap}"
    ".pm2-colors__swatch{display:inline-flex;align-items:center;gap:10px;min-height:48px;padding:6px 18px 6px 8px;border-radius:999px;"
    "border:1.5px solid rgba(var(--color-foreground),.18);text-decoration:none;color:rgb(var(--color-foreground));font-weight:600}"
    ".pm2-colors__swatch span{width:30px;height:30px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.15)}"
    ".pm2-colors__swatch.is-active{border-color:rgb(var(--color-button));box-shadow:0 0 0 1px rgb(var(--color-button))}"
    ".pm2-colors__swatch:hover{border-color:rgb(var(--color-foreground))}</style>"
    "{%- endif -%}")}}
if "colors" not in main["block_order"]:
    main["block_order"].insert(main["block_order"].index("price") + 1, "colors")
save("templates/product.json", P)
print("main blocks:", main["block_order"])
