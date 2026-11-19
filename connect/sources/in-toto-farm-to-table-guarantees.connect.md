---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/in-toto-farm-to-table-guarantees.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: in-toto — Providing farm-to-table guarantees for bits and bytes

**Source:** [in-toto: Providing farm-to-table guarantees for bits and bytes](../../../sources/in-toto-farm-to-table-guarantees.md)

This is an immutable `snapshot` under `kb/sources/` with **no matching `.ingest.md`**. Per `kb/sources/COLLECTION.md`, a snapshot never authors outbound links; its authored surface is the ingest report (absent here), and the primary connect deliverable is the **reverse-edge** set — library notes that should point at this snapshot with `evidence`/`derived-from`. The `Connections Found` entries below are therefore recommendations for a *future* `in-toto-farm-to-table-guarantees.ingest.md`, not edits to the snapshot.

Cross-domain caveat carried throughout: in-toto is a software-supply-chain **security** paper (signed layout + per-step link metadata verifying an artifact's whole production chain). Every KB connection is an analogy from supply-chain provenance/verification onto the KB's own lineage, staleness, and verification-cost theory. Analogical stretches are flagged where they matter.

## Discovery Trace

**Source COLLECTION.md outbound section read:** `kb/sources/COLLECTION.md` "Outbound links" + labels table. Extracted: snapshots are immutable (no outbound authoring); ingest/source-review carry the outbound surface; authorised labels `evidence`, `derived-from`, `rationale` (→notes), `compares-with` (→sources/agent-memory/agentic-systems), `defined-in` (→notes/definitions), `see-also` (sparingly). Excluded destinations: `kb/work/`, `kb/instructions/`. Reverse-edge posture explicitly named as the snapshot's authoring signal. Notes→sources vocabulary (from `kb/notes/COLLECTION.md`) governs the reverse edges: `evidence`, `derived-from`, `see-also`.

**Description listing scan:**
- Scoped `rg '^description:'` over `kb/sources/` (60+ rows) — flagged [prov-overview.md](../../../sources/prov-overview.md) (W3C PROV provenance family) and [build-systems-a-la-carte.md](../../../sources/build-systems-a-la-carte.md) (scheduler×rebuilder build-step model) as `compares-with` candidates; both model the same "steps consuming materials → producing products with dependency tracking" shape in-toto secures.
- `rg -l '^tags:.*academic-paper' kb/` — in-toto shares the `academic-paper` tag with ~50 sources; no editorial index for that tag, so no membership candidate arose from the tag alone.

**Topic indexes:**
- `kb/notes/README.md`, `kb/notes/tags-README.md` — scanned tag hubs; relevant hubs are learning-theory (verification/oracles), artifact-analysis (lineage), links (source-tracking), observability. No `<tag>-README.md` declared a signal specific to in-toto's supply-chain framing.

**Body search:**
- `rg -l -i 'provenance|lineage|attestation|chain of custody|derivation chain' kb/notes kb/reference` — surfaced [definitions/lineage.md](../../../../notes/definitions/lineage.md) (explicitly bounds "lineage" against "full provenance"), [distilled-artifacts-need-source-tracking.md](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md), the review-subsystem ADRs (provenance in the review-run sense — not a match, see Rejected).
- `rg -l -i 'graceful degrad|lose-one-lose-all|whole chain|supply chain|integrity of' kb/notes kb/reference` — thin; only tangential hits. in-toto's "not lose-one-lose-all / graceful degradation under key compromise" has **no** existing KB note it corroborates.
- `rg -l -i 'verifiable|validated by code|the boundary of.*verification' kb/notes` — surfaced [the-boundary-of-automation-is-the-boundary-of-verification.md](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [verifiability-gradient.md](../../../../notes/verifiability-gradient.md), [inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md), [document-types-should-be-verifiable.md](../../../../notes/document-types-should-be-verifiable.md).
- `rg -l -i 'derived copy|recomputable|mark.*(cache|validat)' kb/notes kb/types` — surfaced [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) and the four-field security note.

**Link following:**
- From `distilled-artifacts-need-source-tracking.md` followed its outbound cluster → `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` → `definitions/lineage.md`. This is the KB's derived-artifact/staleness neighbourhood; in-toto sits alongside it as an external verification exemplar rather than inside it.
- From `the-four-field-record...security-and-sovereignty.md` read the "security = untrusted-or-stale artifact reaching a high-authority channel" framing; in-toto is a clean cross-domain instance of the defence.

## Connections Found

*(Outbound edges the source cannot author itself — recommended for a future `in-toto-farm-to-table-guarantees.ingest.md`; the snapshot stays untouched.)*

- [prov-overview.md](../../../sources/prov-overview.md) -- **compares-with**: both capture provenance of produced artifacts; PROV is a descriptive interchange model for provenance, in-toto adds cryptographic *verification* (signed layout + link metadata + MATCH rules) — a reader comparing provenance approaches gains the trust/verification axis in-toto layers on PROV's descriptive one.
- [build-systems-a-la-carte.md](../../../sources/build-systems-a-la-carte.md) -- **compares-with**: both model a chain of steps consuming materials and producing products with dependency tracking; build-systems formalizes scheduler×rebuilder staleness/verifying-traces, in-toto secures the same step-graph with per-step attestation — the pair frames "verify a build chain" from the freshness side and the integrity side.

## Bidirectional Candidates

None. The snapshot authors nothing, so there is no return path to add from its side; all useful edges are reverse-edges below.

## Reverse-edge Candidates

*(Notes that should author a link TO this snapshot under `kb/notes/` COLLECTION.md rules; labels drawn from notes→sources: `evidence`, `derived-from`, `see-also`.)*

- [the-boundary-of-automation-is-the-boundary-of-verification.md](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidence**: in-toto is a clean cross-domain instance of the thesis — supply-chain *trust decisions became automatable precisely because the chain became cheaply verifiable* (Kubernetes admission controllers gate promotion on `VERIFY_FINAL_PRODUCT`, sub-0.6s per package). Strongest reverse-edge; note is `status: current` with `has-external-sources`, so a fourth corroborating source fits its convergence argument. Cross-domain but the mechanism (verification cost → automation boundary) is exactly the note's claim, not a loose analogy.
- [distilled-artifacts-need-source-tracking.md](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) → source -- **evidence** (analogical, flag): in-toto is an at-scale exemplar of the note's core move — the dependency record lives *outside* the delivered artifact (signed link metadata + a MATCH-rule graph), and it is verifiable rather than trusted. Note is `status: seedling`; treat as corroborating a general design pattern (lineage stored separately, made checkable), not as bits-domain proof of a prose-distillation claim.
- [the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) → source -- **see-also** (or **evidence**, flag): the note defines *security risk* as "does anything untrusted, or anything stale, reach a high-authority channel? — a behavioral-authority × lineage question." in-toto operationalizes exactly that defence in the supply-chain domain (reject a tampered/wrong-functionary artifact; supersede a layout to drop a compromised key). A reader wanting a concrete security-via-verifiable-lineage system gains one; the cross-domain gap keeps it short of clean `evidence`.
- [definitions/lineage.md](../../../../notes/definitions/lineage.md) → source -- **see-also** (sparingly): the definition explicitly states "lineage is deliberately narrower than full provenance." in-toto (with prov-overview) is a canonical *full-provenance-plus-verification* system that illustrates the boundary the definition draws. Useful only as an anchor for what "full provenance" the definition is excluding; do not over-link a `current` definition.

## Off-authorisation Candidates

None. The notes→sources labels (`evidence`, `derived-from`, `see-also`) cover every candidate that passed the articulation test; nothing needed a label outside the authorised set.

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- [verifiability-gradient.md](../../../../notes/verifiability-gradient.md) -- shares the "verify → automate" vocabulary and in-toto does deterministic pass/fail checks, but the note is scoped to deploy-time-learning artifacts (prompts→schemas→tests→code) moving along a hardening ladder. in-toto is a fixed security framework, not an artifact climbing that gradient; keyword overlap only, no traversal gain.
- [inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- tempting ("verify via inspectable artifact, not trust in the process"), but the note's claim is about *representational form* (readable code/schemas vs blackbox weights). in-toto's links are inspectable, yet the note's point is form-choice, not chain verification — merely-related.
- [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) -- in-toto's MATCH rule ("checked or absent": a link with an invalid signature is dropped) rhymes with the note's checked-or-omitted mark discipline, but the note is tightly about KB caches/marks recomputable from a ground-truth source. in-toto verifies a *history*, not a recomputable cache; the analogy is aesthetic, not load-bearing.
- [trace-derived-memory-earns-authority-per-operation-not-at-capture.md](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) -- "authority earned through verification operations, not at capture" and in-toto's "verification coverage / per-step attestation" rhyme, but the note is a memory-maturation ladder (fail→investigate→verify→distill→consult); in-toto attests provenance, it has no maturation ladder. Too much of a stretch for a link.
- Review-subsystem ADRs (`034-...execution-provenance`, `031/032/033/036`) -- matched "provenance" lexically but mean *review-run execution provenance* (which model ran which review), an unrelated internal-plumbing sense; not connections.

## Index Membership

None. `kb/sources/` has no curated per-tag index that in-toto would join; the `academic-paper` tag has no editorial README. A future `in-toto.ingest.md` would be the discoverability surface, not an index entry.

## Synthesis Opportunities

Possible (do not author now): in-toto + [prov-overview.md](../../../sources/prov-overview.md) + [build-systems-a-la-carte.md](../../../sources/build-systems-a-la-carte.md) form a three-source external cluster on **"verify a chain of production steps"** — build-systems from the freshness/staleness side, PROV from the descriptive-interchange side, in-toto from the cryptographic-integrity side. Together they could ground a note on *external supply-chain/provenance verification as corroboration for the KB's own lineage + managed-staleness machinery*. Speculative; needs the ingest report first.

## Maintenance Observations

- **Missing ingest report.** `kb/sources/in-toto-farm-to-table-guarantees.ingest.md` does not exist, so this snapshot currently has no authored outbound surface and the `Connections Found` edges above cannot be placed anywhere. If in-toto is meant to inform KB theory (its farm-to-table verification maps onto lineage/staleness), running `cp-skill-ingest kb/sources/in-toto-farm-to-table-guarantees.md` would create that surface and let the compares-with edges land.
- **Uncorroborated in-toto concept.** in-toto's "graceful degradation / not lose-one-lose-all under partial key compromise" (thresholds, k-of-n functionaries shrinking the single-key attack surface) has no matching KB note. If the KB later develops a claim about *redundant/independent verification degrading gracefully rather than catastrophically* (analogous to error-correction with decorrelated checks), in-toto's Section 5 / Table 1 would be direct evidence — flagged here as a durable gap, not a current candidate.

## Flags

- **Cross-domain source.** Every candidate is an analogy from software-supply-chain security onto KB methodology. The single connection that survives without an analogical discount is the reverse-edge to `the-boundary-of-automation-is-the-boundary-of-verification.md` (the verification-cost→automation mechanism transfers directly). The rest are `see-also`/soft-`evidence`; a future writer should confirm each earns its keep before authoring.
- **Not a split candidate.** in-toto makes one substantive assertion for KB purposes (verifiable whole-chain provenance enables automated trust), landing on <5 notes concentrated in one topic area (verification/lineage); it does not meet the split-candidate threshold.
- **No genuine strong-outbound.** Because the snapshot is immutable and un-ingested, this report is honestly reverse-edge-only plus two ingest-report recommendations; no library artifact is edited.
