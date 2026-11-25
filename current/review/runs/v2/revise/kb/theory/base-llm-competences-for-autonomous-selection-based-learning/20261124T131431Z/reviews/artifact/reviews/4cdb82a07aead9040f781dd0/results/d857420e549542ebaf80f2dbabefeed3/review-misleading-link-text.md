---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - ([diagnostic richness](./diagnostic-richness-constrains-outer-loop-learning-quality.md))
  reason: The link is placed as the label for competence 2, the model's ability to
    turn a failure and trace into a diagnosis and propose remedies. A reader who does
    not follow the link may take 'diagnostic richness' to name that model competence.
    The target defines diagnostic richness as the retained evidence available to the
    proposer and says that proposer capability is 'separate from the evidence surfaces
    this note isolates.' Reframe the inline link to state the relation, e.g. 'its
    quality depends on the harness's [diagnostic richness](…)', as the footer already
    does.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/d857420e549542ebaf80f2dbabefeed3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/4cdb82a07aead9040f781dd0/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: d857420e549542ebaf80f2dbabefeed3
completed-at: '2026-11-24T13:17:10Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/d857420e549542ebaf80f2dbabefeed3/outputs/review-misleading-link-text.md
raw-output-sha256: 100b1494528ede5eb68e670f4a2b8efdc9dbf44968934cf5dfa0d47e838eea41
format: 2
---

# Review

## Summary

Eight distinct targets were checked; all resolved.

- Selection-based learning, scheduler–LLM separation, semantic work relocation, and Harness Evolution Hits a Ceiling: the link text matches the target title or claim.
- Operative change (competence 1): the target defines change that reaches later behavior through a consumer path. This fits "let them govern its behavior."
- On-balance judgment with an LLM (competence 3): the target covers comparing options under genuine trade-offs and tracing misleading directions. This fits the competence.
- Criterion revision → single-loop and double-loop learning: the target defines double-loop as revising the deciding criterion. This matches.

One inline link gives a wrong impression. The diagnostic-richness link names the evidence surface as if it were the model's diagnostic competence, which the target explicitly separates from proposer capability. The footer annotation states the relation accurately.
