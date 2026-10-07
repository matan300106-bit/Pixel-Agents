# Slow ramp and testing method (Sponsored Products)

Owner: Experiment Lab / Optimizer. Status: **research, suggested method**. Nothing was changed on Amazon. Date: 2026-10-07.
Context: on 2026-10-07 we raised all bids by +30% or to the suggested bid (up to $1.50), switched to dynamic up & down and set top of search to +50%, all on the same day. The full ~$92 daily budget was spent in about 1 hour and brought 2 sales (`learnings.md`). The rollback is in `outbox/2026-10-07/chrome-bids-rollback.md`.
This method sits on top of `docs/ramp-up-rules.md` and CLAUDE.md sections 8–10, and does not replace them. Where this file is stricter, use this file during the ramp.

Source quality: Amazon publishes **no** official bid-step size or "learning period". All step sizes below come from agency and tool blogs plus our own numbers, so treat them as cautious defaults. Amazon's own facts (budget averaging, TOS impression share, budget rules) are marked **[Amazon]**.

---

## 0. The numbers that drive everything (our products)

Break-even CPC = profit before ads × conversion rate (CVR). New brand with few reviews: plan on **8% ad CVR** (sponsored-ads benchmark for pet supplies is 6–12%, see §2).

| Product | Price | Profit before ads | Break-even CPC @ 8% CVR | @ 12% CVR | H10 suggested CPC, main terms |
|---|---|---|---|---|---|
| Camera feeder B0GTCGYZDM | $52.99 | $12.39 | **$0.99** | $1.49 | $1.66–2.21 ("cat feeder with camera" $2.21) |
| Dual feeders 3L | $49.99 | $11.27 | **$0.90** | $1.35 | $0.92–1.52 ("automatic cat feeder" $1.39) |
| 5L WiFi feeder (launch) | $49.99 | $5.98 | **$0.48** | $0.72 | $1.50–1.95 |
| Stainless fountain B0DR7FCLZR | $39.99 | $13.86 | **$1.11** | $1.66 | $0.86–1.27 ("cat water fountain" $0.86) |
| Small fountains (3 ASINs) | $21.99–24.99 | ~$4.1–4.7 | **$0.34–0.37** | $0.50–0.56 | $0.71–1.31 |

Prices and profit come from `products.yaml`. The H10 figures are from `research/helium10/selected-keywords.md` (Cerebro, 2026-10-04). Check the small-fountain price: `products.yaml` says $21.99, but the brief says $24.99.

What this means:
- **Head terms for feeders cost more than we can pay** (suggested bid ≥ break-even). For the camera feeder and the dual feeders, bid below the suggested bid. Win on long-tail and exact terms, and accept a low top-of-search share.
- **The stainless fountain is our one product where the suggested bid is at or below break-even.** It is the best place to scale first.
- **The small fountains and the WiFi feeder cannot win head terms.** Keep them on long-tail, ASIN targeting and auto at ≤ $0.35–0.45, or let them sell organically.
- Hard ceiling per target = **break-even CPC @ 8%** (the table above) until a target has its own CVR from 30+ clicks. After that, ceiling = profit × its real CVR × 0.8.

---

## 1. Safe step sizes and cadence

### 1.1 Bids
| Situation | Step | Cadence |
|---|---|---|
| Raise (target has < 50 impressions in 3 days, campaign NOT out of budget) | **+10–15%** (max +20%, `max_bid_change_per_day`) | **1 change per target per 3 days** |
| Raise on a target that already has clicks but no sale | **No raise** | — |
| Cut for ACOS above target (≥ 10 clicks) | bid × target ACOS ÷ actual ACOS, **max −20%** | 1 per 3 days |
| Cut for "spending with no orders" | **−30%** (§4 stop-loss) | right away when hit |
| Emergency cut (budget gone before 12:00) | **−20 to −30%** on the top 10 spenders only | same day, once |

- Vendors give 10–20% per step (Sellersprite, AdLabs). BidX waits **at least 3 days** before it touches the same keyword again. Some tools argue 10% barely moves impressions, so +15% is a sensible middle.
- Start new targets at **50–75% of Amazon's suggested bid** (Sellermetrics, Ad Badger says 20–30% under). Never start above our break-even CPC.
- The suggested bid is the median of recent *winning* bids, roughly the 25th–75th percentile **[per Amalyze]**. It says nothing about profit, and on low-volume terms it swings up to 50%. Use it as a sanity check only, never as a target.

### 1.2 Budgets
- Raise a budget by **at most +20–25%** (`max_budget_increase_without_approval` 25%), **at most once per 7 days per campaign**. Only do it when the campaign ran out of budget **after 18:00** on 2 of the last 3 days **and** its 7-day ACOS is below target with ≥ 2 orders.
- If the budget runs out **early** (before ~15:00), the bids are too high for the budget. **Lower the bids. Do not raise the budget** (Intentwise, My Amazon Guy).
- Budget averaging **[Amazon]**: the SP daily budget is averaged over the month. A single day can spend **+25% over budget**, and campaigns made after 27 Mar 2023 default to **up to +100%** (Perpetua). A $92 budget can therefore spend about $184 on one day. **Action:** in Campaign Manager → Settings, set budget flexibility to **25%** during the ramp (owner approval needed; this is an account setting).
- Total spend ramp: keep the actual daily spend inside `daily_spend_cap` (now $120). Grow **actual** total spend by at most **+20% per week**, and only while total ACOS ≤ break-even.

### 1.3 Placements and strategy
- Bidding strategy: **Dynamic – down only** on every campaign until that campaign has **≥ 3 orders and ACOS below target** over 14 days. "Up and down" can raise the bid **up to +100% on top of search** and +50% elsewhere, and it **stacks** with the placement % **[per Perpetua/BidX]**. A $1.00 bid with TOS +50% and up & down can clear at $3.00. That stack is what burned the budget today.
- Top of search: steps of **0 → +10 → +25 → +50%**, **one step per 7 days**. Only on a campaign with orders, where the TOS placement CVR beats rest-of-search. Product pages stay at 0% (lower CVR for a no-review brand).
- **Never stack levers.** In one campaign, change only ONE of {keyword bids, strategy, placement %, budget} per 3-day window (7 days for strategy and placement).

### 1.4 How long Amazon needs to settle after a change
| What you look at | Readable after | Why |
|---|---|---|
| Spend, impressions, CPC | **same day** (hourly report) / 24 h | spend reacts first (AdLabs) |
| Clicks, impression trend | **3 days** | daily noise |
| Orders, ACOS | **3 days mostly, 7 days fully** | data updates in about 12 h; orders are corrected for 72 h; the SP attribution window is **7 days [Amazon]** (BidX) |
| "Real" trend / learning | **2–4 weeks** | Bobsled, Be Bold: data "settles" after about 2 weeks |

Rule: judge **spend and impressions on 3 days**, **ACOS and CVR on 7 days (or 14 days)**, and never on yesterday alone.

---

## 2. Market CPC and conversion benchmarks (2025–2026)

**Our keywords (Helium 10 Cerebro, 2026-10-04, suggested bid / min):**
- automatic cat feeder **$1.39 / $1.19** (SV 187K) · auto cat feeder $1.52 · automatic pet feeder $1.48 · cat food dispenser $0.79
- automatic cat feeder with camera **$1.66 / $1.32** · cat feeder with camera **$2.21 / $1.45** · pet feeder with camera $1.88 · smart cat feeder $1.79
- cat water fountain **$0.86 / $0.68** (SV 319K) · stainless steel cat water fountain $1.05 · pet water fountain $0.81 · cat fountain $0.91 · kitten water fountain $1.12
- (Third-party Google estimate: "cat feeding station" $1.19, iSpionage. That is Google, not Amazon, so use it only as a cross-check.)

**General:** pet supplies SP CPC is about **$0.45–1.20** (EcomBrainly 2026), or about $0.75–1.50 with the fastest rise in 2025 (+23%) (`research/ad-options-2026-10-04.md`). The Amazon-wide average CPC is about $1.00–1.10+ in 2025 (Sellermetrics). Sponsored Brands in pet can run above $2.

**Conversion:** pet supplies listing CVR (all traffic, unit session %) is about **10–14% average**, < 7% weak, 15–20% strong (EcomBrainly / Sellermetrics). Sponsored-ads pet CVR is lower, about **6–12%**, with ACOS 30–40% and CTR 0.5–0.8% (ATTN Agency 2026). With 25 reviews at 3.8★ (camera feeder), plan on **6–8%** until our own data proves better.

Clicks needed per expected order at 8% CVR = **~12.5**. That number sets every threshold in §4.

---

## 3. Pacing spend through the day

**Amazon does not pace SP budgets evenly.** It enters every auction you qualify for until the budget is gone, so high bids plus competitive head terms make the spend front-loaded (Sellermetrics, Intentwise). **Bids are the pacing lever. The budget is only the ceiling.**

Tools, in order of use:
1. **Bids + down-only strategy** (main lever, §1).
2. **Hourly report** **[Amazon]**: Campaign Manager → Reports → Sponsored Products → Campaign, time unit "Hourly". Check daily during the ramp.
3. **Budget rules [Amazon]**:
   - *Schedule-based*: raise the budget by X% for a date range, an event or recurring **hours of the day** (console and API). They can only **raise** the budget, not lower it, and are reviewed daily. Use them later to add budget in the evening hours that convert best. **Not during the ramp** (14+ days of hourly data first; AdLabs/Ad Badger say 14–30 days).
   - *Performance-based*: raise the budget when 7-day ACOS/CVR/CTR is past a threshold. They need a **≥ $10 budget**. This is a good, safe way to "raise only if profitable" after day 14.
4. **Dayparting of bids**: there is no native hour-of-day bid control, only API or third-party tools. **Skip** for an account this small.
5. **Placement %**: §1.3.

### Signals: bid too high vs too low
| Signal (3-day window) | Means | Action |
|---|---|---|
| Out of budget **before 15:00** | **Bids too high** for the budget | −15–20% on the top spenders; do not raise the budget |
| Out of budget after 18:00, ACOS < target | Budget-limited winner | Budget +20% (1×/7 d) |
| Out of budget, ACOS > target or 0 orders | Paying for bad traffic | Cut bids, add negatives; budget unchanged |
| Avg CPC ≥ 1.3× our bid (TOS% or up & down active) | Modifiers are inflating the CPC | Remove the modifier / go back to down-only |
| Avg CPC near break-even, CVR < 6% | Bid too high for this term | −20% or move it to long-tail |
| < 50 impressions/3 d on a relevant term, bid < 50% of suggested | **Bid too low** | +15% (1×/3 d), up to the ceiling |
| Impressions OK, CTR < 0.3% | Not a bid problem (relevance, image, price) | Do not raise; review the listing or the target |
| TOS impression share **[Amazon]** < 5% on a converting exact term | Losing the top slot | TOS +10% step (only if ACOS < target) |
| Campaign spends < 30% of budget for 7 days | Bids too low or terms too narrow | +15% on targets with < 50 impressions |
| Healthy pacing | Spend ~40–60% of budget by 14:00 and runs out late evening or not at all | Hold |

---

## 4. Testing design for a tiny account, plus stop-loss

### 4.1 Cadence
- **1 change per campaign per 3 days** (one lever, §1.3). **1 change per target per 3 days.** Strategy or placement: 1 per 7 days.
- Fixed check days: Mon / Thu (3–4 day windows). Every change goes in `changes-log.csv` with its old value and the test ID.
- **Freeze rule:** while a test runs in a campaign, nothing else changes in that campaign except stop-loss actions.

### 4.2 Test designs that work with ~$5–20/day per campaign
1. **Pre/post with a control (default).** Change one lever in campaign A. Campaign B (similar, unchanged) is the control. Compare 7 days before vs 7 days after, as CPC, CVR and cost per order versus the control's drift.
2. **Split bid groups inside one ad group.** Sort the targets by spend and split them alternately into group A (+15%) and group B (unchanged). That gives about equal traffic in each arm, and both arms share the same budget and placement settings. Read the result after **≥ 100 clicks total, or 14 days** (CLAUDE.md §9).
3. **Placement test without duplicating.** Run TOS 0% for 7 days, then +25% for 7 days, in the same campaign. Read the placement report (TOS vs rest-of-search CPC/CVR). Do not duplicate campaigns to A/B placements: on a small budget the duplicates bid against each other.
4. Keep tests to ≤ 15% of the total budget and ≤ 3 at once (§9). Use Amazon's own SP experiments only if they show up in the console (not checked).

### 4.3 Minimum data before judging
| Decision | Minimum |
|---|---|
| Raise for low traffic | 3 days at the current bid |
| "No sale" cut | **≥ 25 clicks** (≈ 2× clicks per order at 8% CVR) **or** spend ≥ 1× profit before ads, with 0 orders |
| ACOS-based bid change | **≥ 30 clicks or ≥ 3 orders** (at 30 clicks / 3 orders the true CVR is anywhere from 2–27%, so change by ≤ 20%) |
| Declare a test winner | ≥ 100 clicks in total and ≥ 14 days, and the difference in cost per order is > 25%; otherwise "inconclusive", keep the cheaper setting |

### 4.4 Stop-loss rules (apply immediately, override test freezes)
**Target (keyword / ASIN) level**
- Spend ≥ **1× profit before ads** with 0 orders (camera $12.39, dual $11.27, stainless $13.86, WiFi $5.98, small fountain ~$4.20) → **bid −30%**.
- Spend ≥ **2× profit before ads** with 0 orders, or a second hit → **pause** the target (never delete).
- Search term with spend ≥ 1.5 × target cost per sale and 0 orders → negative exact (existing rule).

**Campaign level**
- Budget spent **before 12:00** → same day: cut the top 10 spenders by −20%, set down-only, set TOS to 0%. Log it as "pacing stop".
- 3-day cost per order **> profit before ads** (losing money on every sale) with ≥ 3 orders → stop all raises; next change is −20% on the top spender.
- After a raise: within 3 days the CPC rose > 25% while orders did not rise → **revert** to the logged old value.
- 7-day ACOS > break-even with ≥ 30 clicks → revert the last change in that campaign.

**Account level** (Guardian, CLAUDE.md §10)
- Yesterday's spend > 1.5 × `daily_spend_cap`, or ACOS doubled vs the 7-day average → stop all changes and report to the owner.
- **Ramp-specific:** actual total spend in any 3-day window > 1.3× the planned spend, or 7-day total ACOS > break-even → freeze all raises for 7 days.

---

## 5. Recommended ramp from today (after the rollback)

| Days | Do |
|---|---|
| 0 (today) | Rollback (×0.7, down-only, TOS +10%, product pages 0%). Set budget flexibility to 25% (owner approval). |
| 1–3 | Watch only. Check the hourly report daily: does the spend last past 15:00? |
| 4, 7, 10, 13 | Bid raises +15% only on targets with < 50 impressions and campaigns not out of budget. Stop-loss cuts at any time. |
| 7 | If one campaign still runs out before 15:00 → −15% on its top spenders. |
| 14 | Review: CVR per product. Replace the 8% assumption with real numbers, recompute the ceilings, and pick 1 test per product (Stainless first). |
| 14–30 | Max +20% total weekly spend. Performance-based budget rule (ACOS < target → +20%) on the winners. TOS steps on campaigns with ≥ 3 orders. |

---

## Sources
- Amazon Ads, SP budget best practices (daily budget averaged monthly, +25% day): https://advertising.amazon.com/library/guides/sponsored-products-budget-best-practices
- Amazon Ads, hours-of-day schedule budget rules: https://advertising.amazon.com/resources/whats-new/hours-of-day-available-for-schedule-based-budget-rules
- Amazon Ads, dynamic budget control (budget rules): https://advertising.amazon.com/resources/whats-new/dynamic-budget-control
- Amazon Ads, Top-of-search impression share: https://advertising.amazon.com/resources/whats-new/top-of-search-impression-share-metric
- Amazon Ads India help, budget rules reviewed daily and the $10 minimum: https://advertising.amazon.in/help/GNSMLANWNF344YBE
- Perpetua, daily budgets (100% vs 25% rollover): https://help.perpetua.io/en/articles/7211394-amazon-daily-budgets
- Perpetua, dynamic bidding and placement guide: https://perpetua.io/blog-amazon-ppc-advertising-dynamic-bidding-bid-strategy/
- BidX, strategy and placement case study (stacking up to ×20): https://bidx.io/blog/case-study-bidding-strategies ; attribution window and the 3-day wait: https://www.bidx.io/blog/amazon-attribution-window
- AdLabs, how long to wait between bid changes: https://adlabs.app/?p=26194 ; dayparting guide: https://adlabs.app/guides/amazon-dayparting-guide/
- Sellersprite, new product PPC launch (10–20% steps, 3–5 days): https://www.sellersprite.com/en/blog/How-to-Launch-a-PPC-Campaign-for-a-New-Product-on-Amazon
- Carbon6/ZonTools, bid increase for low impressions: https://carbon6.io/zontools-help/how-much-should-i-increase-my-bid-when-im-having-low-impressions
- Intentwise, out of budget (lower bids vs raise budget): https://wf.intentwise.com/blog/out-of-budget-issues ; budget rules: https://www.intentwise.com/blog/amazon-budget-rules
- Amalyze, bid range explained: https://amalyze.com/resources/guides/advertising/amazon-ppc-bid-range-explained ; significance: https://amalyze.com/resources/glossary/statistical-significance
- Sellermetrics, suggested bid: https://sellermetrics.app/amazon-ppc-suggested-bid/ ; CPC rising 2026: https://sellermetrics.app/rising-amazon-ad-cpcs/ ; conversion rate: https://sellermetrics.app/amazon-conversion-rate/
- Ad Badger, 2025 benchmarks: https://www.adbadger.com/blog/2025-amazon-benchmarking-insights-trends-for-optimal-performance/ ; dayparting: https://www.adbadger.com/blog/amazon-ppc-dayparting-weekparting/
- EcomBrainly, Amazon PPC cost 2026 (pet $0.45–1.20): https://ecombrainly.com/amazon-ppc-cost ; conversion rate by category: https://ecombrainly.com/amazon-conversion-rate/
- ATTN Agency, pet retail media 2026 (pet SP CVR 6–12%, ACOS 30–40%): https://www.attnagency.com/blog/pet-brand-retail-media-strategies-2026
- Bobsled, data settles after about 2 weeks: https://bobsledmarketing.libsyn.com/interpreting-your-amazon-ppc-data-for-the-truest-insights
- Internal: `research/helium10/selected-keywords.md`, `products.yaml`, `research/ad-options-2026-10-04.md`, `learnings.md`.

Note: the WebFetch of these pages was blocked by the network proxy. The figures come from search-result extracts of the pages listed, so check the key Amazon facts (budget flexibility setting, budget rules) in the console.
