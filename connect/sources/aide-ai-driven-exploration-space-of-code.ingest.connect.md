---
description: "Candidate connections for AIDE's solution-tree search and retained experiment feedback"
type: types/connect-report.md
source: kb/sources/aide-ai-driven-exploration-space-of-code.ingest.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: AIDE

**Source:** [AIDE](../../../../sources/aide-ai-driven-exploration-space-of-code.ingest.md)

## Discovery Trace

- Post-ingest pass: read the accepted report in full and reran `rg -n '^description:.*(AIDE|Weco)|AIDE|ignition'` over the new AIDE ingest, existing AIDE2 ingest/review, the user-named article and later-improvement test note. Re-evaluated the candidates below against the report's explicit uncertainty about the criticism pathway. Shared collection prospecting from this batch remains applicable; no library links were authored.

- Read the source, sources collection contract, and connect-report type. Read the curated README for notes, reference, agent-memory-systems, agentic-systems, tags, and sources; generated their complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`.
- Scanned descriptions with `rg -n '^description:.*(theory|critic|compounding|oracle|conjectur|AIDE|research|hypothes|eval)'` over those destination collections except tags. Focused body search: `rg -n 'AIDE|Weco|solution tree|content-directed|fixed.search'` over the same destinations. AIDE2 was the direct system and source match; reference architecture was too Commonplace-specific; historical memory reviews lacked a comparably direct lineage connection.
- Read theory-builder and self-improving-systems tag heads and followed the theory-builder definition and its criticism boundary. Read the AIDE2 review, accumulation/compounding note, and disconnected-witnesses note. The article named by the user resolves under articles, not notes; read it and its collection contract for the reverse edge.
- Tags supply navigation but sources authorize no outbound label to tags; no tag edge proposed. External prospecting skipped; canonical arXiv source is already supplied. Instructions and work are excluded destinations.

## Connections Found

- [Theory builder](../../../../notes/definitions/theory-builder.md) — **defined-in**: supplies the distinction between stated criticism and selecting code variants by score, needed when interpreting the plan and feedback machinery.
- [AIDE2 paper ingest](../../../../sources/aide2-recursive-self-improvement-research-agents.ingest.md) — **compares-with**: compares task-code tree search with the later outer loop that searches research-agent harnesses.
- [AIDE2 review](../../../../agentic-systems/reviews-archive/aide2.md) — **compares-with**: identifies what changes when the object optimized is the research agent itself.
- [Disconnected witnesses do not establish a full causal path through theory](../../../../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) — **compares-with**: AIDE's plans, summaries and execution feedback name concrete joins to inspect without inferring content-directed criticism from storage alone.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Which Existing Self-Improving Systems Are Theory Builders](../../../../articles/which-existing-self-improving-systems-are-theory-builders.md) → the paired ingest — **evidenced-by**: a prospective AIDE/Weco case needs the original tree-search mechanism before judging the later self-improver. This supplies a bounded implementation description, not a classification verdict. Article rules permit this evidence link; its source grounding bound must be considered when editing.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md): less direct than the theory-builder boundary for this architecture ingest; avoid a general evaluation link based only on numeric scoring.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The user's paper title differs from the captured v1 title. Preserve the actual title. Membership in the theory-builder class remains a later evidential judgment.
