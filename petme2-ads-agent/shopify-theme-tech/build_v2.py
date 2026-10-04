"""V2 'friendly minimal, built to sell' layout: runs after build.py. Rebuilds the homepage around the pm2-*
sections (hero, ticker, product tabs, quiz, short bento, compare, FAQ, CTA band), adds spec chips + sticky add-to-cart to the
product page, and the global style section to the header group. True claims only."""
import json
from pathlib import Path

HERE = Path(__file__).parent
IMG = "shopify://shop_images/"
load = lambda p: json.loads((HERE / p).read_text())
save = lambda p, o: (HERE / p).write_text(json.dumps(o, indent=2, ensure_ascii=False) + "\n")


def sec(type_, settings, blocks=()):
    s = {"type": type_, "settings": settings}
    if blocks:
        s["blocks"] = {f"b{i}": {"type": t, "settings": st} for i, (t, st) in enumerate(blocks, 1)}
        s["block_order"] = list(s["blocks"])
    return s


old = load("templates/index.json")["sections"]
# Built-to-sell homepage: white base, ONE soft neutral (scheme-4 cloud), mint (scheme-5) only for trust.
# The action blue is reserved for buttons, so the buy/shop buttons are the most visible thing on each screen.
# Order: hero -> ticker -> shop tabs -> quiz -> short bento -> compare feeders -> compare fountains -> FAQ -> CTA.
OFFER = "Free U.S. shipping · 30-day money-back guarantee"
S = {}
S["hero"] = sec("pm2-hero", {
    "color_scheme": "scheme-4", "show_grid": False, "eyebrow_tag": "Sale", "eyebrow": "Save up to 33% · for cats & small dogs",
    "heading_line_1": "Easy everyday", "heading_highlight": "pet care.",
    "subtext": "Meals on time from an automatic feeder. Fresh, moving water from a quiet fountain. Set it up once and enjoy more time together.",
    "button_label_1": "Shop now", "button_link_1": "shopify://collections/all",
    "button_label_2": "", "button_link_2": "",
    "chip_1": OFFER, "chip_2": "", "chip_3": "",
    # pet photo (the old theme's mobile hero banner): shown on phones instead of the product card
    "product": "smart-feeder", "link_product": True, "image": IMG + "image_846.jpg",
    "badge_1": "1080P live view", "badge_2": "2-way audio", "badge_3": "",
    "padding_top": 40, "padding_bottom": 56})
S["ticker"] = sec("pm2-marquee", {"color_scheme": "scheme-3", "duration": 40, "size": "small",
                                   "show_divider": True, "show_borders": True, "reverse": False}, [
    ("item", {"text": "Sale: save up to 33%", "icon": "sparkle"}),
    ("item", {"text": "Free U.S. shipping", "icon": "truck"}),
    ("item", {"text": "30-day money-back guarantee", "icon": "sparkle"}),
    ("item", {"text": "10% off your first order", "icon": "sparkle"}),
    ("item", {"text": "For cats & small dogs", "icon": "paw"})])
S["shop"] = sec("pm2-product-tabs", {"eyebrow": "Shop", "heading": "Feeders, fountains & supplements",
                                     "color_scheme": "scheme-3", "products_per_tab": 4, "show_view_all": True,
                                     "padding_top": 56, "padding_bottom": 56}, [
    ("tab", {"label": "Feeders", "collection": "feeders", "text": "Meals on time, set from your phone."}),
    ("tab", {"label": "Fountains", "collection": "water-fountains", "text": "Fresh, moving water with a quiet pump."}),
    ("tab", {"label": "Supplements", "collection": "supplements", "text": "Daily soft chews for cats and dogs. Coming soon."})])
# Feeder finder quiz (another agent's section): only added when the section exists.
if (HERE / "sections" / "pm2-quiz.liquid").exists():
    S["quiz"] = {"type": "pm2-quiz", "settings": {
        "color_scheme": "scheme-4",
        "note_feeder": "For dry food · cats & small dogs · " + OFFER,
        "note_fountain": "Quiet pump · comes apart for cleaning · " + OFFER}}
# Short bento: 4 tiles (large + 2 small + wide fills a clean 4x2 grid on desktop, 2 cols on phones).
S["bento"] = sec("pm2-bento", {"eyebrow": "Why pet parents pick PETME2", "heading": "Simple care, done for you.",
                               "subheading": "<p>Set it up once. They eat on time and drink fresh water.</p>",
                               "color_scheme": "scheme-3", "padding_top": 56, "padding_bottom": 56}, [
    ("image_tile", {"size": "large", "image": IMG + "Your_pets_meals_managed_from_your_phone_3d0ac522-2f46-4a7b-a1d9-e2b48f76d5bb.jpg",
                    "eyebrow": "App control", "title": "Meals on time, from your phone",
                    "text": "Set meal times and portions in the app.", "link": "shopify://collections/feeders", "link_label": "Shop feeders"}),
    ("stat_tile", {"size": "small", "value": "1080P", "label": "Live view", "text": "See and talk to your pet with the 3L Camera feeder."}),
    ("text_tile", {"size": "small", "icon": "bowl", "title": "Two bowls, two pets",
                   "text": "Dual-bowl feeders fill two stainless steel bowls. Dry food only."}),
    ("image_tile", {"size": "wide", "image": IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png",
                    "eyebrow": "Fountains", "title": "Fresh water they'll love",
                    "text": "Quiet pumps. Every model comes apart for cleaning.", "link": "shopify://collections/water-fountains", "link_label": "Shop fountains"})])
cmp_f = old["cmp_feeders"]; cmp_f["settings"]["color_scheme"] = "scheme-4"
S["cmp_feeders"] = cmp_f
cmp_w = old["cmp_fountains"]; cmp_w["settings"]["color_scheme"] = "scheme-3"
S["cmp_fountains"] = cmp_w
S["faq"] = old["faq"]
S["faq"]["settings"].update(color_scheme="scheme-4", container_color_scheme="scheme-3", caption="FAQ",
                            heading="Questions? We've got you.", padding_top=56, padding_bottom=56)
# Google FAQ structured data, built from the visible FAQ rows above so the two never drift (schema only)
if (HERE / "sections" / "pm2-faq-schema.liquid").exists():
    _rows = [S["faq"]["blocks"][k]["settings"] for k in S["faq"]["block_order"]]
    S["faq_schema"] = sec("pm2-faq-schema", {"output_schema": True, "show_visible": False}, [
        ("faq", {"question": r["heading"], "answer": r["row_content"]}) for r in _rows])
S["cta"] = sec("pm2-cta-band", {"eyebrow": "Ready when you are", "heading": "Easy care starts here.",
                                "text": "<p>Try it for 30 days. If your pet doesn't love it, get your money back.</p>",
                                "button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders",
                                "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains",
                                "color_scheme": "scheme-5", "padding_top": 64, "padding_bottom": 64}, [
    ("chip", {"text": "Free U.S. shipping"}), ("chip", {"text": "30-day money-back guarantee"}),
    ("chip", {"text": "10% off your first order"})])
save("templates/index.json", {"sections": S, "order": list(S)})

# product page: spec chips under main, sticky add-to-cart
P = load("templates/product.json")
ps = P["sections"]
new = {"main": ps["main"],
       "specs": {"type": "pm2-spec-chips", "settings": {"heading": "Key specs", "color_scheme": "scheme-3", "padding_top": 8, "padding_bottom": 40}}}
for k in P["order"]:
    if k != "main":
        new[k] = ps[k]
new["related-products"]["settings"]["color_scheme"] = "scheme-3"
new["sticky_atc"] = {"type": "pm2-sticky-atc", "settings": {"color_scheme": "scheme-3", "show_thumbnail": True, "hide_on_desktop": False}}
save("templates/product.json", {"sections": new, "order": list(new)})

# header group: global friendly-minimal style (frosted header, pill buttons, 16px body on phones)
H = load("sections/header-group.json")
H["sections"]["pm2-global-style"] = {"type": "pm2-global-style", "settings": {
    "action_color": "#2F5FE0", "action_label": "#FFFFFF", "check_color": "#1E7B4F", "enable_sell": True,
    "enable_glass_header": True, "glass_tint": "light", "glass_opacity": 80, "enable_buttons": True, "enable_cards": True,
    "enable_image_zoom": True, "enable_typography": True, "enable_eyebrow": True, "enable_focus": True,
    "enable_selection": True, "enable_smooth_scroll": True}}
if "pm2-global-style" not in H["order"]:
    H["order"].append("pm2-global-style")
save("sections/header-group.json", H)

# footer: newsletter on (10% off first order, code sent by email), soft neutral background
F = load("sections/footer-group.json")
F["sections"]["footer"]["settings"].update(newsletter_enable=True, color_scheme="scheme-4",
                                           newsletter_heading="Get 10% off your first order")
save("sections/footer-group.json", F)
print("homepage:", list(S))
print("product:", list(new))
