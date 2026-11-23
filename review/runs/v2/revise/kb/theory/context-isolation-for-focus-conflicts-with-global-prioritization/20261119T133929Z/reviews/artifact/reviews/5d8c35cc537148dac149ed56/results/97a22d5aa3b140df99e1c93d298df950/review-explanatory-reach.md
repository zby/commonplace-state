---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A system operating under those conditions whose isolated task workers reliably
    make decisions whose right answer depends on unseen competing work—or that loads
    full live portfolio state alongside deep task context without degrading execution
    competence—would refute the claim.
  reason: 'The core mechanism is present and hard-to-vary on its stated premises,
    but one link is thin: the opening argues that full live portfolio state cannot
    fit beside deep task context and that static rules cannot substitute, whereas
    the next section treats compressed summaries of competing items as sufficient
    for wide-shallow triage. The mechanism does not yet constrain why a compact, dynamically
    updated compressed summary of global state could not be co-loaded with deep task
    context without eroding focus—a boundary the note leaves to Open Question 2.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/5d8c35cc537148dac149ed56/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 97a22d5aa3b140df99e1c93d298df950
completed-at: '2026-11-19T13:47:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/outputs/review-explanatory-reach.md
raw-output-sha256: 55ab4a47449b913f7bf99ecd2824b4ebaa26af905e0061ec3d78ae44db4e434b
format: 2
---

# Review

The central claim supplies a genuine, load-bearing mechanism: per-window attention feasibility forces excluding unrelated work during deep task solving; stateless workers retain no ambient cross-project state outside their window; and relational prioritization depends on a live comparison set that static priority rules cannot supply. Varying any of these premises changes the conclusion in the ways the note itself identifies—removing the context bound eliminates the conflict on small single-thread tasks, replacing relational prioritization with intrinsic local checks lets isolated workers succeed, and flipping the default action flips the failure direction from eager escalation to silent suppression.

The Scope boundaries follow directly from the mechanism rather than acting as ad-hoc escape hatches, and explicit refutation conditions are stated. The one thin link—why compressed live global summaries that suffice for wide-shallow triage cannot simply be co-loaded into a deep task window—is acknowledged in the interface discussion and Open Questions, making this an informational note on an otherwise well-constrained explanation.
