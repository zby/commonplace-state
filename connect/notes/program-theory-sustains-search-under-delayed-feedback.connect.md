---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/program-theory-sustains-search-under-delayed-feedback.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Holding a program theory means sustaining coherent search under delayed feedback

**Source:** [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md)

## Discovery Trace

**Source and authorisation:**

- Read the source note, `kb/notes/COLLECTION.md`, and `kb/reports/types/connect-report.md` in full. The source claim joins Naur's theory-holder test to the least-warrantable open-ended modification decision: a partial, fallible program theory must causally shape search, provisional evaluation, recovery, outcome interpretation, and later revision while decisive evidence is delayed.
- The notes contract authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `work`. The reserved `external` destination was skipped because no external target was supplied or already loaded as a candidate.
- Verified that every authorised local destination has a `COLLECTION.md`. Read the main `README.md` for each destination. Read the two tag heads selected by the source frontmatter: `kb/notes/foundations-README.md` and `kb/notes/self-improving-systems-README.md`. Neither declares `complete: true`, so neither by-tag description sweep was skipped.

**Fresh title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the seven authorised local destinations. The notes surface highlighted the open-ended-search, lightweight-control, backtracking, failure-explanation, search-controller, natural-language project-state, system-use, and Commonplace-revision cluster. The other title surfaces highlighted Exo, Reflexion, Agent-R, HyperAgents, Compound Engineering, ScienceFlow, and the Naur ingest for closer evaluation.
- Ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `self-improving-systems` query. These kept the same theory-series cluster and exposed `a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md` as an additional candidate.
- Ran filtered destination description listings with `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'theory|search|feedback|backtrack|recovery|self-improv|revision'` over `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`. The types title surface had no plausible trigger beyond structural contracts, so body prospecting there was skipped. The instructions filter produced no candidate, consistent with the collection's exceptional outbound posture and the absence of an operationalization of this specific claim.

**Notes body search:**

- `rg -n -i "program theory|theory-holder|coherent modification" kb/notes/ --glob "*.md"` -- kept the Naur basis, delayed-search, residue, and system-use neighborhood; existing inbound links from the open-ended-search, backtracking, residue, warranted-transfer, theory-mediated-path, and system-use notes were recorded rather than re-proposed as reverse edges.
- `rg -n -i "delayed (evidence|feedback)|later (demand|consequence)|longitudinal" kb/notes/ --glob "*.md"` -- kept open-ended search, search-controller evaluation, and system-use selection; rejected generic longitudinal-maintenance hits.
- `rg -n -i "backtrack|rollback|recovery" kb/notes/ --glob "*.md"` -- kept the explicit backtracking mechanism and failure-explanation read-back; rejected scheduler and generic recovery matches that did not preserve a theory-guided branch relation.
- `rg -n -i "search control|allocat(e|es|ing).*search|provisional evaluation" kb/notes/ --glob "*.md"` -- kept lightweight control and the stronger-evaluation test because they distinguish branch allocation from adoption.
- `rg -n -i "withhold|replac(e|ing).*theory|counterfactual" kb/notes/ --glob "*.md"` -- kept the natural-language project-state perturbation and system-use comparison designs; rejected generic counterfactual-method notes.

**Other-destination body search:**

- Ran `rg -n -i "program theory|coherent modification|theory-guided|delayed (feedback|evidence)|backtrack|self-improv" kb/<destination>/ --glob "*.md"` over `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Reference hits (`where-change-candidates-come-from-in-commonplace.md`, the tag-readme trace, and the declared frame) describe Commonplace state or one short trace but do not test a theory-holder across novel demands; none passed the articulation test.
- Agent-memory hits led to full or focused reads of Reflexion, Agent-R, and HyperAgents. Reflexion passed as bounded evidence for failure-guided retry and as a limit case; Agent-R and HyperAgents did not expose an addressable program theory or the required delayed theory read-back.
- Agentic-system hits led to Exo, Compound Engineering, and GBrain. Exo passed as bounded evidence for the rollback-and-preserved-record submechanism and for the insufficiency of shallow oracles. Compound Engineering and GBrain did not establish longitudinal theory-guided program modification.
- Source hits led to `programming-as-theory-building.ingest.md` and ScienceFlow. Naur's ingest passed as primary conceptual lineage. ScienceFlow's recoverable checkpoints lacked the program-theory causal relation and were rejected.
- No instruction implemented the claim's ordering, defaults, or stopping conditions, so no `operationalized-from` candidate was retained and no inverse `instruction -> note` edge was proposed.

**Link following:**

- Read the complete candidate notes for open-ended search allocation, lightweight search control, backtracking, failure explanation, search-controller evaluation, natural-language project state, system-use selection, and the Commonplace revision evidence. Their claims divide cleanly into premise, mechanism, extension, and bounded evidence roles rather than keyword overlap.
- Followed the existing neighborhoods around the proposal-selection loop, theory-mediated path, warranted-transfer residue, Naur basis, and repeatable operative revision. Those seven links are already authored from the source and were not repeated as candidates.
- Read the relevant Exo, Reflexion, Compound Engineering, Agent-R, HyperAgents, ScienceFlow, and Naur ingest passages. Only Exo and Reflexion materially bear on a subclaim while also exposing why the full theory-possession claim remains unestablished.
- Verified every retained candidate and index path with `test -f` before writing this report.

## Connections Found

- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- **grounds**: establishes the prior allocation problem that makes a fallible program theory useful before the strongest evidence exists.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- **grounds**: distinguishes the source's provisional theory-guided branch choices from the separate authority to adopt an operative modification.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **mechanism**: explains how restoring an earlier usable state and redirecting search prevents a theory-guided trial from becoming commitment merely because it was attempted.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **mechanism**: makes the source's outcome read-back causal by requiring a retained interpretation of failure to change a later scope, probe, continuation, or abandonment choice.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **extends**: supplies a matched, distributional evaluation design for judging whether theory-guided routing improves later candidates, evidence, failure information, or recovery without assuming exhaustive counterfactual search.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- **mechanism**: offers a substrate-specific conjecture for how retained intent, theory, branch history, and constraints can alter an LLM's search, together with the withholding and perturbation test the source requires.
- [System use is an initial selection environment when theory fit lacks a fixed oracle](../../../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) -- **extends**: develops delayed operational consequences into a provisional selection environment for revising program theory when no complete local oracle decides global fit.
- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) -- **evidenced-by**: records one bounded case in which retained project theory shaped computational search while human global selection, missing ablation, and the absence of a long track record limit the inference.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **evidenced-by**: implements rollback that preserves the failed-attempt record and exposes the source's recovery submechanism, while its build-and-test oracle gap shows that reversible search alone does not establish coherent theory-mediated modification.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) -- **evidenced-by**: programming retries feed failed implementations, test feedback, and task-local reflections into the next attempt, corroborating a narrow failure-guided-search mechanism while its same-instance scope falls short of possession across later demands.
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) -- **abstracted-from**: Naur supplies the theory-holder capabilities, modification-demand horizon, and program-life criterion; the source note adds the residue synthesis, fallible search account, delayed-warrant path, and computational test. A future author should place this link in the opening Naur attribution rather than only in the footer.

## Bidirectional Candidates

- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) <-> source -- **is-evidence-for** from the ingest: the ingest's active connection surface should route readers to this new synthesis because its retained capabilities and life/death criterion materially support the claim while its limitations bound the inference.
- [Exo](../../../../agentic-systems/reviews/exo.md) <-> source -- **is-evidence-for** from the system analysis: Exo's preserved attempt record and rollback path bear on the recovery subclaim, and its shallow acceptance gate supplies the limiting contrast; this is narrow enough for the collection's rare evidence label.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) <-> source -- **is-evidence-for** from the review: the programming loop witnesses failure interpretation changing a retry, while same-instance memory and test oracles make clear that it is not yet evidence of a longitudinal program theory.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- rejected because the local discrimination test is already carried more concretely by lightweight search control and failure-explanation read-back; adding it would not improve traversal for this claim.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected because it retains project knowledge and supports rollback, but its own analysis finds later-episode outcome feedback mostly omitted; it therefore does not test the source's longitudinal theory-possession claim.
- [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md) -- rejected because revision trajectories become opaque parametric policy and the runtime exposes neither an addressable program theory nor outcome read-back into that theory.
- [HyperAgents](../../../../agent-memory-systems/reviews/hyperagents.md) -- rejected because benchmark-selected patch lineages are operative, but prior evaluation history is not reliably surfaced to the meta-agent and no semantic theory state guides recovery across later demands.
- [ScienceFlow](../../../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) -- rejected because recoverable workspaces and evidence-preserving checkpoints instantiate generic recovery, not the source's program-specific theory causal path.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- rejected because one Commonplace change maps search, evaluation, and retention but does not exercise the novel-demand horizon or theory-guided recovery that distinguishes the source claim.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the selective head could place this note under “What reflection adds” as the operational theory-possession test that develops its existing theory-mediated-learning entry across novel demands, delayed evidence, and recovery.

## Synthesis Opportunities

None. The apparent synthesis across theory perturbation, branch allocation, stronger evaluation, recovery, and delayed consequences is already stated in the source's computational-test section rather than remaining an uncaptured higher-order claim.

## Maintenance Observations

None

## Flags

None
