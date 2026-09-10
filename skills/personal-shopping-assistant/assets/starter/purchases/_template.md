---
schema_version: 1
order_id: ""
store: ""
ordered_at: ""
status: "ordered"
status_verified_at: ""
updated_at: ""
currency: ""
total: ""
source: ""
---

# Order

Use ISO 8601 with a timezone for `ordered_at`, `status_verified_at`, and `updated_at`. Store `total` as digits with a period decimal separator and no thousands separator; `currency` carries the unit.

## Items

| Product | Quantity | Unit | Unit price | Line total | Substitution or cancellation |
|---|---:|---|---:|---:|---|

## Summary

| Component | Amount |
|---|---:|
| Items | |
| Discounts and loyalty credit | |
| Delivery | |
| Packaging, taxes, and service fees | |
| Total | |

## Total history

When weight, substitution, or refund changes the order, append the previous total here before updating the frontmatter `total` and summary above.

| Time | Previous total | New total | Reason | Source |
|---|---:|---:|---|---|

## Status history

| Time | Status | Source and note |
|---|---|---|

Never store an address, phone number, payment details, cookie, or token.
