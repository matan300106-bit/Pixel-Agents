# PETME2 Amazon Ads: Oct 8 morning check + small fixes

You are helping PETME2 on **Amazon Ads** (advertising.amazon.com, US marketplace).

**Situation:** on Oct 7 a big bid raise spent the whole daily budget in about 1 hour. Then we lowered bids (rollback). Amazon prices are lower than we planned, so 3 products need a lower max bid, and the small fountains ($19.99) lose money on ads.
**Goal today:** record yesterday, check the rollback is in place, make a few small CUTS, pause the small-fountain ads, and download reports. **No bid raises today.**

## Rules
- Work only in **Campaign Manager → Sponsored Products** (plus the Reports page in Step 7).
- Change **only** what Steps 2–5 say. Do **not** raise any bid or budget. Do **not** change any daily budget.
- Before you change anything, write down what you see (Step 1 and the old bid in Step 3).
- Do **not** create, delete, archive or rename any campaign, ad group, ad, keyword or target. Pause only what Step 5 says. (Creating and downloading reports in Step 7 is OK.)
- Do **not** upload any file (no bulk upload).
- Do **not** change prices, listings, products or negatives.
- If logged out, asked for a code, or shown a CAPTCHA: stop and tell the owner.
- If a page looks different than expected: take a screenshot, explain, and stop.

---

## Step 1: Record yesterday (Oct 7) first (don't skip)
Date range: **Yesterday**. For every campaign write down:
name · daily budget · spend · impressions · clicks · orders · sales · "Out of budget" yes/no.

Then date range **Today**: for every campaign write down spend so far and the time you checked.

## Step 2: Check the rollback is in place (look, fix only if wrong)
For every enabled campaign check:
- Bidding strategy = **Dynamic bids – down only**. If not → set it.
- Placements: **Top of search +10%**, **Product pages 0%**, rest of search 0%. If not → set it.
- Daily budget. Write it down. Do not change it.
- If any campaign budget is above **$35**, or all enabled budgets add up to more than **$120**: do not fix it, write it under "warnings" in the report.

## Step 3: Lower bids that are above the new max
For every enabled keyword and product target (skip "Waiting For Stock" and the Auto campaign, see Step 4):
**If the current bid is above the max below, set it to the max. If it is at or below the max, do not touch it.**
This also applies to keywords/targets that had orders.

| Product in the ad group | New max bid |
|---|---|
| Camera feeder (ASIN B0GTCGYZDM) | **$0.90** |
| Dual feeder 3L, black or white (B0GHMCG8Q9, B0GHLSQMJ9) | **$0.85** |
| 5L WiFi feeder (B0GHH8L59K) | **$0.75** |
| Stainless 3.2L fountain (B0DR7FCLZR) | **$1.00** |
| Brand campaign ("petme2" searches) | **$0.50** |
| Ad group with several products | use the **lowest** max of the products in it (ignore the 3 small fountains, they get paused in Step 5) |
| Ad group with **only** small fountains | do not change bids, it gets paused in Step 5 |

**Examples:**
- Camera feeder, current $1.00 → **$0.90**
- Dual feeder, current $0.73 → no change
- 5L feeder, current $0.85 → **$0.75**
- Brand campaign, current $0.60 → **$0.50**
- A bid below $0.30 → leave it, do not raise it

## Step 4: Auto campaign (Discovery)
Close match, loose match, substitutes, complements: if a bid is above **$0.55**, set it to **$0.55**. Do not raise any.

## Step 5: Pause small-fountain ads (they are $19.99, ads lose money)
Small fountains = **B0GHKN9DBR** (2L), **B0GHLBGCP3** (2.2L clear), **B0GHKRYV6W** (2.2L steel tray).
- Campaign "Fountains | Exact" → ad group for the small fountains → **Pause the ad group**.
- In every other campaign (Keyword Test, Discovery Auto, Competitors, Brand): open each ad group → **Ads** tab → **Pause** the product ads of these 3 ASINs.
- If an ad group has **only** these 3 products → pause the whole ad group.
- **Never** pause the stainless fountain (B0DR7FCLZR) or any feeder.

## Step 6: Check 1 price
Open the Amazon product page of the stainless fountain **B0DR7FCLZR**. Write down the price you see. Do not change it. If it is not $39.99, add it to the warnings.

## Step 7: Download reports
Reports → Sponsored Products → create and download (date range: **last 7 days**):
1. **Search term** report
2. **Targeting** report
3. **Campaign** report, time unit **Hourly** (if Hourly is not offered: Daily)
4. **Placement** report (Campaign report with "Placement")
Also: Bulk operations → download the **bulk file** (last 30 days).
Write down each file name. The owner will save them into the `inbox/` folder.

---

## Report back (copy this format)
1. **Yesterday (Oct 7):** campaign | budget | spend | impressions | clicks | orders | sales | out of budget?
2. **Today so far:** campaign | spend | time checked
3. **Settings check:** campaign | strategy | TOS % | product pages % | budget | what you fixed
4. **Bid changes:** campaign | ad group | keyword/target | old bid | new bid
5. **Paused:** campaign | ad group | ASIN or "whole ad group"
6. **Stainless price seen:** $
7. **Files downloaded:** report | file name
8. **Warnings:** budgets above $35 or total above $120, stainless price not $39.99, anything you could not do, any error you saw
