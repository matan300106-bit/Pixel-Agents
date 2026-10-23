# Chrome prompt 6 — raise bids (owner asked 2026-10-07)

Paste everything below the line into Claude in Chrome (advertising.amazon.com, PETME2 US).

---

You are helping PETME2 on Amazon Ads (US). Goal: raise bids so ads win more clicks. Change ONLY bids and placement settings. Do not change budgets, products, prices or listings. Do not create or delete anything.

STEP 1 - Campaign Manager > Sponsored Products > open each ENABLED campaign > each ad group > Targeting (keywords and product targets). Skip the "Waiting For Stock" campaign.

STEP 2 - For EVERY enabled keyword / product target:
new bid = the HIGHER of (old bid x 1.30) and (Amazon "Suggested bid" middle number),
then cap it at the max for that product (use the product the ad group advertises):
| Product in the ad group | Max bid |
|---|---|
| Camera feeder (B0GTCGYZDM) | $1.50 |
| Stainless 3.2L fountain (B0DR7FCLZR) | $1.50 |
| Dual feeder 3L, black or white | $1.40 |
| 5L WiFi feeder | $1.30 |
| Small fountains 2L / 2.2L ($24.99) | $0.75 |
| Brand campaign ("petme2" searches) | $0.80 |
| Mixed ad group (several products) | use the LOWEST max of its products |
Never lower a bid. Round to 2 decimals.

STEP 3 - Auto campaign (Discovery): set close match, loose match, substitutes and complements each to $0.90 (small-fountain-only ad groups: $0.60). Never lower an existing higher bid.

STEP 4 - Placements: in every enabled campaign set "Top of search (first page)" to +50% and "Product pages" to +20%. Leave "Rest of search" at 0%.

STEP 5 - Reply with a table: campaign | ad group | keyword/target | old bid | suggested bid | new bid. Then list the placement settings per campaign, and any warning or error you saw.
