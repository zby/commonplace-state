---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - our working hypothesis is that three irreducible semantic competences remain on
    the frozen base LLM
  reason: The cited mechanism (semantic work can be placed but not eliminated) says
    semantic judgment can move to another processor or upstream through codification.
    It does not say the judgment must stay on the base LLM. The note gets to 'remain
    on the frozen base LLM' only through its autonomy condition, where no other semantic
    processor is available. That condition comes earlier ('autonomous selection-based
    learning loop') but is not restated here. The framing emphasizes the LLM as the
    location without excluding cases the mechanism covers. The later human-assisted
    bootstrap passage also shows the note knows people can supply the step.
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
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/c424e09f358a437589cf445774df407b/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/e602dbec8643c25b58dd3f01/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: c424e09f358a437589cf445774df407b
completed-at: '2026-11-24T13:17:09Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/c424e09f358a437589cf445774df407b/outputs/review-framing-mismatch.md
raw-output-sha256: 9a9476e6de2bf35bab84e5ddc6b5f97a6024ddc839428680fad35518bd325699
format: 2
---

# Review

## Summary

I checked each sentence that gives a reason or names a mechanism.

- The opening says fixed weights do not remove dependence on the base model, and that harness code can take over loop machinery. Both frame the offloading claim at the right level: loop functions in general, not one domain.
- "Because an LLM that writes code can also build new harness tools ..." names the actual mechanism, which is code-writing ability that extends the harness.
- The three competences name semantic operations: interpretation, diagnosis/synthesis and judgment. None is narrowed to one task domain. The "open-ended work" qualifier states the condition under which new failure modes keep arriving, so it is the right scope rather than an exclusion.
- The store-maintenance paragraph places detection on harness code and semantic conflict work on competences 2 and 3. That matches the mechanical/semantic split used throughout.
- The evidence paragraph frames the source as a "bounded empirical illustration" within "one benchmark and loop". This fits the source's confound between weak models and no-gain lines.

The only point is the info finding. The mechanism allows relocation to any semantic processor, and the sentence reaches "the frozen base LLM" only through the autonomy premise.
