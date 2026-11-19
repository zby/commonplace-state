---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/can-ai-agents-conduct-open-ended-ai-research.md"
source_has_frontmatter: true
date: "2026-08-06"
depth: standard
---

# Connection Report: Can AI agents conduct open-ended AI research?

**Source:** [Can AI agents conduct open-ended AI research? Early evidence from two case studies](../../../sources/can-ai-agents-conduct-open-ended-ai-research.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 335 files under `kb/notes/`, 127 under `kb/reference/`, 172 under `kb/agent-memory-systems/`, 11 under `kb/agentic-systems/`, and 442 under `kb/sources/`.
- Ran complete scoped description listings with `rg '^description:' kb/<destination>/ --glob '*.md'` over all five authorised local destinations. The notes listing foregrounded the oracle-boundary, fixed-decomposition, contextual-activation, and proposal-selection clusters. The sources listing foregrounded prior reports on research taste, known-target scientific-discovery benchmarks, long-running harnesses, and autonomous-research memory. The agentic-system listing contained no analysis of OpenClaw or Codex research runs.
- The strongest path-and-description candidates were [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md).

**Topic indexes:**

- Read [Tags](../../../../tags/README.md), [Evaluation](../../../../tags/evaluation-README.md), [discovery](../../../../tags/discovery-README.md), [LLM reliability](../../../../tags/llm-reliability-README.md), and [Failure modes](../../../../tags/failure-modes-README.md). The discovery head led directly to the known-target and missing-oracle notes; the reliability head led to the automation-boundary and discrimination notes.
- Read the curated heads for [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). Reference was rejected as a destination after its current-system head and focused body search exposed no shipped Commonplace component this source directly describes.

**Body search:**

- `rg -n -i 'open[- ]ended|shadow evaluations?|research automation|automating (AI )?research|AI research' kb/notes/ --glob '*.md'` -- kept the KB-learning, automation-boundary, and known-target-discovery candidates; rejected generic open-ended-tool-loop matches.
- `rg -n -i 'verification boundary|verifiable tasks?|cheap verifier|oracle|blind (peer )?review|expert grad' kb/notes/ --glob '*.md'` -- kept the automation-boundary and discrimination candidates; the broader oracle cluster was redundant once these two were loaded.
- `rg -n -i 'backtrack|instruction drift|context rot|resource awareness|budget|creative problem|research judgment|hypothes' kb/notes/ --glob '*.md'` -- kept contextual activation and proposal selection; rejected scheduling and budget notes that did not address semantic project revision.
- `rg -n -i 'shadow evaluations?|open[- ]ended (AI )?research|automating (AI )?research|research taste|scientific discovery|verifiable tasks?|instruction drift|context rot' kb/sources/ --glob '*.md'` -- found no duplicate capture and kept the research-taste, DiscoverPhysics, and FALSIFYBENCH comparisons.
- `rg -n -i 'instruction drift|context rot|long-horizon|backtrack|research agent|scientific|self-review' kb/agent-memory-systems/ --glob '*.md'` -- kept ARIS as a comparison on research memory and cross-model review, not as evidence that those mechanisms solve the failures here.
- `rg -n -i 'instruction drift|context rot|long-horizon|backtrack|research|review|budget' kb/agentic-systems/ --glob '*.md'` -- evaluated Autogenesis and Claude Code dynamic workflows but rejected both as execution-surface overlap without a direct claim about open-ended research judgment.
- `rg -n -i 'shadow evaluation|open-ended research|research automation|instruction drift|context rot' kb/reference/ --glob '*.md'` -- returned no relevant current-system target.

**Link following:**

- Followed the automation-boundary note to its discrimination mechanism and KB-learning application. This separated expensive expert evaluation from a cheap inner-loop verifier.
- Followed the known-target note to automated synthesis and the oracle-strength cluster. This exposed shadow evaluation as a distinct construction: the question is hidden and authentic, but success is not scored by matching the original paper's answer.
- Followed fixed decomposition to proposal selection and diagnostic richness. The source had rich logs and multiple review channels, so missing diagnostics was rejected; failure to make project-level alternatives operative remained live.
- Followed contextual activation to process structure and long-context failure. The agents' reviews often named the same problems as the human experts, making context-to-action failure more precise than retrieval failure.
- Followed the research-taste ingest to the automation-boundary synthesis. The CRUX source supplies bounded empirical evidence for a claim that the earlier source made conceptually.

## Connections Found

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) -- **is-evidence-for**: the agents autonomously executed literature review, coding, experiments, and paper production, yet failed at the judgment-heavy mutations most analogous to KB synthesis and regrouping: deciding that evidence was adequate, abandoning a weak framing, and choosing a more valuable direction.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **is-evidence-for**: the source directly contrasts cheap verifier-scored research engineering with expensive open-ended research judgment, then constructs a task-specific human oracle to show that autonomous execution still did not close the research loop.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- **is-evidence-for**: repeated AI reviews rejected the drafts and surfaced many real weaknesses, but the all-reject sample cannot establish per-instance discrimination and the agents did not use those verdicts to govern project-level selection.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- **compares-with**: shadow evaluation avoids exact target reconstruction by supplying only an unpublished paper's question and using its authors as expert judges; it trades known-target scoring for expensive, non-blind judgment.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: the agents had critiques in live context that overlapped the final expert reviews, yet mostly added caveats or narrowed claims instead of letting the critiques change the plan.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting the model/scaffold robustness run requires separating what changed jointly from what stayed fixed: two selected questions, paper-shaped output, budgets, reviewer construction, task framing, and the surrounding research protocol.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: AI reviews supplied reject-capable evaluation, but the agents rarely expanded search after rejection and instead retained weaker framings; evaluation existed without effectively governing project-level candidate selection.
- [Ingest: When code is free, research is all that matters](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) -- **compares-with**: the earlier essay argues conceptually that engineering has oracles while research taste does not; CRUX supplies two deeply observed cases that split autonomous engineering from research judgment.
- [Ingest: DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- **compares-with**: DiscoverPhysics creates executable counterfactual worlds and a known law, while CRUX preserves authentic open-ended questions and pays for expert grading; the two designs occupy different points on the oracle/open-endedness trade-off.
- [Ingest: FALSIFYBENCH](../../../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) -- **compares-with**: FALSIFYBENCH makes hypothesis-test selection measurable against a planted rule, whereas CRUX observes hypothesis choice, underpowered falsification, and project-level backtracking where no planted answer scores the run.
- [Auto-claude-code-research-in-sleep](../../../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) -- **compares-with**: ARIS installs research-wiki memory, cross-model review, and separate completion/acceptance gates; CRUX shows that correct-looking review feedback and retained project state do not by themselves produce substantive pivots, while not testing ARIS directly.

## Bidirectional Candidates

- [Ingest: When code is free, research is all that matters](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) <-> source -- **compares-with**: a return link would let readers move from the conceptual research-taste claim to a later empirical case study that operationalizes and bounds it.
- [Ingest: DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) <-> source -- **compares-with**: the pair makes the oracle/open-endedness trade explicit between simulator-verified law discovery and expert-graded authentic research.

## Reverse-edge Candidates

- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) → source -- **evidenced-by**: the two runs are bounded evidence that autonomous execution can coexist with failure on judgment-heavy integration and synthesis.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidenced-by**: the source is a direct empirical comparison between verifier-scored research work and expert-graded open-ended research.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) → source -- **evidenced-by**: the source explicitly notes that uniformly rejecting weak drafts does not establish a reviewer's discrimination.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source -- **evidenced-by**: shadow evaluation is a useful bounding alternative that preserves open-endedness without scoring similarity to a known target.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: multiple critiques were available and substantially correct but did not change project-level behavior.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected because these runs exposed detailed logs, experiment results, budget telemetry, and repeated reviews; the observed failure was prioritization and action, not absence of diagnostic evidence.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- rejected because the AI reviews often did identify the human reviewers' central objections; the source does not primarily show answer reconstruction substituting for route evaluation.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) -- rejected as a direct connection: it bundles persistent work state, decomposition, and end-to-end coding verification without controlled evidence, while CRUX's central failures persisted after state and review surfaces were available.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- rejected because shared budgets, subagents, and isolated reviewers are execution-surface overlap; the analysis does not claim they improve scientific judgment or project-level backtracking.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- rejected because its soft reviewer gate and fixed orchestration boundary are analogous but not specific enough to help a reader interpret these research runs.

## Index Membership

None

## Synthesis Opportunities

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), and this source imply a distinct evaluation construction: an **expert-grounded shadow evaluation** converts an open-ended, uncontaminated question into an expensive externally judged test without importing a target answer or manufacturing a cheap inner-loop verifier. That construction deserves integration into the existing discovery-evaluation account, not a standalone note yet.

## Maintenance Observations

None

## Flags

- The fixed-decomposition audit is load-bearing: the robustness run changes model and scaffold together, while task selection, paper objective, budget shape, evaluator construction, and much of the protocol remain fixed. It reproduces failure modes but does not identify which model or scaffold choice caused them or validate the surrounding decomposition.
- The source makes several independent assertions across evaluation design, research capability, context-to-action failure, and resource control. The ingest should select a compact role rather than treating all findings as one universal deficit.
