---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Testing the bet therefore requires a two-part empirical check
  reason: The bet states that a fixed-weight model can autonomously run double-loop
    deliberative learning with targeted correction. It requires recognizing a misleading
    gate, validator or criterion and revising it. The stated test checks, per change,
    operative dependence and on-balance improvement. The failure condition compares
    hazards with the gains the loop finds. Neither checks criterion revision, autonomy
    or targeted correction. Consider a loop that makes only single-loop edits under
    fixed human-written gates. It could pass both checks and avoid the failure condition,
    yet the double-loop core of the bet would remain untested. The test drifts from
    the claim it is said to test.
  level: warn
- scope: passage
  quotes:
  - 'Proof, formula, judgment: where the bet enters'
  reason: 'The section promises ''three precedents'' and its heading names proof,
    formula and judgment. The body gives four bolded entries: proof, fixed formula,
    changing heuristics and on-balance judgment. The heading omits EURISKO, and on-balance
    judgment is not a precedent. This is likely drift in the section''s enumeration.'
  level: info
- scope: passage
  quotes:
  - EURISKO's symbolic heuristics remained brittle
  reason: The section claims that the bottleneck was 'always' what played the value-function
    role. Its own EURISKO entry attributes that system's limit to brittle symbolic
    heuristics, which is a substrate property, and to human intervention. That sits
    in tension with 'always'. A human should confirm whether the intervention point
    counts as a judge limitation.
  level: info
- scope: passage
  quotes:
  - Second, an on-balance judgment played the role a scalar loss or value function
    plays in weight training
  reason: '''On-balance judgment'' names the in-loop decision in the example and the
    intro. In the precedent section it names the verdict standard: an improvement
    when every reasonable measure favors it. In the example the judge approves the
    edit on reversibility while the verdict would be open. The section''s last sentence
    separates the open verdict from the bounded decision, so the two senses are recoverable.
    The term still drifts between decision and verdict.'
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/294a65563f19bc7930c69f57/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a494636333e44e6fab547975bb757825
completed-at: '2026-11-21T19:30:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/outputs/review-internal-consistency.md
raw-output-sha256: fca4943d68701b82bb4fdfb5ad74b8e22f2065374663712d558892bf92517968
format: 2
---

# Review

Most claims hang together. The definition paraphrase, the fixed-criterion
special case, the "learned" verdict and the evidence-status section are
consistent with one another. The article does not overclaim against its own
admission that no end-to-end run has been completed.

The material inconsistency lies between the bet and its test. The bet is
specifically about autonomous double-loop revision of working criteria. The
evaluation apparatus that follows measures only per-change improvement and
net hazard balance, so the core of the bet could go unexamined.

Three smaller drifts are recorded as INFO:

- The precedent section's enumeration does not match its heading.
- The "always" bottleneck claim sits uneasily with the section's own EURISKO
  explanation.
- "On-balance judgment" slides between the in-loop decision and the
  improvement verdict.
