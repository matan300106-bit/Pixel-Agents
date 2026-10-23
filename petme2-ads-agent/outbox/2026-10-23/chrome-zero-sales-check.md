# PETME2: 0 sales since Oct 21 evening, quick check (read only first)
Last order: Oct 21, 6:29 PM Pacific. All 8 listings are BUYABLE (checked by API). If logged out / 2-step code / CAPTCHA: stop.

1. **Ads console** (advertising.amazon.com) → Campaigns, date = Yesterday and Today:
   campaign | state | status (Delivering? Out of budget? Payment failure?) | budget | impressions | clicks | spend.
   Also: Administration → Billing & payments: is there any payment failure or hold? (read only)
2. **Seller Central** → Account Health: anything red? Performance → Notifications: any new message since Oct 21?
3. **Stainless fountain image error** (SKU QY-HHE8-0H1B): Inventory → Manage All Inventory → Edit → Images. Amazon says image 6 (PT05) breaks image rules. Write what Amazon shows. Do not delete anything; just report.
4. If ads are delivering and nothing is wrong: run `outbox/2026-10-21/chrome-ads-push.md` next.

Report: step 1 table · billing status · account health · image message · anything else unusual.
