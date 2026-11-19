---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/agent-memory-systems/reviews/ReframeWeb.md"
source_has_frontmatter: true
date: "2026-07-07"
depth: standard
---

# Connection Report: ReframeWeb

**Source:** [ReframeWeb](../../../../agent-memory-systems/reviews/ReframeWeb.md)

The source is a code-grounded `agent-memory-system-review`. It already carries a rich `Relevant Notes` block (9 outbound edges to `kb/notes/` definitions and theory notes), so outbound-to-notes is largely satisfied; the open work is within-collection `compares-with` edges on ReframeWeb's distinctive axes and reverse edges from theory notes that maintain `evidence:` example lists. Per the source `COLLECTION.md`, links into `kb/notes/` "usually run inverse (theory links in)."

## Discovery Trace

**Description listing scan:**
- `rg '^description:' kb/agent-memory-systems/` (full roster, 141 code-grounded reviews + lightweight) — used to size the landscape and locate root-level analyses (`agentic-memory-systems-comparative-review.md`, `systems-table.md`, `trace-derived-learning-techniques-in-related-systems.md`, `review-framework-design.md`, `thalo-type-comparison.md`).
- `rg '^description:' kb/agentic-systems/` — 4 whole-harness analyses (claude-code-dynamic-workflows, fractal, gbrain, semantic-engine). None center on ReframeWeb's memory axes; the source review explicitly scopes out the voice pipeline, so no `→ kb/agentic-systems/` candidate. Skipped that destination.

**Topic indexes:**
- Read `kb/agent-memory-systems/README.md` — confirms the review vocabulary (four-field record, read-back direction/signal, faithfulness) and that `systems.csv` / `systems-table.md` are machine-generated from `reviews/` (not hand-authored, so not an authoring target).
- Read `kb/agent-memory-systems/COLLECTION.md` outbound section — authorised labels per destination captured below.

**Body search (ReframeWeb's distinctive axes, not the standard review sections):**
- Standard-section terms (`recency`, `read-back: push`, `curation operations none`, `faithfulness tested no`) each matched 50–130 reviews — too broad for `compares-with`, which needs a shared *distinctive* axis. Rejected as candidate-generators.
- `rg -i 'shallow tree|graph.*only.*scop|not graph reasoning|no multi-hop|relational.*identical'` over `reviews/` → **graphiti**, ReframeWeb. graphiti is the genuine-graph counterpart.
- `rg -i 'two-stage.*retriev|hint.*breadth|LLM-planned|planned retrieval'` → **siftly**, ReframeWeb. siftly's own review flags the same precision-or-silence failure.
- `rg -i 'anti-repetition|recently.read|reads mutate|read_at|read.*side.effect'` → Agent-S, agent-workflow-memory, **reasoning-bank**, spacebot, tendril, Auto-claude-...-sleep. On inspection only **reasoning-bank** shares the "retrieval mutates the store" axis (appends the task embedding on every retrieval); Agent-S is write-side dedup, the others matched on stale-push "suppression rules," a different mechanism.
- `rg -i 'few-shot|example pool|per-stage|per-decision'` → **expel**, g-memory, meta-harness. expel is the clearest "few-shot examples as retrievable, steering memory" counterpart; g-memory/meta-harness inject few-shots but without ReframeWeb's dedicated per-stage pool framing.
- `rg -i 'side-effect-free|pure read|recency|freshness'` over `kb/notes/` → surfaced **many-to-many-edge-state-is-where-files-yield-to-a-database** (files-vs-database boundary the review's Comparison invokes). No note on read-purity / side-effect-free reads exists.

**Link following:**
- `symbolic-context-engineering-is-bounded-by-symbol-availability.md` (already linked from the review) maintains an explicit `evidence:` list citing CrewAI, REM, EQUIPA, cq, Binder — a pattern of reviews-as-evidence with no ReframeWeb entry yet. Same for `knowledge-storage-does-not-imply-contextual-activation.md` (evidence list of ingests/tweets). These are the reverse-edge openings.
- `rg -l 'ReframeWeb' kb/` → only `systems-table.md` (generated) references the review; no note or peer review backlinks it, so reverse-edge and bidirectional slots are open.

## Connections Found

- [graphiti](../../../../agent-memory-systems/reviews/graphiti.md) -- **compares-with**: both classify their storage substrate as `graph`, but ReframeWeb's "graph memory" is a shallow root→child tree that (its own Curiosity Pass admits) a relational store would serve identically, whereas Graphiti actually exploits graph structure — BFS expansion, communities, multi-hop, hybrid BM25+embedding+traversal. Following the link, an agent comparing graph-substrate memory sees a nominal graph and a genuine one on the same axis: does a graph substrate earn its keep?
- [siftly](../../../../agent-memory-systems/reviews/siftly.md) -- **compares-with**: both run two-stage retrieval — a lexical/structured candidate narrowing (ReframeWeb: LLM-emitted tag/substring hints + per-domain recency breadth; Siftly: FTS5 + category-intent regex + keywords) followed by an LLM rerank/prune — and both carry the identical precision-or-silence failure, where a hard miss in candidate selection prevents the LLM stage from ever seeing a relevant item.
- [reasoning-bank](../../../../agent-memory-systems/reviews/reasoning-bank.md) -- **compares-with**: both break read-purity by giving retrieval a store-mutating side effect — ReframeWeb stamps `read_at` on served nodes to suppress repeats (anti-repetition/freshness), reasoning-bank appends the current task embedding to its cache on every retrieval (a side-effect log). Shared distinctive axis: retrieval is not side-effect-free, against the common design where reads are pure.
- [expel](../../../../agent-memory-systems/reviews/expel.md) -- **compares-with**: both treat a pool of few-shot examples as retrievable memory that steers LLM decisions; ExpeL wires the writer (distills successful trajectories into the few-shot slot via a FAISS store), while ReframeWeb ships five per-stage example pools with no production writer — the wired-vs-scaffolding contrast on "few-shot examples as an adaptation surface."
- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) -- **rationale** (low-confidence; usual direction is inverse — see Reverse-edge Candidates): the note supplies the files-vs-database theory the review's "Comparison with Our System" invokes ("the database costs diffability… buys typed relation traversal"). A reader of the Comparison paragraph gains the structural criterion (churning ownerless many-to-many edge) that decides when a store is warranted. The sharper edge is the reverse one (the review is an evidence instance for the note), so prefer authoring that unless a `rationale` pointer is wanted on the review side.

## Bidirectional Candidates

- [graphiti](../../../../agent-memory-systems/reviews/graphiti.md) <-> source -- **compares-with**: `compares-with` reads both ways; Graphiti's review would gain the nominal-graph foil (a system whose graph substrate buys only traversal scoping) on the same "does the graph earn its keep" axis.
- [siftly](../../../../agent-memory-systems/reviews/siftly.md) <-> source -- **compares-with**: Siftly's review already names the precision-or-silence risk of two-stage lexical-then-LLM retrieval; a return link to ReframeWeb supplies a second instance of the same pattern.

## Reverse-edge Candidates

- [symbolic-context-engineering-is-bounded-by-symbol-availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) → source -- **evidence**: the note maintains an `evidence:` example list (CrewAI, REM, EQUIPA, cq, Binder) and the review already links *to* the note. ReframeWeb is a purer case than any listed — symbolic-only push with no semantic ranking at all, where empty positive hints match nothing (test-confirmed `test_empty_positive_hints_do_not_match_historic_candidates`), i.e. the bound at its limit. The note author (or a future connect on the note) should add ReframeWeb to that evidence list.
- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidence**: the note's `evidence:` list is mostly ingests/tweets; ReframeWeb is a clean code-grounded instance of stored-but-unverified activation — it pushes memory into every turn yet runs no with/without-memory ablation (`Faithfulness tested: no`), the exact gap the note names between read-back and activation.
- [many-to-many-edge-state-is-where-files-yield-to-a-database](../../../../notes/many-to-many-edge-state-is-where-files-yield-to-a-database.md) → source -- **evidence**: ReframeWeb instantiates the note's boundary from the "store not structurally required" side — it adopted a graph database whose edges are a churn-free shallow tree (parent links, static `contains`/`has_message` relations), exactly the note's "a many-to-many edge without churn → links / churn without a many-to-many edge → regenerate" case where files/tree would suffice.

## Off-authorisation Candidates

None. Every surfaced candidate fits an authorised label for its source→destination pair (`compares-with` and `see-also` within-collection; `rationale`/`evidence` to `kb/notes/`).

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- Agent-S, spacebot, tendril, agent-workflow-memory -- surfaced on `suppression`/`recently-read` search but reject: Agent-S "suppresses repeat writes" is write-side dedup; the others' "suppression rules/path" are about stale *pushes*, none share ReframeWeb's read-stamping-mutates-store mechanism.
- The 50–130-review hits on `read-back: push`, `Curation operations: none`, and `Faithfulness tested: no` -- rejected as connection candidates: these are standard review sections present in most systems, not a distinctive shared axis; keeping them would be keyword-only "related" links that do not help traversal.
- g-memory, meta-harness -- inject few-shot examples but lack ReframeWeb's dedicated per-stage example-pool framing; expel is the sharper single `compares-with` for that axis, so these are not surfaced to avoid a low-value spray.
- `systems-table.md` / `systems.csv` -- already reference ReframeWeb but are machine-generated from `reviews/`; not an authoring target.

## Index Membership

- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) -- the 141-row synthesis (whose thesis includes "push is rarely behavior-tested" and "full lifecycle curation is rare"); ReframeWeb is a textbook double instance (push read-back + `Faithfulness tested: no` + `Curation operations: none`) a future revision of the synthesis could cite as an example.
- [trace-derived-learning-techniques-in-related-systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) -- ReframeWeb's per-stage few-shot pools are a *not-yet* trace-derived case (scaffolding present, no production writer); the review's "What to Watch" flags that wiring the writer would require re-tagging it `trace-derived`. A near-miss worth naming in that analysis.

## Synthesis Opportunities

There is no note on **retrieval side effects / read-purity as a design axis**, yet ReframeWeb (read-stamping to suppress repeats) and reasoning-bank (retrieval appends an embedding) both break the "reads are pure" default the ReframeWeb review calls out as a Commonplace commitment. Two reviews is thin for a note today; recorded as a watch item, not a promotion.

## Maintenance Observations

- The review is well-connected outbound to `kb/notes/` (9 `Relevant Notes` edges) but no note or peer review backlinks it (only the generated `systems-table.md`). The value gap is the three reverse edges above, since the collection contract makes note→review the primary direction.
- Two theory notes cited by the review (`symbolic-context-engineering-is-bounded-by-symbol-availability`, `knowledge-storage-does-not-imply-contextual-activation`) maintain hand-curated `evidence:` example lists; ReframeWeb is a stronger/cleaner instance than several already listed, so these lists are the concrete promotion target for a later maintenance pass.

## Flags

None. No split candidate (the review is a single-system descriptive artifact), no unresolved tension, and genuine connections were found.
