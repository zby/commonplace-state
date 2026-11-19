---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/envharness-awakening-static-worlds-for-agent-learning.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: EnvHarness: Awakening Static Worlds for Agent Learning

**Source:** [EnvHarness: Awakening Static Worlds for Agent Learning](../../../sources/envharness-awakening-static-worlds-for-agent-learning.md)

## Discovery Trace

**Source and linking contract:**
- Read the complete paper snapshot, `kb/sources/COLLECTION.md`, and the connect-report type. The source collection authorizes prospecting into notes, reference, agent-memory systems, agentic systems, and sources; snapshots are immutable, so outbound candidates belong on the companion ingest and load-bearing note citations are reverse-edge candidates.
- Applied the experiment-ingest lens from [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md). EnvRigger can condition on five baseline trajectories, their aggregate success and failure signals, task text, and a bridge-provided environment-state schema; validation adds five fresh trajectories, success rate, failure distribution, and timeout count. It can compose Stage action replays and Contract action, transition, and observation transformations; Chain is implemented but excluded from the autonomous main pipeline. The designer maps this evidence to component code, ReasoningBank maps resulting trajectories to natural-language skills, the acting policy maps skill-conditioned observations to benchmark actions, and the RL arm additionally updates Qwen3-8B weights through GRPO.
- Fixed outside those effective update spaces are the Stage/Contract/Chain decomposition, reset/step and textual I/O boundary, benchmark bridges and domain prompts, action bases, tasks and verifiers, train/evaluation partitions, ReasoningBank extraction and serving path, EnvRigger prompt and rollout/revision budgets, policy/designer backbone pairing, objectives, and evaluation metrics. The main environment-source comparisons vary the compound wrapper-generated training signal, not these adjacent choices; the Chain analysis varies serial task pairing only.

**Full title and description listings:**
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- Ran `rg '^description:' kb/notes/ --glob '*.md'`, `rg '^description:' kb/reference/ --glob '*.md'`, `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`, and `rg '^description:' kb/agentic-systems/ --glob '*.md'`. The notes listing surfaced the effective-update-space, deployed-system, retained-instruction, diagnostic-richness, experiment-contrast, and compounding claims. Reference and agentic-system descriptions produced no source-specific fit. The agent-memory listing surfaced ReasoningBank and SkillRL.
- Ran `rg '^description:' kb/sources/ --glob '*.ingest.md' | rg -i 'environment|harness|skill|trajectory|self-improv|co-evol|learning signal'`. The closest source comparisons were SPADE, the ReasoningBank fragility re-evaluation, SkillRL, passive skill distillation, Co-Harness, and harness-learning papers.

**Topic indexes:**
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, [Self-improving systems](../../../../tags/self-improving-systems-README.md), [deploy-time-learning](../../../../tags/deploy-time-learning-README.md), and [Evaluation](../../../../tags/evaluation-README.md). These route the paper to update-space analysis, proposal selection, retained artifacts, feedback quality, and later-episode compounding tests.
- Read the curated heads for sources, agent-memory systems, and agentic systems. The agent-memory head and [trace-learning survey](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) confirm that ReasoningBank is the exact retained-skill lineage used by the paper. The agentic-system head contains no existing environment-harness casebook entry.

**Body search:**
- `rg -n -i 'fixed decomposition|effective update space|hypothesis class|action-closure|information omission' kb/notes --glob '*.md'` -- kept the fixed-decomposition note and followed it to the experiment-contrast and local-use claims.
- `rg -n -i 'diagnos|fresh rollout|accepting metric|acceptance metric|selection loop|search, evaluation|search evaluation|retention' kb/notes --glob '*.md'` -- kept the proposal-selection and diagnostic-richness candidates; rejected oracle-only matches that did not address this source's training-environment intervention.
- `rg -n -i 'environment (design|generation|scaling)|learning environment|training environment|environment.*policy|policy.*environment' kb/notes --glob '*.md'` -- found no existing note whose main claim is environment-side learning, making the deployed-system boundary a useful synthesis tension rather than a duplicate note.
- `rg -n -i 'skill extraction|distilled skill|trace-extracted|retained instruction|checked outcome|compounding' kb/notes --glob '*.md'` -- kept the retained-instruction and later-improvement claims; the checked-outcome note was retained as interpretive context but not as a separate edge because the paper evaluates extracted skills on held-out tasks rather than relying only on source-episode success.
- `rg -n -i 'environment harness|training environment|skill extraction|distill(ed|ing).*skill|reasoningbank|trajectory|self-improv|co-evol' kb/agent-memory-systems --glob '*.md'` -- kept the ReasoningBank review; SkillRL was rejected as a broader but less exact comparison for the paper's fixed extraction pipeline.
- `rg -n -i 'environment harness|training environment|skill extraction|self-improv|co-evol|rollout|diagnos' kb/agentic-systems --glob '*.md'` -- Autogenesis, Exo, and Compound Engineering were rejected because they mutate or coordinate agent-side machinery rather than reshape a training environment.
- `rg -n -i 'environment harness|environment (design|generation|scaling)|training environment|envharness|envrigger|co-evol' kb/sources --glob '*.ingest.md'` and `rg -n -i 'skill extraction|distill(ed|ing).*skill|reasoningbank|later improvement|compounding' kb/sources --glob '*.ingest.md'` -- kept SPADE and the ReasoningBank fragility paper. Co-Harness and passive distillation were rejected as redundant once the deployed-system note, exact ReasoningBank lineage, and closer environment-generation comparison were loaded.

**Link following:**
- Followed the fixed-decomposition note to [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) and [Use tests a decomposition locally; retained rationale makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md). These bound component and domain-generalization claims.
- Followed the deployed-system and retained-instruction notes to [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). EnvRigger realizes search and reject-capable validation; accepted wrappers affect later trajectories, which are then distilled into operative prompt instructions or used for weight learning.
- Followed the self-improving-systems head to [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). EnvHarness's scaling protocol is unusually relevant because later environment batches target a policy equipped with earlier skills and are compared with equal-budget learner-independent batches, but no removal or swapped-history arm isolates the earlier retained skills' contribution.
- Followed SPADE to its validity/learning-value and fixed-decomposition readings, and followed the fragility ingest to its repeated-run, task-order, and diagnostic-surface findings. These provide the closest positive and negative neighboring cases.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting EnvHarness gains requires separating the mappings EnvRigger, the skill extractor, and the policy can update from the wrapper types, interfaces, verifiers, partitions, and objectives the experiments leave fixed.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the skill-based arm improves held-out behavior without changing the policy backbone, while environment-side interventions change which retained skills enter the deployed system; the paper therefore supplies bounded evidence for non-weight learning while also exposing a training-environment surface outside the note's deployed-system boundary.
- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) -- **is-evidence-for**: skills extracted from accepted EnvHarness trajectories outperform skills extracted through the same pipeline from original environments on all five tested benchmarks, showing value in retaining the procedure selected by a changed evidence-generating process, though not isolating individual skills.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **compares-with**: EnvRigger proposes wrappers from full successful and failed trajectories plus aggregate rollout statistics and then validates on fresh runs; the source instantiates a rich diagnostic loop but does not ablate that evidence against scores-only or compressed alternatives.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **compares-with**: later batches target the policy carrying prior skill banks, held-out performance is displaced from component acceptance, and equal-budget static/generated batches provide a useful control, but the protocol does not remove or swap earlier retained skills to isolate their causal contribution to the next improvement.
- [SPADE: Self-Play in Adaptive Synthetic Executable Environments](../../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md) -- **compares-with**: both adapt the training environment to the current learner, but SPADE generates executable environments and jointly updates shared model weights whereas EnvHarness wraps trusted base environments and preserves their verifiers before extracting skills or training a policy.
- [On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) -- **compares-with**: EnvHarness uses ReasoningBank-style trajectory distillation and reports three-run means, while the neighboring re-evaluation shows that the same memory family can amplify variance and depend on task order; EnvHarness does not report shuffled co-evolution orders.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) -- **compares-with**: this is the exact extraction lineage the paper holds fixed, so the useful comparison is upstream—EnvHarness changes which trajectories ReasoningBank distills rather than changing ReasoningBank's natural-language memory form, retrieval, or prompt authority.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) → source -- **evidenced-by**: the paper's held-out skill comparisons are a direct multi-domain instance of testing selecting a reusable natural-language procedure.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source -- **evidenced-by**: the environment-scaling experiment supplies a later-episode, learner-conditioned protocol with static and generated controls, while its missing history intervention usefully bounds what that protocol establishes.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Artifacts as Memory Beyond the Agent Boundary](../../../../sources/artifacts-as-memory-beyond-agent-boundary.ingest.md) -- rejected: both locate consequential structure in the environment, but EnvHarness's wrappers generate training experiences rather than serving as environment-side memory that exposes the agent's own past.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) -- rejected as a direct edge: it is a useful broader trajectory-to-skill and skill-to-weight system, but ReasoningBank is the paper's named extraction pipeline and SPADE is the closer adaptive-environment comparison.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- rejected: shared self-improvement vocabulary does not overcome the different mutable object—agent protocol resources and orchestration there, training-environment wrappers here.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected: its protected-substrate/rewritable-executor boundary is relevant to self-modification governance but gives no concrete reader benefit for understanding environment reshaping.
- `kb/reference/` candidates -- rejected: the Commonplace system documentation contains no shipped environment-learning mechanism; linking this external paper to general review or proposal docs would be topical rather than operational.

## Index Membership

None.

## Synthesis Opportunities

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [Artifacts as Memory Beyond the Agent Boundary](../../../../sources/artifacts-as-memory-beyond-agent-boundary.ingest.md), and this source together expose a boundary worth sharpening: the deployed system is the behavior-producing evaluation unit, while the wider improvement pathway can also revise or exploit environment-side structures that shape what the deployed system learns. The environment need not become part of behavior-determining organization for its design to become a consequential learning surface.

## Maintenance Observations

- The paper links an official `google-research/envharness` repository and names released class terminology that differs from the paper (`Setups`, `Rules`, `Link` versus Stage, Contract, Chain). This ingest is paper-grounded only; a later code-grounded review would be needed before implementation or release-completeness claims gain code authority.

## Flags

- The paper's “domain-agnostic” claim is bounded by one bridge and domain prompt per benchmark, textual actions and observations, deterministic/resettable environments, and the exclusion of Chain from automated generation. It establishes a reusable interface above heterogeneous runtimes, not zero domain integration.
- The main comparisons identify the EnvHarness-generated environment bundle against named environment sources. They do not isolate Stage, Contract, diagnosis, validation, skill extraction, or their interactions; the Chain experiment identifies serial random pairing only.
- The co-evolution scaling protocol is stronger than a static score curve but still leaves a causal-history question: whether earlier retained skills, rather than merely more learner-conditioned batches and cumulative skill volume, made later improvement more productive.
