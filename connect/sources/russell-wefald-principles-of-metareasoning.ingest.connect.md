---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/russell-wefald-principles-of-metareasoning.ingest.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Ingest: Principles of Metareasoning (Russell and Wefald, 1991)

**Source:** [Ingest: Principles of Metareasoning](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md)

The ingest already carries eight inline connections (failure-explanation, lightweight search control, cost-sensitive formalisms, information value, bounded-optimal agents, PrimeScientist, Pirolli, codify-versus-LLM). All eight paths exist. This report lists only new candidates.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` outbound section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. The label table gives `compares-with` for theory, sources, agent-memory-systems and agentic-systems; `is-evidence-for` for theory and agent-memory-systems; `see-also` only for reference. External prospecting was skipped because no external target was supplied.

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (432 titles), filtered with `rg -i 'search|control|cost|budget|stop|decision|controller|alloc|branch|default|deliberat|regress|myopic|greedy|information|value|fixed decomposition|codif|precompil|select|exchange|incommensur|trade'`. Flagged: a-search-controller-is-tested..., open-ended-improvement-allocates-search..., backtracking-keeps-lightweight-search-control..., learning-inside-a-fixed-decomposition..., promotion-selects-for-unreliable-activation...regress..., a-methodology-governs-its-own-extension..., promote-only-when-value-exceeds-cost, intent-controls-choices..., choosing-what-to-learn..., opposed-recompute-factors (found later through the body search).

**Description reads:** I read `rg -N '^description:'` for the 13 flagged theory notes and for the sources autoreason, model-discovery-agent, epiplexity, competence-theory, provably-bounded-optimal, primescientist, optimal-ordered-problem-solver, weco-autoresearch-vs-classical-hpo, huxley-godel-machine, harnesscompass and socratic-agents.

**Topic indexes:**
- `kb/tags/improvement-loop-README.md` (complete: true): its "Search and search control" section is the cluster the ingest lands in. No source carries this tag (`rg -l '^tags:.*improvement-loop' kb/sources` returned nothing), so I skipped the by-tag rg.
- `kb/tags/learning-theory-README.md` (complete: true; working-tree edit adds a "Source analyses" section), `kb/tags/self-improving-systems-README.md`, `kb/tags/evaluation-README.md` (lists the search-controller note under "Oracles and judges"), and the discovery and computational-model descriptions.
- `rg -n -i 'russell|bounded-optimal|primescientist|chaff' kb/tags/` returned nothing. No tag head links this ingest or its nearest source neighbours.

**Body search:**
- `rg -il 'metareason|value of computation|bounded.optimal|bounded rationality|meta-greedy|anytime|deliberation cost|opportunity cost|value of information|stopping rule|when to stop'` across theory, reference, agentic-systems, agent-memory-systems, tags and sources returned 30 files. Matches outside the ingest's existing links were incidental ("stopping rule" in full-improvement-pass-closure and ADR 081; "anytime" nowhere relevant). Kept for follow-up: autoreason, model-discovery-agent and epiplexity.
- `rg -l -i 'horvitz|howard|expected utility|budget' kb/sources --glob '*.ingest.md'` returned about 30 files. Flagged: weco-autoresearch-vs-classical-hpo (budget-constraint inconsistency), huxley-godel-machine (separates expansion from evaluation; immediate score versus descendant productivity) and optimal-ordered-problem-solver (budget split).
- `rg -n -i 'exchange rate|opportunity cost|computation cost'` across theory, sources, reference and agentic-systems returned five hits. Kept: opposed-recompute-factors (comparison currency; incomparable without an exchange rate), cost-sensitive-formalisms line 42 (already linked) and chaff ingest item 3 ("charge controller overhead when comparing search heuristics"). Rejected: ADR 079/082 and the archived review-link-budget proposal (see Rejected).
- `rg -l -i 'search control|controller|value of computation|exchange rate|net value'` in reference, agentic-systems and agent-memory-systems returned only incidental uses of "controller" and budget ADRs. Nothing in agentic-systems or agent-memory-systems passed the articulation test.

**Link following:**
- From a-search-controller-is-tested...: its footer leads to lightweight search control, open-ended allocation, backtracking, failure-explanation, diagnostic-richness and an-experiment-identifies-only-the-contrast. These are the same cluster. The note itself says controllers are compared "under matched tasks, resources, and downstream evaluation", which R&W's priced-cost comparison directly qualifies.
- From learning-inside-a-fixed-decomposition: its section "Improvement inside a boundary does not test the fixed layer" matches Extractable Value item 3 (R&W's results compare control policies within one fixed base-level search).
- From promotion-selects...regress: its "activation regress" ends at an external trigger; R&W's meta-control regress ends in prior design or adaptation (item 7).
- `rg -n 'sources/'` over the five search-control theory notes returned nothing. None of the cluster's notes yet cites any source, which shapes the reverse-edge pass.

## Connections Found

- [A search controller is tested by what it brings to stronger evaluation](../../../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **compares-with**: axis: how two controllers are compared. The note requires matched tasks and resources and judges routing by its downstream consequences. R&W judge controllers by outcome net of computation cost, price unequal resources into one utility, and sweep the exchange rate. This is the note test 1 operationalizes, and the ingest names it nowhere.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: R&W's DTA\*/MGSS results hold the evaluation function and cost ratio fixed. The paper therefore shows only that a control policy improves within one base-level decomposition (Extractable Value item 3). The meta-greedy barrier is a depth-1 limit that no tuning inside the controller can remove. This is a formal-domain instance of "improvement inside a boundary does not test the fixed layer".
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) -- **compares-with**: axis: where a control regress terminates. R&W's meta-control regress ("no computation can be executed until a computation has been executed to decide on it") ends in hardwired defaults or in policies built by earlier adaptation. The note's activation regress ends at a live external firing event. Item 7 currently stands as just-a-reference with no landing note.
- [Opposed recompute factors do not decide documentation segmentation](../../../../theory/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) -- **compares-with**: axis: comparing alternatives that consume non-substitutable resources. The note holds such values incomparable without a defensible exchange rate. R&W instead report the comparison across a range of exchange rates (Extractable Value item 2). An agent deciding between "refuse to compare" and "sweep the rate" needs both.
- [Ingest: Chaff](../../../../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) -- **compares-with**: axis: charging controller overhead when comparing search heuristics. Chaff counts only runtime because decision counts hide unequal heuristic cost. R&W put time cost inside net value. Both say a controller is judged net of what it consumes, and test 1 needs that premise.
- [Ingest: Weco AutoResearch vs classical HPO](../../../../sources/weco-autoresearch-vs-classical-hpo.ingest.md) -- **compares-with**: axis: comparing two controllers with unequal resource consumption. The ingest records that Weco states equal GPU-hours and also a token-inclusive monetary budget, which are different constraints. R&W's single-utility pricing with an exchange-rate sweep is the discipline whose absence that limitation names.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- **compares-with**: axis: myopic versus descendant-valued scoring of the next expansion. R&W's single-step assumption undervalues computations that matter only by enabling later ones. HGM argues that immediate benchmark score mis-ranks parents and that clade metaproductivity predicts better. HGM also separates expansion from evaluation spending. HGM is an empirical case of the failure that Extractable Value item 4 predicts.

## Bidirectional Candidates

- [Ingest: Provably bounded-optimal agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) <-> source -- **compares-with**: the ingest already links forward to its successor. The bounded-optimality ingest has no back-link. The return path helps a reader who arrives at program-level optimality and needs the metareasoning gap it was built to close.
- [Ingest: Chaff](../../../../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) <-> source -- **compares-with**: Chaff item 3 says it qualifies the search-controller note. A return link to R&W gives that qualification its decision-theoretic form.

## Reverse-edge Candidates

These would be authored under `kb/theory/COLLECTION.md` rules. Theory notes are limited to five unquoted sources, and the ingest has no retained quotes yet, so ground through `cp-skill-ground` first.

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) → source -- **evidenced-by**: the context phrase must say that the source bounds the claim and does not corroborate it. A definition from 1991 is not a test the note could have failed, as the ingest itself notes. The prior formal statement is "value only through changed action choice", with Δ = 0 when the choice is unchanged.
- [A search controller is tested by what it brings to stronger evaluation](../../../../theory/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) → source -- **evidenced-by** (qualifies): R&W show controllers compared with priced unequal resources, not only under matched resources. This qualifies the note's "matched ... resources" condition.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) → source -- **see-also**, or an inline citation inside a new family entry: Extractable Value item 6 proposes adding value of computation, stop-when-none-positive and the two myopic approximations as a missing family. The catalogue currently cites no sources.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) → source -- **evidenced-by** (bounds): the source supplies an allocation and stopping rule, which the note leaves unspecified. The rule assumes numerical utilities that Commonplace lacks (item 5).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../theory/open-ended-improvement-allocates-search-before-evaluation.md) -- topically close (Gödel-machine expected-utility switching). The note argues allocation precedes evaluation for reasons that are explicitly "not merely economic". R&W assume a standing default action and known estimate revisions, so they do not address the note's claim. Linking would blur that boundary.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) -- applies the same null-effect test as failure-explanation, to intent. The ingest already reaches that test through failure-explanation, and a second edge adds no new axis.
- [Promote only when future value exceeds maintenance cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- value-minus-cost shape only. It concerns memory retention, not choosing computations, so the match is at keyword level.
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) -- R&W's controller is irrevocable once committed and has no backtracking. No shared axis.
- [Ingest: Optimal ordered problem solver](../../../../sources/optimal-ordered-problem-solver.ingest.md) -- has a fixed budget split but no value-based selection of computations. The overlap is weak.
- [Ingest: Autoreason](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- "incumbent survival" resembles R&W's default action, but autoreason's stopping is judge-based, not value-of-computation. Plausible but thin; not kept.
- [Ingest: Epiplexity](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) and [Ingest: Model discovery agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- bounded observers and experimental-design information value are both reachable through the existing information-value-is-observer-relative link. A direct edge would duplicate it.
- [ADR 082](../../../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md) and the archived review-link-budget proposal -- both record that observed stop points do not identify the exchange rate between artifact-switching and bytes. Only `see-also` is authorised for reference. An agent reading the ingest gains nothing operational from these ADRs, and the shared axis is already carried by the opposed-recompute note. See Synthesis.

## Index Membership

- [improvement-loop tag head](../../../../tags/improvement-loop-README.md) -- "Search and search control" section: the ingest is the formal basis for that cluster's value and stopping questions. The head is `complete: true`, so assigning `tags: [improvement-loop]` to the ingest requires adding a head entry. That needs a source-analyses subsection, because no source carries this tag yet.
- [learning-theory tag head](../../../../tags/learning-theory-README.md) -- weaker fit through the improvement-loop and self-improving-systems children. The head's new "Source analyses" section (uncommitted working-tree edit) would be the place. Prefer improvement-loop alone unless the parent is wanted.

## Synthesis Opportunities

The exchange-rate problem recurs across several notes and sources with no shared account. The opposed-recompute note says to stay incomparable without a defensible rate. Cost-sensitive formalisms says to scalarize only warranted components. ADR 079/082 deferred a price because stop points do not identify the rate. Weco mixes two budget constraints. R&W sweep the rate and report wins at every rate. Together these suggest a candidate claim: when no exchange rate is defensible, a controller comparison is reportable as dominance across a swept rate range, and it stays incomparable only where the preference flips inside that range. Test 1 in the open-ended-work-economics workshop is the natural place to try this before any note is written.

## Maintenance Observations

- The ingest has no `tags:` field, although `kb/sources/COLLECTION.md` says tracked ingests carry tags. Its nearest neighbours (provably-bounded-optimal-agents, primescientist, chaff) also showed no tags in the scoped rg. This may be a broader gap in ingest tagging.
- None of the five search-control theory notes in the improvement-loop head cites any `kb/sources/` ingest. The cluster now has at least four relevant ingests (R&W, bounded-optimal, PrimeScientist, Chaff) and no inbound source edges.

## Flags

- Tension: the opposed-recompute note treats a missing exchange rate as grounds for incomparability, while R&W treat it as a parameter to sweep. These are not contradictory, since a sweep can still show a flip, but the two should not be cited as agreeing.
- The ingest's Quotes section is empty. Any reverse edge from a theory note will count against that note's five-unquoted-source limit until quotes are retained.
- Not a split candidate: the ingest is one source analysis, and its connections span one cluster (search control and controller cost) plus two adjacent areas.
