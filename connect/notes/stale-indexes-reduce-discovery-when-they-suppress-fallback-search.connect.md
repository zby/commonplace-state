---
description: "Discovery report for possible KB connections from Stale indexes reduce discovery when they suppress fallback search"
type: kb/cache/types/connect-report.md
source: "kb/notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Stale indexes reduce discovery when they suppress fallback search

**Source:** [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md)

## Discovery Trace

**Description listing scan:**

- Read the source collection's outbound rules and the curated heads for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Read `kb/notes/kb-maintenance-README.md`. It has no `complete: true` mark, so the by-tag sweep was not skipped. Ran `rg -l '^tags:.*\bkb-maintenance\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and retained the retrieval-miss, curation, checked-copy, enforced-tag-README, recovery, and staleness-detection cluster for evaluation.
- Ran `rg -n '^description:.*(stale|index|fallback|discovery|complete|exhaustive|derived|navigation)' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'`. The strongest cross-collection candidates remained the tag-README contract and trace, LLM Wiki's regenerated cache, the stale-spec practitioner report, and the curated-index maintenance instruction.

**Topic indexes:**

- `kb/notes/tags-README.md` routed the source through KB maintenance; `kb/notes/kb-maintenance-README.md` already includes the source under Detection.
- `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md` were read as destination heads. `agentic-systems` had no direct candidate that passed the articulation test; `Exo` is already reached through the separate stale-self-description note rather than this index-specific mechanism.

**Full title surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each authorised local destination. The note surface exposed nearby claims about retrieval misses, curated orientation, checked derived copies, recovery after enforcement, and reflective staleness. The other surfaces exposed the shipped tag-README contract, ADRs 025/026, the observed tag-README trace, index-maintenance procedures, and external-system witnesses.

**Body search:**

- Ran `rg -n -i 'stale (index|view)|false completeness|apparent(ly)? (complete|exhaustive)|fallback (discovery|search)|derived view|generated listing|canonical membership|stop(ped|s)? (looking|search|discovery)' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'`.
- Ran `rg -n 'stale-indexes-are-worse-than-no-indexes|Stale indexes are worse than no indexes|Stale indexes reduce discovery' kb/instructions kb/reference kb/types kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` to distinguish already-authored inbound uses, stale visible link text, and missing edges.
- External prospecting was skipped: `external` is authorised only for already-known targets, and none was supplied independently of the repository's captured source reports.

**Link following:**

- Followed the source's existing link to `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`, then its links to the tag-README type, ADR 025, and the staleness-detection note. The checked-copy note already owns the general enforce-or-omit consequence, so another source edge to it would be redundant.
- Followed inbound uses from `a-retrieval-miss-is-a-local-reflective-path-failure.md`, `index-curation-adds-orientation-that-generation-cannot-produce.md`, `stale-self-description-conceals-its-own-staleness.md`, ADR 026, the tag-README trace, and the source ingests. Kept only targets that add a concrete downstream reading purpose from this source.

## Connections Found

- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- **extends**: places the source's fallback-suppression mechanism inside a wider causal model where a missed artifact breaks one discovery wire while other paths can remain live.
- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -- **extends**: develops the source's orientation-versus-enumeration defense into a two-surface design: selective editorial guidance plus an independently complete listing.
- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) -- **extends**: supplies the missing step between invalidating a false completeness claim and actually routing the consumer to repair, fallback, or escalation.
- [Tag README](../../../../types/tag-readme.md) -- **evidenced-by**: the shipped `complete` and `covered_by` marks are validator-enforced caches whose absence preserves the scoped-search fallback.
- [The tag-readme change as an observed causal-connection trace](../../../../notes/evidence/tag-readme-trace-observed-causal-connection.md) -- **evidenced-by**: records the concrete Commonplace episode in which this note's failure model motivated an enforced completeness mark and changed validator and discovery behavior.
- [LLM Wiki (nvk)](../../../../agent-memory-systems/reviews/llm-wiki.md) -- **evidenced-by**: an independently implemented wiki treats indexes as derived caches and regenerates them from canonical files when stale, corroborating the source/view separation behind the note's first defense.
- [Ingest: What spec-driven development gets wrong](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) -- **evidenced-by**: a practitioner report independently describes stale authoritative specs producing confident execution against an obsolete plan, while its lack of outcome data bounds this to mechanism-level corroboration.
- [Maintain curated indexes](../../../../instructions/maintain-curated-indexes.md) -- **operationalized-from**: the procedure makes curated heads explicitly selective, reconstructs full membership with scoped search, and routes enforced-mark repair through the tag-README contract.

## Bidirectional Candidates

None. Several targets already cite the source through directional `grounds`, `mechanism`, or `rests-on` relationships; those existing inbound edges do not make the proposed source-side edges semantically bidirectional.

## Reverse-edge Candidates

- [Maintain curated indexes](../../../../instructions/maintain-curated-indexes.md) → source -- **rests-on**: the procedure's rule that curated heads are selective and exhaustive consumers continue through a generated or scoped listing depends on the source's suppression mechanism; this meta-reader edge is independently useful even if the source later carries the operationalized-into edge.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) -- already linked inline from the source at the exact defense it generalizes; another edge would not improve traversal.
- [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- useful for detecting dependent-note drift, but its current inbound link already treats this source as motivation and its mechanism does not directly repair index membership.
- [ADR 026](../../../../reference/adr/026-tag-readme-type-with-completeness-and-coverage-marks.md) -- a valid witness, but the observed tag-README trace is the more useful evidence target because it separates the motivating claim, implemented decision, validation behavior, and historical limits.
- [Ingest: LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- clearly illustrates an index becoming load-bearing, but supplies no observed stale-index failure or enforcement mechanism beyond the stronger LLM Wiki code review.
- [Index](../../../../types/generated-index.md) -- defines build-time generated listings but adds structure, not evidence or a further explanation of the suppression mechanism.

## Index Membership

None. The source is already curated under Detection in [KB maintenance](../../../../tags/kb-maintenance-README.md), and no other tag landing passed the membership test.

## Synthesis Opportunities

None. The nearby material deepens the existing note's causal variable and repairs; it does not imply a separate higher-order claim that is not already owned by this note or the checked-copy note.

## Maintenance Observations

- The source title now states the narrower fallback-suppression claim, but the `kb-maintenance` landing and several inbound visible link texts still state the former overall “worse” comparison. The required post-pass rename and citer reconciliation must update those authored surfaces; changing only paths would preserve the rejected wording.

## Flags

- The artifact is not a split candidate. Its index case, broader-authoritative-artifact paragraph, synchronization mechanism, defenses, and scope all serve one suppression mechanism.
- The reframed title now names suppression of fallback search, while the description and body retain apparent false completeness as the condition that changes stopping behavior.
