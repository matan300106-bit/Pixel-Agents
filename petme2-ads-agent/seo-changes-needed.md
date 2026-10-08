# PETME2 – SEO changes needed (audit, 2026-10-04)

Data: current listings from Amazon (SP-API) + Helium 10 Cerebro (14,405 keywords, real search volume).
Next step: the writer agents make the new text; 2 checker agents check rules + facts.

## Problems found in ALL listings

| Problem | Why it hurts | Fix |
|---|---|---|
| Top keywords are **not in the title as exact phrases** | Amazon ranks the title highest. "automatic cat feeder" (187k searches/month) and "cat water fountain" (319k) are missing as exact phrases on most listings | Put the #1 keyword right after the brand |
| **Same word more than 2 times** in 5 titles (Amazon rule since 2025) | Amazon can hide or suppress the listing | Max 2 times per word |
| Titles are 192–200 characters, full of features | Mobile shows only ~80 characters. The first 80 must sell | Brand + main keyword + size + top benefit in the first 80 characters |
| Bullets differ in count (5 to 10) and some are very short | Weak keywords in bullets, hard to read | 5 strong bullets, CAPS header + benefit, ~200–250 characters each |
| Backend search terms: **unknown** (not visible via API) | Hidden keywords may be empty or wasted | New 249-byte backend for each product (synonyms, long-tail, Spanish) |

## Product by product

| Product | Current title problem | Main keywords to win (Helium 10 searches/month) |
|---|---|---|
| **3L dual feeder WHITE** (B0GHLSQMJ9) | Starts with "Dual Automatic Pet Feeder". Missing exact "automatic cat feeder" (187k), "cat feeder" (26k), "automatic dog feeder" (32k) | automatic cat feeder · automatic cat feeder for 2 cats · cat food dispenser · automatic dog feeder |
| **3L dual feeder BLACK** (B0GHMCG8Q9) | ❗ Starts with **"Cat Treat Dispenser"**: wrong product type. "cat" used 4 times (rule break) | Same as white. Titles must match except the color |
| **5L WiFi feeder** (B0GHH8L59K) | "cat" 3 times (rule break). 200 characters, too long. Missing "cat food dispenser" (23k), "automatic dog feeder" (32k) | automatic cat feeder wifi · automatic cat feeder for 2 cats · elevated · 5L |
| **Camera feeder** (B0GTCGYZDM) | Says "Cat Automatic Feeder with Camera", not the exact phrase "automatic cat feeder with camera" (6.4k). Only 1 of 12 top keywords | automatic cat feeder with camera · cat feeder with camera · pet feeder with camera |
| **3.2L stainless fountain** (B0DR7FCLZR) | ❗ Starts with **"Luxury Smart Pet Fountain 2026"**: no brand first, and "2026" wastes space. Missing "cat water fountain" (319k), "stainless steel cat water fountain" (70k), "cat fountain" (83k) | cat water fountain · stainless steel cat water fountain · dog water fountain (97k, it ranks #402 in Dog Fountains) |
| **$19.99 fountain** (B0GHKN9DBR) | "water" 4 times, "fountain" 3 times (rule break). 10 short bullets | cat water fountain · cat fountain · water fountain for cats · quiet |
| **2.2L smart fountain** (B0GHLBGCP3) | "water" 3 times (rule break). Missing "cat fountain" (83k) and "pet water fountain" (42k) | cat water fountain · transparent · 2.2L · quiet |
| **Fountain with filters** (B0GHKRYV6W) | "water" 3 times (rule break). Missing "cat fountain", "pet water fountain" | cat water fountain with filter · stainless steel tray · 2.2L |
| **Dual feeder parent** (B0H3L6VXV6) | ❗ Keyword-stuffed: "automatic" 4×, "cat" 4×, "feeder" 5×. Suppression risk | Clean parent title like the children, without color |

## What we will deliver per product
1. **Title:** brand first, #1 keyword next, ≤ 200 characters, no word more than 2 times, the first 80 characters work on mobile.
2. **5 bullets:** CAPS header + benefit + keywords, only true features.
3. **Description**, clean, for products without A+ content.
4. **Backend search terms:** 249 bytes max, no brands or ASINs, no words repeated from the title.
5. **Attributes to fill:** color, capacity, material, special features, target species, number of bowls.
6. **Image and A+ notes:** what to show so the images match the keywords.

## Important before changing
- **Change one listing at a time**, and keep a copy of the old text. I save the old texts in `research/seo/current-listings.json`.
- **Changing the main keyword in a title** can move your rank for a few days. That's normal.
- **Black and white dual feeders:** the same title with only the color different. They share reviews.
