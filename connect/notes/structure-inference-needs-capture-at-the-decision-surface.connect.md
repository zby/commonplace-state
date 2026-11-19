---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/structure-inference-needs-capture-at-the-decision-surface.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: Bottom-up structure inference needs capture at the decision surface, not the state

**Source:** [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md)

The source is already densely linked: its footer authors 11 edges (exemplifies/mechanism/grounds/contrasts/extends/defined-in/derived-from) covering history-has-one-chance, spec-mining, raw-accumulation, wikiwiki, memory-design-axes, specification-strategy, trace-derived-authority, create-memory-directly, use-trace-derived-extraction, lineage, and the Palantir source. Prospecting below targets only edges **not** already present.

## Discovery Trace

**Topic indexes:**
- `agent-memory-README.md` — the source is already listed under "Boundaries And Failure Modes"; siblings there (raw-accumulation, trace-derived-authority, memory-design-axes) are already linked from the source. New sibling surfaced: `preserve-evidence-without-loading-history` (in the Requirements area via `agent-memory-requirements/README.md`).
- `context-engineering-README.md` — selective; no unlinked candidate (core-claims are recomputable-truth, scheduling, stateful-tools — off this note's claim).
- `learning-theory-README.md` / `observability-README.md` — read for framing; no new candidate. Note has no `complete:` mark on any of its three tag READMEs, so by-tag/body rg sweeps were run below.

**Description listing scan:**
- `rg -l -i "provenance|receipt|commit surface|write-time" kb/notes/` — flagged `distilled-artifacts-need-source-tracking` (provenance-locality parallel), `preserve-evidence-without-loading-history`, `history-has-one-chance` (already linked). Others (axes-of-artifact-analysis, derived-copy, scenario-decomposition) off-claim or already-neighboured.
- `rg -l -i "\bintent\b|legible|reconstruct.*intent" kb/notes/` — flagged `readable-artifact-loop`, `active-work-state`, `changing-requirements`; all evaluated and rejected (topical only).
- `rg -l -i "instrument|capture point|capture policy|decision surface" kb/notes/` — returned only the source + memory-design-axes (already linked). Confirms "decision surface" phrasing is near-unique to this note.

**Body search:**
- `rg -l -i "trace|decision|provenance|capture" kb/agent-memory-systems/ -g '!*.replaced.*'` — flagged `lightweight/trajectory-informed-memory-generation` (tag `trace-derived`), the comparative review, several reviews. Read trajectory-informed: a trace-extraction pipeline that mines tips from completed trajectories, with tip categories tied to outcome shape (strategy/recovery/optimization) — decision-shaped trace as input. Strong `evidence` candidate.
- `rg -l "structure-inference-needs-capture" kb/` — no artifact currently links to the source except `agent-memory-README.md`; no reverse edges exist yet.

**Link following:**
- From `preserve-evidence-without-loading-history` → its Methods list already names "Structured event logs that capture actions, decisions, errors, approvals" — i.e. decision-shaped capture — and its evaluation question "Does the system separate capture from activation?" The source supplies the missing *positional* precondition on that requirement.
- From `distilled-artifacts-need-source-tracking` → the "forward query must reach the editor **at edit time**, because its job is to interrupt" is the same locality-of-provenance argument the source makes for the "why" at the decision surface. See Synthesis.

## Connections Found

- [preserve evidence without making history the next context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **extends**: that note requires trace capture keep enough for later extraction/audit and separate capture from activation; this note adds the positional precondition it leaves open — the preserved evidence must be *decision-shaped at the capture point*, or extraction recovers endpoints without the why regardless of how much is stored.
- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) — **evidence**: a trace-extraction system whose reported success corroborates the claim — it mines tips from completed *trajectories* (not final state), and its tip categories are tied to outcome shape (strategy from success, recovery from failure-handling, optimization from inefficient-but-successful), i.e. the exception/branch/why the source says extraction needs. (`evidence` → agent-memory is authorised for the notes source→destination pair.)

## Bidirectional Candidates

- [distilled artifacts need source tracking](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) <-> source — **contrasts**: the same locality-of-provenance principle applied to a different provenance kind. Source: the decision "why" is cheap at the decision surface, unrecoverable from produced state. That note: the forward lineage query must reach the editor *at edit time* because its job is to interrupt. `contrasts` is symmetric, so authoring it from either side surfaces the neighbouring-shape distinction (intent-of-decision vs source-dependency) on both. Weaker than the two edges above — surface for the source author's judgment. See Synthesis.

## Reverse-edge Candidates

- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) → source — under `kb/agent-memory-systems/COLLECTION.md` the note→review `evidence` edge (in Connections Found) is the canonical direction; that COLLECTION explicitly says theory "links in via evidence/derived-from," so no separate review-side `rationale` backlink is warranted. Recorded here only to note the reverse direction was considered and deliberately routed as the outbound `evidence` edge instead.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — the "understanding is live" adjacency is already carried by the source's link to `create-memory-directly`; this note is about live-state lifecycle, not capture position. Topical only.
- [orchestration strategies and run state have opposite persistence](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — about persistence *value* of run-state vs strategies, not whether the captured stream carries the why. No traversal gain.
- [the readable artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — matched on "intent" incidentally; about substrate coevolution, not capture position.
- [changing requirements conflate genuine change with disambiguation](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — matched on "intent/interpretation"; unrelated claim (Agile requirements phenomenology).

## Index Membership

- [context-engineering-README](../../../../tags/context-engineering-README.md) — the source carries the `context-engineering` tag but is not listed. The README is selective by design; a future maintainer could add it under a capture/loading grouping, but this is optional, not a gap.

## Synthesis Opportunities

Three notes now instantiate one principle — *provenance is convertible to durable/checkable form only at the moment of production, and decays after*: `history-has-one-chance-to-become-checkable` (the general claim, which the source already `exemplifies`), this source (the decision "why"), and `distilled-artifacts-need-source-tracking` (the source→distillate dependency, which "must reach the editor at edit time"). The general note already exists, so this is not a new synthesis note — but `distilled-artifacts-need-source-tracking` currently links to neither and arguably should `exemplify` `history-has-one-chance` the way this source does. See Maintenance Observations.

## Maintenance Observations

- `distilled-artifacts-need-source-tracking.md` makes the same locality-of-provenance argument as this source and `history-has-one-chance-to-become-checkable.md` but links to neither; it may warrant an `exemplifies` edge to `history-has-one-chance`. Durable enough for a later triage/maintenance pass to consider; not a connection candidate for *this* source.

## Flags

None. The source makes one primary assertion (capture position is a precondition on inference feasibility); its existing footer plus the 2 new edges keep it within one topic area — not a split candidate despite the link density.
