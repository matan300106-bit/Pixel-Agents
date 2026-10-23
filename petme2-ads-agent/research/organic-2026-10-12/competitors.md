# Competitor study: 5 products with flat Best Sellers Rank (2026-10-12)

Competitor agent. Read only, so nothing was changed on Amazon. I used competitor text only to understand how their listings are built. Do not copy it.

## Sources and caveats

- **Live data (SP-API, pulled 2026-10-12):** catalog items (title, bullets, attributes, BSR, image count) and item offers (New condition: Buy Box price, list price, offer count, Prime) for 52 ASINs, plus 11 catalog keyword searches to find who ranks today. Raw table: `competitors.json` in this folder.
- **Earlier research:** `research/competitors-2026-10-04.md`, `research/seo/competitors-summary.md` and `competitors-listings.json`, `research/pricing-analysis-2026-10-04.txt`, `research/reviews-analysis-2026-10-04.md`, `research/reviews-negative-topics.txt`, plus the verified facts list in `research/seo/images-aplus.json` (`true_facts` and `audit_current_images`) and `products.yaml`.
- **Cerebro:** the files `cerebro-competitors-A.csv` (a PETLIBRO Dockstream fountain) and `-B.csv` (a PETLIBRO feeder) are single-ASIN exports. They have no per-ASIN rank columns, only an Organic 0/1 flag, so I used them only to cross-check search volume and whether the competitor ranks. The per-ASIN organic ranks come from `cerebro-feeders-B0GHLSQMJ9.csv` and `cerebro-fountains-B0DR7FCLZR.csv`:
  - Feeder file columns: our B0GTCGYZDM and B0GHH8L59K, and competitors PETLIBRO B09S8WMJY9, PETLIBRO B0B5ZGGWBQ / B0953SDCRG, oneisall B0C5X2G933 and Frienhund B0DCNNN5FC.
  - Fountain file columns: our B0GHKN9DBR and B0GHLBGCP3, and competitors Veken C1 B08NC54VZN, Veken B0FPFZ3C5K, PETLIBRO B0FDKQGRCK, Neareal 2.2L B0FJMBNZQ1 and B0C8MHHVPC.
  - **The Cerebro ranks are from 2026-10-03, before our title and bullet rewrite.** I checked whether each "gap" keyword is still missing against the **live** title and bullets of 2026-10-12.
- **Ads:** I read the search-term and targeting reports from `inbox/2026-10-07` and `inbox/2026-10-11`, and the business report for 10-11.
- **Not available:** the SP-API does not return star rating, review count or coupons. A coupon or Lightning Deal can only be checked by eye on Amazon. Backend search terms are not visible either.
- **How to read rank:** BSR is the category rank (Automatic Cat Feeders or Cat Fountains). It is shared by all variations of a parent ASIN; for example, all PETLIBRO colors share one rank.
- **Facts we may claim:** I limited this to `true_facts` in `images-aplus.json`. For example, the 5L feeder has a **recorded meal call, not 2-way audio**; the camera feeder has **no night vision**; the 2L fountain B0GHKN9DBR has **no filter**; the tray fountain has a **plastic body**.

## Where we stand today (live 2026-10-12)

| ASIN | Product | Price (Buy Box) | List price shown in data | BSR (category) | Images | Title chars | Sessions / CVR, 7 days to Oct 10 |
|---|---|---|---|---|---|---|---|
| B0GHH8L59K | 5L WiFi elevated dual feeder | $54.99 | $99.99 | #670 Automatic Cat Feeders | 8 | 189 | 25 / 4.0% (sold at $45.99) |
| B0GTCGYZDM | 3L camera feeder | $52.99 | $89.99 | #909 Automatic Cat Feeders | 9 | 191 | 13 / 0% |
| B0GHKN9DBR | 2L fountain (no filter) | $21.99 | none | #1,611 Cat Fountains | 9 | 179 | 33 / 9.1% (sold at $19.99) |
| B0GHLBGCP3 | 2.2L transparent fountain | $21.99 | $65.99 | #2,185 Cat Fountains | 9 | 192 | 26 / 3.8% |
| B0GHKRYV6W | 2.2L fountain, stainless steel tray | $21.99 | $65.99 | #2,431 Cat Fountains | 9 | 170 | 14 / 7.1% |

We hold the only offer and the Buy Box (Prime, FBA) on all five. Traffic is very low, at 13 to 33 sessions a week. The flat BSR is mainly a **traffic** problem: ads were paused or cut on Oct 4, and organic rank for the head terms is 200 to 300 or worse. Image count is not a gap, because we already have 8 to 9 images while winners have 6 to 9.

---

## 1. B0GHH8L59K: 5L WiFi elevated dual-bowl feeder ($54.99, #670)

### a) Closest winners (same shopper: WiFi or app, 2 cats or 5L+, $40–$100)

| ASIN | Brand | Title (first 80 chars) | Price now | BSR Auto Cat Feeders | Images | Key features |
|---|---|---|---|---|---|---|
| B0C5X4N132 | oneisall | oneisall 5G WiFi Automatic Cat Feeder for 2 Cats, App Control, 20 Cups/5L | $69.99 (list $84.99) | #3 | 9 | 5G/2.4G WiFi, 2 opposite bowls, 10-day capacity for 2 cats, 10 g portions, 10 s voice, desiccant, family app sharing |
| B09S8WMJY9 | PETLIBRO | PETLIBRO Automatic Cat Feeder, 5G WiFi Automatic Dog Food Dispenser with Freshne | $71.99 (list $99.99) | #2 | 9 | Single bowl 5L, 10 meals/day, 1–48 portions, low-food sensor and app alerts, twist-lock lid, 10 s meal call |
| B09VGDGR4B | PETLIBRO | PETLIBRO 5L Automatic Cat Feeder for 2 Cats, 5G&2.4G Wi-Fi Programmable Cat Food | $79.99 | #9 | 6 | Dual stainless bowls, airtight lock, low-food sensor, alerts for clog and low battery, dual power |
| B0D44QYZ7Z | PETLIBRO | PETLIBRO Automatic Cat Feeder for 2 Cats, 5G&2.4G WiFi Pet Feeders, 5L Programma | $99.99 | #9 | 9 | Same as above (black) |
| B0GR69G44J | MUBBI | MUBBI Automatic Dog Feeder with Elevated Stand - 7L Cat Food Dispenser with Larg | $44.99 | #17 | 8 | **Elevated legs** (the only other elevated design), 7L, no WiFi, 6 meals, anti-clog, triple lock |
| B0GXYJTFKB | KATALICLAB | Automatic Cat Feeders WiFi for Two Cats, 5L/20 Cups Double Automatic Cat Food Di | $49.99 (list $69.99) | #19 | 7 | Closest copy of ours: 5L/20 cups, dual-band WiFi, 2 bowls, 10 meals × 20 portions, D-battery backup, one-touch treat |
| B0GTXN5MJK | HoneyGuaridan | HoneyGuaridan 5L Automatic Cat Feeder for Two Cats, 2.4/5G WiFi Smart Feed Pet F | $69.99 | #25 | 6 | 5L, 2 bowls, rubber seal + desiccant, 10 s meal call, Type-C + 3 D batteries |
| B0GY4P3DHN | MRSDAYU | 6L Automatic Cat Feeder for 2 Cats, APP Control, Precise Portion Control | $42.99 (list $59.99) | #50 | 8 | 6L see-through tank, Tuya app, 2 bowls, USB-C + 3 C batteries, dishwasher safe |

Context: the non-WiFi #1 and #3 sellers, ANDOLL B0DCFW2LQT (4L, $42.99) and oneisall B0C5X2G933 (dual, $49.99), take the same budget shoppers with short 68–71-character titles.

### b) Title pattern of the winners

- **Leading keyword:** "Automatic Cat Feeder" right after the brand in 10 of 11 titles. "for 2 Cats" / "for Two Cats" follows in 8 of 11, inside the first 50 characters.
- **WiFi band:** "5G" / "2.4G" WiFi appears in 6 of 9 WiFi titles, usually within the first 80 characters.
- **Capacity:** placed early, at character 0 to 63. It is written "5L" or "20 Cups/5L"; KATALICLAB and oneisall give both units.
- **Length:** two styles. Short titles of 68–73 characters (oneisall #3, ANDOLL #1, HoneyGuaridan, MRSDAYU) or full titles of 167–197 characters (PETLIBRO, KATALICLAB, MUBBI).
- **Ours:** `PETME2 Automatic Cat Feeder for 2 Cats, 5L Elevated Feeding Station with WiFi Ap…`. This already follows the pattern: the exact phrase is at the front and the 5L capacity is in the first 45 characters. What it lacks against the winners:
  - "20 Cups" next to 5L
  - the WiFi band
  - "Programmable" / "Timed" near the front
  - The first 80 characters end mid-word at "WiFi Ap…".

### c) Winner keywords we do not use (Cerebro, generic only)

| Keyword | Search volume | Best winner rank | Our rank (Oct 3) | In our live listing? |
|---|---|---|---|---|
| cat food dispenser | 23,065 | PETLIBRO #10 | not ranked | bullets only, not in title |
| cat feeding station | 6,414 | oneisall #9 | 228 | bullets only (title says "Feeding Station") |
| automatic pet feeder | 4,241 | oneisall #14 | 289 | bullets only |
| timed cat feeder | 3,330 | PETLIBRO #8 | 270 | bullets only (title says "Timed Pet Food Dispenser") |
| automatic feeder cat dry food | 3,330 | PETLIBRO #15 | 242 | **missing** ("dry food" not used) |
| automatic cat feeder with app | 1,768 | oneisall #9 | 186 | bullets only |
| timed cat feeders for dry food | 1,766 | oneisall #10 | not ranked | bullets only |
| dual cat feeder automatic | 1,246 | oneisall #3 | 87 | **missing** |
| wifi automatic cat feeder app control | 1,244 | oneisall #5 | 158 | bullets only |
| double cat feeder | 1,156 | oneisall #5 | not ranked | bullets only. **It converted in our ads (1 order).** |
| automatic cat feeder programmable | 977 | oneisall #7 | not ranked | **missing** |
| double automatic cat feeder | 977 | oneisall #9 | 73 | **missing** |
| smart cat feeder / smart pet feeder | 882 / 880 | oneisall #3 / #6 | 253 / 213 | **missing** |
| cat food station | 882 | oneisall #13 | not ranked | **missing** |
| dual power automatic cat feeder battery backup | 731 | oneisall #7 | 99 | **missing** ("battery backup" not used) |
| wifi cat feeder | 666 | oneisall #2 | 158 | **missing** as a phrase |

Words in winner titles that are absent from ours:
- "5G" / "2.4G" (6 titles): only if verified.
- "20 Cups" (2 titles): true, because 5L ≈ 21 US cups.
- "Programmable", "Low Food Sensor" and "Airtight / Freshness": only if true. Our verified 5L facts do not include a low-food sensor or a seal or desiccant.

### d) Price position

- **Cheaper than the branded WiFi duals:**
  - $15 below oneisall #3 ($69.99)
  - $17 below PETLIBRO 5L #2 ($71.99)
  - $25–45 below the PETLIBRO dual units ($79.99–$99.99)
  - $15 below HoneyGuaridan ($69.99)
- **More expensive than the close copies ranking above us:** KATALICLAB 5L WiFi dual is $49.99 (#19, $5 less) and MRSDAYU 6L app dual is $42.99 (#50, $12 less).
- **Non-WiFi models are cheaper:** MUBBI's elevated 7L is $44.99, $10 less.
- **Deals:** coupons are not visible through the API. 7 of 8 winners carry a list price above the sale price (for example KATALICLAB $49.99 vs $69.99, oneisall $69.99 vs $84.99). Ours shows $54.99 vs a $99.99 list price, a 45% gap that Amazon may not display unless that price was really charged.
- **Margin:** $54.99 is the break-even price when all sales come from ads ($54.00, per the pricing analysis). We cannot win on price against KATALICLAB; we have to win on the "elevated" design.

### e) Feature and claim gaps (features we have, said too weakly)

1. **Elevated + dual + WiFi in one unit is unique.** MUBBI is elevated but single-bowl with no WiFi; KATALICLAB and oneisall have WiFi but no legs. Our title says "Elevated" but never says why it matters, for example that raised bowls give a better eating posture. A bullet already says "comfortable eating height". Put the bowl height in inches in an image; the item is 15.62 in tall, so measure the bowl rim height.
2. **Hard numbers.** Every winner states capacity in cups and days for 2 cats, grams per portion and meals per day. We only say "5L". Add "5L (about 20 cups)", and add portion size, meals per day and days of food only after confirming them with the supplier.
3. **Power.** Winners name the battery type (4 AA, 3 D, 3 C). A review says ours takes 4 AA batteries (not included). Say this plainly once it is confirmed, so buyers are not surprised.
4. **Image accuracy.** Reviews say "pic does not match" and "thought legs were wood; gray legs". Show the real gray legs and the real color in the main image and image 2. This is a conversion leak, not a ranking one.
5. **Voice recording.** Winners state "10 s meal call". If the length is verified, add the seconds. Do **not** call it 2-way audio.

### f) 3 honest ideas to beat them

1. **Title v2 (keep it under 150 characters and put more value in the first 80):** `PETME2 Automatic Cat Feeder for 2 Cats, 5L/20 Cups Elevated WiFi Cat Food Dispenser, Timed Dual Bowl Smart Pet Feeder…`. Add "5G/2.4G WiFi" only if verified. Move "double cat feeder", "dry food", "programmable" and "battery backup" into bullets and backend terms.
2. **Image order:**
   - Image 2: elevated side view with raised-bowl height, a 2-cat even split and true gray legs.
   - Image 3: "5L / about 20 cups".
   - Image 4: app schedule screen.
   - Image 5: power adapter and battery backup with the battery type.

   Then add a **comparison chart in A+ against our own 3L dual feeder** (B0GHLSQMJ9). Use our own ASINs only, as A+ rules require.
3. **Price and promo:** keep $54.99 as the base. Run a **$5 coupon** (net $49.99, matching KATALICLAB) only while ads run, so the cost is measured. The alternative is a Prime-exclusive discount before Black Friday. Do not go below $54.00 net plus ad cost. Raise bids on the ASIN targets B0C5X4N132, B09S8WMJY9 and B0GTXN5MJK: they earned only 3–17 impressions last week, so we are not visible on their pages yet. The "double cat feeder" keyword already converted.

---

## 2. B0GTCGYZDM: 3L camera feeder, 1080P, 2-way audio, app ($52.99, #909)

### a) Closest winners (camera feeders, $48–$100)

| ASIN | Brand | Title (first 80 chars) | Price now | BSR Auto Cat Feeders | Images | Key features |
|---|---|---|---|---|---|---|
| B0CNNNJ3FQ | Yuposl | Automatic Cat Feeder with Camera - 5G WiFi Auto Cat Food Dispenser, 1080P HD Vid | $59.99 (list $66.99) | #4 | 8 | **Only 2L**, 1080P + night vision, wide angle, 2-way audio, 1–15 meals / 1–99 portions, motion capture alerts |
| B0B5ZGGWBQ | PETLIBRO | PETLIBRO Automatic Cat Feeder with Camera, 1080P HD Video & Night Vision | $125.99 | #8 | 9 | 145° lens, night vision, motion and sound alerts, activity recording, desiccant |
| B0DCNNN5FC | Frienhund | Frienhund Automatic Cat Feeder with 2K Camera: 5G WiFi Automatic Dog Feeder with | $59.99 (list $69.99) | #10 | 9 | 3MP/2K, 7L/29 cups, 15 meals, dual-band WiFi, 2-way audio, anti-tip |
| B0GSR1GTHW | MUBBI | Automatic Cat Feeder with Camera - 7L/29 Cups Auto Dog Feeder with Large Food Tr | $59.99 (list $69.99) | #17 | 9 | 7L, elevated legs, 1080P + night vision, privacy mode, 2-way audio, 10 s call |
| B0H7WS6PX9 | Minikey | Automatic Cat Feeder with 2K Camera, 6.5L Smart App Control 5G/2.4WiFi | $48.29 (list $69.99) | #33 | 8 | 2K, 145°, AI activity tracking, family sharing, anti-tip clip, 304 bowl |
| B0FR4Z89KT | Faroro | Faroro Automatic Cat Feeder with Camera, 1080P HD Video with Night Vision, 5G Wi | $59.99 (list $129.99) | #37 | 9 | 4L, 120° adjustable lens, dual-band WiFi, 2-way audio, blockage sensor |
| B0GFDH3WD5 | oneisall | oneisall Automatic Cat Feeder with Camera for 2 Cats Pets, 20 Cups/5L | $99.99 | #35 | 9 | 2 cameras, 2 bowls, 5L, 3 D-battery backup |

The PETLIBRO camera family (B0FJM41MLT, $149.99) shares rank #2.

### b) Title pattern of the winners

- **Leading keyword:** all 8 start with "Automatic Cat Feeder with Camera" or "…with 2K Camera", either right after the brand or with no brand at all (Yuposl, MUBBI, Minikey).
- **"Night Vision" appears in 6 of 8 titles**, plus "5G WiFi" (6/8), "1080P/2K" (7/8) and "2-Way Audio".
- **Capacity:** often absent or late. Only Frienhund, MUBBI, Minikey and oneisall show it, and they have 5–7L, which is bigger than our 3L.
- **Length:** split between short (69–72 characters: PETLIBRO, Minikey, oneisall) and long (185–200).
- **Ours:** `PETME2 Automatic Cat Feeder with Camera, 3L WiFi Cat Food Dispenser with 1080P H…`. The exact phrase is at the front and correct. We do **not** have night vision, so do not add it. The first 80 characters spend room on "3L". 3L is a weakness against 5–7L competitors; Yuposl #4 shows its 2L only in the attributes.

### c) Winner keywords we do not use (Cerebro, generic only)

| Keyword | Search volume | Best winner rank | Our rank (Oct 3) | In our live listing? |
|---|---|---|---|---|
| automatic cat feeders | 4,110 | PETLIBRO #13 | 299 | plural form only, low impact |
| timed cat feeder | 3,330 | PETLIBRO #8 | 242 | bullets only |
| automatic feeder cat dry food | 3,330 | PETLIBRO #15 | 250 | **missing** ("dry food") |
| pet feeder | 3,330 | Frienhund #8 | not ranked | bullets only |
| cat food dispenser automatic | 2,667 | Frienhund #12 | 251 | word order only, OK |
| pet food dispenser | 1,598 | PETLIBRO #9 | not ranked | **missing** |
| automatic dog feeder with camera | 977 | PETLIBRO #11 | 102 | words present, not as a phrase |
| smart pet feeder / smart cat feeder | 880 / 882 | PETLIBRO #13 / Frienhund #1 | 218 / 220 | "smart" only in bullets |
| pet feeder with camera | 782 | Frienhund #5 | 140 | **missing** as a phrase |
| wifi cat feeder | 666 | PETLIBRO #16 | 218 | **missing** as a phrase |
| automatic pet feeder with camera | 615 | Frienhund #10 | 151 | **missing** as a phrase |
| cat food dispenser with camera | 605 | PETLIBRO #10 | 86 | **missing** as a phrase |
| cat feeder camera | 518 | Frienhund #7 | 117 | covered by the words |

The head terms "automatic cat feeder with camera" (6,417) and "cat feeder with camera" (2,519) are already in the title. We ranked #121 and #127 on Oct 3, against winners at #6 to #12. The gap is sales velocity and reviews, not indexing.

### d) Price position

- **We are the 2nd-cheapest camera feeder among the winners.** Only Minikey is cheaper at $48.29, and it has 6.5L and 2K.
- We are $7 below the $59.99 cluster (Yuposl, Frienhund, MUBBI, Faroro), $47 below oneisall and $73 below PETLIBRO.
- **Deals:** Faroro shows a $129.99 list price against $59.99, and Minikey $69.99 against $48.29. Ours shows $89.99 against $52.99. No coupons are visible through the API.
- Price is **not** the reason we lose. At $52.99 we are near the healthy price ($53.50), with no room to cut. Reviews call it "pricey at $65.99", which was the old price.

### e) Feature and claim gaps (features we have, said too weakly)

Review complaints point to the app experience, not specs: "app only, no manual button", "instructions unclear", "won't connect to WiFi", "Android 16 crash".

1. **WiFi band.** Winners all advertise "5G/2.4G" because connection failure is the top fear. If ours is **2.4 GHz only**, say so clearly ("Connects to 2.4 GHz WiFi") in bullet 3 and in an image. This is honest, prevents returns and answers the review complaint.
2. **Tap to feed on demand** is true and is a selling point for winners (Minikey, oneisall: "Tap to Treat"). It is in our bullet 3 but not in the title or images.
3. **Freshness.** The moisture seals and desiccant box are true but not mentioned. Winners PETLIBRO, Yuposl, MUBBI and Faroro all mention them.
4. **Dishwasher-safe stainless bowl** is true; say "dishwasher safe" explicitly.
5. **Setup help.** Add a QR code or setup-video image ("3-step WiFi setup") and a short main video. This answers "instructions unclear". Do not add night vision, field of view or motion alerts unless they are confirmed.

### f) 3 honest ideas to beat them

1. **Title:** keep the start, then a value hook. `PETME2 Automatic Cat Feeder with Camera, 1080P Video & 2-Way Audio, WiFi App Pet Feeder with Camera, Tap-to-Feed, 3L Cat Food Dispenser for Dry Food, Anti-Jam, Battery Backup`. This adds the "pet feeder with camera", "dry food" and "battery backup" phrases. Add "2.4GHz" once confirmed.
2. **Images and A+:**
   - Image 2: live-view phone screen with a 2-way audio bubble.
   - Image 3: an "Easy WiFi setup" image with the band and 3 steps.
   - Image 4: an image showing what's included and what's not, with the batteries not included, so the "app only" expectation is set honestly.
   - A+: a "No WiFi? It still feeds on schedule" module, **only if** the feeder keeps the saved schedule offline (confirm first).
3. **Positioning and price:** at $52.99 we sit under the $59.99 cluster. Show the value in the price ("1080P camera + 2-way audio under $55" in ads copy, not on images). Bid on Yuposl B0CNNNJ3FQ (2L, $59.99), because our 3L is bigger and $7 cheaper. That is a fair page to win, and today we get 0–16 impressions on camera competitor targets.

---

## 3. B0GHKN9DBR: 2L plastic fountain, no filter ($21.99, #1,611)

### a) Closest winners ($18–$26 basic 2–2.8L fountains)

| ASIN | Brand | Title (first 80 chars) | Price now | BSR Cat Fountains | Images | Key features |
|---|---|---|---|---|---|---|
| B08NCDBT7Q | Veken | Veken Innovation Award Winner 95oz/2.8L Cat Water Fountain, C1 Classic | $21.99 | #3 | 9 | Award, 2 flow modes, 5-stage filter, **2 filters + 2 sponges + mat + brush included**, level window, LED |
| B0FJMF2T4J | Neareal | Cat Water Fountain Stainless Steel: 74oz/2.2L Cat Fountain for Drinking | $24.99 | #4 | 9 | Stainless, 4-layer filter, ≤28 dB 5V pump, window |
| B0DDPYHHFX | GIOTOHUN | Cat Water Fountain Stainless Steel: 74oz/2.2L Cat Fountain for Drinking | $19.94 (list $24.99) | #5 | 9 | SUS304, faucet and fountain modes, <25 dB, 4-stage filter |
| B0FBS5L5BY | BalimoPet | Cat Water Fountain Stainless Steel - 74oz/2.2L Automatic Large Pet Watering Bowl | $18.99 (list $22.99) | #6 | 9 | Stainless, **3 filters + 3 sponges**, no-spill |
| B0GGM2KHL5 | PETUNO | PETUNO Cordless Cat Water Fountain, Battery Operated, Black, 78oz/2.3L | $23.99 (list $29.99) | #33 | 9 | Cordless 30-day battery, 3 modes, 30 dB, lock |
| B07SBXDMZQ | Wonder Creature | Wonder Creature Cat Water Fountain Stainless Steel Lid 81oz/2.4L-3 Filters | $22.99 | #39 | 7 | Stainless lid, 3 carbon filters, <40 dB, LED |
| B0DCVXBSYS | KOOGMOON | Cat Water Fountain Stainless Steel: 2.2 L Cat Fountain for Drinking - Automatic | $19.99 (list $29.99) | #43 | 9 | Stainless, window, quiet |
| B0BF5CQMKX | PETKIT | PETKIT Eversweet Solo SE Cat Water Fountain 65oz/1.85L Wireless Pump | $25.99 (list $29.99) | #55 | 8 | Wireless pump, tank separated from power, dry-burn stop, indicator light |

### b) Title pattern of the winners

- **Short titles win:** 9 of 11 are 46–74 characters. The format is "Cat Water Fountain [Stainless Steel]: 74oz/2.2L Cat Fountain for Drinking".
- **Leading keyword:** "Cat Water Fountain" in the first 1–30 characters (11/11). Capacity is in **oz/L, oz first**, at character 30–45 (9/11).
- **One hook only:** award, stainless, "3 Filters", cordless or wireless pump.
- **Ours (179 characters):** `PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Li…`. The structure is good. The issue is the product: 7 of the top-8 sellers at our price are **stainless 2.2L** units, and ours is plastic with no filter.

### c) Winner keywords we do not use (Cerebro, generic only; fits a plastic, no-filter fountain)

| Keyword | Search volume | Best winner rank | Our rank (Oct 3) | In our live listing? |
|---|---|---|---|---|
| pet water fountain | 42,109 | Neareal #2 | not ranked | bullets only |
| cat water bowl | 27,400 | Neareal #3, Veken #6 | not ranked | bullets only. **Our ads: 837 impressions, 14 clicks, 1 order.** |
| cat water dispenser | 17,542 | Neareal #8 | 254 | bullets only. **Converted in ads.** |
| automatic water dispenser for cats | 8,819 | Veken #2 | 257 | bullets only |
| cat drinking fountain | 5,948 | Neareal #3 | 216 | bullets only |
| kitten water fountain | 2,502 | Veken #1 | 277 | bullets only |
| cat water dish | 2,414 | Neareal #2 | not ranked | **missing** |
| dog drinking fountain | 2,169 | Neareal #11 | 198 | **missing** |
| small cat water fountain | 1,768 | Neareal #1 | 128 | bullets only |
| water dish for cats | 1,761 | Neareal #2 | not ranked | **missing** |
| auto water for cats | 1,594 | Veken #1 | 145 | **missing** |
| quiet cat water fountain | 1,594 | Neareal #1 | 143 | bullets only |
| cat waterer | 1,246 | Neareal #6 | not ranked | **missing** |
| water bowls for cats | 1,246 | Neareal #4 | 270 | **missing** as a phrase |
| pet drinking fountain | 1,103 | Neareal #3 | not ranked | **missing** |

Do not use "filter" keywords on this ASIN, because it has no filter.

### d) Price position

- **Same price as Veken C1 ($21.99).** Veken is #3, bigger (2.8L) and award-winning, with filters and accessories included. A month ago Veken was $13.99; it has since gone up to $21.99, which narrows our gap.
- We are $2–3 **above** the stainless 2.2L units GIOTOHUN ($19.94), BalimoPet ($18.99) and KOOGMOON ($19.99), and $3 below Neareal ($24.99).
- **Deals:** this is the only one of our five with **no list price**. Most winners show one: GIOTOHUN $24.99, KOOGMOON $29.99, PETKIT $29.99, PETUNO $29.99.
- We cannot cut price: break-even with ads is about $27.50.

### e) Feature and claim gaps (features we have, said too weakly)

1. **Safety and pump protection.** We have the anti-dry pump shut-off **and** the red low-water light. PETKIT (#55, $25.99) sells on exactly these: dry-burn stop and indicator light. Most stainless winners do not mention a low-water light. Make it the hook, at the front of the title.
2. **Slim and light 2L.** "Small" searches are ones the winners rank for (Neareal #1). Ours is the smallest: 7.5 in square package, 1.5 lb. Give the footprint in inches in an image.
3. **Quiet.** Every winner gives a dB number (≤25 to ≤40 dB). We say "quiet" with no number. Measure it first; add the number only if measured.
4. **What's in the box.** Winners list the box contents (filters, sponges, mat, brush). Ours is the unit, reservoir, cable and manual, with no filter to replace. Say this honestly as a benefit: "No filters to buy: rinse and refill." That framing is only fair if we tell people to clean weekly.

### f) 3 honest ideas to beat them

1. **Short, demand-led title (~110 characters):** `PETME2 Cat Water Fountain 68oz/2L, Small Quiet Cat Water Dispenser with Low Water Light & Auto Pump Shut-Off, Cat Water Bowl for Indoor Kittens`. Put "water dish", "cat waterer", "auto water" and "pet drinking fountain" in the backend.
2. **Bundle or variation:** this ASIN cannot win a feature fight against stainless 2.2L units at $19–25. Make a **variation family** of the three PETME2 fountains (2L / transparent 2.2L / stainless tray 2.2L) so they share reviews and BSR and each sells a clear difference. Alternatively, sell the 2L with an add-on (for example a silicone mat) only if it is real.
3. **Ads plus coupon:** keep $21.99. Put the small budget on the terms that already converted ("cat water bowl" and "cat water dispenser") and on the Veken C1 B08NCDBT7Q product page. That target got 762 impressions, 17 clicks and **2 orders** in the week to Oct 7. A 10% coupon is affordable only while it lifts the conversion rate. The earlier 9.1% CVR at $19.99 is the best of the five.

---

## 4. B0GHLBGCP3: 2.2L transparent fountain, 4-layer filter ($21.99, #2,185)

### a) Closest winners (see-through or windowed plastic fountains, $18–$33)

| ASIN | Brand | Title (first 80 chars) | Price now | BSR Cat Fountains | Images | Key features |
|---|---|---|---|---|---|---|
| B08NCDBT7Q | Veken | Veken Innovation Award Winner 95oz/2.8L Cat Water Fountain, C1 Classic | $21.99 | #3 | 9 | Level window, blue LED, 2 flow modes, 5-stage filter, 2+2 filters in box |
| B0BF5CQMKX | PETKIT | PETKIT Eversweet Solo SE Cat Water Fountain 65oz/1.85L Wireless Pump | $25.99 | #55 | 8 | See-through tank, wireless pump, separate power base, dry-burn stop |
| B0FN7FQ7RJ | oneisall | oneisall 2.2L/74oz Wireless Cat Water Fountain | $29.99 | #57 | 9 | Semi-transparent body, battery, 3 modes, 20 dB, 5-layer filter |
| B08XB56DKP | HAPUP | HAPUP Cat Water Fountain Animal Water Dispenser 61OZ/1.8L Automatic Pet Drinking | $20.99 (list $28.99) | #328 | 7 | Clear body, 2 flow modes, 2 spare filters, adjustable pump |
| B07ZVHMRPS | PETNF | PETNF Transparent 3L/101oz Pet Water Fountain - Automatic Cat & Dog Dispenser wi | $18.99 (list $21.99) | #345 | 9 | Transparent, 3L, LED (blue to red when low), auto shut-off, 2 filters, 300 ml reserve |
| B09PDZ2GFR | NPET | NPET WF100 Cat Foutain, 54oz/1.6L Automatic Pet Water Fountain Dog Water Dispens | $19.99 (list $30.99) | #684 | 8 | Transparent window, 2 flow modes, LED, bottom-suction pump, 3-layer filter |
| B0H8RFKYN8 | ATADD | ATADD Cat Water Fountain 304 Stainless Steel Tray with Food-Grade Clear Plastic | $32.99 | #1,489 | 6 | Clear tank + 304 tray, multi-layer filter |

Glass fountains (Brook $89.95 #82, VinDox $45.99 #113, Cepheus $37.99 #168) own the "transparent" look but sell to a different price band.

### b) Title pattern of the winners

- The direct transparent competitors (PETNF, HAPUP, NPET) use long titles of 136–184 characters. They lead with "Cat Water Fountain" or "Transparent 3L/101oz Pet Water Fountain", put capacity in oz/L at character 18–48, then add "2 flow modes", "LED", "2 filters".
- Search demand for "clear" or "transparent" is tiny: "cat water fountain clear" gets **89 searches a month**. Transparency sells on the **image**, not in search.
- **Ours:** `PETME2 Transparent Cat Water Fountain 74oz/2.2L, 4-Layer Filtered Cat Water Disp…`. That is fine, but "Transparent" takes the most valuable slot after the brand for a word nobody searches.

### c) Winner keywords we do not use (Cerebro, generic only)

| Keyword | Search volume | Best winner rank | Our rank (Oct 3) | In our live listing? |
|---|---|---|---|---|
| pet water fountain | 42,109 | Neareal #2 | not ranked | bullets only |
| water fountains for cats indoor | 49,512 | Neareal #1, Veken #3 | 285 | bullets only (it is in the title of B0GHKN9DBR, not here) |
| cat water bowl | 27,400 | Neareal #3 | not ranked | bullets only |
| water fountain for cats | 7,835 | Neareal #2 | not ranked | **missing** |
| automatic water dispenser for cats | 8,819 | Veken #2 | 249 | bullets only |
| cat drinking fountain | 5,948 | Neareal #3 | not ranked | bullets only |
| kitten water fountain | 2,502 | Veken #1 | 228 | bullets only |
| cat water dish / water dish for cats | 2,414 / 1,761 | Neareal #2 | not ranked | **missing** |
| quiet cat water fountain | 1,594 | Neareal #1 | 299 | bullets only |
| auto water for cats | 1,594 | Veken #1 | not ranked | **missing** |
| cat waterer | 1,246 | Neareal #6 | 277 | **missing** |
| cat water fountain with filter / with filters | 731 / 532 | Neareal #3, Veken #2 | not ranked | **missing**, and true for this ASIN |
| cat water fountain with filters included | 339 | competitor A ranks | n/a | **missing**, and true (1 cartridge in box) |

### d) Price position

- Same price as Veken C1 ($21.99). We are $1–3 above the direct transparent competitors PETNF ($18.99), NPET ($19.99) and HAPUP ($20.99), and $4–8 below PETKIT ($25.99) and oneisall ($29.99).
- **Deals:** our list price in the data is $65.99, which is 3× the sale price. Amazon will most likely not show a strike-through for it, and it could look misleading. Use a believable list price that was really charged, or none.
- Break-even with ads is about $27.50, so there is no room to cut.

### e) Feature and claim gaps (features we have, said too weakly)

Reviews ask for replacement filters ("can't find replacement filters"), say "not wireless" and "not what's shown", and mention flow slowing when the filter clogs.

1. **Replacement filter availability.** Winners give a refill ASIN (PETKIT names its spare pump ASIN) or say "3 filters included". Our biggest fixable gap: list a PETME2 replacement filter pack (or state a compatible cartridge) and say in a bullet how often to change it.
2. **Corded USB, said honestly.** Writing "USB powered (plug-in, not cordless)" stops the "not wireless" disappointment.
3. **Low-water protection.** We have anti-dry protection. PETNF (the most similar transparent unit) sells on "LED turns red when low + auto shut-off". Our verified facts for this ASIN list anti-dry but not a red light, so only claim the light if this model has it.
4. **Image accuracy.** One review says "not what's shown". Make the main image the real clear body, with color and top exactly as delivered (color: "Clear Base With White Topping").

### f) 3 honest ideas to beat them

1. **Title reorder (demand first, transparency second):** `PETME2 Cat Water Fountain with Filter, 74oz/2.2L Transparent Water Fountain for Cats Indoor, Quiet Cat Water Dispenser, Anti-Dry Pump, Visible Water Level`.
2. **Image 2 = "See when to refill."** A side-by-side of full vs low water through the clear body; this is the one thing the stainless winners cannot show. Image 3: the 4-layer filter exploded view + "1 filter included, replacement filter pack: [ASIN]". Image 4: a setup and cleaning image.
3. **Sell a 3-pack replacement filter ASIN, or a fountain + 2 extra filters bundle.** Several competitors list it ("2 filters", "3 filters"), and it answers our top review complaint. Consider a **variation family** with B0GHKRYV6W, which may share the same cartridge (confirm first), to pool reviews.

---

## 5. B0GHKRYV6W: 2.2L fountain with stainless steel tray + filters ($21.99, #2,431)

### a) Closest winners (2–2.5L fountains with steel top or tray, $19–$46)

| ASIN | Brand | Title (first 80 chars) | Price now | BSR Cat Fountains | Images | Key features |
|---|---|---|---|---|---|---|
| B0FJMF2T4J | Neareal | Cat Water Fountain Stainless Steel: 74oz/2.2L Cat Fountain for Drinking | $24.99 | #4 | 9 | Stainless, level window, 4-layer filter, ≤28 dB |
| B0DDPYHHFX | GIOTOHUN | Cat Water Fountain Stainless Steel: 74oz/2.2L Cat Fountain for Drinking | $19.94 | #5 | 9 | SUS304, 2 flow modes, <25 dB, 4-stage filter, carbon + sponge in box |
| B0FBS5L5BY | BalimoPet | Cat Water Fountain Stainless Steel - 74oz/2.2L Automatic Large Pet Watering Bowl | $18.99 | #6 | 9 | **3 filters + 3 sponges**, window, no-spill |
| B0G6ZMT8T3 | PETLIBRO | PETLIBRO Cat Water Fountain Stainless Steel Tray, Wireless Pump Cat Fountain, Ul | $45.58 (list $49.99) | #11 | 7 | SS tray, wireless pump, <23 dB, dual flow, 2.5L |
| B07SBXDMZQ | Wonder Creature | Wonder Creature Cat Water Fountain Stainless Steel Lid 81oz/2.4L-3 Filters | $22.99 | #39 | 7 | SS lid, dishwasher safe, **3 filters**, <40 dB, LED |
| B0H74TPPHS | Cheerble | Cheerble Elfin E1S Pumpless Cat Water Fountain, 2L/67oz, 304 Food-Grade Stainles | $44.99 | #272 | 8 | 304 tray "no more cat acne", pumpless, 3-layer filter |
| B0GX4XR23M | HomeRunPet | HomeRunPet Cat Water Fountain Stainless Steel Tray with Cordless Pump, 68oz | $29.99 (list $45.99) | #613 | 7 | SS tray, cordless pump, "clean in 20 seconds", <20 dB |
| B0H8RFKYN8 | ATADD | ATADD Cat Water Fountain 304 Stainless Steel Tray with Food-Grade Clear Plastic | $32.99 | #1,489 | 6 | 304 tray + clear tank, multi-layer filter |

### b) Title pattern of the winners

- **Top 3 (#4–#6):** `Cat Water Fountain Stainless Steel: 74oz/2.2L …`. The material word comes immediately after the head term, the capacity is at character 36 (oz first), and two of the three titles are only 68–71 characters.
- **Tray-specific sellers** (PETLIBRO, HomeRunPet, ATADD, Cheerble): "Cat Water Fountain Stainless Steel Tray" in the first 40 characters. They add "304" / "Food-Grade" (2 titles), and filter count ("3 Filters") appears in 2 titles.
- **Ours:** `PETME2 Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Automatic Pet Fou…`. The pattern is right and honest (tray, not whole body). Missing compared with the winners:
  - the **number of filters included**: the count is not confirmed yet, so confirm it
  - "304" / food-grade, which we may only add if verified
  - "Quiet" with a dB number

### c) Winner keywords we do not use (Cerebro, generic only; this ASIN has no Cerebro rank column)

| Keyword | Search volume | Best winner rank | In our live listing? |
|---|---|---|---|
| pet water fountain | 42,109 | Neareal #2 | **missing** |
| cat water bowl | 27,400 | Neareal #3 | **missing** |
| water fountain for cats | 7,835 | Neareal #2 | **missing** |
| cat drinking fountain | 5,948 | Neareal #3 | **missing** |
| cat water dish / water dish for cats | 2,414 / 1,761 | Neareal #2 | **missing** |
| kitty water fountain | 1,870 | Neareal #2 | **missing** |
| quiet cat water fountain | 1,594 | Neareal #1 | **missing** (title has "Quiet Pump") |
| auto water for cats | 1,594 | Veken #1 | **missing** |
| cat waterer | 1,246 | Neareal #6 | **missing** |
| water bowls for cats | 1,246 | Neareal #4 | **missing** |
| pet drinking fountain | 1,103 | Neareal #3 | **missing** |
| cat water fountain with filter(s) | 731 / 532 | Neareal #3, Veken #2 | **missing** (title has "Filters Included") |
| cat water fountain with filters included | 339 | competitor A ranks | words present, phrase split |

Stainless head terms such as "cat water fountain stainless steel" (79,303) and "stainless steel cat water fountain" (70,227) are where Neareal and GIOTOHUN rank #2. Our title already has "Stainless Steel Tray", which is honest and indexes those words. **Do not** call it a "stainless steel fountain".

### d) Price position

- We sit $2–3 above GIOTOHUN ($19.94) and BalimoPet ($18.99), $3 below Neareal ($24.99) and $1 below Wonder Creature ($22.99).
- We are $8–24 below the other tray designs: HomeRunPet $29.99, ATADD $32.99, Cheerble $44.99, PETLIBRO $45.58.
- **Deals:** the same $65.99 list-price issue as the transparent fountain. No coupons are visible through the API.

### e) Feature and claim gaps (features we have, said too weakly)

Reviews say "hard to clean", "the tank is still plastic" and "no replacement filters found".

1. **Number of filters in the box.** BalimoPet (3+3) and Wonder Creature (3) put the count in the title. Our title says "Filters Included" with no number, and the count is not confirmed. Confirm the count and put it in the title, for example "2 Filters". Also offer a refill pack, which answers the reviews.
2. **Stainless steel tray benefits.** We state it, and a bullet explains it ("wipes clean"). Cheerble and HomeRunPet sell the tray as "resists staining and odor, easier to keep clean than plastic". That is fine to say. Avoid health claims ("chin acne"); the image audit already says to remove them.
3. **Be clear about the plastic body.** The bullet already says "the fountain body is light plastic". Keep that wording, because it sets expectations and reduces "tank is still plastic" reviews.
4. **Cleaning.** HomeRunPet says "clean in 20 seconds" and Veken says "4-step snap assembly". We say "fully detachable". Add an exploded-parts cleaning image with the number of parts.

### f) 3 honest ideas to beat them

1. **Title v2:** `PETME2 Cat Water Fountain Stainless Steel Tray, 74oz/2.2L Quiet Pet Water Fountain with [N] Filters, Cat Water Dispenser with Low Water Alert & Auto Shut-Off`. This uses the winners' order: head term, material, capacity, filter count.
2. **Images:**
   - Image 2: a close-up of the stainless tray and an exploded view of the parts, with an honest caption ("stainless drinking tray, BPA-free plastic body" only if the plastic is BPA-free).
   - Image 3: "[N] filters included + refill pack".
   - Image 4: a size image against a cat.
   - A+ comparison chart of **our own** fountains: 2L basic, 2.2L clear, 2.2L tray and the 3.2L stainless B0DR7FCLZR. This moves shoppers to the right model and to the 3.2L stainless if they want "all steel".
3. **Price:** at $21.99 we are already in the band of the #4–#6 winners. Do not discount further. Use a small coupon (5–10%) only together with ads on the converting terms ("cat water dispenser", "water fountains for cats indoor"). Target competitor ASINs where we are clearly better value: HomeRunPet B0GX4XR23M ($29.99) and ATADD B0H8RFKYN8 ($32.99) have the same tray design and cost $8–11 more.

---

## Cross-product notes

- **Competitor targeting is mostly not serving.** In the week to Oct 11, the feeder targets got 0–17 impressions each (5L group: 22 impressions in total; camera group: 19). The $19.99-fountain targets got 54–123 impressions each with 0 orders. ASIN targeting needs higher bids on a few chosen pages; across the ad groups, only B09S8WMJY9 (2 orders, for the 3L dual feeder) and Veken C1 (2 orders) have converted.
- **Our list prices** ($99.99 / $89.99 / $65.99) are 1.7–3× the sale price. Competitors use 1.1–1.5×, except Faroro at 2.2×. Amazon only shows a strike-through it can verify, so these are probably not shown, and a 3× list price can look like a fake discount. Set realistic list prices.
- **Verify before claiming:**
  - the WiFi band on both feeders
  - portion grams, meals per day and voice-recording length (5L)
  - pump dB (fountains)
  - the filter count (B0GHKRYV6W)
  - "304" / BPA-free
  - whether the camera feeder keeps its schedule offline
  - the 5L battery type (4 AA, per a review)

## 10-line summary

1. All 5 products hold the Buy Box but get only 13–33 sessions a week. The flat BSR is mostly a traffic problem (ads cut on Oct 4, organic rank 200+), not a price or Buy Box problem.
2. **5L feeder ($54.99):** cheaper than the branded WiFi duals (oneisall #3 $69.99, PETLIBRO #2 $71.99), but $5–12 above KATALICLAB ($49.99, #19) and MRSDAYU ($42.99, #50). Our edge is being the only elevated + dual + WiFi unit.
3. **5L:** add "5L/20 Cups", "Timed / Dry Food / Programmable", "Double / Smart" phrases and the battery type. Fix the gray-leg images. Test a $5 coupon only with ads on. "Double cat feeder" already converted.
4. **Camera feeder ($52.99):** 2nd-cheapest among the winners and $7 under the $59.99 cluster. We lose on reviews, capacity (3L vs 5–7L) and night vision, which we must not claim.
5. **Camera:** state the WiFi band honestly, add a 3-step setup image, and sell tap-to-feed, the desiccant and the dishwasher-safe bowl. Target Yuposl B0CNNNJ3FQ (2L, $59.99).
6. **Fountains ($21.99):** the top sellers at this price are short-titled stainless 2.2L units (Neareal, GIOTOHUN, BalimoPet, #4–#6) and Veken C1 (#3) at the same $21.99. Plastic models cannot win the head term.
7. **Fountains:** move "cat water bowl", "cat water dispenser" and "automatic water dispenser for cats" into the titles (they convert in our ads). Add "cat waterer", "water dish", "pet drinking fountain" and "auto water for cats" to the backend.
8. **Transparent:** nobody searches "clear" (89 a month), so lead with demand terms and use images to show transparency. The fix with the most impact is replacement filters (top review complaint).
9. **Tray:** copy the winners' title order (head term, "Stainless Steel Tray", 74oz/2.2L, filter count). Confirm the filter count and add a refill pack. Keep "plastic body" honest.
10. **All:** set realistic list prices (we show $65.99 against $21.99), form a fountain variation family to pool reviews, add an own-product A+ comparison chart, and raise bids on a few chosen competitor ASINs. Today they barely serve.
