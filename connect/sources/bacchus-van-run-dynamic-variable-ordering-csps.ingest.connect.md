---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Ingest: Dynamic Variable Ordering In CSPs (Bacchus and van Run, CP-95)

**Source:** [Ingest: Dynamic Variable Ordering In CSPs](../../../../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md)

The ingest already carries inline links to five targets but no labelled footer. The candidates below would give those inline links a labelled footer and add two edges the ingest does not yet make.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links". Destinations scanned: notes, reference, agent-memory-systems, agentic-systems, sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (notes, agent-memory-systems), `abstracted-from` / `rests-on` / `defined-in` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `see-also` (sparingly), `derived-from` (external). External prospecting skipped. The source URL is already in frontmatter.

**Topic indexes:**
- `kb/notes/computational-model-README.md`: the source's domain `computational-model` matches the tag of the low-degree-of-freedom note. The README does not list the low-DoF, failure-explanation, backtracking, or cost-sensitive notes (rg for their slugs gave no hits). This README is a notes-side index, so the source does not belong in it.

**Body search** (over `kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources`, excluding snapshots):
- `rg -l -i "fail-first|fail first|most.constrained|minimum remaining|MRV"` gave only the source itself. The KB has no other artifact on fail-first or MRV.
- `rg -l -i "variable ordering|dynamic ordering|search order|branch order"` gave `competence-theory-problem-solving-method-construction.ingest.md` (method-construction commitments, not search ordering; rejected).
- `rg -l -i "constraint satisfaction|\bCSP\b|forward.checking|backjump|backtrack"` gave about 30 hits. Kept for evaluation: `backtracking-keeps-lightweight-search-control-provisional.md`, `cost-sensitive-formalisms-for-tentative-theory-search.md`, `failure-explanation-changes-later-branch-decisions.md`, `lightweight-search-control-does-not-license-adoption.md`, `an-assumption-based-tms.ingest.md`. The rest are "backtrack" in unrelated senses (reviews, benchmarks). Also checked: `optimal-ordered-problem-solver.ingest.md` (rejected).
- `rg -l -i "degree.of.freedom|degrees of freedom"` gave `solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md`, `decomposition-heuristics-for-bounded-context-scheduling.md` (restates the rule at line 53 with the optionality rationale), `alexander-patterns-and-knowledge-system-design.md`, and `fix-what-the-executor-cant-determine-not-what-it-will.md`.
- `rg -l -i "GSAT|local search|nogood"` gave `an-assumption-based-tms.ingest.md` (nogoods). The other hits were unrelated.
- `rg -l -i "commitment order|commit.*first|irreversib"` gave `pindyck-irreversibility-uncertainty-investment.ingest.md` and `productive-deferral-requires-option-evidence-and-convergence.md`. Both give the optionality-under-irreversibility account, which the source's fail-first mechanism competes with.

**Link following:**
- From the low-DoF note, its footer links `decomposition-heuristics-...`, `alexander-patterns-...`, and `fix-what-the-executor-...`. Only decomposition-heuristics restates the ordering rule itself.
- From `backtracking-keeps-...`, its footer links lightweight-search-control, productive-deferral, failure-explanation, and search-controller. This confirms a cluster (lightweight search control, then backtracking, then failure explanation) that the source bears on.
- From `productive-deferral-...`, it cites the Pindyck ingest as the primary mechanism for option preservation. The Pindyck ingest's footer has two `abstracted-from` edges into notes.
- `cost-sensitive-formalisms-...`, "Conflict-directed backtracking" section and Scope: the section calls the family a "close operational analogy" and Scope says families "require source grounding". The catalogue has no ordering family; limited discrepancy search assumes an ordering exists.

## Connections Found

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- **is-evidence-for**: MRV with dynamic reordering is the note's four-step rule, and the source gives theorem- and benchmark-backed support for it in reversible, exact-check search, plus a rival mechanism (fail-first) and four scope boundaries. The note has not yet incorporated these, so `is-evidence-for` fits and `abstracted-from` does not.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **is-evidence-for**: Theorem 2 is a formal case where retained failure information (standard backjumping) changes no later branch decision under MRV, so it is inert. This bears on the note's claim and suggests a scope condition: the value of retained failure analysis depends on how weak the ordering is.
- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: the note's Scope asks for source grounding. The source grounds the "conflict-directed backtracking" family with measured check counts, and shows that the family's gain is small under a strong ordering. The source also indicates a missing "dynamic ordering" family.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- **compares-with**: axis: where a heuristic's authority ends. The authors restrict MRV to naming the next variable and show that letting it share pruned domains turns it into forward checking. This is a formal counterpart to the note's line between allocating search and licensing change.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- **compares-with**: axis: when to commit a constrained choice. Productive deferral says to hold an irreversible choice open when evidence can discriminate. Fail-first says to commit the most constrained choice at once, because commitments are cheap to undo there. The contrast makes explicit the reversibility condition that the ingest's Connections section names in prose.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **compares-with**: axis: the cost of the return path. Fail-first ordering pays because chronological backtracking restores the earlier state cheaply. That cheap restoration is the precondition this note names for keeping a branch choice provisional. The source works entirely inside that precondition.
- [An assumption-based TMS](../../../../sources/an-assumption-based-tms.ingest.md) -- **compares-with**: axis: avoiding redundant work after a contradiction. The ATMS retains nogoods. This source shows that a good ordering makes some retained failure structure redundant. The ingest already names this comparison inline.
- [Irreversibility, Uncertainty, and Investment (Pindyck)](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md) -- **compares-with**: axis: commitment timing. Pindyck's option value of waiting depends on irreversibility. MRV's early commitment depends on reversibility. Together the two sources bracket the low-DoF note's mechanism question. Pair this edge with the productive-deferral edge; do not use it alone.

## Bidirectional Candidates

- [An assumption-based TMS](../../../../sources/an-assumption-based-tms.ingest.md) <-> source -- **compares-with**: the ATMS ingest could return the comparison on the same axis. This is optional.

## Reverse-edge Candidates

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) → source -- this is the primary reverse edge, and the ingest's Recommended Next Action already asks for it. After revision (fail-first beside optionality, scope boundaries, answer to the first open question for the exact-check case), the note should cite the ingest as evidence under `kb/notes/COLLECTION.md` rules.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) → source -- line 53 restates "commit low-degree-of-freedom choices first" with the optionality rationale. It could cite the ingest for the CSP basis. This is lower priority: the edge is better routed through the low-DoF note after its revision.
- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) → source -- the "Conflict-directed backtracking" section could cite the ingest to meet its own Scope requirement for source grounding.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) → source -- this is a possible Scope bullet: under a strong ordering, retained failure information can be correct and still inert (Theorem 2).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A competence theory approach to problem-solving method construction](../../../../sources/competence-theory-problem-solving-method-construction.ingest.md) -- it matched "order" lexically. It is about commitments made while refining competence into methods, not about search ordering.
- [Optimal Ordered Problem Solver](../../../../sources/optimal-ordered-problem-solver.ingest.md) -- "ordered" refers to program-search bias and reuse, not to the order in which decisions are committed. The shared axis is too weak.
- [Alexander patterns and knowledge system design](../../../../notes/alexander-patterns-and-knowledge-system-design.md) -- it is upstream of the low-DoF note's kitchen example, but it does not address ordering mechanisms. The edge is better reached through the low-DoF note.
- [Fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- it is about which actor owns a decision, which is separate from ordering. The source says nothing about that axis.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- it is adjacent to the search-control cluster, but the source evaluates ordering by check counts, not by what the ordering brings to stronger evaluation. The link would add nothing specific.
- [Ad hoc explanation can be rational when error is cheap and local](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) -- it matched "local search". The source makes no claim about disposable explanations.

## Index Membership

None. Sources are not listed in the notes tag READMEs. Discovery runs through the reverse edges above.

## Synthesis Opportunities

The source, [Pindyck](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md), [productive deferral](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md), and [backtracking keeps search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) together suggest a higher-order claim: the right order in which to commit constrained choices depends on the cost of undoing them. When undoing is cheap, commit the most constrained choice first to surface failure (fail-first). When undoing is costly, the case for committing it first rests on option preservation, and the deferral conditions govern whether to wait at all. This is probably best folded into the low-DoF note's revision rather than written as a new note.

## Maintenance Observations

- The ingest links its five targets inline in Connections Found but has no labelled footer. Other ingests in `kb/sources/` (for example the Pindyck ingest) use one. Labelled edges would make the source's relations machine-readable.
- `kb/notes/computational-model-README.md` does not list `solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md` even though the note carries the `computational-model` tag. That is acceptable unless the README declares `complete: true`, which it does not.
- The search-control cluster (lightweight search control, backtracking, failure explanation, search controller, cost-sensitive formalisms) now has one external CSP anchor, and it has nothing on ordering heuristics. The cost-sensitive catalogue's missing "dynamic ordering" family is a durable gap.

## Flags

- Tension, not resolved here: the low-DoF note's rationale (optionality preservation) and the source's mechanism (fail-first) coincide only when commitments are reversible. Productive deferral and Pindyck point the other way for irreversible commitments. Any revision of the low-DoF note should state which mechanism applies in which setting.
