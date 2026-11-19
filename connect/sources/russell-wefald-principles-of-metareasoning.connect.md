---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/russell-wefald-principles-of-metareasoning.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Principles of Metareasoning (Russell and Wefald, 1991)

**Source:** [Principles of Metareasoning](../../../../sources/.snapshots/russell-wefald-principles-of-metareasoning.md)

The source is an immutable snapshot. Under `kb/sources/COLLECTION.md` the snapshot is never the link author. Every outbound candidate below is meant for the matching ingest, `kb/sources/russell-wefald-principles-of-metareasoning.ingest.md`. That ingest **does not exist yet** at report time. Durable links from other collections must point to that ingest, never to the snapshot.

Source content used for judging: computations are actions. The net value of a computation is the expected utility of the external action it leads to, minus the utility of the default action, with time cost included (Sections 4.1 and 5.2). The ideal control rule is to keep doing the computation with the highest positive expected net value, then commit (Section 4.2). The paper separates partial computations, which do not commit to action, from complete ones, which do (Section 4.1). Meta-greedy and single-step approximations are myopic simplifications; relaxing either one alone would make the other exact (Section 5.3). Meta-control regresses, and the regress ends only in hardwired or default decisions or in policies built earlier by deliberation or adaptation (Section 3). Simon's substantive rationality "can only arise by prior design or adaptation" and cannot cover environments with much variation (Section 2). Sections 7 and 8 cover compilation, anytime composition and the metareasoning-versus-bounded-optimality gap.

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` § Outbound links. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources and external. Excluded: `kb/work/` and `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). No label covers tags. External prospecting was skipped: the only known external target is the source URL, which belongs to the ingest's `derived-from`.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'stop|budget|cost|frontload|compil|codif|precomput|deliberat|decide|decision|regress|allocat|spend|search|explor|heuristic|myopic|greedy|termin|enough|value|cheap|expens|scheduler|bounded|effort|when to'`. Flagged: the search-control cluster (open-ended-improvement, lightweight-search-control, backtracking, search-controller-tested, failure-explanation), cost-sensitive-formalisms, promotion-regress, codify-versus-llm heuristics, ad-hoc-explanation, frontloading (two notes), promote-only-when-value-exceeds-cost, a-methodology-governs-its-own-extension and information-value-is-observer-relative.
- `rg -m1 '^description:'` over the flagged files above, plus source ingests surfaced by name: `ls kb/sources/ | rg -i 'simon|good|horvitz|dean|anytime|bounded|ration|soar|search|heuristic|bandit|expect|decision|thinking|reason|compute|test-time|budget|overthink|stop'`. Flagged: provably-bounded-optimal-agents, primescientist-research-effort-allocation, pirolli-proximal-information-scent, chunking-in-soar, autoreason, sift and epiplexity.

**Topic indexes:**
- `kb/tags/improvement-loop-README.md` (`complete: true`). Its "Search and search control" block confirmed the theory search-control cluster as the main landing area. The by-tag rg was skipped because the head is complete.
- `kb/tags/computational-model-README.md` and `kb/tags/learning-theory-README.md`: no direct metareasoning or value-of-computation entry. learning-theory is `complete: true`, so its by-tag rg was skipped.
- `kb/tags/COLLECTION.md`: `participating` excludes `sources`, so ingests carry no tags and the tags destination has no authorised label anyway.

**Body search** (all scoped to `kb`, excluding `kb/work/**`, `kb/reports/**` and `.snapshots/**`):
- `rg -l -i 'metareason|meta-reason'`: **0 hits**. The KB has no metareasoning vocabulary yet.
- `rg -l -i 'value of computation|value-of-computation'`: **0 hits**.
- `rg -l -i 'value of information|value-of-information|VOI\b'`: information-value-is-observer-relative, model-discovery-agent-bayesian-experiment-design.ingest, epiplexity.ingest, learning-by-writing.ingest. Kept the first; the rest are topical only.
- `rg -l -i 'bounded rational|bounded optimal|resource-bounded|Simon'`: about 30 files, mostly incidental Simon mentions. Kept provably-bounded-optimal-agents.ingest and information-value-is-observer-relative; the soft-bound-traditions note was evaluated and rejected (below).
- `rg -l -i 'anytime'`: llmwiki-marimo review and one retained analysis, both incidental. Rejected.
- `rg -l -i 'Russell|Wefald|Horvitz'`: provably-bounded-optimal-agents.ingest and sutskevers-list/full.md. The PBO ingest is the direct successor work.
- `rg -l -i 'myopic|meta-greedy'`: **0 hits**.
- `rg -l -i 'stopping rule|when to stop|stop deliberat|deliberation cost'`: about 30 hits. Kept pirolli.ingest (its stopping rule comes from the same value quantity). Evaluated and rejected autoreason.ingest. Most of the rest are reference proposals or analyses that use "when to stop" procedurally.
- `rg -l -i 'infinite regress|regress'`: mostly "regression" in the testing sense. Kept promotion-selects-for-unreliable-activation (regress of activation dependencies).
- `rg -l -i 'reasoning effort|thinking budget|effort level|compute budget|deliberation' kb/agentic-systems kb/agent-memory-systems`: ReframeWeb, crewai-memory and retained-archive results. All incidental; none analyses decision-theoretic control of deliberation.
- `rg -n -i 'value of information|expected value|voi|bandit|bayes|decision.theor|good \(|howard' kb/theory/cost-sensitive-formalisms-for-tentative-theory-search.md`: **0 hits**. The catalogue lists ten model families and does not include decision-theoretic metareasoning.

**Link following:**
- provably-bounded-optimal-agents.ingest → its Connections Found (deployed-system unit of learning, warranted-autonomy-by-oracle-domain, methodological/computational closure). These are the natural neighbours for bounded optimality. For R&W, only the deployed-system note was weighed, and it was rejected: PBO already carries that edge more precisely.
- primescientist.ingest → a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation (its main edge). This confirmed that the KB's search-control cluster is where effort-allocation evidence lands.
- pirolli.ingest → information-value-is-observer-relative and soft-bound-traditions (its own edges). These confirmed that the value-per-cost framing exists in the KB only through human foraging, not through computation-as-action.
- lightweight-search-control → open-ended-improvement, backtracking, failure-explanation (one hop through the improvement-loop head).

## Connections Found

All of the following are candidates for the future `.ingest.md`.

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) -- **is-evidence-for**: R&W define a computation's value entirely by how it changes the agent's later action choice (V(Sj) = U([αSj, [Sj]]) − U([α])). A computation that leaves the choice unchanged has zero value. This is a decision-theoretic precedent for the note's operative test. It bears on the claim without corroborating it, since it is a formal definition, not a test the note could have failed.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) -- **compares-with**: shared axis is the authority of a deliberative step. R&W's partial computations change internal state without committing to external action; complete computations commit. This maps closely onto lightweight control versus adoption. R&W also give an allocation rule (highest expected net value, stop at none positive), which the note explicitly declines to specify.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- **is-evidence-for**: the catalogue omits the family that prices "should I compute further?" directly. R&W supply that family: value of computation, time cost, the ideal stop-when-no-positive-net-value rule, and the meta-greedy and single-step myopic approximations with their joint-relaxation property. This is a candidate missing row for the catalogue, not a claim that it is the right model.
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) -- **compares-with**: shared axis is how a regress of control terminates. R&W argue that meta-level control regresses without end ("no computation can be executed until a computation has been executed to decide on it"). It ends only in hardwired or default actions or in policies built by prior deliberation or adaptation. The note ends a regress of activation dependencies at a live external trigger. Comparing the two separates "root by prior design" from "root by external event".
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- **is-evidence-for**: R&W explicitly extend information-value theory (Howard, Good) to computations by resource-bounded agents. A computation's value is relative to the agent's current estimates, its decision and its time cost. This gives the note's bounded-rationality bullet, now attributed only to Simon, a formal computation-side source.
- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) -- **compares-with**: shared axis is precompiling a decision versus deliberating at run time. R&W's Section 2 argues that substantive (compiled) rationality "can only arise by prior design or adaptation" and becomes intractable for the designer under significant environmental variation, so situation-dependent allocation is needed. Section 3 adds that some decisions must still be hardwired. This is a classical framing of the same codify/interpret boundary. It predates LLMs, so the transfer argument is owed.
- [Provably bounded-optimal agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) -- **compares-with**: shared axis is the optimality target for a resource-bounded agent. R&W control individual computations by expected value; Russell & Subramanian (1995) move optimality to the program/architecture/environment level. R&W's own Section 7 flags the gap ("Instantaneous metareasoning yields bounded optimality when it is available, but when it has costs itself, the picture muddies"), which the PBO paper takes up.
- [PrimeScientist: strategic allocation of research effort](../../../../sources/primescientist-research-effort-allocation.ingest.md) -- **compares-with**: shared axis is charging deliberation against the same budget as action. PrimeScientist charges plan construction and execution to one token budget with a supplied budget-sensitive selection rule. R&W derive time cost as part of the computation's net value. The comparison shows PrimeScientist's schedule as a hand-supplied approximation of R&W's ideal control rule.
- [Pirolli: proximal information scent and distal content](../../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md) -- **compares-with**: shared axis is one value estimate that both selects the next step and stops. Pirolli's scent ranks links and sets patch abandonment. R&W's net value of computation ranks computations and terminates deliberation when none is positive. Both join selection and stopping through one quantity. Pirolli's ingest already flags that joining as a missing deep-dive.

## Bidirectional Candidates

- [Provably bounded-optimal agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) <-> source -- **compares-with**: under `kb/sources/` rules the PBO ingest may author `compares-with` back to the R&W ingest. A reader of the bounded-optimality paper benefits from the predecessor's computation-level control theory, and R&W's Section 7 states the open problem PBO addresses.

## Reverse-edge Candidates

All targets must be the future `russell-wefald-principles-of-metareasoning.ingest.md`, never the snapshot. Labels are drawn from `kb/theory/COLLECTION.md` (theory → sources: `evidenced-by`, `abstracted-from`, `derived-from`, `see-also`).

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) → ingest -- **evidenced-by**: the context phrase must say "qualifies/bounds" or "prior formal statement", not corroboration. R&W's definition was not a test the note could have failed. This is the strongest reverse edge: the note currently has no external grounding for its test.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) → ingest -- **see-also** or a new catalogue section citing the ingest inline. The catalogue is exploratory, so a new "decision-theoretic metareasoning" family section with an inline citation is the better repair than a footer link.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) → ingest -- **evidenced-by** (bounds): the partial/complete computation distinction is an independent prior statement of the same authority split, and the R&W allocation rule marks what the note's Scope section leaves open.
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) → ingest -- **evidenced-by** (qualifies): R&W's alternative regress terminus (prior design or adaptation) bounds the "only at an external trigger" wording in the title.

## Off-authorisation Candidates

- [Improvement-loop tag head](../../../../tags/improvement-loop-README.md) -- the source substantively treats search control (allocation, stopping), but `sources` is not a participating tag collection and no sources label targets `kb/tags/`. Reject as off-scope for the ingest. If R&W becomes a theory note's evidence, the head reaches it through that note.

## Raw Text Candidates

None

## Rejected Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- PBO.ingest already supplies the program/architecture/environment basis. R&W's computation-level theory adds nothing specific to this claim.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../theory/open-ended-improvement-allocates-search-before-evaluation.md) -- R&W also allocate before outcomes are known, but they assume a fixed action set and prior statistics on value revisions. The note argues that open-ended search lacks exactly these. Linking lightweight-search-control and failure-explanation carries the useful signal; a third cluster link would be a spray.
- [A search controller is tested by what it brings to stronger evaluation](../../../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- R&W evaluate their controller by final decision quality in game play, which only loosely fits. PrimeScientist is the better evidence for this note.
- [Ad hoc explanation can be rational when error is cheap and local](../../../../theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) -- the "deliberation cost versus error cost" framing matches Good's type-II rationality as cited by R&W, but R&W do not discuss retention or reuse, which carry the note's argument. Keyword-level overlap only.
- [Promote only when future value exceeds maintenance cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- value-minus-cost has the same shape, but it is about memory retention, not computation. Forcing the link would confuse a reader.
- [Frontloading spares execution context](../../../../theory/frontloading-spares-execution-context.md) -- R&W's compilation of reasoning (Sections 3 and 7) is adjacent, but the paper leaves compilation explicitly outside its framework. The codify-versus-LLM edge already carries the precompute-versus-deliberate axis.
- [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../theory/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) -- "meta-decisions" there are methodological, not computational control. Name overlap only.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- its traditions are about selecting what to load under a bound. R&W are about selecting what to compute. A row could be argued for, but that is a theory-side edit, not a strong ingest edge.
- [Autoreason](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- "knows when to stop" uses an empirical stop-when-incumbent-survives criterion. It shares no mechanism with expected net value, so the comparison would be keyword-driven.
- [SIFT](../../../../sources/sift-self-improvement-fast-tree-search.ingest.md), [Epiplexity](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md), [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) -- respectively: cheap judgments guiding search without a value-of-computation model; observer-bounded information without action selection; Soar is mentioned by R&W only as the universal-subgoaling contrast in Section 7. All are too thin to help.
- `kb/agentic-systems/`, `kb/agent-memory-systems/` -- no review analyses decision-theoretic control of reasoning effort. Destination skipped with no candidates.

## Index Membership

None. Source ingests are not tag-bearing (`kb/tags/COLLECTION.md` participating list excludes `sources`).

## Synthesis Opportunities

R&W (net value of computation, myopic approximations, stop when none positive), [Pirolli](../../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md) (one scent quantity both selects and stops) and [PrimeScientist](../../../../sources/primescientist-research-effort-allocation.ingest.md) (a supplied budget-sensitive selection rule charging planning and execution together) together suggest a higher-order claim for the theory search-control cluster. **Search control that selects the next branch and decides when to stop is one value-of-further-work estimate, and stopping rules defined apart from selection are approximations of it.** [Lightweight search control](../../../../theory/lightweight-search-control-does-not-license-adoption.md) explicitly declines to say how search should be allocated, so the gap is real. The synthesis owes the LLM transfer argument: R&W assume prior statistics on value revisions, and open-ended search usually lacks them.

## Maintenance Observations

- The KB has **no metareasoning or value-of-computation vocabulary**: `metareason`, `value of computation`, `myopic` and `meta-greedy` all return 0 hits outside work and reports. The search-control cluster (improvement-loop head) develops lightweight control, backtracking and failure-explanation tests without citing the decision-theoretic tradition that names computation selection. This is a repeated unnamed mechanism and a candidate gap for a theory note or definition.
- `cost-sensitive-formalisms-for-tentative-theory-search.md` catalogues ten budget-exposing model families and omits decision-theoretic metareasoning, which prices the continue/stop decision directly.
- The target snapshot has no tracked `.ingest.md` yet. Every candidate here is blocked until that ingest exists, because theory may link only to the ingest.

## Flags

- **Ingest prerequisite:** all Connections Found and Reverse-edge Candidates assume `kb/sources/russell-wefald-principles-of-metareasoning.ingest.md`. It is currently absent; a concurrent `cp-skill-ingest` agent may be creating it.
- **Transfer caveat:** R&W's results assume a fixed external action set, a known utility function, and prior distributions over how computation revises value estimates. Every edge into an LLM-agent claim must state that the transfer is structural (computation as action, value through changed choice, regress terminus), not quantitative.
- **Tension to flag, not resolve:** R&W's regress terminus (prior design or adaptation) and the promotion note's "regress ends only at an external trigger" may disagree, or may be talking about different regresses (control of computation versus activation of retained content). A reader authoring that edge should decide which.
