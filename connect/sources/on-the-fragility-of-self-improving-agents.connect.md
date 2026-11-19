---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/on-the-fragility-of-self-improving-agents.md"
source_has_frontmatter: true
date: "2026-08-22"
depth: standard
---

# Connection Report: Fragility of Self-Improving Agents

**Source:** [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](../../../sources/on-the-fragility-of-self-improving-agents.md)

The target is an immutable source snapshot. Its matching `on-the-fragility-of-self-improving-agents.ingest.md` does not yet exist, so `Connections Found` recommends edges for that future authored surface. The load-bearing present-tense signal is under `Reverse-edge Candidates`; nothing should be authored into the snapshot.

## Discovery Trace

**Contracts and indexes read before discovery:**

- Read `kb/sources/COLLECTION.md`, `kb/cache/types/connect-report.md`, the full snapshot, and the full `cp-skill-connect` skill. The authorised destinations are notes, reference, agent-memory reviews, agentic-system analyses, and other sources; `kb/work/` and `kb/instructions/` were excluded.
- Read the curated heads `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no `tags` field, so the topic-index pass used its stated subjects: self-improving systems, agent memory, evaluation, LLM reliability, observability, and deploy-time learning. Their tag heads were read and non-complete tags were swept with `rg`.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' <destination> --glob '*.md'` and `rg '^description:' <destination> --glob '*.md'` over each authorised repo-local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- The listings surfaced the exact AWM and ReasoningBank reviews, the original AWM ingest, the general agent-reliability ingest, and the self-evolver-faithfulness ingest. No whole-agent-system analysis described the paper's memory subsystem closely enough to retain.

**Body search:**

- `rg -l -i 'task order|curriculum|shuffle(d|s|ing)?' kb/notes/ --glob '*.md'` — the experimental-contrast note was inspected but rejected because it does not need this paper as evidence and the paper reports its observed condition pairs without making a finer causal attribution.
- `rg -l -i 'underspecification|underspecified|under-specified|task specification|environment specification' kb/notes/ --glob '*.md'` — produced broad instruction-interpretation and specification notes; the generic matches were rejected in favour of the paper's more specific trace-to-memory and diagnostic-evidence mechanisms.
- `rg -l -i 'trace-extracted|memory validation|wrong lesson|erroneous memor|unverified (memory|hypoth)' kb/notes/ --glob '*.md'` — retained the checked-outcome and trace-authority notes because the evaluator-bug, irrelevant-medical-advice, unsupported-API, and Haversine cases instantiate their exact failure boundary.
- `rg -l -i 'multiple runs|repeated runs|single-run|run-to-run|variance|stochastic' kb/notes/ --glob '*.md'` — inspected execution-indeterminism and reliability neighbours; rejected the former as a single-sampling-process account that does not capture path-dependent accumulation across a task stream.
- `rg -l -i 'task order|curriculum|underspecification|trace-extracted|memory validation|run-to-run|trajectory|outcome-only' kb/reference/ --glob '*.md'` — inspected the trajectory-aware evaluation proposal and rejected it as a Commonplace workflow-compliance experiment rather than an analysis of learned memory quality.
- `rg -l -i 'Agent Workflow Memory|ReasoningBank|task order|curriculum|underspecification|memory validation|run-to-run' kb/agent-memory-systems/ --glob '*.md'` — retained the two exact system reviews. The same query over `kb/agentic-systems/` produced no candidate.
- `rg -l -i 'Agent Workflow Memory|ReasoningBank|task order|curriculum|underspecification|faithful self-evolver|agent reliability' kb/sources/ --glob '*.md'` — retained three comparison ingests after reading their claims and limitations; broad self-improvement and prompt-stability matches were rejected.

**Link following and candidate evaluation:**

- Read [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) and [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) in full, then followed their links to the trace-learning and memory-authority neighbourhood. Both reviews document automatic outcome-gated induction, prompt injection, and absent memory-specific faithfulness or provenance controls; the paper directly tests the reliability consequences of those mechanisms.
- Read the checked-outcome, trace-authority, diagnostic-richness, fixed-decomposition, final-task-success, memory-oracle, and experimental-contrast notes in full and followed their relevant-note links one hop. Three passed the articulation test; fixed-decomposition and final-task-success were useful lenses but their claims were broader or differently scoped than the paper's result.
- Read the AWM, agent-reliability, and self-evolver-faithfulness ingests in full. They passed on named axes: original claimed benefit versus shuffled/repeated re-evaluation; general stateless reliability versus stateful amplification; and memory uptake versus memory correctness. No similarity scores were available; candidates were judged by the articulation test and collection contracts.

## Connections Found

*(Recommendations for a future `on-the-fragility-of-self-improving-agents.ingest.md`.)*

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: adding evaluator rubrics, action-error feedback, and explicit environment constraints to memory construction improves shuffled-order ReasoningBank performance, while the remaining 69% gap shows that richer diagnostic evidence helps without being sufficient.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — **is-evidence-for**: the paper shows successful or failed task outcomes being abstracted into misleading reusable lessons when a shortcut happens to score, an evaluator produces a false negative, or an ambiguous task's intended interpretation is absent.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **is-evidence-for**: unsupported API advice, irrelevant medical guidance, and a reward-hacking Haversine workaround become future prompt guidance without a separate verification or bounded-abstraction step, then recur through retrieval.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — **is-evidence-for**: the paper re-evaluates this exact trace-to-workflow loop under a stronger harness, repeated runs, and shuffled task orders, adding empirical reliability evidence to the review's documented weak provenance, validation, and faithfulness controls.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) — **is-evidence-for**: the paper's main failure inspection concerns this exact outcome-gated, top-1-retrieved, prompt-injected memory system and tests what happens when its induction context omits task and environment constraints.
- [Ingest: Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md) — **compares-with**: the original ingest records positive WebArena and cross-domain results; this paper reproduces the mechanism with a stronger baseline and shows that gains can reverse under shuffled order and vary substantially across runs.
- [Ingest: Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) — **compares-with**: that paper defines consistency and robustness for repeated stateless agent trials, while this paper shows a stateful learning loop amplifying baseline noise and makes task-stream order an additional robustness perturbation.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) — **compares-with**: the faithfulness study asks whether stored summaries causally affect behaviour; this paper assumes retrieval and examines the complementary question of whether the affected behaviour is reliable when the stored lesson is wrong or underspecified.

## Bidirectional Candidates

- [Ingest: Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md) ↔ source — **compares-with**: a return comparison would put the original positive evidence beside the newer repeated-run and task-order-sensitive re-evaluation.
- [Ingest: Towards a Science of AI Agent Reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) ↔ source — **compares-with**: a return comparison would connect the general four-dimensional reliability framework to a worked stateful-memory case.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) ↔ source — **compares-with**: readers need both causal uptake and retained-content quality to evaluate whether memory-based self-improvement is genuinely useful.

## Reverse-edge Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source — **evidenced-by**: the +Rub, +Env, and +PMod interventions are a direct memory-learning case where improving the proposer's evidence surface modestly improves later outcomes.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) → source — **evidenced-by**: the paper supplies multiple concrete counterexamples in which outcome feedback does not warrant the generalized lesson later retained.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → source — **evidenced-by**: the observed contagious memories are empirical instances of captured diagnoses being granted consult-level authority before verification and bounded abstraction.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) → source — **evidenced-by**: the source is a newer, controlled evaluation of the reviewed implementation family and directly bears on its validation and maintenance caveats.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) → source — **evidenced-by**: the source evaluates the reviewed WebArena path and demonstrates concrete failure modes of its outcome gating, generic induction prompt, and injected-memory authority.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None — every retained candidate has frontmatter.

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — the fixed memory-generation inputs are a useful lens, but the paper's interventions recover part of the loss; it does not establish that the needed correction is outside the effective update space.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — the Haversine fallback resembles its worked mechanism, but the note is about hidden infrastructure-path failure and guarantee degradation, whereas the paper's load-bearing result is propagation of an accepted lesson.
- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — repeated runs share stochastic vocabulary, but the paper's novel issue is amplification through stateful memory and sensitivity to sequence, not the existence of sampling variance itself.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — useful for reading the ablations cautiously, but the paper reports the actual +Rub/+Env/+PMod/+All contrasts and does not make a finer component-causal claim that this note would need to correct.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — both distinguish final outcomes from process evidence, but the proposal concerns Commonplace workflow-protocol compliance, not online memory induction or task-stream order.
- Agentic-system analyses under `kb/agentic-systems/` — none covers AWM or ReasoningBank as a whole agentic harness; linking from a memory-subsystem paper would be category-level overlap only.
- [Ingest: Prompt Stability in Code LLMs: Emotion and Personality Variations](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — measures non-stateful prompt perturbations in code generation and lacks the accumulating-memory or task-order mechanism.

## Index Membership

None. `kb/sources/README.md` is an orientation document rather than an item index, and note tag heads index notes rather than source snapshots.

## Synthesis Opportunities

- This source plus [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) and [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) imply a sharper evaluation principle: **a stateful improvement method must randomize the learning sequence as well as repeat the run, because an early unverified lesson changes the evidence and behaviour available to every later episode**. Run count measures dispersion; task-order variation probes path dependence.
- This source plus [the self-evolver faithfulness ingest](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) separates two necessary checks for memory-based improvement: whether a memory causally changes behaviour and whether the memory's content deserved that authority. A system can fail by ignoring good memory or by faithfully applying bad memory.

## Maintenance Observations

None.

## Flags

- **No ingest companion exists.** `kb/sources/on-the-fragility-of-self-improving-agents.ingest.md` is absent, so the outbound recommendations have no authored surface until ingest creates it.
- **Scope limit.** The source evaluates two textual-memory methods on web-browsing benchmarks with three runs and manually inspects a subset of ReasoningBank memories. Preserve those bounds; do not generalize the 71% variance-amplification rate or the 31% recovery result to all self-improving agents.
