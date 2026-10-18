"""Shop all: /collections/shop-all (template collection.shop-all) and /pages/shop (template page.shop) share one layout:
title + jump pills, then Water Fountains -> Automatic Feeders -> Supplements (coming soon), each a pm2-shop-group
(category photo card + product grid). Also keeps the homepage tab order Fountains, Feeders, Supplements."""
import json
from pathlib import Path

HERE = Path(__file__).parent
IMG = "shopify://shop_images/"
PILLS = (
    "<div class=\"pm2-shop page-width\"><h1 class=\"pm2-shop__title\">Shop all</h1>"
    "<p class=\"pm2-shop__sub\">Free U.S. shipping on every order · 30-day money-back guarantee</p>"
    "<nav class=\"pm2-shop__nav\" aria-label=\"Shop by category\">"
    "<a href=\"#fountains\"><span class=\"pm2-shop__n\">01</span>Water Fountains</a>"
    "<a href=\"#feeders\"><span class=\"pm2-shop__n\">02</span>Automatic Feeders</a>"
    "<a href=\"#supplements\"><span class=\"pm2-shop__n\">03</span>Supplements <span class=\"pm2-shop__soon\">Soon</span></a></nav></div>"
    "<style>.pm2-shop{text-align:center}.pm2-shop__title{margin:0 0 6px}.pm2-shop__sub{margin:0 0 18px;color:rgba(var(--color-foreground),.7)}"
    ".pm2-shop__nav{display:flex;flex-wrap:wrap;justify-content:center;gap:8px}"
    ".pm2-shop__nav a{display:inline-flex;align-items:center;gap:8px;min-height:44px;padding:0 16px 0 8px;border-radius:999px;"
    "border:1.5px solid rgba(var(--color-foreground),.12);text-decoration:none;color:rgb(var(--color-foreground));font-weight:700;font-size:15px;background:rgb(var(--color-background))}"
    ".pm2-shop__nav a:hover{border-color:rgb(var(--color-button));color:rgb(var(--color-button))}"
    ".pm2-shop__n{display:inline-flex;align-items:center;justify-content:center;width:30px;height:30px;border-radius:50%;font-size:12px;font-weight:800;background:rgba(var(--color-button),.1);color:rgb(var(--color-button))}"
    ".pm2-shop__soon{padding:2px 8px;border-radius:999px;font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;background:rgb(var(--color-button));color:rgb(var(--color-button-text))}"
    "[id=fountains],[id=feeders],[id=supplements]{scroll-margin-top:calc(var(--header-height,64px) + 12px)}"
    "@media (max-width:749px){.pm2-shop__nav{flex-wrap:nowrap;overflow-x:auto;justify-content:flex-start;margin:0 -1.5rem;padding:0 1.5rem 4px;scrollbar-width:none}"
    ".pm2-shop__nav::-webkit-scrollbar{display:none}.pm2-shop__nav a{flex:none}}</style>"
)

def group(handle, anchor, number, title, text, image, scheme, badge="", quick_add=True):
    return {"type": "pm2-shop-group", "settings": {
        "collection": handle, "anchor": anchor, "number": number, "title": title, "badge": badge, "text": text,
        "image": image, "show_link": True, "quick_add": quick_add, "color_scheme": scheme,
        "padding_top": 48, "padding_bottom": 48}}

S = {
    "intro": {"type": "custom-liquid", "settings": {"custom_liquid": PILLS, "color_scheme": "scheme-4", "padding_top": 36, "padding_bottom": 28}},
    "fountains": group("water-fountains", "fountains", "01", "Water Fountains",
                       "Fresh, moving water all day. Quiet pumps, easy to clean.",
                       IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png", "scheme-3"),
    "feeders": group("feeders", "feeders", "02", "Automatic Feeders",
                     "Meals on time, set from your phone. For 1 or 2 cats.",
                     IMG + "petme2-hero-2-cats-poster.jpg", "scheme-4"),
    "supplements": group("supplements", "supplements", "03", "Supplements",
                         "Daily soft chews for cats and dogs, launching soon. Open a product and tap Notify me.",
                         IMG + "petme2-supplements-banner.png", "scheme-3", badge="Coming soon", quick_add=False),
}
doc = json.dumps({"sections": S, "order": list(S)}, indent=2, ensure_ascii=False) + "\n"
(HERE / "templates/collection.shop-all.json").write_text(doc)
(HERE / "templates/page.shop.json").write_text(doc)
print("shop-all:", list(S))
