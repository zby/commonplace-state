---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), harness code can take over much of the loop's machinery"
    reason: "The target defines scheduler–LLM separation as code maintaining workflow state (task records, dependencies, counters, completion state) and enforcing defined transitions while models supply judgments. The note's list extends that to context assembly, replay, ablations, bisects and rollbacks, which the target does not discuss. The core division (code enforces defined procedure; the model judges) supports the extension, so this is an application, not a mismatch. Recorded for visibility only."
    level: info
outcome: pass
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
