"""Shop page (/pages/shop, template page.shop): Water Fountains -> Feeders -> Supplements (coming soon),
with jump pills at the top. Also sets the homepage tab order to the same 3 groups."""
import json
from pathlib import Path

HERE = Path(__file__).parent
PILLS = (
    "<div class=\"pm2-shop page-width\"><h1 class=\"pm2-shop__title\">Shop</h1>"
    "<p class=\"pm2-shop__sub\">Free U.S. shipping on every order · 30-day money-back guarantee</p>"
    "<nav class=\"pm2-shop__nav\" aria-label=\"Shop by category\">"
    "<a href=\"#fountains\">Water Fountains</a><a href=\"#feeders\">Feeders</a>"
    "<a href=\"#supplements\">Supplements <span class=\"pm2-shop__soon\">Coming soon</span></a></nav></div>"
    "<style>.pm2-shop{text-align:center}.pm2-shop__title{margin:0 0 6px}.pm2-shop__sub{margin:0 0 18px;color:rgba(var(--color-foreground),.7)}"
    ".pm2-shop__nav{display:flex;flex-wrap:wrap;justify-content:center;gap:10px}"
    ".pm2-shop__nav a{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 18px;border-radius:999px;"
    "border:1.5px solid rgba(var(--color-foreground),.14);text-decoration:none;color:rgb(var(--color-foreground));font-weight:700;font-size:15px;background:rgb(var(--color-background))}"
    ".pm2-shop__nav a:hover{border-color:rgb(var(--color-button));color:rgb(var(--color-button))}"
    ".pm2-shop__soon{padding:2px 8px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;background:rgb(var(--color-button));color:rgb(var(--color-button-text))}"
    ".pm2-anchor{position:relative;top:calc(-1 * var(--header-height, 64px) - 12px)}</style>"
)

def anchor(i):
    return {"type": "custom-liquid", "settings": {"custom_liquid": f"<div id=\"{i}\" class=\"pm2-anchor\"></div>",
                                                  "color_scheme": "scheme-3", "padding_top": 0, "padding_bottom": 0}}

def group(handle, title, text, scheme, quick_add="standard"):
    return {"type": "featured-collection", "settings": {
        "collection": handle, "products_to_show": 12, "title": title, "heading_size": "h1",
        "description": f"<p>{text}</p>", "show_description": True, "description_style": "body",
        "columns_desktop": 4, "enable_desktop_slider": False, "full_width": False, "show_view_all": False,
        "view_all_style": "outline", "color_scheme": scheme, "image_ratio": "square", "image_shape": "default",
        "show_secondary_image": True, "show_vendor": False, "show_rating": False, "quick_add": quick_add,
        "columns_mobile": "2", "swipe_on_mobile": False, "padding_top": 28, "padding_bottom": 44}}

S = {
    "intro": {"type": "custom-liquid", "settings": {"custom_liquid": PILLS, "color_scheme": "scheme-4", "padding_top": 36, "padding_bottom": 32}},
    "a_fountains": anchor("fountains"),
    "fountains": group("water-fountains", "Water Fountains", "Fresh, moving water all day. Quiet pumps, easy to clean.", "scheme-3"),
    "a_feeders": anchor("feeders"),
    "feeders": group("feeders", "Automatic Feeders", "Meals on time, set from your phone. For 1 or 2 cats.", "scheme-4"),
    "a_supplements": anchor("supplements"),
    "supplements": group("supplements", "Supplements · Coming soon",
                         "Daily soft chews for cats and dogs, launching soon. Open a product and tap Notify me to get an email on launch day.",
                         "scheme-3", quick_add="none"),
}
(HERE / "templates/page.shop.json").write_text(json.dumps({"sections": S, "order": list(S)}, indent=2, ensure_ascii=False) + "\n")
print("page.shop:", list(S))
