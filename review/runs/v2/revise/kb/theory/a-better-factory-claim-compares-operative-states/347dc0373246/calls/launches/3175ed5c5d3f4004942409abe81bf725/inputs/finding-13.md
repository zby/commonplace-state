---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: c50667b742724b11b82a141c9cc38486
completed-at: '2026-11-16T22:00:06Z'
findings:
- scope: passage
  quotes:
  - is stated for factories because the preserved-scope clause draws on factory development
    being in scope
  reason: The scope bullet frames the factory restriction as falling on the fourth
    listed part ('The first three parts carry'), which is evaluator location declared
    apart from the learner boundary. But the stated reason, the preserved-path consequence,
    comes from scope-indexed non-regression (the second part) applied to factory development,
    and the preserved path is not among the four listed parts. The mechanism separating
    admission from measurement, and evaluator location from boundary, applies to any
    system that revises its own machinery. The framing therefore excludes cases that
    the mechanism covers. The factory-specific item is the preserved-path consequence,
    not the fourth structural part.
  level: warn
- scope: passage
  quotes:
  - A real episode can be described either way, and the description determines where
    the evaluator sits.
  reason: 'The body places the evaluator by a causal fact: whether judgment gated
    installation (''falls on opposite sides depending on whether it gated the successor'').
    This bullet frames evaluator location as fixed by the chosen description. The
    mechanism is whether evaluation determined the successor, and the description
    should track that fact. Framing it as a descriptive choice misdirects the reader
    about what settles the declaration.'
  level: warn
- scope: passage
  quotes:
  - This is also why the oracle problem for better-factory claims is sharp rather
    than incidental.
  reason: '''This is also why'' presents the oracle problem''s sharpness as following
    from the preceding point about evaluator location and admission. Of the three
    reasons given, only the third (human acceptance judgments re-entering the boundary)
    depends on that point. The expense of judging over the declared family and the
    gameability of inspectable tests are independent mechanisms. Present them as separate
    reasons, and present the boundary consequence as the one link to this section.'
  level: warn
- scope: passage
  quotes:
  - At a learner boundary that includes the operator, a passing successor is cheap
  reason: 'The surrounding sentences concern attribution: ''the open part is attribution'',
    and ''the operator can be the learner''. What is cheap at an operator-inclusive
    boundary is attributing the improvement to learning, not producing a passing successor.
    The framing emphasizes the wrong object but is recoverable from context.'
  level: info
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e5555efeb6ede2efc7417a70/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/e5555efeb6ede2efc7417a70/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/c50667b742724b11b82a141c9cc38486/outputs/review-framing-mismatch.md
raw-output-sha256: 8cdcce3b1a91b96afc27915d0537011a990e418fb0c8647f143482ed9696c5db
---

# Review

The reason-giving sentences in the main sections mostly identify their mechanisms correctly. Antecedence blocks post-hoc dimension choice. Scope indexing makes non-regression meetable. Measurement following the update keeps it off the causal path. The deployed-system boundary brings all operative machinery into the compared states.

Three framings misdirect. The final Scope bullet attaches the factory restriction to the wrong part of the structure, so it understates how far evaluator-location separation transfers. The route-as-description bullet reframes a causal fact from the body as a choice of reading. The oracle paragraph presents mostly independent difficulties as consequences of the evaluator-location point. A fourth sentence calls the passing successor cheap when the cheap thing is the learning attribution; this is information only.
