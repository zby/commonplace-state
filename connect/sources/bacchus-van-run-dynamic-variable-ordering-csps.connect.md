---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/bacchus-van-run-dynamic-variable-ordering-csps.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Dynamic Variable Ordering In CSPs (Bacchus and van Run, CP-95)

**Source:** [Dynamic Variable Ordering In CSPs](../../../../sources/.snapshots/bacchus-van-run-dynamic-variable-ordering-csps.md)

The source is an immutable snapshot. Every outbound candidate below is meant for the matching tracked ingest, `kb/sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md`, which does not exist yet. A durable link must target that ingest and never the snapshot.

What the source contributes, in the terms the candidates use:
- **Node/variable separation:** DVO can be added to any CSP tree-search algorithm, including backmarking, by keeping search-tree depth (node index) separate from variable identity (variable index).
- **Theorem 2:** under MRV, standard backjumping is redundant. BT+MRV and BJ+MRV perform identical checks, and so do BM+MRV and BMJ+MRV.
- **Theorem 3:** BT, BJ, BM, and BMJ with MRV computed by forward-checking pruning (MRV_FC) use between 1x and 2KN times the checks of FC+MRV. Once information from the MRV computation is shared with the search, the combination becomes FC. MRV also "promot[es] future failures to the next variable".
- **Empirical result:** FCvar, FC-BJvar, and FC-CBJvar rank top three on every test. Adding CBJ gains at most 5%, plausibly because MRV already groups conflicted variables together. The paper's own stated caveat is that CBJ may matter more when initial domain sizes differ. FC stays limited on large, easy problems.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, Outbound links section. Authorised destinations are notes, reference, sources, agent-memory-systems, agentic-systems, and external. The contract excludes `kb/work/` and `kb/instructions/`. The labels for notes are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` (notes/definitions), and `see-also`. The labels for sources are `compares-with` and `see-also`. `derived-from` applies only to external. The snapshot never authors links; the ingest does.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i "order|first|prun|constrain|search|heuristic|fail|branch|dead end|commit|defer|early"`. This surfaced `solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md`, the MRV principle stated for design decomposition and the strongest candidate. It also surfaced the search-control cluster: `backtracking-keeps-lightweight-search-control-provisional`, `failure-explanation-changes-later-branch-decisions`, `lightweight-search-control-does-not-license-adoption`, `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation`, `natural-language-project-state-specializes-search-heuristics`, `cost-sensitive-formalisms-for-tentative-theory-search`, and `decomposition-heuristics-for-bounded-context-scheduling`.
- `rg -N --no-heading '^description:' kb/sources/*.ingest.md | rg -i "search|backtrack|constraint|heuristic|truth maintenance|TMS|discrepancy|restart|SAT\b|conflict"`. This surfaced the sibling classic-search sources `an-assumption-based-tms.ingest.md`, `chunking-in-soar-general-learning-mechanism.ingest.md`, `pathway-beyond-transformers-sudoku-bench.ingest.md`, `optimal-ordered-problem-solver.ingest.md`, and `eurisko-learns-new-heuristics-and-domain-concepts.ingest.md`.

**Topic indexes:**
- The snapshot has no `tags:`, so no tag-README was selected from source metadata. The strongest note candidate is tagged `computational-model`. I checked `kb/notes/computational-model-README.md` only through its description, as a possible index home, not to recall candidates.

**Body search:**
- `rg -il "constraint satisfaction|\bCSP\b|minimum remaining values|\bMRV\b|fail-first|fail first|forward checking|variable ordering|most constrained|backjump|backtrack" kb/ --glob '*.md'` (with kb/work filtered out). No note uses MRV, forward checking, or variable ordering by name. The only direct technical overlap is the "Conflict-directed backtracking, learned constraints, and restarts" section of `cost-sensitive-formalisms-for-tentative-theory-search.md` (lines 142–155). The other hits are about backtracking in general.
- `rg -il "bacchus|haralick|dechter" kb/`: no hits. No existing artifact already cites this source or its neighbours.
- `rg -il "bacchus|dynamic variable ordering|minimum remaining" kb/work kb/messages`: no hits. No workshop names this source as its target.
- `rg -n -i "dependency-directed|chronological|nogood" kb/notes`: no search-theoretic hits (the matches were ACM prefix compression and chat history). Rejected.
- `rg -l "solve-low-degree-of-freedom" kb`: inbound links from `alexander-patterns-and-knowledge-system-design.md`, `decomposition-heuristics-for-bounded-context-scheduling.md`, `fix-what-the-executor-cant-determine-not-what-it-will.md`, `context-efficiency-is-the-central-design-concern-in-agent-systems.md`, and the sibling source `creative-thinking-by-claude-shannon.ingest.md`.

**Link following:**
- `solve-low-degree-of-freedom-...`: I read it in full. Its four-step rule is MRV. Its step 3, "recompute feasible sets for remaining choices", is dynamic reordering with forward-checking pruning. It justifies the rule by *optionality preservation*, grounded only in Alexander's kitchen example. Its open question asks whether degree-of-freedom estimates can be made explicit enough for deterministic schedulers, and MRV_FC is exactly such an estimate. Kept.
- `cost-sensitive-formalisms-...`: I read it in full. Its Scope says the model families "require source grounding before they support a design decision". It covers conflict-directed backjumping but has no family for variable ordering. Kept.
- `backtracking-keeps-...` and `failure-explanation-changes-...`: I read both in full. Kept the second one. It says a retained failure explanation counts only when it changes a later branch decision, and Theorem 2 and the CBJ result give a formal case where good ordering leaves little for failure analysis to change. The first one was rejected, see below.
- `lightweight-search-control-...`: I read it through its description and through its use in neighbouring notes. Kept, with lower priority.
- `natural-language-project-state-...`: I read it in full. Rejected, see below.
- `an-assumption-based-tms.ingest.md`: I read the summary lines on nogoods. Kept as a `compares-with` sibling.
- `creative-thinking-by-claude-shannon.ingest.md`: it already links the low-DoF note as a companion sequencing heuristic. Considered and rejected, see below.

## Connections Found

All of these are candidates for the future `bacchus-van-run-dynamic-variable-ordering-csps.ingest.md`.

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- **is-evidence-for**: Bacchus and van Run give the formal and empirical CSP form of this note's rule. MRV commits the variable with the fewest remaining values first, and dynamic reordering recomputes feasible sets after each commitment. The source bears on the note in three ways. (1) It supports the rule: DVO with MRV gave large net speedups, often orders of magnitude, in every test the authors reported. (2) It offers a rival mechanism: the source's rationale is *fail-first*, meaning dead ends surface at the next level, not *optionality preservation*. (3) It prices step 3: computing MRV costs at least as many checks as forward checking, which answers part of the note's open question about explicit degree-of-freedom estimates. A future ingest should state that this is binary exact CSP evidence, not design-decomposition evidence.
- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: the source gives a check-counted formal result about the interaction the catalogue leaves open. Theorems 2–4 bound how much retained-failure machinery (standard backjumping, CBJ) contributes once successor ordering is dynamic and constraint-aware. That is evidence about which budget is worth adding to the "candidate composite". Step 3 of the composite, retaining conflict explanations, may add little on top of a good ordering rule, and Theorem 3 prices the heuristic itself in consistency checks. It also supplies source grounding that the note's Scope says it lacks.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **is-evidence-for**: Theorem 2 is a precise case of retained failure information that is correct but leaves later branch decisions unchanged. Under MRV every standard backjump is a chronological backstep, so the backjumping machinery changes nothing. CBJ's gain of 5% or less shows the same effect more weakly. The case supports the note's claim that an explanation is operative only when it changes a later choice. It also adds a condition the note does not state: another controller component may already capture what the explanation would contribute.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- **is-evidence-for** (lower priority): the source deliberately restricts MRV's output to "return the next variable, it communicates no other information to the tree-search algorithm". It then shows that sharing pruned domains or domain wipeouts leads "naturally to a combined algorithm that is identical to FC". This formal example marks where a heuristic's authority to order search stops, and what happens when that authority widens. Drop this candidate if the ingest's scope keeps to ordering evidence.
- [An assumption-based TMS (ingest)](../../../../sources/an-assumption-based-tms.ingest.md) -- **compares-with**: the shared axis is *how a search system avoids redundant work after a contradiction*. The ATMS retains minimal nogood environments and avoids most backtracking by caching. Bacchus and van Run show that failure-first ordering plus forward pruning makes one class of retained failure structure (standard backjumping) redundant and leaves little for CBJ. Together they show that retaining failure structure and choosing a good ordering are partly substitutable routes to the same saving.

## Bidirectional Candidates

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) <-> ingest -- **evidenced-by** (under the notes COLLECTION.md): the note's only support is Alexander's kitchen example. The return link would give it an external formal and empirical anchor. It would also make the fail-first versus optionality-preservation rationale visible to a reader who starts from the note.
- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) <-> ingest -- **evidenced-by**: the return link is useful from the "Conflict-directed backtracking" section and from composite step 3. A new family entry for dynamic variable ordering and fail-first heuristics is a reasonable place for it.

## Reverse-edge Candidates

- [Failure explanation changes later branch decisions](../../../../notes/failure-explanation-changes-later-branch-decisions.md) → ingest -- **evidenced-by**: a possible Scope bullet: "retained failure information can be correct yet redundant when the ordering already captures it (MRV makes standard backjumping a no-op)". Author it only if the note's owner accepts the added condition.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) → ingest -- weak. The note reaches the ordering rule through the low-DoF note, so the direct edge is probably redundant. It is listed so the owner can decide.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- the source takes chronological backtracking as given and studies ordering and pruning, not the provisional status of a branch choice or the restoration of state. Node/variable separation is an implementation detail of restoring state, not evidence for the note's claim.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- MRV is a hand-coded symbolic heuristic. The source says nothing about weights, prompts, or project-state specialization. The only overlap is the keyword "heuristic".
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- CSP consistency checks are exact evaluation, not a provisional judgment routed into a stronger one. The distinction the note depends on does not arise.
- [Creative thinking by Claude Shannon (ingest)](../../../../sources/creative-thinking-by-claude-shannon.ingest.md) -- it touches the same ordering heuristic only through the low-DoF note. There is no shared axis for `compares-with`, and `see-also` would be a spray.
- [Pathway Sudoku bench (ingest)](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- the two share the constraint-satisfaction domain only. Pathway concerns LLM architectural limits, not search algorithms. A link would suggest a comparison that neither source supports.
- [Chunking in Soar (ingest)](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) and [EURISKO (ingest)](../../../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md) -- both concern *learned* search control. Bacchus and van Run evaluate a fixed heuristic, so a comparison axis would be forced.
- External: Frost and Dechter 1994, Prosser 1993, Kondrak 1994, and Haralick and Elliott 1980 are cited in the paper but not held in the KB. I did no external prospecting, as the skill requires.

## Index Membership

None. Ingest reports are not listed in note tag-READMEs, and `kb/sources/` has no curated topical index to join.

## Synthesis Opportunities

The low-DoF note, the conflict-directed section of the cost-sensitive catalogue, the failure-explanation note, and this source together imply a claim the KB does not yet state: **ordering by constraint and retaining failure explanations are partial substitutes for one another**. A good fail-first ordering moves dead ends forward, so explanation-driven backjumps have less to skip. The value of retained failure analysis therefore depends on how weak the ordering is. Bacchus and van Run show this only for exact binary CSPs with uniform domain sizes. Whether it carries over to fallible, natural-language theory search is open. This is a candidate claim for a future writer, and a possible question to add to the cost-sensitive catalogue's "Complexity questions".

## Maintenance Observations

- The low-DoF note grounds a general ordering rule in a single architecture example and gives only the optionality-preservation rationale. The CSP literature's standard justification, fail-first, is absent. Adding the ingest link would let a later revision state both mechanisms and say when each applies. Fail-first matters when commitments can be undone; optionality matters when they cannot.
- The cost-sensitive catalogue lists search families but has no variable-ordering or value-ordering family, although its framing ("a partial project theory orders search") is at bottom about ordering.

## Flags

- **Tension, unresolved:** the low-DoF note justifies most-constrained-first by preserving options for the remaining choices. The source justifies MRV by surfacing failure early (fail-first). The two predict different behaviour when commitments cannot be undone, which is the note's design setting, compared with when backtracking is cheap, which is the source's CSP setting. The ingest should report this and not merge the two.
- **Scope caution for the ingest:** the results cover binary CSPs, identical domain sizes in the reported tests, check counts as the cost measure, and 1995-era algorithms. The paper names three limits itself: FC does poorly on large, easy problems; CBJ may matter when domain sizes differ; and the Frost and Dechter comparison may reflect a bug in their code.
- The target ingest does not exist yet. All outbound candidates presuppose it.
