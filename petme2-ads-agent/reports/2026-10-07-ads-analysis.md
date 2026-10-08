# Ads analysis: last 7 days (Sep 30 – Oct 6), from the owner's 4 reports

Files: `inbox/2026-10-07/` (search terms, targeting, hourly campaign, placement). The reports end **Oct 6**, so they don't include the Oct 7 bid raise.

## Big finding: the OLD campaigns were working; the new ones barely run
| Period | Spend | Clicks | Orders | Sales | ACOS | Conv. |
|---|---|---|---|---|---|---|
| Sep 30 – Oct 3 (old campaigns, now PAUSED) | $292 | 272 | 22 | $622 | 47% | **8.1%** |
| Oct 5 – Oct 6 (new PETME2 campaigns) | $8 | 15 | 0 | $0 | – | – |

On Oct 4 the old campaigns were paused and the new ones started. The new ones get almost no clicks, which is why there was "no traffic".

## Old campaigns: winners and losers (7 days)
| Campaign (old) | Clicks | Spend | Orders | Sales | ACOS | Verdict |
|---|---|---|---|---|---|---|
| 2L-Fountain-Brd-11 (water dispenser for cat) | 38 | $38.75 | 6 | $119.94 | 32% | ✅ restart |
| 2L-Fountain-Brd-12 (water bowls for cats) | 37 | $33.49 | 5 | $99.95 | 34% | ✅ restart |
| 3L-Feeder-Brd-4 (dog feeder automatic) | 31 | $63.23 | 3 | $149.97 | 42% | ✅ restart, block "automatic dog feeder" |
| Transparent-Fountain-Brd-New-15 | 43 | $26.63 | 2 | $39.98 | 67% | ✅ restart, lower bid |
| Veken (competitor ASIN) | 17 | $24.22 | 2 | $79.98 | 30% | ✅ restart |
| 5L-Feeder-Brd-5 (cat food container) | 18 | $22.05 | 1 | $45.99 | 48% | ✅ restart, block 2 terms |
| 5L-Feeder-Brd-6 (feeding station) | 4 | $4.70 | 1 | $45.99 | 10% | ✅ restart |
| Transparent-Fountain-Brd-10 (CPC $0.50) | 25 | $12.38 | 1 | $19.99 | 62% | ✅ restart (cheap clicks) |
| 2.2L-Steel-Tray-Broad-New-14 | 39 | $38.07 | 1 | $19.99 | 190% | ❌ keep paused |
| 3L-Feeder-Brd-3, Camera-Brd-2/7/8, Steel-Tray-Phr-13 | 20 | $28.90 | 0 | $0 | – | ❌ keep paused |

## Placements: top of search sells best
| Placement | Clicks | CPC | Orders | Conv. | ACOS |
|---|---|---|---|---|---|
| **Top of search** | 97 | $1.56 | **14** | **14.4%** | **37%** |
| Product pages | 108 | $0.83 | 6 | 5.6% | 52% |
| Rest of search | 80 | $0.73 | 2 | 2.5% | 147% |

Top of search is expensive per click but converts 2.5× better.

## Waste to block (negative exact)
- "automatic dog feeder" (3L-Brd-4): 12 clicks, $23.37, 0 orders
- "cat feeder" and "cat food dispenser" (5L-Brd-5): 8 clicks, $10.17, 0 orders

## What this changes in the plan
1. **Restart the 8 winning old campaigns** with modest budgets ($66/day total) and their old bids. They are proven: 8% conversion, ACOS 30–48%.
2. **Small fountains: do NOT pause.** At $19.99 they converted at about 15% (2L) and cost about $6.50 per order. That is a small loss per sale (profit before ads is about $2.40–3) but it builds rank and reviews. At $24.99 it becomes profitable. **Fix the price.**
3. **New PETME2 campaigns:** keep them, but with smaller budgets ($50/day total), because they barely serve.
4. **Top of search:** the owner wants +10%, so keep +10% on the new campaigns. Leave the old campaigns' placement settings as they were.

## Oct 7 orders (SP-API, all channels: ads + organic)
| Time (PT) | Product | Qty | Price |
|---|---|---|---|
| 12:54 | Stainless 3.2L fountain (QY-HHE8-0H1B) | 1 | $39.99 |
| 13:20 | Dual feeder black (93-E8EG-20UY) | 1 | $49.99 |
| 13:20 | Stainless 3.2L fountain | 1 | $39.99 |
| 17:15 | Dual feeder black | 1 | $49.99 |
Total: 4 orders, about $180 in sales, against about $92 in ad spend (both totals are estimates). It is not yet confirmed how many orders came from ads; Amazon attributes them within 1–3 days.
Oct 4–6 had 7 orders, all organic or from the old campaigns before they were paused: 2 stainless, 2 dual white, 1 5L, 2 small fountains.
