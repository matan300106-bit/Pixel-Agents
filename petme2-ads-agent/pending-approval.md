# Waiting for your approval

Write **APPROVED** or **NO** next to each number. The next daily run applies the approved ones.
Items with no answer after 7 days expire.

1. **New campaign: PETME2 | SP | Feeders | Manual** (created PAUSED). LOW COST: $10/day, 3 ad groups, 4 feeders, 9 keywords, 6 negatives, bids $0.40–$0.65.
   Why: no feeder ads plan yet; "automatic cat feeder" is a very big search. Details: `campaign-plan.md`. → **APPROVED** (owner, chat, 2026-10-04)
2. **New campaign: PETME2 | SP | Fountains | Manual** (created PAUSED). LOW COST: $8/day, 3 ad groups, 2 fountains, 8 keywords, 5 negatives, bids $0.30–$0.55.
   Why: 3.2L stainless fountain is the best seller. Details: `campaign-plan.md`. → **APPROVED** (owner, chat, 2026-10-04)

Ready rows (48, under the 50/day limit): `outbox/2026-10-03/proposed-changes.json`. Before upload I still need: mode change to `supervised` + `max_bid` and `daily_spend_cap` in settings.yaml (only you). Owner said START on 2026-10-03.

Upload file ready: `outbox/2026-10-04/bulk-upload.xlsx` (48 rows). UPLOADED by owner 2026-10-04. Logged in `changes-log.csv`.

3. **New campaign: PETME2 | SP | Competitors | Manual** (PAUSED). $15/day, 24 competitor products, bids $0.25–$0.65 (each target its own bid). → **APPROVED** (owner asked for the upload file, chat 2026-10-04)
4. **New campaign: PETME2 | SP | All Products | Keywords** (PAUSED). $6/day, 2.2L fountains + out-of-stock groups (paused). → **APPROVED** (owner asked for the upload file, chat 2026-10-04)
5. **New campaign: PETME2 | SP | Brand | Exact** (PAUSED). $3/day, "petme2" searches, all in-stock products. → **APPROVED** (owner asked for the upload file, chat 2026-10-04)
6. **Live campaign fixes** (Part C of `ads-draft-2026-10-04.md`): higher honeymoon bids, new keywords, negatives. Needs your bulk file download first. →

Upload file for 3+4+5: `outbox/2026-10-04/bulk-upload-2-new-campaigns.xlsx` (83 rows). UPLOADED by owner 2026-10-04: 77 OK, 6 failed (out-of-stock product ads, expected). Campaigns created PAUSED. Full draft: `ads-draft-2026-10-04.md`.

7. **New campaigns: Keyword Test | Phrase ($13/day, 184 keywords incl. Helium 10) + Discovery | Auto ($5/day)** (PAUSED). Upload **2026-10-05**. File: `outbox/2026-10-05/bulk-upload-3-test-campaigns.xlsx` (240 rows). Draft: `test-campaigns-draft.md`. →

8. **V2 REBUILD (replaces 1–7):** owner archives all old campaigns and uploads ONE file `outbox/2026-10-04-v2/PETME2-ALL-CAMPAIGNS-V2.xlsx` (427 rows, 7 campaigns, $58/day, all PAUSED). Draft: `ads-v2-draft.md`. → **APPROVED** (owner: "make me something to upload 1 time", chat 2026-10-04). UPLOADED and campaigns 1–6 turned ON by owner 2026-10-04. Items 1–7 replaced by V2.

## 2026-10-05 — Bid raise, careful version (owner: "lower side, we are still testing")
Owner instruction in chat counts as APPROVED. Done by the owner's Chrome agent on screen, no bulk upload.
- New bid = Amazon suggested bid LOW end (first number of the range), never lower than now, never more than +50% over now, capped:
  - 3L camera feeder, 3L dual feeder black/white: max $0.85
  - 5L WiFi feeder (launch): max $0.70
  - 3.2L stainless fountain: max $1.00
  - $21.99 fountains (B0GHKN9DBR, B0GHLBGCP3, B0GHKRYV6W): max $0.45
  - Brand campaign: max $0.45. Auto default bids: same caps.
- Top of search +15% on Exact campaigns only, strategy "down only".
- Ramp: every 3 days, if a keyword has < 100 impressions, +15% (within max_bid $1.50). Review 2026-10-08.
