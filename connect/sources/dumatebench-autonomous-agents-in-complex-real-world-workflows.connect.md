---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/dumatebench-autonomous-agents-in-complex-real-world-workflows.md"
source_has_frontmatter: true
date: "2026-09-03"
depth: standard
---

# Connection Report: DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows

**Source:** [DuMateBench: Evaluating Autonomous Agents in Complex Real-World Workflows](../../../../sources/.snapshots/dumatebench-autonomous-agents-in-complex-real-world-workflows.md)

## Discovery Trace

**Source and authoring surface:**

- Read the complete snapshot. Its main contribution is a 200-task benchmark reconstructed from production-agent sessions, with pre-task history and workspace state, cross-capability workflows, insufficient/unstable/noisy execution conditions, a deterministic-checklist plus artifact-specific-judge evaluation, and a fully crossed experiment over five frameworks and four base models. Its results show framework-model interaction, different noise sensitivity, quality/latency/token trade-offs, and trace-derived failure categories.
- The snapshot is immutable. `kb/sources/COLLECTION.md` assigns its authored connection surface to `kb/sources/dumatebench-autonomous-agents-in-complex-real-world-workflows.ingest.md`, but that ingest does not currently exist. Every outbound item below is therefore a candidate for that future ingest; no link should be authored in the snapshot.
- The source collection authorizes prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. It excludes `kb/work/` and `kb/instructions/`. External targets are authorized only when already known, not as a search surface; no external candidate beyond the snapshot's own source URL was supplied, so external prospecting was skipped.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no matching tag-README pass applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (427 title hits), `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (160), `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (175), `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (15), and `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` (372). The strongest title-level candidates were the whole-system learning and runtime-diagnosis notes, the trajectory-aware evaluation proposal, the Hermes review, the whole-system evaluation account in *AI Agents in Depth*, and three adjacent benchmark ingests.

**Description listing scan:**

- Notes: ran `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'benchmark|evaluat|reliab|robust|environment|failure|harness|framework|task completion|artifact quality|agent.runtime|model.*framework|framework.*model|verification|oracle|noise|context contamination|budget'`. Kept the whole-system boundary, runtime-responsibility, and typed-verification notes. Evaluated but rejected diagnostic-richness, context-contamination, and soft-workaround candidates because DuMateBench does not isolate their mechanisms.
- Reference: ran `rg '^description:' kb/reference/ --glob '*.md' | rg -i 'benchmark|evaluat|trajectory|agent.workflow|artifact|judge|oracle|verification|harness|model'`. The trajectory-aware evaluation proposal passed the articulation test, but the useful authored direction is from that proposal to the future ingest under reference's `evidenced-by` rule.
- Agent memory systems: ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'benchmark|evaluat|trajectory|failure|harness|Hermes|OpenClaw|Claude Code|workflow|artifact|environment'`. Kept Hermes because DuMateBench evaluates the exact named framework release family and adds whole-agent outcome evidence to a code-grounded subsystem review. Rejected generic trajectory-learning systems because DuMateBench reconstructs sessions for evaluation but does not learn memory from them.
- Agentic systems: ran `rg '^description:' kb/agentic-systems/ --glob '*.md' | rg -i 'benchmark|evaluat|failure|harness|model|workflow|verification|artifact|environment'`. Kept *AI Agents in Depth* because its Model-Harness and typed-evaluation doctrine is directly instantiated and qualified by DuMateBench's crossed experiment.
- Sources: ran `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'benchmark|evaluat|trajectory|failure|harness|model|workflow|verification|artifact|environment|real.world|noise'`. Kept the fixed-model harness study, AutoResearchEval, and the non-atomic tool-failure study as comparisons on, respectively, framework/model interaction, trajectory diagnosis, and fault-model coverage.

**Body search:**

- Notes: `rg -n -i 'agent.framework|base model|model.framework|deployed system' kb/notes/ --glob '*.md'`; `rg -n -i 'workspace noise|environmental noise|distractor|context contamination|noisy environment' kb/notes/ --glob '*.md'`; `rg -n -i 'failure recovery|budget exhaustion|incomplete execution|strict task completion|task completion' kb/notes/ --glob '*.md'`; and `rg -n -i 'deterministic.*(judge|rubric|evaluation)|artifact-specific|hybrid.*evaluation|typed target|oracle.*artifact' kb/notes/ --glob '*.md'`. These searches confirmed that the strongest note-level value is evidence for the system boundary, the diagnostic split among scheduling/context/external services, and artifact-class-specific verification.
- Reference: `rg -n -i 'trajectory-aware|task completion|execution trace|artifact-specific|LLM-as|agent framework|base model|model.harness|workspace noise|environmental' kb/reference/ --glob '*.md'`. This isolated the trajectory-aware workflow-evaluation proposal.
- Agent memory systems: `rg -n -i 'Hermes|OpenClaw|Claude Code|agent.framework|base model|model.harness|workflow|benchmark|evaluation|failure|environment|artifact verification' kb/agent-memory-systems/ --glob '*.md'`. Hermes was retained; broad memory-evaluation matches did not gain anything concrete from a benchmark that does not isolate memory.
- Agentic systems: `rg -n -i 'benchmark|evaluation|failure|environment|model|harness|workflow|artifact verification|task completion' kb/agentic-systems/ --glob '*.md'`. *AI Agents in Depth* was retained; other whole-system reviews lacked a named framework or a closer evaluation-axis match.
- Sources: `rg -n -i 'same model|different harness|agent.model interaction|framework.model|model.framework|workspace noise|distractor files|unstable network|missing dependenc|non-atomic failure|artifact-specific.*rubric|deterministic checklist|failure mode|execution trace' kb/sources/ --glob '*.md'`. The three retained ingests provide narrower comparison regimes rather than duplicate DuMateBench.

**Link following:**

- Followed the whole-system learning note to its runtime decomposition, fixed-decomposition, and three-source-deviation neighbors. DuMateBench's fully crossed 5x4 results support the system boundary; its manually assigned failure categories give bounded case evidence for the runtime-responsibility split but do not identify unique causes.
- Followed the typed-verification note to its oracle-domain and document-type neighbors. DuMateBench classifies expected artifact suffixes and supplies modality-specific evidence representations and rubrics, a concrete typed-oracle implementation rather than proof of logical necessity.
- Followed the trajectory-aware proposal to AutoResearchEval. DuMateBench adds a second trajectory-inspection case, but its trace analysis is limited to sampled non-complete runs and has no output-only control, so it motivates rather than satisfies the proposal.
- Followed the Hermes review through its trace-learning and evaluation caveats. DuMateBench supplies whole-agent task outcomes for Hermes v0.19.0 configurations but does not isolate Hermes memory, background review, or skill curation.
- Followed *AI Agents in Depth* through its Model-Harness, typed-task, resettable-state, trajectory, verifier, and diagnostic-evidence claims. DuMateBench implements this bundle and also demonstrates that framework-model interactions prevent a model-swap result from uniquely identifying the harness bottleneck.
- Followed the three source comparisons through their existing connections: the fixed-model harness study points to the deployed-system and actual-contrast notes; AutoResearchEval points to diagnostic richness and the trajectory-aware proposal; the verified-tool-call study points to intended-path health and structured recovery. DuMateBench broadens their task and framework coverage but is weaker on their isolated causal contrasts.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: DuMateBench fully crosses five agent frameworks with four base models and finds large, non-uniform framework-model interactions, directly supporting evaluation of the behavior-producing pair rather than attributing outcomes to model weights alone.
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **is-evidence-for**: the sampled failures separate incomplete execution/budget exhaustion, requirement or context grounding, and environment or dependency failure, giving bounded empirical cases for locating failures at different runtime responsibilities even though the study's single-primary-category coding does not establish unique causes.
- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- **is-evidence-for**: DuMateBench first classifies heterogeneous target artifacts and exposes modality-appropriate text, structure, formulas, pages, images, or video frames to artifact-specific rubrics, showing a concrete verification design whose oracle domain depends on artifact class.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) -- **compares-with**: DuMateBench contributes whole-agent outcome, robustness, efficiency, and failure data for Hermes v0.19.0 across four models, while the review supplies code-grounded memory and trace-learning mechanisms that the benchmark does not isolate.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) -- **compares-with**: DuMateBench instantiates the book analysis's model-plus-Harness, typed-task, resettable-environment, verifier, trajectory, and diagnostic-evidence evaluation doctrine, while its interaction results qualify any inference that a model swap alone identifies a harness bottleneck.
- [Same Model, Different Harness: Different Coding-Agent Results](../../../../sources/same-model-different-harness-different-coding-agent-results.ingest.md) -- **compares-with**: the earlier study isolates one bundled harness effect under fixed models and context regimes, whereas DuMateBench fully crosses models and frameworks over heterogeneous workflows and imperfect environments but does not isolate any framework component.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) -- **compares-with**: both inspect execution evidence to diagnose agent failures, but AutoResearchEval uses a 45-pattern artifact-aware taxonomy with human calibration across 800 trajectories, while DuMateBench assigns one primary category to sampled non-complete runs and contributes broader framework-model and environmental comparisons.
- [Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) -- **compares-with**: both inject execution faults, but the verified-tool-call study isolates ambiguous response-versus-effect failures and duplicate side effects, while DuMateBench covers transient network/tool failures in compositional workflows without a path-sensitive non-atomic-effect metric.

## Bidirectional Candidates

- [Same Model, Different Harness: Different Coding-Agent Results](../../../../sources/same-model-different-harness-different-coding-agent-results.ingest.md) <-> source -- **compares-with**: readers of either benchmark need the narrower causal harness-package contrast beside DuMateBench's broader fully crossed framework-model-environment design.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) <-> source -- **compares-with**: the two studies offer complementary failure-analysis granularity and benchmark scope.
- [Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures](../../../../sources/verified-tool-calls-improve-llm-agent-reliability.ingest.md) <-> source -- **compares-with**: the return path makes DuMateBench's broad unstable-environment coverage legible beside a narrower path-sensitive fault model.

## Reverse-edge Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → future ingest -- **evidenced-by**: the 5x4 crossed experiment is direct whole-system evidence that model and framework jointly determine user-visible outcomes.
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) → future ingest -- **evidenced-by**: DuMateBench's failure coding supplies empirical examples at each of the note's three diagnostic responsibilities, with the study's attribution limits kept explicit.
- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) → future ingest -- **evidenced-by**: the benchmark's artifact-suffix inventory and modality-specific judge inputs are a concrete implementation of class-dependent verification.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → future ingest -- **evidenced-by**: DuMateBench's trace inspection recovers planning, recovery, grounding, and artifact-verification failures unavailable from aggregate scores, while its lack of a controlled output-only arm preserves the proposal's need for a paired test.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) → future ingest -- **evidenced-by**: the benchmark adds version-named whole-agent results for Hermes, explicitly bounded so they do not validate its memory or trace-learning mechanisms separately.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) → future ingest -- **evidenced-by**: DuMateBench is a current empirical case for the analysis's whole-system and typed-evidence evaluation claims and for its warning against unique model-versus-harness attribution.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- DuMateBench shows that trace inspection can produce useful failure descriptions, but it does not compare proposer learning with and without those diagnostics; the source therefore does not test the note's outer-loop learning claim.
- [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- DuMateBench's file-noise experiment measures performance under distractor workspaces, but it does not show that distractors entered model context or caused the below-compliance stance-drift mechanism in the note.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- insufficient and unstable environments create opportunities for fallback, but the paper does not isolate successful workarounds or measure their per-encounter context and reasoning tax.

## Index Membership

None

## Synthesis Opportunities

- [DuMateBench](../../../../sources/.snapshots/dumatebench-autonomous-agents-in-complex-real-world-workflows.md) and [Same Model, Different Harness](../../../../sources/same-model-different-harness-different-coding-agent-results.ingest.md) jointly support a higher-order claim that a measured harness effect is indexed by the model-framework pairing, task distribution, environment regime, resource limits, and endpoint rather than being a scalar property of either model or harness. The fixed-model study identifies a bundled harness effect under context pressure; DuMateBench adds a fully crossed interaction design and imperfect-environment variation. A future synthesis would still need to keep component attribution and cross-benchmark comparability out of scope.

## Maintenance Observations

- The snapshot has no matching `kb/sources/dumatebench-autonomous-agents-in-complex-real-world-workflows.ingest.md`. Because snapshots are immutable and cannot be durable link targets, the source currently lacks an authored connection surface. A later explicit ingest should create that surface before any outbound candidates are applied.

## Flags

- Immutable-source flag: all outbound candidates target the future matching ingest; reverse-edge candidates should also link to that ingest, never to `.snapshots/`.
