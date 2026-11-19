---
description: "Candidate connections for aide-agent-implementation-60b3978"
type: types/connect-report.md
source: kb/sources/aide-agent-implementation-60b3978.ingest.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: aide-agent-implementation-60b3978

**Source:** [AIDE agent.py at 60b3978ddf65b71f86eb7c64506965048a1398cf](../../../../sources/aide-agent-implementation-60b3978.ingest.md)

## Discovery Trace

- Post-ingest pass: read the accepted agent and journal ingests fully and reran `rg -n 'generate_summary|node.analysis|debugging|Consumption|Iteration'` over both and the storage/activation note. Evaluated the actual call sites against the journal's summary projection at the same commit. The pair supports a static analysis-to-summary-to-prompt route; neither supplies realized model criticisms or causal uptake results. Shared collection prospecting is retained below.

- Read sources/COLLECTION.md and the connect-report type. Read the source fully, the curated README of notes, reference, agent-memory-systems, agentic-systems, tags, and sources; generated a fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`.
- Description scan: `rg -n '^description:.*(theory|critic|compounding|oracle|conjectur|AIDE|research|hypothes|eval)'` across notes, reference, agent-memory-systems, agentic-systems and sources. Body searches: `rg -n 'AIDE|Weco|solution tree|content-directed|fixed.search'` across those collections; `rg -n 'proxy|hypothes|conjectur|parameter'` on the fixed-decomposition and exact-implementation notes. Read retained candidates in full and followed their linked theory-builder, compounding, experimental-contrast and storage/activation distinctions where relevant.
- Notes supplied the direct conceptual matches below; sources and agentic-systems supplied AIDE2's retained analysis and review. Reference README and search results concern Commonplace-specific machinery, with no direct implementation connection. Agent-memory-system indexes suggested generic retained-memory parallels, rejected in favor of the direct storage/activation claim. Tags were used for routing through theory-builder and self-improving-systems heads, not proposed as outbound targets because sources has no authorized label to tags.
- Read the user-named article and articles/COLLECTION.md for the reverse evidence path. Its source-grounding bound is relevant to future edits. External prospecting skipped: only the supplied canonical source and already-known linked sources are in scope. Instructions and work are excluded destinations.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **compares-with**: Draft and improve load generated summaries, while debug loads parent code and execution output; distinguish actual supplied inputs from stored fields.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **defined-in**: Feedback requests, atomic-change instructions and metric ranking let a reviewer inspect the criticism condition without treating a schema as a realized trace.
- [Disconnected witnesses do not establish a full causal path through theory](../../../../notes/disconnected-witnesses-do-not-establish-a-causal-path-through-theory.md) — **compares-with**: The static execution-to-analysis-to-next-prompt path narrows which joins can be reconstructed and which require observed LLM outputs.

- [AIDE journal implementation](../../../../sources/aide-journal-implementation-60b3978.ingest.md) — **see-also**: supplies the exact summary body behind the agent's generate_summary calls at the same pinned commit. Together the files identify which plans, analyses and scores reach draft/improve prompts.

## Bidirectional Candidates

- [AIDE journal implementation](../../../../sources/aide-journal-implementation-60b3978.ingest.md) → this ingest — **see-also**: the journal defines retained fields and their projection; readers need the agent call sites to establish when that projection is actually loaded. This independently serves the storage-to-consumption question.

## Reverse-edge Candidates

- [Which Existing Self-Improving Systems Are Theory Builders](../../../../articles/which-existing-self-improving-systems-are-theory-builders.md) → paired ingest — **evidenced-by**: supplies this source's bounded contribution to a prospective Weco/AIDE case. Keep the criticism verdict open; documentation, source code, conceptual criteria and measured outcomes answer different questions.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

Generic memory-store implementations: no specific mechanism comparison beyond the more direct note retained above.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

One complete file at a fixed repository commit; no imports or runtime execution are included in the primary capture. Do not attribute this current file to the paper's historical evaluation revision.
