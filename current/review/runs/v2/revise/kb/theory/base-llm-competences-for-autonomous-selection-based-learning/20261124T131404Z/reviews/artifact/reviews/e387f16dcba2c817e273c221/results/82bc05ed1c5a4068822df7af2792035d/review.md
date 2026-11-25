---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A bounded empirical illustration of a base-model floor appears in [Harness Evolution
    Hits a Ceiling](../sources/harness-evolution-ceiling-weight-training.ingest.md)
  reason: The note draws empirical support from an external study via its source ingest,
    but `traits` lists only `title-as-claim`. The `has-external-sources` trait ("The
    note cites material outside the project") would route the review that checks this
    citation. Traits are optional, so this is advisory only.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/types/note.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/types/note.md
note-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/82bc05ed1c5a4068822df7af2792035d/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/e387f16dcba2c817e273c221/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: 82bc05ed1c5a4068822df7af2792035d
completed-at: '2026-11-24T13:16:20Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/82bc05ed1c5a4068822df7af2792035d/outputs/review.md
raw-output-sha256: 510ed120b6feba8c27db72268b3ae27096982b85f6a5f5d3a1f97f5014c4eada
format: 2
---

# Review

## Summary

The note does what the `note` type spec's authoring instructions ask.

- **Transferable claim, main claim near the top.** The opening paragraph, marked "Working hypothesis", states the mechanism: harness code can take over enforcement, evidence capture and store bookkeeping. The numbered list right after it names the three semantic competences that remain on the frozen base LLM. A reader gets the claim before any elaboration.
- **Title as compressed handle.** The title carries both halves of the claim: harness offloading, and the three competences that remain.
- **Description as retrieval filter.** It is one sentence. It separates this note from the scheduler–LLM separation and semantic-relocation notes by naming the three-competence split, and it flags the claim's hypothesis status.
- **Links to adjacent notes.** The body links inline where each relationship applies: scheduler–LLM separation, semantic relocation, operative change, diagnostic richness, on-balance judgment and criterion revision. The footer gives each link a relation label and a reason.
- **Rationale, not procedure.** The note explains why the split falls where it does. It also explains why store maintenance and criterion revision need no fourth competence. It gives no imperative operating steps.
- **`## Scope`.** The section exists and states the claim's limits. The split is a working hypothesis that offloading results can narrow or practice can extend. The competences are proposed as necessary for autonomous operation, not sufficient for continual learning. The empirical illustration is also bounded inline to one benchmark and one loop.
- **Template shape.** The note follows the template: prose body, `## Scope`, `## Open Questions`, then the `Relevant Notes` footer.

The only remark is advisory. The trait list could add `has-external-sources` because the note cites an external study through its ingest.
