---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - claims in the knowledge base may be empirical, formal, source-derived, or procedural
  reason: The title and opening frame the claim for any working theory, but the scope
    bullet justifies the broad sense of warrant by reference to 'the knowledge base',
    a definite article pointing to a narrower domain that the note never introduces.
    A reader outside this KB cannot tell whether the broad sense of warrant applies
    only there. Generalize to 'claims in a working theory may be...' or mark the KB
    explicitly as the motivating case.
  level: warn
- scope: passage
  quotes:
  - This claim helped the system
  reason: '''The system'' is a definite reference to an operating system around the
    theory that the opening does not establish; the general framing speaks of a working
    theory, not a system using it. The phrase reads as residue from the self-improving-system
    setting. Low impact because the sentence is clearly an illustrative quoted inference;
    ''This claim helped the system that uses the theory'' or similar would remove
    the gap.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 971c8f5432f48a0220ce73b0af03ebf07d41624a648304f63b01ede1bf00a723
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/d6d4622b517db638dd9740b4/inputs/target/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/d6d4622b517db638dd9740b4/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews
launch: 02c36456a8c441219c2924d4496636b6
completed-at: '2026-11-16T11:27:55Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/calls/launches/02c36456a8c441219c2924d4496636b6/outputs/review-source-residue.md
raw-output-sha256: 623f96f29a729984a593a3c3d78c0db7ecf2a1ac2f39a8c529c5ef260d4cf3f2
format: 2
---

# Review

The title and opening paragraph claim generality over any claim used in a working theory. Most of the body keeps that generality: its examples (duplication, wrong abstraction level, mismatched scope, assumption by neighboring claims) apply to working theories in general.

Two phrases carry a narrower setting without framing it. The scope bullet grounds the broad sense of warrant in "the knowledge base", which ties a definitional choice to this KB rather than to working theories. The quoted inference "This claim helped the system" presupposes a system operating the theory, which fits the self-improving-system context the note is tagged for but is not set up in the opening. The first is a warn because it shapes how the key term is scoped; the second is informational.
