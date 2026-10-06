# Chrome prompts — 2026-10-06

## Prompt 1 — Amazon prices (Seller Central)

```
Open Seller Central > Inventory > Manage All Inventory. Change ONLY these prices (Your price), then Save each one:
- SKU L6-L3S1-I7Q6 (Quiet Cat Water Fountain 2L): 19.99 -> 27.99
- SKU SD-85ET-IOZ3 (Transparent Cat Water Fountain 2.2L): 19.99 -> 27.99
- SKU JE-LQEW-9EHL (Cat Water Fountain with Stainless Steel Tray 2.2L): 19.99 -> 27.99
- SKU QO-7VBS-CVT4 (Elevated WiFi Cat Feeder 5L): 45.99 -> 49.99
Do not set a Sale price or a List price. Do not change anything else.
If Amazon shows a "price alert" / "potential pricing error", click to confirm the price is correct.
After saving, wait 2 minutes, refresh, and tell me the price now shown for each SKU and the status (Active / Inactive / Search suppressed).
```

## Prompt 2 — Ads: find why ads are not showing, then raise bids

```
Open advertising.amazon.com > Sponsored Products > Campaigns. Date range: last 7 days. Don't create, delete or archive anything.

PART A — check and report (no changes yet):
1. For every campaign: status, daily budget, "Out of budget" yes/no, impressions, clicks, spend.
2. Open each ad group > Ads tab: is every ad "Delivering"? If any says "Not delivering", "Ineligible", "Not buyable", "Not featured offer" or "Policy", write the exact reason.
3. Any campaign "Paused", "Scheduled" or with an end date in the past? Write it.
4. Account level: any billing / payment problem banner? Write it.

PART B — bids (do this after Part A):
For each keyword and product target in ENABLED ad groups, look at Amazon's "Suggested bid" range.
- If my bid is below the LOW end of the range: set the bid to the low end, but never above the cap below.
- If my bid is already at or above the low end: leave it.
- If there is no suggested range: raise the bid by 20%, never above the cap.
Caps (max bid per click):
- Camera Feeder, Dual Feeders (white + black): $1.10
- 5L WiFi Feeder: $0.90
- Stainless Fountain 3.2L: $1.00
- The three 2L/2.2L fountains (now $27.99): $0.60
- PETME2 brand keywords: $0.45
- Auto ad groups (close/loose/substitutes/complements): same caps as the product.
Placements: in every campaign set "Top of search (first page)" to +20%. Bidding strategy: "Dynamic bids - down only". Don't change it if it's already that.
Budgets: if a campaign shows "Out of budget" in the last 7 days, raise its daily budget by 25%. Otherwise leave budgets.

At the end, give me a table: campaign | ad group | keyword/target | old bid | suggested low | new bid. And list every Part A problem you found.
If you see a login, 2-step code or CAPTCHA, stop and tell me.
```
