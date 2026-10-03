# Bid ramp-up rule book — first 30 days

Owner: Optimizer. Status: **suggested** (rules only, no changes now). Date: 2026-10-03.
For: the 2 new low-cost manual SP campaigns in `outbox/2026-10-03/proposed-changes.json`.

| Campaign | Daily budget | Ad groups (start bids) |
|---|---|---|
| PETME2 \| SP \| Feeders \| Manual | $10 | Feeders-Exact $0.60 · CameraFeeder-Exact $0.65 · Feeders-Broad $0.40 |
| PETME2 \| SP \| Fountains \| Manual | $8 | Stainless-Exact $0.55 · Fountains-Exact $0.35 · Fountains-Broad $0.30 |

Goal: spend as little as possible. Start low, raise bids in small steps only where we get no traffic,
and cut fast where we pay and do not sell. These rules follow CLAUDE.md section 8 and section 10.

---

## 0. Always true (check first, every day)

- **Day 1** = the first day the campaign is enabled. Count days per campaign.
- We are in `audit` mode: every rule below makes a **proposal** only. Nothing changes without the owner.
- One keyword: max **one change every 3 days** (check `changes-log.csv`). Max **±20% per day** for bid raises.
- Max **$1.00** bid during ramp-up (owner cap). If `max_bid` in `settings.yaml` is set lower, use the lower one.
- Max **50 changes** per run. Every change goes to `changes-log.csv` with the old value.
- Product under **21 days of stock**: no bid raises (lower 30%). Under **10 days**: pause its ads, tell the owner.
- **Emergency stop**: spend yesterday > 1.5 × `daily_spend_cap`, or ACOS doubled vs the 7-day average → no changes, report, wait.
- Read data on 3-day windows (last 3 full days). Amazon data for the last 1–2 days is late; do not judge yesterday alone.
- Days 1–3: **watch only**. No bid changes (except emergency or stock rules).

Words used below:
- **Target ACOS** = from `products.yaml`. Not set yet (we need product cost). Until it is set, use a temporary
  **25%** for the $19.99 fountains and **30%** for everything else, and mark the proposal "temporary target".
- **Target cost per sale** = price × target ACOS. Example: $19.99 × 25% = about $5.00.

---

## 1. When to RAISE a bid (+15%)

Raise a keyword bid by **+15%** only when ALL are true:
1. Fewer than **50 impressions** in the last 3 days.
2. No change on this keyword in the last 3 days.
3. New bid stays at or below **$1.00** (round down to the cent; if +15% passes $1.00, set exactly $1.00).
4. Product has 21+ days of stock.
5. The campaign did **not** run out of budget in the last 3 days.
6. The keyword is not in a running test (`experiments/`).

Example (fountain broad): $0.30 → 0.34 → 0.39 → 0.45 → 0.52 → 0.60 → 0.69 → 0.79 → 0.91 → 1.00.
One step every 3 days, so a keyword needs about 27 days to reach $1.00. That is the slowest, cheapest path.

## 2. When to STOP raising

Stop raising a keyword (keep the bid as it is) when ANY is true:
- It has **50+ impressions** in the last 3 days (it now gets traffic — let it collect data).
- It reached **$1.00** (or `max_bid`). If it still has < 50 impressions at $1.00 after 6 more days:
  mark it "no traffic at max bid" and ask the owner (keep, or pause). Do not go above $1.00 without owner OK.
- It has **10+ clicks** (now the ACOS rules in section 3 decide).
- It has clicks but **0 orders** and spend ≥ 1 × target cost per sale (do not pay more for traffic that does not buy).
- The campaign **runs out of budget** (see section 6) — more bid only burns the budget sooner.
- Product stock under 21 days.

## 3. When to CUT a bid

Cut only with enough data. Never cut a keyword in its first 3 days.
- **ACOS above target, 10+ clicks**: new bid = current bid × (target ACOS ÷ actual ACOS). Max cut 20% per change.
- **No sales**: clicks ≥ max(15, 2 × average clicks per order) and **0 orders** → bid −30%.
  If it was already cut once for this reason → propose **pause** (never delete).
- Until the campaign has its first orders, "average clicks per order" is unknown: use **15 clicks**.
- After a cut, wait 3 days before the next change on that keyword.

## 4. When to ADD NEGATIVES

Check the search term report every run (Broad ad groups give most of the terms).
- Search term with spend ≥ **1.5 × target cost per sale** and **0 orders** → **negative exact** in that ad group.
  Example: fountain $19.99, target 25% → cost per sale $5.00 → negative at **$7.50** spend with no order.
- Search term that is clearly the wrong product (filter, pump, replacement, bowl only, bird, fish, other animals,
  feeder in fountains / fountain in feeders) → propose **negative phrase** at campaign level even before it spends.
  This is outside section 8, so it goes to `pending-approval.md` for the owner.
- Never add a negative that blocks one of our own exact keywords.

## 5. When to HARVEST

- Search term from a **Broad** ad group with **≥ 2 orders** and **ACOS below target** →
  1. add it as an **exact** keyword in the matching Exact ad group (same campaign, right product),
     start bid = its average cost per click, max $1.00;
  2. add it as **negative exact** in the Broad ad group it came from, so the two do not compete.
- Before day 14, harvest only if it is very clear (≥ 2 orders). Do not harvest on 1 order.

## 6. If a campaign RUNS OUT OF BUDGET

"Out of budget" = the campaign spent its full daily budget on 2 of the last 3 days.
- **ACOS below target** (with 2+ orders) → raise budget up to **+25%** (Feeders $10 → $12.50, Fountains $8 → $10),
  only if the total stays within `daily_spend_cap`. While `daily_spend_cap` is TBD, every budget raise needs owner OK.
- **ACOS above target, or no orders yet** → do **not** raise the budget. Stop all bid raises in that campaign and
  cut the bid of the keyword with the most spend and fewest orders (section 3 rules, max −20%).
- **Day 14+: ACOS far above target** (more than 1.5 × target) for 14 days → cut the campaign budget **20%**.
- Budget is never raised more than once in 3 days.

## 7. Timeline (per campaign)

| Days | What we do |
|---|---|
| 1–3 | Watch only. Check that ads serve, products are in stock, spend is under budget. |
| 4–14 | Raise checks every 3 days (days 4, 7, 10, 13). Negatives and "no sales" cuts as soon as the numbers are hit. No big decisions. |
| 14 | Review with the owner: what has traffic, what sells, set real target ACOS. Experiment Lab may start tests (see `experiments/queue.md`). |
| 15–30 | Same rules. ACOS-based cuts and harvesting become normal. Keywords in a test are frozen (no ramp-up changes). |
| 30 | Ramp-up ends. Write what we learned in `learnings.md`. Normal section 8 rules from now on. |

## 8. Open items for the owner

- `max_bid` and `daily_spend_cap` in `settings.yaml` (suggested: max bid $1.00 during ramp-up, cap $18/day).
- Product cost per ASIN, so we can replace the temporary target ACOS (25% / 30%).
