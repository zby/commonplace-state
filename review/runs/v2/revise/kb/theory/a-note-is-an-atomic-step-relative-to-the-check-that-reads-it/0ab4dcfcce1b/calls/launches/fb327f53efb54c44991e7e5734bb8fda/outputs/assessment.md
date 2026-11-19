# Assessment: A note is an atomic step relative to the check that reads it

**Proposed purpose (operator named none):** Agents and maintainers who design or
operate Commonplace's grounding review should understand that a note's step size
is relative to the check that reads it, what the grounding check's cost unit is,
and why the bound is placed on the artifact, with the limits of that placement
stated where the claims are made.

**Decision: stop.** The highest-value changes are claim corrections, not text
passes. Three claims are wrong or unsupported as stated, and one of them is the
unit that ADR 082, its archived proposal and the linked-note-grounding note rely
on. The passes do not change claims, so none is recommended.

## What reads well

The opening separation of the co-loading bound from the checking bound, and the
check-relativity of atomicity, are clear, well linked and held by every depth 1
report (premise decomposition: HOLDS on both).

## Ranked changes (highest value against the purpose first)

1. **Restate the cost unit from "the unquoted source" to the unquoted
   attribution** (Mechanism section, description, Scope). Premise decomposition
   marks "A source that has been quoted verbatim is not one of them" DEFEATED:
   a partly quoted source with further unquoted attributions still has to be
   opened, and the linked paired assay records exactly that case (the
   HyperAgents FAIL). Cost: a claim change touching the unit dependents rely on.
   Pass: none — rewrite route.
2. **Correct "an absence of that kind is a validator's result rather than a
   reviewer's finding"** (experiment section). The ADR 046 validator matches
   quotes that exist; it cannot detect a missing quote. Flagged by composition
   friction (UNSUPPORTED), critique, premise decomposition, epistemic-status-blur,
   grounding-alignment and framing-mismatch. Either name a required-quote rule
   as a premise or restate the absence as a reviewer finding the bound makes
   cheaper. Cost: claim change. Pass: none — rewrite route.
3. **Qualify "An artifact-side bound does not have that failure mode … on a
   conforming note it never binds"** (placement section). The silent failure
   moves to the author's choice of passage, to linked-note representation and
   to inference labelling; the note concedes some of this later but not here.
   Critique, friction and premise decomposition all attack it. Cost: claim
   narrowing on a passage ADR 082 relies on for placement. Pass: narrow-overclaims
   would fit the wording, but the narrowing changes the placement argument
   dependents use, so it goes to the operator.
4. **Account for all four cap-only findings in the experiment rereading.** Two
   (linked-note representation; unmarked hypotheses) fall outside the proposed
   unit; the note recruits only two and says "the four notes would have had to
   split or quote". Cost: evidence reinterpretation. Pass: none — rewrite route.
5. **Weaken "no observed loss … not a reviewer capacity exhausted"**. The assay
   had no ground truth for misses in PASS outcomes and the linked report
   declines that conclusion (grounding-alignment, epistemic-status-blur, premise
   decomposition). Cost: two-sentence narrowing. Pass: narrow-overclaims, but
   held with the rest of the rewrite.
6. **Specify the corpus count's population and unit** ("eight cite more than
   five distinct sources"): distinct sources vs unquoted sources, and `kb/notes/`
   vs the note's own `kb/theory/` location; no method or link. Cost: evidence
   restatement; the count is duplicated in the linked-note-grounding note.
   Pass: none — claim question.
7. Text-level work that would follow a rewrite: compress the Descartes/Lamport
   precedent section (detail-overhang, synthesis opportunity 1; the Descartes
   gloss also sizes parts to the solution, not the checker); surface the
   bound coupling and soften "nothing to do with each other" (synthesis 2,
   internal-consistency); place auditability in the placement argument
   (synthesis 3); define N and gloss "ingest" and "snapshot"; split the packed
   oracle-domain sentence and the archived-proposal appositive; fix "the one it
   cannot", "which is the behaviour…", "prices already paid elsewhere"; the
   title/body alignment ("Whether a note is an atomic step depends on…").
   Pass: abstractions, readability-and-flow, plain-wording, opening-and-title,
   fix-strategy-taxonomy. Not recommended now: a rewrite will replace much of
   this text.

## Sentence a hostile reviewer attacks first

"Both are absences of a retained passage, and an absence of that kind is a
validator's result rather than a reviewer's finding." It asserts a capability
the cited validator lacks, and the section's reinterpretation of the experiment
rests on it.

## Overclaim candidates: support or divergence

- "A step is atomic relative to a particular check" — divergence (keep).
- "These are different quantities set by different mechanisms, and a note can
  satisfy one and fail the other." — divergence (keep).
- "N is a convention, chosen so that a second checker — including a person —
  can redo the step." — divergence (keep; premise decomposition HOLDS; friction
  calls the elimination over three candidates thin, which may be narrowed).
- "An artifact-side bound does not have that failure mode" — support (narrow).
- "an absence of that kind is a validator's result" — support (correct).
- "on this evidence it is not a reviewer capacity exhausted" — support (narrow).
- "under such a bound the four notes would have had to split or quote" —
  support (narrow to the two source-retention findings).

## Stale qualifications (claim questions for the operator)

- Scope says the note "Does not decide N, a validator rule that would enforce
  it, or the fate of the review-side budget currently in force", and the footer
  calls ADR 079 "currently in force". The role report says ADR 082, accepted and
  resting on this note, decides five sources with a FAIL rule and drops the
  reader-side caps. The present-tense validator in the placement section and
  the "hypothetical validator" objections from critique and friction both turn
  on this status.
- The corpus count is scoped to `kb/notes/` as of 2026-08-27, while the note
  now lives in `kb/theory/`.
- The archived proposal *Exceeding a review budget splits the task* and the
  self-disagreement measurement are cited without links (orphan-references).

## Dependents affected (from the role report)

Role report run directory:
`kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/role`.
The unit ("the unquoted source", with quoted sources and linked notes exempt)
and artifact-side placement are relied on by
`kb/reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md`,
`kb/reference/proposals/archive/atomic-step-grounding-bounds-unquoted-sources-per-note.md`
and `kb/theory/a-linked-note-discharges-its-own-grounding-so-a-citing-note-owes.md`
(which also carries the 344/eight corpus count). Restating the unit as the
unquoted attribution changes what ADR 082's validator must count.

## Findings not acted on, with reasons

All fourteen stored findings are deferred by the stop; none is planned because
the rewrite will replace or move the passages they name.

- `semantic/epistemic-status-blur`, `semantic/grounding-alignment`,
  `sentence/framing-mismatch`: their main findings are the claim errors in
  items 2 and 5; they belong to the rewrite.
- `semantic/internal-consistency`: "costs the reviewer nothing" contradicts the
  body's support-judgment cost; a claim-level fix tied to item 1.
- `semantic/underspecified-assertions`, `prose/orphan-references`: corpus-count
  population and unlinked measurements; claim/evidence questions (item 6).
- `frontmatter/title-body-alignment`: a title change on a note whose title
  dependents cite; opening-and-title after the rewrite.
- `compression-bundle/detail-overhang`, `compression-bundle/marginal-value-redundancy`,
  `accessibility/notation-opacity`, `accessibility/undefined-terms`,
  `prose/mannered-prose`, `sentence/clause-packing`, `sentence/parsing-ambiguity`:
  valid text-level fixes on passages a rewrite is expected to change; rerun the
  review on the rewritten text.
