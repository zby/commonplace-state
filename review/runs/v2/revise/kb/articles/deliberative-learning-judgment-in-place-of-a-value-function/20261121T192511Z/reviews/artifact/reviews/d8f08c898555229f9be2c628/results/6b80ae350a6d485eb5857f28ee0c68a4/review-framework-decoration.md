---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Three payoffs follow directly from storing what the system retains in readable,
    addressable artifacts.
  reason: 'The comparison table''s last three rows (when updates happen, credit assignment
    and correction, inspectability) are restated in prose straight after it: immediate
    deployment-time adaptation, inspectability now, and fixing the faulty line without
    wiping out unrelated work. The table is still load-bearing, because each row''s
    distinction is used later (substrate and value-function role in the precedents
    and Bitter Lesson sections, targeted correction for PRODIGY and EURISKO). The
    overlap is redundancy, not decoration; the paragraph could be cut to the payoff
    claims the table does not state, such as inspection by agents at volumes people
    could not read.'
  level: info
- scope: passage
  quotes:
  - 'four hazards can defeat it:'
  reason: 'The four-hazard list is load-bearing: three of its items reappear in the
    falsification condition. ''Unfaithful rationales'' repeats the faithfulness cost
    already stated in the comparison section, and ''Judgment reliability'' is not
    named in the falsification sentence. These are minor alignment points, not a decorative
    structure.'
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/6b80ae350a6d485eb5857f28ee0c68a4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/d8f08c898555229f9be2c628/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 6b80ae350a6d485eb5857f28ee0c68a4
completed-at: '2026-11-21T19:26:18Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/6b80ae350a6d485eb5857f28ee0c68a4/outputs/review-framework-decoration.md
raw-output-sha256: d1eb5c21300b5559bb13fc61c140d8c670c6161ba7c72c84b752a7d800156640
format: 2
---

# Review

## Summary

I checked each structure in the article:

- **Comparison table (five axes).** Each axis marks a distinction that the argument uses later. Substrate and value-function role frame the precedents section and the Bitter Lesson section. Update timing supports the deployment-time claim. Credit assignment supports targeted correction in PRODIGY and EURISKO. Inspectability supports the payoff and faithfulness discussion. The table adds no vocabulary or categories that go unused. One sentence could list the contrasts, but readers coming from machine learning use the table as a lookup that later sections keep returning to. The table is load-bearing. Its overlap with the next paragraph is noted as info.
- **Proof / formula / changing heuristics / on-balance judgment ladder.** Each rung carries its own inference: proof is optimal but blocks improvements it cannot prove; PRODIGY shows single-loop targeted correction; EURISKO shows double-loop revision; on-balance judgment handles the case where no single formula fits. The bet is placed at the last rung. The ladder is load-bearing.
- **Two-condition definition.** Its boundary cases separate concrete systems: opaque weight updates fail the first condition, while click-ranking jobs, tabular RL tables and count-triggers fail the second. It is load-bearing.
- **Two-part empirical check.** This is a decision rule for testing the bet. It is load-bearing.
- **Four-hazard list.** Three of its items feed the falsification condition. It is load-bearing, with the minor alignment points noted as info.

The article contains no notation or equations.
