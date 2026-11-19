---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 62495c7f609ed31af00ff4646346793e8d78702222af9f60bab5a4af6eb6614c
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: b2349810d23546738f291648de810ccc
completed-at: '2026-11-16T21:58:17Z'
findings:
- scope: passage
  quotes:
  - 'Four declarations make a better-factory claim determinate: which states are compared,
    what relation they are compared under, how a state becomes the successor, and
    where the evaluator sits.'
  reason: 'Scope drift (title narrower than body). The body says four declarations
    make the claim determinate and gives each its own section: operative-state relata,
    an antecedent and scope-indexed relation, the measurement-versus-admission route
    to the successor, and evaluator location declared apart from the learner boundary.
    It also derives the preserved factory-development path from scope indexing. The
    H1 names only the first two declarations, and it omits scope indexing even though
    the body treats scope indexing as half of the relation''s design. The description
    carries the evaluator-location claim but the title does not. A title naming the
    four-declaration structure, or at least adding scope indexing and the separate
    evaluator location, would match what the body establishes.'
  level: warn
- scope: passage
  quotes:
  - Antecedence guards this claim's auditability; it is not constitutive of improvement.
    An independently supplied retrospective criterion can ground a legitimate improvement
    claim, just not this audit-proof one.
  reason: The title states without qualification that a better-factory claim uses
    an antecedent relation. The body limits that requirement to the auditable, relation-relative
    form of the claim and says that a retrospective criterion can ground a legitimate
    improvement claim. The opening paragraph's 'better under the declared relation'
    stipulation mostly covers this. Still, a reader linking the bare title could take
    it as a claim about every improvement judgment. This is a minor qualification
    and does not need a retitle by itself.
  level: info
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/a18942122cf57eb6e0c69c08/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/a18942122cf57eb6e0c69c08/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/b2349810d23546738f291648de810ccc/outputs/review-title-body-alignment.md
raw-output-sha256: 877e5c9da07973cd438e20d032b869ba82366e13ba24cef905fb1e7c96aa86b2
---

# Review

The body supports the title's two assertions. The relata are operative predecessor and successor states, not candidates or construction events. The relation is fixed before the development it judges. There is no claim drift.

The body establishes more than the H1 names, which is scope drift. It frames the claim as resting on four declarations and spends substantial sections on scope indexing, the two routes to a successor, and the separation of evaluator location from the learner boundary. The title captures only part of that structure. A smaller qualification also applies: the body limits antecedence to the auditable form of the claim, while the title states it without that limit.
