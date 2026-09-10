# Records, states, and learning

Read this when changing preferences, stock, product feedback, orders, or delivery status.

## Source ownership

| Source | Purpose |
|---|---|
| `shopping-workspace.md` | workspace map, market region, locale, currency, units, and precision |
| `preferences.md` | stable habits, default checks, exclusions, and substitution rules |
| `stock.md` | dated latest-known household state, expected arrivals, and meaningful consumption |
| `current-shopping.md` | decisions for the active shopping cycle and verified carts |
| `product-notes.md` | experience with specific products and preparation methods |
| `stores.md` | stores, ordering channels, roles, and durable delivery conditions; category-, store-, or season-specific selection rules belong in `preferences.md` |
| `purchases/` | actual orders, quantities, totals, and statuses |

When records conflict, use this priority within the relevant domain: a newer explicit user statement -> a dated verified fact -> an older persistent rule. A one-off exception for the current shop does not rewrite a permanent preference.

## Classify a new message

- “Always choose unsweetened” is a persistent selection rule.
- “Two packages this time” is a current-shopping quantity.
- “We used up the eggs” is a stock state, not automatic permission to buy.
- “This chicken tastes good” is feedback about a specific product, not necessarily a `buy_again` decision.
- “Produce from this store is poor in late summer” is a seasonal rule for one store, not a universal produce ban.
- “The order has been placed” is an order fact. Take its contents from the confirmed order or explicitly reported lines, not an older cart snapshot.

Evaluate ingredients, taste, convenience, preparation method, and the decision to buy again independently. Do not promote one dimension into another. A purchase or a high public rating is not user feedback.

## Stock without false precision

Use `plenty`, `available`, `low`, `out`, or `unknown`. Store a known quantity as an estimate with its unit and fact date.

- “Half a package remains” means half a package; convert to weight or volume only when the package size is known.
- “Used 200 g” can be subtracted from a known amount of the same product. If the starting amount is unknown, record the consumption without inventing the remainder.
- An old receipt does not prove the current stock of perishable food.
- A placed order is expected stock first. Move it into household stock once after receipt is confirmed, accounting for cancellations and substitutions.
- An agreed plan to cook or freeze something is not evidence that it happened.

If a food diary is connected, keep it as a separate source. Read only food events after the stored reconciliation boundary. Do not copy medical details or count the same meal more than once through daily, monthly, or derived notes.

## Orders and receipt

For a new order, copy `purchases/_template.md` to `YYYY-MM-DD-store.md`. Distinguish multiple orders from the same store on one day with a short identifier. Search first by store and `order_id` so an existing order is updated instead of duplicated.

Keep `ordered`, `in_delivery`, `delivered_by_store`, `received_by_user`, and `cancelled` distinct. A store's “delivered” status is not the user's physical verification of the contents.

After a weighed item adjustment, substitution, or refund, update the same order: replace the current `total` and summary table, then append the old and new totals, reason, and evidence to “Total history.” Do not create a second order merely because its total changed.

Do not allocate an order-level discount across lines without evidence, and never subtract it twice. Do not reconstruct an exact weight from a rounded product card when only the line total is known.

## Dates, numbers, and evidence

Store calendar dates as ISO `YYYY-MM-DD`. Store timestamps as ISO 8601 with an explicit timezone offset. Parse a user's displayed prices and quantities according to the recorded locale and the source page; if `1,234` or `1.234` remains ambiguous and changes the decision, ask rather than guessing.

In frontmatter and other machine-read numeric fields, use ASCII digits, a period as the decimal separator, and no thousands separators; keep the currency separately. Preserve the source-formatted amount in evidence only when it is useful.

`updated_at` is when the record changed. `verified_at` is when the stated physical or external source was actually checked. Reading an old note does not advance `verified_at`.

For a new rule or product review, retain the date and short evidence such as a user message, order link, or product page. Never store secrets or temporary browser identifiers as evidence.
