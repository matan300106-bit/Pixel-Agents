"""V2 'friendly minimal' layout: runs after build.py. Rebuilds the homepage around the new pm2-* sections
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
# Friendly-minimal homepage: light, calm, one dark accent (the closing CTA). Schemes:
# 3 white, 5 warm cream, 4 soft sky, 1 soft night (CTA only). Backgrounds alternate so no two
# neighbouring bands share a tint (compare feeders + fountains read as one sky-blue chapter).
S = {}
S["hero"] = sec("pm2-hero", {
    "color_scheme": "scheme-5", "show_grid": False, "eyebrow_tag": "Hi!", "eyebrow": "For cats & small dogs",
    "heading_line_1": "Happy meals.", "heading_highlight": "Fresh water.",
    "subtext": "Smart feeders and quiet fountains that make pet care easy, even on busy days.",
    "button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders",
    "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains",
    "chip_1": "Free U.S. shipping $50+", "chip_2": "App control", "chip_3": "Quiet pumps",
    "product": "smart-feeder", "link_product": True, "image": IMG + "main-banner.jpg",
    "badge_1": "1080P live view", "badge_2": "2-way audio", "badge_3": "WiFi app",
    "padding_top": 56, "padding_bottom": 72})
S["ticker"] = sec("pm2-marquee", {"color_scheme": "scheme-3", "duration": 48, "size": "small",
                                   "show_divider": True, "show_borders": True, "reverse": False}, [
    ("item", {"text": "Free U.S. shipping on orders $50+", "icon": "truck"}),
    ("item", {"text": "Made for cats & small dogs", "icon": "paw"}),
    ("item", {"text": "Easy app control", "icon": "wifi"}),
    ("item", {"text": "Quiet fountain pumps", "icon": "drop"}),
    ("item", {"text": "Stainless steel bowls", "icon": "sparkle"}),
    ("item", {"text": "Also sold on Amazon", "icon": "sparkle"})])
S["shop"] = sec("pm2-product-tabs", {"eyebrow": "Shop", "heading": "Find their new favorite",
                                     "color_scheme": "scheme-3", "products_per_tab": 4, "show_view_all": True,
                                     "padding_top": 64, "padding_bottom": 64}, [
    ("tab", {"label": "Feeders", "collection": "feeders", "text": "Meals on time, set from your phone."}),
    ("tab", {"label": "Fountains", "collection": "water-fountains", "text": "Fresh, moving water with a quiet pump."})])
# Reserved slot: the feeder finder quiz (built by another agent). Only added when the section exists,
# so the template never references a missing section type.
if (HERE / "sections" / "pm2-quiz.liquid").exists():
    S["quiz"] = {"type": "pm2-quiz", "settings": {"color_scheme": "scheme-4"}}
S["bento"] = sec("pm2-bento", {"eyebrow": "Why pets (and people) like it", "heading": "Simple care, done for you.",
                               "subheading": "<p>Feeders and fountains that just work, so you can relax.</p>",
                               "color_scheme": "scheme-5", "padding_top": 72, "padding_bottom": 72}, [
    ("image_tile", {"size": "large", "image": IMG + "Your_pets_meals_managed_from_your_phone_3d0ac522-2f46-4a7b-a1d9-e2b48f76d5bb.jpg",
                    "eyebrow": "App control", "title": "Meals on time, from your phone",
                    "text": "Set meal times and portions in the app.", "link": "shopify://collections/feeders", "link_label": "Shop feeders"}),
    ("stat_tile", {"size": "small", "value": "1080P", "label": "Live view", "text": "See your pet on the 3L Camera feeder."}),
    ("text_tile", {"size": "small", "icon": "mic", "title": "Say hello", "text": "2-way audio lets you talk to your pet."}),
    ("text_tile", {"size": "wide", "icon": "bowl", "title": "Two bowls for two pets",
                   "text": "Our dual-bowl feeders fill two stainless steel bowls. Dry food only."}),
    ("image_tile", {"size": "wide", "image": IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png",
                    "eyebrow": "Fountains", "title": "Fresh water they'll love",
                    "text": "Quiet pumps. Every model comes apart for cleaning.", "link": "shopify://collections/water-fountains", "link_label": "Shop fountains"}),
    ("stat_tile", {"size": "small", "value": "3.2L", "label": "Stainless fountain", "text": "108 oz, with an LED light."}),
    ("text_tile", {"size": "small", "icon": "filter", "title": "4-layer filter", "text": "On the stainless and steel-tray fountains."})])
S["steps"] = sec("pm2-steps", {"eyebrow": "How it works", "heading": "Set up in minutes. Relax for months.",
                               "image": IMG + "Smart_Feeding.png", "color_scheme": "scheme-3",
                               "padding_top": 72, "padding_bottom": 72}, [
    ("step", {"icon": "bowl", "title": "Fill it up", "text": "Pour dry food into the container."}),
    ("step", {"icon": "wifi", "title": "Connect the app", "text": "Pair the feeder with your WiFi in a few taps."}),
    ("step", {"icon": "clock", "title": "Pick meal times", "text": "Choose times and portions. That's it."})])
cmp_f = old["cmp_feeders"]; cmp_f["settings"]["color_scheme"] = "scheme-4"
S["cmp_feeders"] = cmp_f
cmp_w = old["cmp_fountains"]; cmp_w["settings"]["color_scheme"] = "scheme-4"
S["cmp_fountains"] = cmp_w
# Lifestyle: video, two_pets and the collage are dropped; the bento already carries the lifestyle photos.
S["faq"] = old["faq"]
S["faq"]["settings"].update(color_scheme="scheme-3", container_color_scheme="scheme-5", caption="FAQ",
                            padding_top=72, padding_bottom=72)
S["cta"] = sec("pm2-cta-band", {"eyebrow": "Ready when you are", "heading": "Easy care starts here.",
                                "text": "<p>Smart feeders and quiet fountains for cats and small dogs.</p>",
                                "button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders",
                                "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains",
                                "color_scheme": "scheme-1", "padding_top": 88, "padding_bottom": 88}, [
    ("chip", {"text": "Free U.S. shipping $50+"}), ("chip", {"text": "Also on Amazon"})])
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

# header group: global friendly-minimal style (frosted header, pill buttons, 16px body on phones)
H = load("sections/header-group.json")
H["sections"]["pm2-global-style"] = {"type": "pm2-global-style", "settings": {
    "enable_glass_header": True, "glass_tint": "light", "glass_opacity": 80, "enable_buttons": True, "enable_cards": True,
    "enable_image_zoom": True, "enable_typography": True, "enable_eyebrow": True, "enable_focus": True,
    "enable_selection": True, "enable_smooth_scroll": True}}
if "pm2-global-style" not in H["order"]:
    H["order"].append("pm2-global-style")
save("sections/header-group.json", H)

# footer: newsletter back on (homepage newsletter section was replaced by the CTA band)
F = load("sections/footer-group.json")
F["sections"]["footer"]["settings"].update(newsletter_enable=True, color_scheme="scheme-5")
save("sections/footer-group.json", F)
print("homepage:", list(S))
print("product:", list(new))
