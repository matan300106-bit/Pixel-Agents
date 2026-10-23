# Competitor targeting check — 2026-10-04

Campaign checked: `outbox/2026-10-04/competitors-changes.json` (PETME2-SP-Competitors, 24 ASIN targets, 4 ad groups).
Read only. Nothing changed in Amazon. Optimizer proposal for Guardian.

## How this was checked

- Catalog: SP-API `catalog/2022-04-01/items/{asin}` (brand, title, capacity, features, sales rank). All 24 OK.
- Price: SP-API `products/pricing/v0/competitivePrice` (2 calls). All 24 OK, no 403. Price = new Buy Box landed price.
- "Rank" = Pet Supplies best seller rank (lower = sells more). Under ~1,000 = very strong seller.
- Star rating and review count: **not available** in the catalog attributes. Rank is used as the strength signal instead. Check stars by eye on Amazon before upload if you want.
- Replacements found with SP-API catalog keyword search + competitivePrice.

**Rule used:** KEEP when our offer looks better (lower price, same or more capacity, or better features) and it is the same product type. REPLACE when the competitor is much cheaper, or a very strong seller (rank < ~500) at the same or lower price, or a very different product.

**Wrong type / own product check:** none of the 24 targets is a PETME2 product, and none is a filter or accessory. All are real feeders/fountains. (Note: a keyword search for "cat water fountain 2.2L filter" returns mostly filter packs — do not pick replacements from that kind of search.)

---

## 1. Comp-Feeders (our ads: B0GHH8L59K $45.99 5L dual-bowl WiFi; B0GHLSQMJ9 $49.99 3L dual app + 2-way audio; B0GHMCG8Q9 $49.99 3L dual stainless)

| Competitor ASIN | Brand | Price | Capacity / feature | Rank | Our price | Verdict | Bid |
|---|---|---|---|---|---|---|---|
| B0953SDCRG | PETLIBRO | $62.99 | 3L, no app, no WiFi | 2,011 | $45.99 | KEEP — we are cheaper and have WiFi | $0.45 |
| B09S8WMJY9 | PETLIBRO | $78.99 | 5L WiFi, single bowl | 915 | $45.99 | KEEP — same 5L WiFi, $33 cheaper | $0.50 |
| B0C5X2G933 | oneisall | $49.99 | dual bowl, no WiFi (USB) | 1,351 | $45.99 | KEEP — we are cheaper and have WiFi | $0.45 |
| B0C5X4N132 | oneisall | $69.99 | 5L WiFi, 2 cats | 1,351 | $45.99 | KEEP — near copy of our 5L, $24 cheaper | $0.50 |
| B0F93L6WRN | Yuposl | $33.99 | 3L, no WiFi, battery | 2,678 | $45.99 | **REPLACE** — $12 cheaper; budget shoppers. Use **B0GTXN5MJK** HoneyGuaridan 5L dual WiFi, $69.99, rank 9,081 (backup: B09VGDGR4B PETLIBRO 5L dual WiFi $79.99) | $0.45 |
| B0D44QYZ7Z | PETLIBRO | $99.99 | 5L dual tray WiFi | 4,528 | $45.99 | KEEP — best match, we are half price | $0.55 |

## 2. Comp-CameraFeeder (our ad: B0GTCGYZDM $52.99, 3L, 1080P camera, app, 2-way audio)

| Competitor ASIN | Brand | Price | Capacity / feature | Rank | Our price | Verdict | Bid |
|---|---|---|---|---|---|---|---|
| B0B5ZGGWBQ | PETLIBRO | $122.93 | 5L, 1080P camera | 2,011 | $52.99 | KEEP — we are $70 cheaper | $0.55 |
| B0CNNM1WRB | Yuposl | $72.99 | 4L, 1080P camera | 2,678 | $52.99 | KEEP — $20 cheaper, close size | $0.50 |
| B0DCNNN5FC | Frienhund | $69.99 | 7L, 2K camera | 4,287 | $52.99 | KEEP (lower bid) — they are bigger + 2K, we are $17 cheaper | $0.40 |
| B0FCBCS9HR | Frienhund | $99.99 | 7L, two cameras | 4,286 | $52.99 | KEEP — much pricier | $0.45 |
| B0GSR1GTHW | MUBBI | $59.99 | 7L, 1080P camera | 5,384 | $52.99 | KEEP (test, low bid) — only $7 more but 7L vs our 3L | $0.30 |
| B0H7WS6PX9 | Minikey | $48.29 | 6.5L, 2K camera | 5,787 | $52.99 | **REPLACE** — cheaper AND bigger AND 2K. Use **B0GHP7LHPP** NUANTU 5L camera, $74.99, rank 41,391 (backup: B0FR4Z89KT Faroro 1080P $59.99) | $0.45 |

## 3. Comp-Stainless (our ad: B0DR7FCLZR $39.99, 3.2L / 108oz stainless)

| Competitor ASIN | Brand | Price | Capacity / feature | Rank | Our price | Verdict | Bid |
|---|---|---|---|---|---|---|---|
| B0FPFZ3C5K | Veken | $39.99 | 108oz stainless (other color $27.99) | **98** | $39.99 | **REPLACE** — #1 Cat Fountain, same size, same or lower price. We lose. Use **B0G6ZMT8T3** PETLIBRO stainless, wireless pump, $49.99, rank 1,747 | $0.45 |
| B0FDKQGRCK | PETLIBRO | $79.99 | 3L, app, Dockstream 2 | 214 | $39.99 | KEEP — strong seller but we are half price, same size | $0.45 |
| B0C8MHHVPC | Neareal | $33.24 | 108oz stainless | 255 | $39.99 | **REPLACE** — same size, $7 cheaper, strong seller. Use **B0DQC6H9FB** KittySpout stainless, $64.95, rank 3,531 | $0.45 |
| B0FVXPBX4N | Petlipo | $16.19 | 2.5L stainless | 833 | $39.99 | **REPLACE** — $24 cheaper. Use **B0FDKVJNXB** PETLIBRO cordless app 3L, $89.99, rank 1,126 (moved here from Comp-Fountains) | $0.40 |
| B0GDCZCXMY | PETLIBRO | $39.99 | 3L stainless | 1,754 | $39.99 | KEEP (test, low bid) — same price, we are a bit bigger (3.2L) | $0.30 |
| B0F2T6CXKT | IHOUONE | $24.99 | 2.6L stainless | 1,806 | $39.99 | **REPLACE** — $15 cheaper, smaller. Use **B0F2MZ4QW2** DownyPaws stainless wireless, $49.99, rank 12,014 (backup: B0BWHFS3PK FEELNEEDY 4L $43.48) | $0.40 |

## 4. Comp-Fountains (our ads: B0GHKN9DBR, B0GHLBGCP3, B0GHKRYV6W — all $19.99, 2.2L)

| Competitor ASIN | Brand | Price | Capacity / feature | Rank | Our price | Verdict | Bid |
|---|---|---|---|---|---|---|---|
| B08NC54VZN | Veken | $19.99 | 2.8L plastic, C1 Classic | **432** | $19.99 | **REPLACE** — top brand, same price, bigger. We lose. Use **B0FN7FQ7RJ** oneisall 2.2L wireless, $29.99, rank 5,428 | $0.30 |
| B0FJMBNZQ1 | Neareal | $27.98 | 2.2L stainless | 255 | $19.99 | KEEP — same size, $8 cheaper (note: a Neareal 2.2L variant B0FJMF2T4J sells at $19.98) | $0.30 |
| B0DDPYHHFX | GIOTOHUN | $24.99 | 2.2L stainless | 1,160 | $19.99 | KEEP — same size, $5 cheaper | $0.30 |
| B0F5BF98CW | ATMZIQXR | $24.99 | 2.6L stainless | 753 | $19.99 | KEEP — $5 cheaper | $0.25 |
| B0FBS5L5BY | BalimoPet | $18.99 | 2.2L stainless + 3 filters | 2,120 | $19.99 | **REPLACE** — cheaper and more filters. Use **B0BF5CQMKX** PETKIT Eversweet Solo SE 1.85L, $24.99, rank 5,215 (smaller and pricier than ours) | $0.30 |
| B0FDKVJNXB | PETLIBRO | $89.99 | 3L cordless, app | 1,126 | $19.99 | **REPLACE (move)** — too far from a $19.99 basic fountain. Move it to Comp-Stainless (see above). Here use **B0FP56XQJG** VinDox 2.2L ceramic, $29.99, rank 6,695 | $0.25 |

---

## Summary of changes proposed

- KEEP 14, REPLACE 10 (1 of them is a move to another ad group).
- Bids: keep the $0.25–$0.55 range, max_bid $1.00. Fountain group stays low ($0.25–$0.30) because $19.99 products have small margin.
- Campaign setting "Dynamic bids – down only" and $5/day budget: fine for a test.

## Extra option: category targeting

Add 1–2 category targets with refinements, at low bid ($0.25–$0.35):
- Automatic Cat Feeders, price $55–$130, rating 4.0 and up → feeder + camera ads.
- Cat Fountains, price $45–$90 → stainless ad. Price $23–$35 → $19.99 fountains.
- Exclude brands Veken and Neareal in the fountain categories (strong + cheap).
Then harvest the best converting ASINs from the search term report into this campaign after 2 weeks.

## Best practice source (web, 2026)

- Target competitors with similar products but weaker price/reviews/features ("offensive ASIN targeting"). — [eva.guru](https://eva.guru/blog/the-role-of-asin-targeting-in-amazon-ads/), [Perpetua](https://perpetua.io/blog-amazon-ppc-ads-product-targeting-campaigns/)
- Categories can be refined by price, rating and brand. — [SellerApp](https://www.sellerapp.com/blog/amazon-product-category-targeting-strategies/)
- Move high-converting ASINs from auto campaign search terms into manual ASIN targeting. — [ecombrainly](https://ecombrainly.com/amazon-product-targeting/)
