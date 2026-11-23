---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Second, and this is our empirical bet: **putting a fixed-weight language model
    in the judge slot turns deliberative learning into an automated machine learning
    paradigm.**'
  reason: 'The body supports the title''s claim. It defines deliberative learning,
    and in the routing-line example and the proof/formula/judgment section it shows
    an on-balance judgment doing the work of a scalar value function. The body also
    establishes a second level of claim that the title does not name: a fixed-weight
    language model can fill the judge slot. The article calls this machine judge what
    is new, and most of the later sections serve that bet: the precedents, the Bitter
    Lesson section and the evidence and limits. So the H1 is narrower than the body.
    It names the paradigm and its judge role but not the LLM bet. This is not drift,
    because the bet is about who fills the judgment role the title names. A title
    that also named the language-model judge would match the body more closely.'
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 18cb61e22005e8f5cc0d519de94f3b6171734341f305219f295b68697b3ce0cc
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/bdfbde965aac4fe598acb9a5dcaa39dc/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/48d678b0b9d8ffb3864a8af2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: bdfbde965aac4fe598acb9a5dcaa39dc
completed-at: '2026-11-21T19:25:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/bdfbde965aac4fe598acb9a5dcaa39dc/outputs/review-title-body-alignment.md
raw-output-sha256: 2225cd86dcf9af2cb92c13fdfe9839b96b28f2c205e2a6cd284b2a71cbbb41fc
format: 2
---

# Review

## Summary

The H1 is "Deliberative Learning: Judgment in Place of a Value Function". The body holds to it. The opening states that an on-balance judgment works in place of a value function. The worked example concludes that the judgment "played the role a scalar loss or value function plays in weight training". The comparison table sets "Rejectable judgment in the loop" against "Scalar loss, reward, or value function". The precedents section treats proof, fixed formula and on-balance judgment as successive fillers of the value-function role. Nothing in the body contradicts or replaces the title's claim.

The one gap is emphasis. The body explicitly makes a two-level claim, and its second level, the fixed-weight language-model judge, is the part the article calls new. The title leaves it implicit. That bet is a specialization of the title's judgment role, not a different claim, so the finding is info-level and the gate passes.
