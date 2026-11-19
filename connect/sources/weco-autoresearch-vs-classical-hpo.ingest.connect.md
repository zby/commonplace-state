---
description: "Candidate connections for weco-autoresearch-vs-classical-hpo"
type: types/connect-report.md
source: kb/sources/weco-autoresearch-vs-classical-hpo.ingest.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: weco-autoresearch-vs-classical-hpo

**Source:** [AutoResearch vs Classical Hyperparameter Tuning](../../../../sources/weco-autoresearch-vs-classical-hpo.ingest.md)

## Discovery Trace

- Post-ingest pass: read the accepted report in full and reran `rg -n '^description:|generate_summary|Memory|Optuna|numeric' kb/sources/weco-*.ingest.md kb/sources/aide-*.ingest.md`. Read the accepted companion reports and re-evaluated each candidate against the actual capture boundary. Shared collection-wide prospecting is recorded below.

- Read sources/COLLECTION.md and the connect-report type. Read the source fully, the curated README of notes, reference, agent-memory-systems, agentic-systems, tags, and sources; generated a fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`.
- Description scan: `rg -n '^description:.*(theory|critic|compounding|oracle|conjectur|AIDE|research|hypothes|eval)'` across notes, reference, agent-memory-systems, agentic-systems and sources. Body searches: `rg -n 'AIDE|Weco|solution tree|content-directed|fixed.search'` across those collections; `rg -n 'proxy|hypothes|conjectur|parameter'` on the fixed-decomposition and exact-implementation notes. Read retained candidates in full and followed their linked theory-builder, compounding, experimental-contrast and storage/activation distinctions where relevant.
- Notes supplied the direct conceptual matches below; sources and agentic-systems supplied AIDE2's retained analysis and review. Reference README and search results concern Commonplace-specific machinery, with no direct implementation connection. Agent-memory-system indexes suggested generic retained-memory parallels, rejected in favor of the direct storage/activation claim. Tags were used for routing through theory-builder and self-improving-systems heads, not proposed as outbound targets because sources has no authorized label to tags.
- Read the user-named article and articles/COLLECTION.md for the reverse evidence path. Its source-grounding bound is relevant to future edits. External prospecting skipped: only the supplied canonical source and already-known linked sources are in scope. Instructions and work are excluded destinations.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: The 16-knob Optuna space excludes numeric and structural edits that the agent can introduce; identify the actual effective search boundary.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: The agent/Optuna comparison bundles proposal method with editable search space and treats one observed seed as a natural control.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **defined-in**: Inventing edits outside an initial parameter list does not alone settle whether revision is guided by criticism of stated content.

- [AIDE paper](../../../../sources/aide-ai-driven-exploration-space-of-code.ingest.md) — **compares-with**: compares the architecture of code-space search with Weco's separate AutoResearch/Optuna experiment; do not attribute that experiment to AIDE or AIDE2.

## Bidirectional Candidates

None

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

Source capture is textual; inspect capture_scope before relying on graphics. No runtime experiments were performed.
