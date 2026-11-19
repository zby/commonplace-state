---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/prov-overview.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: PROV-Overview (W3C PROV family roadmap)

**Source:** [PROV-Overview](../../../sources/prov-overview.md)

The source is an **immutable snapshot** (`type: snapshot`) with **no `.ingest.md` companion**. Per `kb/sources/COLLECTION.md`, snapshots are never edited and never author outbound links; the authoring signal from running connect on a snapshot is **reverse-edge** — which library artifacts should point *at* this snapshot under their own rules. The `Connections Found` section below therefore lists candidate edges for a *future* `prov-overview.ingest.md` (which would have to be created first), not edges to author anywhere today.

## Discovery Trace

**Description listing scan:**
- `rg -l -i "provenance"` across `kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/` -- large hit set; most are agent-memory reviews using "provenance" loosely. Filtered to artifacts about lineage/derivation *as a modeled concept*: `kb/notes/definitions/lineage.md`, `kb/notes/distilled-artifacts-need-source-tracking.md`, `kb/sources/in-toto-farm-to-table-guarantees.md`, `kb/reference/link-vocabulary.md`.
- `rg '^description:'` on `in-toto...ingest.md` and `build-systems-a-la-carte.ingest.md` -- confirmed in-toto ingest frames itself as a cross-domain provenance/lineage/staleness exemplar (compares-with fit).

**Topic indexes:**
- No `documentation`-tag README exists to prospect (source carries `tags: [documentation]` only). Checked `kb/notes/definitions/` neighborhood via `lineage.md` links.

**Body search:**
- `rg -l -i "\bPROV\b|W3C|prov-o|dublin core"` over notes/reference/agent-memory/agentic -- only incidental hits (`adr/023`, `systems-table.md`, `semiont.md`); none about the PROV data model. No existing artifact references PROV -> this snapshot is currently unlinked.
- `rg -l -i "lineage"` over notes/reference -- `lineage.md`, `distilled-artifacts-need-source-tracking.md`, plus review-freshness ADRs/proposals. The review-freshness cluster is about *this KB's* dependency machinery, not general provenance modeling -> rejected (see below).
- `rg -l -i "reproducib|attribution|provenance of provenance|derivation edge"` over notes -- no note treats these as a provenance-model concept the source would ground.

**Link following:**
- From `lineage.md` -> `retained-artifact.md`, `storage-substrate.md`, `behavioral-authority.md`: internal lineage cluster, none about *full* provenance; confirms `lineage.md` is the single note that explicitly contrasts itself with "full provenance" (the source's exact scope).
- From `distilled-artifacts-need-source-tracking.md` -> `link-vocabulary.md`: this KB's own `derived-from` / `Distilled into:` vocabulary — a domain-specific provenance scheme parallel to PROV's derivation model.

## Connections Found

*(Candidate outbound edges for a future `prov-overview.ingest.md`; the snapshot itself never authors links. Labels from `kb/sources/COLLECTION.md`.)*

- [lineage](../../../../notes/definitions/lineage.md) -- **evidence**: PROV is the canonical W3C standard for the "full provenance" that `lineage.md` explicitly names itself narrower than (it records attribution, derivation, provenance-of-provenance, versioning, reproducibility); the snapshot corroborates that "full provenance" is a real, broad, standardized concept the note is deliberately carving down from.
- [in-toto: farm-to-table guarantees](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) -- **compares-with**: both are external standards modeling provenance/derivation of artifacts; PROV is a descriptive interchange model for *what happened*, in-toto adds cryptographic integrity over a supply-chain *derivation graph* — parallel treatments an agent studying provenance should read together.

## Bidirectional Candidates

None. (Source is an immutable snapshot; it cannot carry return links.)

## Reverse-edge Candidates

*(The actionable deliverable: artifacts that should link TO this snapshot under their own COLLECTION.md rules.)*

- [lineage](../../../../notes/definitions/lineage.md) → source -- **evidence** (notes→sources): `lineage.md` states "Lineage is deliberately narrower than full provenance." A reader hitting that line has no pointer to what "full provenance" concretely is; PROV-Overview is the standard reference that scopes it (the eight PROV requirements — attribution, reproducibility, versioning, derivation, provenance-of-provenance — are exactly the superset lineage trims). Strongest reverse edge.
- [in-toto: farm-to-table guarantees](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) → source -- **compares-with** (sources→sources): the in-toto ingest already frames itself as a cross-domain lineage/verification exemplar; adding a compares-with to PROV situates cryptographic supply-chain provenance against the W3C descriptive provenance model. `compares-with` is authorised for the sources→sources pair.
- [distilled artifacts need source tracking](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) → source -- **see-also** (notes→sources, use sparingly): the note designs forward/reverse lineage queries and derivation records; PROV formally models derivation and provenance-of-provenance, i.e. a standardized vocabulary for the edges this note tracks. Lower confidence — the note is about *where the record lives* (a design question), not about modeling provenance, so PROV is adjacent background rather than load-bearing. Include only if the author wants an external reference model.

## Off-authorisation Candidates

None. Every surfaced candidate fits an authorised source-collection label (`evidence`, `compares-with`, `see-also`).

## Raw Text Candidates

None.

## Rejected Candidates

- [link-vocabulary.md](../../../../reference/link-vocabulary.md) -- defines this KB's `derived-from` / `Distilled into:` provenance edges. Rejected as a direct edge: it is a `reference` descriptive artifact and outbound-into-sources is not its job; the conceptual overlap is real but the useful direction is via `distilled-artifacts-need-source-tracking.md` (already surfaced), not a raw vocabulary-to-standard link.
- Review-freshness cluster (`adr/032`, `adr/034`, `proposals/factored-dependency-pairs-for-review-freshness.md`) -- use "lineage"/"provenance" for *this KB's* staleness machinery. Rejected: keyword-only overlap; PROV models provenance of arbitrary web data, not review dependency-tracking, so a link would mislead an agent expecting operational relevance.
- Agent-memory reviews mentioning "provenance" (`cortex.md`, `graphiti.md`, `mem0.md`, etc.) -- rejected: incidental use of the word for memory-record origin; none engages the PROV model.

## Index Membership

None. No curated index in a linkable collection currently groups external provenance/standards sources; a future `sources`-side grouping (PROV + in-toto + build-systems-a-la-carte as "provenance / supply-chain / build-lineage standards") would be the natural home — noted under Synthesis Opportunities rather than as an existing index.

## Synthesis Opportunities

Three captured external sources now converge on artifact lineage/derivation from different domains: **PROV** (web provenance interchange model), **in-toto** (cryptographic supply-chain integrity over a derivation graph), and **build-systems-à-la-carte** (scheduler×rebuilder freshness). A note abstracting "external provenance/build-lineage models and what each contributes to KB derived-artifact staleness theory" would tie them to `lineage.md` and `distilled-artifacts-need-source-tracking.md`. Do not create it during connect; flagged for a future writer.

## Maintenance Observations

- `prov-overview.md` has **no `.ingest.md` companion**, so it currently has no authored outbound surface at all; its only path into the KB graph is the reverse edges above. If the source is meant to earn its keep, creating `prov-overview.ingest.md` (via `cp-skill-ingest kb/sources/prov-overview.md`) would let the `Connections Found` candidates be authored.
- PROV-Overview is presently an **orphan snapshot** — no artifact in notes/reference/agent-memory/agentic references it or its terms. This is expected for a fresh capture but worth noting for triage.

## Flags

- **No outbound authoring possible today**: the snapshot is immutable and has no ingest companion. The report's real output is the Reverse-edge Candidates plus the `Connections Found` list held for a future ingest report.
- **Scope check**: PROV is a web-provenance standard, one step outside the KB's core methodology scope, but it is captured on the same footing as in-toto and build-systems-à-la-carte (external conceptual grounding for lineage/staleness theory), so the reverse edges are in-frame.
