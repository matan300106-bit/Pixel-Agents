# Oct 12: analysis of the Chrome report (pulled Oct 11, 8:55 PM PT)

## Facts
- Only the 6 PETME2 campaigns run. The old campaigns (Veken, 3L-Brd-4, 5L-Brd-5/6) were **never re-enabled**: the oct8-v2 prompt was not run.
- Enabled budgets $98/day. Top of search impression share under 5% everywhere.
- Live prices (SP-API, Oct 12): **not raised yet** (camera 52.99, dual 49.99, small fountains 19.99).

| Campaign (Oct 4–10) | Spend | Orders | ACOS | Oct 11 | Verdict |
|---|---|---|---|---|---|
| Competitors \| ASIN | $55.74 | 4 | 31% | $30.33, 3 orders, 25% (out of budget 5:58 PM) | ✅ winner (budget raised to $30 on Oct 11; let it run) |
| Fountains \| Exact | $39.03 | 3 | 32.5% | $5, 0 | ✅ near break-even (35%) |
| Discovery \| Auto | $21.45 | 1 | 53.6% | $2.61, 0 | ⚠️ small loss |
| Keyword Test \| Phrase | $106.13 | 4 | **66.3%** | $16.95, 1, 42% (out of budget daily) | ❌ biggest leak: $26.5 per order vs $13.86 profit |
| Feeders \| Exact | $10.19 | 0 | – | $0 | ⚠️ almost no traffic (bids too low to win) |
| Brand \| Exact | $0 | 0 | – | $0 | – |
| **Total** | **$232.54** | **12** | **46.5%** | $54.89, 4 orders, 34% | Oct 11 about break-even |

Oct 11 changes (from the first version of the oct11 prompt, before the audit fixes):
- "water fountain for dogs" $1.00 → $1.10 (3 orders, ACOS 41.8%: above break-even 35%, should go back).
- "dog drinking fountain" $1.00 → $1.10 (1 order, ACOS 2.5%: fine).
- PETLIBRO B0G6ZMT8T3 $0.87 → $0.96 (ACOS 33.8%: just under break-even, keep).
- Competitors budget $20 → $30 (+50%, bigger than the +20% rule, but ACOS 25–31% so keep). Keyword Test $25 → $16.

## Business report: week over week (Sep 27–Oct 3 → Oct 4–10)
| Product | Sessions | Units | Conversion |
|---|---|---|---|
| 2L fountain | 131 → 33 | 21 → 3 | 16.0% → 9.1% |
| Stainless | 78 → 238 | 5 → 15 | 6.4% → 6.3% |
| Dual white | 55 → 15 | 3 → 2 | 5.5% → 13.3% |
| Dual black | 36 → 19 | 2 → 2 | 5.6% → 10.5% |
| 5L | 51 → 25 | 3 → 1 | 5.9% → 4.0% |
| Clear 2.2L | 110 → 26 | 3 → 1 | 2.7% → 3.9% |
| Tray 2.2L | 80 → 14 | 3 → 1 | 3.8% → 7.1% |
| Camera | 18 → 13 | 1 → 0 | 5.6% → 0% |
| **Total** | **559 → 383** | **41 → 25** | |

- Units fell 41 → 25 because the small-fountain ads were paused (2L 21 → 3). That was on purpose: at $19.99 each ad sale lost about $7. **The fix is the price ($24.99)**, then restart the 2L ads. The 2L converted at 16%, so at $24.99 it can be profitable.
- No listing got worse in conversion except the 5L (price went up to $54.99) and the camera (tiny traffic). Traffic fell, not conversion. So the main problem is ads/traffic, not the listings.
- Clear 2.2L converts badly in both weeks (2.7–3.9%): listing fix needed (images/title), later.

## Plan for Oct 12 (chrome-oct12.md, small steps)
1. Keyword Test: stop the leak (back to $1.00 on "water fountain for dogs", −20% on $14+/0-order targets, negative exact for wasted search terms).
2. Feeders Exact: dual feeder keywords +20% (cap $1.05). The dual feeder converts 10–13% and the break-even CPC is about $1.13.
3. Restart Veken (stainless competitor targets) at $10, bid cap $1.00. Total $108 ≤ $120.
4. No change to Competitors, Fountains Exact, Auto, Brand.
5. Ramp tests 1–3: postponed one week (too many changes at once).
