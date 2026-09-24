# Personal Shopping Assistant

Version 0.9.0. A portable Codex skill for planning grocery and household shopping, maintaining approximate home stock, and learning a person's product preferences over time.

The implementation and documentation are in English, but the assistant speaks the user's current language unless asked otherwise. It reuses relevant facts already available in the conversation or personal workspace and asks only for missing information that changes the current shopping decision.

It can:

- turn recurring needs and current stock into an agreed shopping list;
- compare suitable products by comparable unit price rather than package price alone;
- split urgent purchases now from cheaper purchases later;
- account for order minimums, delivery fees, promotions, and multiple deliveries;
- preserve manual cart edits and require explicit permission before final checkout;
- keep personal shopping records outside the installed skill.

## Install from GitHub

Ask Codex:

> Use $skill-installer to install the skill from https://github.com/Lisabet/codex-skills/tree/main/skills/personal-shopping-assistant

Or copy the `personal-shopping-assistant` folder into `$CODEX_HOME/skills/`, or into `~/.codex/skills/` when `CODEX_HOME` is not set. Start a new Codex task after installation.

## First run

Choose a separate persistent folder for personal shopping records. The skill initializes it from blank templates and asks only for context needed to make the first shop useful:

- country or broad shopping region, currency, and preferred measurement system when relevant;
- stores or delivery services the person actually uses;
- the immediate shopping horizon and any hard restrictions;
- a few recurring needs, if the person already knows them.

Known details are prefilled from the current conversation and existing workspace; they are not asked again. Language alone is never treated as proof of country, currency, stores, or measurement system.

Store names are never hard-coded. Prices, availability, order minimums, fees, and delivery windows are treated as current facts and rechecked when they affect a decision.

## Personal data boundary

Share only this skill folder or a release archive. A user's filled workspace, preferences, receipts, stock, delivery address, payment details, cookies, and browser tokens do not belong in the package.

Browser cart building requires supported browser control and an active user login. The skill does not place or pay for an order without a separate explicit instruction at checkout time.

## License

MIT. See the `LICENSE` file included with the skill.
