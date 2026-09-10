---
schema_version: 1
owner_name: ""
market_region: ""
locale: ""
currency: ""
measurement_system: ""
stock_precision: "approximate"
created_at: ""
updated_at: ""
---

# Personal shopping workspace

## Source map

- `preferences.md`: stable needs, selection criteria, and exclusions.
- `stock.md`: approximate latest-known household stock and expected arrivals.
- `current-shopping.md`: one active shopping cycle from draft through ordering.
- `product-notes.md`: feedback about specific products.
- `stores.md`: stores, ordering channels, roles, and durable delivery conditions; store- or season-specific product rules remain in `preferences.md`.
- `purchases/`: actually placed orders.
- `history/`: completed current-shopping snapshots when useful.

## Boundaries

Stock is approximate. Do not store full addresses, phone numbers, payment data, passwords, cookies, or browser tokens here. A food diary connection is optional; if used, record only its location and reconciliation boundary in `stock.md`, without duplicating the diary itself.

Use `metric`, `us_customary`, `imperial`, or `mixed` for `measurement_system`. Keep US customary and Imperial volume units distinct. Dates use `YYYY-MM-DD`; timestamps use ISO 8601 with a timezone. Machine-read numbers use a period as the decimal separator and no thousands separators.
