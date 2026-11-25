---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Because an LLM that writes code can also build new harness tools for those jobs,
    the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head.
  reason: The stated reason is the LLM's ability to author harness tools. The mechanism
    that relieves the model is that harness code holds the state, whoever wrote the
    code. The LLM-authorship framing is relevant to autonomy, since no human builds
    the tools. It emphasizes one route but does not exclude human-written or pre-existing
    harness code, so the finding is INFO.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/d857420e549542ebaf80f2dbabefeed3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/e602dbec8643c25b58dd3f01/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: d857420e549542ebaf80f2dbabefeed3
completed-at: '2026-11-24T13:17:10Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/d857420e549542ebaf80f2dbabefeed3/outputs/review-framing-mismatch.md
raw-output-sha256: 4e848eecc06a42dee71c2b24590a12ba43cf73fe4764395d2f81f4c3ebfdfad9
format: 2
---

# Review

## Summary

The note's mechanism statements are mostly framed at the right level. The harness/LLM split is stated in terms of mechanical versus semantic work, which matches its grounding. The empirical paragraph is explicitly bounded to one benchmark and loop. The Scope section states the hypothesis's limits.

One causal sentence ties the offloading benefit to the LLM's code-writing ability rather than to the existence of harness code itself. Because the note concerns autonomous loops, this is emphasis rather than exclusion.
