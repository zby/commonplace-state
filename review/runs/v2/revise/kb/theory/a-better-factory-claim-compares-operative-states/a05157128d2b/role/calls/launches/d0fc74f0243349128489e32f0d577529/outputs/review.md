---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/tags/software-factory-README.md — needs only a citation glossed as 'what an improvement claim compares, and that the relation is fixed in advance'; the note's sections on operative-state relata and the antecedent, scope-indexed relation supply both halves of the gloss."
  - scope: passage
    quotes: ["If the checked prior scope includes an operative path for [factory development](./definitions/factory-development.md), non-regression requires the successor to preserve that capability: a production gain alone does not show that the system can still produce another revision."]
    reason: "SUPPLIED — kb/theory/an-improvement-can-close-the-path-to-further-improvement.md — presents itself as a supplement to 'the preserved-capability consequence' of the comparison; the note states that consequence, conditional on the revision capability being in the checked scope, matching the dependent's description."
  - scope: passage
    quotes: ["Preserving factory development follows only when that capability is included in the checked scope."]
    reason: "DUPLICATED — kb/theory/an-improvement-can-close-the-path-to-further-improvement.md — the dependent's description ('fails a non-regression requirement only when the revision capability is included in the checked scope') restates the condition the note gives twice (in the factory-development paragraph and in this Scope bullet). The supplied passage shows only the supplement line, so which states it better cannot be judged beyond this: the note states the condition as a consequence of its relation; the dependent is the dedicated treatment."
  - scope: document
    quotes: []
    reason: "PARTLY SUPPLIED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md — needs the comparison to discipline 'the improvement half of the learning claim', i.e. establishing that a change 'improved the factory relative to a declared objective', with relata and an antecedent relation. The note supplies the relata (predecessor, operative successor) and the antecedent relation, but it frames improvement as 'better under the declared relation' and says 'A change that improves the factory against another objective need not pass this comparison'; it does not state how its assessment relation relates to the dependent's declared objective, so the bridge from the objective the definition is indexed to and the relation the comparison checks is left implicit."
  - scope: passage
    quotes: ["Retention has no quality requirement: a retained change can degrade the factory as easily as improve it."]
    reason: "DUPLICATED — kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md — the dependent's passage already states that a retained change can degrade later production, establishing retention but not learning. The note restates it as its motivation, and its 'Improvement, retention and learning are different claims' section restates the same distinction with three hypothetical cases. The dependent states the definitional point better for dependents, since it owns the definition; the note's cases add worked separation the dependent's passage does not contain."
  - scope: passage
    quotes: ["A comparison judges the adopted states. Whether an evaluator also controlled adoption is a separate causal question; a description cannot change whether its judgment was required for installation."]
    reason: "PARTLY SUPPLIED — kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md — needs the claim that a judgment that the system improved 'does not by itself show whether human evaluation was required to operate it'. The note supplies the before/after comparison of adopted states and separates the comparison's judgment from an evaluator's causal role, but it frames that role as controlling adoption or installation, not as evaluation required to operate the system, and the note is framed around software factories while the dependent applies it to 'a system' generally (the last Scope bullet licenses only the operative-state and relation apparatus for other systems)."
outcome: report
---

# Role in the KB: A better-factory claim compares operative states under an antecedent assessment relation

## Role
The note is the KB's account of what a factory-improvement claim compares: the predecessor and the installed, operative successor, judged under a relation declared before development. The factory-learning definition cites it as the discipline for the improvement half of learning, one theory note extends its preserved-capability consequence, another cites its separation of the comparison's judgment from an evaluator's causal role, and the software-factory tag head lists it.
Relied on: operative-state relata (predecessor, operative successor); the antecedent assessment relation; non-regression on the predecessor's prior scope; the preserved factory-development path, conditional on the checked scope; the separation of retention, improvement and learning; the comparison judging adopted states, not the evaluator's role in adoption. Unused: the term "candidate"; the deployed-system-as-unit paragraph; the "improve by a declared amount" component; the three hypothetical cases and the experiment-contrast test; the retrospective-criterion and retirement-relation scope bullets; the open questions.

## Dependents
- `kb/tags/software-factory-README.md` — a citation glossing what the claim compares and that the relation is fixed in advance.
- `kb/theory/an-improvement-can-close-the-path-to-further-improvement.md` — the preserved-capability consequence it supplements.
- `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md` — the relata and antecedent relation that discipline establishing improvement relative to a declared objective; also a reciprocal "extends" footer link.
- `kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md` — the before/after comparison of an adopted change and the claim that an improvement judgment does not show whether human evaluation was required.

## Duplication
- With `factory-learning-is-experience-responsive-retention-that-improves.md`: the note's opening ("Retention has no quality requirement…") and its retention/improvement/learning section restate the dependent's point that retention can degrade the factory and so is not learning. The dependent owns the definition; the note adds worked cases.
- With `an-improvement-can-close-the-path-to-further-improvement.md`: the dependent's description restates the note's condition that non-regression preserves revision capability only when that capability is in the checked scope, which the note itself states twice.

## Untaken recommendations
None. No linking passage recommends a change to the note.

## Reach
- The antecedent assessment relation and the operative-state relata reach `factory-learning-is-experience-responsive-retention-that-improves.md` (whose measurement problem is disciplined by them) and the gloss in `kb/tags/software-factory-README.md`.
- The non-regression scope and preserved factory-development consequence reach `an-improvement-can-close-the-path-to-further-improvement.md`.
- The framing of "better" relative to the declared relation, and its relation to an "objective", reaches `factory-learning-is-experience-responsive-retention-that-improves.md`.
- The Scope bullet separating the comparison's judgment of adopted states from an evaluator's control of adoption reaches `removing-approval-waits-can-leave-required-human-evaluation-in-place.md`.
- The term "software factory" (the note carries a TODO about replacing it with "software house") reaches the tag head's gloss and the factory-learning dependent, which use factory vocabulary.
- Changes to the candidate term, the deployed-system paragraph, the declared-amount component, the three cases, the experiment-contrast paragraph, the retrospective-criterion and retirement-relation bullets, and the open questions reach no dependent visible in the supplied passages.
