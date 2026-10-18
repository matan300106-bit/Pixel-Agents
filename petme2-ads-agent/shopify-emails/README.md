# PETME2 order confirmation email

**Where:** Shopify admin → Settings → Notifications → Customer notifications → **Order confirmation** → Edit code.

1. **Email subject:** `Thank you! Your PETME2 order {{ name }} is confirmed 🐾`
2. **Email body (HTML):** delete everything and paste the whole `order-confirmation.liquid` file.
3. Click **Preview** (top right) to check it, then **Save**.
4. Send yourself a test: "Send test email".

**Before you paste:**
- Upload your logo once in Settings → Notifications → **Customize email templates** → Logo (width about 140 px). Without a logo, the email shows "PETME2" in blue text.
- The help line uses your store's sender email (`shop.email`). Change the sender to a domain email (support@petme2.com) in Settings → Store details for better trust and inbox delivery.

**What it shows:** thank-you header with first name, "View your order" button, 3-step "what happens next", items with photos and prices, discount, free shipping, total, setup tips only for what they bought (fountain and/or feeder), shipping address, free shipping / 30-day guarantee / real help row, and a help line.

`preview-order-confirmation.html` is a preview with a sample order (images are placeholders).
