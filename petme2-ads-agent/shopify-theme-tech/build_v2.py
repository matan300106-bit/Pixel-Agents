"""V2 'modern' layout: runs after build.py. Rebuilds the homepage around the new pm2-* sections
(hero, marquee, product tabs, bento, steps, CTA band), adds spec chips + sticky add-to-cart to the
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
S = {}
S["hero"] = sec("pm2-hero", {
    "color_scheme": "scheme-1", "show_grid": True, "eyebrow_tag": "New", "eyebrow": "Smart feeders & fountains",
    "heading_line_1": "Smart feeding.", "heading_highlight": "Zero guesswork.",
    "subtext": "App-controlled automatic feeders and quiet water fountains for cats and small dogs. Schedule meals, check in, and keep fresh water flowing.",
    "button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders",
    "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains",
    "chip_1": "Free U.S. shipping $50+", "chip_2": "App control", "chip_3": "Quiet pumps",
    "product": "smart-feeder", "link_product": True, "image": IMG + "main-banner.jpg",
    "badge_1": "1080P live view", "badge_2": "2-way audio", "badge_3": "WiFi app control",
    "padding_top": 96, "padding_bottom": 96})
S["ticker"] = sec("pm2-marquee", {"color_scheme": "scheme-4", "duration": 36, "size": "medium",
                                   "show_divider": True, "show_borders": False, "reverse": False}, [
    ("item", {"text": "Free U.S. shipping on orders $50+", "icon": "truck"}),
    ("item", {"text": "1080P HD live view", "icon": "camera"}),
    ("item", {"text": "WiFi app control", "icon": "wifi"}),
    ("item", {"text": "Quiet fountain pumps", "icon": "drop"}),
    ("item", {"text": "For cats & small dogs", "icon": "paw"}),
    ("item", {"text": "Stainless steel bowls", "icon": "sparkle"}),
    ("item", {"text": "Also sold on Amazon", "icon": "sparkle"})])
S["shop"] = sec("pm2-product-tabs", {"eyebrow": "Shop PETME2", "heading": "Smart feeders and quiet fountains",
                                     "color_scheme": "scheme-3", "products_per_tab": 4, "show_view_all": True,
                                     "padding_top": 88, "padding_bottom": 72}, [
    ("tab", {"label": "Feeders", "collection": "feeders", "text": "App control, dual bowls and a 1080P camera model."}),
    ("tab", {"label": "Fountains", "collection": "water-fountains", "text": "Quiet pumps, from 2L to 3.2L stainless steel."})])
S["bento"] = sec("pm2-bento", {"eyebrow": "Smart pet tech", "heading": "Everything your pet needs. Nothing they don't.",
                               "subheading": "<p>Automatic feeders and quiet fountains, managed from your phone.</p>",
                               "color_scheme": "scheme-1", "padding_top": 96, "padding_bottom": 96}, [
    ("image_tile", {"size": "large", "image": IMG + "Your_pets_meals_managed_from_your_phone_3d0ac522-2f46-4a7b-a1d9-e2b48f76d5bb.jpg",
                    "eyebrow": "App control", "title": "Your pet's meals, managed from your phone",
                    "text": "Set meal times and portions in the app.", "link": "shopify://collections/feeders", "link_label": "Shop smart feeders"}),
    ("stat_tile", {"size": "small", "value": "1080P", "label": "HD live view", "text": "3L Camera feeder, live in the app."}),
    ("stat_tile", {"size": "small", "value": "5L", "label": "Elevated WiFi feeder", "text": "Two stainless steel bowls."}),
    ("text_tile", {"size": "wide", "icon": "shield", "title": "Sealed container keeps food fresh",
                   "text": "Desiccant box on the 3L dual model. Dry food only."}),
    ("product_tile", {"size": "tall", "product": "2-in-1-smart-feeder", "eyebrow": "Dual bowl", "link_label": "View"}),
    ("text_tile", {"size": "small", "icon": "mic", "title": "2-way audio", "text": "Talk to your pet from the app."}),
    ("text_tile", {"size": "small", "icon": "bowl", "title": "Anti-jam design", "text": "For cats and small dogs."}),
    ("image_tile", {"size": "wide", "image": IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png",
                    "eyebrow": "Fountains", "title": "Quiet water, always fresh",
                    "text": "Quiet pumps. Every model comes apart for cleaning.", "link": "shopify://collections/water-fountains", "link_label": "Shop fountains"}),
    ("stat_tile", {"size": "small", "value": "3.2L", "label": "Stainless fountain", "text": "108 oz, LED light."}),
    ("stat_tile", {"size": "small", "value": "4-layer", "label": "Filter", "text": "On the stainless and steel-tray fountains."}),
    ("product_tile", {"size": "tall", "product": "water-fountain", "eyebrow": "Fountain", "link_label": "View"}),
    ("image_tile", {"size": "small", "image": IMG + "main-05.jpg", "eyebrow": "Fresh storage", "title": "Sealed container",
                    "text": "", "link": "shopify://products/2-in-1-smart-feeder", "link_label": ""})])
cmp_f = old["cmp_feeders"]; cmp_f["settings"]["color_scheme"] = "scheme-3"
S["cmp_feeders"] = cmp_f
S["steps"] = sec("pm2-steps", {"eyebrow": "How it works", "heading": "Set it up once. Feed on time, every time.",
                               "image": IMG + "Smart_Feeding.png", "color_scheme": "scheme-5",
                               "padding_top": 96, "padding_bottom": 96}, [
    ("step", {"icon": "bowl", "title": "Fill the container", "text": "Add dry food to the container. The anti-jam design keeps it flowing."}),
    ("step", {"icon": "wifi", "title": "Connect the app", "text": "Pair the feeder with your WiFi in a few taps."}),
    ("step", {"icon": "clock", "title": "Set the schedule", "text": "Pick meal times and portions. On the camera model, check in with 1080P live view."})])
S["video"] = old["video"]
S["two_pets"] = old["two_pets"]
cmp_w = old["cmp_fountains"]; cmp_w["settings"]["color_scheme"] = "scheme-3"
S["cmp_fountains"] = cmp_w
S["life"] = old["life"]; S["life"]["settings"]["color_scheme"] = "scheme-5"
S["faq"] = old["faq"]; S["faq"]["settings"].update(color_scheme="scheme-3", container_color_scheme="scheme-5")
S["cta"] = sec("pm2-cta-band", {"eyebrow": "Feeders + fountains", "heading": "Smarter feeding starts today.",
                                "text": "<p>Automatic feeders with app control, and quiet water fountains for cats and small dogs.</p>",
                                "button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders",
                                "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains",
                                "color_scheme": "scheme-1", "padding_top": 120, "padding_bottom": 120}, [
    ("chip", {"text": "Free U.S. shipping $50+"}), ("chip", {"text": "WiFi app control"}),
    ("chip", {"text": "Stainless steel bowls"}), ("chip", {"text": "Also on Amazon"})])
save("templates/index.json", {"sections": S, "order": list(S)})

# product page: spec chips under main, sticky add-to-cart
P = load("templates/product.json")
ps = P["sections"]
new = {"main": ps["main"],
       "specs": {"type": "pm2-spec-chips", "settings": {"heading": "Key specs", "color_scheme": "scheme-3", "padding_top": 8, "padding_bottom": 40}}}
for k in P["order"]:
    if k != "main":
        new[k] = ps[k]
new["sticky_atc"] = {"type": "pm2-sticky-atc", "settings": {"color_scheme": "scheme-3", "show_thumbnail": True, "hide_on_desktop": False}}
save("templates/product.json", {"sections": new, "order": list(new)})

# header group: global modern style (glass header, buttons, cards)
H = load("sections/header-group.json")
H["sections"]["pm2-global-style"] = {"type": "pm2-global-style", "settings": {
    "enable_glass_header": True, "glass_tint": "light", "glass_opacity": 70, "enable_buttons": True, "enable_cards": True,
    "enable_image_zoom": True, "enable_typography": True, "enable_eyebrow": True, "enable_focus": True,
    "enable_selection": True, "enable_smooth_scroll": True}}
if "pm2-global-style" not in H["order"]:
    H["order"].append("pm2-global-style")
save("sections/header-group.json", H)

# footer: newsletter back on (homepage newsletter section was replaced by the CTA band)
F = load("sections/footer-group.json")
F["sections"]["footer"]["settings"].update(newsletter_enable=True, color_scheme="scheme-2")
save("sections/footer-group.json", F)
print("homepage:", list(S))
print("product:", list(new))
