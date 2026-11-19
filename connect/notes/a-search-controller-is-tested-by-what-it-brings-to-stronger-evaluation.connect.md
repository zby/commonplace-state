---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: A search controller is tested by what it brings to stronger evaluation

**Source:** [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md)

## Discovery Trace

**Authorisation and curated heads:**

- Read the source note, `kb/reports/types/connect-report.md`, and `kb/notes/COLLECTION.md` in full. The notes contract authorises prospecting in notes, types, reference, agent-memory systems, agentic systems, sources, instructions, and already-known external targets; it excludes `kb/work/`. No external target was supplied, so external prospecting was skipped.
- Read `kb/notes/README.md` and the source-tag heads `foundations-README.md`, `evaluation-README.md`, and `self-improving-systems-README.md`. None declares `complete: true`, so no by-tag search was skipped.
- Read the destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The types surface had no plausible trigger beyond the already-resolved note contract. Instructions were assessed under their exceptional-outbound posture and usual inverse `instruction -> note` direction.

**Complete title and description scans:**

- Generated the complete title surface once per local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg -N --no-heading '^description:\s*' kb/<destination>/ --glob '*.md'` across all seven local destinations.
- Ran the required tag-specific description queries for `foundations`, `evaluation`, and `self-improving-systems`, in the form `rg -l '^tags:.*<tag>' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*'`. These surfaced the provisional-control cluster, delayed-feedback account, diagnostic-richness note, candidacy/verdict distinction, and acceptance-oracle comparison.

**Focused body search:**

- Notes: `rg -l -i 'search controller|stronger evaluation|downstream evaluation|provisional.*branch|branch decision|informative failure|backtrack|diagnostic richness|matched tasks|counterfactual.*branch' kb/notes/ --glob '*.md'` -- kept the backtracking, failure-explanation, project-state specialization, diagnostic-richness, matched-contrast, and weak-discrimination candidates. It also surfaced the already-linked lightweight/open-ended notes and the rejected program-theory, proposal-loop, and path-health neighbours.
- Cross-system and source surface: `rg -l -i 'metaproduct|parent[- ]selection|exploration controller|value of information|query planning|discriminating probes|matched.*budget' kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- kept Huxley-Gödel Machine for descendant-productivity selection and Model Discovery Agent for experiment-routing outcomes. Darwin Gödel Machine, HyperAgents, AlphaDev, Meta-Harness, and the automata-learning benchmark were evaluated as one-hop comparisons but not retained as separate outbound edges.
- Reference: `rg -l -i 'trajectory-aware|matched repository tasks|search.*evaluation|controller|branch.*evaluation' kb/reference/ --glob '*.md'` -- evaluated the trajectory-aware workflow-evaluation and declared-objective ablation proposals; both test different objects from branch allocation and were rejected.
- Instructions: `rg -l -i 'search controller|branch.*evaluation|candidate.*assessment|trajectory-aware|matched.*task' kb/instructions/ --glob '*.md'` returned no candidates. Types: `rg -l -i 'search controller|branch.*evaluation|candidate.*assessment' kb/types/ --glob '*.md'` returned no candidates. These searches produced no relevance scores.

**Link following and inbound check:**

- Ran `rg -n --fixed-strings 'a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md' kb --glob '*.md' --glob '!reports/cache/connect/**'`. The only inbound link is in the workshop `kb/work/theory-mediated-self-improvement-series/shared-model.md`; it was recorded for discovery but excluded as an authorised destination.
- Followed the source's two authored links. The open-ended-improvement note exposes an explicit unanswered question about evaluating allocation without exhaustive counterfactual search, while the lightweight-control note explicitly leaves effectiveness unspecified. Those gaps make return links to this source independently useful rather than merely reciprocal.
- Followed one hop through the kept note candidates and through Huxley-Gödel Machine and Model Discovery Agent. The Huxley neighbourhood exposed Darwin Gödel Machine's greedy-versus-branching predecessor and Meta-Harness's distinct diagnostic-access axis. The MDA neighbourhood exposed FALSIFYBENCH, DiscoverPhysics, and the automata-learning benchmark; these confirmed that probe informativeness, hypothesis construction, and final verification are separable, while MDA supplies the closest tested controller comparison.
- Loaded every kept target's substantive claim and limitations, then verified all kept, return-link, reverse-edge, rejected, index, and synthesis paths with `test -f`.

## Connections Found

- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **mechanism**: explains how the source's “improved recovery” consequence works by restoring an earlier usable state and redirecting search after contrary evidence, without retroactively validating the original branch choice.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **mechanism**: operationalises the source's “informative failures” outcome by requiring retained failure understanding to change later scope, priority, probing, continuation, or abandonment.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- **extends**: develops one candidate controller implementation and proposes the matching intervention test: withhold or perturb project state while holding model, tools, symbolic state, and task fixed, then compare later branch consequences.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **grounds**: explains why discriminating evidence and inspectable failures are controller value even before a candidate is accepted: they improve the causal search context available to the next proposer independently of oracle strength.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **grounds**: supplies the causal limit behind the source's matched comparison; controller quality can be attributed only when the controller is the varied treatment and tasks, resources, downstream evaluation, and other consequential machinery are held fixed or reported as a bundle.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **contrasts**: separates the controller's candidate-availability and routing bottleneck from the downstream oracle's acceptance discrimination, so a quality gap among accepted outputs is not automatically evidence that the controller routed badly.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- **evidenced-by**: directly reports that immediate node performance can mis-rank future lineage productivity and tests a descendant-outcome selection target, while its scheduling confound and benchmark-local scope bound the transfer. A future authored source use must carry `(snapshot required)` because the ingest retains no quotes.
- [Ingest: Model Discovery Agent: LLM-assisted Bayesian Experiment Design](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- **evidenced-by**: compares experiment-routing policies through later interventional forecasts and experiment efficiency; value-of-information routing is not always better than LLM or random acquisition, which both demonstrates the proposed evaluation shape and rejects a universal controller verdict. A future authored source use must carry `(snapshot required)` because the ingest retains no quotes.

## Bidirectional Candidates

- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) <-> source -- **extends** from the target side: this source answers that note's explicit open question by giving a comparative controller test that does not require exhaustive knowledge of the best counterfactual branch.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) <-> source -- **extends** from the target side: this source supplies the effectiveness criterion that note deliberately leaves unspecified while preserving its limited-authority boundary.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) <-> source -- **grounds** from the target side: the general downstream-consequence criterion explains why that note's withholding and perturbation test must measure later branch effects rather than prompt plausibility.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) <-> source -- **is-evidence-for** from the target side: its metaproductivity-performance mismatch bears materially on the source's controller-quality claim and gives the ingest's recommended selection-target-alignment note a current landing.
- [Ingest: Model Discovery Agent: LLM-assisted Bayesian Experiment Design](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) <-> source -- **is-evidence-for** from the target side: its controlled probe-allocation comparisons bear on the source's claim that controllers should be judged by evidence and candidates delivered downstream.

## Reverse-edge Candidates

- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -> source -- **grounds**: its HyperAgents case distinguishes making parent selection editable from showing that the learned selector is good; this source supplies the missing controller-quality criterion for interpreting that negative comparison.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- rejected as a duplicate route to the authority distinction already discharged by the source's authored link to lightweight search control; it adds a broader staged-evidence vocabulary but no controller-specific evaluation criterion.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as too general and already reachable through both authored neighbours; a direct edge would repeat the search-versus-acceptance decomposition without advancing the controller test.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- rejected as an additional direct edge because the authored open-ended-improvement link already routes to it, and the candidate develops the delayed-feedback setting rather than a distinct controller-comparison rule.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) -- rejected because it identifies hidden fallback and infrastructure-health ambiguity within one execution path, not the distributional quality of a policy allocating search among branches; the selected experimental-contrast note states the relevant attribution limit more generally.
- [Ingest: Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) -- rejected as a separate outbound evidence edge because Huxley-Gödel Machine is the controlled successor targeting the exact immediate-score-versus-descendant-productivity mismatch. DGM remains a useful one-hop predecessor, but its principal selector ablation is not compute-matched.
- [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md) -- rejected because the code-grounded review establishes selectable parent policies and lineage replay but reports no with/without-lineage or controller-quality comparison; it is an implementation case, not evidence for the source's evaluation rule.
- [Ingest: Faster sorting algorithms discovered using deep RL](../../../../sources/faster-sorting-algorithms-discovered-using-deep-rl.ingest.md) -- rejected because its learned-search versus stochastic-search comparison changes objective access and a larger treatment bundle; it cannot isolate controller quality as cleanly as the Huxley and MDA cases.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- rejected because it evaluates workflow compliance and hidden process failures after a transforming run, not which search branches a controller should allocate for further work.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- candidate entry because the source gives the tag a general controller-evaluation principle: compare routing policies by downstream candidates, evidence, failure information, and recovery under matched conditions rather than by isolated branch outcomes.

## Synthesis Opportunities

- [This source](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md), [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), and [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) together imply three separable outer-loop evaluation surfaces: whether the controller's selection target tracks productive downstream consequences, whether retained evidence lets the proposer explain prior attempts, and whether the final oracle discriminates acceptance correctly. Huxley-Gödel Machine's ingest independently names this three-factor programme, but no current note owns the synthesis.

## Maintenance Observations

None

## Flags

None
