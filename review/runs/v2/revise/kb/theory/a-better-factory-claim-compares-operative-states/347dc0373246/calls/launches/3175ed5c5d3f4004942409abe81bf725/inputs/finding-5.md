---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 5c21f7686bc944168332189f20307082
completed-at: '2026-11-16T21:59:47Z'
findings:
- scope: passage
  quotes:
  - The claim holds between two operative states of the factory, under an assessment
    relation fixed before the development it judges, and its evaluator sits at a declared
    location that is not settled by the learner boundary.
  reason: 'This sentence lists the claim''s parts, and the next paragraph lists them
    again as the four declarations. The second list is the one later sections use:
    it says ''the fourth declaration below'' and adds the successor route. Two lists
    in a row cost space without telling the reader anything new. Cut this sentence,
    or fold its one distinct point, that the evaluator location is not settled by
    the learner boundary, into the four-declaration paragraph.'
  level: warn
- scope: passage
  quotes:
  - This is not an extra virtue bolted onto the comparison; it is what scope-indexed
    non-regression already says once the factory-development path is part of what
    the predecessor could do.
  reason: This is defensive redundancy. The heading already says preservation falls
    out of scope indexing, and the sentence before this one already derives it from
    non-regression over the predecessor's prior capability set. This sentence says
    the same thing a third time to answer an objection the derivation has already
    closed. Cut it.
  level: warn
- scope: passage
  quotes:
  - 'Antecedence blocks post-hoc dimension selection. It does not make the declared
    dimensions the right ones: a comparison can be properly declared in advance and
    still measure something that does not matter.'
  reason: 'The body has already said this: ''That is all antecedence buys: a comparison
    capable of failing, not a relation shown to track factory quality.'' The Scope
    bullet restates that limit. Its only new part is the phrase ''still measure something
    that does not matter''. Fold that phrase into the body sentence and delete the
    bullet, or keep the bullet and cut the body sentence.'
  level: warn
- scope: passage
  quotes:
  - The framework indexes and disciplines the comparison; it does not supply an oracle
    for it. What makes a successor genuinely better over an open family remains unresolved
    here.
  reason: The opening paragraph already says the claim is 'not a verdict on the factory's
    quality over its open production family', and the evaluator section already discusses
    the oracle problem. This bullet may still be useful as the place where the note
    marks this as unresolved. It is unclear whether that marker does enough reader
    work to justify the third statement of the same limit.
  level: info
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/47cb77c4c9b63a8eb83170ba/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/47cb77c4c9b63a8eb83170ba/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/5c21f7686bc944168332189f20307082/outputs/review.md
raw-output-sha256: 1b98f3cafbc700cfba734bcae6925e848a9e69930f1f9d2312e22a596128588b
---

# Review

## Summary

Most chunks earn their space. These parts are not redundant: the three-term vocabulary, the two successor routes, the two-component relation with scope indexing, the split between preservation and compounding, the evaluator/boundary argument, and the 'Neither claim entails the other' section. Each one adds a distinction that a later part of the note relies on. Most Scope bullets also add something new: the retrospective-criterion admission, the retirement-permitting relation, routes as declarations rather than partitions, and the reach claim.

The redundancy comes from one pattern. The note restates one limit several times: the comparison is auditable but is not a verdict on factory quality. That limit appears in the opening paragraph, at the end of the antecedence paragraph, and in two Scope bullets. The note also lists its structure twice in the opening, and it justifies the preserved-path consequence a third time after the heading and derivation have already established it. The fix is to cut and fold, not rewrite. The closing sentence of the successor-routes section and the closing sentence of the evaluator section restate earlier points, but each turns them into a consequence that the next part uses. They therefore pass.
