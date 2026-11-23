---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - deciding how much effort a local branch deserves relative to other work, when
    to stop or defer it, and whether a blocker warrants interrupting scarce operator
    attention
  - '**"This run should stop"** — a local execution judgment the isolated worker can
    make.'
  - a worker still makes many local branch choices (which hypothesis to test next,
    when to stop digging).
  reason: 'Stopping shifts roles across three sections: the opening places ''when
    to stop or defer it'' under global prioritization (which an isolated worker cannot
    reliably make), the split section classifies ''"This run should stop"'' as a local
    execution judgment the isolated worker can make, and the residual-friction section
    treats ''when to stop digging'' as a local within-episode choice. These can be
    reconciled—stopping a run on an injected local stop condition differs from stopping
    or deferring a branch on cross-task opportunity cost—so this is mild drift/ambiguity
    for confirmation rather than a hard contradiction.'
  level: info
- scope: passage
  quotes:
  - (under bounded effective context and a competing workload whose live state does
    not fit beside task-solving context). A system operating under those conditions
    whose isolated task workers reliably make decisions whose right answer depends
    on unseen competing work—or that loads full live portfolio state alongside deep
    task context without degrading execution competence—would refute the claim.
  - A separate pass—an operator, coordinator, or dedicated triage call—reads compressed
    summaries of competing items side-by-side against current bottlenecks without
    loading deep task context for any single item.
  reason: The state required for global prioritization shifts subtly between 'full
    live portfolio state' in the opening refuter and 'compressed summaries of competing
    items' in wide-shallow triage (as well as 'compressed global state' potentially
    injected into a worker's handoff in Residual friction and Open Questions). Because
    compressed summaries are lossy and still consume context, this is a mild tension
    rather than an outright contradiction.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/3af191ac890bf24628f656e7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 97a22d5aa3b140df99e1c93d298df950
completed-at: '2026-11-19T13:47:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/outputs/review-internal-consistency.md
raw-output-sha256: 0322b5007862f953deb906adcc3da13a7b14cff0c3232aec04b6aed3a0660793
format: 2
---

# Review

Across its frontmatter description, opening claim, mechanism section, two-view split, residual friction, Scope, and Open Questions, the note contains no pairwise contradictions. The description accurately summarizes the main trade-off without erasing the missing-context vs default-direction distinction, and the Scope boundaries align with the opening claim and the standing-rules qualification.

Two minor points of conceptual drift merit confirmation: "stopping" appears in three different roles (global branch stopping/deferral, local run stopping, and within-episode digging limits), and the comparison set required for global prioritization shifts from "full live portfolio state" in the opening refuter to "compressed summaries" in the triage pass and injected worker proxies. Both are reconcilable in context, so the gate passes with informational findings.
