# Keyword report: 5 products with flat BSR (2026-10-12)

Keyword agent. Read-only. Nothing was changed on Amazon.

**Products:** 5L WiFi dual feeder B0GHH8L59K, 3L camera feeder B0GTCGYZDM, 2L fountain B0GHKN9DBR, 2.2L transparent fountain B0GHLBGCP3, 2.2L fountain with steel tray B0GHKRYV6W.

**Sources:**
- **Live listing text:** SP-API Catalog Items 2022-04-01, pulled today (Oct 12): title, bullets, description, attributes, BSR.
- **Oct 4 keyword copy:** `research/seo/drafts/*.json` and `research/seo/final/listings-final.json`, the version that was published.
- **Keyword data:** Helium 10 Cerebro exports from Oct 3/4 (`research/helium10/*.csv`, about 14.4k phrases).
- **Ads reports:**
  - `inbox/2026-10-07` search terms: Sep 30 - Oct 6, mostly the OLD campaigns.
  - `inbox/2026-10-11` search terms and targeting: Oct 5 - Oct 10, the NEW V2 campaigns.
- **Business report:** `inbox/2026-10-11/BusinessReport-child-10-11-26.csv` (Oct 4 - 10).

**Important limits:**
1. **Organic ranks are from Oct 3/4, before the new copy went live.** We don't know the current keyword ranks. See the last section for the exact Helium 10 export we need.
2. **Cerebro shows ranks only down to about #306.** "Not ranked" means worse than about #306 or not found.
3. **B0GHKRYV6W was never in a Cerebro run, so it has no rank data.** For it we show the sister fountains' ranks (2L / clear) as a rough guide only.
4. **The API does not return backend search terms.** We assume the 219-246 byte strings in `listings-final.json` are live. Please check in Seller Central.
5. **"Ads" = customer search term clicks/orders from both reports.** Mapping:
   - 5L: 5L-Feeder-*, WiFi Feeder groups.
   - Camera: Camera-* groups.
   - 2L: 2L-Fountain-*.
   - Transparent: Transparent-Fountain-*.
   - Tray: 2.2L-Steel-Tray-*.
   - "shared" = the "$19.99 Fountains" / "Basic Fountains" groups, which advertise all 3 cheap fountains together, so we cannot tell which one got the click.
   - The "Veken" competitor campaign (2 orders: "dog water fountainsmall", "flowing dog water bowl") does not show which SKU it advertised, so it is not counted.
6. **"Live placement" checks:**
   - Exact phrase in the title, and whether it is in the first 80 chars (what mobile shows).
   - Exact phrase in the bullets, or in the description only.
   - "Words only" = every word is somewhere in title/bullets/description/backend, but not as the exact phrase.

---

## 0. Big picture first

| Product | ASIN | BSR Oct 4 | BSR today (Oct 12) | Sessions Oct 4-10 | Units | Conversion | Oct 4 copy live? |
|---|---|---|---|---|---|---|---|
| 5L WiFi dual feeder | B0GHH8L59K | #436 | #670 Automatic Cat Feeders | 25 | 1 | 4.0% | Yes, the full final version |
| 3L camera feeder | B0GTCGYZDM | #931 | #909 Automatic Cat Feeders | 13 | 0 | 0% | Yes, final version, but 2 attribute errors not fixed |
| 2L fountain | B0GHKN9DBR | #726 | #1,611 Cat Fountains | 33 | 3 | 9.1% | Yes (went live late, about Oct 5-11) |
| 2.2L transparent | B0GHLBGCP3 | #1,433 | #2,185 Cat Fountains | 26 | 1 | 3.8% | Yes, plus an unconfirmed "4-Layer" claim |
| 2.2L steel tray | B0GHKRYV6W | #1,327 | #2,431 Cat Fountains | 14 | 1 | 7.1% | Yes, but included_components not fixed |
| (for compare) 3.2L stainless | B0DR7FCLZR | #1,191 | (#682 on Oct 11) | 238 | 15 | 6.3% | Yes |

**What this means:**
- **All 5 new titles, bullets and descriptions are live, word for word as in `listings-final.json`.** The rewrite was applied.
- **The problem is traffic, not missing keywords.** These 5 products get 13-33 sessions a week, while the stainless fountain gets 238.
- **Their BSR fell after the old campaigns were paused on Oct 4.** Those campaigns brought 11 orders to the 2L fountain alone (Sep 30 - Oct 6). The new campaigns brought 0 orders to these 5 products (Oct 5-10).
- **Copy alone will not move BSR quickly.** We rank on page 1-2 (top ~100) only for long-tail phrases. Head terms ("automatic cat feeder", "cat water fountain") sit around #230-300 or are not ranked.
- **The fastest organic wins are:**
  - Long-tail phrases where we already sit near page 1-2 but the exact phrase is missing.
  - Ad-proven search terms.
- **The copy has heavy keyword chains** (for example "a cat automatic feeder and dog automatic feeder in one"). Those words are already indexed. These chains add nothing for ranking and can hurt conversion on mobile.

---

## 1. B0GHH8L59K: 5L WiFi dual-bowl elevated feeder (SKU QO-7VBS-CVT4)

### a) Live listing vs Oct 4 draft
- **Title (189 chars), live:** "PETME2 Automatic Cat Feeder for 2 Cats, 5L Elevated Feeding Station with WiFi App and Voice Recording, Automatic Dog Feeder, Stainless Steel Dual Bowls, Timed Pet Food Dispenser, Dual Power"
- **Mobile first 80 chars:** "PETME2 Automatic Cat Feeder for 2 Cats, 5L Elevated Feeding Station with WiFi Ap". Good: brand + #1 rank phrase + size.
- **Applied fully:** title, 5 bullets and description = `listings-final.json`.
- **Changes vs the Oct 4 draft (`drafts/feeders.json`):**
  - "Dual Power" was added back to the title. The draft had removed it until the battery backup is confirmed.
  - Bullets were extended with keyword chains.
  - All [CONFIRM] placeholders were removed, but the facts were **never added**: meals per day, portions per meal, grams per portion, cups, 2.4GHz WiFi, recording length.
- **Attributes not fixed:**
  - `special_feature` does not mention elevated, anti-jam or dual power.
  - No `material` is set.
  - `recommended_uses` still says Wet Food and Outdoor. The owner said to keep them, but the bullets say dry kibble.
- **Backend:** cannot be read by API. Expected: the final 236-byte string.

### b) Top 15 priority keywords
| # | Keyword | SV/mo | Competing | Title dens. | Our rank Oct 4 | Live placement now | Ads (clicks/orders) | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | automatic cat feeder for 2 cats | 1,059 | 2,000 | 24 | #49 | Title, first 80 | - | Best Oct 4 rank (#49), exact phrase leads the title. Protect; do not reword. |
| 2 | automatic cat feeder 2 cats | 4,741 | 2,000 | 6 | #64 | Bullets | - | Highest-SV "2 cats" phrase, page 2 (#64). Already indexed via title words. |
| 3 | elevated automatic cat feeder | 576 | 963 | 0 | #20 | Words only, no exact phrase | - | Rank #20 (page 1) with low competition (963) but the exact phrase is nowhere. Easiest win: put it in bullet 4 header/first sentence. |
| 4 | cat feeder automatic for 2 cats | 525 | 2,000 | 0 | #40 | Words only, no exact phrase | - | Rank #40 on page 1. Indexed by words only; keep "for 2 cats" next to "automatic". |
| 5 | cat feeder for 2 cats | 476 | 9,000 | 22 | #41 | Title, first 80 | - | Rank #41. Exact in title. Protect. |
| 6 | dual automatic cat feeder | 1,159 | 759 | 1 | #64 | Bullets | - | Rank #64, competition 759. True feature (2 bowls). |
| 7 | dual cat feeder automatic | 1,246 | 741 | 0 | #87 | Words only, no exact phrase | - | Rank #87, competition 741; words only. Same root as above. |
| 8 | double cat feeder | 1,156 | 3,000 | 0 | not ranked | Bullets | 3clk/1ord | Only search term with an ad order for this ASIN (3 clicks, 1 order). In bullets. |
| 9 | multi cat feeder | 882 | 4,000 | 3 | #133 | Not present (missing: multi) | - | Rank #133 but the word "multi" is missing everywhere. 2 bowls = true for 2 pets only; use "multi-cat homes" wording. |
| 10 | elevated cat feeding station | 2,101 | 2,000 | 3 | #204 | Bullets | - | Feature term (raised bowls). Rank #204. Bullet header has it; title has "Elevated Feeding Station" (missing "cat"). |
| 11 | wifi automatic cat feeder app control | 1,244 | 501 | 0 | #158 | Bullets | - | Rank #158, competition 501. In bullet 2. |
| 12 | automatic cat feeder with app | 1,768 | 495 | 5 | #186 | Bullets | - | Rank #186, competition 495. App is true. |
| 13 | timed cat feeder | 3,330 | 582 | 1 | #270 | Bullets | - | Low competition (582) for 3.3k SV. Rank #270, only in bullets. |
| 14 | cat food dispenser | 23,065 | 5,000 | 10 | not ranked | Bullets | 4clk/0ord | 23k SV, only 10 title density. Not in title (title has "Pet Food Dispenser", SV 1.6k). Ad clicks but no orders. |
| 15 | automatic cat feeder | 187,032 | 4,000 | 42 | #268 | Title, first 80 | 2clk/0ord | Head term (187k). Rank #268, so it is a long-term target only. Keep at the front of the title. |

**How to use:** keep #1, #5 and #15 exactly where they are (title). The quick wins are #3, #4, #7 and #9: we are already on page 1-2, and the copy only needs the exact phrase. Put "elevated automatic cat feeder" into bullet 4's header ("5L ELEVATED AUTOMATIC CAT FEEDER") and "multi-cat homes" into bullet 1.

### c) Wasted / risky words in the live listing
- **"not live 2-way audio"** (bullet 3 and description): writing the competitor feature "2-way audio" makes Amazon index it. Searches for 2-way audio feeders then click and don't buy. Say "records your own voice message" and drop the 2-way text.
- **"Dual Power" (title end) and "backup batteries" (bullet 5, description):**
  - Attributes say batteries are not required and not included.
  - The Oct 4 research flagged this as unconfirmed.
  - The phrase has some value ("dual power automatic cat feeder battery backup" 731 SV, rank #99), so keep it only if the owner confirms a battery compartment. If not, remove it everywhere.
- **"Timed Pet Food Dispenser" (title):** "timed pet food dispenser" has SV 39 and "pet food dispenser" 1.6k.
  - "cat" is already used 2 times in the title (cat + cats), so "Cat Food Dispenser" cannot go there.
  - Option: "Dog Food Dispenser" (8.8k). "dog" is used 1 time, so this stays within the 2-times rule.
- **Keyword chains with no new words:**
  - "cat food feeder and dog food feeder, a cat automatic feeder and dog automatic feeder in one" (bullet 5).
  - "Set a dog feeder automatic schedule once" (bullet 3).
  - "It is an automatic cat feeder 2 cats can share" (bullet 1).
  - Description lines such as "cat food automatic feeder and auto pet feeder in one" and "pet feeder automatic schedule".
  - Every word is already indexed. Replace this text with the missing facts (meals/day, grams, cups) once the owner confirms them.
- **Attribute `recommended_uses`: "Wet Food", "Outdoor"** is wrong for a dry-kibble feeder with an adapter. It risks bad clicks from "wet food"/"outdoor feeder" searches (we filtered both out as wrong product types).
- **Title repeat check:** automatic 2, cat 2, feeder 2, dual 2. At the limit, no word appears more than 2 times. No emojis or banned symbols.
- **Backend (if the final string is live):** 14 of its words are already in the title/bullets and waste bytes: auto, backup, control, double, dry, kibble, meal, portion, raised, schedule, self, smart, timer, two.

### d) Gaps (relevant, high-value, exact phrase nowhere)
| Keyword | SV | Competing | Our rank Oct 4 | Now | Note |
|---|---|---|---|---|---|
| elevated automatic cat feeder | 576 | 963 | #20 | words only | Top gap: page 1 already |
| automatic cat feeder 2 bowls | 365 | 1,000 | #71 | words only | True |
| auto cat feeder for 2 cats | 493 | 936 | #93 | words only | True |
| multi cat feeder / multiple cat feeder | 882 / 785 | 4,000 / 5,000 | #133 / - | "multi" missing | Use "multi-cat homes" |
| automatic cat feeder stainless steel bowl | 350 | 1,000 | #115 | words only | True |
| cat food dispenser for 2 cats | 464 | 2,000 | #116 | words only | True |
| automatic dog feeder for 2 dogs | 369 | 2,000 | #115 | words only | Small dogs only |
| automatic cat feeder programmable / with timer | 977 / 583 | 631 / 598 | - | words only | True |
| large capacity automatic cat feeder | 215 | 1,000 | #175 | words only | 5L is true |
| automatic feeder cat dry food | 3,330 | 1,000 | #242 | words only | True (dry only) |

Do not add: camera, 2-way audio, night vision, wet food, outdoor, 3 cats, "slow feeder", competitor brands.

---

## 2. B0GTCGYZDM: 3L camera feeder (SKU 2H-2T1T-CJC3)

### a) Live listing vs Oct 4 draft
- **Title (191 chars), live:** "PETME2 Automatic Cat Feeder with Camera, 3L WiFi Cat Food Dispenser with 1080P HD Video and 2-Way Audio, App Control, Automatic Dog Feeder for Small Dogs, Timed Portions, Anti-Jam, Dual Power"
- **Mobile first 80 chars:** "PETME2 Automatic Cat Feeder with Camera, 3L WiFi Cat Food Dispenser with 1080P H". Good.
- **Copy applied fully** (= final). Emojis removed (good).
- **Changes vs the Oct 4 draft:**
  - ", Dual Power" was added to the end of the title.
  - The draft phrases "pet feeder with camera and two-way audio" and "smart automatic dog feeder with camera" were dropped, so the exact phrase **"pet feeder with camera" (rank #140) is lost.**
  - Facts never added: night vision yes/no, meals/day, grams, 2.4GHz, what is in the box.
- **Attributes NOT fixed (both were on the Oct 4 list):**
  - `special_feature` still says "Feed your cat or small dog at the same time with balanced portions". That text was copied from the dual feeder and is wrong for a single bowl.
  - `included_components` lists only "Main Unit".
  - No `material` is set.

### b) Top 15 priority keywords
| # | Keyword | SV/mo | Competing | Title dens. | Our rank Oct 4 | Live placement now | Ads (clicks/orders) | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | automatic cat feeder with camera | 6,417 | 521 | 30 | #121 | Title, first 80 | 3clk/0ord | Main feature term (6.4k SV, competition 521). Rank #121, exact in title. Ads: 3 clicks, 0 orders on this exact search term. |
| 2 | cat feeder with camera | 2,519 | 527 | 31 | #127 | Title, first 80 | - | Rank #127. Exact in title. |
| 3 | automatic dog feeder with camera | 977 | 419 | 4 | #102 | Bullets | 2clk/0ord | Rank #102. In bullet 1. Exact ad: 2 clicks, 0 orders. |
| 4 | cat food dispenser with camera | 605 | 438 | 0 | #86 | Words only, no exact phrase | 1clk/0ord | Rank #86, competition 438. Words only: the title says "Cat Food Dispenser with 1080P HD Video". Writing "with Camera" there gives the exact phrase. |
| 5 | automatic cat feeder with camera 1080p | 564 | 441 | 0 | #86 | Words only, no exact phrase | - | Rank #86. The 1080p fact is true; words only now. |
| 6 | wifi cat feeder with camera | 250 | 446 | 0 | #95 | Words only, no exact phrase | - | Rank #95, competition 446. Words only. |
| 7 | dog feeder with camera | 574 | 438 | 5 | #119 | Bullets | - | Rank #119. In bullets ("automatic dog feeder with camera"). |
| 8 | pet feeder with camera | 782 | 720 | 0 | #140 | Words only, no exact phrase | 1clk/0ord | Rank #140. Words only (the Oct 4 draft had it; the published version dropped the exact phrase). 1 ad click. |
| 9 | automatic cat feeder camera | 612 | 509 | 0 | #124 | Words only, no exact phrase | - | Rank #124. Close variant, covered by the title words. |
| 10 | auto cat feeder with camera | 586 | 478 | 0 | #132 | Words only, no exact phrase | - | Rank #132. Words only. Add "auto" next to camera once in a bullet. |
| 11 | automatic pet feeder with camera | 615 | 723 | 0 | #151 | Words only, no exact phrase | - | Rank #151. Words only. |
| 12 | auto cat feeder | 8,838 | 1,000 | 1 | #160 | Bullets | - | Best generic rank (#160) with lower competition (1,000). |
| 13 | cat food dispenser | 23,065 | 5,000 | 10 | not ranked | Title, first 80 | 1clk/0ord | 23k SV, in the title. No rank. 1 ad click. |
| 14 | timed cat feeder | 3,330 | 582 | 1 | #242 | Bullets | - | Competition 582, rank #242. |
| 15 | automatic cat feeder | 187,032 | 4,000 | 42 | #271 | Title, first 80 | 2clk/0ord | Head term; rank #271. Keep at the front of the title. |

**How to use:**
- **Title fix:** change "3L WiFi Cat Food Dispenser with 1080P HD Video" to "3L WiFi Cat Food Dispenser with Camera, 1080P HD Video". That gains the exact #4 (rank #86) and still covers #5. It would put "camera" 2 times in the title: allowed.
- **Bullets:** put "pet feeder with camera" and "wifi cat feeder with camera" into bullet 1 or 2.
- All camera long-tails sit at #86-#151, our closest to page 1. The generic terms are #160-#300.

### c) Wasted / risky words in the live listing
- **Attribute `special_feature`:** dual-feeding text on a single-bowl feeder. This is a wrong claim; fix it.
- **"feeding station" text** in bullet 1 ("a tidy cat feeding station") and bullet 5 ("small dog feeding station or pet feeding station"): feeding station searches are mostly for bowl stands and dual setups. Low fit for a single-bowl camera feeder.
- **Keyword chains in bullet 5 and the description** ("a cat automatic feeder and dog automatic feeder in one", "cat food automatic feeder and auto pet feeder in one", "dog food dispenser automatic schedule"): no new words.
- **"Dual Power" / "switches to backup batteries"**: attributes say batteries are not required and not included. Keep only if confirmed. The value is small ("automatic cat feeder battery backup" 415 SV, rank #241).
- **"Anti-Jam", "Timed Portions" in the title:** these phrases have almost no SV. "Anti-Jam" is a real feature and a fine differentiator. If space is needed for "Night Vision" (only if true), drop these first.
- **Title repeat check:** automatic 2, cat 2, feeder 2, dog 2, with 2. OK.
- **Backend (if final is live):** 20 words repeat the front end: auto, backup, dry, electric, feeding, kibble, kitty, live, meal, pet, phone, programmable, puppy, schedule, self, smart, station, talk, timer, view.

### d) Gaps
| Keyword | SV | Competing | Our rank Oct 4 | Now | Note |
|---|---|---|---|---|---|
| cat food dispenser with camera | 605 | 438 | #86 | words only | Title tweak above |
| automatic cat feeder with camera 1080p | 564 | 441 | #86 | words only | True |
| dog feeder and camera | 159 | 365 | #85 | words only | Small |
| wifi cat feeder with camera | 250 | 446 | #95 | words only | True |
| cat automatic feeder with camera | 228 | 558 | #105 | words only | |
| cat feeder camera / camera cat feeder | 518 / 166 | 375 / 481 | #117 / #116 | words only | |
| pet feeder with camera | 782 | 720 | #140 | words only (lost in final) | Re-add |
| automatic dog feeder with wifi | 334 | 537 | #135 | words only | True |
| night vision (camera feeder long-tail) | n/a | n/a | n/a | not present | **Only if true.** 6 of 8 competitors claim it. Ask the owner. |

Do not add: "2 cats", "dual", "double", "multi", "elevated", "voice recording" (single bowl, not this model), competitor brands.

---

## 3. B0GHKN9DBR: 2L fountain (SKU L6-L3S1-I7Q6)

### a) Live listing vs Oct 4 draft
- **Title (179 chars), live:** "PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Light Low Level Alert, Visible Window, Anti-Dry Pump Shut-Off, Small Pet Dispenser for Kitten and Dog"
- **Mobile first 80 chars:** "PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Li". Very good.
- **Applied fully.** The title is identical to the Oct 4 draft. Bullets and description = final.
- **This listing went live later than the others** (learnings.md: still old on Oct 4; rank-check Oct 11: live). It has the least "SEO time".
- **No filter claims anywhere.** That is correct, because the in-box list has no filter.
- **Attribute `special_feature` "2L Portable Water Capacity"** and the description "slim, portable white body": "portable" suggests cordless. The unit is corded (AC100-240V / DC5V).

### b) Top 15 priority keywords
| # | Keyword | SV/mo | Competing | Title dens. | Our rank Oct 4 | Live placement now | Ads (clicks/orders) | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | plastic cat water fountain | 1,883 | 2,000 | 0 | #29 | Bullets | - | Our best fountain rank (#29). True (plastic). In bullet 4. Protect it. |
| 2 | cat water fountain plastic | 518 | 2,000 | 0 | #31 | Words only, no exact phrase | - | Rank #31. Indexed by words. Protect. |
| 3 | water fountains for cats indoor quiet | 357 | 4,000 | 0 | #52 | Words only, no exact phrase | - | Rank #52 on long tail. Title words cover it; keep "Quiet" next to "Water Fountains for Cats Indoor". |
| 4 | compact cat water fountain | 213 | 1,000 | 0 | #83 | Words only, no exact phrase | - | Rank #83, low SV. True (slim/compact). |
| 5 | pet water fountains for cats and dogs | 335 | 4,000 | 0 | #87 | Words only, no exact phrase | - | Rank #87. Words only. |
| 6 | cat water fountain with led indicator | 1,246 | 786 | 0 | #112 | Not present (missing: led) | - | Rank #112, competition 786. The red low-water light is true; ask the owner whether it is an LED. If yes, write "LED low water indicator". |
| 7 | small cat water fountain | 1,768 | 5,000 | 0 | #128 | Bullets | 1clk/1ord | Rank #128, and it had an ad order (1 click, 1 order). In bullet 4. |
| 8 | quiet cat water fountain | 1,594 | 2,000 | 0 | #143 | Bullets | 1clk/0ord | Rank #143. In bullet 4. The same term sold the tray fountain via ads. |
| 9 | running water bowl for cats | 1,159 | 1,000 | 0 | #158 | Bullets | - | Rank #158, competition 1,000. In bullet 1. |
| 10 | water fountains for cats indoor | 49,512 | 2,000 | 2 | #236 | Title, first 80 | - | 49.5k SV, title density only 2. Rank #236. Exact in title (first 80 chars). |
| 11 | cat water dispenser | 17,542 | 6,000 | 8 | #254 | Bullets | 3clk/1ord; shared 1clk/0ord | Ad proven: 3 clicks, 1 order (old campaign). Rank #254. |
| 12 | cat water bowl | 27,400 | 10,000 | 5 | not ranked | Bullets | 14clk/1ord | Ad proven: 14 clicks, 1 order. It is a broad term, so bullets only. |
| 13 | kitten water fountain | 2,502 | 1,000 | 0 | #277 | Bullets | - | Competition 1,000, rank #277. In bullet 1. |
| 14 | cat water fountain | 319,141 | 5,000 | 46 | not ranked | Title, first 80 | 4clk/0ord | Head term (319k), first in the title. Not ranked. 4 ad clicks, 0 orders. |
| 15 | dog water fountain | 97,595 | 4,000 | 31 | not ranked | Bullets | shared 1clk/0ord | 97.6k SV. Only in bullet 4 (as "small dog water fountain"/"for small dogs"), not in the title. No rank. |

**How to use:**
- **Protect #1-#3:** keep "plastic cat water fountain" in a bullet, and keep "Quiet Water Fountains for Cats Indoor" in the title.
- **Biggest cheap win:** if the red light is an LED (ask the owner), change the title's "Red Light Low Level Alert" to "LED Low Water Indicator". The exact phrase is "cat water fountain with led indicator" (1,246 SV, rank #112, low competition 786).
- **Title has no "Dog Water Fountain" (97.6k):** "Small Pet Dispenser for Kitten and Dog" (no SV) could become "Small Dog Water Fountain for Kittens". "Water" is then used 3 times, which breaks the 2-times rule, so write it as "Small Dog Fountain for Kittens", or drop "Visible Window".

### c) Wasted / risky words in the live listing
- **"Small Pet Dispenser for Kitten and Dog"** (title, 38 chars): "small pet dispenser" is not a search phrase in Cerebro. Weak use of title space.
- **"Visible Window"** (title): no SV. The visible level is a true benefit; keep it in bullet 2 only.
- **"Red Light Low Level Alert"** (title): no SV as a phrase. See the LED note above.
- **"portable"** (description, attribute) and **"light and easy to move"** (bullet 4) suggest a cordless unit.
  - Ads show about 10 clicks on cordless/wireless/rechargeable searches for this ASIN, and only 1 order ("wireless water fountain for cats").
  - Prefer "compact". Never claim cordless.
- **Keyword chains:** bullet 3 ("a water dispenser for dogs that will not run the pump empty, a cat or dog automatic water dispenser in one"), bullet 5, and description reorders ("fountain dog water bowl", "dog bowl fountain or fountain dog water bowl", "fountain cat water bowl"). No new words; they read as spam.
- **Title repeat check:** cat 2, water 2, fountain 2 (fountain + fountains), for 2. OK, at the limit.
- **Backend (if final is live):** 18 words repeat the front end: auto, automatic, bedroom, bowl, circulating, clean, compact, drinking, easy, flowing, fresh, indicator, inside, kitty, plastic, refill, running, slim.

### d) Gaps
| Keyword | SV | Competing | Our rank Oct 4 | Now | Note |
|---|---|---|---|---|---|
| cat water fountain with led indicator | 1,246 | 786 | #112 | "led" missing | Only if the red light is LED |
| dog water fountain small size dog | 561 | 3,000 | #145 | "size" missing | Backend word "size" |
| dog water bowl fountain small breed | 418 | 786 | #131 | "breed" missing | Backend word "breed" |
| puppy water fountain | 407 | 2,000 | #158 | "puppy" missing | Backend word "puppy" (small/medium dogs are in the attributes) |
| cat water fountain white | 354 | 1,000 | #132 | words only | True (white). The ad search "white cat water fountain" got 1 click, 1 order |
| cat water fountain for 2 cats | 275 | 10,000 | #90 | "2" missing | Fine for 2 cats at 2L |
| ultra quiet cat water fountain | 569 | 1,000 | - | "ultra" missing | Only if a dB value supports it |
| fonte de agua para gatos (Portuguese) | n/a | n/a | n/a | missing | 1 ad order on Oct 1-6. Add "fonte" to the backend |
| **filterless cat water fountain / cat water fountain no filter / cat fountain no filter needed** | **11,089 / 5,955 / 4,088** | 934 / 1,000 / 932 | - | missing | **CONDITIONAL.** Use only if the owner confirms the 2L has NO filter (the in-box list shows none). Ads: 3 clicks on "no filter / without filter" searches, 0 orders. This would be the biggest new niche for this ASIN. |

Do not add: filter/filtration (unless confirmed), stainless, steel, metal, ceramic, wireless, cordless, battery, smart, app, outdoor, large dog.

---

## 4. B0GHLBGCP3: 2.2L transparent fountain (SKU SD-85ET-IOZ3)

### a) Live listing vs Oct 4 draft
- **Title (192 chars), live:** "PETME2 Transparent Cat Water Fountain 74oz/2.2L, 4-Layer Filtered Cat Water Dispenser with Quiet Pump, Clear Tank Shows Level, Anti-Dry Protection, Automatic Pet Fountain for Small Dogs Indoor"
- **Mobile first 80 chars:** "PETME2 Transparent Cat Water Fountain 74oz/2.2L, 4-Layer Filtered Cat Water Disp". Good: exact "cat water fountain" plus size.
- **Copy applied** (= final). It differs from the Oct 4 draft in 3 places that the draft said must be confirmed first:
  1. **"4-Layer" was added** to the title, bullet 2 and description. The draft said "built-in filter cartridge" only, and to add 4-layer only after the owner confirms it. Live `special_feature` still says only "Built-In Filter Cartridge". **Confirm with the owner, or remove "4-Layer".**
  2. **"USB powered"** (bullet 5, description) vs `power_source_type` "AC100-240V DC5V". The draft used "low-voltage power cable" because of this conflict.
  3. **"Covered by a 1-year limited warranty"** was added. The draft said to confirm first.
- **Attribute `dog_breed_size` = extra_small only**, while the copy says small dogs.

### b) Top 15 priority keywords
| # | Keyword | SV/mo | Competing | Title dens. | Our rank Oct 4 | Live placement now | Ads (clicks/orders) | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | plastic cat water fountain | 1,883 | 2,000 | 0 | #92 | Bullets | - | Rank #92. In bullet 1 ("clear plastic cat water fountain"). True. |
| 2 | dog water fountain small size dog | 561 | 3,000 | 0 | #87 | Not present (missing: size) | - | Rank #87, but the word "size" is missing. Low SV. |
| 3 | dog water fountain for small dogs | 1,870 | 3,000 | 0 | #110 | Bullets | - | Rank #110, competition 3,000. In bullet 1. |
| 4 | dog water bowl fountain small breed | 418 | 786 | 0 | #111 | Not present (missing: breed) | - | Rank #111, competition only 786. The word "breed" is missing. |
| 5 | flowing cat water bowl | 557 | 1,000 | 0 | #129 | Words only, no exact phrase | - | Rank #129. Words only. |
| 6 | running water bowl for cats | 1,159 | 1,000 | 0 | #145 | Bullets | - | Rank #145. In bullet 3. |
| 7 | kitten water fountain | 2,502 | 1,000 | 0 | #228 | Bullets | - | Rank #228, competition 1,000. In bullet 1. |
| 8 | automatic water dispenser for cats | 8,819 | 3,000 | 2 | #249 | Bullets | 2clk/1ord | Rank #249. Ad proven: 1 order (old campaign). |
| 9 | cat water dispenser | 17,542 | 6,000 | 8 | #266 | Title (after 80) | 9clk/0ord; shared 1clk/0ord | Rank #266, exact in title. 10 ad clicks, 0 orders. |
| 10 | cat water fountain | 319,141 | 5,000 | 46 | #293 | Title, first 80 | 6clk/1ord | Rank #293, exact in the first 80 chars. Old campaign: 1 order from 6 clicks. |
| 11 | dog water fountain | 97,595 | 4,000 | 31 | #269 | Bullets | 1clk/0ord; shared 1clk/0ord | Rank #269. Not in the title as an exact phrase. |
| 12 | water fountains for cats indoor | 49,512 | 2,000 | 2 | #285 | Bullets | - | Rank #285. Bullet 3 only. |
| 13 | cat water fountain with filtration | 4,522 | 3,000 | 0 | #302 | Bullets | - | Filter is true (cartridge included). Rank #302. Bullet 2. |
| 14 | filtered dog water fountain | 2,944 | 3,000 | 0 | not ranked | Bullets | - | Filter is true. Not ranked. Bullet 2. |
| 15 | small dog water fountain | 2,529 | 5,000 | 1 | not ranked | Bullets | 2clk/0ord | Not ranked. Bullet 1. 2 ad clicks, 0 orders. |

**How to use:**
- **#2 and #4 are near page 1** and need only one backend word each: "size" and "breed".
- **#1, #3, #5 and #6 are page 2-3 long-tails.** Keep them in the bullets.
- **The title lacks "dog water fountain" (rank #269) as an exact phrase.** "Automatic Pet Fountain for Small Dogs Indoor" (SV 36 for "automatic pet fountain") could become "Dog Water Fountain for Small Dogs Indoor". Check the 2-times rule for "water": the title already has it 2 times. So use "Dog Fountain for Small Dogs" (dog fountain 4.7k) instead.

### c) Wasted / risky words in the live listing
- **"4-Layer"**: unconfirmed claim (see a). This is a compliance risk, not a keyword gain.
- **"Transparent" + "Clear Tank Shows Level"** say the same thing twice. Cerebro shows no search volume for "transparent cat water fountain" or "clear cat water fountain". Keep one as the differentiator. "Clear Tank Shows Level" (22 chars) is the better one to cut.
- **"Automatic Pet Fountain"** (SV 36) vs "pet water fountain" (42k, bullets only).
- **"Filtered Cat Water Dispenser"**: no SV as a phrase. It does hold "cat water dispenser" (17.5k).
- **"USB powered"**: possibly wrong (see a).
- **Keyword chains** in bullet 5 ("an automatic dog water bowl or an automatic water bowl for dogs, a cat or dog automatic water dispenser in one") and in the description ("dog bowl fountain or fountain dog water bowl").
- **Ads:** "no filter" searches got 6 clicks and 1 order on the old campaign. These searches are irrelevant for a filter fountain. Ads team: add negatives ("no filter", "filterless", "without filter"), unless the order proves otherwise.
- **Title repeat check:** cat 2, water 2, fountain 2. OK.
- **Backend (if final is live):** 16 words repeat the front end: bedroom, bowl, circulating, dish, drinking, easy, filtration, flowing, fresh, inside, kitten, kitty, plastic, running, see, system.

### d) Gaps
| Keyword | SV | Competing | Our rank Oct 4 | Now | Note |
|---|---|---|---|---|---|
| capsule water fountain for cats | 251 | 675 | **#14** | "capsule" missing | **Only if the body is capsule-shaped.** Check the main image. We already rank #14 without the word |
| dog water fountain small size dog | 561 | 3,000 | #87 | "size" missing | Backend |
| dog water bowl fountain small breed | 418 | 786 | #111 | "breed" missing | Backend |
| running water for cats | 513 | 4,000 | #124 | words only | |
| dog water fountain with filter | 977 | 3,000 | #248 | words only | True |
| filtered pet water fountain | 882 | 4,000 | - | words only | True |
| cat water fountain with filter | 731 | 4,000 | - | words only | True |
| quiet dog water fountain | 663 | 1,000 | - | words only | True |
| puppy water fountain | 407 | 2,000 | - (2L #158) | "puppy" missing | Backend |

Do not add: stainless/steel/metal, LED (unless this model has a low-water light; the draft asked and it is not confirmed), "no filter", wireless/cordless/battery, smart/app, ceramic, large dog. Do not add replacement-filter phrases ("cat water fountain filter" 34k, "cat fountain filter" 23k): those shoppers want spare filters, not a fountain.

---

## 5. B0GHKRYV6W: 2.2L fountain with stainless steel tray and filters (SKU JE-LQEW-9EHL)

### a) Live listing vs Oct 4 draft
- **Title (170 chars, 30 unused), live:** "PETME2 Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Automatic Pet Fountain for Cats and Dogs, 4-Layer Filtration, Filters Included, Low Water Alert, Quiet Pump"
- **Mobile first 80 chars:** "PETME2 Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Automatic Pet Fou". Good: exact head term, honest steel wording, size.
- **Copy applied** (= final). Changes vs the Oct 4 draft:
  - Title "Automatic Water Dispenser for Cats and Dogs" became "Automatic Pet Fountain for Cats and Dogs". This lost the exact title phrase "automatic water dispenser for cats" (8.8k; now in bullets only) for a phrase with SV 36.
  - "Filter Included" became "Filters Included" (plural). The filter count is still unconfirmed.
  - "Red Light Alert" became "Low Water Alert".
  - Bullet 1 got contrived lines: "a cat water fountain, stainless steel tray included, and a cat fountain, stainless steel tray and all".
- **Attributes NOT fixed (on the Oct 4 list):**
  - `included_components` still holds feature text ("2.2L Portable Water Capacity...") and lists no filter, even though the title says "Filters Included".
  - `special_feature` has only "Stainless Steel Tray Design".
  - `material` lists Stainless Steel before Plastic.
- **No organic rank data at all.**

### b) Top 15 priority keywords
| # | Keyword | SV/mo | Competing | Title dens. | Our rank Oct 4 | Live placement now | Ads (clicks/orders) | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | quiet cat water fountain | 1,594 | 2,000 | 0 | no data (sister: 2L #143, clear #299) | Words only, no exact phrase | 2clk/1ord | The ONLY ad order for this ASIN (2 clicks, 1 order). The exact phrase is missing ("quiet cat fountain", "Quiet Pump"). Put it in the title. |
| 2 | cat water fountain with led indicator | 1,246 | 786 | 0 | no data (sister: 2L #112, clear #187) | Not present (missing: led indicator) | 1clk/0ord | The old ad group was built on it (1 click). The red light alert is true per the old listing; confirm it is an LED. Sister 2L is #112. |
| 3 | small cat water fountain | 1,768 | 5,000 | 0 | no data (sister: 2L #128) | Bullets | - | Sister 2L ranks #128. In bullet 5. |
| 4 | kitten water fountain | 2,502 | 1,000 | 0 | no data (sister: 2L #277, clear #228) | Bullets | 1clk/0ord | Competition 1,000. Bullet 5. 1 ad click. |
| 5 | dog water fountain for small dogs | 1,870 | 3,000 | 0 | no data (sister: 2L #211, clear #110) | Bullets | - | Sister clear fountain ranks #110. Bullet 5. |
| 6 | cat water fountain with filtration | 4,522 | 3,000 | 0 | no data (sister: clear #302) | Bullets | - | 4-layer filter is true. Bullet 2. |
| 7 | filtered dog water fountain | 2,944 | 3,000 | 0 | no data | Bullets | - | Bullet 2. Competition 3,000. |
| 8 | water fountains for cats indoor | 49,512 | 2,000 | 2 | no data (sister: 2L #236, clear #285) | Bullets | 4clk/0ord | 49.5k SV, title density 2. Bullet 5 only. 4 ad clicks, 0 orders. |
| 9 | cat water dispenser | 17,542 | 6,000 | 8 | no data (sister: 2L #254, clear #266) | Bullets | shared 1clk/0ord | Bullet 2. Sisters rank #254/#266. |
| 10 | automatic water dispenser for cats | 8,819 | 3,000 | 2 | no data (sister: 2L #257, clear #249) | Bullets | - | Bullet 3. |
| 11 | pet water fountain | 42,109 | 7,000 | 10 | no data | Description only | 1clk/0ord | 42k SV. Description only; the title says "Automatic Pet Fountain" (SV 36). |
| 12 | cat fountain | 83,521 | 6,000 | 13 | no data | Bullets | 4clk/0ord | 83.5k SV, title density 13. Bullet 1. 4 ad clicks, 0 orders. |
| 13 | dog water fountain | 97,595 | 4,000 | 31 | no data (sister: clear #269) | Bullets | shared 1clk/0ord | 97.6k SV. Bullet 5 ("dog water fountain for small dogs"). Not in the title. |
| 14 | cat water fountain | 319,141 | 5,000 | 46 | no data (sister: clear #293) | Title, first 80 | 1clk/0ord | Head term, exact at the front of the title. 1 ad click. |
| 15 | cat water fountain stainless steel | 79,303 | 2,000 | 21 | no data | Bullets | 1clk/0ord | Big SV, but only the TRAY is steel. Only use it as "with stainless steel tray" wording. Ads: about 10 clicks on stainless searches, 0 orders. Low priority. |

**How to use:**
- **#1 is the only search term that ever sold this ASIN through ads.** Put the exact "Quiet Cat Water Fountain" in the title. There are 30 free chars, or replace "Quiet Pump".
- **Then:** "LED indicator" if true, and "Pet Water Fountain" in place of "Automatic Pet Fountain".
- **Keep the stainless wording honest ("with Stainless Steel Tray").** Do not chase "stainless steel cat water fountain" head terms. Ads gave about 10 clicks on those searches and 0 orders. A shopper who wants an all-steel fountain will bounce or return it.

### c) Wasted / risky words in the live listing
- **Contrived stainless lines:**
  - Bullet 1: "a cat water fountain, stainless steel tray included, and a cat fountain, stainless steel tray and all".
  - Description: "For dogs, it is a dog water fountain, stainless steel tray included".
  - These are keyword stuffing that pulls all-steel-fountain shoppers who do not convert. They read badly. Replace them with one clear sentence.
- **"Automatic Pet Fountain"** (title): SV 36. "pet water fountain" (42k) is only in the description.
- **"Filters Included"** (title, bullet 2): no count is given, and `included_components` lists no filter. Fix the attribute and add the real count ("2 Filters Included" if true; it is also a competitor hook).
- **"food-grade materials"** (description): not in the Oct 4 facts. Confirm it or remove it.
- **Keyword chains** in bullets 3-4 ("an automatic water dispenser for dogs and a water dispenser for dogs") and in the description ("dog fountain water bowl and dog water bowl fountain").
- **Title repeat check:** cat 2, water 2, fountain 2. OK.
- **Backend (if final is live):** 15 words repeat the front end (bowl, clean, dispenser, drinking, easy, filtered, indoor, inside, kitten, level, plastic, refill, running, small, window). "metal" in the backend is risky for a plastic body; "acero inoxidable" is fine only for the tray.

### d) Gaps
| Keyword | SV | Competing | Sister rank (2L / clear) | Now | Note |
|---|---|---|---|---|---|
| quiet cat water fountain | 1,594 | 2,000 | #143 / #299 | words only | Only ad order (2 clicks, 1 order). Top gap |
| cat water fountain with led indicator | 1,246 | 786 | #112 / #187 | "led indicator" missing | Only if the red light alert is LED |
| running water bowl for cats | 1,159 | 1,000 | #158 / #145 | words only | True |
| dog water fountain with filter | 977 | 3,000 | - / #248 | words only | True |
| filtered pet water fountain | 882 | 4,000 | - | words only | True |
| cat water fountain with filter | 731 | 4,000 | - | words only | True |
| quiet dog water fountain | 663 | 1,000 | - | words only | True |
| kitten fountain | 532 | 1,000 | #152 / #172 | words only | True |
| puppy water fountain | 407 | 2,000 | #158 / - | "puppy" missing | Backend |

Do not add: "stainless steel cat water fountain" as a product claim, "metal fountain", "no filter", wireless/cordless/battery, smart/app, ceramic, large dog.

---

## 6. The fresh Helium 10 export we need (to replace the Oct 3/4 ranks)

1. **Cerebro, fountains run (most urgent).** Enter **B0GHKRYV6W, B0GHKN9DBR, B0GHLBGCP3, B0DR7FCLZR** plus the same 5 competitors as the Oct 4 file (B08NC54VZN, B0FPFZ3C5K, B0FDKQGRCK, B0FJMBNZQ1, B0C8MHHVPC). Amazon US, no filters. Export CSV.
   - It gives a per-ASIN organic rank column for each of our fountains, comparable 1:1 with `cerebro-fountains-B0DR7FCLZR.csv`.
   - It is the **first-ever rank data for B0GHKRYV6W**.
2. **Cerebro, feeders run.** Enter **B0GHH8L59K, B0GTCGYZDM, B0GHLSQMJ9** plus the same competitors as the Oct 4 file (B09S8WMJY9, B0B5ZGGWBQ, B0953SDCRG, B0C5X2G933, B0DCNNN5FC). Export CSV. This is comparable with `cerebro-feeders-B0GHLSQMJ9.csv`.
3. **Keyword Tracker (best for weekly checks).** Add the 75 keywords in `keywords.json` (15 per ASIN) plus the gap phrases. Track each on its own ASIN.
   - Cerebro is one snapshot and caps at about #306. Tracker gives daily organic + sponsored rank history.
   - Export the Tracker CSV each Monday.

Send the exports to `research/helium10/` with the date in the file name (for example `cerebro-fountains-2026-10-13.csv`). Then the before/after can be measured per keyword.

---

## 7. Summary (10 lines)
1. All 5 rewrites from Oct 4 are live word for word (`listings-final.json`). The SEO copy was applied. The problem is traffic: 13-33 sessions a week each, vs 238 for the stainless fountain.
2. BSR fell for 4 of the 5 mainly because the old ad campaigns (11 orders on the 2L alone, Sep 30 - Oct 6) were paused. New campaigns brought 0 orders to these 5 products (Oct 5-10).
3. Ranks are from Oct 3/4 (before the rewrite). We need 2 new Cerebro runs (fountains incl. B0GHKRYV6W, and feeders) plus Keyword Tracker on the 75 keywords to know the current ranks.
4. 5L feeder: protect "automatic cat feeder for 2 cats" (#49). Quick win: "elevated automatic cat feeder", rank #20, missing as a phrase. Remove the "2-way audio" text; confirm "Dual Power".
5. Camera feeder: write "Cat Food Dispenser with Camera" in the title (rank #86 phrase) and re-add "pet feeder with camera". Fix the wrong `special_feature` (dual-feeding text) and `included_components`.
6. 2L fountain: protect "plastic cat water fountain" (#29). Replace the no-SV title words ("Small Pet Dispenser", "Visible Window"). If the light is an LED, use "LED indicator" (#112). The "filterless" niche (11k) is open only if the owner confirms there is no filter.
7. Transparent fountain: "4-Layer" and "USB powered" are unconfirmed claims; confirm or remove. Cheap backend wins: "size", "breed", "puppy". Check whether it is capsule-shaped (we rank #14 for "capsule water fountain for cats").
8. Steel-tray fountain: its only converting search is "quiet cat water fountain". Put that exact phrase in the title (30 chars free). Remove the contrived "stainless steel tray and all" lines. Fix `included_components` and the filter count.
9. All 5 listings carry keyword chains that add no new words and hurt mobile reading. Replace them with the missing facts: meals/day, grams, cups, filter count, dB, LED, night vision (only what the owner confirms).
10. Backend strings repeat 14-20 front-end words each. Free those bytes for the gap words (elevated, multi, size, breed, puppy, fonte, led) after confirming in Seller Central what is actually live.
