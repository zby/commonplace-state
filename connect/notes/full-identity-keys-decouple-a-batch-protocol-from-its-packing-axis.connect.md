---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/full-identity-keys-decouple-a-batch-protocol-from-its-packing-axis.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: Full-identity keys decouple a batch protocol from its packing axis

**Source:** [Full-identity keys decouple a batch protocol from its packing axis](../../../../notes/full-identity-keys-decouple-a-batch-protocol-from-its-packing-axis.md)

Source already authors three footer edges: `derived-from` → ADR 029, `see-also` → decomposition-heuristics, `see-also` → agent-orchestration-multi-dimensional-design-space. Those are treated as existing state and not re-proposed.

## Discovery Trace

**Curated heads:**
- `kb/notes/tags-README.md` — source carries `tags: [computational-model]`; hub points to `computational-model-README.md`.
- `kb/notes/computational-model-README.md` — read in full. It is a **selective** head (not `complete: true`), so the by-tag `rg` sweep below was still required. Source is NOT listed in this README. Clusters relevant to the source: Scheduling & Orchestration, Error Correction & Reliability.

**Description listing scan:**
- `rg -l '^tags:.*computational-model' kb/notes/ | xargs rg '^description:'` — enumerated the full ~55-note `computational-model` membership. Flagged from descriptions: `scheduler-llm-separation-exploits-an-error-correction-asymmetry` (symbolic-vs-LLM bookkeeping), `unified-calling-conventions-enable-bidirectional-refactoring` (stable calling convention absorbs substrate change), `semantic-sub-goals-that-exceed-one-context-window-become-scheduling` (partition + symbolic collection between semantic calls), `access-burden-and-transformation-burden-are-distinct-query-dimensions` (distinct burdens that can vary separately).

**Body search:**
- `rg -ln '\bbatch(ed|ing)?\b' kb/notes/ kb/reference/` — mostly review-system reference (ADRs 029/030/034, review proposals) plus the source. Confirms the batch-protocol vocabulary is concentrated in the review subsystem, from which the source was abstracted.
- `rg -ln 'wire (format|protocol)|renderer|coverage check'` — only ADRs 038/029/026 and the source. No other note works the wire-protocol layer.
- `rg -ln 'self-identif|composite (key|identit)|full identity'` — hits `many-to-many-edge-state-is-where-files-yield-to-a-database` (composite-key phrase, but relational-store context — evaluated and rejected below), plus unrelated hits.
- `rg -ln 'packing axis|grouping axis|policy .{0,20}protocol'` — only ADR 029 and the source (ADR 029 §5 "Batching is a packing choice, not a protocol" — the exact statement the note generalizes; already the `derived-from` edge).

**Link following:**
- From ADR 029, followed footer edges: 031 (run-owned pairs), gate-learning proposal, ADRs 035/036 — all storage/acceptance refinements downstream of the protocol, not general claims. No new note-collection candidates.
- From `computational-model-README` Error Correction cluster → `scheduler-llm-separation`, confirming the error-correction reading of the source's "Why this matters more for LLM calls" section.

## Connections Found

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — **grounds** (context: the "Why this matters more for LLM calls" section rests on symbolic bookkeeping — coverage, ordering, failure attribution — being recoverable where LLM positional inference is not; that asymmetry is exactly this note's premise). **LOAD-BEARING LABEL FLAG:** target is `status: seedling`, and `grounds` is load-bearing. A future writer should confirm the premise is solid before authoring, or downgrade to `see-also`. Alternative label: `mechanism` (how the decoupling's recovery guarantee operates).
- [unified-calling-conventions-enable-bidirectional-refactoring](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — **contrasts** (context: neighbouring-shape instance of the same move — a stable interface key makes one axis of variation free without changing the interface; there a name-based calling convention decouples call sites from the neural/symbolic substrate, here a full-identity key decouples the wire protocol from the packing axis; reader wants to see what each key decouples). Target `status: current`; `contrasts` is additive. Could reasonably be `see-also` instead.

## Bidirectional Candidates

- [unified-calling-conventions-enable-bidirectional-refactoring](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) <-> source — **contrasts** is symmetric; if authored, the return edge is equally useful (a reader on either note benefits from the paired "stable-key-absorbs-an-axis" framing).

## Reverse-edge Candidates

- [structured-output-codec-for-review-protocol](../../../../reference/proposals/structured-output-codec-for-review-protocol.md) → source — **rationale** (under `kb/reference/COLLECTION.md`, a design proposal may carry a `rationale` edge to a note it rests on). The codec proposal swaps the review protocol's *representation* (sentinel markdown vs schema-validated structured output); the source's claim that identity lives in the key, not in position/representation, is part of why a codec swap is safe. Weak/optional — the axes differ (packing axis vs representation), so a writer may judge it too loose. Do NOT author from here; flagged for the proposal's owner.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) — shares the phrase "keyed by the composite identity," but that is a relational-store-on-the-filesystem argument (when files yield to a DB). Keyword-only overlap; no traversal benefit. Rejected.
- [access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — shares the move of separating dimensions that can vary independently, but the source already carries that framing via its authored `see-also` to `agent-orchestration-occupies-a-multi-dimensional-design-space`. A third instance would be redundant and dilute traversal. Rejected.
- [semantic-sub-goals-that-exceed-one-context-window-become-scheduling](../../../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — adjacent (partition semantic work with symbolic collection between calls), but it is about *deciding to partition*, while the source is about the *wire format of the response* once partitioned — the source's own Scope section explicitly disclaims the content-selection choice. The existing `see-also` to decomposition-heuristics already covers the scheduler-facing side. Rejected to avoid a near-duplicate edge.
- ADR 029 reverse `rationale` edge — not proposed: the honest lineage is note `derived-from` ADR 029 (already authored). An ADR-rests-on-note edge back would invert lineage and create a cycle. Rejected.

## Index Membership

- [computational-model-README](../../../../tags/computational-model-README.md) — the source carries the `computational-model` tag but is absent from this selective head. A future writer could add it under **Scheduling & Orchestration** (or a protocol/wire-format line), since it is the only note in the tag working the batched-call *wire protocol* layer. Connect does not edit indexes; this is a candidate only.

## Synthesis Opportunities

Two notes — this source and [unified-calling-conventions-enable-bidirectional-refactoring](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — together imply a higher-order claim not yet captured: *a well-chosen stable interface key converts a variation that would otherwise be a protocol/architecture choice into a free policy choice made by the caller* (full-identity key → packing axis is policy; name-based dispatch → neural/symbolic substrate is a refactor, not a call-site change). `agent-orchestration-occupies-a-multi-dimensional-design-space` supplies the "independent axes" framing that would sit under it. Do not author during connect; noted for a possible future synthesis note.

## Maintenance Observations

- The batched-call wire-protocol concept lives almost entirely in the `kb/reference/` review subsystem (ADR 029 and its lineage 030/031/034/035/036, plus the codec and factored-dependency proposals). This source is the sole `kb/notes/` generalization. If further protocol-agnosticism claims get abstracted, they will cluster here — worth watching for a small "batch/wire-protocol" sub-theme.

## Flags

- One load-bearing (`grounds`) candidate points at a `status: seedling` target — see Connections Found. Author only after confirming the premise, or use the `see-also` fallback.
