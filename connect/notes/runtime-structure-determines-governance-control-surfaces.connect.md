---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/runtime-structure-determines-governance-control-surfaces.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: Runtime structure determines the control surfaces available to governance

**Source:** [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md)

Source collection: `notes` (theoretical). Authorised outbound labels (from `kb/notes/COLLECTION.md`): to notes — `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`; to reference/agent-memory/agentic-systems/sources — `evidence`, `derived-from`, `see-also`; to instructions — `see-also` only (usual direction is inverse). Do not link into `kb/work/`.

Existing outbound edges already authored (excluded from candidates): agent-runtimes-decompose (grounds), methodology-enforcement-is-constraining (extends), semantic-review-catches-content-errors (exemplifies), inspectable-artifact-not-supervision (grounds).

## Discovery Trace

**Curated heads read:**
- `kb/notes/tags-README.md` — top-level hub; located tag areas: architecture, computational-model, observability, kb-maintenance, failure-modes.
- `kb/notes/architecture-README.md` — no `complete` mark, so ran by-tag sweep. Curated list is control-plane/install-focused; nearest neighbour is agent-runtimes-decompose (already linked).
- `kb/notes/computational-model-README.md` — no `complete` mark, so ran by-tag sweep. Has an "Error Correction & Reliability" cluster and a "Scheduling & Orchestration" cluster relevant to the scheduler/context-engine framing; source not currently listed there.

**Description listing scan (by tag):**
- `rg -l '^tags:.*\barchitecture\b' … | xargs rg '^description:'` — flagged agent-runtimes-decompose (linked), files-not-database, agents-md-as-control-plane. None new load-bearing.
- `rg -l '^tags:.*\bcomputational-model\b' …` — large set; flagged agent-memory-is-a-crosscutting-concern (strong parallel), agent-runtimes-decompose (linked), the scheduling cluster (topical, not load-bearing here).
- `rg -l '^tags:.*\bobservability\b' …` — flagged link-graph-plus-timestamps-enables-make-like-staleness-detection (drift-oracle contrast), semantic-review (linked), inspectable-artifact (linked).
- `rg -l '^tags:.*\bkb-maintenance\b' …` — flagged a-derived-copy-of-recomputable-truth, link-graph-plus-timestamps, criteria-edits-invalidate-verdicts.

**Body search:**
- `rg -l -i "governance" kb/notes/` — target plus agent-memory cluster, orchestration-strategies-run-state; none besides the memory-crosscutting parallel articulate cleanly.
- `rg -l -i "control surface" kb/notes/` — llm-mediated-schedulers, subtasks-that-need-different-tools, tool-loop-optional (all about the scheduler surface; already covered by agent-runtimes-decompose grounding).
- `rg -l -i "drift" kb/notes/` and `rg -l -i "content.?hash|content.address"` — content-hash appears only in this note and llm-recompute-cost; drift appears widely. The drift-oracle claim ("content-addressed comparison is a stronger drift oracle than timestamps") lands directly against link-graph-plus-timestamps.
- `rg -l -i "stale" kb/notes/` — link-graph-plus-timestamps, a-derived-copy, stale-indexes; drift/staleness thread confirmed.
- `rg -N '^description:' kb/reference/*.md | rg -i "review|storage|hash|valid"` — review-architecture.md, storage-architecture.md, agent-memory-coverage.md as evidence for the worked commonplace matrix.
- `rg -l -i "governance|control surface" kb/instructions/` — no hits; no instruction-side reverse edge.

**Link following:**
- From agent-memory-is-a-crosscutting-concern: it already grounds in agent-runtimes-decompose with a "runtime decomposition predicts this" section and an explicit "Memory is not a fourth component alongside these three" — mirror of the source's "governance should not be modeled as a fourth peer component." Confirms a sibling/parallel edge and a synthesis opportunity.
- From link-graph-plus-timestamps: its "Relationship to existing staleness work" and "make analogy" sections stake the timestamp oracle the source explicitly rates weaker than content-hash. a-derived-copy already carries a `contrasts` edge to link-graph on the same detection/verification distinction — the source is a third node on that thread but on a different axis (governance surface, not check price).

## Connections Found

- [agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) — **contrasts**: both argue a whole-system function is crosscutting rather than a fourth component beside scheduler / context engine / execution substrate — governance here, memory there — so a reader gains the neighbouring-shape distinction between the two crosscutting concerns over the same decomposition. (Target is `status: seedling`; `contrasts` is symmetric and additive, so no load-bearing flag.)
- [link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — **contrasts**: the source rates content-addressed comparison a stronger drift oracle than timestamps (a re-saved-unchanged file still looks modified; a clock-skewed edit looks untouched), while this note builds staleness detection on exactly the timestamp oracle — the reader wants the drift-oracle distinction between the two. (Target is `status: seedling`; `contrasts` is symmetric/additive, no load-bearing flag.)
- [review-architecture](../../../../reference/review-architecture.md) — **evidence**: the source's substrate/context-engine governance cells (link-health and uncommitted-state checks, targeted rewrites, review verdicts) are realized in the shipped Commonplace review subsystem; this doc corroborates that the substrate actually affords those diff/test/review operations. (Reference destination; `evidence` authorised.)

## Bidirectional Candidates

- [agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) <-> source — **contrasts**: `contrasts` is symmetric; the return link lets a reader at the memory note reach the governance sibling of the same "crosscutting, not a fourth component" pattern.
- [link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) <-> source — **contrasts**: symmetric; the return link warns a reader building timestamp-based staleness detection that content-hash is the stronger oracle the governance note prefers.

## Reverse-edge Candidates

- [review-architecture](../../../../reference/review-architecture.md) → source — a `see-also`/theory backlink from the shipped review-subsystem doc to this note would let a maintainer reading the architecture find the governance-control-surface theory it instantiates. Author only if `kb/reference/COLLECTION.md` authorises outbound theory links; connect does not edit it.
- [agent-memory-coverage](../../../../reference/agent-memory-coverage.md) → source — this doc maps shipped surfaces (control plane, validation, review, lifecycle) to requirements, i.e. the same governance operations the source's matrix crosses against structure; a backlink is plausible under reference's rules. Author-side decision.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [a derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — shares the content-hash/mechanical-comparison drift thread and already carries a `contrasts` edge to link-graph-plus-timestamps, but its claim is about enforce-or-omit for recomputable copies (validators, marks), a different level from the source's "which governance operations the substrate affords." Overlap is topical, not a load-bearing dependency either way.
- [enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) — about the missing recovery column in the enforcement gradient (a governance-"Correct" concern), but it develops the already-linked methodology-enforcement note, not the structure-affords-governance claim; too indirect to help traversal.
- [topology, isolation and verification form a causal chain for reliable execution](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — echoes "a supervisory/verification function is downstream of structural choices," but its chain is about decomposition→isolation→verification for execution reliability, a different partition than structure×governance; the analogy is real but not concrete enough for a reader to gain a specific handle.
- [system-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — touches the source's "governance hardens structure over time (findings crystallize into scripts/checks)" but that thread is already carried by the authored `extends` edge to methodology-enforcement-is-constraining; adds no distinct edge.
- Scheduler-surface cluster (llm-mediated-schedulers-are-a-degraded-variant, subtasks-that-need-different-tools-force-loop-exposure, llm-frameworks-should-keep-the-tool-loop-optional) — matched on "control surface," but they elaborate the scheduler component the source already reaches via its `grounds` edge to agent-runtimes-decompose; linking each would be redundant.

## Index Membership

- [computational-model-README](../../../../tags/computational-model-README.md) — the source fits the "Error Correction & Reliability" cluster (governance = validate/correct/detect-drift over the runtime) or a new governance line; a future writer could add a curated entry. README is not `complete`, so this is optional curation, not a completeness fix.
- [architecture-README](../../../../tags/architecture-README.md) — the source is tagged `architecture` and sits beside agent-runtimes-decompose in the structural-decomposition thread; a curated entry would place it there.

## Synthesis Opportunities

- A general note — "functions over a runtime crosscut its structural decomposition rather than forming peer components" — is implied by this source (governance) together with [agent memory is a crosscutting concern](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) (memory). Both derive from the same [scheduler / context engine / execution substrate](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) decomposition and both explicitly deny "fourth component" status. Do not author during connect; flag for a future writer.

## Maintenance Observations

None.

## Flags

- The source makes one primary assertion (structure affords/constrains governance) with a worked commonplace matrix; it is not a split candidate. No unresolved tensions surfaced.
