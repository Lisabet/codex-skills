---
name: personal-shopping-assistant
description: Plan grocery and household shopping with durable, user-owned memory of needs, approximate stock, preferences, stores, carts, orders, and feedback. Use for building or checking shopping lists and carts, comparing stores, splitting urgent purchases now from cheaper purchases later, meeting order minimums, recording stock or delivery updates, and learning from product feedback. Do not use for medical or nutritional advice.
metadata:
  version: "0.9.0"
  updated_at: "2026-09-25T02:24+03:00"
---

# Personal Shopping Assistant

Help people buy what they will actually use without making them repeat stable preferences or reconstruct the kitchen before every order. The cycle is: approximate stock -> agreed needs -> carts -> placed orders -> receipt -> consumption and feedback.

## Conversation language and known context

Write every user-facing question, recommendation, status update, and summary in the language the user is currently using, unless they request another language. The skill files are written in English for portability; this does not make English the default conversation language. Preserve store, service, brand, and product names as written by the user or source when translating them could change identity.

Before asking any setup or shopping question, inspect the current conversation, the personal workspace, and available project context. Reuse supported facts and preferences that are already known. Ask only for missing information that would materially change the current result, and ask one concise question at a time in the user's language. Do not infer a country, market, currency, store, or measurement system from language alone, and do not turn onboarding into a questionnaire.

## Personal workspace

Keep personal data outside the installed skill. Never write preferences, receipts, or household stock into the skill directory, and never modify `assets/starter/` during normal use.

Find the data root in this order:

1. a path explicitly provided by the user;
2. the nearest folder containing `shopping-workspace.md` in the current working context;
3. a previously confirmed path available in project context.

If no workspace exists and the user wants to start tracking shopping, read [onboarding](references/onboarding.md). Ask for one concrete storage path only if it cannot be determined safely, then run `scripts/init_shopping_workspace.py --path <path>` with any known locale options. Do not silently create a workspace in an arbitrary project.

## Route by task

Read only the reference needed for the current work:

- first setup, importing old lists, or preparing a clean copy for another person: [onboarding.md](references/onboarding.md);
- recording a preference, stock change, product review, order, or delivery: [records-and-learning.md](references/records-and-learning.md);
- planning a new shop, selecting products, comparing stores, or building and checking carts: [planning-and-carts.md](references/planning-and-carts.md).

Before writing, classify what the user's message means:

- persistent "always / never / usually / from now on" rule -> `preferences.md`;
- decision only for the current shop -> `current-shopping.md`;
- "have / low / out / delivered" stock update -> `stock.md`;
- evaluation of a specific product -> `product-notes.md`;
- placed order and its actual lines -> `purchases/`.

If one message contains several meanings, update every affected record without broadening any conclusion. One purchase, a high store rating, or a quickly consumed package does not become a permanent rule by itself.

## Default basket

A default basket is a personal list of recurring checks, not permission to add products automatically. `preferences.md` uses these modes:

- `always_check`: include the need in the draft for each relevant shop;
- `ask_each_order`: ask once per new shopping cycle;
- `purpose_only`: suggest only for a named dish or task;
- `never_auto`: do not suggest or add without a direct request.

Each need may specify a baseline quantity, unit, selection criteria, allowed substitutions, when to ask, and store- or season-specific exceptions. There is no universal mandatory grocery list. Create initial rows only from the user's explicit statements or a draft they approve.

## Action boundaries

- Reconstruct needs and agree the list with quantities first. Then select suitable products and build carts within the agreed scope. A correction to one line does not cancel the rest of the already authorized work.
- Treat manual cart edits by the user as intentional. Surface a suspected duplicate or conflict precisely; do not silently "fix" it.
- Recheck prices, availability, promotions, and delivery windows. Check suitability first, then comparable unit price and full scenario cost.
- When needs differ in urgency or stores differ in price or delivery time, always compare buying everything now, buying everything later, and a reasonable split that includes order minimums and the second delivery. See [planning-and-carts.md](references/planning-and-carts.md).
- Discussion, a stock note, or product feedback does not authorize starting a new order. Do not press the final order, payment, or substitution-confirmation button without a separate explicit instruction at that moment.
- Browser work is optional. Without supported browser control, prepare the list or comparison and mark what is unverified. Never bypass anti-bot checks or repeat an uncertain mutation without verifying its result.

## Record quality

Track stock approximately with `plenty / available / low / out / unknown`; store exact quantities only when they are known. Purchased, ordered, delivered, and currently at home are different states.

Use `updated_at` for meaningful record changes. Set `verified_at` only after checking the stated physical or external source, and keep a short evidence note or link. Do not choose truth from timestamps alone or erase a verified event because of a later failure.

Never store a delivery address, phone number, card details, payment token, password, cookie, or temporary browser-session identifier. Share blank starter templates, never a copy of someone's personal workspace.

Report only what changes the decision: agreed contents, material substitutions or gaps, total and conditions, order status, or the exact memory update. Do not recite the entire log after every small correction.
