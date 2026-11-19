---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/build-systems-a-la-carte.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: Build Systems à la Carte

**Source:** [Build Systems à la Carte](../../../sources/build-systems-a-la-carte.md)

The source is an **immutable snapshot** (`type: ./types/snapshot.md`, tag `academic-paper`) and has **no `.ingest.md` companion**. Per `kb/sources/COLLECTION.md`, a snapshot is never a link author; the primary connect signal is **reverse-edge** — which library artifacts should add `evidence`/`derived-from` links pointing at this paper. The paper's transferable core for this KB: **minimality** (Def 2.1 — rebuild only what transitively depends on changed inputs, at most once), **early cutoff** (stop when a recomputed result is unchanged), the **scheduler × rebuilder** orthogonal decomposition, and the rebuilder ladder **dirty bit → verifying traces → constructive traces** (store a hash of a derived value, re-check it against the source to decide rebuild; a content-addressable cache to fetch instead of recompute).

## Discovery Trace

**Topic indexes:**
- Read `kb/notes/tags-README.md` — routed toward `kb-maintenance`, `observability`, `context-engineering`, `computational-model` tag areas as the plausible landing zone for staleness/caching/recompute theory.
- Listed `kb/notes/*README*` — no build-systems-specific tag head; the relevant clusters are kb-maintenance (staleness) and context-engineering (recompute cost).

**Body search (actual queries over `kb/notes/`, `kb/reference/`):**
- `content-address`, `à la carte`, `early cutoff`, `self-track`, `isolated points`, `build system` — **zero hits**; the paper's own vocabulary is not present in the KB, so matches are conceptual, not lexical.
- `minimal` / `incremental` / `recomput` / `recomputable` — surfaced `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`, `llm-recompute-cost-inverts-the-store-vs-recompute-default.md`, `distilled-artifacts-need-source-tracking.md`, `kb-maintenance-README.md`.
- `hash` / `cache` / `rebuild` — surfaced `link-graph-plus-timestamps-enables-make-like-staleness-detection.md` (explicit Make analogy), plus reference review-freshness files `adr/032-review-freshness-uses-db-snapshots-not-git.md`, `adr/038-...`, `proposals/factored-dependency-pairs-for-review-freshness.md`.
- `scheduler` / `rebuild` — surfaced the agent-orchestration "scheduler" cluster (`scheduler-llm-separation-...`, `llm-mediated-schedulers-...`, `agent-runtimes-decompose-...`, `the-practical-scheduler-is-the-host-language.md`); evaluated as keyword collision (see Rejected).
- `rg -l "build-systems-a-la-carte|Build Systems à la Carte"` across `kb/` — one existing reference: `kb/work/lineage-mechanisms/verification-locus-and-provenance-theory.md` (workshop; excluded destination — see Maintenance Observations).

**Link following:**
- Followed the "Relevant Notes" footer of `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` → confirmed a tight cluster: make-staleness (detection), distilled-artifacts-need-source-tracking (lineage), llm-recompute (value half), tag-readme marks. This cluster is the KB's "derived-artifact freshness" neighborhood — the exact territory the paper formalizes.
- Followed the workshop reference → it already maps review-freshness (acceptance table keyed on `note_hash`/`gate_hash`) to a **"verifying trace" in the Build Systems à la Carte sense**, confirming the reference-side reverse edges below.

**Authorisation check:**
- `kb/sources/COLLECTION.md`: snapshots immutable, primary signal reverse-edge; do not link into `kb/work/` or `kb/instructions/`.
- `kb/notes/COLLECTION.md`: notes→sources labels are `evidence` (source corroborates the claim) and `derived-from` (claim abstracted from the source). These notes predate the 2026-07-06 capture, so `evidence` — not `derived-from` — is the correct reverse-edge label.
- `kb/reference/COLLECTION.md`: reference→sources edges are `evidence`/`derived-from`, marked "uncommon" — use when a design choice was informed by or is corroborated by a specific source. Fits the review-freshness = verifying-trace mapping.

## Connections Found

The source is an immutable snapshot with **no authored outbound surface** — no `.ingest.md` exists, so there is no artifact for connect to recommend outbound edits to. Outbound edges (the paper `evidence` [note X]) would have to be authored from a future ingest report; the same landing notes listed under **Reverse-edge Candidates** are what that ingest report should cite. See Flags.

## Bidirectional Candidates

None. (No outbound edge exists to pair a return link with; the substantive edges are the inbound/reverse ones below.)

## Reverse-edge Candidates

Notes and reference docs that, under their own `COLLECTION.md` rules, should add an `evidence` link **to** this snapshot. Connect does not author these.

**From `kb/notes/` (label `evidence`):**

- [link-graph-plus-timestamps-enables-make-like-staleness-detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) → source — **evidence**: the note reasons from an informal Make analogy (timestamps, rebuild-if-source-newer, accept false positives). This paper is the formal home of that analogy — Def 2.1 minimality, and the rebuilder ladder that generalizes crude timestamps to verifying/constructive traces, i.e. exactly the "more precise than age-based heuristics" mechanism the note reaches for. Strongest reverse edge.
- [a-derived-copy-of-recomputable-truth-must-be-checked-or-absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) → source — **evidence**: the note's "checked or absent" rule for a derived copy is the build-system rebuilder in prose — a verifying trace stores a hash of a derived value and re-checks it against the source before trusting it (checked), while a content-addressable cache lets you drop and refetch (absent-and-recover). The paper corroborates the checked-vs-recompute asymmetry with a formal, executable external system.
- [llm-recompute-cost-inverts-the-store-vs-recompute-default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) → source — **evidence**: the note argues LLMs invert software's "prefer recompute, distrust the stored copy" default. The paper is the canonical build-system treatment of that ordinary default — persistent build information as "memory", and §7.3 showing minimal build systems *are* generalized memoization — so it grounds the code-side baseline the note claims to flip.
- [distilled-artifacts-need-source-tracking](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) → source — **evidence**: the note requires a dependency record so a source edit names its downstream distillates for staleness review. That is the build system's dependency graph plus rebuild-on-change; the paper formalizes both the graph and the minimality guarantee the tracking is trying to approximate. (Somewhat redundant with the make-staleness edge above; author whichever the note-owner finds tighter.)

**From `kb/reference/` (label `evidence`):**

- [adr/032-review-freshness-uses-db-snapshots-not-git](../../../../reference/adr/032-review-freshness-uses-db-snapshots-not-git.md) → source — **evidence**: review freshness stores content hashes of the note and gate and re-checks current filesystem text against accepted-snapshot hashes to decide whether a verdict must be recomputed. That is precisely the paper's **verifying-traces** rebuilder (Shake). The workshop lineage theory already names this mapping explicitly.
- [proposals/factored-dependency-pairs-for-review-freshness](../../../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) → source — **evidence**: generalizes the hash-keyed verifying-trace freshness to arbitrary `(document, gate)` pairs — the same rebuilder abstraction the paper isolates, applied to review artifacts.

## Off-authorisation Candidates

None. The candidate edges all fit the `evidence` label authorised for `notes→sources` and `reference→sources`.

## Raw Text Candidates

None. (Source has frontmatter; all candidates carry frontmatter.)

## Rejected Candidates

- [scheduler-llm-separation-exploits-an-error-correction-asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md), [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md), [the-practical-scheduler-is-the-host-language](../../../../notes/the-practical-scheduler-is-the-host-language.md) — **keyword collision**. These use "scheduler" for agent control-flow / task ordering in a tool loop; the paper's "scheduler" is a build-system task-order engine (topological/restarting/suspending). The abstract "clean separation of two concerns" parallel is real but too loose to help traversal, and a reader following the link would land in an unrelated problem domain. Reject.
- [axes-of-artifact-analysis](../../../../notes/axes-of-artifact-analysis.md) — the paper's à-la-carte method (decompose two deeply-wired choices into orthogonal axes, tabulate the design space, recombine to reach unoccupied points) is a genuine methodological rhyme with this note's design-space framing, but the note's axes concern retained-artifact analysis, not build systems; citing the paper adds a nice analogy without a concrete traversal payoff. Reject as "merely related."

## Index Membership

None. `kb/sources/` has no curated index that would need this snapshot added; the `academic-paper` tag is the only membership and it is already stamped in frontmatter.

## Synthesis Opportunities

A latent higher-order claim spans four KB artifacts: **the KB's derived-artifact freshness machinery is a build system.** Its scheduler is "when is review/re-distillation due" (link-graph timestamps, lineage records); its rebuilder ladder runs from a dirty bit (`status:` fields) through verifying traces (review-freshness hash checks, tag-README `complete`/`covered_by` marks) — with early cutoff as the "unchanged result stops the cascade" optimization. `a-derived-copy-...`, `llm-recompute-...`, `link-graph-plus-timestamps-...`, and ADR 032 each occupy one cell of that design space without naming the space. A synthesis note mapping these onto the paper's scheduler×rebuilder classification would name it. **Do not author it during connect** — and note the workshop below is already developing this line.

## Maintenance Observations

- `kb/work/lineage-mechanisms/verification-locus-and-provenance-theory.md` (workshop, excluded destination) already cites this snapshot by name and maps review-freshness to a "verifying trace in the Build Systems à la Carte sense", and lists it in a sources sweep ("paths to be finalized"). This is a durable synthesis-in-progress: a later maintenance step may promote a library note and/or an ingest report from that workshop, at which point the reverse edges above become live authoring targets. Recorded here, not as a connection candidate, because `kb/work/` is not a linkable destination.

## Flags

- **No `.ingest.md` companion exists** for this snapshot. Snapshots carry no outbound surface, so the paper's outbound landing (all the `evidence` edges above, authored from the source side) currently has no vehicle. Recommend creating `kb/sources/build-systems-a-la-carte.ingest.md` (via `cp-skill-ingest`) if outbound authoring is wanted; otherwise the reverse edges are the complete authoring path.
- **Rich source, single deliverable.** The paper connects to 5+ artifacts across two collections and multiple topic areas (staleness, caching, recompute cost, review freshness). Not a "split candidate" in the note sense (it is an immutable snapshot), but a signal that the Synthesis Opportunity above is worth a dedicated note rather than scattered per-note `evidence` edges.
