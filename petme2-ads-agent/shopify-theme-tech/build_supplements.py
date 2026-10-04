"""Supplements landing page: templates/collection.supplements.json (collection handle 'supplements', template suffix 'supplements').
Banner photo -> product grid -> 3 reasons -> 30-day guarantee -> FAQ. Claims stay at 'supports' level (pet supplement rules)."""
import json
from pathlib import Path

HERE = Path(__file__).parent
base = json.loads((HERE / "templates/collection.json").read_text())["sections"]

def blocks(items):
    b = {f"b{i}": {"type": t, "settings": s} for i, (t, s) in enumerate(items, 1)}
    return b, list(b)

S = {}
hb, ho = blocks([
    ("heading", {"heading": "Daily care in a tasty chew", "heading_size": "h1"}),
    ("text", {"text": "Soft chew supplements for cats and dogs. Free U.S. shipping + 30-day money-back guarantee.", "text_style": "body"}),
])
S["hero"] = {"type": "image-banner", "blocks": hb, "block_order": ho, "settings": {
    "image": "shopify://shop_images/petme2-supplements-banner.png", "image_overlay_opacity": 0, "image_height": "medium",
    "image_behavior": "none", "desktop_content_position": "middle-left", "desktop_content_alignment": "left",
    "show_text_box": False, "color_scheme": "scheme-1", "stack_images_on_mobile": False,
    "mobile_content_alignment": "left", "show_text_below": True}}
grid = base["product-grid"]
grid["settings"].update(columns_desktop=4, enable_filtering=False, products_per_page=24, padding_top=40, padding_bottom=48)
S["product-grid"] = grid
cb, co = blocks([
    ("column", {"title": "Tasty soft chews", "text": "<p>Chicken-flavored chews pets see as a treat. No pills, no mess.</p>"}),
    ("column", {"title": "Made for cats and dogs", "text": "<p>Skin & coat, cat grass digestion, hips & joints and tear stains. Pick what your pet needs.</p>"}),
    ("column", {"title": "Clear dosing", "text": "<p>Simple amounts by weight on every jar. Start with half and slowly increase.</p>"}),
])
S["why"] = {"type": "multicolumn", "blocks": cb, "block_order": co, "settings": {
    "title": "Why pet parents choose PETME2 chews", "heading_size": "h1", "image_width": "third", "image_ratio": "adapt",
    "button_label": "", "button_link": "", "columns_desktop": 3, "column_alignment": "left", "background_style": "primary",
    "color_scheme": "scheme-4", "columns_mobile": "1", "swipe_on_mobile": False, "padding_top": 48, "padding_bottom": 48}}
S["guarantee"] = {"type": "pm2-guarantee", "settings": {"style": "card", "icon": "shield", "color_scheme": "scheme-3", "padding_top": 36, "padding_bottom": 36}}
faq = [
    ("How many chews per day?", "<p>It depends on your pet's weight. The amount is on every jar and product page. Start with half and slowly increase over a few days.</p>"),
    ("When will I see a difference?", "<p>Supplements work best with steady daily use. Give them every day. Many pets need a few weeks.</p>"),
    ("Can I give more than one supplement?", "<p>Yes, our chews can be given together. If your pet takes medicine or has a health condition, ask your veterinarian first.</p>"),
    ("Is it safe for kittens, puppies, or pregnant pets?", "<p>Safe use in pregnant pets or pets used for breeding has not been proven. Ask your veterinarian before giving it to young, pregnant or nursing pets.</p>"),
    ("What if my pet doesn't like it?", "<p>No worries. Every order comes with a 30-day money-back guarantee. Contact us and we will make it right.</p>"),
    ("Is shipping free?", "<p>Yes. Shipping is free on every U.S. order.</p>"),
]
fb, fo = blocks([("collapsible_row", {"heading": q, "icon": "question_mark", "row_content": a}) for q, a in faq])
S["faq"] = {"type": "collapsible-content", "blocks": fb, "block_order": fo, "settings": dict(base["faq"]["settings"], heading="Supplement questions")}
(HERE / "templates/collection.supplements.json").write_text(json.dumps({"sections": S, "order": list(S)}, indent=2, ensure_ascii=False) + "\n")
print(list(S))

# product.supplement.json: the feeder/fountain product page minus the feeder-only sections
# (highlights + extras pick feeder or fountain copy from product.type, which is wrong for supplements).
P = json.loads((HERE / "templates/product.json").read_text())
keep = [k for k in P["order"] if k not in ("highlights", "extras")]
PS = {k: P["sections"][k] for k in keep}
PS["story"]["settings"].update(eyebrow="Why it works", heading="Good care, made simple", subheading="One small chew a day.")
(HERE / "templates/product.supplement.json").write_text(json.dumps({"sections": PS, "order": keep}, indent=2, ensure_ascii=False) + "\n")
print("product.supplement:", keep)
