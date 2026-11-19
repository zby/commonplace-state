---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md"
source_has_frontmatter: true
date: "2026-06-03"
depth: standard
---

# Connection Report: Symbolic context engineering is bounded by symbol availability

**Source:** [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md)

The source is a `structured-claim` seedling. It already authors four notes-internal links (`knowledge-storage-does-not-imply-contextual-activation`, `agent-statelessness-means-the-context-engine-should-inject-context`, `codification`, `frontloading-spares-execution-context`). The conspicuous gap: its Evidence section names four external systems — CrewAI's LiteAgent, EQUIPA, cq, Binder — but authors **no** `evidence`/`derived-from` edges into `kb/agent-memory-systems/`, which is exactly where those reviews live and exactly the destination the source COLLECTION authorises for corroborating observations. That is the main payload of this report.

## Discovery Trace

**Index scan:**
- Read [notes dir-index](../../../notes/dir-index.md) — flagged candidates by title/description: `agent-statelessness-makes-routing-architectural-not-learned` (source already links its sibling injection note; the routing note is cited inline but not in footer), `in-context-learning-presupposes-context-engineering` (selection machinery), `pointer-design-tradeoffs-in-progressive-disclosure` (query-time vs fixed pointers), `access-burden-and-transformation-burden-are-distinct-query-dimensions` (specification-sensitive symbolic-vs-semantic routing), `always-loaded-context-mechanisms-in-agent-harnesses` (already cited), `session-history-should-not-be-the-default-next-context` (loaded-state carryover).
- Read [agent-memory-systems dir-index](../../../agent-memory-systems/dir-index.md) and [reviews dir-index](../../../agent-memory-systems/reviews/dir-index.md) — flagged the four named systems plus the comparative review.
- Read [reference dir-index](../../../reference/dir-index.md) — `navigation.md`, `agent-memory-coverage.md`, `control-plane-goals.md` scanned; none corroborate the symbol-availability claim specifically (they describe the shipped system, not the push/pull regime distinction).

**Topic indexes:**
- Source carries empty `tags: []`, so no tag-index traversal was possible. (See Maintenance Observations.)

**Body search:**
- `rg -li "equipa|liteagent|crewai"` over agent-memory/reference/sources — confirmed current review files `equipa.md`, `crewai-memory.md` exist (non-`.replaced`).
- `rg -li "\bbinder\b|\bcq\b"` — confirmed current `cq.md`, `binder.md`.
- `rg -n "anticipat|push|read-back|rerank|vector|semantic"` in `equipa.md` — confirmed: "From the acting agent's perspective, this is push activation"; relevance selection "combines symbolic filters, recency, Q-values, keyword overlap, optional embeddings, and optional graph reranking"; `Read-back: push`; `tags: [push-activation]`. Directly substantiates the source's claim that EQUIPA's anticipatory surfacing is semantic, not symbolic.
- `rg` in `crewai-memory.md` — confirmed: LiteAgent "injects recalled memories into the next LLM call"; recall "combines vector search with scopes, recency, importance, and optional LLM query analysis"; `tags: [push-activation]`. Substantiates the LiteAgent example.
- `rg` in `cq.md` — confirmed: `Read-back: pull`; "Stored cq knowledge reaches an agent when the agent or skill-guided workflow deliberately calls `query`". Substantiates the pull-oriented half of the Evidence bullet.
- `rg` in `binder.md` (via dir-index description) — local-first typed knowledge graph with "CLI/MCP/LSP access, and agent-facing skills" — a pull/tool interface, matching the source's "expose structured search tools" framing.
- `rg -n "push|pull|symbolic|semantic"` in `agentic-memory-systems-comparative-review.md` — found the navigability-vs-retrieval split and the search-vs-navigate theory of knowledge access, which is adjacent but frames *link structure*, not the *symbol-availability boundary on routing*. Kept as a weaker candidate (see Rejected / Synthesis).

**Link following:**
- From `agent-statelessness-makes-routing-architectural-not-learned` (the [stateless agent] inline anchor in the source's Reasoning section): its footer cites `instruction-specificity-should-match-loading-frequency`, `context-efficiency-is-the-central-design-concern`, `frontloading-spares-execution-context`. Confirms the source is sitting in the routing-architecture cluster; the routing note is a `mechanism`/`grounds`-grade neighbour the source leans on but does not footer-cite.
- From `access-burden-and-transformation-burden-are-distinct-query-dimensions`: links to `scheduler-llm-separation` and `bounded-context-orchestration-model` — the specification-sensitive symbolic-versus-semantic routing cluster. The source's closing dichotomy (route reliably once a symbol exists vs infer the symbol when none does) is a routing-stage instance of that same split.

## Connections Found

- [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — **evidence**: the comparative review's navigability-vs-retrieval finding (Mem0/Graphiti/Cognee "search for" knowledge via vector/graph/BM25; commonplace "navigates" via links) corroborates the source's claim that anticipatory surfacing is the semantic regime, not symbolic routing. Load-bearing-label note: target is a `note` (status not seedling), so `evidence` is additive and safe.
- [equipa](../../../../agent-memory-systems/reviews/equipa.md) — **evidence**: EQUIPA's `push` read-back with relevance blended from embeddings, keyword overlap, Q-values, and graph reranking is a concrete instance of the source's "anticipatory push systems are semantic, not symbolic" Evidence bullet. The note already names EQUIPA in prose but authors no edge.
- [crewai-memory](../../../../agent-memory-systems/reviews/crewai-memory.md) — **evidence**: CrewAI's LiteAgent injects vector-recalled memories into the next call before any explicit query — the exact "push, before an explicit query, via vector search" mechanism the source cites. Note names "CrewAI's LiteAgent" in prose with no edge.
- [cq](../../../../agent-memory-systems/reviews/cq.md) — **evidence**: cq's `pull` read-back (stored knowledge reaches the agent only when the skill-guided workflow calls `query`) is the source's "pull-oriented ones expose structured search tools, but stored knowledge reaches the agent only when something calls them" claim, grounded in code.
- [binder](../../../../agent-memory-systems/reviews/binder.md) — **evidence**: Binder's CLI/MCP/LSP access surface is the pull/tool half of the same Evidence bullet (named alongside cq in the note). Slightly weaker than cq because the note leans on cq for the explicit "something calls them" phrasing; still a direct corroborating instance.
- [agent-statelessness-makes-routing-architectural-not-learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — **grounds**: the source's Reasoning invokes "a [stateless agent] externalizes that property only by acting on it or signalling it." This note supplies the statelessness premise (every session is day one; routing is permanent architecture, not learned). The source currently inlines a *different* statelessness note (`agent-statelessness-means-the-context-engine-should-inject-context`); this routing note is the closer grounding for the "agent externalizes the symbol only by acting" step. Note: target is `status: current`, so `grounds` is fine.

## Bidirectional Candidates

- [knowledge-storage-does-not-imply-contextual-activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source — **extends**: the source already cites this as `grounds` (the activation gap sharpened into a symbolic-routing constraint). A return edge labelled `extends` would let a reader of the activation-gap note reach the specific bound the source adds. Worth adding from the target side.
- [agent-statelessness-means-the-context-engine-should-inject-context](../../../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) <-> source — **contrasts**: source cites this as `contrasts` (its open "how to identify what to inject" question, answered symbolically only once a symbol exists). The injection note's open trigger question is directly answered by the source, so a return `contrasts`/`extends` edge would close the loop for a reader of the injection note.

## Reverse-edge Candidates

- [equipa](../../../../agent-memory-systems/reviews/equipa.md) → source — **evidence/rationale**: under `kb/agent-memory-systems/COLLECTION.md`, links to `kb/notes/` "usually run inverse (theory links in via evidence/derived-from)," and the authorised review→notes labels include `rationale` and `evidence` (rare). EQUIPA's push-activation design rests on the theoretical claim this source makes (anticipation is reaction to an earlier symbol; genuine before-query surfacing is semantic). A `rationale` edge from the EQUIPA review to this source would let a review reader reach the governing theory. Connect does not author it; flagged for the review author or a connect run on `equipa.md`.
- [crewai-memory](../../../../agent-memory-systems/reviews/crewai-memory.md) → source — **rationale**: same inverse-direction logic; the LiteAgent push path is an instance of the semantic regime the source characterizes.
- [cq](../../../../agent-memory-systems/reviews/cq.md) → source — **rationale**: cq's pull architecture is the symbolic-trigger-fires-only-after-the-action case; a `rationale` link to this source explains *why* cq's read-back is pull rather than anticipatory.

These three reverse edges and the three forward `evidence` edges above are the two directions of the same source↔review relationships; whichever side authors first, the other becomes a computed backlink (forward edges are asymmetric, so both directions add reader value).

## Off-authorisation Candidates

None. Every candidate that passed the articulation test fits an authorised label for the `notes → {notes, agent-memory-systems}` pairs.

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- [access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — strong topical adjacency: its preference for symbolically executing fully specified transformations mirrors the source's “infer the symbol when none does” semantic regime. Rejected as a primary edge because that note is about the *transformation* axis (computing the answer), while the source is about the *access/routing* axis (selecting context). Linking risks conflating the two dimensions the access-burden note deliberately separates. A future writer could add a narrow `contrasts` edge if they articulate the access-vs-transformation distinction explicitly; not confident enough to recommend now.
- [in-context-learning-presupposes-context-engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) — adjacent ("something has to decide what 'right' means... before the model sees a token"). Rejected: it asserts that selection machinery is *learned/refined over deployment*, which is a different claim from *when a symbol is available to key on*. Overlap is thematic, not premise-level; an edge would be "related," which the articulation test rejects.
- [pointer-design-tradeoffs-in-progressive-disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) — fixed vs query-time pointers is adjacent to symbolic vs semantic routing, but pointers are about *resolution of a representation for deciding what to load*, not about *whether an identifying symbol exists yet*. No premise dependency; rejected.
- [session-history-should-not-be-the-default-next-context](../../../../notes/session-history-should-not-be-the-default-next-context.md) — the source's "context already loaded is cached reaction... symbols a prior operation made available" rhymes with this note's loaded-state theme, but the session-history note argues against defaulting to history, not about symbol availability for routing. Too oblique.

## Index Membership

- [context-engineering-index](../../../notes/context-engineering-index.md) — the source is squarely a context-engineering claim (routing under bounded context) and is not yet listed in the curated index. A future writer would add it; connect does not edit indexes.
- [tags-index](../../../notes/tags-index.md) / a context-engineering or routing tag index — the source has empty `tags:`, so it is invisible to every tag index. Adding `context-engineering` (and possibly `computational-model`) tags would make it routable. Flagged in Maintenance Observations rather than authored here.

## Synthesis Opportunities

The source plus [agentic-memory-systems-comparative-review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md)'s "navigability vs retrieval" split together imply a sharper higher-order claim: the comparative review's two "theories of knowledge access" (search-for vs navigate-to) are the *same* symbolic/semantic boundary the source draws, viewed from the storage-and-link side rather than the routing-trigger side. A synthesis note could state that the push/pull (read-back) axis catalogued across the reviews collapses onto the symbol-availability boundary — pull = act first to emit the symbol; semantic push = infer the symbol. Not created here; recorded for later judgment.

## Maintenance Observations

- **Source has empty `tags: []`.** This blocks all tag-index discovery and makes the note unreachable from `tags-index.md` and any topic index. A maintenance pass should consider `context-engineering` and `computational-model` tags. (Durable routing gap, not a connection candidate.)
- **Prose-named systems without edges.** The note names four external systems in its Evidence section but authors zero edges to their reviews, despite `kb/notes/COLLECTION.md` authorising `evidence`/`derived-from` into `kb/agent-memory-systems/`. This is the dominant under-connection and is the substance of Connections Found; noted here as a recurring pattern worth a maintenance check across other Evidence-section notes that name systems inline.

## Flags

- **Not a split candidate.** The source makes one assertion (symbolic routing is bounded by symbol availability) with corollaries; candidates cluster in two areas (notes routing/statelessness, agent-memory push/pull reviews), under the split-candidate threshold of three topic areas plus multiple independent assertions.
- **Seedling status.** Source is `status: seedling`. The `evidence` edges proposed are additive and safe to author now; the `grounds` edge to the routing note is load-bearing but points at a `status: current` target, so it is also safe.
