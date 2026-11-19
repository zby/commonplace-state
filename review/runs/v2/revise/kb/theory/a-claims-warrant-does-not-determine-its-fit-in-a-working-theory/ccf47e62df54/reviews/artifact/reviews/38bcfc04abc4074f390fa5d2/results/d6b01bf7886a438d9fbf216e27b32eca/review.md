---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Theory fit is therefore relational: it concerns how warranted claims compose
    into an operative explanatory structure'
  reason: 'DOUBTFUL — (universal, stated) Fit is a property that unwarranted claims
    can also have, so fit and warrant vary separately in both directions. — The note''s
    own characterisation of fit says it ''concerns how warranted claims compose'',
    which makes warrant part of what proper fit is. On that reading, fit proper entails
    warrant, and the reverse direction of the commitment (''neither evaluation determines
    the other''; the description''s ''apparent fit may be produced by an unwarranted
    ... claim'') survives only for ''apparent'' fit. Paragraph 3 says only ''Apparent
    fit does not imply warrant'', which signals this slippage. The title''s direction
    (warrant does not determine fit) is unaffected. — LOCAL: fix it by restating line
    16 without ''warranted'', or by narrowing the symmetric claim in Scope to apparent
    or operational fit. — instance'
- scope: passage
  quotes:
  - claims in the knowledge base may be empirical, formal, source-derived, or procedural
  reason: 'DOUBTFUL — (unstated, universal) Every claim kind has a warrant standard
    that can be assessed independently of the working theory and the system that uses
    it. — Procedural claims are the counterexample, and the note puts them in scope.
    Take a procedure or prompt instruction that is claimed to produce an outcome.
    Often the only available warrant is that it produced the outcome when run inside
    this system. That is the same evidence as its fit (''helped the system'', ''guide
    recovery''). Here the evidence for one question does settle the other, or the
    two can no longer be told apart. Formal claims derived inside the theory''s own
    axioms likewise get their validity from the theory. — LOCAL: limit the commitment
    to claims whose warrant has a standard external to the system, or say how procedural
    warrant stays separate from use-based fit evidence. — instance'
- scope: passage
  quotes:
  - use a scope that does not match the decisions the theory must guide
  reason: 'DOUBTFUL — (universal, stated) Each listed way a warranted claim can fit
    poorly is a fit failure and not a warrant failure. — Scope mismatch mis-sorts.
    If a claim is warranted only over scope S and the theory uses it to guide decisions
    outside S, the claim as applied is unwarranted. That is a warrant failure in use,
    not a fit failure of a warranted claim. The other listed items (irrelevance, duplication,
    maintenance cost without changed inference) do not have this problem. — LOCAL:
    drop this item, or recast it as a scope that is narrower than the decisions require,
    which is a usefulness gap and not an over-application. — instance'
- scope: passage
  quotes:
  - A claim used in a working theory faces at least two different evaluations.
  reason: HOLDS — (universal) Warrant and fit ask different questions with different
    failure conditions. — A hunt for a collapse found none. Even coherentist accounts,
    where coherence contributes to justification, keep separate the question of whether
    a claim should be retained in this particular theory, given its purpose, redundancy
    and maintenance cost. The KB's Popperian stance rejects coherence as warrant in
    any case.
- scope: passage
  quotes:
  - A warranted claim may fit poorly.
  reason: 'HOLDS — (existential) Some warranted claims fit poorly. — One checkable
    case is enough: an exact duplicate of a claim that is already present and well
    supported is fully warranted and adds nothing. A hunt for a theory whose fit criterion
    is just ''every warranted in-scope claim'' (an exhaustive catalogue) still fails
    on duplication.'
- scope: passage
  quotes:
  - Apparent fit does not imply warrant either.
  reason: HOLDS — (existential) Some unwarranted claims integrate smoothly because
    neighbouring claims or the implementation already assume them. — Historical cases
    such as epicycles accommodating observations, and codebases built around a mistaken
    convention, confirm it. No defeater was found at this modality. The separate problem
    with 'apparent' versus proper fit is the first finding.
- scope: passage
  quotes:
  - The prohibition is substitution.
  reason: HOLDS — (universal) Evidence may pass between the two evaluations without
    one replacing the other. — A hunt was made for a case where fit evidence must
    count as warrant, such as corroboration through surviving demanding tests. In
    that case the evidence still informs warrant without settling it, because surviving
    tests is defeasible. That matches the note's 'inform but not substitute'.
outcome: report
description: Retained report review of kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/38bcfc04abc4074f390fa5d2/inputs/target/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/38bcfc04abc4074f390fa5d2/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews
launch: d6b01bf7886a438d9fbf216e27b32eca
completed-at: '2026-11-16T11:30:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/calls/launches/d6b01bf7886a438d9fbf216e27b32eca/outputs/review.md
raw-output-sha256: 781f21188637475fb9dc6fa5f01e9d80743dddb25806834b64db37fe31ec0c6d
format: 2
---

# Premise decomposition: A claim's warrant does not determine its fit in a working theory

**Register:** claim
**Central commitment (one sentence):** Whether a claim is warranted and whether it fits a working theory are distinct evaluations, and evidence settling one does not settle the other, though each may inform the other.

## Premises and counterexamples

The commitment has a stated core and two directions. The core says there are two separable evaluations. The first direction is warrant ⇏ fit: a warranted claim can fit poorly. The second is fit ⇏ warrant: a claim can fit without being warranted. The section on informing without substituting adds that evidence may pass between them without settling either. Each part is an existence or separation claim, so one checkable case either way decides it. The stated existence premises hold easily.

The weak points are two unstated background premises. The first is that fit is defined independently of warrant. The note undercuts this itself when it describes fit as composing *warranted* claims. That makes the fit ⇏ warrant direction depend on the word "apparent". The second is that every in-scope claim kind has a warrant standard independent of the theory. Procedural claims, which the Scope section includes, often get their warrant only from use inside the system, and that is fit evidence. One listed fit failure, scope mismatch, is also mis-sorted. Each of these failures can be repaired with a qualification. None reaches the title's direction.

## For the human

Look first at line 16, "how warranted claims compose". If proper fit presupposes warrant, the symmetric "neither determines the other" holds only for apparent fit, so pick one reading and state it in Scope.
