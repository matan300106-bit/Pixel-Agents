# PETME2 supplements — store setup (2026-10-04)

All 4 products are **DRAFT** (hidden). Nothing is for sale until the owner sets them Active.

| Product | Handle | Suggested price | Images |
|---|---|---|---|
| Skin & Coat Soft Chews for Cats – 100 Chews | skin-coat-soft-chews-for-cats | $24.99 | hero (box+jar), grey tabby lifestyle, chews close-up |
| Advanced Hip & Joint Soft Chews for Dogs – 100 Chews | hip-joint-soft-chews-for-dogs | $29.99 | hero, golden retriever lifestyle, chews close-up |
| Cat Grass Soft Chews – Digestion & Hairball Support – 100 Chews | cat-grass-soft-chews-digestion-hairball | $24.99 | hero (NEW design), orange tabby + cat grass, box front |
| Tear Stain Soft Chews for Dogs – 100 Chews | tear-stain-soft-chews-for-dogs | $26.99 | hero (NEW design), white Maltese, box front |

- Images: AI mockups made with GPT Image 2.5 (Higgsfield) from the owner's box/label PDFs. Replace with real photos when samples arrive.
- Product type `Supplements`, tags, SEO title/description, inventory not tracked (Amazon/FBA holds stock).
- Theme template `product.supplement` (no feeder-only sections). Metafields custom.spec_chips + custom.story set.
- Collection **Supplements** (`/collections/supplements`, smart: type = Supplements), template `collection.supplements`:
  banner → product grid → 3 reasons → 30-day guarantee → FAQ.
- Theme files are in the draft theme "PETME2 — Homepage refresh (draft)" (188818587860) and in `shopify-theme-tech/templates/`
  (built by `shopify-theme-tech/build_supplements.py`). The live theme does not have them until that draft is published.

## Before going live (owner)
1. Real prices (suggested above) and Amazon match.
2. Cat Grass + Tear Stain: real formula from the factory (the box files use a PROPOSED formula, GA = TBD). Add "What's inside" + "How much" to the product description.
3. Confirm "Veterinarian formulated" and "Third-party tested" are true (they are on the existing boxes). If not, remove them.
4. Chew count: Skin & Coat label says 200 chews / 2 g, the box says 100 chews / 4 g. Pick one.
5. Set products Active, then add "Supplements" to the main menu and a Supplements tab on the homepage.

Claims are kept at "supports / helps" level + FDA disclaimer (pet supplement rules). No disease claims.
