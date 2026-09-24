# Close Project Session

A configurable Codex skill for closing long, multi-part project sessions without
losing accepted work, unfinished commitments, process lessons, or reusable human
knowledge.

The skill separates a universal six-outcome closure contract from project-specific
configuration. Each user or team supplies a closure profile and route connector
for their own repositories, trackers, documentation, and knowledge destinations.

## What it preserves

1. accepted and verified results;
2. durable versioned state;
3. explicit continuations and unaccepted ideas;
4. process improvements based on demonstrated failures;
5. a plain-language human summary;
6. a reusable human knowledge artifact when the session produced a new lesson.

It also reconstructs the full unclosed window, compares the original user goal
with the observable result, and refuses to treat a commit, test suite, or model
summary as proof that the requested user journey was completed.

## Install with Codex

Ask Codex:

> Use $skill-installer to install the skill from https://github.com/Lisabet/codex-skills/tree/main/skills/close-project-session

Start a new Codex task after installation.

## First use

If no closure profile exists, the skill first reconstructs known conventions
from the project, labels inferences and unknowns, and asks one compact setup
question. Later closures reuse the confirmed profile and ask only about genuine
project differences.

The profile never grants publication, destructive changes, persistent-task
creation, or access to external systems. Those actions retain their own gates.

## Privacy

The package contains no personal profile, project path, tracker content, session
transcript, credentials, or private service configuration. Users keep their own
closure profile and route connector outside the shared skill package.

## License

MIT. See [LICENSE](LICENSE).
