# Ad options and Guardian check — 2026-10-04

Written by: Guardian + Experiment Lab. Status: **research only**. Nothing was changed in Amazon, no file was uploaded, no setting was changed.

Files checked:
- `outbox/2026-10-04/approved-changes.json` (48 rows, already UPLOADED today, both campaigns enabled by the owner)
- `outbox/2026-10-04/competitors-changes.json` (37 rows, not uploaded)
- `outbox/2026-10-04/allproducts-changes.json` (33 rows, not uploaded)
- `ads_source/files.py` (`UPLOAD_COLUMNS`), `ads_source/make_upload.py`, `settings.yaml`, `data/2026-10-03/products.csv`

Note on sources: advertising.amazon.com and m.media-amazon.com are blocked from this machine, so I could not open the official help pages directly. The strongest proof is (a) the **official Amazon seller bulksheet template** (`AdvertisingBulksheetTemplate-seller.xlsx`, copy found in a public GitHub tool, its "Config" sheet lists the allowed values) and (b) **our own upload today**, which Amazon accepted.

---

## 1. Bulksheets 2.0 (Sponsored Products): how to CREATE new things

### 1a. Official columns (seller template, sheet "Sponsored Products Campaigns", 32 columns)

`Product | Entity | Operation | Campaign ID | Ad Group ID | Portfolio ID | Ad ID | Keyword ID | Product Targeting ID | Campaign Name | Ad Group Name | Start Date | End Date | Targeting Type | State | Daily Budget | SKU | Ad Group Default Bid | Bid | Keyword Text | Native Language Keyword | Native Language Locale | Match Type | Bidding Strategy | Placement | Percentage | Product Targeting Expression | Audience ID | Shopper Cohort Percentage | Shopper Cohort Type | Sites | Off-Amazon ad serving`

Allowed values (template "Config" sheet):

| Field | Allowed values |
|---|---|
| Product | `Sponsored Products` |
| Entity | `Campaign`, `Ad Group`, `Bidding Adjustment`, `Campaign Negative Keyword`, `Keyword`, `Negative Keyword`, `Product Targeting`, `Negative Product Targeting`, `Product Ad` |
| Operation | `Create`, `Update`, `Archive` (no delete) |
| Targeting Type (campaign) | `AUTO`, `MANUAL` |
| State on create | `enabled`, `paused` (Campaign Negative Keyword: only `enabled`) |
| Match Type (keyword) | `exact`, `phrase`, `broad` |
| Match Type (negatives) | `negativeExact`, `negativePhrase` |
| Bidding Strategy | `Dynamic bids - down only`, `Dynamic bids - up and down`, `Fixed bid` |
| Placement (Bidding Adjustment) | `placementTop`, `placementProductPage`, `placementRestOfSearch`, `placementAmazonBusiness` |
| Off-Amazon ad serving | `Increase reach` (default), `Limit off-Amazon spend` (column added June 2026, US) |

### 1b. Minimum fields per row when creating

| Entity | Fill these |
|---|---|
| Campaign | Product, Entity, Operation=Create, Campaign ID (temporary text), Campaign Name, Start Date, Targeting Type, State, Daily Budget, Bidding Strategy |
| Ad Group | Campaign ID (same text), Ad Group ID (temporary text), Ad Group Name, State, Ad Group Default Bid |
| Product Ad | Campaign ID, Ad Group ID, State, **SKU** (sellers use SKU, vendors use ASIN) |
| Keyword | Campaign ID, Ad Group ID, State, Bid, Keyword Text, Match Type (`exact/phrase/broad`) |
| Product Targeting | Campaign ID, Ad Group ID, State, Bid, Product Targeting Expression |
| Negative Keyword (ad group) | Campaign ID, Ad Group ID, State, Keyword Text, Match Type (`negativeExact/negativePhrase`) |
| Campaign Negative Keyword | Campaign ID, State=`enabled`, Keyword Text, Match Type (`negativeExact/negativePhrase`) |
| Negative Product Targeting | Campaign ID, Ad Group ID, State, Product Targeting Expression (`asin="B0..."`, or `brand="ID"`) |
| Bidding Adjustment | Campaign ID, Placement, Percentage (0–900) |

### 1c. Product Targeting Expression format

- One competitor product: `asin="B0XXXXXXXX"` (our files use this — correct).
- Expanded product (wider, like broad): `asin-expanded="B0XXXXXXXX"`.
- Auto targets (only in AUTO campaigns): `close-match`, `loose-match`, `substitutes`, `complements`.
- Category: `category="<category ID>"`, with optional refinements (brand, price range, star rating, Prime). The exact refinement spelling could not be checked against the official page from here. **Safe way:** create ONE category target in the console, download the bulk file, and copy the exact expression text from it. Do not guess the syntax.

### 1d. The 3 questions

- **Full template or a subset of columns?** A subset with the correct header names works. Proof: today's `bulk-upload.xlsx` had only our 25 columns and Amazon accepted all 48 rows. Header text must match exactly. Sheet name must be `Sponsored Products Campaigns`.
- **Start Date `YYYYMMDD`?** Yes (`20261004` was accepted). Use the **upload day** or a future day. Do not use a past date (older guide: blank or past = set to processing day; safer to set it right).
- **Temporary text IDs for new things?** Yes. For a new campaign/ad group, put any unique text in Campaign ID / Ad Group ID and repeat the same text on the child rows. Proof: `PETME2-SP-Feeders`, `Feeders-Exact` etc. worked today. Amazon replaces them with real numbers. For **existing** campaigns you must use the real numeric ID from a bulk download.

### 1e. Our code and JSON vs Amazon

| Check | Result |
|---|---|
| `UPLOAD_COLUMNS` header names | Match the official template (25 of 32). OK. |
| Missing columns (Native Language…, Audience ID, Shopper Cohort…, Sites, Off-Amazon ad serving) | Not needed for create. But **`Off-Amazon ad serving` is missing**, so new campaigns get the default "Increase reach" (spend can go off Amazon). Small risk for a low budget. Code change later (not now). |
| `Targeting Type` = `Manual` | Template says `MANUAL`. `Manual` was accepted today, so OK; use `MANUAL` to be safe. |
| `asin="..."` expressions | Correct format. None of the 24 targets is our own ASIN. |
| Match types `exact` / `negativePhrase` | Correct. |
| Bidding strategy text | Correct (`Dynamic bids - down only`). |
| States | Campaign `paused`, children `enabled`, negatives `enabled`. Correct. |
| Start Date `20261004` in both new files | **Must change** to the real upload day (today is already used up, see section 4). |
| Temporary IDs `PETME2-SP-Competitors`, `PETME2-SP-AllProducts` | Unique, not used before. OK. |

**Rows Amazon could reject:** only risk is the Product Ads for SKUs with no active offer (section 2). Everything else matches the format that worked today.

---

## 2. Product Ad for a SKU with 0 stock / no active offer

- Sponsored Products only serves for products that are **buyable and win the featured offer (Buy Box)**. Out of stock = the ad does not show.
- In bulk, such a row is either **rejected** with an error like "Product is ineligible for advertising" / invalid SKU (common when the offer is inactive or has no price), or **created but shown as "Ineligible"** (out of stock / not buyable). Bulk downloads show "Eligibility status" and "Reason for ineligibility" columns.
- **Cost: $0.** SP is cost-per-click. No impressions = no clicks = no charge. But it adds clutter, uses rows of the 50/day limit, breaks our rule "under 10 days of stock: pause its ads", and the keywords will look like "no traffic" in reports.
- 11 of 13 Product Ads in `allproducts-changes.json` are like this (5 filters, 3 grooming, 1 supplement, 2 feeder+waterer). All have 0 FBA stock and no price. Two are **not PETME2 brand** (`2in1_FEEDER` = ROJECO, `MULTI_GROOMNG_KIT` = FIXR).

**Recommendation:** remove these 11 Product Ads and their 4 ad groups and 10 keywords now. Add them back when each product has stock (≥ 21 days) and an active price. Ask the owner about the 2 non-PETME2 items.

---

## 3. Ad options for PETME2 (FBA, ~$125/day sales, low budget)

Cost numbers are general benchmarks: SP median CPC about $0.82 in the US, pet supplies about $0.75–$1.50 per click, pet CPCs rose fastest in 2025 (+23%). Median SP ACOS about 28–32%. Sponsored Brands CPC about 20–30% higher than SP.

| Option | What it does | Cost | Pros | Cons | Now or later |
|---|---|---|---|---|---|
| **SP Auto** | Amazon picks searches and product pages (close, loose, substitutes, complements) | Low; you set bid per group | Finds new search terms and competitor ASINs for free; easy | Some waste; less control | **Later (day 14).** $3–5/day, bid $0.30–0.40, to feed keyword and ASIN ideas. Our Broad ad groups do this job for now. |
| **SP Keyword – Exact** | Only that search (and close variants) | Highest CPC per keyword, best conversion | Most control, best ACOS | Low reach | **Now** (live). Main money maker. |
| **SP Keyword – Phrase** | Search contains the phrase | Medium | Good middle step | Some waste | Later, as a test (queue Test 2). |
| **SP Keyword – Broad** | Related searches | Lower bids, more waste | Discovery | Needs negatives often | **Now** (live, low bids). Harvest winners to Exact. |
| **SP Product Targeting – ASIN** | Your ad on a competitor's product page / results | Often lower CPC than keywords | Steal sales from weaker, pricier, lower-rated rivals | Works only if our offer is better (price, rating, reviews); data is slow | **Now, small** ($3–5/day, bids $0.25–0.50). Pick rivals that are more expensive or rated lower than us. |
| **SP Product Targeting – Category** | All products in a category, with brand / price / rating filters | Medium | Wide reach, easy | Wastes money without filters | Later. Use filters: price above ours, rating below ours. |
| **Sponsored Brands** (needs Brand Registry) | Logo + headline + 3 products, Store, or video at top of search | CPC 20–30% above SP; Amazon suggests ≥ $10/day | Brand awareness, video converts well, new-to-brand data | Needs logo, Store, video; more cost | **Later (after day 30)**, if PETME2 is brand registered. Start with video on the stainless fountain and the camera feeder. |
| **Sponsored Display** (needs Brand Registry) | Remarketing to people who viewed your or similar products; product targeting on detail pages | Low CPC, low conversion | Wins back lost shoppers | Hard to measure; easy to waste | **Later (after day 30)**. Small "views remarketing" test only. |

### Placement and bidding advice for a low budget start

- **Bidding strategy:** keep `Dynamic bids - down only` for all new campaigns. It never raises bids above what we set. Do not use "up and down" (can raise top-of-search bids up to +100%).
- **Placement adjustments:** keep **0%** for the first 14 days. Then test top-of-search +25% on ONE campaign (queue Test 3). For the competitor campaign, a product-page adjustment test (+10% to +25%) makes more sense than top-of-search, but only after day 14.
- **Off-Amazon ad serving:** for small budgets choose `Limit off-Amazon spend` (set in the console now, or add the column to the upload code later).
- **Margin warning:** the $19.99 fountains have little margin (break-even ACOS about 25% if cost is ~$5). Keep their bids at $0.25–0.30. Get the product cost per ASIN from the owner.
- **Do not put the three $19.99 fountains in one ad group** (campaign plan): they compete and split data. Both new files do this (`Comp-Fountains`, `More-Fountains22`). Low bids make it acceptable, but watch it.

---

## 4. Guardian verdict on the two prepared files

### Rule checks

| Rule | competitors-changes (37 rows) | allproducts-changes (33 rows) |
|---|---|---|
| Rows ≤ 50 per day | OK alone. **But today already has 48 uploaded rows + 2 enables = 50.** No more changes today. Both files together = 70 > 50. | Same. |
| Bids ≤ max_bid $1.00 | OK (max $0.50) | OK (max $0.40) |
| New campaign created PAUSED | OK | OK |
| Total budget ≤ daily_spend_cap $20 | Now $18. +$5 = $23 → **over cap** | +$5 → $28 total with both → **over cap** |
| Inventory (≥ 10 days stock, else no ads) | OK, all 8 SKUs have 112+ days | **FAIL**: 11 SKUs have 0 stock |
| Brand | OK | 2 products are not PETME2 brand |
| No deletes | OK | OK |
| Start date | `20261004` → must be the upload day | same |

Emergency-stop risk: Amazon may spend up to 2× a campaign's daily budget on one day. With $28 of budgets and a $20 cap, one busy day over $30 would trigger our emergency stop (1.5 × cap). So the **cap must be at least the sum of budgets**.

### Verdict

- **competitors-changes.json: WAITING FOR OWNER.** Good format. Needs: cap raise to ≥ $23 (or $28 if both), new start date, and owner APPROVED.
- **allproducts-changes.json: BLOCKED as it is.** Remove the 11 out-of-stock Product Ads + their ad groups and keywords. What is left (campaign + "2.2L Fountains - Exact" ad group + 2 ads + 4 keywords = 8 rows) can go to the owner.

### Safest launch order

1. **Today (2026-10-04): nothing more.** 50 changes already done. Campaigns are on day 1 (watch only).
2. **Owner decides** (only the owner can): raise `daily_spend_cap` to **$28** (or $23 if only competitors). Keep `max_changes_per_day` at 50 — do not raise it; split uploads by day instead.
3. **2026-10-05: competitors file** (37 rows), start date `20261005`, campaign PAUSED. Owner enables it.
4. **2026-10-06: reduced all-products file** (8 rows), start date `20261006`, PAUSED. Owner enables it. (It could also go on 10-05 together: 37 + 8 = 45 ≤ 50, but one new campaign per day is easier to watch.)
5. **Out-of-stock products:** add them later, one ad group at a time, when stock ≥ 21 days and the offer is active.
6. **Day 14 (2026-10-18):** review. Then consider SP Auto ($3–5/day) and the placement test. Sponsored Brands / Display after day 30, if Brand Registry is confirmed.

Experiment Lab note: the competitor campaign is a new campaign, not a test. After 14 days we compare its cost per sale with the keyword campaigns (same products). Its $5/day is above the 15% test share ($3 of $20), so it is owner-approved spend, not experiment budget.

### Fixes needed in the files (before upload)

1. Both files: change `start_date` `20261004` → the real upload day (e.g. `20261005`, `20261006`).
2. allproducts: remove the 11 Product Ads with 0 stock (filters ×5, grooming ×3, supplement ×1, feeder+waterer ×2), plus ad groups `More-Filters`, `More-Grooming`, `More-Supplement`, `More-FeederWaterer` and their 10 keywords → 8 rows left.
3. Optional (safer): `targeting_type` `Manual` → `MANUAL`.
4. Optional: in `Comp-Fountains` keep only `L6-L3S1-I7Q6` (one $19.99 fountain), or accept the data split.
5. Owner (not files): approve `daily_spend_cap` ≥ $28, approve each new campaign, and set "Limit off-Amazon spend" in the console after upload. Code change later: add `Off-Amazon ad serving` to `UPLOAD_COLUMNS`.

---

## Sources

- Official Amazon seller bulksheet template (`AdvertisingBulksheetTemplate-seller.xlsx`, "Config" sheet), in [Sneakahugquick/amazon-sp-bulksheet-builder](https://github.com/Sneakahugquick/amazon-sp-bulksheet-builder)
- Our accepted upload: `outbox/2026-10-04/bulk-upload.xlsx` and `changes-log.csv` (2026-10-04)
- [Bulk operations for sponsored ads user guide (Amazon PDF)](https://m.media-amazon.com/images/G/01/api/guides/Bulk_operations_user_guide.pdf)
- [Amazon adds off-Amazon spend toggle to SP bulksheets – PPC Land](https://ppc.land/amazon-adds-off-amazon-spend-toggle-to-sponsored-products-bulksheets/)
- [New controls for offsite SP placements – Intentwise](https://www.intentwise.com/blog/new-controls-for-offsite-sponsored-products-placements)
- [Bulksheets ASIN eligibility status – Amazon Ads](https://advertising.amazon.com/resources/whats-new/asin-eligibility-status-bulk-operations)
- [Amazon product ineligible: reasons – Adspert](https://www.adspert.net/amazon-product-status-ineligible/)
- [Inventory stockouts and ad campaigns – Acadia](https://acadia.io/inventory-stockout/)
- [Amazon PPC bulk operations – Adbrew](https://adbrew.io/blog/amazon-ppc-bulk-operations)
- [Amazon Bulk Operations guide – Ad Badger](https://www.adbadger.com/blog/bulk-operations-amazon/)
- [A guide to targeting with Sponsored Products – Amazon Ads](https://advertising.amazon.com/library/guides/targeting-with-sponsored-products)
- [Amazon product targeting – Ad Badger](https://www.adbadger.com/blog/amazon-product-targeting/)
- [Dynamic bidding and placement bids – bidx](https://www.bidx.io/blog/amazons-dynamic-bidding-strategies-placement-bids)
- [Sponsored Brands guide – Amazon Ads](https://advertising.amazon.com/library/guides/sponsored-brands-what-to-know)
- [Sponsored Brands quick start – Canopy](https://canopymanagement.com/ppc-quick-start-guide-sponsored-brands/)
- [Sponsored Display guide – Adbrew](https://adbrew.io/blog/sponsored-display-ads)
- [Amazon PPC cost 2026 – Gigabrands](https://www.gigabrands.ai/blog/amazon-ppc-cost-guide)
- [Pet ads getting more expensive – Netpeak](https://netpeak.us/blog/why-your-amazon-pet-ads-are-getting-more-expensive-every-quarter-since-2025-and-how-smart-brands-manage-it/)
- [SP benchmarks – WisePPC](https://wiseppc.com/blog/amazon-sponsored-products-benchmarks/)
