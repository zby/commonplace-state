---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 6a632aa959714475b2d25ece99660e9e
completed-at: '2026-11-24T13:17:13Z'
findings:
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs,
    the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head.
  reason: This aside sits between the offload list and the sentence that introduces
    the three competences. It restates the offload half of the claim with a tool-building
    point that the note never uses again, and it delays the turn to the residual competences.
    Cutting it, or folding the tool-building point into the offload list's lead-in,
    would put the pivot ('semantic work can be relocated without being eliminated')
    right after the list and make the claim's second half arrive sooner.
  level: info
contract: verdict
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/6a632aa959714475b2d25ece99660e9e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/8512350f2932a35406fe287d/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/6a632aa959714475b2d25ece99660e9e/outputs/review.md
raw-output-sha256: 3460f2adfd9bc0aecd0114c91df3848df9a09c9c697ea880f42548c82f494dcc
---

# Review

## Core claim

Stated in one sentence from the note's own commitments: in an autonomous selection-based learning loop with frozen weights, harness code can take over enforcement, evidence capture and replay, and store bookkeeping, and as a working hypothesis this leaves three semantic competences on the base LLM: interpreting unformalized text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs while recognizing missing evidence.

## Prominence

The title and description state this two-part claim directly. The body opens with it and uses the order the claim needs. First comes the offload list, then the relocation-not-elimination pivot, then the three numbered competences in bold. Later sections stay subordinate. Store maintenance and criterion revision reduce to competences 2 and 3. The independence paragraph explains why the split is useful. The ingest gives a bounded illustration of a base-model floor. The Scope section restates the hypothesis status. None of this competes with the main claim.

The one shape issue is minor. The three competences arrive only after a bulleted list and a transition paragraph. In that paragraph, the sentence about the LLM building its own harness tools adds a side point instead of moving the argument forward. The claim is still easy to find and remember, so this is INFO, not WARN.
