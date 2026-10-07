"""Builds the remaining page templates (collection, list-collections, cart, search, 404,
page, page.contact, password) for the PETME2 'Smart Tech' Dawn theme.
White base (scheme-3), one soft neutral (scheme-4 cloud), mint (scheme-5) only for trust bands;
the action blue is reserved for buttons.
Only true claims. Validate with: python3 validate_templates.py <dawn_dir>"""
import json
from pathlib import Path

HERE = Path(__file__).parent
FEEDERS, FOUNTAINS = "shopify://collections/feeders", "shopify://collections/water-fountains"


def w(name, obj):
    (HERE / "templates" / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def section(type_, settings=None, *items):
    s = {"type": type_}
    if settings is not None:
        s["settings"] = settings
    if items:
        s["blocks"] = {i: {"type": t, "settings": st} for i, t, st in items}
        s["block_order"] = [i for i, _, _ in items]
    return s


def template(*secs, **extra):
    t = dict(extra)
    t["sections"] = {k: v for k, v in secs}
    t["order"] = [k for k, _ in secs]
    return t


def rich_text(scheme, caption, heading, text, buttons=None, pad=(56, 56), size="h1"):
    items = []
    if caption:
        items.append(("caption", "caption", {"caption": caption, "text_style": "caption-with-letter-spacing",
                                             "text_size": "medium"}))
    items.append(("heading", "heading", {"heading": heading, "heading_size": size}))
    if text:
        items.append(("text", "text", {"text": text}))
    if buttons:
        (l1, u1), (l2, u2) = buttons
        items.append(("button", "button", {"button_label": l1, "button_link": u1, "button_style_secondary": False,
                                           "button_label_2": l2, "button_link_2": u2,
                                           "button_style_secondary_2": True}))
    return section("rich-text", {"desktop_content_position": "center", "content_alignment": "center",
                                 "color_scheme": scheme, "full_width": True,
                                 "padding_top": pad[0], "padding_bottom": pad[1]}, *items)


def featured(collection, title, scheme, n=4, pad=(56, 64)):
    return section("featured-collection", {
        "collection": collection, "products_to_show": n, "title": title, "heading_size": "h1",
        "description": "", "show_description": False, "description_style": "body", "columns_desktop": 4,
        "enable_desktop_slider": False, "full_width": False, "show_view_all": True, "view_all_style": "solid",
        "color_scheme": scheme, "image_ratio": "square", "image_shape": "default", "show_secondary_image": True,
        "show_vendor": False, "show_rating": False, "quick_add": "standard", "columns_mobile": "2",
        "swipe_on_mobile": True, "padding_top": pad[0], "padding_bottom": pad[1]})


def faq(scheme, container, heading, rows, caption="FAQ", pad=(64, 72)):
    return section("collapsible-content", {
        "caption": caption, "heading": heading, "heading_size": "h1", "heading_alignment": "center",
        "layout": "row", "container_color_scheme": container, "color_scheme": scheme,
        "open_first_collapsible_row": True, "image_ratio": "adapt", "desktop_layout": "image_second",
        "padding_top": pad[0], "padding_bottom": pad[1]},
        *[(f"row_{i + 1}", "collapsible_row", {"heading": q, "icon": icon, "row_content": a})
          for i, (q, a, icon) in enumerate(rows)])


Q_DRY = ("Do the feeders work with wet food?", "<p>No. PETME2 feeders are made for dry food (kibble).</p>", "serving_dish")
Q_TWO = ("Which feeder is best for 2 pets?", "<p>The 3L Dual Bowl or the 5L Elevated WiFi. Both split food into two "
         "stainless steel bowls.</p>", "paw_print")
Q_WIFI = ("Do I need WiFi?", "<p>WiFi is needed for the app: schedules and portions.</p>", "lightning_bolt")
Q_QUIET = ("Are the fountains loud?", "<p>No. Every PETME2 fountain uses a quiet pump made for use inside the "
           "home.</p>", "bottle")
Q_SHIP = ("How fast is shipping?", "<p>Shipping is free on every U.S. order. Orders are fulfilled by Amazon.</p>", "truck")
Q_BACK = ("What if my pet doesn't like it?", "<p>No worries. Every order comes with a 30-day money-back guarantee. "
          "If it's not a fit, contact us within 30 days and we'll give you your money back.</p>", "heart")
OFFER = "Free U.S. shipping · 30-day money-back guarantee"
Q_AMZ = ("Is PETME2 on Amazon?", "<p>Yes. All PETME2 products are also sold on Amazon, where you can read buyer "
         "reviews.</p>", "chat_bubble")

COMPARE = rich_text(
    "scheme-4", "NEED HELP CHOOSING?", "Compare models side by side",
    "<p>See capacity, bowls, camera and audio for every feeder, or capacity, material and filter for every "
    "fountain.</p>",
    (("Compare feeders", "/#compare-feeders"), ("Compare fountains", "/#compare-fountains")), pad=(56, 64))

# ---------- collection ----------
w("collection.json", template(
    ("banner", section("main-collection-banner", {"show_collection_description": True,
                                                  "show_collection_image": False, "color_scheme": "scheme-4"})),
    ("product-grid", section("main-collection-product-grid", {
        "products_per_page": 24, "columns_desktop": 3, "columns_mobile": "2", "color_scheme": "scheme-3",
        "image_ratio": "square", "image_shape": "default", "show_secondary_image": True, "show_vendor": False,
        "show_rating": False, "quick_add": "standard", "enable_filtering": True, "filter_type": "horizontal",
        "enable_sorting": True, "padding_top": 40, "padding_bottom": 64})),
    ("compare", COMPARE),
    ("faq", faq("scheme-3", "scheme-4", "Good to know", [Q_BACK, Q_SHIP, Q_DRY, Q_TWO, Q_WIFI, Q_QUIET], pad=(56, 64))),
))

# ---------- list-collections ----------
w("list-collections.json", template(
    ("main", section("main-list-collections", {"title": "Shop by category", "sort": "products_high",
                                               "image_ratio": "square", "columns_desktop": 3,
                                               "columns_mobile": "2"})),
    ("shipping", rich_text("scheme-5", "", OFFER,
                           "<p>Smart feeders and quiet water fountains for cats and small dogs.</p>",
                           (("Shop feeders", FEEDERS), ("Shop fountains", FOUNTAINS)), pad=(56, 64), size="h2")),
))

# ---------- cart ----------
w("cart.json", template(
    ("cart-items", section("main-cart-items", {"color_scheme": "scheme-3", "padding_top": 40, "padding_bottom": 24})),
    ("cart-footer", section("main-cart-footer", {"color_scheme": "scheme-3", "padding_top": 16, "padding_bottom": 56},
                            ("subtotal", "subtotal", {}), ("buttons", "buttons", {}))),
    ("shipping", rich_text("scheme-5", "", OFFER,
                           "<p>Not happy? Contact us within 30 days and we'll give you your money back.</p>",
                           pad=(32, 32), size="h2")),
    ("upsell", featured("water-fountains", "You may also like", "scheme-3", pad=(56, 72))),
))

# ---------- search ----------
w("search.json", template(
    ("main", section("main-search", {
        "columns_desktop": 4, "columns_mobile": "2", "image_ratio": "square", "image_shape": "default",
        "show_secondary_image": True, "show_vendor": False, "show_rating": False, "enable_filtering": True,
        "filter_type": "horizontal", "enable_sorting": True, "article_show_date": True,
        "article_show_author": False, "padding_top": 40, "padding_bottom": 56})),
    ("browse", rich_text("scheme-4", "BROWSE", "Not sure what to search for?",
                         "<p>Start with a category: app-controlled feeders or quiet water fountains.</p>",
                         (("Shop feeders", FEEDERS), ("Shop fountains", FOUNTAINS)), pad=(56, 56), size="h2")),
    ("feeders", featured("feeders", "Smart feeders", "scheme-3", n=3)),
))

# ---------- 404 ----------
w("404.json", template(
    ("main", section("main-404")),
    ("help", rich_text("scheme-4", "LOST?", "This page wandered off",
                       "<p>The link may be old or mistyped. Let's get you back to feeding time.</p>",
                       (("Shop feeders", FEEDERS), ("Shop fountains", FOUNTAINS)), pad=(56, 64))),
    ("feeders", featured("feeders", "Smart feeders", "scheme-3", n=3, pad=(64, 72))),
))

# ---------- page ----------
w("page.json", template(
    ("main", section("main-page", {"padding_top": 48, "padding_bottom": 56})),
    ("shop", rich_text("scheme-5", "", "Smart feeding. Fresh water.",
                       "<p>" + OFFER + "</p>",
                       (("Shop feeders", FEEDERS), ("Shop fountains", FOUNTAINS)), pad=(56, 64), size="h2")),
))

# ---------- page.contact ----------
w("page.contact.json", template(
    ("main", section("main-page", {"padding_top": 48, "padding_bottom": 16})),
    ("form", section("contact-form", {"heading": "Send us a message", "heading_size": "h2",
                                      "color_scheme": "scheme-3", "padding_top": 16, "padding_bottom": 64})),
    ("faq", faq("scheme-4", "scheme-3", "Quick answers", [Q_BACK, Q_SHIP, Q_DRY, Q_WIFI, Q_AMZ], caption="BEFORE YOU WRITE")),
))

# ---------- password ----------
w("password.json", template(
    ("main", section("email-signup-banner", {
        "show_background_image": False, "image_overlay_opacity": 0, "image_height": "medium",
        "desktop_content_position": "middle-center", "desktop_content_alignment": "center", "show_text_box": True,
        "color_scheme": "scheme-4", "mobile_content_alignment": "center", "show_text_below": True},
        ("heading", "heading", {"heading": "Smart feeding. Fresh water. Coming soon.", "heading_size": "h1"}),
        ("paragraph", "paragraph", {"text": "<p>Be the first to know when we launch. In the meantime, PETME2 "
                                            "products are also sold on Amazon.</p>", "text_style": "subtitle"}),
        ("email_form", "email_form", {}))),
    layout="password",
))
print("ok")
