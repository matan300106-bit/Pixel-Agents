# PETME2 Amazon Ads: raise budgets and bids

You are helping PETME2, a pet products brand, on **Amazon Ads** (advertising.amazon.com, US marketplace, PETME2 account).

**Goal:** the ads are not getting enough traffic. Raise daily budgets and bids so the ads start spending and winning clicks.

## Rules (read first)
- Work only in **Campaign Manager → Sponsored Products**.
- Change **only** budgets, bidding strategy, bids and placements, as listed below.
- Do **not** create, delete, archive or rename anything.
- Do **not** change prices, listings, products or negative keywords.
- **Never lower** a budget or a bid.
- If a step asks for something you can't find, skip it and say so in your report. Don't guess.
- Before changing anything, write down the current values (Step 1). We need them as a backup.

---

## Step 1: Write down the current state
Show **all campaigns**, date range **Last 7 days**. For every campaign write down:
name · state · status · daily budget · bidding strategy · impressions · clicks · spend · orders.

## Step 2: Daily budgets
Find each campaign by name (names can be slightly different) and set:

| Campaign name contains | New daily budget |
|---|---|
| Feeders + Exact | **$20** |
| Fountains + Exact | **$12** |
| Competitors | **$20** |
| Brand | **$5** |
| Keyword Test | **$20** |
| Discovery (Auto) | **$15** |
| Waiting For Stock | **leave PAUSED, don't touch** |
| Any other enabled PETME2 campaign | **$10** |

- No campaign above **$20/day**.
- Total of all enabled campaigns: **$100/day or less**.

## Step 3: Bidding strategy
- Campaigns with **"Exact"** or **"Competitors"** in the name → **Dynamic bids – up and down**.
- Discovery, Keyword Test and Brand → **Dynamic bids – down only**.

## Step 4: Make sure everything is on
Every campaign above (except Waiting For Stock) must be **Enabled**, along with its ad groups and product ads.
If an ad shows **"Not delivering"**, write down the reason (out of stock, ineligible, no Buy Box, etc.). Don't try to fix listing problems.

## Step 5: Keyword and product-target bids
Open every enabled campaign → every ad group → **Targeting**. Skip Waiting For Stock.

For **every** enabled keyword and product target:

**New bid = the higher of (old bid × 1.30) and Amazon's suggested bid (the middle number).**
Then **cap** it at the max for the product in that ad group:

| Product in the ad group | Max bid |
|---|---|
| Camera feeder (ASIN B0GTCGYZDM) | **$1.50** |
| Stainless 3.2L fountain (ASIN B0DR7FCLZR) | **$1.50** |
| Dual feeder 3L (black or white) | **$1.40** |
| 5L WiFi feeder | **$1.30** |
| Small fountains 2L / 2.2L ($24.99) | **$0.75** |
| Brand campaign ("petme2" searches) | **$0.80** |
| Ad group with several products | use the **lowest** max of those products |

Round to 2 decimals. Never lower a bid.

**Examples:**
- Old $0.80, suggested $0.95 → 0.80 × 1.30 = $1.04 → new bid **$1.04**
- Old $0.80, suggested $1.90, camera feeder → $1.90 is above the $1.50 cap → new bid **$1.50**
- Old $0.50, suggested $0.40, small fountain → 0.50 × 1.30 = $0.65 → new bid **$0.65**

## Step 6: Auto campaign (Discovery) targets
Set **close match, loose match, substitutes, complements** to **$0.90** each.
In ad groups with only small fountains, use **$0.60**. Never lower an existing higher bid.

## Step 7: Placements
In every enabled campaign:
- **Top of search (first page): +50%**
- **Product pages: +20%**
- Rest of search: **0%**

---

## Report back (copy this format)
1. **Budgets:** campaign | old budget | new budget | old strategy | new strategy | state
2. **Last 7 days:** campaign | impressions | clicks | spend | orders
3. **Bids:** campaign | ad group | keyword/target | old bid | suggested bid | new bid
4. **Placements:** campaign | top of search % | product pages %
5. **Problems:** every ad not delivering and why, plus any warning or error banner you saw
