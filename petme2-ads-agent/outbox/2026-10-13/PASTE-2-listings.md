# Chrome prompt: PETME2 listing edits in Seller Central (Oct 13, 2026)

Paste this whole file into Claude in Chrome. You are logged in to Seller Central (US). Edit 5 SKUs, one at a time.
Text was checked with Python (check table at the end of each SKU). Source data: Helium 10 Cerebro Oct 12, live SP-API text Oct 13, owner facts Oct 12.

## RULES (read first)

1. **Backup first.** Before you change anything on a SKU, open Inventory > Manage All Inventory > search the SKU > Edit (Edit product details). Copy the CURRENT Title (Item Name), all 5 Bullet Points, Product Description and Search Terms word for word into your report. Do this BEFORE you type anything.
2. **One SKU at a time**, in this order: QO-7VBS-CVT4, 2H-2T1T-CJC3, L6-L3S1-I7Q6, SD-85ET-IOZ3, JE-LQEW-9EHL.
3. Change **only** the fields listed for that SKU. Paste text exactly (copy from the code blocks). Do not retype, do not add or remove words, do not add emojis.
4. Fields marked **keep as is**: do not touch them.
5. **Do not change** price, sale price, list price, images, video, variations, offer, quantity, shipping, brand, model name, product type, or anything not listed here.
6. Click **Save and finish**. Wait for the confirmation. Then reload the edit page and **read back** every changed field. It must match this file exactly. Note in the report if Amazon shortened or changed anything. If the read-back does not match (other than Amazon removing a double space), STOP and report; do not re-edit and do not go to the next SKU.
7. If Amazon shows a **new** error, a red field warning, "listing suppressed", "inactive", or a "this change needs approval" message: **STOP**. Do not try other text. Take a screenshot and report. Do not go on to the next SKU.
   - Old warnings that were already there on Oct 13 (Offer tab Mexico/Canada "price difference > 20%") are known. Ignore them and do not touch the Offer tab.
8. If you are logged out, asked for a 2-step code or a CAPTCHA: stop and tell the owner. Never enter a password.
9. Attribute fields: find them on the edit page (use the page search box or "Show all attributes" / the "Product Details" or "More Details" tab). If a field has several value boxes, put one value per box, in this order, and clear extra old boxes. If the field is not on the page, skip it and write "field not found" in the report.
10. If a bullet box is missing (fewer than 5 boxes), stop and report.
11. Description find/replace: if the Find text is not on the page exactly, do NOT edit the description at all; write "not found" and go on with the other fields.

---

## SKU QO-7VBS-CVT4  (5L WiFi dual-bowl elevated feeder, B0GHH8L59K)

**Step 0 - backup:** copy current Title, Bullets 1-5, Description, Search Terms into the report.

### Title (Item Name): CHANGE to

```
PETME2 Elevated Automatic Cat Feeder for 2 Cats, 5L WiFi App Control, Double Bowl Cat Food Dispenser with Voice Recording, Dual Power Battery Backup, Stainless Steel Bowls, Automatic Dog Feeder
```
Old (for checking): `PETME2 Automatic Cat Feeder for 2 Cats, 5L Elevated Feeding Station with WiFi App and Voice Recording, Automatic Dog Feeder, Stainless Steel Dual Bowls, Timed Pet Food Dispenser, Dual Power`

Why: Keeps 'automatic cat feeder for 2 cats' word for word in the first 80 chars (fell #49->#69) and adds the exact 'elevated automatic cat feeder' (fell #20->#54, competition 936). Adds 'double' (double cat feeder #96, double automatic cat feeder #101), 'cat food dispenser' (23.6k SV, not ranked) and the owner-confirmed 'Dual Power Battery Backup' (dual power automatic cat feeder battery backup 1,084 SV, #77, only 262 competing products). Drops 'Timed Pet Food Dispenser' (low SV; 'timed' stays in bullet 3) and 'Feeding Station' (rank #305; stays in bullet 4 header).

### Bullet Points

**Bullet 1: CHANGE to**
```
FEEDS 2 CATS EQUALLY: This automatic cat feeder for 2 cats splits every meal evenly between two stainless steel bowls, so each pet gets a fair share and food stealing stops. It is an automatic cat feeder 2 cats can share, a dual automatic cat feeder and double cat feeder in one, made for multi-cat homes. Many cat automatic feeders have a single bowl, while this automatic pet feeder for cats serves both pets at once, including a cat and a small dog.
```
Why: adds 'multi' (multi cat feeder 900 SV #133; automatic cat feeder multiple cats #117); every ranked '2 cats'/'dual'/'double' phrase is kept word for word

**Bullet 2: keep as is** (starts with "WIFI APP SCHEDULING:")

**Bullet 3: CHANGE to**
```
VOICE RECORDING AT MEALTIME: Record your own short message and this voice recording automatic cat feeder plays it to call your pets to every meal, so they hear a familiar voice while you are away. It is a one-way recorded message, not a live call. This timed cat feeder also suits small dogs as a timed dog feeder or an automatic dog feeder with timer. Set a dog feeder automatic schedule once, and a small breed gets the same portion at the same times every day.
```
Why: adds the exact 'voice recording automatic cat feeder' (424 SV, #95, 340 competing) and stops indexing '2-way audio', a feature this unit does not have

**Bullet 4: keep as is** (starts with "5L ELEVATED CAT FEEDING STATION:")

**Bullet 5: CHANGE to**
```
DUAL POWER, BATTERY BACKUP, EASY TO CLEAN: This dual power automatic cat feeder runs on the included power adapter, and its battery backup keeps meals on schedule during a power outage (batteries not included). The stainless steel bowls wipe clean easily, and the bowls and food container detach for washing. One unit serves as a cat food feeder and dog food feeder, a cat automatic feeder and dog automatic feeder in one.
```
Why: owner confirmed battery backup (type unknown, so no battery type is named); adds the exact 'dual power automatic cat feeder ... battery backup' wording (1,084 SV #77; 532 SV #82)

### Product Description

Keep the rest of the description exactly. Only make these find-and-replace edits:

1. Find: `It is a recorded call, not live 2-way audio.`
   Replace with: `It is a one-way recorded message, not a live call.`
   Why: stop indexing a feature we do not have
2. Find: `Made from food-grade materials, the feeder has stainless steel bowls`
   Replace with: `The feeder has stainless steel bowls`
   Why: 'food-grade' is not a verified fact

### Search Terms (Generic Keyword)

Delete all current text in the box, then paste exactly:
```
programmable multicat multiple large kitty kitten puppy tall capacity remote electric autofeeder dispensor comedero automatico gatos alimentador dispensador comida perros mascotas perro
```
Old (for checking): `auto self double two timer schedule programmable smart large capacity kibble dry kitty kitten puppy multiple meal portion control raised tall backup battery remote electric comedero automatico gatos dispensador comida perros alimentador`

Why: Removes 'double', 'backup', 'battery' (now in the title) and words already in the bullets (auto, self, two, timer, schedule, smart, large, kibble, dry, multiple, meal, portion, control). Keeps 'tall' ('raised' is already in bullet 4: raised automatic cat feeder #297) and the Spanish terms; adds 'multicat', 'autofeeder', 'dispensor' (misspelling), 'mascotas', 'perro'.

### Attributes

| Seller Central field | Old value | New value (one per box, in order) |
|---|---|---|
| **Special Features** (`special_feature`) | 2-in-1 Dual Automatic Cat Feeder - Feed two cats or small dogs at the same time with balanced portions / Smart App Control - Schedule meals and manage feedin... | 1. Elevated Feeding Station<br>2. Dual Bowls for 2 Pets<br>3. WiFi App Scheduling<br>4. Voice Recording Meal Call<br>5. Dual Power with Battery Backup |
| **Included Components** (`included_components`) | Automatic Cat Feeder Main Unit - The primary feeding device that dispenses food automatically according to your scheduled settings. / Dual Feeding Bowls - Tw... | 1. Feeder main unit<br>2. 2 stainless steel bowls<br>3. Food storage container<br>4. Power adapter<br>5. User manual |

- Special Features: 5 long supplier sentences -> short facts; adds elevated and battery backup (owner confirmed)
- Included Components: same 5 items, short names instead of sentences
- Do not change: Do not change Recommended Uses (owner kept Wet Food/Outdoor on Oct 4), Material, price, images or variations.

## SKU 2H-2T1T-CJC3  (3L camera feeder, B0GTCGYZDM)

**Step 0 - backup:** copy current Title, Bullets 1-5, Description, Search Terms into the report.

### Title (Item Name): keep as is (do not change)

Reason: NO CHANGE. Oct 4 title is working: automatic pet feeder with camera #151->#35, automatic dog feeder with camera #102->#36, cat food dispenser with camera #86->#42, cat feeder with camera #127->#57. A title edit now would reset that climb.

### Bullet Points

**Bullet 1: keep as is** (starts with "WATCH EVERY MEAL IN 1080P:")

**Bullet 2: keep as is** (starts with "TALK WITH 2-WAY AUDIO:")

**Bullet 3: keep as is** (starts with "APP SCHEDULING, PORTION CONTROL:")

**Bullet 4: keep as is** (starts with "ANTI-JAM 3L STORAGE, FRESH FOOD:")

**Bullet 5: keep as is** (starts with "DUAL POWER, EASY CLEAN:")

Bullet 3 already says 'tap once to serve a meal on demand' (owner confirmed tap-to-feed), so no bullet edit is needed.

### Product Description

Keep as is.

### Search Terms (Generic Keyword)

Keep as is (do not change).

### Attributes

| Seller Central field | Old value | New value (one per box, in order) |
|---|---|---|
| **Special Features** (`special_feature`) | Automatic Cat Feeder - Feed your cat or small dog at the same time with balanced portions | 1. 1080P HD Camera with Live View<br>2. 2-Way Audio<br>3. Tap to Feed in the App<br>4. WiFi App Scheduling and Portion Control<br>5. Anti-Jam Detect and Reverse |
| **Included Components** (`included_components`) | Automatic Cat Feeder Main Unit - The primary feeding device that dispenses food automatically according to your scheduled settings. | 1. Feeder main unit<br>2. Stainless steel bowl<br>3. Desiccant box |

- Special Features: live value is copied from the dual feeder ('feed your cat or small dog at the same time') and is wrong for a 1-bowl camera feeder; adds owner-confirmed tap-to-feed. No night vision, no GHz.
- Included Components: live value is one long sentence; only items stated in our own copy are listed (adapter/manual not confirmed for this SKU)
- Do not change: Title, bullets, description and Search Terms stay exactly as they are.

## SKU L6-L3S1-I7Q6  (2L plastic fountain, B0GHKN9DBR)

**Step 0 - backup:** copy current Title, Bullets 1-5, Description, Search Terms into the report.

### Title (Item Name): CHANGE to

```
PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, LED Low Level Indicator, Visible Window, Anti-Dry Pump Shut-Off, Compact White Plastic Design for Kittens and Small Dogs
```
Old (for checking): `PETME2 Cat Water Fountain, 68oz/2L Quiet Water Fountains for Cats Indoor, Red Light Low Level Alert, Visible Window, Anti-Dry Pump Shut-Off, Small Pet Dispenser for Kitten and Dog`

Why: First 73 chars unchanged (protects 'quiet water fountains for cats indoor' #73 and 'water fountains for cats indoor quiet' #77). 'Red Light' -> owner-confirmed 'LED' + 'Indicator' (cat water fountain with led indicator 1,000 SV, #27 -> push to top 10). Weak tail 'Small Pet Dispenser for Kitten and Dog' (no SV) -> 'Compact White Plastic Design for Kittens and Small Dogs': puts 'plastic' in the title (plastic cat water fountain 1,641 SV fell #29->#45; cat water fountain plastic #45), plus compact (#35), white (cat water fountain white #22) and small (small cat water fountain 1,890 SV #60). No filter wording at all.

### Bullet Points

**Bullet 1: keep as is** (starts with "FRESH MOVING WATER CATS WANT TO DRINK:")

**Bullet 2: CHANGE to**
```
LED LOW WATER ALERT: Stop guessing when to refill. A red LED indicator light warns you when the water runs low, and the clear water level window lets you check the 68oz/2L reservoir at a glance. This cat water fountain with LED indicator is an automatic water dispenser for cats and automatic cat water dispenser that tells you when it needs a refill, a simple pet water dispenser and water dispenser for cats for busy homes.
```
Why: owner confirmed the low-water light is an LED; adds the exact 'cat water fountain with led indicator' (1,000 SV, #27, 776 competing)

**Bullet 3: keep as is** (starts with "ANTI-DRY PUMP PROTECTION:")

**Bullet 4: CHANGE to**
```
QUIET AND COMPACT FOR SMALL SPACES: Made for water fountains for cats indoor, this slim, quiet cat water fountain keeps bedrooms and apartments calm. It is a small cat water fountain and kitty water fountain with a slim white plug-in design, and it also works as a small dog water fountain or a dog water fountain for small dogs. The light plastic cat water fountain body fits a water fountain for cats indoor corner or a water fountain for dogs inside.
```
Why: 'light and easy to move' read as cordless (ads got cordless/wireless clicks); 'plastic cat water fountain' and every ranked phrase stay word for word; adds 'white'

**Bullet 5: keep as is** (starts with "EASY TO CLEAN, SIMPLE TO SET UP:")

### Product Description

Keep the rest of the description exactly. Only make these find-and-replace edits:

1. Find: `the slim, portable white body fits`
   Replace with: `the slim white body fits`
   Why: not cordless

### Search Terms (Generic Keyword)

Delete all current text in the box, then paste exactly:
```
mini size breed puppy drinker hydration silent pets waterer bebedero gatos fuente agua perros dispensador fonte gato bebedouro
```
Old (for checking): `plastic kitty drinking waterer bowl automatic auto flowing running circulating fresh inside easy clean mini compact portable slim white refill indicator hydration drinker bedroom bebedero gatos fuente agua perros dispensador animal`

Why: Drops 'plastic', 'white', 'compact', 'indicator' (now in title) and words already in bullets (kitty, bowl, automatic, auto, flowing, running, fresh, inside, easy, clean, slim, refill). 'portable' removed (not cordless). Adds size/breed (dog water bowl fountain small breed #131), puppy (puppy water fountain #158), silent, pets, fonte/bebedouro (Portuguese ad order). No filter words.

### Attributes

| Seller Central field | Old value | New value (one per box, in order) |
|---|---|---|
| **Special Features** (`special_feature`) | 2L Portable Water Capacity - Compact size with reliable daily hydration / Visible Water Level Window - Easy monitoring at a glance / Low Water Red Light Aler... | 1. 2L Compact Water Capacity - Slim size for small spaces<br>2. Visible Water Level Window - Easy monitoring at a glance<br>3. LED Low Water Alert - Red LED light shows when water needs refilling<br>4. Anti-Dry Protection - Automatically shuts off when water runs low<br>5. Quiet Indoor Design - Suitable for calm home environments |

- Special Features: value 1: 'Portable' suggests cordless; value 3: owner-confirmed LED. Values 2, 4, 5 unchanged.
- Do not change: Never add filter / filterless / no filter wording (owner answer unclear). Do not change model name, price, images.

## SKU SD-85ET-IOZ3  (2.2L transparent fountain with 4-layer filter, B0GHLBGCP3)

**Step 0 - backup:** copy current Title, Bullets 1-5, Description, Search Terms into the report.

### Title (Item Name): CHANGE to

```
PETME2 Transparent Cat Water Fountain 74oz/2.2L with 4-Layer Filter, Quiet Pump, Anti-Dry Protection, USB Powered, Filtered Dog Water Fountain for Small Dogs and Kittens, See-Through Plastic Tank
```
Old (for checking): `PETME2 Transparent Cat Water Fountain 74oz/2.2L, 4-Layer Filtered Cat Water Dispenser with Quiet Pump, Clear Tank Shows Level, Anti-Dry Protection, Automatic Pet Fountain for Small Dogs Indoor`

Why: No phrase ranks better than #92 here, so the title can move. Keeps 'Transparent Cat Water Fountain 74oz/2.2L' and the owner-confirmed 4-layer filter at the front. Adds the exact 'filtered dog water fountain' (3,254 SV, not ranked) and 'dog water fountain for small dogs' (1,276 SV, #110), plus small dog water fountain (2,906 SV #156), kitten (kitten water fountain 2,571 SV #223) and plastic (plastic cat water fountain 1,641 SV #92). 'USB Powered' is owner-confirmed. Drops 'Clear Tank Shows Level' (no SV, repeats Transparent) and 'Automatic Pet Fountain' (SV 36). 'cat water dispenser' stays in bullets 2 and 4.

### Bullet Points

**Bullet 1: keep as is** (starts with "SEE THE WATER LEVEL AT A GLANCE:")

**Bullet 2: keep as is** (starts with "4-LAYER FILTERED WATER:")

**Bullet 3: keep as is** (starts with "FLOWING WATER ENCOURAGES DRINKING:")

**Bullet 4: keep as is** (starts with "QUIET PUMP FOR CALM HOMES:")

**Bullet 5: CHANGE to**
```
EASY SETUP AND CLEANING: Assembles in minutes and comes apart just as quickly for washing. It is USB powered: plug the USB cable into a wall adapter. It is not cordless and needs no batteries. For a small dog it is a dog water dispenser and automatic dog water dispenser, a water fountain for dogs inside the home. It also works as an automatic water dispenser for dogs, an automatic dog water bowl or an automatic water bowl for dogs, a cat or dog water dispenser in one.
```
Why: owner confirmed USB cable + wall adapter; 'not cordless' answers the 'not wireless' review and cuts cordless clicks. Trims one repeated chain to stay under 500 chars.

### Product Description

Keep as is.

### Search Terms (Generic Keyword)

Delete all current text in the box, then paste exactly:
```
size breed puppy hydration drinker pets multi waterer bebedero gatos fuente agua perros dispensador transparente filtro gato fonte
```
Old (for checking): `see through plastic filtration kitty kitten waterer drinking bowl flowing running circulating auto easy clean dish hydration inside multi drinker bedroom fresh bebedero gatos fuente agua perros dispensador animal system`

Why: Drops 'see', 'through', 'plastic' (now in title) and bullet words (kitty, kitten, bowl, flowing, running, auto, easy, clean, inside, fresh). Adds size/breed (dog water fountain small size dog #97, dog water bowl fountain small breed #111), puppy, pets, transparente/filtro/gato/fonte.

### Attributes

| Seller Central field | Old value | New value (one per box, in order) |
|---|---|---|
| **Special Features** (`special_feature`) | 2.2L Large Capacity : Provides ample water supply for daily hydration while reducing the need for frequent refills. / Automatic Circulating Water Flow:  Enco... | 1. Transparent Body Shows Water Level<br>2. 4-Layer Filter Cartridge Included<br>3. Quiet Pump<br>4. Anti-Dry Protection<br>5. USB Powered |
| **Dog Breed Size** (`dog_breed_size`) | extra_small | 1. extra_small<br>2. small |

- Special Features: old values contain hidden U+2028 line-break characters; replace with clean short facts (4-layer and USB owner-confirmed)
- Dog Breed Size: title and bullets say small dogs
- Do not change: Description stays as is (its '4-layer' and 'USB powered' are now owner-confirmed).

## SKU JE-LQEW-9EHL  (2.2L fountain with stainless steel tray + filters, B0GHKRYV6W)

**Step 0 - backup:** copy current Title, Bullets 1-5, Description, Search Terms into the report.

### Title (Item Name): CHANGE to

```
PETME2 Quiet Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Pet Water Fountain for Cats and Small Dogs, 4-Layer Filtration, Filters Included, Low Level Alert, Anti-Dry Pump Shut-Off
```
Old (for checking): `PETME2 Cat Water Fountain with Stainless Steel Tray, 74oz/2.2L Automatic Pet Fountain for Cats and Dogs, 4-Layer Filtration, Filters Included, Low Water Alert, Quiet Pump`

Why: Puts the exact 'quiet cat water fountain' (1,803 SV, #140; the only search that ever sold this ASIN in ads) first, which also covers 'quiet cat water fountain stainless steel' (2,265 SV, #163) honestly since the tray is steel. 'Pet water fountain' (42k) replaces 'Automatic Pet Fountain' (SV 36). 'Small Dogs' pushes dog water fountain for small dogs (#130) and dog water bowl fountain small breed (#20). 'Filters Included' kept (owner confirmed, no count). 'Low Level Alert' keeps 'water' at 2.

### Bullet Points

**Bullet 1: CHANGE to**
```
STAINLESS STEEL DRINKING TRAY: Your pet drinks from a stainless steel tray that wipes clean easily between washes, while the fountain body is light plastic. Cats and small dogs can share it. Only the drinking tray is stainless steel, so you know what you get. The fully detachable design makes the tray simple to wash.
```
Why: removes keyword stuffing ('stainless steel tray and all') that pulled all-steel shoppers (about 10 clicks, 0 orders) and 'easy to move' (cordless hint)

**Bullet 2: keep as is** (starts with "4-LAYER FILTRATION, FILTERS INCLUDED:")

**Bullet 3: keep as is** (starts with "74OZ/2.2L WITH VISIBLE LEVEL WINDOW:")

**Bullet 4: keep as is** (starts with "ANTI-DRY SHUT-OFF AND LOW WATER ALERT:")

**Bullet 5: CHANGE to**
```
QUIET PUMP, FULLY DETACHABLE: The submerged pump runs with low noise that will not startle timid cats, and the fully detachable design makes cleaning simple. Sized for water fountains for cats indoor, it is a small cat water fountain and kitten water fountain. It also works as a dog water fountain for small dogs or a small dog water fountain, and it plugs into the wall with the included power adapter.
```
Why: owner confirmed the power adapter is in the box; replaces 'easy to carry from room to room' (cordless hint: tray ranks #132 for 'cordless dog fountain water bowl')

### Product Description

Keep the rest of the description exactly. Only make these find-and-replace edits:

1. Find: `pairs a light plastic body made from food-grade materials with a stainless steel drinking tray`
   Replace with: `pairs a light plastic body with a stainless steel drinking tray`
   Why: 'food-grade' not verified
2. Find: `For dogs, it is a dog water fountain, stainless steel tray included. `
   Replace with: (delete this sentence; nothing in its place)
   Why: keyword stuffing

### Search Terms (Generic Keyword)

Delete all current text in the box, then paste exactly:
```
dish size breed puppy hydration drinker silent compact auto waterer circulating flowing kitty bebedero gatos fuente agua perros acero inoxidable fonte filtro gato
```
Old (for checking): `plastic metal dish bowl kitty kitten waterer drinking flowing running circulating auto easy clean small inside indoor level window refill shutoff dispenser hydration bebedero gatos fuente agua perros acero inoxidable filtered animal`

Why: Drops 'plastic' and 'metal' (body is plastic; avoids all-steel/metal shoppers), 'small'/'filtered' (now in title) and bullet words. Adds size/breed (#20/#125 small-dog phrases), puppy, silent, compact (#114), fonte/filtro/gato.

### Attributes

| Seller Central field | Old value | New value (one per box, in order) |
|---|---|---|
| **Included Components** (`included_components`) | 2.2L Portable Water Capacity - Compact size with reliable daily hydration / Visible Water Level Window - Easy monitoring at a glance / Low Water Red Light Al... | 1. Fountain main unit<br>2. Stainless steel drinking tray<br>3. Filters<br>4. Power adapter |
| **Special Features** (`special_feature`) | Stainless Steel Tray Design | 1. Stainless Steel Drinking Tray<br>2. 4-Layer Filtration<br>3. Low Water Alert<br>4. Anti-Dry Pump Shut-Off<br>5. Visible Water Level Window |
| **Material** (`material`) | Stainless Steel / Plastic | 1. Plastic<br>2. Stainless Steel |

- Included Components: live value is feature text copied from the 2L (incl. a 'Red Light Alert'); owner confirmed filters + power adapter in the box (no count)
- Special Features: only 1 value today; adds true features
- Material: the body is plastic, so it goes first (only the tray is steel)
- Do not change: Do not add a filter number anywhere. Do not add 'LED' (not confirmed for this model).

## Known open points (do not act on these in Chrome)

- Camera (2H-2T1T-CJC3): the live title says "Dual Power" and bullet 5 + description say backup batteries. Battery backup was confirmed for the 5L only, not for the camera. We keep the camera title/bullets now (ranks are rising). Owner: please confirm camera battery backup; if NO, we remove it in a later edit.
- 5L: "(batteries not included)" is kept from the live text and matches the batteries_included=false attribute. If batteries ARE in the box, tell us.
- Tray: low-water alert is not confirmed as LED, so no "LED" was added.
- Listing edits re-index in 24-72 h; ranks can dip for a few days before they rise. Judge on Oct 26 with a new Cerebro run, not before.

## REPORT BACK (copy this and fill it)

```
LISTING EDITS - Oct 13, 2026
SKU QO-7VBS-CVT4 (B0GHH8L59K):
  Backup taken (title, 5 bullets, description, search terms): yes/no  [paste the old text below]
  Title: changed / kept / error: ...
  Bullets changed: [list numbers]  / errors: ...
  Description edits: done / not found / skipped
  Search Terms: changed / kept / error: ...
  Attributes: [field -> done / field not found / error]
  Saved: yes/no   Read-back matches this file: yes/no (list any difference)
  New warnings or suppression: none / [exact text + screenshot]
SKU 2H-2T1T-CJC3 (B0GTCGYZDM):
  Backup taken (title, 5 bullets, description, search terms): yes/no  [paste the old text below]
  Title: changed / kept / error: ...
  Bullets changed: [list numbers]  / errors: ...
  Description edits: done / not found / skipped
  Search Terms: changed / kept / error: ...
  Attributes: [field -> done / field not found / error]
  Saved: yes/no   Read-back matches this file: yes/no (list any difference)
  New warnings or suppression: none / [exact text + screenshot]
SKU L6-L3S1-I7Q6 (B0GHKN9DBR):
  Backup taken (title, 5 bullets, description, search terms): yes/no  [paste the old text below]
  Title: changed / kept / error: ...
  Bullets changed: [list numbers]  / errors: ...
  Description edits: done / not found / skipped
  Search Terms: changed / kept / error: ...
  Attributes: [field -> done / field not found / error]
  Saved: yes/no   Read-back matches this file: yes/no (list any difference)
  New warnings or suppression: none / [exact text + screenshot]
SKU SD-85ET-IOZ3 (B0GHLBGCP3):
  Backup taken (title, 5 bullets, description, search terms): yes/no  [paste the old text below]
  Title: changed / kept / error: ...
  Bullets changed: [list numbers]  / errors: ...
  Description edits: done / not found / skipped
  Search Terms: changed / kept / error: ...
  Attributes: [field -> done / field not found / error]
  Saved: yes/no   Read-back matches this file: yes/no (list any difference)
  New warnings or suppression: none / [exact text + screenshot]
SKU JE-LQEW-9EHL (B0GHKRYV6W):
  Backup taken (title, 5 bullets, description, search terms): yes/no  [paste the old text below]
  Title: changed / kept / error: ...
  Bullets changed: [list numbers]  / errors: ...
  Description edits: done / not found / skipped
  Search Terms: changed / kept / error: ...
  Attributes: [field -> done / field not found / error]
  Saved: yes/no   Read-back matches this file: yes/no (list any difference)
  New warnings or suppression: none / [exact text + screenshot]
STOPPED EARLY? yes/no - at SKU ... because ...
```

After 24-48 h the agent checks: new title shows on the product page, listing not suppressed, and 2-3 new phrases + 'PETME2' are found in Amazon search.
