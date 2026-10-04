"""Builds the 'PETME2 — Friendly Minimal / built to sell' design system for a fresh Dawn theme (white base,
one soft neutral, ONE action blue reserved for buy buttons, soft mint for trust; rounded Nunito headings,
big radii, airy spacing; mobile first).
Writes templates/index.json, templates/product.json, sections/header-group.json,
sections/footer-group.json and config/settings_data.json. Same photos as the old store,
everything else new. Only true claims (from research/seo facts)."""
import json
from pathlib import Path

HERE = Path(__file__).parent
IMG = "shopify://shop_images/"
# Sell palette (WCAG): white label on ACTION 5.48:1, INK on WHITE 15.2:1, INK on CLOUD 14.0:1, INK on MINT 13.6:1,
# ACTION on CLOUD 5.0:1, GREEN (checkmarks) on MINT 4.7:1 -> every button label / body text >= 4.5:1.
# ACTION is the one strong colour and is used for buy/add-to-cart buttons in every scheme.
INK, WHITE = "#1B2540", "#FFFFFF"
ACTION = "#2F5FE0"   # PETME2 blue, a touch deeper for punch + contrast
CLOUD = "#F4F6FA"    # the one soft neutral background
MINT = "#E9F6EF"     # subtle success tint for guarantee / shipping bands
GREEN = "#1E7B4F"    # checkmark colour (global style)
BLUE = ACTION
NAVY = INK  # used by the reviews app block colours below


def w(path, obj):
    (HERE / path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def blocks(*items):
    """items: (id, type, settings) -> blocks dict + order list"""
    return {i: {"type": t, "settings": s} for i, t, s in items}, [i for i, _, _ in items]


def section(type_, settings, *items):
    s = {"type": type_, "settings": settings}
    if items:
        s["blocks"], s["block_order"] = blocks(*items)
    return s


def model(handle, name, vals, badge=""):
    s = {"product": handle, "name": name, "badge": badge}
    s.update({f"v{i + 1}": v for i, v in enumerate(vals)})
    return s


# ---------- global settings ----------
def scheme(bg, text, button, label, secondary):
    return {"settings": {"background": bg, "background_gradient": "", "text": text, "button": button,
                         "button_label": label, "secondary_button_label": secondary, "shadow": "#000000"}}


current = {
    "logo": IMG + "01-08-Photoroom_1.png", "logo_width": 110, "favicon": IMG + "p2_1.png",
    "color_schemes": {
        "scheme-1": scheme(WHITE, INK, ACTION, WHITE, INK),       # white (Dawn's default scheme, kept safe)
        "scheme-2": scheme(ACTION, WHITE, WHITE, ACTION, WHITE),  # action blue (sale badge only)
        "scheme-3": scheme(WHITE, INK, ACTION, WHITE, INK),       # white (header, product info, most sections)
        "scheme-4": scheme(CLOUD, INK, ACTION, WHITE, INK),       # cloud: the one soft neutral (hero, quiz, compare, cards, footer)
        "scheme-5": scheme(MINT, INK, ACTION, WHITE, INK),        # mint: trust / guarantee / shipping bands
    },
    # Nunito (rounded, friendly) for headings + Nunito Sans for body; both verified in Shopify's font library.
    "type_header_font": "nunito_n8", "heading_scale": 110, "type_body_font": "nunito_sans_n4", "body_scale": 100,
    "page_width": 1300, "spacing_sections": 0, "spacing_grid_horizontal": 20, "spacing_grid_vertical": 24,
    "animations_reveal_on_scroll": True, "animations_hover_elements": "vertical-lift",
    "buttons_border_thickness": 1, "buttons_border_opacity": 100, "buttons_radius": 40,
    "buttons_shadow_opacity": 0, "buttons_shadow_horizontal_offset": 0, "buttons_shadow_vertical_offset": 0, "buttons_shadow_blur": 0,
    "variant_pills_border_thickness": 1, "variant_pills_border_opacity": 30, "variant_pills_radius": 40,
    "variant_pills_shadow_opacity": 0, "variant_pills_shadow_horizontal_offset": 0, "variant_pills_shadow_vertical_offset": 0, "variant_pills_shadow_blur": 0,
    "inputs_border_thickness": 1, "inputs_border_opacity": 25, "inputs_radius": 14,
    "inputs_shadow_opacity": 0, "inputs_shadow_horizontal_offset": 0, "inputs_shadow_vertical_offset": 0, "inputs_shadow_blur": 0,
    "card_style": "card", "card_image_padding": 12, "card_text_alignment": "left", "card_color_scheme": "scheme-4",
    "card_border_thickness": 0, "card_border_opacity": 0, "card_corner_radius": 24,
    "card_shadow_opacity": 0, "card_shadow_horizontal_offset": 0, "card_shadow_vertical_offset": 0, "card_shadow_blur": 0,
    "collection_card_style": "card", "collection_card_image_padding": 0, "collection_card_text_alignment": "left",
    "collection_card_color_scheme": "scheme-4", "collection_card_border_thickness": 0, "collection_card_border_opacity": 0,
    "collection_card_corner_radius": 24, "collection_card_shadow_opacity": 0,
    "collection_card_shadow_horizontal_offset": 0, "collection_card_shadow_vertical_offset": 0, "collection_card_shadow_blur": 0,
    "text_boxes_border_thickness": 0, "text_boxes_border_opacity": 0, "text_boxes_radius": 24,
    "text_boxes_shadow_opacity": 0, "text_boxes_shadow_horizontal_offset": 0, "text_boxes_shadow_vertical_offset": 0, "text_boxes_shadow_blur": 0,
    "media_border_thickness": 0, "media_border_opacity": 0, "media_radius": 24,
    "media_shadow_opacity": 0, "media_shadow_horizontal_offset": 0, "media_shadow_vertical_offset": 0, "media_shadow_blur": 0,
    "popup_border_thickness": 1, "popup_border_opacity": 10, "popup_corner_radius": 24,
    "popup_shadow_opacity": 10, "popup_shadow_horizontal_offset": 0, "popup_shadow_vertical_offset": 8, "popup_shadow_blur": 30,
    "drawer_border_thickness": 1, "drawer_border_opacity": 10,
    "drawer_shadow_opacity": 0, "drawer_shadow_horizontal_offset": 0, "drawer_shadow_vertical_offset": 0, "drawer_shadow_blur": 0,
    "badge_position": "top left", "badge_corner_radius": 40, "sale_badge_color_scheme": "scheme-2", "sold_out_badge_color_scheme": "scheme-4",
    "brand_headline": "Easy, happy care for cats and small dogs.",
    "brand_description": "<p>Smart feeders and quiet water fountains. Free U.S. shipping and a 30-day money-back guarantee on every order.</p>",
    "predictive_search_enabled": True, "predictive_search_show_vendor": False, "predictive_search_show_price": True,
    "currency_code_enabled": False,
    "cart_type": "drawer", "show_vendor": False, "show_cart_note": False, "cart_color_scheme": "scheme-3",
}
_live = json.loads((HERE.parent / "shopify-theme" / "settings_data.json").read_text())["current"]["blocks"]
current["blocks"] = {k: v for k, v in _live.items() if "ag-product-reviews" in v["type"]}  # keep reviews app embed on
w("config/settings_data.json", {"current": current})

# ---------- header / footer ----------
w("sections/header-group.json", {
    "name": "t:sections.header.name", "type": "header",
    "sections": {
        "announcement-bar": section("announcement-bar",
            {"color_scheme": "scheme-5", "show_line_separator": False, "show_social": False, "auto_rotate": True,
             "change_slides_speed": 5, "enable_country_selector": False, "enable_language_selector": False},
            ("a1", "announcement", {"text": "Free U.S. shipping on every order", "link": ""}),
            ("a2", "announcement", {"text": "30-day money-back guarantee", "link": ""}),
            ("a3", "announcement", {"text": "10% off your first order when you join our emails", "link": ""})),
        "header": section("header",
            {"color_scheme": "scheme-3", "menu_color_scheme": "scheme-3", "logo_position": "middle-left",
             "menu": "main-menu", "menu_type_desktop": "dropdown", "sticky_header_type": "always",
             "show_line_separator": True, "enable_country_selector": False, "enable_language_selector": False,
             "mobile_logo_position": "center", "margin_bottom": 0, "padding_top": 12, "padding_bottom": 12}),
    },
    "order": ["announcement-bar", "header"]})

w("sections/footer-group.json", {
    "name": "t:sections.footer.name", "type": "footer",
    "sections": {"footer": section("footer",
        {"color_scheme": "scheme-4", "newsletter_enable": True, "newsletter_heading": "Get 10% off your first order",
         "enable_follow_on_shop": True, "show_social": False, "enable_country_selector": False,
         "enable_language_selector": False, "payment_enable": True, "show_policy": True,
         "margin_top": 0, "padding_top": 56, "padding_bottom": 40},
        ("brand", "brand_information", {"show_social": False}),
        ("l1", "link_list", {"heading": "Products", "menu": "products"}),
        ("l2", "link_list", {"heading": "Quick links", "menu": "quick-links"}),
        ("l3", "link_list", {"heading": "Information", "menu": "information"}))},
    "order": ["footer"]})

# ---------- homepage ----------
S = {}
S["hero"] = section("image-banner",
    {"image": IMG + "main-banner.jpg", "image_2": "", "image_overlay_opacity": 50, "image_height": "large",
     "image_behavior": "none", "desktop_content_position": "middle-left", "desktop_content_alignment": "left",
     "show_text_box": False, "color_scheme": "scheme-1", "stack_images_on_mobile": False,
     "mobile_content_alignment": "left", "show_text_below": False},
    ("h", "heading", {"heading": "Smart feeding. Fresh water. Zero guesswork.", "heading_size": "h0"}),
    ("t", "text", {"text": "App-controlled feeders and quiet fountains for cats and small dogs.", "text_style": "subtitle"}),
    ("b", "buttons", {"button_label_1": "Shop feeders", "button_link_1": "shopify://collections/feeders", "button_style_secondary_1": False,
                      "button_label_2": "Shop fountains", "button_link_2": "shopify://collections/water-fountains", "button_style_secondary_2": True}))
S["specs"] = section("pm2-specs", {"color_scheme": "scheme-1"},
    ("s1", "spec", {"big": "1080P", "label": "HD camera feeder"}),
    ("s2", "spec", {"big": "5L", "label": "Largest feeder"}),
    ("s3", "spec", {"big": "2", "label": "Stainless steel bowls"}),
    ("s4", "spec", {"big": "3.2L", "label": "Stainless fountain"}))
S["categories"] = section("multicolumn",
    {"title": "Shop by category", "heading_size": "h1", "image_width": "full", "image_ratio": "square",
     "button_label": "", "button_link": "", "columns_desktop": 2, "column_alignment": "left",
     "background_style": "none", "color_scheme": "scheme-3", "columns_mobile": "1", "swipe_on_mobile": False,
     "padding_top": 72, "padding_bottom": 36},
    ("c1", "column", {"image": IMG + "homepage-feeder.png", "title": "Automatic feeders",
                      "text": "<p>App scheduling, two-bowl models for 2 pets, and a 1080P camera model.</p>",
                      "link_label": "Shop feeders", "link": "shopify://collections/feeders"}),
    ("c2", "column", {"image": IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png", "title": "Water fountains",
                      "text": "<p>Quiet fountains from 2L to 3.2L, including a stainless steel model.</p>",
                      "link_label": "Shop fountains", "link": "shopify://collections/water-fountains"}))
S["feeders"] = section("featured-collection",
    {"collection": "feeders", "products_to_show": 4, "title": "Smart feeders", "heading_size": "h1",
     "description": "", "show_description": False, "description_style": "body", "columns_desktop": 4,
     "enable_desktop_slider": False, "full_width": False, "show_view_all": True, "view_all_style": "solid",
     "color_scheme": "scheme-3", "image_ratio": "square", "image_shape": "default", "show_secondary_image": True,
     "show_vendor": False, "show_rating": False, "quick_add": "standard", "columns_mobile": "2",
     "swipe_on_mobile": True, "padding_top": 72, "padding_bottom": 72})
S["app"] = section("image-with-text",
    {"image": IMG + "Your_pets_meals_managed_from_your_phone_3d0ac522-2f46-4a7b-a1d9-e2b48f76d5bb.jpg",
     "height": "large", "desktop_image_width": "medium", "layout": "image_first", "image_behavior": "none",
     "content_layout": "no-overlap", "desktop_content_position": "middle", "desktop_content_alignment": "left",
     "mobile_content_alignment": "left", "section_color_scheme": "scheme-1", "color_scheme": "scheme-1",
     "padding_top": 72, "padding_bottom": 72},
    ("c", "caption", {"caption": "THE APP", "text_style": "caption-with-letter-spacing", "text_size": "medium"}),
    ("h", "heading", {"heading": "Meals on schedule. From anywhere.", "heading_size": "h1"}),
    ("t", "text", {"text": "<p>Set feeding times and portions from your phone. The camera model adds 1080P live view and 2-way audio, so you can see and talk to your pet when you're away.</p>", "text_style": "body"}),
    ("b", "button", {"button_label": "Shop feeders", "button_link": "shopify://collections/feeders", "button_style_secondary": False}))
S["video"] = section("video",
    {"heading": "See PETME2 in action", "heading_size": "h1", "enable_video_looping": True,
     "video": "shopify://files/videos/44d805d5a3a14767ba6d3e4964b89523.HD-1080p-7.2Mbps-54726534.mp4",
     "video_url": "", "cover_image": IMG + "Rectangle_34626129.jpg", "description": "PETME2 product video",
     "full_width": True, "color_scheme": "scheme-1", "padding_top": 72, "padding_bottom": 0})
S["cmp_feeders"] = section("pm2-compare",
    {"color_scheme": "scheme-3", "anchor": "compare-feeders", "eyebrow": "Compare feeders",
     "heading": "Which feeder fits your pet?",
     "text": "Every PETME2 feeder runs on a schedule from the app. Made for dry food, cats and small dogs.",
     "row1": "Capacity", "row2": "Bowls", "row3": "Control", "row4": "Camera", "row5": "Audio", "button_text": "View details"},
    ("m1", "model", model("2-in-1-smart-feeder", "3L Dual Bowl", ["3L", "2 stainless steel", "App", "—", "2-way audio"])),
    ("m2", "model", model("2-in-1-feeder-1", "5L Elevated WiFi", ["5L", "2 stainless steel", "WiFi app", "—", "Voice recording"])),
    ("m3", "model", model("smart-feeder", "3L Camera Feeder", ["3L", "1 stainless steel", "WiFi app", "1080P HD, live view", "2-way audio"])))
S["two_pets"] = section("image-with-text",
    {"image": IMG + "image_42_1.jpg", "height": "large", "desktop_image_width": "medium", "layout": "text_first",
     "image_behavior": "none", "content_layout": "no-overlap", "desktop_content_position": "middle",
     "desktop_content_alignment": "left", "mobile_content_alignment": "left", "section_color_scheme": "scheme-5",
     "color_scheme": "scheme-5", "padding_top": 72, "padding_bottom": 72},
    ("c", "caption", {"caption": "DUAL BOWL", "text_style": "caption-with-letter-spacing", "text_size": "medium"}),
    ("h", "heading", {"heading": "Two pets, one easy routine.", "heading_size": "h1"}),
    ("t", "text", {"text": "<p>Even portions in two stainless steel bowls, so both pets eat at the same time. A sealed container and desiccant box help keep dry food fresh.</p>", "text_style": "body"}),
    ("b", "button", {"button_label": "Shop dual feeders", "button_link": "shopify://products/2-in-1-smart-feeder", "button_style_secondary": False}))
S["fountains"] = section("featured-collection",
    dict(S["feeders"]["settings"], collection="water-fountains", title="Water fountains", color_scheme="scheme-3"))
S["water"] = section("image-with-text",
    {"image": IMG + "Homepage-Water-Fountains_79d73496-2084-410b-bd2e-dc1ea0e329a5.png", "height": "large",
     "desktop_image_width": "medium", "layout": "image_first", "image_behavior": "none", "content_layout": "no-overlap",
     "desktop_content_position": "middle", "desktop_content_alignment": "left", "mobile_content_alignment": "left",
     "section_color_scheme": "scheme-5", "color_scheme": "scheme-5", "padding_top": 72, "padding_bottom": 72},
    ("c", "caption", {"caption": "WATER FOUNTAINS", "text_style": "caption-with-letter-spacing", "text_size": "medium"}),
    ("h", "heading", {"heading": "Fresh, moving water. Quiet pump.", "heading_size": "h1"}),
    ("t", "text", {"text": "<p>Every PETME2 fountain has a quiet pump and comes apart for easy cleaning. Choose stainless steel, a steel drinking tray, or a see-through body.</p>", "text_style": "body"}),
    ("b", "button", {"button_label": "Shop fountains", "button_link": "shopify://collections/water-fountains", "button_style_secondary": False}))
S["cmp_fountains"] = section("pm2-compare",
    {"color_scheme": "scheme-3", "anchor": "compare-fountains", "eyebrow": "Compare fountains",
     "heading": "Which fountain fits your home?",
     "text": "Every PETME2 fountain has a quiet pump and comes apart for easy cleaning.",
     "row1": "Capacity", "row2": "Material", "row3": "Filter", "row4": "Water level", "row5": "Best for", "button_text": "View details"},
    ("w1", "model", model("water-fountain", "Stainless 3.2L", ["3.2L / 108oz", "Stainless steel", "4-layer filter", "LED light", "Big drinkers, cats & dogs"], "Premium")),
    ("w2", "model", model("water-fountain-4", "Steel Tray 2.2L", ["2.2L", "Plastic + steel tray", "4-layer filter", "Window + low-water light", "A steel drinking surface"])),
    ("w3", "model", model("water-fountain-2", "Transparent 2.2L", ["2.2L", "Clear plastic", "Filter cartridge", "See-through body", "Seeing water at a glance"])),
    ("w4", "model", model("water-fountain-simple", "Classic 2L", ["2L", "Plastic", "—", "Window + low-water light", "Small spaces"])))
S["life"] = section("collage",
    {"heading": "Life with PETME2", "heading_size": "h1", "desktop_layout": "left", "mobile_layout": "collage",
     "card_styles": "none", "color_scheme": "scheme-3", "padding_top": 72, "padding_bottom": 72},
    ("i1", "image", {"image": IMG + "Two_pets_One_easier_feeding_routine.jpg"}),
    ("i2", "image", {"image": IMG + "Rectangle_67_1.jpg"}),
    ("i3", "image", {"image": IMG + "image_830.jpg"}))
S["faq"] = section("collapsible-content",
    {"caption": "FAQ", "heading": "Good questions", "heading_size": "h1", "heading_alignment": "center",
     "layout": "none", "container_color_scheme": "scheme-3", "color_scheme": "scheme-5",
     "open_first_collapsible_row": True, "image_ratio": "adapt", "desktop_layout": "image_second",
     "padding_top": 72, "padding_bottom": 72},
    ("q1", "collapsible_row", {"heading": "What if my pet doesn't like it?", "icon": "check_mark", "row_content": "<p>No worries. Every order comes with a 30-day money-back guarantee. If it's not a fit, contact us within 30 days and we'll give you your money back.</p>"}),
    ("q2", "collapsible_row", {"heading": "How fast is shipping?", "icon": "check_mark", "row_content": "<p>Shipping is free on every U.S. order. Orders are fulfilled by Amazon.</p>"}),
    ("q3", "collapsible_row", {"heading": "Do the feeders work with wet food?", "icon": "check_mark", "row_content": "<p>No. PETME2 feeders are made for dry food (kibble).</p>"}),
    ("q4", "collapsible_row", {"heading": "Which feeder is best for 2 pets?", "icon": "check_mark", "row_content": "<p>The 3L Dual Bowl or the 5L Elevated WiFi. Both split food into two stainless steel bowls.</p>"}),
    ("q5", "collapsible_row", {"heading": "Do I need WiFi?", "icon": "check_mark", "row_content": "<p>WiFi is needed for the app: schedules and portions.</p>"}),
    ("q6", "collapsible_row", {"heading": "Are the fountains loud?", "icon": "check_mark", "row_content": "<p>No. Every PETME2 fountain uses a quiet pump made for use inside the home.</p>"}),
    ("q7", "collapsible_row", {"heading": "Are the fountains easy to clean?", "icon": "check_mark", "row_content": "<p>Yes. Every PETME2 fountain comes apart for cleaning.</p>"}))
S["newsletter"] = section("newsletter",
    {"color_scheme": "scheme-3", "full_width": True, "padding_top": 56, "padding_bottom": 64},
    ("h", "heading", {"heading": "Get new products and deals first", "heading_size": "h1"}),
    ("p", "paragraph", {"text": "<p>No spam. Just launches and member-only offers.</p>"}),
    ("f", "email_form", {}))
w("templates/index.json", {"sections": S, "order": list(S)})

# ---------- product page ----------
old = json.loads((HERE.parent / "shopify-theme" / "product.json").read_text())
extras = old["sections"]["pm2_extras"]["settings"]
extras["color_scheme"] = "scheme-4"
extras.update(
    dq5="What if my pet doesn't like it?",
    da5="Every order comes with a 30-day money-back guarantee. If it's not a fit, contact us within 30 days and we'll give you your money back.",
    fq5="What if my pet doesn't like it?",
    fa5="Every order comes with a 30-day money-back guarantee. If it's not a fit, contact us within 30 days and we'll give you your money back.",
    # Verifier: keep feature/FAQ copy to facts true for every model in the group.
    feeder_features="Scheduled meals :: Set meal times and portions in the app\nStainless steel bowls :: Easy to wipe clean\nMade for dry food :: For cats & small dogs\nFree U.S. shipping :: 30-day money-back guarantee",
    fountain_features="Quiet pump :: Made for use inside the home\nComes apart :: Easy to clean\nFresh, moving water :: For cats & small dogs\nFree U.S. shipping :: 30-day money-back guarantee",
    da3="WiFi is needed for the app: schedules and portions. Setup steps are in the manual.",
    da4="Take off the bowls and wash them. The manual has the full cleaning steps.",
    fa4="Yes. PETME2 fountains work for cats and small dogs. The Stainless 3.2L holds the most water.")
reviews_block = old["sections"]["1786715348a590fb22"]["blocks"]
for _b in reviews_block.values():
    _b["settings"].update(air_blockreviews_singleStarColor=BLUE, air_blockreviews_primaryColor=NAVY)
P = {
    "main": section("main-product",
        {"enable_sticky_info": True, "color_scheme": "scheme-3", "media_size": "large", "constrain_to_viewport": True,
         "media_fit": "contain", "gallery_layout": "thumbnail_slider", "mobile_thumbnails": "hide",
         "media_position": "left", "image_zoom": "lightbox", "hide_variants": False, "enable_video_looping": False,
         "padding_top": 20, "padding_bottom": 48},
        ("title", "title", {}),
        ("price", "price", {}),
        ("ship", "text", {"text": "Free U.S. shipping · 30-day money-back guarantee", "text_style": "subtitle"}),
        ("variant_picker", "variant_picker", {"picker_type": "button", "swatch_shape": "circle"}),
        ("quantity_selector", "quantity_selector", {}),
        ("buy_buttons", "buy_buttons", {"show_dynamic_checkout": True, "show_gift_card_recipient": False}),
        ("description", "description", {}),
        ("shipping", "collapsible_tab", {"heading": "Free shipping & 30-day guarantee", "icon": "truck",
            "content": "<p>Free U.S. shipping on every order. Orders are fulfilled by Amazon.</p>"
                       "<p>30-day money-back guarantee: if your pet doesn't like it, contact us within 30 days and we'll give you your money back.</p>"})),
    "extras": {"type": "pm2-product-extras", "settings": extras},
    "reviews": {"type": "apps", "settings": {"include_margins": True}, "blocks": reviews_block,
                "block_order": list(reviews_block)},
    "related-products": section("related-products",
        {"heading": "You may also like", "heading_size": "h2", "products_to_show": 4, "columns_desktop": 4,
         "columns_mobile": "2", "color_scheme": "scheme-3", "image_ratio": "square", "image_shape": "default",
         "show_secondary_image": True, "show_vendor": False, "show_rating": False, "padding_top": 56, "padding_bottom": 56}),
}
w("templates/product.json", {"sections": P, "order": list(P)})
print("built:", len(S), "homepage sections,", len(P), "product sections")
