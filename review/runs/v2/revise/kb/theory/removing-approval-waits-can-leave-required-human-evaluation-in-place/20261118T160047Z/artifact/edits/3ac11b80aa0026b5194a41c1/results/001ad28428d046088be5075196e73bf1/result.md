---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: The first is a blocking dependency
  change: 'Name the blocking thing ''wait'' throughout, the word the title and the
    opening already use. Drop the alternate labels ''blocking dependency'', ''dependency''
    and ''human stop'' (4 occurrences, all in scope): ''The first is a blocking dependency;
    the second is an unfulfilled requirement'' -> ''The first blocks execution; the
    second is an unfulfilled requirement''; ''A non-binding recommendation still creates
    a dependency if the agent must wait for it'' -> ''A non-binding recommendation
    still blocks execution if the agent must wait for it''; ''that assessment is a
    dependency of the revision process, though not of the earlier adoption'' -> ''the
    revision process waits for that assessment, though the earlier adoption did not'';
    ''without creating a human stop'' -> ''without creating a wait for a person''.
    Leave the verb ''depends on'' in the Required approval case, which is ordinary
    English.'
  reason: 'No occurrence needs a distinction that ''wait'' lacks: the note itself
    defines ''blocking dependency'' as ''an actual wait'', and every later ''dependency''
    and the ''human stop'' in Scope name that same thing (execution cannot proceed
    until a person acts). With four names for one thing, a reader may take ''dependency''
    in the revision paragraph or ''human stop'' in Scope for something other than
    the wait the title is about. kb-role lists these terms as unused by other notes,
    so no inbound use blocks the change.'
- quote: Optional assessment creates neither
  change: 'Keep ''optional assessment'' throughout and replace its synonym ''optional
    study'' with it (3 occurrences): ''This is an optional study'' -> ''This is an
    optional assessment''; ''Using an optional study''s available findings does not
    itself require future studies'' -> ''Using an optional assessment''s available
    findings does not itself require future assessments''.'
  reason: 'The term is needed: the Optional assessment case and the revision paragraph
    contrast it with assessment that the specification requires or that execution
    waits for. The deciding occurrence is ''Making a new human assessment a condition
    of each revision does'', where the bare word ''assessment'' names the required
    kind, so the optional kind needs its qualifier. ''Optional study'' names the same
    activity under a second name, so it reads as a second referent.'
description: Retained proposed result of kb/instructions/simplification-passes/abstractions.md
  on kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
format: 1
operation: kb/instructions/simplification-passes/abstractions.md
operation-sha256: 66c1e66712553330a826d33689fc281147d52ac6c08ae6f8510f4eb0cd9238a4
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
input-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
candidate: null
candidate-sha256: null
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/artifact/edits/3ac11b80aa0026b5194a41c1/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z
launch: 001ad28428d046088be5075196e73bf1
completed-at: '2026-11-18T16:08:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T160047Z/calls/launches/001ad28428d046088be5075196e73bf1/outputs/result.md
raw-output-sha256: a2d64f8f648c5bc5e971e7069981895b3a002cf716220980329e83c383fddce1
---

# Report

Two of the note's abstractions change the text. Both changes are proposed and none is applied.

- **'blocking dependency' / 'dependency' / 'human stop' -> 'wait'.** Decision: no occurrence needs the distinction. Replace with the ordinary word, 4 replacements. The note defines the term in the same sentence that introduces it, and nothing else in the note uses that definition. So no definition becomes a candidate cut.
- **'optional assessment'.** Decision: keep the term. Deciding occurrence: "Making a new human assessment a condition of each revision does." Replace the synonym 'optional study'/'studies' with it, 3 replacements. The term is defined at first use in the body ("when the process can proceed without it and its specification does not require it").

Terms kept unchanged:

- **'unfulfilled requirement'.** Keep. Deciding occurrence: "not by itself evidence that the system would fail or degrade without the task". There the term separates a requirement left unmet from a task the system needs. A plain 'undone task' would lose that requirement and need are separate.
- **'process specification' / 'specified task'.** Keep. The note separates specified tasks from habitual waits and from optional assessment. The habitual-wait bullet is out of scope and depends on this distinction.

Noticed but not proposed: 'evaluation', 'assessment', 'check' and 'review' all name human examination of results. They are ordinary words rather than abstractions, so this pass leaves them alone. The weekly-review paragraph and the second Scope bullet are out of scope. Neither contains an occurrence that these proposals would change: the bullet's 'actual wait' already matches the first proposal.
