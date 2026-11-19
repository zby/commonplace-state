---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md"
source_has_frontmatter: true
date: "2026-06-15"
depth: standard
---

# Connection Report: Large Language Model Agents Are Not Always Faithful Self-Evolvers

**Source:** [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.md)

This source is an immutable **snapshot** under `kb/sources/`. Per the sources `COLLECTION.md`, snapshots never author outbound links, and no `<name>.ingest.md` companion exists for this snapshot — so there is no authored outbound surface to recommend edits for. The entire actionable deliverable is **reverse-edge candidates**: which library notes should add `evidence` / `derived-from` links pointing at this snapshot under their own collection rules. Several of those edges already exist as bare external URLs and should be upgraded to labelled reverse edges; the rest are new.

## Discovery Trace

**Source collection check:** `kb/sources/COLLECTION.md` exists. Outbound section read: snapshots immutable, authoring signal is reverse-edge (library notes adding `evidence`/`derived-from` to this snapshot). Authorised labels for sources author surfaces: `evidence`, `derived-from`, `rationale`, `compares-with` (sources/agent-memory/agentic-systems), `defined-in`, `see-also`. Reverse-edge candidates are judged against the destination note's own collection rules, not the sources table.

**Description listing scan:**
- `rg '^description:' kb/notes/definitions/` -- flagged `distillation.md` (already cites source twice), `context-engineering.md`.
- `rg '^description:' kb/agent-memory-systems/ kb/agentic-systems/` filtered for memory/experience/evolve -- flagged the reviews of systems this paper directly benchmarks: `dynamic-cheatsheet.md`, `agent-workflow-memory.md`. (G-Memory, ReasoningBank, ExpeL have no standalone reviews — confirmed below.)
- `rg '^description:' kb/sources/` filtered for memory/compress/context -- flagged `the-price-of-meaning-why-every-semantic-memory-system-forgets.ingest.md`, `convexbench-...`, `the-y-combinator-for-llms-solving-long-context-rot.md` as possible `compares-with`.

**Topic indexes:**
- Read candidate notes directly rather than tag READMEs (source carries only `tags: [academic-paper]`, no methodology tag to route on).

**Body search:**
- `rg -l 'distill|condens|compress|faithful|experience|self-evolv|memory' kb/notes/ -i` -- surfaced distillation cluster, agent-memory-requirements, interpretation-errors, evolving-understanding, continual-learning.
- `rg -li 'reasoningbank|self-evolv|dynamic cheatsheet|expel|condensed experience|faithful' kb/` -- confirmed which frameworks have reviews: `dynamic-cheatsheet.md` (yes), `agent-workflow-memory.md` (yes); ExpeL/ReasoningBank/G-Memory mentioned only in reference coverage / work, no review files.
- `rg -l '2601.22436|Faithful Self-Evolvers'` -- existing references: `definitions/distillation.md`, `agent-memory-requirements/evaluate-memory-by-effects.md`, `agent-memory-requirements/activate-behavior-changing-memory.md` (rest are work/ and reports/, out of scope).
- `rg -li 'reverse.compression|compress.*lose|lossy'` -- surfaced `distillation-is-transformation-not-selection.md`, `reverse-compression-...`, `information-value-is-observer-relative.md`.

**Link following:**
- From `definitions/distillation.md` -> `evolving-understanding-needs-re-distillation-not-composition.md` (re-distillation of condensed material) and `learning-is-not-only-about-generality.md`.
- From `agent-memory-requirements/activate-behavior-changing-memory.md` -> `continual-learning-open-problem-is-behaviour-not-knowledge.md` and `knowledge-storage-does-not-imply-contextual-activation.md`. The latter's "context-to-action failure" mode (already grounded by "Agents Explore but Agents Ignore") is a direct sibling to this paper's IG-attribution finding that condensed experience is read into context but not acted on.

## Connections Found

None. The source is an immutable snapshot with no `.ingest.md` authored surface; it authors no outbound edges. All actionable signal is below as reverse-edge candidates.

## Bidirectional Candidates

None. (No outbound edges from the snapshot, so no return paths to pair.)

## Reverse-edge Candidates

Edges other library artifacts should author **to** this snapshot, under their own `COLLECTION.md` rules. The first three already cite the source as a bare external URL and should be upgraded to a labelled local edge pointing at this snapshot path.

- [definitions/distillation.md](../../../notes/definitions/distillation.md) → source -- **evidence** (already referenced, upgrade): the note already uses this paper as a "warning case" (compressed experience can stay semantically plausible yet lose behavioral influence). The two inline citations currently point at the arXiv URL; a local link to this snapshot makes the evidence reverse-edge explicit. Note carries `tags: [learning-theory, distillation]` — this paper is the central empirical evidence for distillation's information-loss claim.
- [agent-memory-requirements/evaluate-memory-by-effects.md](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source -- **evidence** (already referenced, upgrade): note's Relevant Notes already lists this paper as showing "written memory must be evaluated for behavioral influence rather than assumed effective." Direct support for the note's central "evaluate by effects, not existence" claim and the WITH/WITHOUT activation method.
- [agent-memory-requirements/activate-behavior-changing-memory.md](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) → source -- **evidence** (already referenced, upgrade): note's "Behavioral Faithfulness" section already names this paper as the cautionary example that compressed memories can improve measured behavior without being used as designed. Strongest single fit for the source's core finding.
- [knowledge-storage-does-not-imply-contextual-activation.md](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidence** (new): the paper's §5.2 IG-attribution result — condensed experience is present in context but receives consistently low attribution while the current trajectory dominates later layers — is a clean instance of this note's "context-to-action failure" (knowledge visible but not integrated). Pairs with the "Agents Explore but Agents Ignore" evidence the note already cites; this note is a seedling and a load-bearing `evidence` edge here is well within scope.
- [continual-learning-open-problem-is-behaviour-not-knowledge.md](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidence** (new): the note argues knowledge accumulation is solved but behaviour change is the open problem. This paper is direct evidence that readable/condensed system-definition artifacts (heuristics, summaries) often fail to change behaviour even when accumulated and retrieved — i.e. accumulation succeeded but the behaviour-change half did not.
- [evolving-understanding-needs-re-distillation-not-composition.md](../../../../notes/evolving-understanding-needs-holistic-rewrite-not-composition.md) → source -- **evidence** (new, candidate): the paper's design takeaway — condensed experience must be contextualized/actionable, not merely brief — corroborates that compression-for-brevity loses behavioral utility, which is the failure mode re-distillation guards against. Slightly weaker fit (the note is about reconciling fragments, not condensation faithfulness specifically); flag for the note author to judge.

## Off-authorisation Candidates

- [agent-memory-systems/reviews/dynamic-cheatsheet.md](../../../../agent-memory-systems/reviews/dynamic-cheatsheet.md) -- This paper benchmarks Dynamic Cheatsheet (the DC-RS framework, §3.1/Figure 3) and finds its condensed cheatsheet largely behaviorally inert under perturbation. A review citing the paper that directly evaluated its system is high-value, but the **agent-memory-systems** collection's authorised label set governs this edge, not the sources table — its rules were not loaded in this run. Suggestion: a future connect run scoped to `agent-memory-systems/COLLECTION.md`, or the review author, should consider adding an `evidence`/`compares-with`-equivalent edge to this snapshot. Likely a `compares-with` (source↔agent-memory) reverse edge as well.
- [agent-memory-systems/reviews/agent-workflow-memory.md](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) -- AWM is the canonical workflow-memory system; the paper's whole thesis (condensed/induced summaries underused vs raw traces) bears directly on AWM's induced-workflow design. Same caveat: governed by `agent-memory-systems/COLLECTION.md`, not loaded here. Suggestion: route to a connect run on that collection.

## Raw Text Candidates

None.

## Rejected Candidates

- [definitions/context-engineering.md](../../../../notes/definitions/context-engineering.md) -- The paper's Impact Statement explicitly invokes "context engineering," so the keyword matches, but the definition note is a stable `current` definition and gains nothing concrete from this single empirical paper as a direct edge. Topical overlap only.
- [the-price-of-meaning-why-every-semantic-memory-system-forgets.ingest.md](../../../../sources/the-price-of-meaning-why-every-semantic-memory-system-forgets.ingest.md) -- Possible `compares-with` (both about memory limits), but the price-of-meaning paper is about retrieval interference/forgetting, a different mechanism than condensation faithfulness. No concrete reader gain; would be a "related" link. Rejected unless the ingest author sees a sharper parallel.
- [interpretation-errors-are-failures-of-the-interpreter.md](../../../notes/interpretation-errors-are-failures-of-the-interpreter.md) -- Tempting: the paper's "internal processing bias suppresses retrieved memory" looks like an interpreter failure. But this note's frame is outputs *outside the valid interpretation space* (constraint violation, hallucination), whereas ignoring valid condensed experience is underutilization, not a spec violation. Conceptual adjacency without a clean articulation; rejected to avoid a confusing edge.
- ExpeL / ReasoningBank / G-Memory -- benchmarked frameworks with no standalone review file in the KB (confirmed by rg). No artifact to link.

## Index Membership

- [reference/agent-memory-coverage.md](../../../../reference/agent-memory-coverage.md) -- matched the rg sweep and tracks agent-memory source/system coverage; a future writer might list this paper there as faithfulness-of-memory evidence. Not verified against that file's inclusion contract in this run — flag, do not assume.

## Synthesis Opportunities

Three KB notes independently lean on this paper's finding — `distillation.md` (compression loses behavioral influence), `activate-behavior-changing-memory.md` (fired memory may not change action), and `evaluate-memory-by-effects.md` (count effects, not existence). Together with the new `knowledge-storage-does-not-imply-contextual-activation` edge, they imply a sharper higher-order claim already partly present in the KB: **read-back is not activation, and condensation is a systematic activation-killer** — distillation that optimizes for brevity predictably reduces the very behavioral influence memory is stored to produce. The pieces exist; if a synthesis note does not yet name the "condensation reduces activation" mechanism explicitly, that is a promotion candidate. Do not create it during connect.

## Maintenance Observations

- Three notes (`distillation.md`, `evaluate-memory-by-effects.md`, `activate-behavior-changing-memory.md`) cite this source via the `arxiv.org/html/2601.22436v2` URL rather than the local snapshot path. The snapshot's capture note says it is now v3 (13 backbones) while inline anchors still point at v2. Consider standardising these citations on the local snapshot link so the v2/v3 drift is captured in one place.
- No `.ingest.md` companion exists for this snapshot. Given how many notes already cite it as evidence, an ingest report would give the source a proper authored outbound surface and consolidate the scattered citations. Promotion candidate for a later ingest step.

## Flags

- **Reverse-edge-only finding:** as an immutable snapshot with no ingest companion, this source authors zero outbound edges; all value is reverse edges (above). This is expected for `kb/sources/` snapshots, not a defect.
- **Cross-collection edges deferred:** the two strongest system-level edges (Dynamic Cheatsheet, Agent Workflow Memory reviews) are governed by `agent-memory-systems/COLLECTION.md`, which this run did not load. Routed to Off-authorisation Candidates for a collection-scoped follow-up rather than guessed at.
