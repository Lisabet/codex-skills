# Codex Skills by Lisabet

Practical, privacy-conscious skills for Codex, developed from real workflows rather than hypothetical demos.

This is an independent community project and is not affiliated with or endorsed by OpenAI.

The skills are documented in English for portability, but user-facing conversation follows the user's current language. Existing context is reused, and setup asks only for missing facts that materially affect the task.

## Skills

| Skill | What it does | Version |
|---|---|---:|
| [Personal Shopping Assistant](skills/personal-shopping-assistant) | Plans grocery and household shopping across stores, remembers user-owned preferences and approximate stock, and compares urgent-now versus cheaper-later scenarios including order minimums and delivery fees. | 0.9.0 |
| [Close Project Session](skills/close-project-session) | Closes long project sessions through six configurable outcomes: accepted work, durable state, continuations, process repair, a human summary, and reusable knowledge. | 1.0.0 |

## Example

Suppose milk is needed today, while eggs, produce, and household supplies can wait until tomorrow. One store delivers now but costs more and has an order minimum; another is cheaper but delivers tomorrow.

The Personal Shopping Assistant compares:

1. buying everything now;
2. buying everything later, marking it infeasible when it misses the deadline;
3. splitting the shop while counting both order minimums, both delivery charges, and only useful agreed items used to reach a minimum.

It recommends the cheapest feasible scenario rather than the cheapest-looking cart.

## Install with Codex

Ask Codex:

> Use $skill-installer to install the skill from https://github.com/Lisabet/codex-skills/tree/main/skills/personal-shopping-assistant

or:

> Use $skill-installer to install the skill from https://github.com/Lisabet/codex-skills/tree/main/skills/close-project-session

Start a new Codex task after installation.

## Manual installation

1. Download the repository source archive from GitHub.
2. Extract the desired folder from `skills/`.
3. Copy that folder to `$CODEX_HOME/skills/`, or to `~/.codex/skills/` when `CODEX_HOME` is not set.
4. Start a new Codex task.

## Personal data stays personal

The repository contains no user records, project transcripts, credentials, or private configuration. Each user keeps their own working data and project configuration outside the shared skill package.

The shopping skill explicitly excludes delivery addresses, phone numbers, payment details, passwords, cookies, and browser tokens from durable records. The closure skill contains no personal closure profile or route connector; users configure those locally. External publication, final checkout, payment, destructive changes, and persistent-task creation retain separate authorization gates.

## Repository layout

```text
skills/
├── close-project-session/
│   ├── SKILL.md
│   ├── agents/
│   ├── references/
│   └── scripts/
└── personal-shopping-assistant/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

More skills can be added under `skills/` without changing the installation path of existing ones.

## Credits

Created by Lisabet through practical collaboration with Sayr and Codex.

## License

[MIT](LICENSE)
