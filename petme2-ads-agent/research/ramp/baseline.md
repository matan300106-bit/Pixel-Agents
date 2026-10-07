# Ramp baseline — PETME2 Amazon ads (2026-10-07)

Analyst, read only. Facts from the repo files. **Unknown = we have no file for it.**

## 1. Money per product

Rules used:
- Price = the **new price we asked for on Amazon** (Chrome prompt 4, 2026-10-06). **Not confirmed live** (see risks). Second row of numbers = old price, in case the change did not save.
- Cost, shipping and FBA fee = `products.yaml` (owner, 2026-10-04). Referral = 15% of price.
- Break-even ACOS = profit before ads ÷ price. **Target ACOS = 80% of break-even** (house rule in `products.yaml`).
- **Max affordable CPC = price × target ACOS × CVR.** CVR assumption **8% / 10% / 12%** (we have no real CVR yet). Middle column (10%) is the planning number.
- Break-even CPC (10% CVR) = the point where ads eat all profit. Never bid above it.

| ASIN | Product | Price (new) | Cost+ship | Fees (ref+FBA) | Profit before ads | Break-even ACOS | Target ACOS | Max CPC @8% | **@10%** | @12% | Break-even CPC @10% |
|---|---|---|---|---|---|---|---|---|---|---|---|
| B0GTCGYZDM | Camera feeder 3L | $54.99 | $24.26 | $16.64 | $14.09 | 25.6% | 20.5% | $0.90 | **$1.13** | $1.35 | $1.41 |
| B0GHMCG8Q9 | Dual feeder 3L black | $51.99 | $23.16 | $15.86 | $12.97 | 24.9% | 20.0% | $0.83 | **$1.04** | $1.25 | $1.30 |
| B0GHLSQMJ9 | Dual feeder 3L white | $51.99 | $23.16 | $15.86 | $12.97 | 24.9% | 20.0% | $0.83 | **$1.04** | $1.25 | $1.30 |
| B0GHH8L59K | 5L WiFi feeder (launch) | $54.99 | $24.26 | $20.50 | $10.23 | 18.6% | 14.9% | $0.65 | **$0.82** | $0.98 | $1.02 |
| B0DR7FCLZR | Stainless fountain 3.2L | $39.99 | $13.23 | $12.90 | $13.86 | 34.7% | 27.7% | $0.89 | **$1.11** | $1.33 | $1.39 |
| B0GHKN9DBR | Fountain 2L quiet | $24.99 | $7.72 | $10.51 | $6.76 | 27.1% | 21.6% | $0.43 | **$0.54** | $0.65 | $0.68 |
| B0GHLBGCP3 | Fountain 2.2L clear | $24.99 | $7.72 | $10.65 | $6.62 | 26.5% | 21.2% | $0.42 | **$0.53** | $0.64 | $0.66 |
| B0GHKRYV6W | Fountain 2.2L steel tray | $24.99 | $7.72 | $10.06 | $7.21 | 28.9% | 23.1% | $0.46 | **$0.58** | $0.69 | $0.72 |

**If the new price did NOT save on Amazon** (old live price):

| Product | Old price | Profit | Break-even ACOS | Max CPC @10% | Break-even CPC @10% |
|---|---|---|---|---|---|
| Camera feeder | $52.99 | $12.39 | 23.4% | $0.99 | $1.24 |
| Dual feeders | $49.99 | $11.27 | 22.5% | $0.90 | $1.13 |
| 5L WiFi feeder | $45.99 | $2.58 | 5.6% | **$0.21** | $0.26 |
| Stainless 3.2L | $39.99 (unchanged) | $13.86 | 34.7% | $1.11 | $1.39 |
| 3 small fountains | $19.99 | $2.37–2.96 | 12–15% | **$0.19–0.24** | $0.24–0.30 |

Note: `products.yaml` still holds the 2026-10-04 prices (52.99 / 49.99 / 49.99 / 39.99 / 21.99). It is out of date; numbers above are recalculated.
Market check: Helium 10 typical CPC on top-10 keywords = **$0.94 feeders, $0.88 fountains** (`research/pricing-analysis-2026-10-04.txt`). So at 10% CVR only camera, dual and stainless can pay market CPC. 5L and small fountains cannot.

## 2. Campaign structure (V2, live since 2026-10-04)

| Campaign | Ad groups | V2 budget (10-04) | Prompt 5 budget (10-07) | After rollback | Strategy now (if rollback applied) |
|---|---|---|---|---|---|
| Feeders \| Exact | Dual-Exact (8 kw), Camera-Exact (6 kw), WiFi-Exact (5 kw) | $12 | $20 | $20, or ×1.5 (max $35) if it sold | down only |
| Fountains \| Exact | Stainless-Exact (10 kw), Small fountains-Exact (5 kw, 3 products) | $8 | $12 | $12 or ×1.5 | down only |
| Competitors \| ASIN | 5 groups, 28 ASIN targets | $15 | $20 | $20 or ×1.5 | down only |
| Brand \| Exact | 3 kw, all 8 products | $3 | $5 | $5 or ×1.5 | down only |
| Keyword Test \| Phrase | 5 groups, ~180 phrase kw (Helium 10) | $13 | $20 | $20 or ×1.5 | down only |
| Discovery \| Auto | 5 groups (4 auto targets each) | $5 | $15 | $15 or ×1.5 | down only |
| Waiting For Stock | filters + supplement | $2 (paused) | paused | paused | – |
| **Total enabled** | | **$56** | **$92** | ≤ **$120** cap | |

Bid history (all done by the owner's Chrome agent, on screen, no bulk file):

| Date | Change | Caps (camera / stainless / dual / 5L / small fountains / brand) | TOS |
|---|---|---|---|
| 10-04 V2 | start bids: exact $0.55–0.83, small fountains $0.20–0.24, comp $0.24–0.65, auto $0.20–0.40 | – | 0% |
| 10-05 | to suggested LOW end, max +50% | 0.85 (feeders), 5L 0.70 … | – |
| 10-06 prompt 4 | to suggested MIDDLE, never lower | 1.30 / 1.30 / 1.25 / 1.10 / 0.55 / 0.60 | +30% |
| 10-07 prompt 6 | max(old ×1.30, suggested); Exact+Comp up&down; auto $0.90 | 1.50 / 1.50 / 1.40 / 1.30 / 0.75 / 0.80 | +50%, PP +20% |
| 10-07 rollback | ×0.70 (×0.55 if ≥$5 spend & 0 orders), keep bids with orders, auto $0.55 ($0.40 small), all down only, min $0.30 | 1.00 / 1.00 / 0.95 / 0.85 / 0.50 / 0.50 | +10%, PP 0% |

**Unknown:** the real bid per keyword today (Chrome reports never saved to the repo), whether prompts 4/5/6/rollback were fully applied, which campaigns got the 2 orders, final budgets after rollback. `changes-log.csv` has one line saying rollback TOS +20%, the prompt says +10% — the prompt is the latest.

## 3. Data we have (spend / clicks / orders)

| Source | What | Status |
|---|---|---|
| `inbox/` | Bulk file, search term, targeting, campaign reports | **Folder does not exist. No ads report ever downloaded.** |
| `data/` | Only `2026-10-03` products snapshot (price, stock, 60-day units) | No ads data |
| `reports/daily/` | 10-03, 10-04 | Both say "no ads data yet" |
| Owner (chat, 10-06) | "still zero traffic" after 10-05 raise | no numbers |
| Owner (chat, 10-07) | ~$92 spent in ~1 hour after prompt 6, **2 sales**, keywords unknown | no file |

So: **no clicks, CPC, CTR, CVR or ACOS by keyword**. Organic 60-day units (to 10-03): stainless 60, 5L 51, 2L 30, clear 13, tray 12, camera 9, dual black 9, dual white 9.
Rough math on today: $92 / ~1 h with bids up to $1.50 → ~70–100 clicks; 2 orders → **~2–3% CVR, ~$46 per order** (ACOS roughly 90–180%). Very small sample, but far below the 8–12% assumption.

## 4. Key risks

| Risk | Fact | Effect on ramp |
|---|---|---|
| Prices not confirmed on Amazon | Prompts 1/3/4 asked for new prices; no confirmation saved. Market page on 10-07 showed camera **$52.99** (we asked $54.99). Prime Big Deal Days Oct 6–7 lowered competitor prices. | At old prices, 5L max CPC $0.21 and small fountains $0.19–0.24. Rollback caps ($0.85 / $0.50) would lose money on every sale. **Check prices first.** |
| 5L WiFi feeder | Rollback cap $0.85 > max CPC $0.82 even at $54.99 | Cap it at ≤ $0.80 (launch: accept a little more only if owner says so) |
| Low reviews | Camera feeder **3.8★ / 25 reviews** vs competitors 4.1–4.6★ / 1K+. Stainless fountain has 12 of 23 critical reviews in the owner's sheet. | Lower CVR than 10% likely → use the 8% column for camera at first |
| Real CVR unknown | Today ~2–3% CVR on paid clicks (estimate) | Max CPC must be re-checked after 7 days of real data |
| Budget burn speed | Full day budget gone in ~1 h | Day-parting not possible in SP; only lower bids/TOS keep it alive all day |
| Multi-product ad groups | Small fountains, Brand, Auto-$19.99 use one bid for 3–8 products | Use the lowest product max |
| Stock | 10-03 snapshot: camera 262, dual 137/138, 5L 97 (~113 days), stainless 397, small fountains 285–373. All > 21 days. Filters/supplement = 0 (paused). Snapshot is 4 days old. | No stock limit now; recheck before scaling |
| Late data | Amazon attribution lags 1–2 days | The 2 sales may grow; don't judge yesterday alone |
| Season | Q4 / Halloween / BFCM coming → CPC rises | Leave headroom under the caps |

## 5. Suggested max bid caps for the ramp (from the 10% CVR column, rounded down)

| Product group | Cap (if new price live) | Cap (if old price) | Rollback cap |
|---|---|---|---|
| Camera feeder | $1.10 (start ≤ $0.90 because of 3.8★) | $0.95 | $1.00 |
| Stainless 3.2L | $1.10 | $1.10 | $1.00 |
| Dual feeders | $1.00 | $0.90 | $0.95 |
| 5L WiFi feeder | $0.80 | $0.20 (or pause) | $0.85 ⚠ |
| Small fountains (3) | $0.50 | $0.20 (or pause) | $0.50 |
| Brand / mixed groups | lowest of products inside | | $0.50 |

## LIVE price check (SP-API getMyPrices, 2026-10-07 evening) — confirms the risk
| SKU | Product | Live Amazon price | Planned |
|---|---|---|---|
| 2H-2T1T-CJC3 | Camera feeder | 52.99 | 54.99 |
| 93-E8EG-20UY | Dual black | 49.99 | 51.99 |
| LW-EZAJ-KKZD | Dual white | 49.99 | 51.99 |
| QO-7VBS-CVT4 | 5L feeder | 54.99 | 54.99 ✅ |
| L6-L3S1-I7Q6 | 2L quiet fountain | 19.99 | 24.99 |
| SD-85ET-IOZ3 | 2.2L clear fountain | 19.99 | 24.99 |
| JE-LQEW-9EHL | 2.2L tray fountain | 19.99 | 24.99 |
Price prompt (Chrome prompt 4 part 1) was NOT applied except the 5L. Plan must use live prices until updated.
