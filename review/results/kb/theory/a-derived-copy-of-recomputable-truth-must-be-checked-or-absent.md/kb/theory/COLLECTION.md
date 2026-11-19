---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/theory/COLLECTION.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/theory/COLLECTION.md
criterion-sha256: 23ede037003607491dace7447a749ba3d1865aa8fd8cd08a03da6749af864112
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T132933Z
launch: ed5f576ca9a941fab90b636267b50cca
completed-at: '2026-11-15T13:30:18Z'
findings:
- scope: passage
  quotes:
  - The spread is what shows it generalizes
  reason: The contract states that no number of singular observations establishes
    a universal statement and that cases a claim was generalized from explain its
    origin without corroborating it. This sentence presents the four Commonplace instances
    as what shows the universal rule generalizes, which treats illustrations and origin
    cases as corroboration. Recast the instances as illustrations or applications
    of the rule, or name a test the rule could have failed.
  level: warn
- scope: passage
  quotes:
  - validator-enforced instance of the rule
  reason: Under 'Origin is not corroboration', an `evidenced-by` context phrase that
    claims corroboration must say what the claim risked and whether the evidence was
    recorded after the claim or independently of how it was built; otherwise the phrase
    must say that the evidence qualifies or bounds the claim. This phrase presents
    the tag-readme `complete` mark as an instance of the rule without either. The
    case also looks like an origin of the rule, but `abstracted-from` cannot target
    `kb/types/`, so the phrase should say how the case bounds or illustrates the rule.
  level: warn
- scope: passage
  quotes:
  - source-of-truth for the byte-identical
  reason: The ADR 027 `evidenced-by` edge has the same problem. Its context phrase
    cites the ADR as the source of an instance and does not state a risked prediction
    or say that it qualifies or bounds the claim. If the ADR is the source of the
    instance and does not test the claim, use a label that fits that relation, such
    as `abstracted-from` (a permitted destination for reference), or reword the phrase
    to say how the ADR bounds the claim.
  level: warn
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/e87e58f9f9e42219a074f89e/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/e87e58f9f9e42219a074f89e/observation.json
contract-sha256: 9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0
raw-output: kb/reports/state/review/runs/v2/20261115T132933Z/calls/launches/ed5f576ca9a941fab90b636267b50cca/outputs/review.md
raw-output-sha256: a1bed12d7fe4b0a7c1396af503919f13cf835790bb90ae85f67753b18874459c
---

# Review

## Summary

The note follows the collection's main conventions, but its evidence handling breaks the contract's "Origin is not corroboration" rule.

## Conforming conventions

- **Placement:** after the named Commonplace cases are scoped, a substantive design-space claim remains. A derived copy of recomputable information must be machine-checked or absent, and the argument depends on how much each check costs. The tag-README mark, ADR 025 and ADR 027, the skill edits and the `AGENTS.md.template` copies are scoped as examples and are not the note's main contribution. The note therefore belongs in `kb/theory/`, not `kb/reference/`.
- **Explanatory-reach:** the note gives a mechanism, the asymmetry between a bounded recomputation and silent wrongness. It shows where the rule changes regime, from managed staleness under Level B checks to checked-or-absent under Level A checks. It also lists explicit preconditions and the conditions under which the rule fails. A reader can predict how the conclusion changes when the check cost changes.
- **Gaps:** the Open Questions section names real gaps without hedging.
- **Modality:** the note uses the default universal reading, which fits its "two valid states" framing.
- **Outbound links:** all targets are in permitted collections. No link goes into `kb/work/`, and the claim cites no sources, so it adds nothing to the unquoted-source limit. The `grounds`, `extends` and `contrasts` labels point to theory destinations, as the label table allows.

## Unmet convention

The contract treats a case that a universal claim was built from as its origin. Such a case is linked `abstracted-from` and does not corroborate the claim. An `evidenced-by` phrase must either name the risk that the claim took or say that the evidence qualifies or bounds the claim. The note's Instances section says that the spread of four Commonplace instances "shows it generalizes". Two footer `evidenced-by` edges present instances without naming a risked prediction. Neither edge says that its evidence qualifies or bounds the claim. These problems are local and do not undermine the theory claim, so the outcome is a warning rather than a failure.
