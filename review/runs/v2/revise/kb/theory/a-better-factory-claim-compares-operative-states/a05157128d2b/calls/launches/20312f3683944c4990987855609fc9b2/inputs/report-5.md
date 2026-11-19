---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/role
launch: de51d2a25c1f4f39b1609f172d0f7b98
completed-at: '2026-11-18T00:27:57Z'
findings:
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/tags/software-factory-README.md — needs only a citation with
    a gloss: what an improvement claim compares and that the relation is fixed in
    advance. The title, the opening paragraph and the section ''The assessment relation
    is antecedent and scope-indexed'' carry both points.'
- scope: passage
  quotes:
  - If the checked prior scope includes an operative path for [factory development](./definitions/factory-development.md),
    non-regression requires the successor to preserve that capability
  reason: SUPPLIED — kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
    — presents itself as a supplement to 'the preserved-capability consequence' of
    the comparison, so it needs the premise that non-regression preserves a factory-development
    path only when that path is inside the checked scope. The note states that consequence
    with the same scope condition.
- scope: document
  quotes: []
  reason: DUPLICATED — kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
    — the dependent's description ('fails a non-regression requirement only when the
    revision capability is included in the checked scope') restates the note's preserved-path
    paragraph, which the note itself repeats in its last Scope bullet ('Preserving
    factory development follows only when that capability is included in the checked
    scope'). The dependent is the dedicated treatment; only its description and one
    sentence are visible, so which states it better cannot be judged beyond that the
    dependent makes the closing-path case its subject while the note states it as
    a conditional consequence.
- scope: passage
  quotes:
  - The claim compares two operative states of the factory under an assessment relation
    fixed before the development it judges.
  reason: 'SUPPLIED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md
    — needs the measurement discipline for the improvement half of the learning claim:
    the relata and an antecedent relation. The note supplies both, and its Scope bullet
    that antecedence ''is not constitutive of improvement'' fits the dependent''s
    point that improvement can be a fact of the trajectory before anyone verifies
    it.'
- scope: passage
  quotes:
  - 'Retention has no quality requirement: a retained change can degrade the factory
    as easily as improve it.'
  reason: DUPLICATED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md
    — the dependent already states that a retained change can degrade later production
    and that learning additionally requires improvement relative to a declared objective.
    The note restates this in its opening and again in the section 'Improvement, retention
    and learning are different claims'. The dependent states the definition better,
    since it owns the learning concept; the note's three hypothetical cases are more
    concrete, but the dependent cites the note only for the measurement discipline,
    not for that distinction.
- scope: passage
  quotes:
  - A comparison judges the adopted states. Whether an evaluator also controlled adoption
    is a separate causal question; a description cannot change whether its judgment
    was required for installation.
  reason: PARTLY SUPPLIED — kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
    — glosses the note as 'the comparison of a system before and after an adopted
    change' and needs the claim that a judgment that the system improved does not
    by itself show whether human evaluation was required to operate it. The note separates
    the comparison from whether an evaluator's judgment was required for adoption
    or installation; it says nothing about evaluation required to operate the system,
    which is the dependent's sense.
contract: report
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/role/artifact/reviews/5f6632528c4397f346057d59/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/role/artifact/reviews/5f6632528c4397f346057d59/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/role/calls/launches/de51d2a25c1f4f39b1609f172d0f7b98/outputs/review.md
raw-output-sha256: 432fc74b4edc4505cd4e585143fb19cbe4d7873727436586220563723910fbaf
---

# Role in the KB: better-factory claim comparing operative states

## Role
The note is the measurement discipline for the improvement half of factory learning: it says that a better-factory claim compares a predecessor with an installed (operative) successor under non-regression and target requirements declared in advance. The learning definition sends its "did it improve" question here, a supplement argues from its preserved-capability consequence, and a note on approval waits uses it as the before/after comparison that leaves the evaluation question open. The tag head cites it as a member with a short gloss.
Relied on: the operative-state relata (predecessor, operative successor), the antecedent assessment relation, non-regression over a declared scope, the conditional preservation of a factory-development path, and the separation of the comparison from causal questions about adoption. Unused: the candidate/staging-comparison distinction, the deployed-system paragraph on which machinery the compared states include, the three hypothetical cases and the with/without-instruction contrast, the "declared amount" improvement threshold, the retrospective-criterion and retirement-permitting Scope bullets, the generalization to other systems, and both Open Questions.

## Dependents
- `kb/tags/software-factory-README.md` — citation with gloss of what is compared and that the relation is fixed in advance.
- `kb/theory/an-improvement-can-close-the-path-to-further-improvement.md` — premise: the preserved-capability consequence of non-regression under a checked scope.
- `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md` — premise: relata and antecedent relation for establishing the improvement half of learning.
- `kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md` — distinction: an improvement judgment does not settle whether human evaluation was required to operate the system.

## Duplication
- The preserved-path consequence appears twice in the note (body paragraph and last Scope bullet) and is the subject of `kb/theory/an-improvement-can-close-the-path-to-further-improvement.md`, whose description restates the same scope condition.
- The retention-versus-learning distinction in the note's opening and its section "Improvement, retention and learning are different claims" restates what `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md` already defines; the dependent owns the definition, the note adds worked cases.

## Untaken recommendations
None. No linking passage recommends a change to the note. The inline TODO about "software house" is in the note itself, not in a linking source.

## Reach
- The title and the claim that the comparison relates two operative states under an antecedent relation reach `kb/tags/software-factory-README.md` and `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md`; the latter also relies on antecedence not being constitutive of improvement.
- Non-regression over a declared scope and the conditional preservation of a factory-development path reach `kb/theory/an-improvement-can-close-the-path-to-further-improvement.md`.
- The terms predecessor/adopted successor and the Scope bullet separating the comparison from whether an evaluator controlled adoption reach `kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md`.
- Renaming "software factory" per the note's TODO would reach the tag head (`kb/tags/software-factory-README.md`), the factory-learning note and the closing-path supplement, all of which use factory vocabulary.
- Changes to the candidate/staging distinction, the deployed-system paragraph, the three hypothetical cases, the retrospective-criterion and retirement Scope bullets, the generalization bullet and the Open Questions reach no dependent.
