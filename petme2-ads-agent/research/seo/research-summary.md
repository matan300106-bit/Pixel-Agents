# PETME2 SEO research for the listing rewrite (2026-10-04)

Analyst, read only. Sources: SP-API Catalog Items 2022-04-01 (US), pulled 2026-10-04, saved in `current-listings.json`. Helium 10 Cerebro exports in `research/helium10/` (4 files, 14.4k unique phrases), filtered into `keyword-banks.json`.

**How the keyword bank was built.** Phrases were deduped (highest SV kept). We removed: competitor brands (petlibro, petsafe, catit, veken, petkit, furbo, selene, kitty spout, pure stream, voluas, fluff trough, etc.); other product types (litter, slow/puzzle/gravity/wet/treat feeders, bowls and containers, replacement filters/pumps, wireless/battery/ceramic/heated/outdoor fountains, birds and other animals); and features the product does not have (camera on non-camera feeders; "2 cats"/dual on the single-bowl camera feeder; stainless on the plastic fountains; filters on the 2L B0GHKN9DBR; "filterless/no filter" on fountains that have a filter; "smart/app/wifi" on all fountains). "Our rank" = Cerebro organic rank (only ranks of 300 or better are shown; "-" = not ranked or not measured). Rank columns exist only for B0GHLSQMJ9, B0GTCGYZDM, B0GHH8L59K, B0DR7FCLZR, B0GHKN9DBR and B0GHLBGCP3. **B0GHMCG8Q9 (black) and B0GHKRYV6W have no rank data.**

**Rank reality.** Across each product's top 60 keywords, we have only 0-5 top-100 positions. Best: B0GHKN9DBR #29 "plastic cat water fountain". B0GHH8L59K #49 "automatic cat feeder for 2 cats". B0GHLSQMJ9 #62 "automatic cat feeder 2 cats". B0GTCGYZDM #102 "automatic dog feeder with camera". For the head terms ("automatic cat feeder" 187k, "cat water fountain" 319k), every one of our ASINs is at about #230-300 or not ranked at all.

**General gaps (all listings).**
- The Catalog API does not return backend search terms (`generic_keyword`). Check them in Seller Central. Each JSON bank has a ready `suggested_backend_string_249b`.
- No titles use the exact top phrase in order ("automatic cat feeder" is at the front only on the parent; "cat water fountain" is split into "Cat Water Fountain," only on B0GHKN9DBR).
- All titles are 187-200 chars. Amazon's limit is 200 and it suppresses words repeated more than twice in the title. Mobile shows about 80 chars, so the first 80 chars must carry the head keyword plus the key differentiator.
- Spanish search terms (e.g. "fuente de agua para gatos" 8.8k, "comedero automatico gatos" 3.3k) are not used anywhere. Add them to the backend.
- The camera feeder bullets start with emojis. Amazon's bullet guidelines ban emojis and special characters, so remove them.

---
## Facts and contradictions per product (from listing and attributes only)

### B0GHLSQMJ9 (white, SKU LW-EZAJ-KKZD) and B0GHMCG8Q9 (black, SKU 93-E8EG-20UY). Parent B0H3L6VXV6, variation theme COLOR
- Current title, white (192 chars): "PETME2 3L Dual Automatic Pet Feeder - Smart & Quiet Cat Automatic Feeders for 2 Cats with App Control, 2 Way Audio, Dual Power Options, Portion Control, Self-Feeding Cat Food Dispenser - White"
- Current title, black (196 chars): "PETME2 3L Cat Treat Dispenser with Dual Stainless Steel Cat Bowls - Quiet Automatic Cat Feeder for 2 Cats with ..." **Leads with the wrong product type** ("cat treat dispenser" is a different category, and the term was filtered out of the bank). The head term "automatic cat feeder" does not appear until about char 75.
- Parent title (187): "PETME2 Automatic Cat Feeder, Automatic Dog Feeder, Cat Food Dispenser, Cat Feeder Automatic with App Control, Timed Cat Feeder Dry Food, Automatic Pet Feeder Dual Bowls, 3L Large Capacity". This is the best keyword structure of all the titles; reuse it.
- Facts: 3L food container. Dual bowls with an even split, 2x stainless steel bowls (parent: "304 stainless steel"). App control (parent: Tuya Smart app). Up to 10 meals/day and up to 12 portions per meal (parent: about 15 g per portion). Anti-jam 4-compartment design. Silicone seal, desiccant box and sealed outlet ("Triple Freshness Lock"). Detachable for cleaning; care = dishwasher safe. Bowls described as "elevated". For cats and small dogs. Dry food. Item 15.5 x 7.2 x 10.8 in. Package weight about 1.48 (no unit given; likely kg). In the box: main unit, dual bowl base, 2 SS bowls, 3L container, desiccant box, power adapter, manual. List price $129.99. BSR #358 Automatic Cat Feeders (#107,225 Pet Supplies). Images: 9 (MAIN + PT01-08).
- **Contradictions:**
  - The title claims "2 Way Audio", but no bullet or attribute mentions audio. Verify with the owner (the 5L model says "voice recording" instead).
  - "Dual Power Options" vs parent "Backup Battery Protection… continues during power or internet outages". Attributes say batteries_required=false and batteries_included=false. The battery type and count are not stated, and the "internet outages" claim conflicts with the power framing.
  - Parent bullets differ from child bullets (child: 7 bullets, parent: 10). The parent mentions Tuya, 15 g portions and 304 SS; the children don't.
  - Black title says "Cat Treat Dispenser" while every other attribute says automatic feeder.
  - The parent has no color/material attributes.

### B0GHH8L59K: 5L WiFi dual bowl elevated feeder (SKU QO-7VBS-CVT4)
- Current title (200): "PETME2 Dual Bowl Automatic Cat Feeder - 5L WiFi Smart Elevated Cat Feeding Station with App Control, Voice Recording, Dual Power Options, Stainless Steel Cat Bowls & Anti-Jam Technology for Small Dogs"
- Facts: 5L container. 2 bowls with an even split. Stainless steel bowls (bullet). WiFi/app scheduling of custom portions. Voice recording (a recorded call at mealtime; NOT 2-way audio). Anti-jam chute. Detachable, easy clean. Timed feeding, "elevated". Cats and small dogs. Item 18.42 x 7.87 x 15.62 in. In the box: main unit, 2 bowls, food container, power adapter, manual. List price $99.99. BSR #436 Automatic Cat Feeders. Images: 8.
- **Contradictions:**
  - recommended_uses includes "Wet Food" and "Outdoor", while the bullets say dry kibble and indoor directions.
  - "Dual Power Options" in the title, but no bullet explains the battery backup, and batteries are not included.
  - Bullet 5 calls the product a "cat treat dispenser".
  - No material attribute is set. Model name = "PETME2".
  - Meals per day and portion counts are not stated.

### B0GTCGYZDM: 3L camera feeder (SKU 2H-2T1T-CJC3)
- Current title (198): "PETME2 3L Cat Automatic Feeder with Camera, App Control & 2-Way Audio - 1080P Smart Automatic Pet Feeder for Small Dogs with WiFi, Dual Power & Anti-Jam Technology, Easy Scheduling & Portion Control"
- Facts: 3L. 1080p HD camera with live view. 2-way audio. WiFi and app. Scheduling and portion control. Anti-jam that "detects & reverses" blockages. Dual power: adapter plus backup batteries (the description says the battery backup is "optional"). Moisture seals and desiccant box. Single stainless steel bowl (description). Cats and small dogs. Dishwasher safe. Item 6.8 x 7.0 x 11.0 in. List price $89.99. BSR #931 Automatic Cat Feeders. Images: 9.
- **Contradictions:**
  - special_feature says "Feed your cat or small dog at the same time with balanced portions", text copied from the dual model.
  - included_components lists only the main unit (no bowl, adapter or desiccant, though the description mentions them).
  - batteries_included=false while the bullets imply "switches instantly to backup batteries".
  - Bullets use emojis.
  - Meals/day, portion size and night vision are not stated, so do not claim them.

### B0DR7FCLZR: 3.2L/108oz stainless steel fountain (SKU QY-HHE8-0H1B)
- Current title (199): "Luxury Smart Pet Fountain 2026 – 3.2L/108oz Stainless Steel Automatic Cat & Dog Water Fountain, Indoor Pet Water Dispenser with LED Light, Quiet Pump, Dual Flow Modes, 4-Layer Filter, Dishwasher Safe"
- Facts: 3.2L/108oz. Stainless steel (rust-resistant, BPA-free). Dual flow modes (faucet stream and bubbling). LED light for viewing the water level. Ultra-quiet low-voltage pump (DC5V, AC100-240V adapter plus USB cable). 4-layer filter plus a high-density sponge (cotton mesh, activated carbon, ion-exchange resin, fine pad). Filter cartridge included. Spill-proof 360° raised rim. Detachable and dishwasher safe. Cats and dogs, "small or large pets". Indoor and outdoor (attribute). Warranty description present. List price $45.99. BSR #402 Dog Fountains, #1,191 Cat Fountains (#90,686 Pet Supplies). Images: 8 (PT05 missing).
- **Contradictions and issues:**
  - The title does **not start with the brand** and has no "cat water fountain" phrase in order.
  - "2026" and "Luxury" are wasted title chars, and a year can look like a time-sensitive claim.
  - "Smart" with no app.
  - Title says "Indoor", but the bullet and attribute say indoor/outdoor.
  - No item dimensions in the attributes.
  - part_number "B1035".

### B0GHKN9DBR: 2L plastic fountain (SKU L6-L3S1-I7Q6)
- Current title (193): "PETME2 Cat Water Fountain, Automatic Pet Water Fountain for Cats & Dogs, Quiet Indoor Cat Drinking Fountain with Visible Water Level, Low Water Red Light Alert, Anti-Dry Protection, 2L Capacity"
- Facts: 2L. Plastic. Visible water level. Red light low-water alert. Anti-dry auto shut-off. Quiet indoor. Cats and dogs (extra-small/small/medium). Easy to disassemble. Compact and "portable". DC5V. In the box: main unit, reservoir, power cable, manual. **No filter is mentioned anywhere** (not in components, bullets or description). Warranty 1 year limited. No list price set. BSR #726 Cat Fountains (#47,683 Pet Supplies, the best of all 8). Images: 9.
- **Contradictions:**
  - model_name "WaterFountain14" is shared with B0GHKRYV6W (2.2L).
  - "Anti-Dry Heating Protection" wording.
  - Is a filter included or not? It's unclear. If the unit does take a filter, adding it opens the "filter" terms.

### B0GHLBGCP3: 2.2L clear plastic fountain with filter (SKU SD-85ET-IOZ3)
- Current title (198): "PETME2 Automatic Cat Water Fountain - 2.2L Smart Pet Drinking Fountain with 4-Layer Filtration, Transparent Body for Visible Water Levels, Quiet Pump, Easy to Clean Running Water Bowl for Small Dogs"
- Facts: 2.2L. Plastic, clear base with a white top. Built-in filter cartridge, included in components. Quiet. Visible level. USB powered, no batteries. Anti-dry protection (description). Easy disassembly. Cats and small dogs. Indoor. In the box: main unit, reservoir, filter cartridge, power cable, manual. List price $65.99, vs the $19.99 the owner gave. BSR #1,433 Cat Fountains. Images: 9.
- **Contradictions:**
  - The title says "4-Layer Filtration", but the bullets only say "built-in filter cartridge"; the description says "Multi Layer".
  - "Smart" with no app.

### B0GHKRYV6W: 2.2L fountain with stainless tray and filters (SKU JE-LQEW-9EHL)
- Current title (194): "PETME2 Automatic Cat Water Fountain with Filters Included - 2.2L Whisper Quiet Cat Waterer with Stainless Steel Water Bowl Tray, 4-Layer Filtration, Visible Water Level Window & Filter Cartridge"
- Facts: 2.2L ("7 to 10 days"). Plastic body with a stainless steel drinking tray. 4-layer filtration (fur, debris, heavy metals, odors). Anti-dry auto shut-off and low-water alert. Visible level window. Submerged whisper-quiet pump. Fully detachable. Indoor. Cats/dogs/small animals. List price $65.99. BSR #1,327 Cat Fountains. Images: 9.
- **Contradictions:**
  - included_components contains feature text ("2.2L Portable…", "Low Water Red Light Alert…") instead of components. The filter is claimed in the title ("Filters Included") but not listed as a component, and the number of filters is unstated.
  - model_name "WaterFountain14" is the same as the 2L B0GHKN9DBR.
  - Stainless is only the tray, so do not call it a "stainless steel fountain". Use "with stainless steel tray/bowl".
  - The title repeats "Filter" (3x: "Filters", "Filtration", "Filter Cartridge").

---

## Keyword banks: top 15 by search volume (full top 60, title/bullet/backend groups, misspellings, Spanish and long tail are in `keyword-banks.json`)
### B0GHLSQMJ9 / B0GHMCG8Q9: 3L dual feeder (white/black share this bank)
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | automatic cat feeder | 187,032 | 304 | 42 | 46,758 |
| 2 | automatic dog feeder | 32,356 | 249 | 24 | 8,089 |
| 3 | cat feeder | 26,047 | - | 36 | 1,302 |
| 4 | cat food dispenser | 23,065 | - | 10 | 4,613 |
| 5 | cat feeder automatic | 20,495 | 261 | 0 | 5,124 |
| 6 | cat automatic feeders | 14,453 | 231 | 0 | 3,613 |
| 7 | dog feeder | 10,040 | - | 23 | 502 |
| 8 | auto cat feeder | 8,838 | 241 | 1 | 8,838 |
| 9 | dog food dispenser | 8,816 | - | 7 | 1,469 |
| 10 | dog feeding station | 7,599 | 269 | 14 | 1,900 |
| 11 | cat feeding station | 6,414 | 298 | 16 | 1,604 |
| 12 | automatic cat feeder 2 cats | 4,741 | 62 | 6 | 2,371 |
| 13 | dog feeder automatic | 4,515 | 247 | 0 | 1,129 |
| 14 | automatic pet feeder | 4,241 | 245 | 0 | 707 |
| 15 | automatic cat feeders | 4,110 | 283 | 2 | 1,028 |

**Feature-specific terms:** automatic cat feeder 2 cats (4,741, rank 62); automatic feeder cat dry food (3,330, rank 238); timed cat feeder (3,330, rank 245); elevated cat feeding station (2,101, rank -); automatic cat feeder with app (1,768, rank 192); timed cat feeders for dry food (1,766, rank 235); auto cat feeder dry food (1,509, rank 247); timed dog feeder (1,246, rank 214); dual cat feeder automatic (1,246, rank 93); wifi automatic cat feeder app control (1,244, rank 223)

**Title MUST (H10 bank):** automatic cat feeder; automatic dog feeder; cat feeder; cat food dispenser; automatic cat feeder 2 cats; automatic feeder cat dry food; timed cat feeder; automatic cat feeder with app

**Root words (SV across relevant set):** feeder 475,953, cat 441,708, automatic 381,765, dog 117,088, food 99,576, dispenser 73,923, feeders 34,837, pet 31,336, auto 27,638, feeding 27,427

**Spanish (backend):** comedero automatico gatos (3,335), dispensador de comida para gatos (3,332), dispensador de comida para perros (2,414), comedero para perros (2,167), comedero para gatos (1,598), comedero automatico perros (666)

**Relevant keywords:** 655 (total SV 628,830)

**What the listing misses:** The black title leads with "Cat Treat Dispenser". "automatic cat feeder" is not at the front of the child titles. There are no "cat food dispenser"/"timed cat feeder"/"automatic dog feeder" exact phrases in the child titles. The "2 cats" terms are where we rank best (#62/#63), so push them early. Use "dual cat feeder"/"double cat feeder". Bullets never mention "dry food" in phrase form or "timed" in a feature header, and they lack the Tuya/15 g/304 SS facts that the parent has. Spanish terms are missing.

### B0GHH8L59K: 5L WiFi dual elevated feeder
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | automatic cat feeder | 187,032 | 268 | 42 | 46,758 |
| 2 | automatic dog feeder | 32,356 | - | 24 | 8,089 |
| 3 | cat feeder | 26,047 | - | 36 | 1,302 |
| 4 | cat food dispenser | 23,065 | - | 10 | 4,613 |
| 5 | cat feeder automatic | 20,495 | 300 | 0 | 5,124 |
| 6 | cat automatic feeders | 14,453 | 277 | 0 | 3,613 |
| 7 | dog feeder | 10,040 | - | 23 | 502 |
| 8 | auto cat feeder | 8,838 | 306 | 1 | 8,838 |
| 9 | dog food dispenser | 8,816 | - | 7 | 1,469 |
| 10 | dog feeding station | 7,599 | - | 14 | 1,900 |
| 11 | cat feeding station | 6,414 | 228 | 16 | 1,604 |
| 12 | automatic cat feeder 2 cats | 4,741 | 64 | 6 | 2,371 |
| 13 | dog feeder automatic | 4,515 | - | 0 | 1,129 |
| 14 | automatic pet feeder | 4,241 | 289 | 0 | 707 |
| 15 | automatic cat feeders | 4,110 | 300 | 2 | 1,028 |

**Feature-specific terms:** automatic cat feeder 2 cats (4,741, rank 64); timed cat feeder (3,330, rank 270); elevated cat feeding station (2,101, rank 204); automatic cat feeder with app (1,768, rank 186); timed cat feeders for dry food (1,766, rank -); timed dog feeder (1,246, rank -); dual cat feeder automatic (1,246, rank 87); wifi automatic cat feeder app control (1,244, rank 158); dual automatic cat feeder (1,159, rank 64); double cat feeder (1,156, rank -)

**Title MUST (H10 bank):** automatic cat feeder; automatic dog feeder; cat feeder; cat food dispenser; automatic cat feeder 2 cats; timed cat feeder; elevated cat feeding station; automatic cat feeder with app

**Root words (SV across relevant set):** feeder 475,953, cat 441,708, automatic 381,765, dog 117,088, food 99,576, dispenser 73,923, feeders 34,837, pet 31,336, auto 27,638, feeding 27,427

**Spanish (backend):** comedero automatico gatos (3,335), dispensador de comida para gatos (3,332), dispensador de comida para perros (2,414), comedero para perros (2,167), comedero para gatos (1,598), comedero automatico perros (666)

**Relevant keywords:** 655 (total SV 628,830)

**What the listing misses:** The title lacks "automatic dog feeder", "cat food dispenser" and "timed". "Elevated cat feeding station" (2.1k, rank 204) is only partly in the title. Best positions: "automatic cat feeder for 2 cats" #49, "dual automatic cat feeder" #64. Lead with "Automatic Cat Feeder for 2 Cats". Bullet 5 calls it a "cat treat dispenser", which is wrong. Meals/day and portion facts are missing. Fix the wet food/outdoor attributes.

### B0GTCGYZDM: 3L camera feeder
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | automatic cat feeder | 187,032 | 271 | 42 | 46,758 |
| 2 | automatic dog feeder | 32,356 | 291 | 24 | 8,089 |
| 3 | cat feeder | 26,047 | - | 36 | 1,302 |
| 4 | cat food dispenser | 23,065 | - | 10 | 4,613 |
| 5 | cat feeder automatic | 20,495 | 297 | 0 | 5,124 |
| 6 | cat automatic feeders | 14,453 | 287 | 0 | 3,613 |
| 7 | dog feeder | 10,040 | - | 23 | 502 |
| 8 | auto cat feeder | 8,838 | 160 | 1 | 8,838 |
| 9 | dog food dispenser | 8,816 | 283 | 7 | 1,469 |
| 10 | dog feeding station | 7,599 | - | 14 | 1,900 |
| 11 | automatic cat feeder with camera | 6,417 | 121 | 30 | 12,317 |
| 12 | cat feeding station | 6,414 | - | 16 | 1,604 |
| 13 | dog feeder automatic | 4,515 | 259 | 0 | 1,129 |
| 14 | automatic pet feeder | 4,241 | 256 | 0 | 707 |
| 15 | automatic cat feeders | 4,110 | 299 | 2 | 1,028 |

**Feature-specific terms:** automatic cat feeder with camera (6,417, rank 121); timed cat feeder (3,330, rank 242); cat feeder with camera (2,519, rank 127); automatic cat feeder with app (1,768, rank 211); timed cat feeders for dry food (1,766, rank -); timed dog feeder (1,246, rank 241); wifi automatic cat feeder app control (1,244, rank 212); automatic dog feeder with camera (977, rank 102); pet feeder with camera (782, rank 140); timed feeder for cats (663, rank 262)

**Title MUST (H10 bank):** automatic cat feeder; automatic dog feeder; cat feeder; cat food dispenser; automatic cat feeder with camera; timed cat feeder; cat feeder with camera; automatic cat feeder with app

**Root words (SV across relevant set):** feeder 459,123, cat 419,743, automatic 367,505, dog 117,573, food 98,705, dispenser 73,860, feeders 34,210, pet 32,156, auto 27,731, feeding 23,712

**Spanish (backend):** comedero automatico gatos (3,335), dispensador de comida para gatos (3,332), dispensador de comida para perros (2,414), comedero para perros (2,167), comedero para gatos (1,598), comedero automatico perros (666)

**Relevant keywords:** 600 (total SV 607,595)

**What the listing misses:** The title uses "Cat Automatic Feeder with Camera" instead of the exact "automatic cat feeder with camera" (6.4k, rank 121). "cat feeder with camera" (2.5k), "automatic dog feeder with camera", "pet feeder with camera", "cat food dispenser" and "timed cat feeder" are absent. "Small Dogs" is present but "automatic dog feeder" (32k) is not in phrase form. Remove the emojis. special_feature and included_components are copy-paste errors.

### B0DR7FCLZR: 3.2L stainless fountain
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | cat water fountain | 319,141 | - | 46 | 63,828 |
| 2 | dog water fountain | 97,595 | - | 31 | 24,399 |
| 3 | cat fountain | 83,521 | - | 13 | 13,920 |
| 4 | cat water fountain stainless steel | 79,303 | - | 21 | 39,652 |
| 5 | stainless steel cat water fountain | 70,227 | 279 | 15 | 35,114 |
| 6 | water fountains for cats indoor | 49,512 | - | 2 | 24,756 |
| 7 | pet water fountain | 42,109 | - | 10 | 6,016 |
| 8 | cat water dispenser | 17,542 | - | 8 | 2,924 |
| 9 | cat fountain stainless steel | 15,361 | - | 0 | 7,681 |
| 10 | water fountain for dogs inside | 14,057 | 260 | 2 | 14,057 |
| 11 | dog water dispenser | 12,131 | - | 19 | 1,733 |
| 12 | pet fountain | 11,094 | 227 | 6 | 1,387 |
| 13 | dog fountain water bowl | 11,094 | 264 | 3 | 3,698 |
| 14 | pet water dispenser | 8,821 | - | 5 | 882 |
| 15 | automatic water dispenser for cats | 8,819 | - | 2 | 2,940 |

**Feature-specific terms:** cat water fountain stainless steel (79,303, rank -); stainless steel cat water fountain (70,227, rank 279); cat fountain stainless steel (15,361, rank -); stainless steel water fountain for cats (8,816, rank 301); stainless steel dog water fountain (8,814, rank 301); dog water fountain stainless steel (6,419, rank 262); stainless steel cat fountain (4,542, rank -); large dog water fountain (4,088, rank 285); metal cat water fountain (3,337, rank -); stainless steel pet water fountain (3,335, rank 300)

**Title MUST (H10 bank):** cat water fountain; cat fountain; water fountains for cats indoor; pet water fountain; dog water fountain; cat water fountain stainless steel; stainless steel cat water fountain; cat fountain stainless steel

**Root words (SV across relevant set):** water 1,084,221, fountain 1,067,839, cat 759,230, stainless 251,307, dog 250,078, steel 247,553, dispenser 112,915, cats 110,747, pet 106,862, fountains 79,289

**Spanish (backend):** fuente de agua para gatos (8,821), bebedero para gatos (3,128), bebederos para perros (2,213), fuente de agua para perros (1,841), dispensador de agua para perros (1,659), bebedero de agua para perros (977)

**Relevant keywords:** 934 (total SV 1,322,445)

**What the listing misses:** The brand is not first. The exact "cat water fountain" (319k) is missing; the title has "Cat & Dog Water Fountain". "stainless steel cat water fountain" (70k, rank 279) and "cat water fountain stainless steel" (79k) need the exact phrase. "dog water fountain" (98k) is missing as a phrase, and the listing ranks better on dog terms (BSR #402 Dog Fountains). "Large dog water fountain"/"metal cat water fountain" are missing. Drop "Luxury", "2026" and "Smart".

### B0GHKN9DBR: 2L plastic fountain
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | cat water fountain | 319,141 | - | 46 | 63,828 |
| 2 | dog water fountain | 97,595 | - | 31 | 24,399 |
| 3 | cat fountain | 83,521 | - | 13 | 13,920 |
| 4 | water fountains for cats indoor | 49,512 | 236 | 2 | 24,756 |
| 5 | pet water fountain | 42,109 | - | 10 | 6,016 |
| 6 | cat water dispenser | 17,542 | 254 | 8 | 2,924 |
| 7 | water fountain for dogs inside | 14,057 | - | 2 | 14,057 |
| 8 | dog water dispenser | 12,131 | - | 19 | 1,733 |
| 9 | pet fountain | 11,094 | - | 6 | 1,387 |
| 10 | dog fountain water bowl | 11,094 | 285 | 3 | 3,698 |
| 11 | pet water dispenser | 8,821 | - | 5 | 882 |
| 12 | automatic water dispenser for cats | 8,819 | 257 | 2 | 2,940 |
| 13 | water fountain for cats | 7,835 | - | 2 | 1,567 |
| 14 | water dispenser for dogs | 7,806 | - | 1 | 1,115 |
| 15 | automatic water dispenser for dogs | 7,439 | - | 2 | 2,480 |

**Feature-specific terms:** water fountains for cats indoor (49,512, rank 236); small dog water fountain (2,529, rank 304); kitten water fountain (2,502, rank 277); plastic cat water fountain (1,883, rank 29); dog water fountain for small dogs (1,870, rank 211); small cat water fountain (1,768, rank 128); quiet cat water fountain (1,594, rank 143); flowing water bowl for dogs (1,244, rank 264); water fountain for cats indoor (1,244, rank 242); running water bowl for cats (1,159, rank 158)

**Title MUST (H10 bank):** cat water fountain; dog water fountain; cat fountain; pet water fountain; water fountains for cats indoor; automatic water dispenser for cats; automatic water dispenser for dogs; automatic dog water dispenser

**Root words (SV across relevant set):** water 833,649, fountain 795,191, cat 541,764, dog 207,365, dispenser 108,466, cats 96,263, pet 90,516, fountains 70,929, dogs 55,977, indoor 54,114

**Spanish (backend):** fuente de agua para gatos (8,821), bebedero para gatos (3,128), bebederos para perros (2,213), fuente de agua para perros (1,841), dispensador de agua para perros (1,659), bebedero de agua para perros (977)

**Relevant keywords:** 754 (total SV 1,027,242)

**What the listing misses:** Good start ("Cat Water Fountain" first, best BSR). Missing "dog water fountain" as a phrase, "water fountains for cats indoor" (49.5k, rank 236), "cat water dispenser", "small cat water fountain" (rank 128), "plastic cat water fountain" (rank 29, protect it), "kitten", "quiet cat water fountain" (rank 143). Do NOT add filter or stainless terms unless the owner confirms a filter.

### B0GHLBGCP3: 2.2L clear fountain with filter
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | cat water fountain | 319,141 | 293 | 46 | 63,828 |
| 2 | dog water fountain | 97,595 | 269 | 31 | 24,399 |
| 3 | cat fountain | 83,521 | - | 13 | 13,920 |
| 4 | water fountains for cats indoor | 49,512 | 285 | 2 | 24,756 |
| 5 | pet water fountain | 42,109 | - | 10 | 6,016 |
| 6 | cat water dispenser | 17,542 | 266 | 8 | 2,924 |
| 7 | water fountain for dogs inside | 14,057 | - | 2 | 14,057 |
| 8 | dog water dispenser | 12,131 | - | 19 | 1,733 |
| 9 | pet fountain | 11,094 | - | 6 | 1,387 |
| 10 | dog fountain water bowl | 11,094 | - | 3 | 3,698 |
| 11 | pet water dispenser | 8,821 | - | 5 | 882 |
| 12 | automatic water dispenser for cats | 8,819 | 249 | 2 | 2,940 |
| 13 | water fountain for cats | 7,835 | - | 2 | 1,567 |
| 14 | water dispenser for dogs | 7,806 | - | 1 | 1,115 |
| 15 | automatic water dispenser for dogs | 7,439 | - | 2 | 2,480 |

**Feature-specific terms:** cat water fountain with filtration (4,522, rank 302); filtered dog water fountain (2,944, rank -); small dog water fountain (2,529, rank -); kitten water fountain (2,502, rank 228); filtered dog water bowl (2,176, rank 298); plastic cat water fountain (1,883, rank 92); dog water fountain for small dogs (1,870, rank 110); small cat water fountain (1,768, rank -); dog filtered water bowl (1,759, rank -); quiet cat water fountain (1,594, rank 299)

**Title MUST (H10 bank):** cat water fountain; dog water fountain; cat fountain; pet water fountain; water fountains for cats indoor; cat water fountain with filtration; filtered dog water fountain; small dog water fountain

**Root words (SV across relevant set):** water 857,971, fountain 810,751, cat 551,506, dog 219,605, dispenser 109,109, cats 96,703, pet 91,735, fountains 72,442, bowl 58,758, dogs 57,712

**Spanish (backend):** fuente de agua para gatos (8,821), bebedero para gatos (3,128), bebederos para perros (2,213), fuente de agua para perros (1,841), dispensador de agua para perros (1,659), bebedero de agua para perros (977)

**Relevant keywords:** 792 (total SV 1,052,404)

**What the listing misses:** Has "Automatic Cat Water Fountain" but not the leading exact "cat water fountain". Missing "dog water fountain" (rank 269), "water fountains for cats indoor", "cat fountain", "small dog water fountain", "dog water fountain for small dogs" (rank 110), "plastic cat water fountain" (rank 92), "cat water fountain with filtration", "filtered dog water fountain". Drop "Smart" and "Running Water Bowl" (low SV).

### B0GHKRYV6W: 2.2L fountain with SS tray (no rank data)
| # | Keyword | SV | Our rank | Title dens. | IQ |
|---|---|---|---|---|---|
| 1 | cat water fountain | 319,141 | - | 46 | 63,828 |
| 2 | dog water fountain | 97,595 | - | 31 | 24,399 |
| 3 | cat fountain | 83,521 | - | 13 | 13,920 |
| 4 | cat water fountain stainless steel | 79,303 | - | 21 | 39,652 |
| 5 | stainless steel cat water fountain | 70,227 | - | 15 | 35,114 |
| 6 | water fountains for cats indoor | 49,512 | - | 2 | 24,756 |
| 7 | pet water fountain | 42,109 | - | 10 | 6,016 |
| 8 | cat water dispenser | 17,542 | - | 8 | 2,924 |
| 9 | cat fountain stainless steel | 15,361 | - | 0 | 7,681 |
| 10 | water fountain for dogs inside | 14,057 | - | 2 | 14,057 |
| 11 | dog water dispenser | 12,131 | - | 19 | 1,733 |
| 12 | pet fountain | 11,094 | - | 6 | 1,387 |
| 13 | dog fountain water bowl | 11,094 | - | 3 | 3,698 |
| 14 | pet water dispenser | 8,821 | - | 5 | 882 |
| 15 | automatic water dispenser for cats | 8,819 | - | 2 | 2,940 |

**Feature-specific terms:** cat water fountain stainless steel (79,303, rank -); stainless steel cat water fountain (70,227, rank -); cat fountain stainless steel (15,361, rank -); stainless steel water fountain for cats (8,816, rank -); stainless steel dog water fountain (8,814, rank -); dog water fountain stainless steel (6,419, rank -); stainless steel cat fountain (4,542, rank -); cat water fountain with filtration (4,522, rank -); stainless steel pet water fountain (3,335, rank -); filtered dog water fountain (2,944, rank -)

**Title MUST (H10 bank):** cat water fountain; dog water fountain; cat fountain; pet water fountain; cat water fountain stainless steel; stainless steel cat water fountain; water fountains for cats indoor; cat fountain stainless steel

**Root words (SV across relevant set):** water 1,072,469, fountain 1,050,329, cat 747,276, stainless 246,180, dog 243,433, steel 242,399, dispenser 112,728, cats 109,925, pet 103,060, fountains 78,215

**Spanish (backend):** fuente de agua para gatos (8,821), bebedero para gatos (3,128), bebederos para perros (2,213), fuente de agua para perros (1,841), dispensador de agua para perros (1,659), bebedero de agua para perros (977)

**Relevant keywords:** 921 (total SV 1,303,044)

**What the listing misses:** No ranking data. The title is filter-heavy and lacks "dog water fountain", "cat fountain", "water fountains for cats indoor" and "pet water fountain". "stainless steel cat water fountain" (70k) is tempting but only the tray is SS, so use "with Stainless Steel Tray/Bowl" phrasing. "Whisper Quiet Cat Waterer" has low SV; "quiet cat water fountain" (1.6k) is better.

---
## Open questions for the owner (needed before writing copy)
1. 3L dual feeder: does it really have 2-way audio (title), or voice recording only? Does the battery backup use which batteries, and are they included?
2. 5L feeder: does it have battery backup? How many meals/day and portions? Remove "wet food" and "outdoor"?
3. Camera feeder: night vision? Meals/day? Is a bowl/adapter/desiccant included (fix included_components)?
4. B0GHKN9DBR (2L): is a filter used or included? Is it 2L or 2.2L (it shares model WaterFountain14 with the 2.2L B0GHKRYV6W)?
5. B0GHKRYV6W: how many filters are included? Fix included_components (it currently holds feature text).
6. B0DR7FCLZR: indoor only, or indoor/outdoor? Keep "2026"?
7. Price: the owner says $19.99 for the plastic fountains, but list_price shows $65.99 on B0GHLBGCP3/B0GHKRYV6W (list price only; check the live offer).
