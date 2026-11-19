---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/chaff-engineering-an-efficient-sat-solver.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Chaff: Engineering an Efficient SAT Solver

**Source:** [Chaff: Engineering an Efficient SAT Solver](../../../../sources/.snapshots/chaff-engineering-an-efficient-sat-solver.md)

The source is an immutable snapshot. Its authored connection surface is the matching ingest, `kb/sources/chaff-engineering-an-efficient-sat-solver.ingest.md`, which did not exist when this report was written. Every "Connections Found" item is a candidate for that ingest's analysis and `Relevant Notes` footer; link paths below are written relative to this report.

**What the source contributes (for judging candidates).** Moskewicz et al. (DAC 2001) attribute Chaff's 10-100x speedups on hard EDA instances to engineering of the Davis-Putnam loop, not to "sophisticated learning strategies": (1) two-watched-literal BCP, which makes unassignment constant-time on backtrack because watches need no update; (2) VSIDS, per-literal counters incremented when conflict clauses are added and periodically divided by a constant, so decisions favour literals in recent conflict clauses with low overhead; (3) scheduled lazy deletion of learned clauses by a relevance bound; (4) restarts that clear all assignments but keep still-relevant learned clauses and, unlike GRASP, leave decision statistics untouched; completeness is recovered by lengthening the restart period or relevance bound. The VSIDS section argues that decision or conflict counts mislead as heuristic metrics because heuristics differ in BCP consequences and overhead; only total runtime counts. Conflict analysis is said to follow GRASP and is not described. Results are the authors' own benchmark runs, not independent replication.

## Discovery Trace

**Setup:**
- Source collection: `sources`. `kb/sources/COLLECTION.md` exists. Its outbound section authorises destinations `notes`, `reference` (see-also only), `sources`, `agent-memory-systems`, `agentic-systems`, and `external` (derived-from, see-also). It excludes `kb/work/` and `kb/instructions/`. The snapshot itself is never the link author; the ingest carries the edges.
- External prospecting skipped per skill rules; the only known external target is the source URL itself (`https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf`), which the ingest should cite as `derived-from`.

**Topic indexes:**
- Read `kb/notes/learning-theory-README.md` and `kb/notes/self-improving-systems-README.md`. They route to the search-control, accumulation, and proposal-selection notes, which the title listing below confirmed. The snapshot carries no `tags:`, so no tag-scoped description sweep applied.

**Title / description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (444 titles), filtered with `rg -i "search|bias|forget|decay|recen|retain|retention|accumul|compound|heuristic|proxy|metric|measure|restart|reset|learn|prun|delet|engineer|overhead|cost|constraint|conflict|backtrack|propagat|decision"`. Flagged: `cost-sensitive-formalisms-for-tentative-theory-search`, `failure-explanation-changes-later-branch-decisions`, `backtracking-keeps-lightweight-search-control-provisional`, `lightweight-search-control-does-not-license-adoption`, `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation`, `accumulation-counts-dependence-through-the-retained-result`, `ephemeral-computation-prevents-accumulation`, `cheap-adoption-and-weak-retirement-accumulate-cost`, `program-theory-sustains-search-under-delayed-feedback`, `natural-language-project-state-specializes-search-heuristics`, `improvements-can-accumulate-without-compounding`.
- `ls -t kb/sources/.snapshots` and `ls kb/sources/*.ingest.md` showed a same-day sibling capture `bacchus-van-run-dynamic-variable-ordering-csps.md`, which has no ingest yet. Recent search-bias ingests include `optimal-ordered-problem-solver.ingest.md`, `shifting-inductive-bias-success-story-algorithm.ingest.md`, and `reinforcement-learning-self-modifying-policies.ingest.md`. Their `Connections Found` sections were read to see where this line of sources lands.

**Body search:**
- `rg -il "\bSAT\b|sat solver|CDCL|clause learning|chaff|VSIDS|watched literal|boolean constraint propagation|davis-putnam|DPLL" kb/` found no SAT-solver content. All hits were the English word "sat" (ADR 079, `sutskevers-list/full.md`, `citing-retained-theory-...`).
- `rg -n -i "nogood|no-good|constraint satisf|\bCSP|bacchus|learned clause|dependency-directed|truth maintenance|backjump|variable ordering|restart" kb/notes kb/sources/*.ingest.md kb/agentic-systems kb/agent-memory-systems kb/reference`: no conceptual hits. The hits were service restarts (Exo, Agno), browser CSP, and `pathway-beyond-transformers-sudoku-bench.ingest.md`, which is about constraint satisfaction as an LLM benchmark.
- An unscoped grep on `kb/notes/cost-sensitive-formalisms-for-tentative-theory-search.md` found the sections "Conflict-directed backtracking, learned constraints, and restarts" and "Restart schedules and probabilistic search" (lines 141-190). Its Scope says these mappings "require source grounding before they support a design decision". This is the strongest landing point.
- `rg -l -i "decay|recency" kb/agent-memory-systems kb/agentic-systems`: about 20 memory reviews mention decay or recency scoring. These are keyword matches only (see Rejected).
- `rg -n -i "exponential decay|decay factor|recency.weight|low.pass" kb/notes`: no hits.
- `rg -n -i "proxy|overhead"` on the search-controller and open-ended-search notes: one weak-proxy mention in `open-ended-improvement-allocates-search-before-evaluation.md`. No note charges controller overhead.

**Link following:**
- `failure-explanation-changes-later-branch-decisions` → `backtracking-keeps-lightweight-search-control-provisional` → `lightweight-search-control-does-not-license-adoption` → `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation`. This four-note cluster is the search-control theory, and Chaff offers formal instances for three of the four.
- `cost-sensitive-formalisms-for-tentative-theory-search` → `program-theory-sustains-search-under-delayed-feedback`, `a-proposal-selection-loop-requires-search-evaluation-and-retention`. The first is a grounds link; Chaff does not bear on it directly (see Rejected).
- `accumulation-counts-dependence-through-the-retained-result` placements section. It lists gradient descent, Self-Improving Algorithms, and the Homeostat as cases. A learned-clause database under restarts would be a symbolic, cumulative, within-run case, which is not yet represented.
- Sibling ingests OOPS and SSA land on accumulation, compounding, and proposal-selection notes. Chaff fits the same "retained results bias later search" line.

**Destinations with no plausible match:** `reference` (see-also only; no shipped-system doc bears on SAT search), `agentic-systems` (no reviewed system uses constraint learning or restart-based search).

## Connections Found

- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: This is a primary source for the note's "Conflict-directed backtracking, learned constraints, and restarts" and "Restart schedules" families, which the note marks as ungrounded research leads. Chaff confirms that restarts discard the assignment while keeping learned clauses and heuristic statistics. It also bears on the note's open question "What changes when learned failure constraints are retractable": Chaff's relevance-based clause deletion retracts sound constraints for memory reasons, and together with restarts this puts completeness at risk, which Chaff recovers by growing the relevance bound or restart period. That is a concrete price for forgetting, although it is not the fallible-constraint case the note is after. Caveat: the paper does not describe backjumping; it defers conflict analysis to GRASP.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **is-evidence-for**: A conflict clause is a retained explanation of a failed branch, and Chaff makes it operative through two channels: BCP implications prune later assignments, and VSIDS counters raise the priority of its literals in later decisions. The paper states that "it is the conflict clauses that primarily drive the search process" and that VSIDS couples "that driving force to the decision process". This is a formal case of the note's criterion, and its soundness is guaranteed, which marks the contrast with fallible natural-language explanations.
- [Accumulation counts dependence through the retained result, not through the evidence it caused](../../../../notes/accumulation-counts-dependence-through-the-retained-result.md) -- **is-evidence-for**: Restarts divide a run into episodes. After a restart, the new search trajectory is computed from the retained clause database and VSIDS counters. Substituting different learned clauses or counters on the same instance would change later propagation and decisions, so the case passes the note's substitution test through the retained result rather than through the trigger. It would be a "cumulative, symbolic, within-run" placement the note lacks. Scope caveat for the ingest: learning is per-instance, so the horizon is one solver run, not cross-task.
- [Discarding all experience-dependent state prevents cross-run accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md) -- **is-evidence-for**: A Chaff restart is the note's "artifact discarded + retained useful lesson" row at a within-run horizon. The decision stack and assignment are discarded, but still-relevant learned clauses survive, so "the solver will not simply repeat the previous analysis following a restart". GRASP's restarts, which also reset decision statistics, and Chaff's, which keep them, show that what survives a restart is a design choice. Use it only as a horizon-scoped illustration; the note's headline is about cross-run accumulation.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **is-evidence-for**: The VSIDS section is a worked case of comparing search controllers under matched tasks by downstream outcome. Chaff rejects decision and conflict counts as metrics because decisions yield unequal BCP work and heuristics carry unequal overhead, so "the 'best' decision strategy" by such statistics "may actually be the slowest". The case adds a qualification the note does not state: a controller's own computation must be charged in the comparison, and VSIDS won partly by being cheap (about 10% of runtime). This bears on the note's claim; it does not establish it for open-ended search.
- [Optimal Ordered Problem Solver (ingest)](../../../../sources/optimal-ordered-problem-solver.ingest.md) -- **compares-with**: Shared axis: *how a retained search product biases later search*. OOPS changes the continuation probabilities of later program search through frozen code. Chaff changes decision order through recency-decayed counters over learned clauses and prunes through the clauses themselves. OOPS transfers across tasks; Chaff learns within one instance.
- [Shifting inductive bias with the Success-Story Algorithm (ingest)](../../../../sources/shifting-inductive-bias-success-story-algorithm.ingest.md) -- **compares-with**: Shared axis: *how retained search-bias changes are revisited*. SSA rolls back bias changes that fail a lifetime reward-rate comparison, which is reject-capable retention. VSIDS never rejects an update: old bias fades through periodic division, and learned clauses leave by a fixed relevance schedule. This pairs rejection-based and decay-based revision of search bias for the ingest's Limitations or Learning Claims section.
- [Original paper](https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf) -- **derived-from**: the ingest's analysis is worked out from this DAC 2001 paper.

## Bidirectional Candidates

None. No candidate note is a source-side artifact that could author a return link under `kb/sources/` rules. Return links from notes go to Reverse-edge Candidates.

## Reverse-edge Candidates

These all target the future ingest `kb/sources/chaff-engineering-an-efficient-sat-solver.ingest.md`, not the snapshot, because notes must never link `.snapshots/`. Labels come from `kb/notes/COLLECTION.md` (notes → sources: `evidenced-by`, `derived-from`, `abstracted-from`, `see-also`).

- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) → ingest -- **evidenced-by**: This is the strongest reverse edge. The "Conflict-directed backtracking, learned constraints, and restarts" and "Restart schedules" subsections currently rest on no source, and the note's Scope says they need grounding. Chaff grounds the restart-retains-clauses-and-statistics claim and the clause-deletion versus completeness trade-off. The backjump sentence would still need another source, such as GRASP. A verbatim quote retained through `cp-skill-ground` would keep the note inside the five-unquoted-source bound.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) → ingest -- **evidenced-by**: Conflict clauses are a sound, mechanised instance of a retained failure explanation that changes later branch decisions through propagation and decision priority. This gives the note a concrete anchor and a contrast case where the explanation is guaranteed correct.
- [Accumulation counts dependence through the retained result, not through the evidence it caused](../../../../notes/accumulation-counts-dependence-through-the-retained-result.md) → ingest -- **evidenced-by**: This would support a candidate new placement: learned-clause databases across restarts are cumulative within a run, symbolic, and non-reflective. That placement sits between gradient descent (opaque) and the editable-policy file (reflective, non-cumulative).

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- DP backtracking is the textbook instance, and watched literals make the return path cheap (constant-time unassignment). However, the note's point concerns keeping a trial from turning into an adoption, and Chaff adds nothing to that beyond "backtracking exists and can be cheap". Keep it only if the ingest writer wants an example of restore cost. Covered better by the cost-sensitive note's Recovery and Checkpoint budgets.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- A SAT decision is provisional search control, but the note's contrast is with operative adoption, and a SAT solver has no adoption step separate from finding a model. The match is a keyword analogy.
- [Cheap adoption and weak retirement accumulate cost](../../../../notes/cheap-adoption-and-weak-retirement-accumulate-cost.md) -- Every conflict adds a clause cheaply, and Chaff schedules retirement at adoption time ("when each clause is added, it is examined to determine at what point in the future ... it should be deleted"). That is a neat counter-design to the asymmetry. But the note is about structural KB conventions with distributed consumers, and learned clauses have no consumer-coordination cost. The transfer would be a loose analogy; see Synthesis Opportunities instead.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- Learned clauses and VSIDS updates are directly determined and always adopted. They have no reject-capable evaluation, so they fall under the "direct update" architecture, not proposal selection. A link would mislead unless it is framed as a contrast, and SSA and OOPS already serve the proposal-selection side.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- Chaff's "theory" is a sound clause set with immediate conflict feedback. It has no delayed evidence and no partial account of purpose. The link is reached only through the cost-sensitive note.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- The two share only the phrase "search heuristics". The note is about LLM weights plus prompt state.
- [The self-improving-system definition classifies its boundary cases](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- A per-instance CDCL solver would likely be excluded as episode state, but the note's ten cases already cover that exclusion. Adding one more is low value.
- [Pathway beyond transformers — Sudoku bench (ingest)](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- The only shared ground is constraint satisfaction as a benchmark domain for LLM limits; there is no mechanism overlap.
- Agent-memory reviews with decay or recency scoring (for example `kb/agent-memory-systems/reviews/mem0.md`, `MemoryOS.md`) -- VSIDS decay reads like memory decay only at the keyword level. These reviews score retrieval importance, not search-decision priority driven by conflicts. Rejected as keyword-only.

## Index Membership

- [computational-model-README](../../../../tags/computational-model-README.md) / [self-improving-systems-README](../../../../tags/self-improving-systems-README.md) -- Ingests are not normally listed in tag READMEs, so no index entry is recommended for the ingest itself. If the accumulation note gains the CDCL placement, that note's existing index entries already cover it.

## Synthesis Opportunities

- **Scheduling retirement at adoption time.** Chaff decides a learned clause's deletion condition when the clause is added. Read with [cheap adoption and weak retirement](../../../../notes/cheap-adoption-and-weak-retirement-accumulate-cost.md) and the cost-sensitive note's open question on retractable constraints, this suggests a claim: cheap-to-adopt retained items stay affordable when their retirement trigger is fixed at adoption rather than discovered later. Evidence is a single formal-domain case, so for now this belongs in a log entry, not a note.
- **Decay-based versus rejection-based revision of search bias.** VSIDS (low-pass decay, no rejection), SSA (reward-rate rollback), and OOPS (frozen, never revised) together cover three retention disciplines for search bias. A comparison could sit in the self-improving-systems area under update architecture. This needs the Chaff ingest and possibly the Bacchus ingest first.

## Maintenance Observations

- `kb/notes/cost-sensitive-formalisms-for-tentative-theory-search.md` names CDCL and restart families with no source links, and its Scope says so. This Chaff capture (and likely the same-day `bacchus-van-run-dynamic-variable-ordering-csps.md` capture for the variable-ordering and heuristic-search families) looks like the grounding effort for that note. Route the grounding through `cp-skill-ground` once the ingests exist.
- The same-day sibling snapshot `kb/sources/.snapshots/bacchus-van-run-dynamic-variable-ordering-csps.md` has no ingest yet.
- Note-side prose attributes backjumping to conflict-directed search. Chaff does not describe backjumping, so the ingest should not be cited for that sentence.

## Flags

- The ingest does not exist yet. All connections target it, and reverse edges should wait until it is written.
- Tension for the ingest writer: the paper claims its speedup comes "not ... [from] sophisticated learning strategies" but from engineering. Yet VSIDS explicitly draws on learned conflict clauses, and the KB candidates above all read Chaff as a retained-learning case. The ingest should record the authors' framing and separate the within-instance clause learning (inherited from GRASP) from Chaff's own contributions (BCP and decision overhead).
- Not a split candidate.
