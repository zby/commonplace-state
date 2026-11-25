---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md),
    harness code can take over much of the loop's machinery
  reason: The target defines scheduler–LLM separation as code maintaining workflow
    state (task records, dependencies, counters, completion state) and enforcing defined
    transitions while models supply judgments. The note's list extends that to context
    assembly, replay, ablations, bisects and rollbacks, which the target does not
    discuss. The core division (code enforces defined procedure; the model judges)
    supports the extension, so this is an application, not a mismatch. Recorded for
    visibility only.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/c424e09f358a437589cf445774df407b/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/1c24309a664a6811b1dc66ae/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: c424e09f358a437589cf445774df407b
completed-at: '2026-11-24T13:17:08Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/c424e09f358a437589cf445774df407b/outputs/review-concept-attribution.md
raw-output-sha256: 8b092af4b213f5d19dfd38834d9c3c1c77939cc48106fc323515c9bdc1e6d587
format: 2
---

# Review

## Summary

I checked each place where the note identifies one of its concepts with a linked note's concept. All eight targets resolved.

- **Selection-based learning**: the definition's proposal–evaluation–rejection loop matches the "autonomous selection-based learning loop" the note discusses.
- **Scheduler–LLM separation**: the target's division between code and model supports the note's offloading list. The list goes beyond bookkeeping into replay and ablation; see the info finding.
- **Semantic work can be relocated but not eliminated**: the target's title claim and opening, that mechanical work can shrink while semantic judgment can only be placed, match the note's use.
- **Operative change**: the definition requires a behavioral-authority path through which a change reaches later behavior. Competence 1, letting prose actually govern behavior, is that consumer-side condition.
- **Diagnostic richness**: the target concerns the failure evidence a proposer can use to form causal hypotheses. This fits competence 2's diagnosis from traces.
- **On-balance judgment with an LLM**: the target covers trade-off comparison and misleading directions, which fits competence 3's trade-off weighing and recognizing a misleading check.
- **Criterion revision**: the single-/double-loop definition makes double-loop learning the revision of the deciding criterion, which matches the note's usage.
- **Harness Evolution Hits a Ceiling**: the ingest's Limitations section states that "the three no-gain lines are also the three weakest models" and that the rule "may reduce to 'the harness lever needs a capable enough model'". This supports the note's bounded "illustration of a base-model floor".
