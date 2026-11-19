---
description: "Discovery report for possible KB connections from the Darwin Gödel Machine paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Darwin Gödel Machine

**Source:** [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.md)

The authored surface now exists at [Ingest: Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md). This report evaluates the KB after the ingest's recommended promotion was carried out.

## Discovery Trace

**Collection contract:**

- Read `kb/sources/COLLECTION.md`. The snapshot is immutable; its ingest is the authored outbound surface. Authorised local destinations are notes, reference, sources, agent-memory systems, and agentic systems. Work and instructions are excluded.

**Curated heads and comparison surfaces:**

- Read `kb/notes/self-improving-systems-README.md`, `kb/agentic-systems/README.md`, `kb/agentic-systems/COLLECTION.md`, `kb/agent-memory-systems/README.md`, `kb/agent-memory-systems/COLLECTION.md`, and `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`.
- `kb/notes/self-improving-systems-README.md` is selective and has no `complete: true` mark, so the note-title and body passes were not skipped.
- Read the DGM ingest, the two notes that now place DGM, the Gödel-machine comparison note, and the HGM ingest.

**Title and description listings:**

- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`
- `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`
- `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`
- `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.ingest.md'`
- `rg -n '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' | rg -i 'self-improv|self-modif|harness|trace|archive|evolution|oracle|selection|retention|lineage|benchmark|reflective'`

**Body searches:**

- `rg -n -i 'Darwin Gödel|Darwin G[oö]del|\\bDGM\\b|2505\\.22954' kb --glob '*.md'` — confirmed that DGM is now linked from the pathway-profile casebook, the per-function casebook, and the reflective-self-improvement article. HGM still names DGM only as unlinked prose.
- `rg -n -i 'archive|parent selection|viability|stepping stone|selection-target|immediate score|trace-to-executable|executable harness' ...` — kept HGM and the trace-learning comparison; rejected generic archive and benchmark matches.
- `rg -n -i '\\beight\\b|\\bfour cases\\b|\\bfour systems\\b|\\bninth\\b'` over the DGM cluster — found stale case counts in the curated head, the pathway-profile casebook, and one footer in the per-function casebook.
- `rg -n -i 'Darwin|\\bDGM\\b'` over the agentic-systems index and trace-learning comparison — no DGM entry exists in either surface.

**Link following:**

- From [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) to the DGM ingest: the requested fifth case is present and correctly distinguishes viability admission from score-weighted reproduction.
- From [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) to the DGM ingest: the placement row and evidence footer are present.
- From [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) to its “Acceptance evidence varies across systems” section: DGM is the missing empirical middle case between the proof gate and HGM's lineage estimator.
- From [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) to its summary and limitations: DGM is a load-bearing baseline but is not linked to the local ingest.

## Connections Found

None. The DGM ingest already carries the strongest justified outbound links: the two self-improvement casebooks, proposal-selection, Gödel machines, accumulation/compounding, oracle-boundary notes, and HGM. Adding more source-side links would duplicate existing traversal.

## Bidirectional Candidates

- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) ↔ DGM ingest — **compares-with**: DGM already links to HGM; the return path is independently useful because HGM's central experiment evaluates DGM's immediate-score parent-selection signal.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) ↔ DGM ingest — **evidenced-by** from the note side: the note's acceptance-evidence comparison currently jumps from proof-gated Gödel machines to HGM, omitting the system that explicitly relaxed proof to empirical viability and score-weighted reproduction.

## Reverse-edge Candidates

- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) → [DGM ingest](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) — **compares-with**: resolve the repeatedly named DGM baseline to the primary local analysis.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) → [DGM ingest](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) — **evidenced-by**: add DGM to “Acceptance evidence varies across systems” as the declared proof-to-empirical departure.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) → [DGM ingest](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) — **evidenced-by**: DGM is a distinct trajectory-run pattern in which evaluation logs drive executable harness mutation and every viable child enters a monotonic archive. Prefer adding this after inspecting the released code; otherwise mark it explicitly as paper-grounded.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) as a direct DGM entry — the head indexes theoretical notes, not individual paper ingests. Its existing Placements pointer already reaches the casebook containing DGM; only the stale count needs repair.
- [Agentic Systems](../../../../agentic-systems/README.md) as a direct source entry — the index lists per-system analyses, not ingests. DGM belongs there only after a `kb/agentic-systems/darwin-godel-machine.md` analysis exists.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — useful experimental context, but HGM is the cleaner controlled comparison on DGM's selection mechanism and is enough for present navigation.
- Agent-memory system reviews — DGM retains executable agents rather than memory items; the cross-system trace-learning analysis is the narrower fit.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) — no new DGM entry; update “Eight cases” to “Thirteen cases” so the curated head accurately describes the casebook it already links.
- [Agentic Systems](../../../../agentic-systems/README.md) — eventual membership through a dedicated whole-system analysis grounded in the released DGM code, not through the paper ingest itself.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — candidate comparison membership as a trace-to-executable-harness, monotonic-archive variant; code inspection would put it on the same evidence footing as Meta-Harness and Agentic Harness Engineering.

## Synthesis Opportunities

- DGM and HGM jointly imply that archive retention and parent-selection targets are separate design decisions: retaining low-scoring stepping stones preserves reachability, while allocating expansion compute requires evidence about descendant productivity. The current notes describe both mechanisms but do not state the separation as a transferable claim.

## Maintenance Observations

- `kb/notes/self-improving-systems-README.md` says “Eight cases” although the linked casebook now has thirteen rows.
- `kb/notes/real-self-improving-systems-occupy-combinations-no-rung-captures.md` still says “a scale over these eight” although its frontmatter and table now say thirteen.
- `kb/notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md` has a footer saying “all four systems lack” retirement, while the body now analyzes five and distinguishes DGM's deliberate non-retirement.
- The DGM ingest's Recommended Next Action is complete but still written as pending. That is harmless source-analysis history, but a status marker would prevent repeated work if ingest reports are treated as live task surfaces.
- `kb/agentic-systems/README.md` and a new Compound Engineering analysis are currently modified/untracked by another workstream; no library files were changed during this connect run.

## Flags

- The paper-level placement is complete. The only material coverage gap is code-grounded whole-system analysis; it could revise the current paper-derived actor allocation, viability, and archive-policy readings.
