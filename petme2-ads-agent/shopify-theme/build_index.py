"""Builds templates/index.json for the 'PETME2 — Premium Minimal' theme.
Input: index-original.json (the live homepage). Output: index.json.
Changes: orange -> black/stone, true copy only, trust bar, two comparison charts,
false 'feeder scale' claim and 'Feeding Calculator' slide removed."""
import json
from pathlib import Path

HERE = Path(__file__).parent
BLACK, STONE, STONE2, GREY = "#111111", "#f6f5f3", "#efede9", "#6b6b6b"
ORANGES = {"#f3783a", "#ff7138", "#ef7a3b", "#ff6f35", "#b400ff"}

d = json.loads((HERE / "index-original.json").read_text())
S = d["sections"]

# 1. Every orange accent becomes black.
for sec in S.values():
    for k, v in sec.get("settings", {}).items():
        if isinstance(v, str) and v.lower() in ORANGES:
            sec["settings"][k] = BLACK

# 2. Hero
h = S["hero_banner_qeMbmk"]["settings"]
h.update(eyebrow="Automatic feeders & water fountains",
         primary_button_text="Shop feeders", primary_button_url="shopify://collections/feeders",
         secondary_button_text="Shop fountains", secondary_button_url="shopify://collections/water-fountains")

# 3. Category grid: real copy, lighter overlay, white buttons
c = S["category_image_grid_HqG6km"]
b = c["blocks"]
b["category_ME8heP"]["settings"].update(
    text="<p>Automatic feeders with app scheduling, two-bowl models for 2 pets, and a 1080P camera model.</p>",
    secondary_button_text="Compare", secondary_button_link="#compare-feeders")
b["category_bQDyYC"]["settings"].update(
    text="<p>Quiet water fountains from 2L to 3.2L, including a stainless steel model, for cats and dogs.</p>",
    secondary_button_text="Compare", secondary_button_link="#compare-fountains")
c["settings"].update(overlay_opacity=40, card_radius=0, primary_button_bg="#ffffff", primary_button_text=BLACK,
                     primary_button_hover_bg=BLACK, primary_button_hover_text="#ffffff")

# 4. Showcase: honest badges, add camera feeder + stainless fountain, stone background
p = S["product_showcase_slider_EERJYp"]
subs = {"slide_Jxq7cw": "Biggest capacity · 5L", "slide_dfFQGD": "Best seller",
        "slide_T8VK8h": "Most popular feeder", "slide_t6jCby": "For 2 cats · White"}
for k, v in subs.items():
    p["blocks"][k]["settings"]["subtitle"] = v
for bid, handle, sub in [("slide_pm2cam", "smart-feeder", "With 1080P HD camera"),
                         ("slide_pm2ss", "water-fountain", "Stainless steel · 3.2L")]:
    p["blocks"][bid] = {"type": "slide", "settings": dict(p["blocks"]["slide_Jxq7cw"]["settings"], product=handle, subtitle=sub)}
    p["block_order"].append(bid)
p["settings"].update(section_bg=STONE, subtitle_color=GREY, link_bg=STONE2, heading="Shop the range")

# 5. Product picks
pp = S["pet_product_picks_6TDweY"]["settings"]
pp.update(heading="Water Fountains", view_all_link="shopify://collections/water-fountains", feature_card_bg=STONE)

# 6. Tech slider: drop "Feeding Calculator" (no such feature), keep true slides
t = S["tech_slider_Kpet9N"]
t["settings"].update(heading="Made for everyday care", secondary_button_bg=STONE2, dot_color="#d9d6d0", image_radius=0)
t["blocks"]["slide_QwDdXY"]["settings"].update(
    eyebrow="Two pets", title="Two Bowls, One Routine",
    text="<p>Feed two cats or small dogs at the same time, with even portions in two stainless steel bowls.</p>",
    primary_button_text="Shop feeders", primary_button_link="shopify://collections/feeders")
t["blocks"]["slide_BwUzga"]["settings"].update(
    text="<p>A sealed container and desiccant box help keep dry food fresh between meals.</p>",
    primary_button_text="Shop feeders", primary_button_link="shopify://collections/feeders")
t["blocks"]["slide_7j7L7W"]["settings"].update(
    text="<p>Schedule meals and set portions from your phone with the app.</p>",
    primary_button_text="Shop feeders", primary_button_link="shopify://collections/feeders")

# 7. Feature banner: remove the false "scale" claim
f = S["product_feature_banner_GzmHVi"]
f["blocks"]["feature_VFGBPD"]["settings"].update(title="Stainless Steel Bowls",
                                                 text="<p>Food-safe steel bowls that wash easily</p>")
f["blocks"]["feature_GRnnYw"]["settings"].update(title="Smart App Control",
                                                 text="<p>Schedule meals and set portions from your phone</p>")
f["blocks"]["feature_CUkkmU"]["settings"].update(title="Easy to Clean",
                                                 text="<p>Bowls and food container come apart for washing</p>")
f["settings"].update(heading="Smart feeding,\nmade simple", card_bg=STONE, card_radius=0,
                     feature_primary_button_text="Shop feeders",
                     feature_primary_button_link="shopify://collections/feeders",
                     feature_secondary_button_text="Compare", feature_secondary_button_link="#compare-feeders",
                     feature_secondary_button_bg=STONE2)

# 8. Shop feed
S["shop_feed_slider_6BGeeA"]["settings"].update(image_radius=0)

# 9. New sections
S["pm2_trust"] = {"type": "petme2-trust-bar", "settings": {"bg": STONE, "fg": BLACK},
    "blocks": {
        "t1": {"type": "item", "settings": {"icon": "truck", "title": "Free U.S. shipping", "text": "On orders $50+"}},
        "t2": {"type": "item", "settings": {"icon": "lock", "title": "Secure checkout", "text": "Encrypted, safe payments"}},
        "t3": {"type": "item", "settings": {"icon": "drop", "title": "Easy to clean", "text": "Parts come apart for washing"}},
        "t4": {"type": "item", "settings": {"icon": "chat", "title": "Real support", "text": "Help from the PETME2 team"}}},
    "block_order": ["t1", "t2", "t3", "t4"]}

def model(handle, name, vals, badge=""):
    s = {"product": handle, "name": name, "badge": badge}
    s.update({f"v{i+1}": v for i, v in enumerate(vals)})
    return {"type": "model", "settings": s}

S["pm2_compare_feeders"] = {"type": "petme2-compare", "settings": {
    "anchor": "compare-feeders", "eyebrow": "Feeders", "heading": "Which feeder is right for you?",
    "text": "All PETME2 feeders work with dry food, run on a schedule from the app, and are for cats and small dogs.",
    "row1": "Capacity", "row2": "Bowls", "row3": "Control", "row4": "Camera", "row5": "Audio",
    "button_text": "View details", "bg": STONE},
    "blocks": {
        "m1": model("2-in-1-smart-feeder", "3L Dual Bowl", ["3L", "2 stainless steel", "App", "—", "2-way audio"], "Most popular"),
        "m2": model("2-in-1-feeder-1", "5L Elevated WiFi", ["5L", "2 stainless steel", "WiFi app", "—", "Voice recording"]),
        "m3": model("smart-feeder", "3L Camera Feeder", ["3L", "1 stainless steel", "WiFi app", "1080P HD, live view", "2-way audio"])},
    "block_order": ["m1", "m2", "m3"]}

S["pm2_compare_fountains"] = {"type": "petme2-compare", "settings": {
    "anchor": "compare-fountains", "eyebrow": "Water fountains", "heading": "Which fountain is right for you?",
    "text": "Every PETME2 fountain has a quiet pump and comes apart for easy cleaning.",
    "row1": "Capacity", "row2": "Material", "row3": "Filter", "row4": "Water level", "row5": "Best for",
    "button_text": "View details", "bg": "#ffffff"},
    "blocks": {
        "w1": model("water-fountain", "Stainless 3.2L", ["3.2L / 108oz", "Stainless steel", "4-layer filter", "LED light", "Big drinkers, cats & dogs"], "Premium"),
        "w2": model("water-fountain-4", "Steel Tray 2.2L", ["2.2L", "Plastic + steel tray", "4-layer filter", "Window + low-water light", "A steel drinking surface"]),
        "w3": model("water-fountain-2", "Transparent 2.2L", ["2.2L", "Clear plastic", "Filter cartridge", "See-through body", "Seeing water at a glance"]),
        "w4": model("water-fountain-simple", "Classic 2L", ["2L", "Plastic", "—", "Window + low-water light", "Small spaces"], "Best seller")},
    "block_order": ["w1", "w2", "w3", "w4"]}

d["order"] = ["hero_banner_qeMbmk", "pm2_trust", "category_image_grid_HqG6km", "product_showcase_slider_EERJYp",
              "pm2_compare_feeders", "pet_product_picks_6TDweY", "pm2_compare_fountains", "video_feature_banner_bnj3Ri",
              "logo_carousel_swiper_yCntaQ", "tech_slider_Kpet9N", "product_feature_banner_GzmHVi",
              "before_after_slider_T6gP38", "shop_feed_slider_6BGeeA"]

(HERE / "index.json").write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n")
left = [v for v in json.dumps(d).lower().split('"') if v in ORANGES]
print("sections:", len(d["order"]), "| orange left:", left)
