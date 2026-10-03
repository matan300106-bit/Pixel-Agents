# How to download the ads files (browser steps)

> ⚠️ **DRAFT — NOT TESTED YET.** These steps were written before the first real test.
> On the first run with Claude in Chrome, follow them, fix anything that is different,
> and remove this warning. Amazon changes its pages sometimes — if a page looks different,
> take a screenshot, explain, and stop.

Save every file in `inbox/YYYY-MM-DD/` (today's date). Then run:
`python -m ads_source.import_day YYYY-MM-DD`

## Safety
- Read only. Never click Save, Apply, Upload, Create, or Archive while downloading.
- Logged out, 2-step code, or CAPTCHA → stop and tell the owner. Never type a password.

## 1. Bulk file (most important)
1. Open https://advertising.amazon.com and check the account at the top is **PETME2 / United States**.
2. Left menu → **Bulk operations**.
3. Under "Create spreadsheet for download":
   - Date range: **Last 60 days** (or custom: today − 60 days to yesterday).
   - Tick: **Sponsored Products data**, **Sponsored Products search term data**,
     **Campaigns with zero impressions**, **Paused campaigns** (not archived).
   - Optional later: Sponsored Brands / Sponsored Display data.
4. Click **Create spreadsheet for download**. Wait until the file is ready (status changes in the list below).
5. Click **Download**. Move the `.xlsx` file into `inbox/YYYY-MM-DD/` (name: `bulk.xlsx`).

## 2. Reports (Sponsored Products)
Left menu → **Measurement & Reporting → Sponsored ads reports** → **Create report**. For each one:
- Ad product: **Sponsored Products**. Time unit: **Summary**. Period: **Last 60 days**. Format: **.xlsx** (or .csv).

| Report type | Save as |
|---|---|
| Search term | `inbox/YYYY-MM-DD/search_terms.xlsx` |
| Targeting | `inbox/YYYY-MM-DD/targeting.xlsx` |
| Campaign | `inbox/YYYY-MM-DD/campaigns.xlsx` |

Click **Run report**, wait until the status is "Completed", then **Download**.
Tip: after the first time, use the existing reports (or schedule them daily) instead of creating new ones.

## 3. Check
Run `python -m ads_source.import_day YYYY-MM-DD`. It shows rows per file and any "Missing files".

## Upload (Guardian only — changes the account)
Only after the owner says "approved" in the chat:
**Bulk operations → Upload (Upload spreadsheet)** → choose `outbox/YYYY-MM-DD/bulk-upload.xlsx` → wait → open the result
and check **0 errors**. If errors: download the error report and show the owner.
