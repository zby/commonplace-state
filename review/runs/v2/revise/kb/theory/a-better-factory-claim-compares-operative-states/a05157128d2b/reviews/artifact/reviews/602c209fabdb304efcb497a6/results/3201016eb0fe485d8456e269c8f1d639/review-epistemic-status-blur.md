---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - a retained change can degrade the factory as easily as improve it
  reason: '''As easily as'' reads as an empirical parity claim about how often retained
    changes degrade versus improve, and no evidence is given. The argument needs only
    the derived point that retention places no quality requirement on the change,
    so a retained change can degrade the factory.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 8c672c8c1b5fb29a3be9d27397fb32a75d860fe34017c42124b9791e69dfc4e9
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/602c209fabdb304efcb497a6/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/602c209fabdb304efcb497a6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-epistemic-status-blur.md
raw-output-sha256: ad054d04a013ec093abf36b9fbd541068622005620a26041a0023558c2341a46
format: 2
---

# Review

The note is mainly a conceptual framework, and it presents it as the note's own construction throughout:

- "This framework adds prior declaration…"
- "This framework uses the predecessor's prior capabilities as that scope"
- "the shape this framework declares, not the only declarable one"

The opening stipulates that "*better* means better under the declared relation", which tells the reader that the central claim is definitional and relation-relative. It is not presented as an empirical finding.

Derived consequences carry derivation wording, and their limits are stated beside them. "Prior declaration prevents that form of post-hoc selection" is immediately followed by "It does not show that the requirements track factory quality." The three search-machinery cases are labelled "hypothetical". The causal contribution needed for the learning case is assigned to the experimental-contrast requirement rather than assumed from the sequence of events. The open problems are in Open Questions and Scope, so their status is recoverable: what makes a successor genuinely better, and whether prior scope can be specified precisely.

Support is not spread to neighbouring claims. The passed comparison is explicitly said not to establish the experience link, and internal adoption controls are said not to establish passage of the comparison.

The only wording that overstates its status is the parity phrase "as easily as" in the opening (INFO).
