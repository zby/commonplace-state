---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 0beda3578055425f86b0ff83de24e19e
completed-at: '2026-11-19T15:53:05Z'
findings:
- scope: passage
  quotes:
  - 'Crucially, this split unbundles two decisions that naive agent workflows collapse
    into one, while keeping a third workflow-memory policy orthogonal:'
  - '- **"This finding or answer should survive"** — an orthogonal workflow-memory
    policy ensuring later runs do not re-ask the same question, independent of whether
    triage routes the item to immediate action.'
  - an operator's answer to a stop can be recorded so the next run does not re-ask
  reason: Cross-run answer persistence ('ensuring later runs do not re-ask the same
    question') is explicitly orthogonal to the conflict between context isolation
    and global prioritization. Recording scale-bearing local facts for later triage
    is already covered by step 1 and the following paragraph; elevating an ADR 138
    workflow-memory policy to a third co-equal bullet dilutes the two-way unbundling
    of local stopping from global operator-attention allocation. Remove the orthogonal
    third bullet (and its lead-in clause) and trim the matching answer-carryover clause
    from the ADR 138 illustration, leaving that policy in ADR 138.
  level: warn
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/0beda3578055425f86b0ff83de24e19e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/8efbebfa8d7c9d393630d4ee/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/0beda3578055425f86b0ff83de24e19e/outputs/review.md
raw-output-sha256: f01bc25e77764a01467f1837b9944e3d2d698d818c3dc63b30964c53193760bf
---

# Review

The note's core commitment is well-bounded: isolating an agent's context for task focus removes the live comparison set required for relational global prioritization, explaining priority flattening under action-biased defaults and the trade-off in splitting narrow-deep execution from wide-shallow triage. Its boundary conditions, objections handled (standing priority rules and non-calibrated scalar cutoffs), contrast with oracle asymmetry, residual interface friction, and open questions all directly support that argument.

The one branch that dilutes the argument is the workflow-memory policy imported from ADR 138 into the unbundling taxonomy. The narrow-deep versus wide-shallow split directly unbundles two decisions—whether a local run should stop on a hard blocker or rule, and whether the operator should act now given competing work. Recording an operator's answer so future stateless runs do not re-ask the same question is a separate persistence concern, as the text itself concedes by calling it orthogonal and independent of triage routing. Because ADR 138 already houses that carry-over policy and the note already states that the isolated worker preserves scale-bearing local facts on a shared surface or stop record, removing this side branch sharpens the execution-versus-triage interface without losing anything the main claim requires.
