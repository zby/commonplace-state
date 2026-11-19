---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/design-for-the-first-time-human-except-on-access-cost.md"
source_has_frontmatter: true
date: "2026-06-10"
depth: standard
---

# Connection Report: Design for the first-time human, except on access cost

**Source:** [Design for the first-time human, except on access cost](../../notes/design-for-the-first-time-human-except-on-access-cost.md)

The source already carries six labelled outbound edges (context-efficiency, two-context-boundaries, feasibility-net-load, human-llm-differences, agents-navigate, homoiconic-medium). This run prospected `kb/notes/` only — the source's outbound section authorises notes, notes/definitions, reference/agent-memory/sources (evidence/derived-from/see-also), and rare see-also into instructions; `kb/work/` is excluded. The body offers no description/comparison of the shipped Commonplace system, an external source, or a procedure that a reference/agent-memory/sources/instructions edge could carry, so no candidates from those collections arose. The strongest unmet signal is in the closing paragraph, which names two further proxy-breaks but links only one.

## Discovery Trace

**Description listing scan:**
- `rg -l '^tags:.*\bdocument-system\b' kb/notes/ | xargs rg '^description:'` — 10 notes. Flagged: `human-llm-differences-...` (already linked, extends), `why-directories-despite-their-costs` (navigable scale — topical only). Rest are testing/type-system, off-topic.
- `rg -l '^tags:.*\bcontext-engineering\b' kb/notes/ | xargs rg '^description:'` — ~30 notes (mostly the `agent-memory-requirements/` cluster). Flagged: `evolving-understanding-needs-re-distillation-not-composition` (context-bound picture — adjacent but about distillation, not access mode). No new keeper.
- Neither `document-system-README.md` nor `context-engineering-README.md` declares `complete: true`, so the by-tag rg above was run for both tags (recorded, not skipped).

**Topic indexes:**
- `kb/notes/document-system-README.md` — points to `human-llm-differences` (already linked) and `why-directories`. No new keeper.
- `kb/notes/context-engineering-README.md` — core claims are scheduling/memory-system; none matches the access-mode/materialization argument directly.

**Body search:**
- `rg -li 'materializ'` — only the source, `human-llm-differences` (linked), `agent-memory-requirements/import-external-knowledge` (different sense). No new keeper.
- `rg -li 'single source of truth'` — source only.
- `rg -li 'sublinear|search interface|find-in-page'` — source + `human-llm-differences` only.
- `rg -li 'read text as|treat.*as instruction|prompt injection|inert'` — source, `homoiconic-medium` (linked, grounds), `llm-context-is-composed-without-scoping`, `agent-memory-needs-discoverable-composable-trusted-...`. Evaluated `composed-without-scoping`: it is the no-scoping consequence of the homoiconic medium, one hop past the edge the source already authors — adjacent, not a distinct premise the source needs. Rejected.
- `rg -li 'confabulat|hallucinat'` — source + `interpretation-errors-are-failures-of-the-interpreter`, `agentic-systems-interpret-underspecified-instructions`, three others off-topic. The first two ground the closing "confabulate where a human would ask" clause (see Connections Found).
- `rg -li 'read path|build-time|generated (index|listing)'` and `'dual-audience|rendered|browsable|published site'` — surfaced `index-curation-...`, `stale-indexes-...`, `frontloading-spares-execution-context`. Evaluated below; all rejected as topical-not-load-bearing.

**Link following:**
- From `human-llm-differences` (already linked): confirmed the reverse edge to the source already exists (line 76, `extends`); the source's return link is also present. No action.
- From `fix-what-the-executor-cant-determine-not-what-it-will`: already links to the source under `grounds` (competent-executor premise); the dependency runs fix→source, not source→fix. No new outbound candidate.
- From `interpretation-errors-...` → `agentic-systems-interpret-underspecified-instructions`: this pair is the underspecification/confabulation neighbourhood the source's closing clause gestures at but does not link.

## Connections Found

- [interpretation-errors-are-failures-of-the-interpreter](../../notes/interpretation-errors-are-failures-of-the-interpreter.md) — **grounds**: the closing paragraph asserts agents "confabulate where a human would ask"; this note names hallucination as an interpreter property (output outside any valid interpretation), grounding that second proxy-break. Target is `status: seedling`; `grounds` is load-bearing — flagged for the author.
- [agentic-systems-interpret-underspecified-instructions](../../notes/agentic-systems-interpret-underspecified-instructions.md) — **grounds**: the "confabulate where a human would ask" clause is the underspecification case — a human asks when the spec leaves a choice open, an agent fills it; this note is the canonical framing of that semantic-underspecification difference. Target is `status: current`, so the load-bearing label is unflagged.

## Bidirectional Candidates

None. The two grounds candidates above are premises the source consults; neither gains from a return link to a design heuristic it does not itself depend on.

## Reverse-edge Candidates

None outstanding. Inbound edges already exist and are correctly directed:
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → source (`extends`, already authored).
- [fix-what-the-executor-cant-determine-not-what-it-will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → source (`grounds`, already authored).
- Reference inbound (`rationale`) from `navigation.md`, ADR 025, ADR 026 — all already authored, correct inverse direction (the notes outbound section says note→reference/instructions edges are rare and usually inverse).

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — one hop past the already-authored `homoiconic-medium` edge; the no-scoping pathologies are downstream of the text-as-instruction point the source already grounds, not a distinct premise.
- [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) — keyword overlap on read-path/execution-context, but its lever is pre-computing *known* inputs and inserting results; the source's fix routes a single source of truth by access mode. Different mechanism; linking would blur two distinct moves.
- [index-curation-adds-orientation-that-generation-cannot-produce](../../notes/index-curation-adds-orientation-that-generation-cannot-produce.md) — about completeness-vs-orientation in indexes, a different axis from sublinear-vs-linear access. Shares the index example but not the claim.
- [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — about trust in index exhaustiveness; no access-mode dependency.
- [why-directories-despite-their-costs](../../notes/why-directories-despite-their-costs.md) — navigable-scale tradeoff; topical (document-system tag) but not the access-mode argument.

## Index Membership

- [document-system-README](../../notes/document-system-README.md) — the source carries `document-system` and is not listed; a future writer could place it under a "Materialization / dual-audience" grouping near `human-llm-differences`. Connect does not author the entry.
- [context-engineering-README](../../notes/context-engineering-README.md) — the source carries `context-engineering` and is absent from this curated head; a Core-Claims entry would fit the routing/loading theme. Future-writer action.

## Synthesis Opportunities

None new. The source already is the synthesis that sharpens `human-llm-differences`'s navigation row.

## Maintenance Observations

- Neither `document-system-README.md` nor `context-engineering-README.md` lists this source despite its matching tags; both are curated (non-`complete`) heads, so this is allowed lag, not a validation error. Noted under Index Membership for a future curation pass.
- The closing paragraph names two proxy-breaks (text-as-instruction, confabulation) symmetrically but links only the first (`homoiconic-medium`). Authoring the two `grounds` edges above would make the closing parallel structurally complete.

## Flags

- Not a split candidate: the source makes one assertion (access-mode is the sharp, structurally-fixable proxy-break) with a bounded set of exceptions; the closing exceptions are scoped as out-of-claim, so it stays single-claim despite linking to five-plus notes.
- Two load-bearing `grounds` candidates; one target (`interpretation-errors-...`) is `status: seedling` — flagged per the connect-report rule for load-bearing labels onto seedlings.
