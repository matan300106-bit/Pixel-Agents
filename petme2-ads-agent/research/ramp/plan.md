# PETME2 ads: slow ramp plan, Oct 8 to Oct 21, 2026

Planner, 2026-10-07. Status: **plan**. Nothing has been changed on Amazon yet. The owner applies changes through the Chrome agent.
Based on: `baseline.md` (with the LIVE price table), `method.md`, `settings.yaml`, `docs/ramp-up-rules.md`, `outbox/2026-10-07/chrome-bids-rollback.md`, CLAUDE.md §8–11.

Owner's words this plan follows: "start a little bit up, no drastic" · "few agents checking, testing" · "2 sales, increase budgets on them, let them go longer" · "top of search 10% only".

**Main idea:** the bids decide how fast the money is spent. The budget only sets the limit. Today the bids were too high, so the money ran out in 1 hour. From now on we change **one small thing at a time** and wait 3 days before we judge it.

---

## 1. Starting point for Thursday, Oct 8

### 1.1 Max bid per product (uses LIVE Amazon prices)
Cap = profit before ads × 8% conversion (= our target ACOS at 10% conversion), rounded down. We use real prices, not the planned ones. Oct 7 showed only ~2–3% conversion on 2 orders, so the caps are a ceiling, not a target; the stop-loss (§4) protects us until we have 7 days of real data.

| Product | Live price | Profit before ads | **Max bid now** | Rollback max | Max bid once the new price is live |
|---|---|---|---|---|---|
| Camera feeder B0GTCGYZDM | $52.99 | $12.39 | **$0.90** (3.8★ → lower conversion) | $1.00 | $54.99 → $0.95 (stay $0.90 until 30 clicks) |
| Dual feeder 3L black / white | $49.99 | $11.27 | **$0.85** | $0.95 | $51.99 → $0.95 |
| 5L WiFi feeder B0GHH8L59K | $54.99 ✅ | $10.23 | **$0.75** | $0.85 | already live |
| Stainless 3.2L B0DR7FCLZR | $39.99 (check on Oct 8) | $13.86 | **$1.00** (can go up to $1.10 in steps) | $1.00 | no change planned |
| Small fountains 2L / 2.2L / 2.2L tray | $19.99 | $2.37–2.96 | **PAUSE ads** | $0.50 | $24.99 → restart at $0.35, max $0.50 |
| Brand ("petme2" searches) | – | – | **$0.50** | $0.50 | same |
| Auto (Discovery) | – | – | **$0.55** | $0.55 | same |
| Ad group with several products | – | – | lowest max of the products inside | | |

**Hard rules:** never above these caps. Never below $0.30. A keyword that already has orders keeps its bid, **but not above the cap**.

### 1.2 Small fountains at $19.99: **pause the ads** (decision)
- At $19.99 we keep only $2.37–2.96 per sale. To make money we must pay **≤ $0.19–0.24 per click**.
- Market price for fountain clicks is $0.71–1.31. A $0.20 bid gets almost no impressions, so "very low bids" gives no data and only costs effort. Also the Chrome rollback has a $0.30 minimum, which **loses money on every click**.
- They sell organically (285–373 in stock, 55 sales in 60 days). Pausing the ads costs us almost nothing.
- So: **pause** the "Small fountains-Exact" ad group and the 3 small-fountain products (B0GHKN9DBR, B0GHLBGCP3, B0GHKRYV6W) in every other campaign. Pause, never delete.
- **Restart** on the day the price is $24.99 on Amazon: bids $0.35, max $0.50.

### 1.3 Do the rollback values need changes? **Yes, small ones.**
| What | Rollback said | Change to |
|---|---|---|
| Camera feeder max | $1.00 | **$0.90** |
| Dual feeder max | $0.95 | **$0.85** |
| 5L WiFi feeder max | $0.85 | **$0.75** |
| Small fountains | max $0.50 | **pause** (see 1.2) |
| Keywords with orders | "keep bid" | keep bid, **but cut to the cap** if above it |
| Stainless, brand, auto, min $0.30, TOS, strategy, budgets | – | **no change** |

All other rollback values stay. These are cuts only (no raise on Oct 8). Chrome prompt: `research/ramp/chrome-oct8.md`.

### 1.4 Budgets, strategy, placements (from Oct 8)
| Campaign | Budget | Note |
|---|---|---|
| Feeders \| Exact | $20, or $30 if it sold on Oct 7 (×1.5, max $35) | keep the extra budget from the rollback |
| Fountains \| Exact | $12, or ×1.5 if it sold | now only stainless (small fountains paused) |
| Competitors \| ASIN | $20, or ×1.5 if it sold | |
| Brand \| Exact | $5, or ×1.5 if it sold | |
| Keyword Test \| Phrase | $20, or ×1.5 if it sold | |
| Discovery \| Auto | $15, or ×1.5 if it sold | |
| Waiting For Stock | paused | |
| **Total** | **$92 + the extra for the 2 selling campaigns, max $120** | `daily_spend_cap` = $120 |

- **Bidding strategy:** Dynamic bids – **down only**, every campaign, the whole 14 days.
- **Top of search: +10%** (never more, owner rule). **Product pages: 0%.** Rest of search: 0%.

---

## 2. Day by day, Oct 8 → Oct 21

Check-ins: **Monday and Thursday**. Other days: a 2-minute look at spend only, no changes (except stop-loss).
**ONE change per campaign per check-in.** A change is one of: bids, or budget. Strategy and TOS do not change in these 14 days (only exception: test 3 sets TOS to 0% in Feeders | Exact from Oct 19; TOS never goes above +10%).

**The 3 numbers to read every check-in (last 3 full days, per campaign):**
1. What time did it run out of budget? (hourly report, or "out of budget" note)
2. Orders and cost per order (spend ÷ orders).
3. Average CPC vs our bid.

| Date | What to do | Change allowed |
|---|---|---|
| **Thu Oct 8** | Run `chrome-oct8.md`: record Oct 7, fix caps, pause small fountains, check the stainless price, download reports. | Only the fixes in 1.3. **No raises.** |
| Fri Oct 9 – Sun Oct 11 | Watch. Each evening: spend so far and the hour the money ran out. | Stop-loss only (table §4). |
| **Mon Oct 12** (first real check, data Oct 9–11) | Read the 3 numbers. Mark each campaign: **A** (ran out before 15:00), **B** (ran out after 18:00 or spent 60–100%), **C** (spent < 30% of budget). | **A:** −15% on its top 10 spenders. **B:** hold. **C:** **+10%** on targets with < 50 impressions in 3 days (not above cap). Start tests 1 + 2 (§3). |
| Tue Oct 13 – Wed Oct 14 | Watch. | Stop-loss only. |
| **Thu Oct 15** (data Oct 12–14) | Same 3 numbers. Check: are the new prices live? (if yes → new caps from table 1.1, small fountains restart). | **A:** −15% top spenders. **C:** +10–15% on targets not changed since Oct 12 and < 50 impressions. **B with ≥ 2 orders and cost per order < profit:** budget **+20%** (once per 7 days). |
| Fri Oct 16 – Sun Oct 18 | Watch. | Stop-loss only. |
| **Mon Oct 19** (7-day review, data Oct 12–18) | Real conversion per product (orders ÷ clicks). If a product has 30+ clicks: new cap = profit × its conversion × 0.8. Total spend this week vs last week. | One change per campaign, same A/B/C rules. Budget +20% only for campaigns not raised on Oct 15. Total spend grows max +20% per week. Start test 3 if tests 1–2 run clean. |
| Tue Oct 20 – Wed Oct 21 | Watch. Write the 2-week summary for the owner on Oct 21 (what sells, cost per order, next caps). | Stop-loss only. Next check-in: Thu Oct 22. |

**Rules for every raise** (all must be true):
- Campaign is **not** out of budget before 18:00 on 2 of the last 3 days.
- Target has **< 50 impressions** in 3 days and **no clicks-without-sales** problem.
- No change on this target in the last 3 days.
- New bid ≤ product cap (§1.1) and ≤ $1.50 (`max_bid`).
- Step size: **+10%** on Oct 12, **+10–15%** later. Never more than +20%.

**Budget raise:** max **+20%**, max once per 7 days per campaign, only with ≥ 2 orders and cost per order below profit before ads. Total stays ≤ $120 (more needs owner OK).

---

## 3. Tests (max 3, each in its own file in `experiments/` before start)

| # | Campaign | What changes | Control | Start / length | Success rule |
|---|---|---|---|---|---|
| 1 | Fountains \| Exact, Stainless-Exact (10 kw) | Split keywords by spend into 2 halves. Half A: bid +15% (max $1.10). Half B: unchanged. | Half B | Oct 12, 14 days or 100+ clicks (the longer) | A wins if it gets more orders **and** cost per order ≤ $13.86 and not > 25% worse than B. Else keep B's bids. |
| 2 | Competitors \| ASIN (28 targets) | Split targets in 2 halves. Half A: bid −15%. Half B: unchanged. | Half B | Oct 12, 14 days or 100+ clicks | A wins if cost per order is ≥ 25% lower with about the same orders. Then cut all competitor bids 15%. |
| 3 | Feeders \| Exact | Top of search **0%** for 7 days, then back to +10% for 7 days. Compare placement report. | same campaign, before/after | Oct 19, 14 days | Keep the setting with lower cost per order. (TOS never above +10%.) |

- Tests 1 and 2 count as the ONE bid change for that campaign on Oct 12. While a test runs, nothing else changes in that campaign (stop-loss still applies).
- If there are < 30 clicks after 14 days → "not enough data", keep the cheaper setting, no repeat until the price changes.

---

## 4. Stop-loss (do it right away, any day, overrides tests)

| Level | When | Action |
|---|---|---|
| Keyword / target | Spend ≥ 1× profit before ads, 0 orders (camera $12, dual $11, 5L $10, stainless $14) | Bid **−30%** |
| Keyword / target | Spend ≥ 2× profit, 0 orders, or 2nd hit | **Pause** it (never delete) |
| Search term | Spend ≥ 1.5× target cost per sale, 0 orders | Negative exact |
| Campaign | Budget gone **before 12:00** | Same day: −20% on top 10 spenders; check down-only and TOS +10% |
| Campaign | 3-day cost per order > profit before ads (≥ 3 orders) | No more raises; −20% on top spender |
| Campaign | After a raise, CPC up > 25% in 3 days and no more orders | Undo the raise (old value in `changes-log.csv`) |
| Account | Spend in 1 day > $180 (1.5× cap) | Stop all changes, tell the owner |
| Account | 3-day spend > 1.3× planned, or 7-day cost per order > profit | Freeze all raises 7 days, tell the owner |

---

## 5. What the owner must do (short list)

1. **Thu Oct 8 morning:** paste `research/ramp/chrome-oct8.md` into Chrome. Send the report back.
2. **Save the reports** the Chrome agent downloads into `petme2-ads-agent/inbox/` (create the folder). Every Mon + Thu: new Search term, Targeting, Campaign (hourly) and Placement reports, last 7 days.
3. **Fix the prices** (Seller Central, outside ads): camera $54.99, dual $51.99 (both colors), small fountains $24.99. Tell us the day they are live. Until then we use the live prices.
4. **Budget flexibility:** if Campaign Manager → Settings shows a budget rollover / flexibility option, set it to **25%** (stops a $92 day from spending up to $184). If you do not see it, skip.
5. Approve or say NO to: pausing the small fountain ads (§1.2), and tests 1–3. Pausing is not in our standing rules, so it needs your OK: **pasting `chrome-oct8.md` with Step 5 in it = OK.** If you say NO, delete Step 5 before you paste (the small fountains then stay at their rollback bids, max $0.50, and lose a little on every sale).
6. Tests 1–3 touch whole campaigns, which is more than the 15% test budget in `settings.yaml`. Only the changed half counts as test money (tests 1+2 ≈ $16/day ≈ 17%). Say OK, or we run test 2 only on Oct 12 and test 1 after it.
