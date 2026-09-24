# Project Closure Profile

The profile separates the universal closure contract from one person's or
project's tools, repositories, trackers, and knowledge formats. It is editable
configuration, not a permanent ritual.

A separate route connector defines where each outcome goes. The profile defines
meaning, conditions, and acceptance; the connector maps each of the six outcomes
to an owner, destination, and verification. Do not duplicate routes in the skill
or infer them from the current directory.

## Where the profile belongs

Prefer an existing canonical project surface such as `PROJECT.md`, `AGENTS.md`,
a project handbook, or workspace configuration. Do not create a second source
of truth. If none exists, use `closure-profile.md` at the project root.

Never put project paths, private service names, or user preferences into the
shared skill package.

## Inheritance

Profiles may exist at three levels:

1. personal or team default for recurring collaboration practices;
2. workspace or portfolio conventions;
3. project-specific differences only.

Resolve from broad to specific. A narrower level overrides only explicit fields;
missing fields inherit. No profile expands authority to publish, send externally,
create tasks, or perform destructive actions.

If the inherited profile answers every applicable question, setup is complete.
Do not create a project file that merely repeats a default.

## First use

When required fields remain missing, recover as much as possible before asking.
Use sources in this order:

1. explicit user decisions and project instructions;
2. canonical project, status, handoff, and decision files;
3. actual trackers, versioning, and validation mechanisms;
4. recurring confirmed collaboration practice;
5. conversation history for facts not yet preserved elsewhere.

Classify each field:

- `confirmed`: explicitly stated or recorded by an authoritative contract;
- `inferred`: supported by recurring observed practice, with a short reason;
- `unknown`: insufficient evidence; never fill by convenience.

Present one compact candidate:

```text
Already confirmed:
- ...

Inferred from our work:
- ... — evidence: ...

Still missing:
- ...

Is this profile correct? Correct the inferences and fill only the unknowns.
```

Do not ask one question per field or repeat known questions. Unknown fields that
do not affect the current closure remain unknown without blocking it. After the
answer, save the confirmed profile and resume closure automatically.

## Minimal schema

Use only applicable fields; avoid empty bureaucracy.

```yaml
closure_profile:
  updated_at: <ISO 8601>
  route_connector: <absolute path to connector JSON>
  closure_window:
    checkpoint_sources:
      - <where complete earlier receipts, syncs, or handoffs are recorded>
    fallback: session_start
  accepted_result_sources:
    - <where accepted decisions and artifacts live>
  validation:
    - <how readiness is proved>
  durable_state:
    system: <Git | document revisions | tracker history | other>
    location: <canonical surface>
    external_sync_gate: <what needs separate authorization>
  continuations:
    system: <tracker | issues | tasks | handoff files | other>
    location: <canonical queue>
    task_creation_gate: <rule for creating persistent tasks>
  process_rules:
    locations:
      - <skills | project instructions | SOP | scripts | other>
  human_handoff:
    audience: <who needs the summary>
    destination: <chat | status document | other>
    style: <material requirements>
  knowledge_harvest:
    human_audience: <who should retain the understanding>
    novelty_rule: <what counts as a reusable delta>
    human_deliverable:
      kind: <one mandatory result type>
      destination: <canonical human location>
      required_when: positive_novelty
      definition_of_done:
        - <substantive completion criterion>
      substitution_gate: explicit_user_decision
    publication_gate: <what requires separate authorization>
```

## Route connector

The connector is machine-checkable configuration with exactly six result keys,
`1` through `6`. Each result names `name`, `route`, `destination`, and
`verification`. Dynamic destinations identify the canonical owner surface; the
project contract resolves the concrete path before writing. Fixed knowledge
locations use `path_template`; similar invalid roots belong in `forbidden_roots`.

```json
{
  "schema_version": 1,
  "connector_id": "person-or-team-default",
  "results": {
    "1": {
      "name": "accepted_results",
      "route": "resolved_owner",
      "destination": "owning_project.accepted_result_surface",
      "allowed_route_sources": ["project_contract"],
      "verification": "project acceptance gate"
    },
    "2": {
      "name": "durable_state",
      "route": "resolved_owner",
      "destination": "owning_project.versioning_surface",
      "allowed_route_sources": ["project_contract"],
      "verification": "owned package is committed or versioned"
    },
    "3": {
      "name": "continuations",
      "route": "resolved_owner",
      "destination": "owning_project.continuation_surface",
      "allowed_route_sources": ["project_contract"],
      "verification": "canonical continuation updated"
    },
    "4": {
      "name": "process_repair",
      "route": "resolved_owner",
      "destination": "process_defect.owner_surface",
      "allowed_route_sources": ["personal_skill", "project_contract", "deterministic_owner"],
      "verification": "narrow repair passes owner check"
    },
    "5": {
      "name": "human_handoff",
      "route": "literal",
      "destination": "current_task.final_response",
      "verification": "self-contained human summary"
    },
    "6": {
      "name": "human_knowledge_artifact",
      "route": "path_template",
      "destination": "<absolute-root>/{content_id}/source.md",
      "path_template": "<absolute-root>/{content_id}/source.md",
      "required_status": "idea",
      "forbidden_roots": ["<similar-but-wrong-root>"],
      "verification": "exact path, metadata, and owning versioning surface"
    }
  }
}
```

Validate the complete connector before mutation, then every concrete route:

```text
python scripts/validate_closure_route.py --connector <connector.json> --check-connector
python scripts/validate_closure_route.py --connector <connector.json> --result 6 --destination <absolute-path> --content-id <id> --status idea
```

If the connector is incomplete, a destination mismatches, or it falls under a
forbidden root, that outcome remains blocked. “Move it later” is not a fallback.

Git, task cards, and articles are examples, not universal requirements. What is
required is durable state, a clear continuation location, and a deliberate test
for reusable knowledge.

`closure_window.checkpoint_sources` lists surfaces that can prove an earlier
part of the same task was fully reconciled. A checkpoint must name covered scope
and durable state for every applicable outcome. Otherwise use `session_start`.

`human_deliverable` is one default result, not a menu: for example, a substantive
article master draft, an updated handbook page, a reasoned ADR, or a user guide.
The model cannot replace it with technical documentation, a handoff, or an
instruction to itself. Only the user may waive or replace it.

`definition_of_done` describes content, not file existence.
`substitution_gate: explicit_user_decision` makes the human choice explicit.

Legacy fields such as `preferred_forms`, `human_locations`, or
`canonical_locations` may inform migration, but do not form a complete profile
until one human deliverable and its completion criteria are confirmed.

## Changing the profile

- A one-time user instruction overrides the current closure only.
- An explicit durable decision updates the profile immediately.
- A recurring deviation becomes a proposed rule before it is adopted.
- A tool change must not silently change meaning or authority.
- Record `updated_at`, the changed field, and a short reason.
- Do not delete confirmed rules because of one exception.

A profile may record that a new service, installation, or external action needs
authorization; it never provides that authorization.

## Readiness check

A usable profile answers where the closure window starts; where accepted results,
durable state, continuations, and process repairs belong; how readiness is proved;
who needs the summary; what human knowledge deliverable is required, where it
lives, and what complete means; and which actions remain user-only.

A usable connector gives all six outcomes one route, validates fixed paths, and
resolves dynamic paths from the named project contract before writing.

If only an inapplicable field is unknown, it is not a defect. If an unknown blocks
current closure, ask one combined question, mark affected outcomes blocked, and
continue the independent ones.
