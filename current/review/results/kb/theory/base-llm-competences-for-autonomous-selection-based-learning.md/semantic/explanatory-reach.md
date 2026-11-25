---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 86612d19c8e647c5ae2093248b1ab710
completed-at: '2026-11-24T13:18:09Z'
findings:
- scope: passage
  quotes:
  - Any sub-task shown to be reliably offloadable to harness code moves out of the
    LLM column
  reason: The mechanism explains why some semantic residue stays on the model. Code
    enforces defined rules without interpretation. Meaning-dependent judgments cannot
    be pre-paid when their inputs do not yet exist, and open-ended work keeps producing
    new inputs. The note gives no mechanism for the particular three-way cut, however.
    It could be regrouped into two or four competences without changing the argument,
    and the Scope revision clause lets the list change freely. The mechanism is present
    but thin for the specific enumeration in the title.
  level: info
contract: verdict
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/86612d19c8e647c5ae2093248b1ab710/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/b0339ef0f5f9dc140ff1c117/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/86612d19c8e647c5ae2093248b1ab710/outputs/review-explanatory-reach.md
raw-output-sha256: e6964fdf09d91b092ec07ba505e8d3897c4089852c991876358f20b538e660b7
---

# Review

## Summary

The central claim is that harness code can offload much of the loop, leaving semantic competences on the base LLM. Its mechanism is hard to vary. If the premise that new failure modes keep arriving is removed, the residue could be codified upstream, and the conclusion fails. If the error-correction asymmetry is removed, offloading loses its rationale. The claim is falsifiable: showing that one of the three competences can be offloaded reliably would refute part of it, and the Scope section says so. That revision clause is a stated test condition, not an ad-hoc escape hatch.

The weaker part is the decomposition into exactly three competences. The note motivates them as recurring kinds of semantic work in the loop: interpretation, diagnosis and synthesis, and judgment. It does not derive why the boundaries fall there. Its claim that the competences fail independently would constrain the cut if it were supported. Recorded as INFO.
