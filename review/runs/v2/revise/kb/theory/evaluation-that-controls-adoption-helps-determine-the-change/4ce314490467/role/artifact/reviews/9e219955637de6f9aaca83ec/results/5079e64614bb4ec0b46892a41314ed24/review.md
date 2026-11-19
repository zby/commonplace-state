---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/theory/README.md — needs only an index citation: the title
    and a gloss saying the note distinguishes automated adoption from required human
    monitoring or revision, and from optional assessment. The note''s opening section,
    its ''Name the process being automated'' section and its optional-assessment case
    together carry all three parts of that gloss.'
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/role/artifact/reviews/9e219955637de6f9aaca83ec/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/role/artifact/reviews/9e219955637de6f9aaca83ec/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/role
launch: 5079e64614bb4ec0b46892a41314ed24
completed-at: '2026-11-17T13:10:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/role/calls/launches/5079e64614bb4ec0b46892a41314ed24/outputs/review.md
raw-output-sha256: fb933d3248d0070ad8a86e1fe4d630c0a0ae1cd4ef6df28e07cdf9777f2c8a6d
format: 2
---

# Role in the KB: Removing approval waits can leave required human evaluation in place

## Role
Only the theory collection index cites the note; no dependent argues from it, borrows a term from it or uses it as a premise. Its KB role, as dependents show it, is an indexed entry for the distinction between removing a human approval wait, leaving a specified human monitoring or revision task in place, and optional assessment.
Relied on: the overall three-way distinction (automated adoption vs. required human monitoring or revision vs. optional assessment), as an index gloss only. Unused: "blocking dependency" vs. "unfulfilled requirement"; the claim that automating a review differs from retiring it as a change in requirements; the required-approval and optional-assessment cases; the weekly-review example; the scope points on anticipated assessment and habitual waits; the links to the operative-states and routine-approvals notes.

## Dependents
- `kb/theory/README.md` — an index citation with a one-line gloss of the note's distinction.

## Duplication
None. The README gloss summarizes the note's description and is not a competing statement of the claim.

## Untaken recommendations
None. The only linking file is an index and recommends no change.

## Reach
A change to the note's title or to its central three-way distinction would reach `kb/theory/README.md`, whose link text and gloss restate them. No dependent relies on the note's other claims or terms (the blocking-dependency/unfulfilled-requirement pair, the automation-vs-retirement claim, the examples or the scope points), so changing those reaches no one.
