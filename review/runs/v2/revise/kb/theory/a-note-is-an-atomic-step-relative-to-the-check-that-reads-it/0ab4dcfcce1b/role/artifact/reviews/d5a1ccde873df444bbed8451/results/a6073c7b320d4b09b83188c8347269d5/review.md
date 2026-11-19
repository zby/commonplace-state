---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md
    — rests on the note for three things: the artifact-side placement of the grounding
    bound, the unquoted source as the grounding check''s unit, and what kind of number
    N is. The note supplies each in its own section (''Placing the bound on the artifact
    rather than the review'', ''Mechanism: for the grounding check, the unit is the
    unquoted source'', ''What kind of number a step size is''), so no single span
    carries the need. The note leaves N, the validator rule and the review-side budget''s
    fate undecided, which leaves the ADR''s decision of five sources and a FAIL rule
    to the ADR.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md
    — the same three needs as ADR 082 (artifact-side placement, unquoted source as
    unit, kind of number N), supplied by the same three sections. The proposal's description
    also exempts validated inline quotes and note links; the note supplies both exemptions
    (the verbatim-quote mechanism and the paragraph on links to other notes).
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md
    — its ''extends'' edge needs the artifact-side bound and its source-counting unit,
    and its body passage asserts that the note depends on the link exemption. The
    note supplies the bound and the unit across its placement and mechanism sections,
    and confirms the dependence both inline (''Links to other notes are also not sources
    in this sense'') and in its footer (''grounds: the premise that links to other
    notes are not sources for the grounding step'').'
- scope: passage
  quotes:
  - Across 344 notes in `kb/notes/` as of 2026-08-27, eight cite more than five distinct
    sources
  reason: 'DUPLICATED — kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md
    — both state the same corpus count (344 notes, eight citing more than five sources).
    The dependent pairs it with the artifact count (median offer of seven across 337
    targets), which is the comparison its argument needs: it shows why the unit counted
    decides whether a bound of five is affordable. The note uses the count for a different
    purpose: to show that the eight are single-claim notes that still fail the checking
    bound. For the dependent''s use, the dependent''s version is the better one; the
    note''s version adds the single-claim characterization, which the dependent does
    not use.'
- scope: passage
  quotes:
  - These are different quantities set by different mechanisms, and a note can satisfy
    one and fail the other.
  reason: SUPPLIED — kb/theory/short-composable-notes-maximize-combinatorial-discovery.md
    — its 'contrasts' edge needs a second, independent size bound (one checkable inference
    sized to the checker's pass) that a single-claim note over many sources can fail.
    The note states the independence here and supplies the single-claim, many-source
    case in 'The two bounds come apart in the corpus'.
- scope: passage
  quotes:
  - One checkable inference, sized to the checker's pass.
  reason: 'SUPPLIED — kb/tags/review-system-README.md — citation-level need: a one-line
    gloss that the note sizes a note to one inference a reviewer can check in a single
    pass. The note''s statement of the checking bound matches the gloss.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/instructions/review-gates/complexity/claim-to-section-ratio.md
    — rests on the premise that a note is bounded by one claim the reader can hold
    and one inference the checker can verify. The note states both bounds in its opening
    ('One claim per note, sized to the reader's context' and 'One checkable inference,
    sized to the checker's pass'), though it attributes the first to the short-composable-notes
    note and argues only the second. The gate's own use (sections that restate rather
    than extend) is not something the note addresses; the gate needs only the premise.
- scope: document
  quotes: []
  reason: 'PARTLY SUPPLIED — kb/instructions/simplification-passes/split-out-a-treatment.md
    — rests on the claim that ''the retained treatment is sized for a reader''s check,
    not for the artifact''s reader''. The note supplies a distinction between sizing
    to a checker''s pass and sizing to a reader''s context, but only for notes under
    Commonplace''s grounding check; it says nothing about retained treatments or split-out
    arguments. The dependent''s wording also crosses the note''s terms: in the note
    the reader sets the co-loading bound and the checker sets the checking bound,
    and both bounds apply to the same note. ''A reader''s check'' set against ''the
    artifact''s reader'' is not a distinction the note draws. The nearest material,
    that a split ''has to be by claim, so that each fragment states what it establishes'',
    is about splitting jointly supported claims, not about where a full treatment
    is kept.'
- scope: document
  quotes: []
  reason: 'PARTLY SUPPLIED — kb/sources/an-assumption-based-tms.ingest.md — needs
    a comparison basis: ''checker-relative source dependencies'' that, like ATMS assumption
    environments, ''make a conclusion''s usable support conditions inspectable''.
    The note supplies checker-relative atomicity (''a step is atomic relative to a
    particular check'') and the unquoted source as the grounding check''s unit, and
    it argues auditability (''can be re-checked from the same page''). It does not
    frame sources as the dependencies of a conclusion, and it neither mentions ATMS
    nor makes the comparison the ingest describes.'
outcome: report
description: Retained report review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/role/artifact/reviews/d5a1ccde873df444bbed8451/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/role/artifact/reviews/d5a1ccde873df444bbed8451/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/role
launch: a6073c7b320d4b09b83188c8347269d5
completed-at: '2026-11-16T22:43:33Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/role/calls/launches/a6073c7b320d4b09b83188c8347269d5/outputs/review.md
raw-output-sha256: 36681dbc8bd2d3b0eb4b60caf6c6b8dd683b07b303487cc07f958254033bc4cb
format: 2
---

# Role in the KB: A note is an atomic step relative to the check that reads it

## Role
The note is the theory premise behind Commonplace's artifact-side grounding bound. ADR 082 and its archived proposal rest on it for the artifact-side placement, the unquoted source as the grounding check's unit, and the kind of number N is. A second group of dependents (the short-composable-notes note, two instructions and the review-system tag head) cite it for a separate size bound, one checkable inference sized to the checker's pass, which is independent of the co-loading bound. The linked-note-grounding note and this note depend on each other: the exemption for linked notes makes the source-counting unit affordable.
Relied on: the "atomic step" term and checker-relative atomicity; the two independent bounds (co-loading and checking); artifact-side placement of the bound; the unquoted source as the grounding check's unit, with validated quotes and linked notes exempt; N as an auditability convention rather than a capacity limit; the 344/eight corpus count (restated by a dependent). Unused: the silent-failure argument against review-side budgets (used only as part of "placement"); the occurrence-versus-representativeness limit and the `(snapshot required)` route; the joint-support "quote rather than split" consequence; the rereading of the five-link-cap experiment; the Descartes and Lamport precedents; both Open Questions.

## Dependents
- `kb/reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md`: placement, unit and the kind of number N.
- `kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md`: the same three needs as the ADR.
- `kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`: the artifact-side bound and its source-counting unit; it also asserts that the note depends on the exemption.
- `kb/theory/short-composable-notes-maximize-combinatorial-discovery.md`: the second, independent size bound and the case of a single-claim note over many sources.
- `kb/tags/review-system-README.md`: a one-line gloss only.
- `kb/instructions/review-gates/complexity/claim-to-section-ratio.md`: the one-claim, one-inference premise.
- `kb/instructions/simplification-passes/split-out-a-treatment.md`: sizing to a check rather than to a reader, applied to retained treatments.
- `kb/sources/an-assumption-based-tms.ingest.md`: checker-relative source dependencies as a basis for comparison with ATMS.

## Duplication
- The corpus count (344 notes, eight citing more than five sources) appears in both this note and `kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`. The dependent's version serves its unit argument better because it pairs the count with the artifact-count median; the note's version is the one that characterizes the eight as single-claim notes.
- The note summarizes the claims of the short-composable-notes note (the co-loading bound) and the linked-note-grounding note (the link exemption), each with a link. The supplied passages from those dependents are footer edges and a context paragraph, so they show no restatement of this note beyond the count above.

## Untaken recommendations
None in the supplied passages. The ATMS ingest's passage presents the paper as "a technical basis for comparing" ATMS assumption dependencies with this note's checker-relative source dependencies. The note does not make that comparison, but the passage is a statement of relevance, not a recommended action. Only the passages that link to the note were supplied, so any recommended next action elsewhere in that ingest is unseen.

## Reach
- **Artifact-side placement, the unquoted source as the unit, the link and verbatim-quote exemptions, and the kind of number N** reach ADR 082 and the archived proposal. The placement and the unit also reach `kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`, which states that the note depends on the link exemption.
- **The two independent bounds, and "atomic step" as one checkable inference sized to the checker's pass**, reach `kb/theory/short-composable-notes-maximize-combinatorial-discovery.md`, `kb/instructions/review-gates/complexity/claim-to-section-ratio.md`, `kb/instructions/simplification-passes/split-out-a-treatment.md` and `kb/tags/review-system-README.md`.
- **Checker-relative atomicity and the auditability argument** reach `kb/sources/an-assumption-based-tms.ingest.md`, but only as a comparison basis.
- **The corpus count** is shared with `kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`, so a change to the count meets that dependent's copy.
- **The review-side budget's status**: the note calls ADR 079's review-side budget "currently in force" and leaves its fate undecided. The supplied description of ADR 082, an accepted decision that rests on this note, says the link-following review criteria drop their reader-side caps. A change to how the note describes the review-side budget would reach ADR 082.
- No dependent uses any of the following, so a change to them reaches no one: the silent-failure argument in detail, the occurrence-versus-representativeness limit, the snapshot-required route, the joint-support consequence, the rereading of the five-link-cap experiment, the Descartes and Lamport precedents, and the Open Questions.
