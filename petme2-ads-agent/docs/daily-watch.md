# PETME2 daily watch (runs every morning)

Owner asked 2026-10-11: "verify yourself, have few agents that are checking daily, if you need something from me let me know."

The routine runs every day at about 9:40 New York time in the main ADS session. It runs 3 checker agents at the same time, then a Guardian check, then one short message to the owner.
Read only. The watch never changes Amazon, Shopify or ads. Changes still go through Chrome prompts the owner runs.

## Agent 1: Sales checker (SP-API, read only)
- Orders per day for the last 14 days (Pacific time), units per product: last 7 days vs the 7 before.
- Canceled or pending orders.
- Compare with yesterday's daily report.

## Agent 2: Listing checker (SP-API, read only)
- Live price per SKU vs `products.yaml` and the price plan.
- Buy Box: do we own it? Any other seller or lower offer?
- BSR per ASIN vs the last report (flag if more than 30% worse over 3 days).
- FBA stock and days of cover (units/day over the last 14 days).

## Agent 3: Ads checker (files in `inbox/`)
- If new ads reports or a Chrome reply arrived since the last run: spend, clicks, orders, CPC, ACOS per campaign; waste (≥ $8 spend, 0 orders); winners (orders and ACOS under break-even).
- Check that the last Chrome prompt was done as written (bids within caps, total budget ≤ $120/day, no surprises).
- If nothing new arrived: say "no ads data" and what to ask the owner for.

## Guardian (after the 3 agents)
Raise an ALERT when:
- Stock under 21 days (lower bids 30%) or under 10 days (pause ads).
- Lost the Buy Box, a price changed without a plan, or a listing problem.
- Orders fell by 50% or more vs the 7-day average (2 days in a row).
- Ad spend above $180 in one day (1.5 × cap), or ACOS doubled.
- A product got worse: BSR more than 30% worse, or conversion (Unit Session %) down 25% or more week over week. Then propose a listing fix (title, images, price, coupon) in a Chrome prompt. Never invent claims.

## Output
1. `reports/daily/YYYY-MM-DD.md`: one page, simple English.
2. If changes are needed: a Chrome prompt in `outbox/YYYY-MM-DD/` (small steps, ±20% max, follow the Guardian rules in CLAUDE.md).
3. A row in `changes-log.csv` for anything proposed or changed.
4. Commit and push to `petme2-campaign-plan`.
5. One short message to the owner: 3 lines of results, then "I need from you:" with only what no tool can do (Chrome prompts, reports, prices, photos).
