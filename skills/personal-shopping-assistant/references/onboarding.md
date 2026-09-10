# First setup and migration

Read this when creating a personal workspace, importing old records, or preparing a clean copy for someone else.

## Start without a forty-question form

1. Determine one user-owned data root that remains available across Codex tasks. The installed skill directory is not a data workspace.
2. Before asking anything, inspect the current conversation, `shopping-workspace.md`, `stores.md`, and available project context. Prefill only facts supported by those sources and retain a short source or evidence note when writing them. Do not ask again for a known region, currency, measurement system, store, household pattern, or preference.
3. Establish only the missing shopping-market context that changes the current result. If region or usable stores are still unknown, ask one compact question rather than presenting a questionnaire. Ask for currency or preferred measurement system only when it is unknown and affects a comparison. Distinguish `metric`, `us_customary`, `imperial`, and `mixed`; US and Imperial volume units are not interchangeable. Do not infer market region from conversation language alone.
4. Use the language the person is currently using for every setup question, explanation, and confirmation unless they request another language. Preserve proper store, service, brand, and product names when translation could change identity.
5. Run `scripts/init_shopping_workspace.py --path <path>` with any known `--market-region`, `--locale`, `--currency`, and `--measurement-system` values. The script creates missing files only, refuses destinations inside the installed skill, and never overwrites existing records. Missing market settings remain explicit validator warnings; resolve them before live store comparison, but do not block a store-independent paper list.
6. Add each named store or delivery service to `stores.md`. Record only what is known: public website or app, normal role, service area, membership relevance, order minimum, delivery fees or free-delivery threshold, and timing. Mark volatile conditions unverified until checked live.
7. Get only the remaining context needed for the nearest shop: horizon, hard constraints, recurring checks, and who will build and place the order. Do not require the entire system to be completed before the first useful result.
8. If a typical list or one to three recent receipts are available, use them only as candidates for recurring checks. Repetition does not prove preference, current stock, or desired quantity; show the draft to the user.
9. Ask one meaningful decision at a time. Accumulate the rest gradually from normal corrections and feedback.

Useful setup questions, asked only when they affect the current task:

- Which country or broad shopping region are we buying in?
- Which stores, marketplaces, or delivery services should we use, and which should normally be compared?
- Are any memberships, loyalty prices, delivery passes, or hard order minimums relevant?
- How many days and people does a typical shop cover?
- Which dietary constraints or categorical exclusions must never be violated?
- What should be checked every time, and what should be asked each time?
- How approximate should household stock tracking be?
- For each important category, what matters most: price, taste, ingredients, convenience, shelf life, or a particular brand?

Do not request or store a full delivery address during onboarding. A broad market region is enough for durable records; use the live store session for address-dependent availability when browser work is authorized.

Do not turn health answers into a medical profile. Store only concrete product-selection constraints the person explicitly asks the assistant to follow.

## Store setup rules

Store identity is user-specific and never hard-coded into the skill.

- Preserve the store or service name used by the person.
- Keep a public URL or app name when it helps reopen the correct service; never keep login credentials or session identifiers.
- Separate stable roles such as “primary weekly shop” or “better produce” from volatile facts such as today's price, stock, delivery fee, or delivery window.
- If only one store is named, proceed with it and add alternatives later. Do not invent a comparison set.
- If the user requests a live shop but has not named any usable store, ask for one store or delivery service before browsing.

## Import existing notes

First make a read-only map of sources and inspect one or two representative examples. Then propose this mapping:

| Existing meaning | New location |
|---|---|
| recurring requirements and exclusions | `preferences.md` |
| latest known household state | `stock.md` |
| unfinished shopping cycle | `current-shopping.md` |
| reviews of specific products | `product-notes.md` |
| stores and their roles | `stores.md` |
| actually placed orders | `purchases/` |

Do not import a cart as a purchase or reconstruct today's refrigerator by summing old receipts. Preserve dates and sources; leave uncertain facts unknown. Never delete old records after import without separate permission.

## Share with another person

Share the skill folder or an archive containing it. A new user creates a separate workspace from `assets/starter/`; filled personal records are not included.

Before packaging, check for absolute home paths, personal names, addresses, phone numbers, order data, payment data, cookies, and tokens. `scripts/validate_workspace.py` checks workspace structure but does not replace a manual privacy review of the entire archive.
