---
description: "Candidate connections for weco-how-to-build-good-eval"
type: types/connect-report.md
source: kb/sources/weco-how-to-build-good-eval.ingest.md
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: weco-how-to-build-good-eval

**Source:** [How to Build a Good Eval](../../../../sources/weco-how-to-build-good-eval.ingest.md)

## Discovery Trace

- Post-ingest pass: read this accepted ingest fully and reran `rg -n '^description:|^## Recommended Next Action' kb/sources/weco-*.ingest.md` and `rg -n 'compounding|critic|hypothes' kb/articles/which-existing-self-improving-systems-are-theory-builders.md`. Re-evaluated earlier candidates against the report's source and inference boundaries, and read the other accepted Weco reports to evaluate the companion link below. Shared full collection prospecting is recorded below.

- Read sources/COLLECTION.md and the connect-report type. Read the source fully, the curated README of notes, reference, agent-memory-systems, agentic-systems, tags, and sources; generated a fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`.
- Description scan: `rg -n '^description:.*(theory|critic|compounding|oracle|conjectur|AIDE|research|hypothes|eval)'` across notes, reference, agent-memory-systems, agentic-systems and sources. Body searches: `rg -n 'AIDE|Weco|solution tree|content-directed|fixed.search'` across those collections; `rg -n 'proxy|hypothes|conjectur|parameter'` on the fixed-decomposition and exact-implementation notes. Read retained candidates in full and followed their linked theory-builder, compounding, experimental-contrast and storage/activation distinctions where relevant.
- Notes supplied the direct conceptual matches below; sources and agentic-systems supplied AIDE2's retained analysis and review. Reference README and search results concern Commonplace-specific machinery, with no direct implementation connection. Agent-memory-system indexes suggested generic retained-memory parallels, rejected in favor of the direct storage/activation claim. Tags were used for routing through theory-builder and self-improving-systems heads, not proposed as outbound targets because sources has no authorized label to tags.
- Read the user-named article and articles/COLLECTION.md for the reverse evidence path. Its source-grounding bound is relevant to future edits. External prospecting skipped: only the supplied canonical source and already-known linked sources are in scope. Instructions and work are excluded destinations.

## Connections Found

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — **compares-with**: Fidelity, discriminating signal and cost separate weaknesses that a single benchmark score can hide.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **compares-with**: A high score with dissatisfied users questions the proxy-to-objective link even when the evaluation script implements its stated metric.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **compares-with**: The human recommendation to criticize evaluator assumptions does not by itself establish that Weco's automated loop performs that criticism.

- [First Evidence](../../../../sources/weco-first-evidence-recursive-self-improvement.ingest.md) — **compares-with**: compares general advice to revise faulty evaluation assumptions with a particular reported evaluator repair, without treating advice as evidence of automated execution.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Which Existing Self-Improving Systems Are Theory Builders](../../../../articles/which-existing-self-improving-systems-are-theory-builders.md) → paired ingest — **evidenced-by**: supplies this source's bounded contribution to a prospective Weco/AIDE case. Keep the criticism verdict open; documentation, source code, conceptual criteria and measured outcomes answer different questions. The author's evaluation philosophy is evidence of a stated position, not of automated implementation.

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
