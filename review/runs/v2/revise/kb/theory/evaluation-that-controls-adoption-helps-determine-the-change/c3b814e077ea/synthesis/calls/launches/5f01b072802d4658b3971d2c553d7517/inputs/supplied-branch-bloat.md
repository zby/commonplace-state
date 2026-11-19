---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 32c9c946ad8092a20aa5d4cfe1aa0e58bc5f9bfe61100f236c18efc78f6c479b
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: 310ef2cedd52478d9fd5a319c4ad987e
completed-at: '2026-11-17T07:54:55Z'
findings: []
contract: verdict
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/1d5b53cb58da7164cfc54421/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/1d5b53cb58da7164cfc54421/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/310ef2cedd52478d9fd5a319c4ad987e/outputs/review.md
raw-output-sha256: 68dc091ee9e301c9050c279cd957e78da8d4abbb7c8e76818303798db062036b
---

# Review

## Main claim

The note claims that removing approval waits automates adoption but can leave required human evaluation in place, for monitoring or for subsequent revision. Whether evaluation is required depends on the process being automated and on its stated requirements. Human assessment that only observes results does not create that dependency.

## Side material checked

- **Causal-credit contrast and link to the operative-states comparison.** This sets the boundary of the note: it separates an operating dependency from a judgment that the system improved. It is two sentences long and stops a likely misreading, so it stays.
- **Link to the routine-approvals note in the required-approval case.** This backs the case's statement that the process depends on the person "even if the maintainer always approves." The note does not develop the side argument itself; it points to the separate note.
- **"Conversely, a program can apply human-authored acceptance rules..."** This counterexample marks where human authorship stops creating a per-change dependency, so it directly limits the claim.
- **Usefulness and adequacy caveat, and the warning that skipping is not fulfilment.** Both are boundary conditions on "name the process being automated." They block the inference that a requirement, once identified, is justified, and they block treating a skipped task as automation.
- **Scope bullets: anticipated influence and habitual waits.** The first bullet excludes non-blocking influence. The second covers the "prevents that process from proceeding in practice" clause from the opening, so it backs a stated premise rather than adding a new idea.

None of these is a hypothesis, analogy, prediction or extension that needs its own evidence. Each side passage supplies a boundary, counterexample or contrast for the main distinction. No branch needs removal, demotion or a new home.
