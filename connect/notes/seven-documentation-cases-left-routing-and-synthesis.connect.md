---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Seven documentation cases left routing and synthesis

**Source:** [Seven documentation cases left routing and synthesis](../../../../notes/evidence/seven-documentation-cases-left-routing-and-synthesis.md)

## Discovery Trace

**Collection rules:**

- Read `kb/notes/COLLECTION.md`. It authorizes prospecting in notes, types,
  reference, agent-memory systems, agentic systems, sources, and instructions;
  it excludes workshops. The applicable note-to-note labels include
  `exemplifies`, while note-to-reference and note-to-source candidates may use
  `evidenced-by`, `abstracted-from`, or sparse `see-also` edges where their
  reader needs fit.
- Read `kb/notes/README.md`, `artifact-analysis-README.md`, and
  `kb-maintenance-README.md`. The `artifact-analysis` head declares
  `complete: true` and already includes the source, so the by-tag `rg` was
  skipped. The `kb-maintenance` head is curated but not complete, so the
  by-tag description listing was run.

**Full title scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'` and the same
  complete title command over `kb/reference`, `kb/instructions`, and the
  combined `kb/types kb/agent-memory-systems kb/agentic-systems kb/sources`
  surface. The notes scan flagged the source-path sufficiency, durable-payload,
  index-curation, derivation, stateless-routing, and stale-self-description
  candidates evaluated below.
- Read the destination heads at `kb/reference/README.md`,
  `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`,
  `kb/sources/README.md`, and `kb/instructions/README.md`. `kb/types/README.md`
  does not exist; the full type-title scan supplied its prospecting surface.

**Description and body searches:**

- Ran
  `rg -l -i 'documentation|live source|source access|source-readable|recomputable|recoverability|addressability|routing.*source|source.*routing|cross-component' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`.
- Ran
  `rg -n -i 'documentation|live source|source access|source-readable|recomputable|recoverability|addressability|cross-component (boundary|invariant)|unknown command|command catalogue' kb/notes --glob '*.md'`.
- Ran the corresponding body search for
  `documentation|live source|source access|source-readable|recomputable|recoverability|addressability|cross-component|command catalogue`
  over `kb/reference kb/types` and `kb/instructions`.
- Ran the broader external-system/source search for
  `documentation|live source|source access|source-readable|recomputable|recoverability|addressability|cross-component|code as (knowledge|documentation)`
  over `kb/agent-memory-systems kb/agentic-systems kb/sources`.
- Ran
  `rg -l '^tags:.*\\bkb-maintenance\\b' kb/notes --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`.

**Per-destination evaluation:**

- **Notes:** Kept three candidates that explain distinct surviving layers:
  reliability-compliant stopping, consumption-path-relative payload, and
  curated orientation. Rejected derivation, specification timing,
  statelessness, and reflexive-staleness candidates where the casebook did not
  identify their mechanism or already reached them through a stronger linked
  premise.
- **Reference:** The source already links the reference collection contract,
  and the five surviving architecture pages are the post-audit outputs rather
  than preserved before/after evidence. No additional outbound reference edge
  was kept. The contract itself has a useful reverse edge because its live
  implementation default is the rule the seven cases tested.
- **Types:** No candidate passed the trigger. The casebook does not make a
  claim about artifact schemas or type semantics.
- **Agent-memory systems and agentic systems:** The title and body hits used
  documentation as implementation evidence, shipped baseline context, or an
  adoption surface. None tested replacement of exact implementation prose by
  a guaranteed live-source route, so no candidate survived.
- **Sources:** `programming-as-theory-building.ingest.md` bounds what code and
  documentation can convey, but it is already reached through the source's
  linked recovery note. A direct edge would blur external conceptual support
  with the casebook's local empirical basis.
- **Instructions:** The exact-match hit in `analyse-agentic-system/SKILL.md`
  concerns how to inspect an external system. No instruction operationalizes
  this casebook's disposition result, and the completed one-off audit procedure
  was intentionally not promoted.

**Link following:**

- Followed the source's existing links to the recovery assay, checked-copy
  rule, recompute-factor model, addressability-grain rule, and reference
  collection contract. The recovery note already reaches commitment and
  specification-timing claims, so direct links to those notes would duplicate
  a stronger route.
- Followed the addressability note to the source-path sufficiency note, the
  observer-relative note to the durable-payload note, and the maintenance
  heads to the index-curation note. These three targets state distinct theory
  that the seven cases instantiate rather than merely sharing vocabulary.
- Verified every kept target path with `test -f` and checked current inbound
  links with
  `rg -n --fixed-strings 'seven-documentation-cases-left-routing-and-synthesis' kb --glob '*.md'`.

## Connections Found

- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **exemplifies**: exact-field, argument, and behavior prose did not license a reliability-compliant stop, so the live implementation remained in the path and the prose was additive; orientation and synthesis were evaluated as separate questions.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — **exemplifies**: the audit fixed a guaranteed live-source consumption path, then retained unknown-name routing and cross-component relations that path did not cheaply supply.
- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) — **exemplifies**: the checked command catalogue kept complete names plus authored grouping and purpose because entry-point metadata and command-local help did not orient a reader who lacked the command name.

## Bidirectional Candidates

- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) ↔ source — **evidenced-by** from the theory note: the seven cases supply a bounded Commonplace instance where exactness prose failed to remove fallback work.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) ↔ source — **evidenced-by** from the theory note: the casebook tests the retention boundary against live source across seven artifacts rather than one framework recap.

## Reverse-edge Candidates

- [Reference collection contract](../../../../reference/COLLECTION.md) → source — **rests-on**: its live-implementation default and its retained categories of orientation, architecture boundaries, and cross-component invariants are the operative rule extracted from this bounded sweep.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md) — rejected as a direct edge: the source's existing recovery-assay link already reaches this distinction, and the casebook did not establish production lineage or authority for each removed passage.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — rejected as a direct edge: it concerns when specification understanding becomes available, while the casebook tested present-day recovery and read-path value; it is already one hop from the recovery note.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — rejected: the casebook observed value in unknown-name routing but did not compare stateless and stateful readers or identify statelessness as the cause.
- [Stale self-description conceals its own staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md) — rejected: the 0–3-commit lag baseline and the audit's discrepancies do not test reflexive self-concealment, missing operational triggers, or autonomy-scaled load.
- [Ingest: Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) — rejected as a direct source edge: it is already routed through the recovery-assay note and would not be evidence for the casebook's byte reductions or lookup experiments.
- [Current reference architecture pages](../../../../reference/README.md) — rejected as evidence targets: their post-audit forms are outcomes of the experiment and no longer preserve the removed exact-fact prose needed for a before/after comparison.

## Index Membership

- [KB maintenance](../../../../tags/kb-maintenance-README.md) — the source already carries the tag and would add a bounded corpus-maintenance case beside the checked-copy and staleness notes.
- [Document system](../../../../tags/document-system-README.md) — the source would supply the empirical result immediately after the head's documentation-economics and addressability claims; adding membership may also warrant the `document-system` tag.
- [artifact-analysis](../../../../tags/artifact-analysis-README.md) — already present under Applications; no edit needed.

## Synthesis Opportunities

The casebook, the source-path sufficiency note, and the routing findings imply
a narrower hypothesis than “code replaces documentation”: **source code is a
usable software-KB knowledge surface only when the reader can reach the exact
executing version and can discover the relevant unit before knowing its symbol
name**. The Commonplace cases establish both prerequisites locally through
`commonplace-source`, side-effect-free help, and retained discovery maps. A
second software-KB case should test the hypothesis before it becomes a general
note or a framework architecture rule.

## Maintenance Observations

None.

## Flags

- The source is already bounded correctly and does not need splitting.
- Do not promote the software-KB synthesis from this single-repository case;
  its external validity is the remaining empirical question.
