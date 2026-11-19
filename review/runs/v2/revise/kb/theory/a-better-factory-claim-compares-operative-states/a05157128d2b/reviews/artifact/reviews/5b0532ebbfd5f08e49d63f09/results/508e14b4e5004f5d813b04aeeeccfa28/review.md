---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - In a continuously revised system, the successor can instead be the operative state
    at a named measurement boundary, after one change or a period of development.
  reason: The note fixes the comparison requirements in advance but not the successor
    endpoint. If the measurement boundary may be named after development, an assessor
    can choose the operative state that happens to pass. That reopens the post-hoc
    selection the antecedence requirement is meant to block. Require the boundary,
    or the rule that selects it, to be part of the antecedent declaration.
- scope: passage
  quotes:
  - Prior declaration prevents that form of post-hoc selection.
  reason: 'This holds for one declaration taken alone. It does not hold for a factory
    that declares several comparisons, or redeclares after a failed comparison, and
    reports only the one that passes. The preregistration literature shows this: preregistration
    controls selection only when it is paired with a commitment to report every registered
    comparison. Either narrow the sentence to selection within one declaration, or
    add a requirement that declared comparisons be reported regardless of outcome.'
- scope: passage
  quotes:
  - is the factory state current when the comparison is declared.
  reason: Because the predecessor is indexed to the time of declaration, an assessor
    who chooses when to declare also chooses the baseline. For example, declaring
    just after a regression makes recovery count as improvement. The note should say
    whether the declaration time, and therefore the baseline, must itself be chosen
    independently of what the assessor expects.
- scope: passage
  quotes:
  - Antecedence guards this claim's auditability; it is not constitutive of improvement.
  reason: Secondary point. This concession turns the title's general claim about better-factory
    claims into a stipulation about one auditable subclass. The title and opening
    paragraph should make that subclass explicit, so that readers do not take the
    antecedent relation as a necessary condition on any claim that a factory improved.
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/critique-note.md
note-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/5b0532ebbfd5f08e49d63f09/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/5b0532ebbfd5f08e49d63f09/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 508e14b4e5004f5d813b04aeeeccfa28
completed-at: '2026-11-18T00:21:20Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/508e14b4e5004f5d813b04aeeeccfa28/outputs/review.md
raw-output-sha256: 3bddb5c4a958f5a8c604b5d12917398ddc499ce51fa2baf46d38b8e079d278d6
format: 2
---

# Critique: A better-factory claim compares operative states under an antecedent assessment relation

**Note:** kb/theory/a-better-factory-claim-compares-operative-states.md
**Central commitment:** An auditable claim that a factory got better compares the predecessor state with the installed operative successor. It uses an assessment relation, declared before development, that combines non-regression on the predecessor's prior capabilities with a declared improvement on at least one named dimension. Declaring that relation first blocks post-hoc selection of the requirements.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a practitioner from preregistration and research-integrity work, in the tradition of Simmons, Nelson and Simonsohn on researcher degrees of freedom and Gelman and Loken on the garden of forking paths. That opponent accepts the note's diagnosis: choosing dimensions and thresholds after seeing the result lets the successor satisfy whatever requirements were chosen. The opponent rejects the remedy as specified. In their view, fixing the *requirements* in advance does not by itself prevent post-hoc selection, because the claim has other free parameters that the note leaves open or opens itself:

1. **The successor endpoint.** The note says that in a continuously revised system "the successor can instead be the operative state at a named measurement boundary". It never says that the boundary must be named in advance. A factory under constant revision moves through many operative states. If the assessor picks the measurement point after seeing the trajectory, they can choose a passing state just as easily as they could choose a passing dimension. Both kinds of freedom have the same effect on selection.
2. **The baseline.** The predecessor is "the factory state current when the comparison is declared." If the assessor chooses when to declare, they choose the baseline. Declaring just after a known regression makes ordinary recovery count as improvement.
3. **The number of declarations.** One antecedent declaration is unbiased only if it is the only one. A factory that runs several declared comparisons, or redeclares after a failure, and reports the one that passes has engaged in post-hoc selection across declarations. Preregistration controls this only together with a commitment to report every registered comparison. The note contains no such commitment.

The opponent concludes that the sentence "Prior declaration prevents that form of post-hoc selection" claims more than the mechanism delivers. The note's main reason for requiring antecedence is that it makes the claim auditable and resistant to selection. Without fixing the endpoint and baseline and committing to report every declaration, that guarantee is incomplete in exactly the case the note calls typical, a continuously revised factory.

The author cannot answer this by pointing to the scope bullets. Those bullets admit that antecedence does not make the dimensions the *right* ones. This objection is different. It says that antecedence as specified does not deliver even the *selection-resistance* the note claims for it.

## How the note engages it

**Partially engaged.**

- The note specifies that the relation is "fixed before the development it judges" and is "declared while only the predecessor exists." This fixes the requirements but says nothing about the successor endpoint or the reporting obligation.
- The first Open Question asks "what the declared comparison must specify about the predecessor's baseline, measurement procedures and comparable conditions." That is the right place for the gap. But it treats baseline and measurement specification as open matters of content. It does not recognize them as further degrees of freedom that can undermine the selection-resistance the note has already asserted.
- The note does well to separate auditability from improvement itself ("Antecedence guards this claim's auditability; it is not constitutive of improvement") and to admit that properly declared dimensions may measure the wrong thing. Those concessions answer the Goodhart and validity objection, which is the obvious alternative attack. They do not answer the selection-leakage objection.
- The note's own text creates the endpoint freedom ("a named measurement boundary") without tying it to the antecedent declaration.

So the claim "relation-relative and auditable" survives in substance, and the operative-state relata stand. The non-regression-plus-target structure also stands, and the note correctly bounds it as one declarable shape among others. What the attack defeats is the unqualified statement that prior declaration of the requirements prevents post-hoc selection.

## Constructive findings

- Make the measurement boundary part of the antecedent declaration: either a named point or a rule that fixes which operative state counts as the successor. Otherwise, state that a boundary chosen after development leaves the claim open to endpoint selection.
- Narrow "Prior declaration prevents that form of post-hoc selection" to selection *within a single declaration*. Alternatively, add the condition that full auditability needs: every declared comparison is reported whatever its outcome, and redeclaration after a failure counts as a new comparison, not a replacement.
- In the definition of the predecessor, or in the first Open Question, note that the declaration time sets the baseline. The baseline is therefore one of the degrees of freedom the antecedent declaration has to constrain, not just a matter of measurement content.

## Secondary objections (optional)

- **Stipulative title.** The third scope bullet admits that a retrospective criterion supplied independently can ground a legitimate improvement claim. The title still says "A better-factory claim compares operative states under an antecedent assessment relation" without qualification. The opening paragraph's "Throughout, *better* means better under the declared relation" signals the restriction, but the title and description read as a claim about better-factory claims in general. Qualifying the title, for example as an *auditable* better-factory claim, would match it to the scope the note defends.
- **Prior-capability scope.** Non-regression is measured against "the predecessor's prior capabilities." For an open production family, that scope may not be enumerable. The second Open Question already flags this, so it is noted here only as a residual risk: without an enumerable scope, the non-regression part of the relation may in practice reduce to whatever regression suite happens to exist.
- **Leftover TODO.** The line "TODO! remove or update to use software house instead of software factory" is still in the body. That is an editorial issue, not an objection to the claim, but it signals that the note's core term may change.
