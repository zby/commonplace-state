---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The distinction also changes how contradiction should be interpreted.
  reason: 'The opening section ends on the contradiction paragraph. It carries two
    different loads: the note''s only positive account of fit (relational composition
    into an operative structure) and a separate thesis about how to repair a contradiction.
    Because it comes before the substitution rule, the opening ends on a secondary
    point and the crispest statement of the core claim is delayed. A revision could
    keep the relational-fit sentence and the point that poor fit does not license
    rejecting a warranted claim, present them as a consequence after the substitution
    section, and either cut the list of repair options or move it to a separate note
    on contradiction as a revision signal.'
- scope: document
  quotes: []
  reason: The Scope section mixes two kinds of bullet. Two guard against misreadings
    that the body already rules out (the broad warrant bullet repeats the opening
    definition; the statistical-independence bullet repeats the inform-not-substitute
    section and the title). Two add boundary content found nowhere else (fit has no
    scalar definition; objectives, commitments and authority grants affect belonging
    without truth tests). The reader must sort them. A revision could fold 'procedural'
    into the opening list of warrant kinds, fold a non-independence phrase into the
    first sentence of the inform-not-substitute section, and reduce Scope to the two
    bullets that add boundaries.
outcome: report
description: Retained report review of kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
target-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/synthesis/artifact/reviews/7abc91e7666ba7bfe709af42/inputs/target/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/synthesis/artifact/reviews/7abc91e7666ba7bfe709af42/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/synthesis
launch: 7e00a3ebc82b4363a0cfce697debe76c
completed-at: '2026-11-16T11:31:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/synthesis/calls/launches/7e00a3ebc82b4363a0cfce697debe76c/outputs/review.md
raw-output-sha256: 48fbe303fd2693d2415714d35c4593992733c6694fb187cc7b315189468abc2f
format: 2
---

# Simplification synthesis: A claim's warrant does not determine its fit in a working theory

The note states its core claim in the title and the first paragraph and argues both directions in turn. No check found the claim obscured. The compression findings fall into two clusters. One is the contradiction paragraph, which two checks flagged independently. The other is a Scope section in which defensive restatements sit beside real boundary conditions. The remaining local restatements are minor compression and are not listed: the closing sentence of the second paragraph and the closing sentence of the substitution section.

## Opportunities

### 1. Separate the relational account of fit from the theory of contradiction repair

- Location: opening section, last paragraph, from "The distinction also changes how contradiction should be interpreted." to "...not whether each claim passes its independent warrant test in isolation."
- Combines: branch-bloat (the paragraph is the note's one branch; the repair options are a separate thesis); core-claim-obscured (placing it before "The prohibition is substitution" delays the core rule).
- Preserve or decide: The sentence "Theory fit is therefore relational" is the only positive characterization of fit. The Scope section otherwise leaves fit deliberately undefined, so this sentence should survive in some form. The author must decide whether the repair options (a defect in another claim, a scope boundary, a bad decomposition, a larger theory needing revision) belong to this note's contribution or to a separate note. Cutting them is not neutral compression, because they support the point that poor fit does not license rejection. One possible resolution, offered only as an illustration: after the substitution section, add "Because fit is relational, a conflict between a warranted claim and the theory does not by itself identify the claim as the defect."

### 2. Fold the defensive Scope bullets into the body and keep only real boundaries

- Location: `## Scope`, the **Warrant** bullet and the final bullet ("The claim does not imply that warrant and fit are statistically independent...").
- Combines: marginal-value-redundancy (warrant-bullet finding; statistical-independence finding).
- Preserve or decide: Keep "procedural" as a kind of warrant. The bullet is the only place it appears. The non-independence point can move into the inform-not-substitute section, but its meaning must be preserved: the evaluations correlate and exchange evidence while neither determines the other. The bullet on objectives, commitments and grants of authority should stay a distinct boundary. Its relation to the two evaluations is unstated, though: it could be an input to fit, or a third consideration that is neither warrant nor fit. The author should settle that role before rewording the bullet. It should not be merged into the fit bullet as a compression edit.
