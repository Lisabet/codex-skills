---
schema_version: 1
shopping_id: ""
stage: "idle"
list_status: "not_started"
horizon: ""
stores: ""
budget_target: ""
updated_at: ""
cart_verified_at: ""
---

# Current shopping cycle

Allowed stages: `idle`, `draft`, `list_agreed`, `cart_building`, `cart_ready`, `ordered`, `closed`.
List statuses: `not_started`, `draft`, `agreed`, `superseded`.

## Buy

| Need | Quantity | Unit | Urgency | Purpose | Store | Status and evidence |
|---|---:|---|---|---|---|---|

## Skip this shop

| Need | Reason | Decision date |
|---|---|---|

## In carts

| Store | Product | Quantity | Price | Verified | Need covered |
|---|---|---:|---:|---|---|

## Needs decision

| Question | Recommendation | Alternative | Difference or risk |
|---|---|---|---|

## Store and timing scenarios

| Scenario | Now | Later | Order minimum or gap | Delivery and fees | Full total | Delivery window | Verified |
|---|---|---|---:|---:|---:|---|---|

## Placed orders

After checkout, add links to records in `purchases/`. Never treat an older cart snapshot as a placed order.
