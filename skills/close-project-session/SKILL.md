---
name: close-project-session
description: "Close a long or multi-part project session with a configurable protocol that preserves accepted work, durable state, continuations, process improvements, a human summary, and reusable knowledge. Use for explicit final-closing requests such as close this session, wrap this up, summarize the session, close the loose ends, or make sure nothing was forgotten. Do not use for an ordinary progress update."
---

# Close a Project Session

End a stage so later work starts from accepted project state, not a retelling of
the conversation. The six outcomes are universal; the project profile and route
connector define the actual tools, destinations, and human knowledge format.

## Treat closing as a full protocol

An explicit request to close, wrap up, or summarize a finished session does not
mean “report technical status.” Read the profile, establish the unclosed work
window, complete every available outcome, and only then declare closure.

A clean repository, successful release, or publication elsewhere changes the
evidence, not the contract. Never substitute an improvised similar checklist.

## Resolve the profile and routes

Read [the closure-profile reference](references/closure-profile.md). Resolve
configuration from the broadest confirmed default through workspace and project
overrides. A more specific profile overrides only named fields.

The profile defines meaning and acceptance. A separate **route connector** maps
each numbered outcome to its owner, destination, write method, and verification.
Validate it with `scripts/validate_closure_route.py` before the first write and
validate every applicable destination after writing. Never infer destinations
from the current directory, a similar repository, or habit.

If no confirmed profile exists:

1. Inspect project rules, sources of truth, trackers, versioning, handoffs,
   documentation, and publication boundaries.
2. Build a candidate from known facts; mark fields `confirmed`, `inferred`, or
   `unknown`.
3. Show one compact summary of known facts, inferences with reasons, and only the
   material gaps. Ask the user to correct and complete it in one response.
4. Save the confirmed profile at the broadest level where it truly applies and
   resume the original closure without another permission request.

If a complete default exists, skip first-use setup and ask only about real
project differences. Profiles may describe permission gates but never grant
publication, persistent-task creation, destructive action, or external access.

## Establish the closure window

All outcomes cover the whole still-unclosed window, not the last message, topic,
or visible post-compaction fragment.

Start immediately after the latest **proved coverage checkpoint**: a complete
prior closure receipt or explicit sync/handoff that names its scope and durable
state. If none exists, start at the first substantive task turn. End at the
current closing request.

Compaction, a model summary, topic change, commit, publication, deployment, file
sync, article, or documentation update is not a checkpoint by itself. Even a
formal receipt fails as a checkpoint if it omitted a known major topic or
substituted a technical artifact for a required human deliverable.

## Build a durable coverage register

Review every user turn in the window. Record each substantive request, promised
result, correction, decision, independent idea, artifact, error, repair, and
unresolved obligation. Then reconcile the list with canonical project sources.
For every row record:

- its source in session history;
- the expected result and owning goal or topic;
- one class: `done`, `current_task`, `backlog`, `future_gated`, `rejected`,
  `duplicate`, or `superseded`;
- result evidence or the exact canonical continuation destination;
- which closure outcome covers it.

Classify from the complete evidence chain through the last relevant **proved**
event. A later summary saying “the cause is unknown” does not erase an earlier
verified cause, repair, and acceptance. When records conflict, restore their
order, cite primary evidence, and append a dated correction.

An empty tracker, clean Git state, or missing `NEXT_STEPS` entry does not prove
there are no loose ends. Extract from history first; use project records to
confirm status second. Persist the complete classification in the configured
existing closure, status, log, or handoff surface. Do not create a second backlog.

If complete history is unavailable, use the platform's normal history reader.
If it remains unavailable, outcome 3 is blocked: name the unchecked range and do
not claim full closure.

Separately compare the original goal with the observable user journey. Tools,
code, tests, and documentation do not prove that journey completed. Mark every
promised part `done`, `partial`, `not_started`, or explicitly user-confirmed
`superseded`.

## Six atomic outcomes

Assign each outcome exactly one durable status:

- `done`: the result exists and was verified;
- `not_applicable`: it truly does not apply, with a factual reason;
- `blocked`: all available preparation is complete, with one exact external
  gate and one next user action.

1. **Accepted results.** Gather stage artifacts, apply every accepted change,
   and run proportionate acceptance checks.
2. **Durable state.** Preserve and version every ready semantic package through
   the configured mechanism. Publish or sync externally only when authorized.
3. **Continuations.** Reconcile the whole remainder with the original goal,
   including unfinished promises, deferred user journeys, and discussed but
   unaccepted ideas. Prepare self-contained handoffs in the configured system.
   Create or message persistent tasks only with explicit authorization.
4. **Durable process repair.** Find where the user had to repeat, prompt,
   correct, or restore evidence. Make the smallest verified change in the owning
   skill, rule, template, script, or project instruction, or name the blocker.
5. **Human summary.** Explain plainly what changed, why it mattered, what remains,
   and where to resume.
6. **Human knowledge artifact.** Test the whole window for reusable knowledge.
   On positive novelty, create or materially extend the exact human deliverable
   configured in the profile. On negative novelty, prove a named existing human
   artifact already contains the entire potential delta.

Outcome 6 is a closure gate. Publication, deployment, Git state, validation, or
process repair never substitutes for it. A model-facing skill, prompt, schema,
validator, checklist, or agent instruction closes outcome 4, not outcome 6.

Do not confuse an enforceable contract with knowledge documentation. A contract
says what must happen. Reusable knowledge explains why, applicability and limits,
alternatives or trade-offs, and how another person can adapt the method. A file
under `docs/` passes only if its content does.

## Restore and preserve accepted state

1. Record the closure window and checkpoint evidence.
2. Read canonical decisions, status, plan, tracker, handoff, artifacts, and rules.
3. Read the complete window and find facts not yet persisted.
4. Verify actual artifact versions and durable-state mechanisms.
5. Preserve unrelated work; do not demand a clean whole repository when the
   owned package can be separated safely.

When versions conflict, establish their common base, author, time, original
instruction, and intended layering. Do not present versions as equal merely
because both exist. Ask only when a real semantic ambiguity remains.

Historical logs and receipts are append-only unless their own contract defines
a mutable current-state field. Correct a wrong claim with a dated entry naming
the old claim, reason, evidence, and current status.

Apply accepted changes without expanding meaning. Run required project checks
and any configured pre-final audit. Version each ready semantic package. If an
already-authorized external sync is required, perform and verify it. Closure
alone never grants publication.

If preservation is blocked, identify the exact object, owner, and cause; finish
all independent preparation and present one concrete gate.

## Classify what remains

- `done`: verified result exists.
- `current_task`: one immediate executable step and its gate.
- `backlog`: an idea retained without an invented deadline.
- `future_gated`: a known dependency or user decision.
- `rejected`: a rejection important to future work.
- `duplicate`: the canonical item already exists.
- `superseded`: the user explicitly replaced an earlier expectation; preserve
  both decisions and their order.

Classify at final-receipt time. If a `future_gated` dependency was “after this
session ends,” closure satisfies that dependency: convert it to `current_task`,
handoff to the owner, or keep it blocked on a new concrete gate.

Do not hide the original unfinished user journey behind a technical continuation.
List substantial unaccepted ideas explicitly and preserve or reject them in the
configured place.

## Repair the process

Put a recurring solution in its real owner:

- stable known workflow: skill, SOP, template, script, checklist, or project rule;
- new standalone workflow: a new skill only after a complete proven cycle;
- one-off condition: project contract;
- idea without a solution: backlog, not an instruction.

Do not record “be more careful.” The repair must change the next execution and
be traceable to the demonstrated cause.

## Harvest reusable knowledge

Before the final response establish:

- the reusable semantic delta;
- positive or negative novelty and its evidence;
- the profile's mandatory human deliverable;
- its exact destination and proof of completion.

Read `knowledge_harvest.human_deliverable`: `kind`, `destination`,
`required_when`, `definition_of_done`, and `substitution_gate`. The model may not
choose a more convenient format or location. Only the user may waive or replace
the configured deliverable.

Ask whether a person absent from the session could understand the problem,
reasoning, rejected alternatives, boundaries, and adaptation method. A heading,
empty card, command list, short handoff, or promise to write later does not pass.

On negative novelty, create nothing; name the existing human artifact and show
that it covers every potential delta. On positive novelty, complete the configured
deliverable now. Editing, design, or publication may remain separate, but the
substantive human artifact must exist.

Test novelty across the whole window. Unrelated lessons may require multiple
deliverables of the configured type rather than one forced story.

## Hand off continuations

A new task is appropriate only after a substantial stage is accepted and the
next stage has an independent outcome. Do not rotate merely because a chat is old.

Before handoff, persist the objective and exact object; accepted facts, decisions,
versions, sources, results, and validation; open questions and non-scope; and one
next action with its acceptance criterion. Prepare the package without creating
or messaging a persistent task unless the user explicitly authorizes it.

## Final receipt

Keep machine statuses `done | not_applicable | blocked` in durable records. In
the user-facing answer, express the same state naturally in the user's language.
Cover all six outcomes with evidence.

Outcome 3 must state `<N> substantive items found → <N> classified → 0 without
status`, name the durable register destination, and list every row outside
`done`, `duplicate`, and `superseded`. Without complete history review, equal
counts, and a verified destination, outcome 3 cannot be done.

Name the window and topics, then state:

`Original goal → actual result → unfinished work`

If the original goal remains incomplete and the user did not cancel it, say the
stage is preserved and the goal continues. Claims such as “only one item remains”
must agree with the entire register, including other owners and topics.

For every file or system result marked done, name the verified connector
destination. Finish with a short human explanation rather than repeating the
technical checklist. Do not declare closure complete while any outcome lacks a
proved status.
