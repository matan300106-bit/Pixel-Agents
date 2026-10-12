# Organic rank plan: 5 flat products (2026-10-12)

Strategy agent. Read only, so nothing was changed on Amazon. Exact text for every listing change is in `listing-drafts.json` (same folder).
Inputs: `keywords.md/json`, `competitors.md/json`, `research/seo/research-summary.md`, `research/seo/final/listings-final.json` (live copy), `research/seo/current-listings.json` (attributes), `inbox/2026-10-07` + `inbox/2026-10-11` ads and business reports, the V2 campaign file `outbox/2026-10-04-v2/all-campaigns-v2.json`, `reports/2026-10-12-*`, `changes-log.csv`, `products.yaml`, CLAUDE.md.

## The short story

- The Oct 4 copy is live on all 5. **The copy is not the main problem. Traffic is.** These 5 get 13–33 sessions a week. The stainless fountain gets 238.
- Their sales dropped after Oct 4, when their old ad campaigns were paused. Lower sales mean lower rank, and lower rank means fewer sales.
- **Today some of them have almost no working ad:**
  - **5L:** the phrase group bids $0.20, the competitor group bids $0.25, Auto was paused today, and the old 5L campaigns are still paused.
  - **Tray:** its own campaigns are paused, the shared groups bid $0.20–0.24, and Auto was paused today.
  - **Feeders | Exact** has a $20 budget but spends about $2 a day, because its bids are too low to win.
  - **Feeder targets in Competitors and Keyword Test** stop when those budgets run out. Stainless spends them first.
- **So the plan has 2 parts:**
  - (1) **Ads that bring sales on the exact keywords where we already rank on page 1–3.** This is the main lever.
  - (2) **Small listing edits.** They add the missing exact phrases, remove claims we cannot prove, and fix wrong attributes.
- **Rules kept:**
  - Ads stay on for all products. Nothing is paused.
  - Total budgets stay at or under $120 (now $105, $112 after this plan, at most $117 later).
  - Bids change at most ±20% a day.
  - Small fountain bids stay at $0.50 or less.
  - No new campaign: we add ad groups to campaigns that already exist.

## Order of work

| # | When | What | Who |
|---|---|---|---|
| 1 | **Mon Oct 12–Tue Oct 13, before any listing edit** | Helium 10 baseline: Cerebro for the fountains (with B0GHKRYV6W) and for the feeders, plus Keyword Tracker on the keywords in each "How we measure" section. The list is in `keywords.md` §6. Without it we cannot prove what worked. | Owner |
| 2 | **Oct 13** | **Ads first** (Section 4 of each product). Send it as one Chrome prompt. We are in supervised mode, so the owner approves it first. | Owner approves, Chrome applies |
| 3 | Oct 13–14 | Owner answers the fact questions (Section 3 of each product). Most can be answered from the box or the supplier sheet in 5 minutes. | Owner / supplier |
| 4 | **Oct 14, latest Oct 15** | Listing edits. Make **one edit per ASIN**, with title, bullets, description, search terms and attributes together, so Amazon re-indexes once. Use the confirmed variants when answers arrived; otherwise use the safe text. Order: camera (wrong attributes) → tray (wrong attributes, keyword stuffing) → transparent (unproven claims) → 5L → 2L (smallest change; its title only went live about Oct 5–11). | Owner in Seller Central |
| 5 | 24–48 h after each edit | Check that the new title shows and the listing is not suppressed. Search Amazon for 2–3 new exact phrases + "PETME2" to see if they are indexed. | Agent / owner |
| 6 | Thu Oct 15 | Normal ads check-in. Change bids by ±20% at most, following the rules in Section 4. | Guardian |
| 7 | **Before Tue Oct 20** | **The small-fountain sale price ends Oct 20**, and the price then jumps to $27.99. Extend $21.99 or set the planned $24.99 **before** that day, or the jump will break the velocity plan and the measurement. | Owner |
| 8 | Mon Oct 19, Mon Oct 26, Mon Nov 9 | Measure: Keyword Tracker export, business report and BSR. The 2-week and 4-week decisions are in Section 5. | Agent |

**Needs from owner (one line):** run the Helium 10 baseline · approve the Oct 13 ads prompt · answer the fact questions (battery backup on both feeders, WiFi band, camera box contents, 2L light = LED? 2L has no filter at all?, transparent filter layers + power, tray filter count) · approve a 5% camera coupon · fix the small-fountain price before Oct 20 · apply the listing edits in Seller Central.

## Budget after this plan (all campaigns, $/day)

| Campaign | Now | After | Why |
|---|---|---|---|
| Competitors \| ASIN | 30 | 30 | no change (stainless winner) |
| Keyword Test \| Phrase | 16 | 16 | no change |
| Fountains \| Exact | 12 | 12 | no change |
| Feeders \| Exact | 20 | 20 (→ 24 later) | new 5L + camera ad groups use the unused budget. +$4 (+20%) only if it spends ≥ 80% on 2 of 3 days |
| Brand \| Exact | 5 | 5 | |
| Veken | 10 | 10 | |
| 2L-Fountain-Brd-11 | 5 | 5 (→ 6 later) | +$1 when it has 2+ orders at a cost per order under $4.21 |
| 2L-Fountain-Brd-12 | 4 | 4 | |
| Transparent-Fountain-Brd-10 | 3 | 3 | |
| 5L-Feeder-Brd-6 (re-enable) | 0 (paused) | **4** | its keyword sold before (1 order from 4 clicks) |
| 2.2L-Steel-Tray-Broad-New-14 (re-enable) | 0 (paused) | **3** | the tray has no working ad today |
| Discovery \| Auto | paused by owner | paused | owner's decision; left as is |
| **Total** | **105** | **112 (max 117)** | cap 120 |

Real spend is lower than budgets (about $55–65 a day now), so the money at risk is the bids, not the budgets. Each new ad group has a stop-loss (see "Guardrails" at the end).

---

## 1. B0GHH8L59K: 5L WiFi elevated dual feeder ($54.99, profit about $10.23)

### 1. Diagnosis
BSR went from #436 (Oct 4) to #670 (Oct 12). Sessions fell from 51 to 25 a week and units from 3 to 1. Conversion fell from 5.9% to 4.0% after the price went from $45.99 to $54.99. It had 1 unit on Oct 12, plus 3 canceled orders. The old 5L campaigns (Brd-5 and Brd-6) gave 2 orders on Sep 30–Oct 6 and have been paused since Oct 4. **Today the 5L has almost no ad that wins:** phrase bids are $0.20, competitor bids $0.25 (22 impressions in 6 days), and Auto was paused. Organic: page 1–2 only on long tails ("elevated automatic cat feeder" #20, "cat feeder automatic for 2 cats" #40, "automatic cat feeder for 2 cats" #49). The head term "automatic cat feeder" is #268. Its edge is that no other unit is elevated + 2 bowls + WiFi. We cannot win on price ($5–12 above KATALICLAB and MRSDAYU).

### 2. Listing changes (exact text in JSON)
**Title** (189 → 189 chars; first 80: "PETME2 Elevated Automatic Cat Feeder for 2 Cats, 5L/20 Cups WiFi App Control, Do")
- OLD: `PETME2 Automatic Cat Feeder for 2 Cats, 5L Elevated Feeding Station with WiFi App and Voice Recording, Automatic Dog Feeder, Stainless Steel Dual Bowls, Timed Pet Food Dispenser, Dual Power`
- NEW: `PETME2 Elevated Automatic Cat Feeder for 2 Cats, 5L/20 Cups WiFi App Control, Double Bowl Cat Food Dispenser with Voice Recording, Stainless Steel Bowls, Automatic Dog Feeder for Small Dogs`
- Why:
  - One phrase now holds both "elevated automatic cat feeder" (#20, missing as a phrase) and "automatic cat feeder for 2 cats" (#49, kept word for word).
  - Adds "cat food dispenser" (23k SV) and "double" ("double cat feeder" sold in ads).
  - "5L/20 Cups" is a unit conversion (5L ≈ 21 cups).
  - Drops "Dual Power" (not confirmed) and "Timed Pet Food Dispenser" (SV 39).
  - "Elevated cat feeding station" stays exact in the bullet 4 header.
  - Words used twice: automatic, cat, feeder, for. Nothing more than twice.

**Bullets**
- **B1:** OLD "…a dual automatic cat feeder and double cat feeder in one." → NEW "…a dual automatic cat feeder and double cat feeder in one, made for multi-cat homes." This adds "multi" ("multi cat feeder" 882 SV, rank #133; the word is missing everywhere).
- **B3:** OLD "It is a recorded mealtime call, not live 2-way audio." → NEW "It is a one-way recorded message, not a live call." Writing "2-way audio" makes Amazon index a feature we do not have, which brings bad clicks.
- **B5:** OLD "DUAL POWER, EASY TO CLEAN: Run it on the power adapter, with backup batteries for outages (batteries not included)… a cat automatic feeder and dog automatic feeder in one." → NEW "EASY TO CLEAN: Runs on the included power adapter, so this self feeding cat food dispenser keeps meals on schedule. The stainless steel bowls wipe clean easily, and the bowls and food container detach for washing. One unit feeds 2 cats, or a cat and a small dog, at the same time."
  - Battery backup is not confirmed.
  - It also removes a keyword chain with no new words.
- **Description:**
  - Same "2-way audio" fix.
  - Remove the battery sentence until it is confirmed.
  - Remove "Made from food-grade materials" (not verified).

**Search terms** (179 bytes; no title or bullet words)
- OLD: `auto self double two timer schedule programmable smart large capacity kibble dry kitty kitten puppy multiple meal portion control raised tall backup battery remote electric comedero automatico gatos dispensador comida perros alimentador`
- NEW: `programmable multiple multicat kitty kitten puppy tall capacity remote electric autofeeder dispensor comedero automatico gatos alimentador dispensador comida perros mascotas perro`
- About 70 bytes are kept free for confirmed words ("battery", "2.4ghz").

**Attributes**
- `special_feature`: 5 long supplier sentences → "Elevated Feeding Station", "Dual Bowls, Even Split for 2 Pets", "WiFi App Scheduling", "Voice Recording Meal Call", "Anti-Jam Chute", "5L Large Capacity". "Elevated" and "anti-jam" are missing today.
- `included_components`: long sentences → short names (same 5 items).
- `material`: not set → "Plastic, Stainless Steel".
- `recommended_uses`: "Wet Food" and "Outdoor" are wrong for a dry-kibble indoor feeder. The owner kept them on Oct 4. **Suggest removing them, but only with the owner's OK.**

### 3. Confirm before use (drafted out of the text now)
1. Battery backup and battery type (a review says 4 × AA).
   - If yes, use the `new_if_confirmed` text for B5 and the description, and add ", Dual Power" back at the end of the title (196 chars).
2. WiFi band.
   - If 2.4GHz only, add "Connects to 2.4GHz WiFi only." to the end of B2.
3. Meals a day, portions and grams.
   - If known, add them to B2. Every winner shows these numbers.
4. Recording length in seconds.
   - If known, put it in B3.
5. Is the body plastic? This is for the `material` attribute.

### 4. Sales velocity (ads)
Bid cap is **$0.75** (ramp plan). Break-even CPC at 5% conversion is about $0.51, so every ad sale costs about $3–4 of profit. **That is the price of rank for a launch product**, and it is limited by the stop-loss.
- **New ad group "5L WiFi - Exact (rank)" in Feeders | Exact (SKU QO-7VBS-CVT4).** The campaign's budget is unused today.

| Keyword (exact) | Start bid | Why |
|---|---|---|
| elevated automatic cat feeder | $0.70 | rank #20, competition 963: the closest to top 10 |
| double cat feeder | $0.70 | the only 5L search term with an ad order |
| dual cat feeder automatic | $0.65 | #87, competition 741 |
| dual automatic cat feeder | $0.65 | #64, competition 759 |
| elevated cat feeding station | $0.60 | 2,101 SV, the feature phrase |
| pet feeding station with storage | $0.60 | old 5L ad sold on it |
| automatic cat feeder with app | $0.60 | #186, competition 495 |
| wifi automatic cat feeder | $0.60 | true feature |
| 5l automatic cat feeder | $0.50 | cheap and exact |

  - We do **not** add "automatic cat feeder for 2 cats" here. The 3L dual group already bids on it and converts at 10–13%, and two of our ads in one auction only split our own clicks. The 5L keeps that phrase through its title (#49).
- **New product-target ad group "5L WiFi - Competitor ASINs" in Feeders | Exact.** All start at $0.55 (cap $0.75):
  - B0C5X4N132 (oneisall 5L, 2 cats, $69.99, #3)
  - B09VGDGR4B (PETLIBRO 5L, 2 cats, $79.99)
  - B0GTXN5MJK (HoneyGuaridan 5L, $69.99)
  - B0D44QYZ7Z (PETLIBRO, $99.99)

  We are $15–45 cheaper and the only elevated unit. The old $0.25 group in Competitors stays as it is (we never pause).
- **Re-enable 5L-Feeder-Brd-6** ("pet feeding station with storage", broad). Budget $4, bid $0.60, down only, top of search +10%.
- **Note:** a new keyword starting at $0.60–0.70 is not a "bid change", but it is new spend. Guardian and the owner approve it in the same prompt.
- **Coupon: no, for now.** After the price rise the profit is $10.23, and a $2.75 (5%) coupon plus ad cost leaves almost nothing. Look at it again on Oct 26 if conversion stays under 5%.
- **Daily bid steps after day 3:**
  - A keyword with under 50 impressions in 3 days gets +15%, never above $0.75.
  - A keyword with spend ≥ $10 and 0 orders gets −30% (ramp stop-loss).

### 5. How we measure
- **Track:**
  - Our best long-tail ranks: "elevated automatic cat feeder" (#20), "cat feeder automatic for 2 cats" (#40), "automatic cat feeder for 2 cats" (#49), "dual automatic cat feeder" (#64), "automatic cat feeder 2 cats" (#64), "dual cat feeder automatic" (#87)
  - New phrases with no rank yet: "double cat feeder", "multi cat feeder" (#133), "cat food dispenser"
  - The head term: "automatic cat feeder" (#268)
- **2 weeks (Oct 26):**
  - "elevated automatic cat feeder" in the top 10 and 2 more phrases on page 1.
  - Sessions ≥ 40 a week and ≥ 3 units a week.
- **4 weeks (Nov 9):**
  - BSR back to #436 or better.
  - Ad cost per order ≤ $14.
- If not: lower the rank bids 20% and keep the listing.

---

## 2. B0GTCGYZDM: 3L camera feeder ($52.99, profit about $12.39)

### 1. Diagnosis
BSR barely moved (#931 Oct 4 → #909 today). Sessions were 13 a week with 0 units on Oct 4–10, then 2 units on Oct 12. Ads hardly serve:
- The main exact keyword "automatic cat feeder with camera" got 148 impressions in 6 days.
- All camera exact keywords together got 5 clicks ($4.14).
- Camera competitor targets got 19 impressions. They sit in Competitors, which runs out of budget around 6 PM because stainless spends it first.

Organic: the camera long tails are our closest to page 1: "cat food dispenser with camera" #86, "…with camera 1080p" #86, "wifi cat feeder with camera" #95, main term #121. They are missing as exact phrases. The listing also has a **wrong attribute**: `special_feature` holds dual-feeder text on a 1-bowl unit, and `included_components` lists only the main unit. Price is not the problem: we are the 2nd cheapest camera feeder among the winners ($7 under the $59.99 group).

### 2. Listing changes
**Title** (191 → 179 chars; first 80: "PETME2 Automatic Cat Feeder with Camera 1080P HD Video, 2-Way Audio, 3L WiFi Cat")
- OLD: `PETME2 Automatic Cat Feeder with Camera, 3L WiFi Cat Food Dispenser with 1080P HD Video and 2-Way Audio, App Control, Automatic Dog Feeder for Small Dogs, Timed Portions, Anti-Jam, Dual Power`
- NEW: `PETME2 Automatic Cat Feeder with Camera 1080P HD Video, 2-Way Audio, 3L WiFi Cat Food Dispenser with Camera App Control, Tap to Feed, Anti-Jam, Automatic Dog Feeder for Small Dogs`
- Why:
  - Adds the exact "automatic cat feeder with camera 1080p" and "cat food dispenser with camera" (both #86).
  - Mobile now shows 1080P + 2-Way Audio.
  - "Tap to Feed" is true and is the winners' hook.
  - Drops "Dual Power" (not confirmed) and "Timed Portions" (no SV).
  - Words used twice: automatic, cat, feeder, with, camera.

**Bullets**
- **B1:** OLD "A smart cat feeder and electric cat feeder in one compact unit, it makes a tidy cat feeding station in any corner." → NEW "It is a smart pet feeder with camera and a WiFi cat feeder with camera in one compact unit."
  - This puts back "pet feeder with camera" (#140). It was lost in the Oct 4 copy.
  - It adds "wifi cat feeder with camera" (#95).
  - It removes "feeding station", which fits a 1-bowl feeder badly.
- **B5:** OLD "DUAL POWER, EASY CLEAN: Runs on the power adapter and switches to backup batteries… It fits a small dog feeding station or pet feeding station too…" → NEW "DISHWASHER-SAFE BOWL: The stainless steel bowl is dishwasher safe, and the feeder plugs into a power adapter. It serves as a cat food feeder, dog food feeder and puppy feeder for small breeds. Like other cat and dog automatic feeders, it is a cat automatic feeder and dog automatic feeder in one."
- **Description:** remove the battery sentence until it is confirmed.

**Search terms** (146 bytes)
- OLD: `pet auto self monitor cam live view talk two schedule timer programmable smart electric kitty kitten puppy dry kibble meal feeding station backup battery remote phone comedero automatico gatos dispensador comida perros alimentador`
- NEW: `cam monitor webcam remote kitten doggie interactive streaming comedero automatico gatos camara alimentador dispensador comida perros mascotas gato`
- Changes: 20 words that were already in the bullets are removed. "camara" is added (Spanish searches) and "battery" is removed.

**Attributes**
- `special_feature`: OLD "Automatic Cat Feeder - Feed your cat or small dog at the same time with balanced portions" (wrong) → NEW "1080P HD Camera with Live View", "2-Way Audio", "WiFi App Scheduling and Portion Control", "Tap to Feed on Demand", "Anti-Jam Detect and Reverse", "Moisture Seals and Desiccant Box".
- `included_components`: OLD "Automatic Cat Feeder Main Unit - …" → NEW "Feeder main unit", "Stainless steel bowl", "Desiccant box". Add "Power adapter" and "User manual" once confirmed.
- `material`: not set → "Plastic, Stainless Steel".

### 3. Confirm before use
1. Battery backup and battery type.
   - If yes, use the `new_if_confirmed` B5 and description text.
2. WiFi band.
   - If 2.4GHz only, add "Connects to 2.4GHz WiFi only." to B3. This answers the top review complaint ("won't connect").
3. What is in the box (adapter, manual).
4. Meals a day and grams per portion.
5. **Night vision: our facts say NO.** Never add it, even though 6 of 8 competitors claim it.

### 4. Sales velocity
Bid cap is **$0.90**. Break-even CPC at 5.6% conversion is about $0.69, so we bid around $0.60–0.80.
- **Camera Feeder - Exact** (existing; not changed since Oct 7, so the 3-day rule is fine):
  - "automatic cat feeder with camera" +20% now, then +15% steps to $0.90 if impressions stay under 50 in 3 days.
  - "cat feeder with camera" gets the same steps.
- **Add exact keywords** to the same group:
  - "cat food dispenser with camera" $0.70
  - "automatic cat feeder with camera 1080p" $0.60
  - "wifi cat feeder with camera" $0.60
  - "cat feeder camera" $0.60
- **New product-target ad group "Camera - Competitor ASINs" in Feeders | Exact.** Bids $0.60, cap $0.90:
  - B0CNNNJ3FQ (Yuposl, 2L, $59.99, #4): our 3L is bigger and $7 cheaper.
  - B0FR4Z89KT (Faroro, $59.99)
  - B0GSR1GTHW (MUBBI, $59.99)
  - B0DCNNN5FC (Frienhund, $59.99)
  - B0B5ZGGWBQ (PETLIBRO, $125.99)

  We skip Minikey B0H7WS6PX9 (it is cheaper and has 2K).
- **Coupon: 5% ($2.65) for 14 days (Oct 14–28).** Profit allows it ($12.39 → about $9.70 before ads and the coupon fee). The camera feeder has the best margin of the five and 0% conversion last week. A coupon badge lifts click rate in search.
  - Write it as an experiment file first (CLAUDE.md §9).
  - Keep it if conversion goes ≥ 5% with no lower profit per day.

### 5. How we measure
- **Track:** "automatic cat feeder with camera" (#121), "cat feeder with camera" (#127), "cat food dispenser with camera" (#86), "automatic cat feeder with camera 1080p" (#86), "wifi cat feeder with camera" (#95), "automatic dog feeder with camera" (#102), "pet feeder with camera" (#140), "automatic cat feeder" (#271).
- **2 weeks:**
  - 3 camera long tails in the top 50 and the main term in the top 80.
  - Sessions ≥ 35 a week and ≥ 3 units a week.
- **4 weeks:**
  - Main term on page 1–2 (top 50).
  - BSR under #700.

---

## 3. B0GHKN9DBR: 2L plastic fountain, no filter ($21.99 sale, profit about $4.21)

### 1. Diagnosis
This was the biggest fall:
- BSR went from #726 to #1,611.
- Sessions fell from 131 to 33 a week, and units from 21 to 3.
- Conversion was still 9.1% (16% the week before), the best of the five.

The old campaigns 2L-Brd-11 ("water dispenser for cat") and 2L-Brd-12 ("water bowls for cats") gave **11 orders on Sep 30–Oct 6**. They were paused on Oct 4 because each sale lost money at $19.99 with about $1 clicks. They restarted on the night of Oct 11 at $0.50 ($5 and $4 a day). At $0.50 a click and about 13% conversion, an order costs about $3.80, which is under the $4.21 profit. **This is the one product where ads are profitable and also build rank.** Organic: "plastic cat water fountain" #29, "cat water fountain plastic" #31, "water fountains for cats indoor quiet" #52. This title only went live about Oct 5–11, so it has had the least time.

### 2. Listing changes (small: the first 80 chars stay the same)
**Title** (179 → 190 chars)
- OLD: `PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Light Low Level Alert, Visible Window, Anti-Dry Pump Shut-Off, Small Pet Dispenser for Kitten and Dog`
- NEW: `PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Light Low Level Alert, Visible Window, Anti-Dry Pump Shut-Off, Compact Plastic Design for Kittens and Small Dogs`
- Why:
  - Only the weak tail changes. "Small Pet Dispenser for Kitten and Dog" has no SV.
  - The new words support "compact cat water fountain" (#83) and "plastic cat water fountain" (#29), plus kittens and small dogs.
  - "water" is already used twice, so the tail cannot hold "cat water dispenser". That phrase stays in the bullets.

**Bullets**
- **B4:** OLD "…a small cat water fountain and kitty water fountain that is light and easy to move, …" → NEW "…a small cat water fountain and kitty water fountain with a slim plug-in design, …"
  - Ads show about 10 clicks from cordless/wireless searches, so we stop hinting that it is cordless.
- **Description:** "slim, portable white body" → "slim white body".

**Search terms** (123 bytes)
- OLD: `plastic kitty drinking waterer bowl automatic auto flowing running circulating fresh inside easy clean mini compact portable slim white refill indicator hydration drinker bedroom bebedero gatos fuente agua perros dispensador animal`
- NEW: `dish mini size breed puppy drinker hydration silent pets bebedero gatos fuente agua perros dispensador fonte gato bebedouro`
- Changes:
  - The 18 words already in the bullets are removed, and so is "portable".
  - Added: "dish" (cat water dish 2.4k), "size" and "breed" (near-page-1 small-dog phrases), "puppy", and "fonte" (a Portuguese search gave 1 ad order).

**Attributes**
- `special_feature[0]`: "2L Portable Water Capacity…" → "2L Compact Water Capacity - Slim size for small spaces".
- Optional: give it its own `model_name`. "WaterFountain14" is shared with the tray fountain.

### 3. Confirm before use
1. **Is the red light an LED?**
   - If yes, the title says "LED Low Level Indicator" (in the JSON).
   - Target phrase: "cat water fountain with led indicator", 1,246 SV, our rank #112, competition 786.
2. **Does it have no filter and no filter slot at all?**
   - If yes, the title adds "Filterless" (in the JSON), the search terms get "filterless nofilter", and B5 adds "No filter to buy: rinse and refill weekly."
   - That opens "filterless cat water fountain" (11,089 SV, competition 934), **the biggest new niche of the five**.
3. Measured noise in dB. If known, add it to B4.
4. Is it 2L, or 2.2L like the tray fountain? They share a model name.

### 4. Sales velocity
Bid cap is **$0.50** (owner).
- **In 2L-Fountain-Brd-11, add exact keywords** (single product, so the effect on rank is clear):

| Keyword (exact) | Bid | Why |
|---|---|---|
| cat water dispenser | $0.50 | sold in ads (3 clicks, 1 order), 17.5k SV |
| cat water bowl | $0.45 | sold (14 clicks, 1 order), 27k SV |
| small cat water fountain | $0.45 | sold (1 click, 1 order), #128 |
| plastic cat water fountain | $0.40 | our #29: a cheap push to the top 10 |
| white cat water fountain | $0.40 | sold (1 click, 1 order) |
| water bowls for cats | $0.45 | the Brd-12 keyword that sold 5 orders, as exact |

- **Budget:** Brd-11 goes from $5 to $6 once it has 2+ orders at a cost per order under $4.21. Brd-12 stays at $4. Do not raise both in the same week.
- **No competitor ASIN targets for the 2L.** Product-page clicks convert at 2.6% for us, and at $0.50 we lose the auction anyway. (Correction to the competitor report: the 2 Veken C1 orders on Sep 30–Oct 6 were $39.99 stainless sales, not 2L sales.)
- **No coupon:** the profit is $4.21. The $21.99 sale price already shows a deal against $27.99.
- **Price:** extend the sale or set $24.99 **before Oct 20**. The 2L sold 21 units a week with ads at $19.99. At $24.99 the profit per sale goes up a lot and ads can scale.

### 5. How we measure
- **Track:**
  - Ranks to protect: "plastic cat water fountain" (#29), "cat water fountain plastic" (#31), "water fountains for cats indoor quiet" (#52)
  - Phrases to push: "compact cat water fountain" (#83), "small cat water fountain" (#128), "cat water fountain white" (#132), "cat water dispenser" (#254), "water fountains for cats indoor" (#236), "cat water bowl" (not ranked)
  - Only if the LED / no-filter answers are yes: "cat water fountain with led indicator", "filterless cat water fountain"
- **2 weeks:**
  - "plastic cat water fountain" in the top 10.
  - Sessions ≥ 80 a week and ≥ 8 units a week.
  - Ad cost per order ≤ $4.21.
- **4 weeks:** BSR under #900.

---

## 4. B0GHLBGCP3: 2.2L transparent fountain with filter ($21.99 sale, profit about $4.07)

### 1. Diagnosis
- BSR went from #1,433 to #2,185.
- Sessions fell from 110 to 26 a week and units from 3 to 1.
- **Conversion is the weakest of the five (2.7–3.9%) in both weeks**, so the listing leaks buyers too.
- Old ads: Brd-10 got 1 order from 25 clicks, and Brd-New-15 got 2 orders from 43 clicks. Only Brd-10 is back on ($3).

The live copy carries 2 claims the Oct 4 draft said to confirm first:
- "**4-Layer**": the old description said "Multi Layer".
- "**USB powered**": the attribute says AC100-240V / DC5V.

"Transparent" takes the best title slot, but only 89 people a month search "clear" or "transparent". Near page 1: "dog water fountain small size dog" #87, "dog water fountain for small dogs" #110, "dog water bowl fountain small breed" #111 (it needs only the words "size" and "breed"), and "capsule water fountain for cats" #14 without the word "capsule".

### 2. Listing changes
**Title** (192 → 177 chars; first 80: "PETME2 Transparent Cat Water Fountain 74oz/2.2L, Filtered Cat Water Dispenser wi")
- OLD: `PETME2 Transparent Cat Water Fountain 74oz/2.2L, 4-Layer Filtered Cat Water Dispenser with Quiet Pump, Clear Tank Shows Level, Anti-Dry Protection, Automatic Pet Fountain for Small Dogs Indoor`
- NEW: `PETME2 Transparent Cat Water Fountain 74oz/2.2L, Filtered Cat Water Dispenser with Quiet Pump, Anti-Dry Protection, Filter Cartridge Included, Dog Fountain for Small Dogs Indoor`
- If 4 layers are confirmed: the same title with "4-Layer Filtered…" (185 chars).
- Why:
  - Removes the unproven "4-Layer".
  - Swaps "Clear Tank Shows Level" (it repeats "Transparent" and has no SV) for the true "Filter Cartridge Included", which buyers who want filters included look for.
  - Swaps "Automatic Pet Fountain" (SV 36) for "Dog Fountain" (4.7k SV).
  - The first 47 chars stay the same.

**Bullets**
- **B2:** OLD "4-LAYER FILTERED WATER: The built-in 4-layer filter cartridge…" → NEW "FILTERED WATER, FILTER INCLUDED: The built-in multi-layer filter cartridge…". The rest stays.
- **B5:** OLD "USB powered with no batteries needed." → NEW "It plugs in with the included power cable (not cordless), and no batteries are needed." This also answers the "not wireless" review.
- **Description:** "4-layer" → "multi-layer", and "USB powered" → "plugs in with the included power cable".

**Search terms** (135 bytes)
- OLD: `see through plastic filtration kitty kitten waterer drinking bowl flowing running circulating auto easy clean dish hydration inside multi drinker bedroom fresh bebedero gatos fuente agua perros dispensador animal system`
- NEW: `through size breed puppy hydration drinker pets auto multi bebedero gatos fuente agua perros dispensador transparente filtro gato fonte`
- Add "capsule" only if the body is capsule-shaped.

**Attributes**
- `special_feature`: the old values contain hidden U+2028 line-break characters. Clean them → "Transparent Body Shows Water Level", "Filter Cartridge Included", "Quiet Pump", "Anti-Dry Protection", "Easy Disassembly".
- `dog_breed_size`: "extra_small" → "extra_small, small". The copy says small dogs.

### 3. Confirm before use
1. 4 filter layers? If yes, use the 4-Layer title and keep the live B2.
2. Power: is it USB to a plug, and is the adapter in the box?
3. Is the body capsule-shaped? Look at the main image.
4. Does it have a low-water light?
5. Noise in dB.
6. Is there a replacement filter pack we can name? This is the top review complaint.

### 4. Sales velocity
Bid cap is $0.50. At 3–4% conversion, an ad sale costs $12–16 against $4.07 profit, so **keep spend small until conversion is ≥ 6%** after the listing fix.
- **Transparent-Fountain-Brd-10 ($3)** stays on. Add exact keywords:
  - "automatic water dispenser for cats" $0.45 (sold 1 from 1 click)
  - "dog water fountain for small dogs" $0.40 (#110)
  - "cat water fountain with filter" $0.40 (true here; the 2L has no filter)
- **Negative phrase on the transparent and tray ad groups:** "no filter", "filterless", "without filter", "cordless", "wireless", "battery".
  - About 6 clicks went to "no filter" searches on a filter fountain.
  - The 2L must NOT get "filterless" negatives.
- No coupon (profit $4.07).

### 5. How we measure
- **Track:** "dog water fountain small size dog" (#87), "plastic cat water fountain" (#92), "dog water fountain for small dogs" (#110), "dog water bowl fountain small breed" (#111), "automatic water dispenser for cats" (#249), "cat water dispenser" (#266), "cat water fountain with filter", and "capsule water fountain for cats" (#14, if the capsule shape is confirmed).
- **2 weeks:**
  - The "size" and "breed" phrases in the top 50.
  - **Conversion ≥ 6%** (the main goal here).
- **4 weeks:**
  - BSR under #1,500.
  - If conversion is still under 5%, the next fix is images (see-through level side by side, filter in the box). Not more keywords.

---

## 5. B0GHKRYV6W: 2.2L fountain with stainless steel tray + filter ($21.99 sale, profit about $4.66)

### 1. Diagnosis
- BSR went from #1,327 to #2,431.
- Sessions fell from 80 to 14 a week and units from 3 to 1. Conversion was 3.8% → 7.1%.
- **There is no working ad today:**
  - Its own campaigns (Tray-Phr-13 and Broad-14) are paused.
  - The shared groups bid $0.20–0.24, and their exact keywords show "Paused".
  - Auto was paused today.
- **The only search that ever sold it in ads is "quiet cat water fountain".** That phrase is not in the listing as a phrase.

Listing problems:
- `included_components` holds feature text copied from the 2L, including a "Red Light Alert" this model may not have.
- The title says "Filters Included" with no count.
- Bullet 1 has keyword stuffing ("stainless steel tray and all"). It pulls all-steel shoppers: about 10 stainless clicks, 0 orders.

There is no organic rank data at all (it was never in a Cerebro run).

### 2. Listing changes
**Title** (170 → 183 chars; first 80: "PETME2 Quiet Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Pet Water F")
- OLD: `PETME2 Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Automatic Pet Fountain for Cats and Dogs, 4-Layer Filtration, Filters Included, Low Water Alert, Quiet Pump`
- NEW: `PETME2 Quiet Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Pet Water Fountain for Cats and Dogs, 4-Layer Filtration, Filter Included, Low Level Alert, Anti-Dry Pump Shut-Off`
- With the filter count: "…4-Layer Filtration, [N] Filters Included, …" (188 chars).
- Why:
  - The exact converting phrase goes first.
  - "Pet water fountain" (42k) replaces "Automatic Pet Fountain" (SV 36).
  - "Low Level Alert" keeps "water" at 2.
  - "Anti-Dry Pump Shut-Off" fills the free space with a true safety feature.
  - "4-Layer" stays: it was consistent in the supplier's original title and bullets (fur, debris, odors).

**Bullets**
- **B1:** OLD "It is a cat water fountain, stainless steel tray included, and a cat fountain, stainless steel tray and all, that cats and small dogs can share." → NEW "Cats and small dogs can share it. Only the drinking tray is stainless steel, so you know what you get."
- **B2:** "FILTERS INCLUDED" / "Filters come in the box" → "FILTER INCLUDED" / "A filter comes in the box". If the count is confirmed, use "[N] FILTERS INCLUDED".
- **Description:**
  - Remove "made from food-grade materials" (not verified).
  - Remove "For dogs, it is a dog water fountain, stainless steel tray included."

**Search terms** (127 bytes)
- OLD: `plastic metal dish bowl kitty kitten waterer drinking flowing running circulating auto easy clean small inside indoor level window refill shutoff dispenser hydration bebedero gatos fuente agua perros acero inoxidable filtered animal`
- NEW: `dish size breed puppy hydration drinker silent medium auto bebedero gatos fuente agua perros acero inoxidable fonte filtro gato`
- "metal" is removed: it is risky for a plastic body.

**Attributes**
- `included_components`: OLD feature sentences → NEW "Fountain main unit", "Stainless steel drinking tray", "Filter cartridge", "Power cable". Add the manual, the reservoir and the filter count when confirmed.
- `special_feature`: "Stainless Steel Tray Design" → "Stainless Steel Drinking Tray", "4-Layer Filtration", "Low Water Alert", "Anti-Dry Pump Shut-Off", "Visible Water Level Window".
- `material`: "Stainless Steel, Plastic" → "Plastic, Stainless Steel". The body is plastic, so it goes first.
- Optional: give it its own `model_name`.

### 3. Confirm before use
1. **How many filters are in the box?** This is the competitor hook ("3 Filters").
2. Is the low-water alert an LED light? If yes, use "LED Low Level Alert".
3. Is the plastic BPA-free or food-grade? Only then say it.
4. The full box list.
5. Noise in dB.

### 4. Sales velocity
Bid cap is $0.50.
- **Re-enable 2.2L-Steel-Tray-Broad-New-14** at $3/day, down only, top of search +10%.
  - Set the broad "cat water fountain with led indicator" to the $0.50 cap if it is above it (it had 39 clicks and 1 order), then −20% steps toward $0.35.
  - We keep its keyword. The owner's rule is never pause.
- **Add exact keywords:**
  - "quiet cat water fountain" $0.50 (the only order)
  - "cat water fountain with filter" $0.40
  - "kitten water fountain" $0.40 (competition 1,000)
  - "small cat water fountain" $0.40
- **Negative phrase:** "stainless steel cat water fountain", "cat water fountain stainless steel", "metal", plus the filter and cordless negatives above.
  - These go on the tray only. The 2L actually sold 2 units on "cat water fountain stainless steel", so do not add them there.
- No coupon (profit $4.66).

### 5. How we measure
- **Track (first data ever):** "quiet cat water fountain", "cat water fountain with filter", "pet water fountain", "kitten water fountain", "small cat water fountain", "cat water dispenser", "automatic water dispenser for cats", "cat water fountain" (head term).
- **2 weeks:**
  - It has a rank on "quiet cat water fountain" (top 100).
  - Sessions ≥ 35 a week and ≥ 3 units a week.
- **4 weeks:**
  - "Quiet cat water fountain" in the top 40.
  - BSR under #1,500.

---

## Guardrails for all 5 (Guardian checks them daily)

- **Stop-loss, from the ramp plan:**
  - A keyword or target with spend ≥ 1 × profit and 0 orders gets −30%. Profit: 5L $10, camera $12, small fountains $4.
  - A second hit gets −30% again.
  - We do **not** pause (owner rule). A search term with spend ≥ 1.5 × profit and 0 orders becomes a negative exact.
- **Rank-investment limit per week:**
  - 5L: ad loss up to $35.
  - Camera: up to $25.
  - Transparent and tray: up to $10 each.
  - 2L: must be ≥ break-even.
  - If a product goes over its limit, cut its rank bids 20% and keep the listing changes.
- **Do not judge too early:**
  - Listing edits need 2–4 weeks to show in rank.
  - Ad changes need 3 days (attribution lag).
  - Ads and listing edits start in the same week, so we read the effect **per keyword**. Phrases added only to the listing show the listing effect; keywords we advertise show the sales effect.
- **Free extra measure:** if Brand Analytics is open for PETME2, export the Search Query Performance report per ASIN every Monday. It shows our share of impressions, clicks and purchases for each query.
- **Not in this plan, but it hurts trust:**
  - The list prices of $99.99 / $89.99 / $65.99 are 1.7–3 × the sale price. Set realistic list prices (pricing decision).
  - Image fixes (the 5L's gray legs, the transparent's see-through level) come after this plan, if conversion stays low.

## Guardian check (2026-10-12): PASS WITH FIXES, all applied
1. Camera: "Tap to Feed" removed from title and special_feature until confirmed. New title in JSON.
2. 5L: "20 Cups" removed (5L ≈ 21.1 cups, not a stated fact). New title in JSON.
3. Tray: "Power cable" moved to needs_confirmation; "medium" removed from backend.
4. Oct 13 ads prompt must first set Sites = Amazon only on Feeders | Exact, 5L-Feeder-Brd-6, 2.2L-Steel-Tray-Broad-New-14, 2L-Brd-11, Transparent-Brd-10.
5. 3-day rule: new exact keywords for 2L-Brd-11 and Transparent-Brd-10 go in at the Thu Oct 15 check-in, not Oct 13.
6. Camera 5% coupon moved to Oct 26.
7. 2L: whole listing edit moved to Oct 26.
8. No model_name changes this round.
Hard gate: the Helium 10 baseline must be in before the Oct 13 ads prompt goes out.
