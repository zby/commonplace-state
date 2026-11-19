---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/parametric-reproduction-cannot-replace-an-authoritative-record.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Parametric reproduction alone cannot replace an authoritative record

**Source:** [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md)

## Discovery Trace

**Source reading and authorisation:**

- Verified the closing-pass source SHA-256 as `ae2a74d6467584560135974d8d32153b91697532f0d58d879c1c6359658c9b99` and read the source in full. Its single central distinction is between reproducing record content and transferring authority; the mechanism is a governed-artifact/interface requirement comprising identity, integrity, contestability, attribution, and, for mutable records, currentness and addressable revision.
- Read `kb/notes/COLLECTION.md`. It authorises local prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; excludes `kb/work/`; and authorises `external` only for already-known targets. No external target was supplied, so external prospecting was skipped.

**Curated heads and indexes:**

- Read `kb/notes/README.md`, `kb/notes/agent-memory-README.md`, `kb/notes/foundations-README.md`, and `kb/notes/tags-README.md`. Neither matching tag README declares `complete: true`, so both tag-scoped description sweeps were run. The source fits the agent-memory head's authority/lifecycle boundary cluster and the foundations head's core-theory role, producing two index-membership candidates.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The external-system head exposed Decapod's governed internalization-artifact contract; the reference head exposed the shipped source-of-truth claim in `agent-memory-coverage.md`; the other heads confirmed that Exo and the already-authored source ingests cover the main existing examples.

**Full title and description scans:**

- Generated the complete title surface once for each authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, then filtered the generated surfaces with `rg -i 'authorit|record|provenance|lineage|identity|integrity|contest|revision|supersed|current|parametric|weight|checkpoint|cache|govern|signature|source of truth|derived|mutable'`. This surfaced the history/attestation, authority-operation, lifecycle, runtime-governance, derived-copy, Decapod, ROME, in-toto, and retirement-procedure clusters.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` for each of the six destinations with the same concept filter.
- Ran `rg -l '^tags:.*\bagent-memory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the same query with `foundations`, filtering both for the authority/revision/parametric vocabulary above. These recalled `make-authority-explicit.md`, `keep-compiled-views-aligned.md`, `retire-redact-supersede-relax.md`, `history-has-one-chance-to-become-checkable.md`, and the source itself.

**Body search by destination:**

- `rg -n -i 'contestab|stable identity|authenticity|integrity|authoritative object|transfer.*authority|retire.*record|signed checkpoint|adopting authority|institutional status' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'` -- retained the history/attestation note and in-toto ingest; rejected broad governance and ordinary contestability matches.
- `rg -n -i 'parametric|model weights|checkpoint' kb/notes/ --glob '*.md'` -- confirmed that the source already links the strongest addressability, deploy-time-learning, and commitment premises; `runtime-structure-determines-governance-control-surfaces.md` remained useful because it explains how an interface can expose governance handles rather than assuming explicit text is the only eligible form.
- `rg -n -i 'source.of.truth|canonical|derived (copy|view|cache)|independent authority' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'` -- kept `agent-memory-coverage.md` as a reverse-edge candidate and rejected `storage-architecture.md` as an implementation description already subsumed by that coverage map.
- `rg -n -i 'supersed|revision|currentness|temporal validity|lineage' kb/notes/agent-memory-requirements/ kb/notes/definitions/ --glob '*.md'` -- rejected the broad lifecycle and lineage notes because the source already carries the narrower currentness/addressable-revision links it needs.
- `rg -l -i 'parametric|model.weights|checkpoint|adapter' kb/agent-memory-systems/ --glob '*.md'` followed by focused reads of Agent-R, KBLaM, Decapod, Hindsight, and SAGE -- Agent-R and KBLaM are already authored evidence; Decapod was retained as a qualified contract-level witness; Hindsight and SAGE govern explicit/database records rather than the reproduction-to-substitution boundary.
- `rg -n -i 'canonical|protected|record|rewrit|checkpoint|parametric|model.weights' kb/agentic-systems/ --glob '*.md'` -- Exo is already authored; GBrain and Swamp were rejected because their governance surfaces do not test parametric reproduction or authority transfer.
- `rg -l -i 'signature|attestation|authenticity|integrity|model weights|parametric|checkpoint' kb/sources/ --glob '*.ingest.md'` -- retained in-toto as the clean cryptographic-integrity witness; ROME and the text-optimization/scaffolding sources are already authored.
- `rg -l -i 'source.of.truth|canonical|authorit|provenance|lineage|mutable|supersed|current|audit|model.weights|checkpoint|selective revision|invalidation' kb/instructions/ --glob '*.md'` -- no instruction warranted an outbound edge. `retire-artifact.md` was rejected because its extraction gate does not depend on parametric reproduction; under the instruction collection's exceptional-link posture, no reverse `rationale` edge was forced.
- `rg -n 'parametric-reproduction-cannot-replace-an-authoritative-record|Parametric reproduction alone cannot replace|Parametric reproduction cannot replace' kb/ --glob '*.md' --glob '!reports/**'` -- found one article citation and one workshop mention. Articles are not an authorised outbound destination and `kb/work/` is explicitly excluded, so neither was prospected as a candidate.

**Link following:**

- Followed the source's local links to `deploy-time-learning-is-the-missing-middle.md`, `only-explicit-retention-is-durable-writable-and-addressable.md`, `commitment-not-derivation-creates-new-ground-truth.md`, `definitions/system-definition-artifact.md`, and `agent-memory-requirements/keep-compiled-views-aligned.md`. Their neighborhoods showed that currentness, addressability, commitment creation, binding force, and derivative-cache governance are already directly represented.
- Followed the explicit-retention note to `reflection-buys-addressability.md`; rejected another direct edge because the source already imports its more specific comparison through the explicit-retention note.
- Followed the authority and lineage cluster through `make-authority-explicit.md`, `retire-redact-supersede-relax.md`, `definitions/knowledge-artifact.md`, and `definitions/lineage.md`. The first two are broader operational checklists, while the definitions use source/behavioral-authority senses that should not be substituted for the source's institutional-authority claim.
- Followed Decapod's internalization artifact to its limitation section: the manifest supplies source hash, model id, profile/binary hashes, replay recipe, capability contract, risk tier, TTL, and mount leases, but the built-in adapter is a noop. The candidate is therefore evidence for a governable artifact/interface contract, not evidence that parametric substitution has succeeded.
- Followed the in-toto ingest to `history-has-one-chance-to-become-checkable.md`. Together they separate content resemblance from later-checkable attestation: one gives the general production-history mechanism and the other its signed, hash-checked systems witness.
- Read `kb/reference/COLLECTION.md` before retaining the reverse-edge candidate and confirmed that reference→notes `rationale` is authorised. Verified every retained candidate path with `test -e`.

## Connections Found

- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) -- **grounds**: explains why reproduced content cannot authenticate who adopted a record or how it was produced; those facts remain checkable only through contemporaneous attestation or re-derivability carried by the authoritative object.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **grounds**: supplies the mechanism behind the source's interface qualification: a parametric artifact can support authority only when its surrounding structure exposes handles for identity, validation, correction, appeal, and drift control.
- [Decapod](../../../../agent-memory-systems/reviews/decapod.md) -- **evidenced-by**: provides a code-grounded governed-internalization contract with source/model/profile hashes, replay recipe, capability scope, expiry, integrity checks, and mount leases; its noop adapter also cleanly bounds the evidence to governance infrastructure rather than demonstrated parametric substitution.
- [Ingest: in-toto — Providing farm-to-table guarantees for bits and bytes](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) -- **evidenced-by**: shows in a mature cross-domain system that authenticity and integrity come from signed identities, hashes, and verified production relations, not from reproducing signature-shaped content.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) → source -- **rationale**: the shipped distinction between authored Markdown as source of truth and generated or compiled behavior-facing views as derivative rests on the source's explanation of why reproducing content does not transfer authority.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Make Authority Explicit](../../../../notes/agent-memory-requirements/make-authority-explicit.md) -- its operation-by-operation governance checklist is compatible with the source, but it is broader and less precise than the source's own substitution guarantees; another edge would add adjacency rather than a premise or developed consequence.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) -- shares mutable-currentness vocabulary, but the source already links the more direct deploy-time-learning and compiled-view notes; the lifecycle checklist does not further explain authority transfer.
- [Knowledge artifact](../../../../notes/definitions/knowledge-artifact.md) and [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) -- both distinguish authority families, but the source uses institutional/source authority (who adopted an operative record and under what mandate), not the KB's registered consumer/channel/force field. A definition link would blur rather than resolve that distinction.
- [Storage](../../../../reference/storage-architecture.md) -- its authored-Markdown/generated-index split is a shipped instance, but the broader `agent-memory-coverage.md` row is the better reverse-edge source because it states the authority limitation and regeneration gap directly.
- [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md), [KBLaM](../../../../agent-memory-systems/reviews/KBLaM.md), [ROME](../../../../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md), and [Exo](../../../../agentic-systems/reviews/exo.md) -- all pass the articulation test but are already authored in the source, so they were evaluated as existing coverage rather than surfaced as new candidates.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) and [Swamp](../../../../agentic-systems/reviews/swamp.md) -- expose explicit governance, revision, audit, and provenance handles, but neither tests the claim's reproduction-to-substitution boundary; Decapod is the more discriminating system case.
- [Retire an artifact](../../../../instructions/retire-artifact.md) -- its extraction gate protects irreproducible residue during deletion, but the procedure does not rely specifically on parametric reproduction or authority transfer, so a reverse `rationale` edge would overstate the dependency.

## Index Membership

- [Agent memory](../../../../tags/agent-memory-README.md) -- candidate addition under Boundaries And Failure Modes: separates beneficial parametric internalization from retirement of the governed record that remains the source of authority.
- [Foundations](../../../../tags/foundations-README.md) -- candidate addition near the core theory/self-improving-system boundary: states the general reason stronger reproduction does not by itself eliminate the authoritative project state on which agents and humans coordinate.

## Synthesis Opportunities

None. The higher-order claim implied by the attestation, control-surface, internalization-contract, and model-editing evidence -- representation and authority are orthogonal until governance binds them -- is already the source note's central synthesis.

## Maintenance Observations

- The source deliberately uses *authority* for institutional/source status, while the KB's registered *behavioral authority* records consumer, channel, and force. The distinction is coherent but remains easy to collapse during later linking; the source's explicit adoption/mandate wording should remain load-bearing.

## Flags

- Evidence boundary: Decapod demonstrates a strong manifest, lease, and integrity contract around a prospective adapter, but its built-in profile is a noop and the review found no durable parametric memory. Cite it only for the governance/interface requirements a future authoritative parametric artifact would need, not as a successful substitution case.
