---
description: "Discovery report for possible KB connections from Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/recursive-experiential-working-memory-evolution.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses

**Source:** [Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses](../../../../sources/.snapshots/recursive-experiential-working-memory-evolution.md)

## Discovery Trace

**Collection rules:** Read `kb/sources/COLLECTION.md`. The snapshot is immutable, so its matching ingest is the authored surface for outbound candidates. The collection permits links to notes, reference, agent-memory systems, agentic systems, other sources, and already-known external sources; it excludes work and instructions.

**Curated heads:**

- Read `kb/notes/tags-README.md`, `kb/notes/agent-memory-README.md`, `kb/notes/context-engineering-README.md`, `kb/notes/self-improving-systems-README.md`, and the observability, evaluation, tool-loop, and deploy-time-learning tag heads. These exposed the active-work-state, activation, diagnostic-richness, proposal-selection, fixed-decomposition, and compounding candidates.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The agent-memory and source heads exposed ReasoningBank, SkillRL, Memento-Skills, SkillOpt, and Self-Harness. The reference and agentic-system heads produced no comparison more specific than the candidates retained below.

**Full title and description listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for notes, reference, agent-memory systems, agentic systems, and sources, then scanned `^description:` in the same destinations.
- The note listings flagged active work state, contextual activation, rule-ready selection signals, diagnostic richness, proposal selection, fixed update spaces, governed behavior-changing writes, and later-episode compounding tests. The system/source listings flagged trace-derived skill memories, stateful memory routing, validation-gated skill evolution, and bounded harness optimization. No prior Recuris artifact or citation was found.

**Body search:**

- `rg -n -i 'working memory|experiential memory|verified task state' kb/notes/ --glob '*.md'` — retained the active-work-state distinction; rejected human-working-memory analogies that do not describe agent control state.
- `rg -n -i 'skill invocation|memory activation|before the mistake|state-grounded' kb/notes/ --glob '*.md'` — retained pre-action activation and the rule-ready-signal neighbor; the general storage-versus-activation note was useful context but less specific than the behavior-changing-memory requirement.
- `rg -n -i 'structured trace|diagnostic richness|outer-loop' kb/notes/ --glob '*.md'` — retained diagnostic richness because Recuris uses a structured execution trace to localize failures before proposing component-scoped changes.
- `rg -n -i 'proposal-selection|validation gate|held-out|paired bootstrap' kb/notes/ --glob '*.md'` — retained the proposal-selection decomposition and later-episode compounding test; generic evaluation matches added no traversal value.
- `rg -n -i 'recursive self-improvement|self-improving system|memory-control layer|externalized memory' kb/notes/ --glob '*.md'` — retained the self-improving-system definition and fixed-decomposition boundary.
- `rg -n -i 'self-improv|recursive|working memory|skill memory|experiential memory|trajectory|validation gate|held-out' kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md' --glob '!kb/sources/.snapshots/**'` — retained Self-Harness, SkillOpt, Memento-Skills, ReasoningBank, and SkillRL as the closest mechanism-level comparisons.

**Candidate evaluation:**

- Kept active work state because Recuris's working-memory ledger represents live goals as pending, done, or blocked and closes them only from tool evidence, rather than asking the model to reconstruct state from the transcript.
- Kept pre-action activation because current working-memory state selects experiential skills before the next action; this is the exact behavioral problem the requirement names.
- Kept diagnostic richness because the structured trace links working-memory transitions, invoked skills, actions, observations, and checker decisions to a component-level repair diagnosis. Scalar task success alone would not supply that proposal evidence.
- Kept proposal selection because the fixed Meta-Agent generates a localized candidate patch, the gate can reject it on a failed source task plus development anchors, and accepted memory packages become operative in later runs.
- Kept the fixed-decomposition boundary because the base model, outer harness, localization procedure, update coordinates, and gate stay fixed while only the declared memory-control layer evolves.
- Kept the self-improving-system definition as vocabulary, not as outcome evidence: under the paper's composite harness boundary, accepted memory changes enter later operation, but the reported objective gains and recursive dynamics remain separate claims.
- Kept Self-Harness, SkillOpt, and Memento-Skills because each isolates one neighboring design axis: whole-harness versus memory-layer edits, one-skill versus multi-component memory packages, and utility-trained skill routing versus verified-state activation.
- Kept ReasoningBank and SkillRL as code-grounded memory-system comparisons. ReasoningBank retrieves distilled memories by task-query similarity rather than live goal state; SkillRL combines skill-bank updates with policy training rather than freezing the acting model and evolving only external memory.
- Rejected broad analogies to human working memory and generic agent-harness analyses because they do not clarify Recuris's verified-state, activation, or promotion mechanisms.

**Link following:**

- Followed the active-work-state note to session-history, workshop, and contextual-activation neighbors. This confirmed that Recuris supplies a distinct executable ledger case rather than another retrospective-memory store.
- Followed the activation requirement to governed behavior-changing writes, contextual activation, and effects-based evaluation. This preserved the boundary between implemented routing, observed invocation, causal uptake, and aggregate task benefit.
- Followed diagnostic richness to oracle strength, Meta-Harness, AutoSaddler, and trace-learning reviews. Recuris adds component-tagged state and checker events but does not isolate every trace field's marginal value.
- Followed proposal selection to the self-improving-system definition, fixed decomposition, and compounding tests. This separated membership in a bounded improvement pathway from claims of open-ended redesign or recursive compounding.
- Followed Self-Harness, SkillOpt, Memento-Skills, ReasoningBank, and SkillRL through their own comparison neighborhoods. The retained set spans the nearest distinct edit, gate, routing, and parametric-update choices without duplicating the whole trace-learning landscape.

## Connections Found

- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **is-evidence-for**: Recuris implements live task state as a goal ledger updated from checker-grounded tool evidence, so its next action can depend on unresolved work rather than reconstructing that state from the chronological trace.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) -- **is-evidence-for**: Recuris uses current pending goals and runtime events to select and inject experiential skills before the next action, then separately reports invocation reach and task effects.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: Recuris's structured trace binds working-memory transitions, skill selections, actions, observations, and checker decisions to a component label that conditions the next patch, while the held-out gate remains a distinct selection signal.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: the fixed Meta-Agent proposes a localized memory-package edit, a source-task-plus-development gate can reject it, and an accepted package becomes the memory controller used by later executions and evolution rounds.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting Recuris's gains requires keeping its editable experiential memory, working memory, routing, and checker coordinates separate from the fixed base model, outer harness, localization method, gate, task splits, and objective.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **rests-on**: Recuris reports an additional accepted second-round gain, but successive retained improvements do not by themselves show that the first gain made the later improvement episode more productive.
- [Self-improving system](../../../../notes/definitions/self-improving-system.md) -- **defined-in**: Recuris's RSI framing depends on declaring the composite harness boundary, the task-success objective, the evolution horizon, and the path by which admitted memory changes shape later executions.
- [Ingest: Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both use structured failure evidence, local edits, and regression-aware gates around fixed models; Self-Harness edits broader harness surfaces, while Recuris confines proposals to a four-coordinate memory-control layer coupled to verified working state.
- [Ingest Report: SkillOpt: Executive Strategy for Self-Evolving Agent Skills](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) -- **compares-with**: both validation-select natural-language skill changes around frozen models; SkillOpt optimizes one compact skill with text-edit history, whereas Recuris evolves a package whose skill contents, state ledger, routing, and checkers jointly structure execution evidence.
- [Ingest: Memento-Skills: Let Agents Design Agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- **compares-with**: both treat external skills as mutable behavior-shaping memory and localize failures before gated changes; Memento-Skills learns a utility-oriented router over skill folders, while Recuris routes from verified pending state and retains a separate working-memory ledger.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) -- **compares-with**: ReasoningBank retrieves trajectory-derived memories by task-query embedding similarity and pushes them into the prompt, while Recuris keys skill activation to the current verified goal state and runtime events.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) -- **compares-with**: both distill failed trajectories into reusable skill memory, but SkillRL can co-train policy weights and append skills during training, whereas Recuris keeps the acting model frozen and promotes validation-gated external memory packages.

## Bidirectional Candidates

- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) ↔ source -- **evidenced-by** from the note side: Recuris supplies an executable long-horizon case where verified pending/done/blocked state guides future action independently of the full transcript.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) ↔ source -- **evidenced-by** from the note side: its state/event-grounded invocation path and ablations bear directly on pre-action delivery, while its aggregate results still stop short of per-item causal-faithfulness proof.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) ↔ source -- **evidenced-by** from the note side: Recuris reports a structured-trace versus unstructured localization contrast and implements a trace-to-component-to-patch path distinct from its promotion oracle.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) ↔ source -- **evidenced-by** from the note side: Recuris exposes all three functions in a bounded external-memory update loop with explicit rejection and later reuse.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) ↔ source -- **evidenced-by** from the note side: the paper explicitly fixes the outer procedure and confines all recursive updates to named memory coordinates, making its update-space boundary unusually inspectable.

## Reverse-edge Candidates

- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) → source -- **evidenced-by**: Recuris turns verified pending goals and typed runtime events into rule-ready selection inputs for skill delivery instead of expecting a rule to infer relevance from an undifferentiated history.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source -- **evidenced-by**: the paper reports skill-invocation reach and downstream task success separately and includes mechanism ablations, while leaving individual-skill causal uptake as an additional evaluation layer.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected as a regular edge because the more specific pre-action activation requirement owns the mechanism; Recuris's task-level ablations also do not establish causal uptake of each injected skill.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) -- rejected: Recuris fingerprints and logs memory-path use, but the note concerns successful fallback paths masking broken infrastructure rather than memory-routing attribution.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) -- rejected in favor of sharper comparisons: its coarse website-level workflow injection overlaps the topic, but ReasoningBank better isolates task-query retrieval and SkillOpt/Self-Harness better isolate the update gate.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) and [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected: both expose broader whole-system self-revision boundaries, but neither clarifies the verified-state or memory-package mechanisms as directly as the retained source and system comparisons.

## Index Membership

None. The source itself belongs in `kb/sources/`; a future code-grounded Recuris review, rather than this ingest, would belong in the agent-memory-system index.

## Synthesis Opportunities

- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md), [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md), and [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) together suggest a higher-order claim: a verified work-state ledger can serve both as a pre-action context router and as a post-failure diagnostic scaffold. Recuris is one strong implementation and experiment bundle, but a transferable note should compare another system or derive the dual use before generalizing it.

## Maintenance Observations

None

## Flags

- Split candidate for downstream promotion: the paper makes independent claims about live-state memory, skill activation, failure localization, validation-gated updating, benchmark effects, and recursive dynamics across agent-memory, context-engineering, and self-improvement topics. Keep the ingest unified as source analysis, but place durable system description in a code-grounded Recuris review and promote any general claim separately.
- The pinned checkout can establish that the runtime, working-memory ledger, grounding checks, state/event activation, component-scoped patch schema, and gate machinery are implemented. It does not independently establish the paper's benchmark outcomes, transfer claims, or recursive-effect sizes because no raw experiment results or reproduction run were available.
