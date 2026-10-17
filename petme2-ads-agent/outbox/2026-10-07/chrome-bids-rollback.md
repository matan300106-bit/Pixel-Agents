# PETME2 Amazon Ads: lower bids (budget ran out in 1 hour)

You are helping PETME2 on **Amazon Ads** (advertising.amazon.com, US marketplace).

**Problem:** we raised bids today and the campaigns spent their whole daily budget in about 1 hour.
**Goal:** lower bids so the same budget lasts the full day and we get more clicks per dollar.

## Rules
- Work only in **Campaign Manager → Sponsored Products**.
- Change **only** bids, bidding strategy, placements and the budgets in Step 6, as listed below.
- Change daily budgets **only** as in Step 6.
- Do **not** create, delete, archive or rename anything.
- Do **not** change prices, listings, products or negatives.
- Before changing anything, write down what you see (Step 1).

---

## Step 1: Record today first (important, don't skip)
Date range: **Today**. For every campaign write down:
name · daily budget · spend · impressions · clicks · orders · sales · "Out of budget" yes/no.

Then open **each campaign → Targeting**, sort by **Spend** (high to low), and write down the **top 10 keywords/targets**:
keyword/target · current bid · clicks · spend · orders.

## Step 2: Bidding strategy
Set **every** enabled campaign to **Dynamic bids – down only**.

## Step 3: Placements
In every enabled campaign:
- **Top of search (first page): +10%**
- **Product pages: 0%**
- Rest of search: 0%

## Step 4: Lower every keyword and product-target bid
For every enabled keyword and product target (skip "Waiting For Stock"):

**New bid = current bid × 0.70**, then make sure it is **not above** the new max for that product:

| Product in the ad group | New max bid |
|---|---|
| Camera feeder (ASIN B0GTCGYZDM) | **$1.00** |
| Stainless 3.2L fountain (ASIN B0DR7FCLZR) | **$1.00** |
| Dual feeder 3L (black or white) | **$0.95** |
| 5L WiFi feeder | **$0.85** |
| Small fountains 2L / 2.2L ($24.99) | **$0.50** |
| Brand campaign ("petme2" searches) | **$0.50** |
| Ad group with several products | use the **lowest** max |

**Extra cut:** if a keyword/target spent **$5 or more today with 0 orders**, use **current bid × 0.55** instead (same max).

Never go below **$0.30**. Round to 2 decimals.

**Do NOT lower** a keyword/target that got **1 or more orders today**. Keep its bid as it is.

**Examples:**
- Camera feeder, current $1.50 → 1.50 × 0.70 = $1.05 → above $1.00 max → **$1.00**
- Dual feeder, current $1.04 → 1.04 × 0.70 = **$0.73**
- Spent $6 today, 0 orders, current $1.40 → 1.40 × 0.55 = **$0.77**

## Step 5: Auto campaign (Discovery)
Set close match, loose match, substitutes and complements to **$0.55** each ($0.40 in small-fountain-only ad groups).

## Step 6: More budget for the campaigns that sold
We had **2 sales today**. Find the campaign(s) with **1 or more orders today** (from Step 1).
- Each of those campaigns: **daily budget × 1.5** (example $20 → $30), max **$35** per campaign.
- Do not change the budget of campaigns with 0 orders.
- Total of all enabled campaigns must stay at or under **$120/day**.

---

## Report back (copy this format)
1. **Today before changes:** campaign | budget | spend | clicks | orders | sales | out of budget?
2. **Top spenders:** campaign | keyword/target | bid | clicks | spend | orders
3. **Bid changes:** campaign | ad group | keyword/target | old bid | new bid
4. **Strategy and placements** per campaign, after the change
5. **Budget changes:** campaign | orders today | old budget | new budget
6. Any warning or error you saw
