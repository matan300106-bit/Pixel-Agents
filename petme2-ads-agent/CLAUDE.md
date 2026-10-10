# PETME2 Ads Team — Project Brief

You are building and running an AI ads team for **PETME2**, an Amazon pet-products brand (water fountains, smart feeders). The team manages Amazon PPC (Sponsored Products first, then Sponsored Brands and Sponsored Display) for **all PETME2 products**, runs **once per day**, and keeps testing to lower the cost per sale while keeping or growing sales.

The owner's English is a second language. Write every report and question in **simple, short English**.

---

## 1. Main goal

Lower the cost of every sale (ACOS and TACOS) **without losing sales**.
Cheap ads that sell nothing are not a win. The real target is **more profit from ads**.

- **Launch** products: accept higher ACOS to gain ranking and reviews.
- **Growth** products: keep ACOS near break-even, grow sales.
- **Profit** products: push ACOS down, protect margin.

Break-even ACOS per product = (price − product cost − shipping per unit − Amazon fees) ÷ price.

---

## 2. Connections

- **Seller Central data** (products, prices, fees, FBA inventory, sales/orders): the owner's own **SP-API private app**. Region: North America. Marketplace: US (ATVPDKIKX0DER). Keys are read from `.env` only: `LWA_CLIENT_ID`, `LWA_CLIENT_SECRET`, `SP_API_REFRESH_TOKEN`.
- **Ads data and ad changes: NO Ads API. Use the website through the browser** (Claude in Chrome, logged in to the owner's account). All ads access goes through one swappable "ads source" layer (`ads_source/`), so the Ads API can replace the browser later without rebuilding the team.
  - **Reading (automatic, daily):** open advertising.amazon.com, download the bulk file (Bulk operations, last 60 days) and the Sponsored Products search term, targeting, and campaign reports, and save them to `inbox/YYYY-MM-DD/`. Prefer downloads over reading screens one by one: faster and more reliable.
  - **Changes:** never click through hundreds of edits. Guardian puts all approved changes into ONE bulk upload file in `outbox/`. Uploading it in the Ads console is a change to the account, so it happens only after the owner says "approved" in the chat; then upload it in the browser and confirm the result on the website.
  - **If logged out, asked for a 2-step code, or shown a CAPTCHA:** stop, do not try to get around it, and tell the owner. Never enter passwords.
  - If a page looks different than expected, take a screenshot, explain in simple English, and stop instead of guessing.
- **Gmail** (optional, read only): search for factory/Alibaba invoices to find product cost per unit.
- Never store passwords, tokens, or API keys anywhere except `.env`. Never print or log them.

---

## 3. The team (6 agents + 1 manager)

Create each agent as a Claude Code subagent in `.claude/agents/`.

| # | Agent | Job | Can change the account? |
|---|-------|-----|-----|
| 0 | **Manager** (main session) | Runs the daily routine in order, passes data between agents, makes the final call | Only through Guardian |
| 1 | **Collector** | Pulls ads data, sales, inventory, prices, fees. Saves a daily snapshot in `data/` | No |
| 2 | **Analyst** | Calculates ACOS, TACOS, ROAS, CPC, CTR, CVR, break-even per product, campaign, keyword, and search term. Finds waste and winners | No |
| 3 | **Optimizer** | Daily bid changes, negative keywords, search-term harvesting, budget moves | Proposes only |
| 4 | **Experiment Lab** | Designs and runs tests (bids, budgets, placements, strategies). Measures results, keeps winners | Proposes only |
| 5 | **Guardian** | Checks EVERY proposed change against the rules and limits. Approves, blocks, or sends to owner | Executes approved changes |
| 6 | **Reporter** | Daily report, weekly report, experiment results | No |

Only **Guardian** executes changes (for now: by writing one bulk upload file in `outbox/`, uploaded in the browser only after the owner approves). Every other agent proposes.

---

## 4. Files

```
petme2-ads-agent/
├── CLAUDE.md                 ← this brief (project rules)
├── settings.yaml             ← limits, goals, mode (owner approves)
├── products.yaml             ← every ASIN: price, cost, fees, goal, break-even ACOS
├── data/YYYY-MM-DD/          ← daily raw snapshots
├── changes-log.csv           ← every change: date, item, before, after, reason, agent
├── pending-approval.md       ← big changes waiting for the owner
├── experiments/              ← one file per test
├── learnings.md              ← what worked / didn't, kept forever
├── reports/daily/ and reports/weekly/
├── inbox/                    ← ads files downloaded by the browser
├── outbox/                   ← bulk upload files with approved changes
├── ads_source/ and sp_api/   ← data access code
├── .env                      ← keys (owner fills in, never shared)
├── docs/how-to-download-reports.md
└── .claude/agents/ and .claude/commands/daily-run.md
```

---

## 5. Modes (in settings.yaml)

1. **audit** — read only. Collect, analyze, report. No changes. *(Start here.)*
2. **supervised** — every change goes to `pending-approval.md`.
3. **auto** — small changes run automatically; big changes still need approval.

Only the owner changes the mode. Never change it yourself.

---

## 6. First run (setup) — read only

1. Test the SP-API connection. Use the browser to download today's ads files into `inbox/` (steps in `docs/how-to-download-reports.md`).
2. Pull all PETME2 products: ASIN, title, price, Amazon fees, stock, sales (last 60 days).
3. Pull all campaigns, ad groups, keywords, targets, search terms (last 60 days).
4. Product cost: search Gmail for supplier invoices. Show the owner what you found, per ASIN, and ask to confirm. If not found, ask for ONE number per product.
5. Calculate break-even ACOS for each product.
6. **Suggest** settings: goal per product (based on age, reviews, sales trend), total daily budget (based on current spend), max bid, target ACOS per product. Write them to `settings.yaml` and `products.yaml` marked `status: suggested`.
7. Full audit report: wasted spend, best keywords, missing campaigns, structure problems, top 10 actions.
8. Ask the owner to approve the settings. Stay in **audit** mode until they do.

---

## 7. Daily routine (`/daily-run`)

1. **Collector**: pull fresh data. Ignore the **last 2 days** for decisions (Amazon attribution is late).
2. **Analyst**: compare last 7 / 14 / 30 days vs targets.
3. **Guardian**: check inventory first (see safety rules).
4. **Optimizer**: propose daily changes.
5. **Experiment Lab**: check running tests, end finished ones, propose new ones.
6. **Guardian**: review every proposal → execute / block / send to approval. Apply anything the owner marked APPROVED.
7. **Reporter**: write the daily report. On Mondays, also the weekly report.
8. Update `changes-log.csv` and `learnings.md`.

---

## 8. Optimizer rules

**Bids**
- Keyword ACOS above target (≥ 10 clicks): lower bid toward target. Formula: new bid = current bid × (target ACOS ÷ actual ACOS).
- Keyword ACOS well below target with good sales: raise bid to win more traffic.
- Max change: **±20% per day** per keyword. Same keyword: wait **3 days** between changes.
- Never above `max_bid` in settings.

**Waste (negatives / pause)**
- Search term with spend ≥ 1.5 × the product's target cost per sale and 0 orders → add as negative exact.
- Keyword with clicks ≥ max(15, 2 × average clicks per order) and 0 orders → lower bid 30%, or pause if already lowered once.

**Harvesting**
- Search term with ≥ 2 orders and ACOS below target (from auto/broad/phrase) → add as exact keyword in a manual campaign, and add negative exact in the source campaign.

**Budgets**
- Campaign runs out of budget AND ACOS below target → raise budget up to +25%, within the total daily cap.
- Campaign ACOS far above target for 14 days → cut budget 20%.

---

## 9. Experiment Lab rules (the testing team)

Purpose: keep trying new setups to find a cheaper cost per sale. Every test must be measured, not guessed.

**Rules for every test**
- Change **one thing at a time**.
- Write a file in `experiments/` BEFORE starting: hypothesis, what changes, control, start date, end rule, success metric.
- Use a **control** where possible (a similar campaign or product that does not change), or compare with the 14 days before.
- Run at least **14 days** or until **100+ clicks**, whichever is longer. Don't judge early.
- Max **3 tests at the same time**. Max **15%** of total daily budget for tests.
- Success = lower cost per sale (or ACOS) with the same or more orders.
- At the end: keep the winner, undo the loser, write the result in `learnings.md`.
- Don't repeat a test that already failed unless something important changed (price, season, new reviews).

**Test ideas (rotate through them)**
- Bid level: −15% vs +15% on a keyword group.
- Budget level: lower vs higher daily budget on a profitable campaign.
- Top-of-search placement adjustment: 0% vs 25% vs 50%.
- Bidding strategy: "dynamic down only" vs "up and down" vs "fixed".
- Match types: same keyword in exact vs phrase vs broad.
- Winner isolation: move a top keyword into its own single-keyword campaign.
- Product targeting: target competitor ASINs vs categories.
- New campaign types (Sponsored Brands, Sponsored Display) — needs owner approval.

---

## 10. Guardian — safety rules (never break these)

**Owner approval always needed for:**
- Creating any new campaign (create it PAUSED, then ask).
- Raising total daily ad spend above `daily_spend_cap`.
- Any bid above `max_bid`.
- Any budget increase above `max_budget_increase_without_approval`.
- Archiving anything. Changing mode. Anything not covered by these rules.

**Never:**
- Delete anything (pause instead).
- Change listings, prices, or anything outside advertising.
- Make more than `max_changes_per_day` changes in one run.

**Inventory protection**
- Less than 21 days of stock: lower that product's bids 30%, no tests.
- Less than 10 days of stock: pause its ads. Tell the owner.
- Back in stock: restore previous bids from `changes-log.csv`.

**Emergency stop**
- If total spend yesterday was more than 1.5 × the daily cap, or ACOS doubled vs the 7-day average: stop all automatic changes, report, and wait for the owner.

**Undo:** every change is in `changes-log.csv` with the old value, so it can be reversed.

---

## 11. Owner approval flow

`pending-approval.md` lists each big change with a number, what, why, and expected result. The owner writes **APPROVED** or **NO** next to each one. The next daily run applies the approved ones and clears the list. Items with no answer after 7 days expire.

---

## 12. Reports (simple English)

**Daily report** (`reports/daily/YYYY-MM-DD.md`, max one page)
1. Top line: spend, sales, orders, ACOS, TACOS — vs yesterday and vs last 7 days (green/red arrows).
2. What I changed today, and why (short list).
3. Experiments: running / finished / results.
4. Waiting for your approval (count + link).
5. Alerts: low stock, spend spikes, problems.

**Weekly report** (Mondays): trends per product, money saved vs last week, best and worst keywords, experiment results, what the team learned, 3 recommendations.

Optionally email the daily report to the owner's own Gmail address only.

---

## 13. settings.yaml (filled during first run, approved by owner)

```yaml
mode: audit                 # audit | supervised | auto
daily_spend_cap: TBD        # total $ per day, all campaigns
max_bid: TBD                # highest $ per click allowed
max_budget_increase_without_approval: 25%
max_bid_change_per_day: 20%
max_changes_per_day: 50
experiment_budget_share: 15%
max_running_experiments: 3
min_stock_days_for_ads: 10
report_email: TBD
```

---

## 14. How to run the code (technical notes)

- Install: `pip install -r requirements.txt`
- Keys: copy `.env.example` to `.env` and fill it. `.env` is in `.gitignore` and must never be committed, printed, or logged.
- Test SP-API: `python -m sp_api.test_connection`
- Products table (ASIN, title, price, FBA stock, units 60d) + snapshot in `data/YYYY-MM-DD/`: `python -m sp_api.snapshot`
- Ads files: the browser saves them in `inbox/YYYY-MM-DD/` (steps in `docs/how-to-download-reports.md`). Then `python -m ads_source.import_day [YYYY-MM-DD]` reads them and writes clean CSV files to `data/YYYY-MM-DD/`.
- Bulk upload file (Guardian only): `python -m ads_source.make_upload outbox/YYYY-MM-DD/approved-changes.json` writes `outbox/YYYY-MM-DD/bulk-upload.xlsx`. It refuses in `audit` mode, refuses deletes, refuses archive without owner approval, refuses bids above `max_bid`, and refuses more than `max_changes_per_day`.
- `ads_source` setting in `settings.yaml` picks the ads data source (`browser` now, `ads_api` later).

---

## 15. Owner preferences (standing)

- 2026-10-06, owner: "always do whatever is needed, don't ask me." Do the work directly (Shopify store data, theme copies, content, SEO, Search Console, review requests, reports). Only hand the owner the steps no tool can do (publishing a theme, installing apps, logins/2FA, Seller Central and Ads console clicks via Chrome prompts).
- Still log every change in `changes-log.csv` with the old value so it can be undone. Never delete what can't be restored, never invent claims, keep supplement wording compliant.

---

## 16. Side project: Cat Town (Instagram + web page)

Cat Town work moved to its own session (owner, 2026-10-06: keep this session for ADS). Everything needed is in `social/cat-town/HANDOFF.md` (state, files, links, how to render/upload). In this ADS session, don't start Cat Town work; point the owner to the Cat Town session.
