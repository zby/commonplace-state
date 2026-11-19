---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/efficiently-intertwining-widening-narrowing.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Efficiently intertwining widening and narrowing

**Source:** [Efficiently intertwining widening and narrowing](../../../../sources/.snapshots/efficiently-intertwining-widening-narrowing.md) (Amato, Scozzari, Seidl, Apinis, Vojdani, arXiv 1503.00883, 2015)

The source is an immutable snapshot. No `efficiently-intertwining-widening-narrowing.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest's `## Connections Found` section. No durable link may target the snapshot itself.

Source content in brief: the paper defines a combined operator that acts as narrowing while an unknown's value is descending and as widening otherwise. It shows that plugging this operator naively into round-robin or worklist iteration can fail to terminate even on monotonic systems. It then gives solver variants (round-robin, worklist, local solver SLR, side-effecting SLR+) that return sound post-solutions and terminate for monotonic systems with finitely many encountered unknowns. For non-monotonic systems it proposes practical remedies. It also localizes the operator to dynamically detected loop heads and restarts iteration for subsets of unknowns. Its stated motivation: precision lost in a widening phase and propagated through the system generally cannot be recovered by a later narrowing phase.

## Discovery Trace

**Setup:**
- Source collection `sources`; read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: notes (`is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; `defined-in` for notes/definitions), reference (`see-also` only), sources (`compares-with`, `see-also`), agent-memory-systems and agentic-systems (`compares-with`, `see-also`; plus `is-evidence-for` for agent-memory-systems), external (`derived-from`, `see-also`). Excluded: `kb/work/`, `kb/instructions/`.
- Read `kb/reports/types/connect-report.md`.
- Read the snapshot abstract, introduction (lines 1-200), and section headings (Chaotic fixpoint iteration; Enhancing narrowing; Enforcing termination; Local generic solvers; Localized operator; Restarting in SLR; Side-effecting systems; Experimental evaluation).
- Context: sibling ingests in the same session (`bacchus-van-run-dynamic-variable-ordering-csps.ingest.md`, `chaff-engineering-an-efficient-sat-solver.ingest.md`) route into the KB's search-control cluster; read the Bacchus ingest and Chaff's footer links to see that cluster's current targets.

**Description / title listing scan (kb/notes):**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i "search|narrow|general|widen|precision|terminat|converg|fixpoint|fixed|iterat|loop|over-approx|approximat|abstraction|monoton|oscillat|revision|revis|phase|interleav|lossy|recover|propagat|sound|stop"` -- flagged: `generality-bought-to-avoid-counterexamples-is-paid-for-in`, `narrowing-bought-to-survive-review-is-paid-for-in-content`, `cost-sensitive-formalisms-for-tentative-theory-search`, `productive-deferral-requires-option-evidence-and-convergence`, `backtracking-keeps-lightweight-search-control-provisional`, `failure-explanation-changes-later-branch-decisions`, `lightweight-search-control-does-not-license-adoption`, `abstract-an-experience-only-when-you-can-state-the-boundary`.
- Descriptions read for all flagged; full bodies read for the generality, narrowing, and cost-sensitive notes.

**Topic indexes:**
- `kb/sources/README.md` -- describes the collection only; no curated per-topic index for sources.
- Tag READMEs listed (`kb/notes/*-README.md`); `rg -i "cost-sensitive|failure-explanation|backtracking"` over computational-model, learning-theory, and self-improving-systems READMEs returned no hits, so the search-control cluster is not curated in a tag head. No tag README complete-mark skips applied (snapshot has no `tags:`).

**Body search:**
- `rg -il "widening|narrowing operator|fixpoint|fixed point|abstract interpretation|Cousot" kb --glob '*.md' --glob '!kb/sources/.snapshots/**'` -- no source on abstract interpretation; hits on "narrowing"/"widening" are figurative uses (claim scope, vocabulary).
- `rg -n -i "abstract interpretation|over-approximat|fixpoint|fixed-point iteration|guaranteed to terminate|monotonic|cannot be recovered|irrecoverabl|interleav"` over notes, reference, agentic-systems, agent-memory-systems, sources -- mostly unrelated uses ("monotonic" gains, "interleaved" tool calls). `documentation-generates-the-system-rather-than-describing-it` and `commitment-not-derivation-creates-new-ground-truth` match "irrecoverable" in an unrelated sense (information recovery between documents); rejected.
- `rg -l -i "terminat|when to stop|stopping rule|convergence rule|oscillat|thrash"` over notes, sources, reference -- surfaced `kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md` and `kb/reference/full-improvement-pass-closure.md`; `rg -n -i "terminat|converg|stop|oscillat|precision"` in those plus productive-deferral and backtracking confirmed the proposal argues note refinement "is not convergent" and relies on a budget as a termination backstop, and the closure doc imposes a one-round closing stopping rule because "one repair reopens a different concern".
- `rg -n -i "fixed point|fixed-point" kb/notes` -- figurative uses only (`machinery-persists-by-warrant...`, `stale-self-description...`); rejected.
- `rg -l -i "widening|fixpoint|fixed point|abstract interpretation|static analysis" kb/agent-memory-systems kb/agentic-systems` -- no hits; both destinations skipped (no system in scope uses fixpoint iteration).

**Link following:**
- From `generality-bought...` footer to `narrowing-bought...`, `abstract-an-experience-only-when-you-can-state-the-boundary`, and the unearned-generality gate (instructions; excluded destination). Confirmed the pair uses "widening"/"narrowing" for claim vocabulary and claim subject, not for iteration operators.
- From the Bacchus/Chaff ingests to `cost-sensitive-formalisms...`, `failure-explanation-changes-later-branch-decisions`, `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation`. The cost-sensitive catalogue has families for discrepancy, iterative deepening, memory-bounded, real-time, conflict-directed, mind-change, pebble, restart, and budgeted-decision search, but none for approximate fixpoint iteration where termination is bought by precision loss.

**External:**
- No external prospecting (not authorised as a search surface). The paper's own URL is already known from the snapshot frontmatter.

## Connections Found

- [Original paper](https://arxiv.org/pdf/1503.00883) -- **derived-from**: the future ingest is worked out from this arXiv preprint (v1, 2015); state that the published journal version may differ.
- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: the source supplies a formal family the catalogue lacks, accelerated fixpoint iteration, in which a per-unknown bound on increases buys termination and the price is paid in precision rather than in search work or memory. It also shows that when a corrective downward step runs, relative to propagation, changes the result, and that termination depends on monotonicity and on finitely many encountered unknowns. The catalogue's Scope asks for source grounding of its families. Transfer caveat for the ingest: the paper's setting is sound over-approximation on a lattice with exact operators; a tentative theory has no such ordering by default.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- **compares-with**: shared axis is precision spent to buy a guarantee. Widening spends precision to guarantee termination; defensive abstraction spends precision to guarantee survival of counterexamples. Two parts of the paper bear on the note's repairs: (a) precision lost in one place and propagated through the system is generally not recoverable later, which matches the note's claim that diffuse abstraction cannot be audited or undone site by site; (b) restricting the operator to loop heads raised precision, which matches the note's "Abstraction must be localized to be auditable" section. The comparison is structural only: the paper's widening is a sound, formally specified operator, while the note's widening is a rhetorical move. The ingest should state that, and should flag the term clash noted under Flags.
- [Automated note refinement as search over a source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) -- **see-also**: the proposal argues that note refinement "is not convergent" and names runaway drift or non-termination as a risk held off only by a budget and an incumbent-survival counter. The paper gives formal sufficient conditions for an iterative up-and-down refinement to terminate (monotonic right-hand sides, finitely many unknowns). It also shows that combining an improving step with a coarsening step inside a standard iteration can fail to terminate even when those conditions hold, unless the iteration order is changed. That gives the proposal a precise statement of which assumptions its loop lacks.

## Bidirectional Candidates

- [Cost-sensitive formalisms for tentative theory search](../../../../notes/cost-sensitive-formalisms-for-tentative-theory-search.md) <-> source -- **evidenced-by** (notes-side label): once the ingest exists, the catalogue could add an "accelerated fixpoint iteration" family paragraph citing it. The family would add a budget the table does not yet name: precision surrendered to guarantee termination.

## Reverse-edge Candidates

- [Automated note refinement as search over a source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) → future ingest -- **evidenced-by** (reference → sources): the proposal's "Runaway drift / non-termination" risk could be bounded by the source's termination conditions and its example that a naive combined operator fails to terminate on monotonic systems. Uncommon edge per `kb/reference/COLLECTION.md`, so author it only if the proposal is revised to discuss termination conditions.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) → future ingest -- **evidenced-by** (notes → sources): only if the note's localization section is extended with the formal precedent (localized widening at loop heads raises precision). Low priority; the note's argument does not currently depend on it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) -- false friend. In the KB note, narrowing shrinks a claim's subject and can lower content to zero. In the paper, narrowing is a downward iteration that recovers precision. Linking them on the shared word would mislead an agent; the clash is recorded under Flags instead.
- [Full improvement pass closure](../../../../reference/full-improvement-pass-closure.md) -- its one-round closing stopping rule resembles the paper's practical remedies for non-monotonic systems (forcing termination by bounding how often iteration may switch back to widening). Rejected as redundant with the automated-refinement proposal candidate, since `see-also` should be used sparingly; revisit if the ingest's analysis leans on the non-monotonic remedies specifically.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- "convergence rule" is a keyword match. The note is about postponing one consequential choice, not about iterative approximation; no specific transfer.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md), [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md), [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- search-control cluster neighbours of the sibling CSP/SAT ingests. The paper has no branching, backtracking, or retained failure explanations, so no articulation beyond "also about search".
- [Dynamic variable ordering in CSPs (Bacchus and van Run)](../../../../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) and [Chaff](../../../../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) -- possible `compares-with` on "when a corrective step runs relative to propagation" (fail-first surfaces failures before they propagate; intertwined narrowing corrects before over-approximation propagates). Rejected as too loose: the Bacchus and Chaff mechanisms are about decision ordering in exact search, while this paper is about approximation in iteration. Revisit if a note on timing corrections before propagation is written.
- `documentation-generates-the-system-rather-than-describing-it`, `commitment-not-derivation-creates-new-ground-truth`, `machinery-persists-by-warrant-not-position-in-a-reflective-loop`, `stale-self-description-conceals-its-own-staleness` -- matched "irrecoverable" or "fixed point" in unrelated senses.

## Index Membership

None -- `kb/sources/README.md` is not a per-topic index, and no notes tag README curates the search-control cluster.

## Synthesis Opportunities

Possible, not yet warranted. The paper (correct before propagated over-approximation becomes unrecoverable), Bacchus and van Run (fail-first surfaces dead ends before exponential work), and `generality-bought...` (localize abstraction so each site can be audited) together suggest a claim about when to apply a corrective step. The claim would be that corrections are cheapest before a lossy or committing step's effects have propagated, and that localizing the lossy step keeps later correction possible. A note would need a mechanism that holds outside exact formal settings before it earns a place; leave it as a signal.

## Maintenance Observations

- Term collision: `kb/notes/` uses "widening" and "narrowing" figuratively for claim-scope moves (`generality-bought...`, `narrowing-bought...`, and the notes COLLECTION.md qualifier rule). In the paper these are formal fixpoint operators, and "narrowing" has the opposite effect on precision from the KB's "narrowing" of a claim's subject. If this source is ingested and cited from those notes, the citing text needs to disambiguate the two senses.
- The KB's search-control cluster (`cost-sensitive-formalisms...`, `failure-explanation...`, `backtracking...`, `lightweight-search-control...`) is not curated in any tag README. Three same-day solver ingests now route into it.

## Flags

- The source is far from the KB's core scope. Its value is as a formal precedent for termination bought with precision and for the timing of correction. The future ingest should make the transfer caveats explicit (sound lattice-based over-approximation vs fallible natural-language theories) so the `is-evidence-for` edge to the cost-sensitive catalogue is not read as confirmation of any claim about theory search.
- No ingest exists yet for this snapshot; all outbound candidates wait for it.
