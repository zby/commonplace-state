---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/the-alberta-plan-for-ai-research.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: The Alberta Plan for AI Research

**Source:** [The Alberta Plan for AI Research](../../../../sources/.snapshots/the-alberta-plan-for-ai-research.md)

## Discovery Trace

**Source reading and authorisation:**

- Read the full snapshot. Its stable vision treats intelligence as online reward maximization through continual sensing, acting, learning, and model-based planning under finite computation. Its research plan progressively adds learned representations, prediction, control, planning, temporal abstraction, utility-based replacement of abstractions, and intelligence amplification.
- Read the source collection's outbound rules. The snapshot is immutable; candidate outbound edges belong on the matching ingest report. Authorised local prospecting destinations are `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`; `work` and `instructions` are excluded. The matching ingest did not exist during this pass.

**Notes:**

- Curated head read: [notes README](../../../../notes/README.md). The source has no `tags:` field, so no tag-README or by-tag `rg` pass applied.
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`.
- Description listing: `rg '^description:' kb/notes/ --glob '*.md'`.
- Body searches: `rg -n -i 'bitter lesson|search and learning|human[- ](coded|designed|supplied)|scal(e|ing).*comput' kb/notes/ --glob '*.md'`; `rg -n -i 'continual learning|non[- ]stationar|temporal uniform|online learning' kb/notes/ --glob '*.md'`; `rg -n -i 'world model|action-conditioned|transition model|model-based.*planning' kb/notes/ --glob '*.md'`; `rg -n -i 'fixed decomposition|feature.*(replace|utility)|simplest setting|parts and (the )?whole|low-degree-of-freedom' kb/notes/ --glob '*.md'`; `rg -n -i 'foreground|background|asynchronous|reaction time|limited computation' kb/notes/ --glob '*.md'`.
- Kept [the production-method reading of the Bitter Lesson](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md), with the qualification that the Alberta Plan supports Sutton's search/learning-versus-human-insight axis but not the note's representational-form orthogonality or learned-localized conjecture.
- Kept [the action-model consumption-path claim](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md): the Plan's transition model affects action only through planning that updates value functions and policies.
- Kept [the human-analogy boundary claim](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md): computational latency and per-step duties warrant the foreground/background split before a footnote compares it with Kahneman.
- Kept [the fixed-decomposition claim](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): the roadmap progressively enlarges the effective update space, culminating in Oak's utility-based replacement of features, subtasks, options, and option models, while leaving the reward objective, signal interface, and temporal discipline fixed.
- Rejected the obvious world-model, continual-learning, and decomposition keyword hits listed under Rejected Candidates when their stronger claims did not pass the articulation test.

**Reference:**

- Curated head read: [reference README](../../../../reference/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`.
- Description listing: `rg '^description:' kb/reference/ --glob '*.md'`.
- Body searches: `rg -n -i 'bitter lesson|continual learning|world model|reinforcement learning|temporal uniform' kb/reference/ --glob '*.md'`; `rg -n -i 'agent architecture|self-improv|adaptive|background.*loop|asynchronous.*planning' kb/reference/ --glob '*.md'`.
- No candidate passed. The hits describe Commonplace's shipped state, review machinery, or proposals rather than a reader-useful relationship to the Alberta Plan.

**Sources:**

- Curated head read: [sources README](../../../../sources/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`.
- Description listing: `rg '^description:' kb/sources/ --glob '*.md'`.
- Body searches: `rg -n -i 'bitter lesson|search and learning|Sutton' kb/sources/ --glob '*.md'`; `rg -n -i 'continual learning|non[- ]stationar|online learning|temporal uniform' kb/sources/ --glob '*.md'`; `rg -n -i 'world model|action-conditioned|transition model|planning' kb/sources/ --glob '*.md'`; `rg -n -i 'feature.*(utility|replace)|self-adapt|reward.*(modify|learn)|representation learning' kb/sources/ --glob '*.md'`; `rg -n -i 'foreground|background|asynchronous|fast[/ -]slow|dual[- ]loop' kb/sources/ --glob '*.md'`.
- Kept comparisons with [Meta V-JEPA 2](../../../../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md), [Ashby's *Design for a Brain*](../../../../sources/ashby-design-for-a-brain-1960.ingest.md), and [Craik's model-mediated action hypothesis](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md).
- The Plan explicitly depends on [Sutton's original Bitter Lesson essay](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md), but the load-bearing `rests-on` label is not authorised for a sources-to-sources edge; this is therefore off-authorisation rather than a downgraded `see-also`.
- Rejected the broader MAPE-K comparison because both documents being agent-architecture research agendas was not specific enough after the stronger timing, world-model, and update-space candidates were available.

**Agent memory systems:**

- Curated head read: [agent-memory-systems README](../../../../agent-memory-systems/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`.
- Description listing: `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Body searches: `rg -n -i 'continual learning|online learning|reward|long-lived|lifelong' kb/agent-memory-systems/ --glob '*.md'`; `rg -n -i 'world model|transition model|planning|policy learning|feature (finding|selection)' kb/agent-memory-systems/ --glob '*.md'`; `rg -n -i 'foreground|background|asynchronous|dream[- ]cycle|fast[/ -]slow' kb/agent-memory-systems/ --glob '*.md'`.
- Kept [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) as a lower-evidence, doc-grounded comparison on lifelong reward maximization, self-modification, payoff-per-time, and reversible retention.
- Rejected AgeMem because its fixed memory-operation policy and task rewards concern memory management rather than the Plan's general agent architecture. Rejected AriGraph because its per-run semantic graph is retrieval state, not the learned transition model the Plan uses for continual control.

**Agentic systems:**

- Curated head read: [agentic-systems README](../../../../agentic-systems/README.md).
- Full title surface: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`.
- Description listing: `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Body searches: `rg -n -i 'continual|self-improv|adaptive|rewrit|reward' kb/agentic-systems/ --glob '*.md'`; `rg -n -i 'foreground|background|asynchronous|scheduler|dream[- ]cycle|fast[/ -]slow' kb/agentic-systems/ --glob '*.md'`; `rg -n -i 'world model|planning|policy|transition model' kb/agentic-systems/ --glob '*.md'`.
- Kept [GBrain](../../../../agentic-systems/reviews/gbrain.md) for its explicit scheduled dream cycle versus the Plan's temporal-uniformity discipline, and [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) for its versioned mutable resource space versus Oak's continually replaced abstraction stack.

**Link following:**

- Followed the action-model note to [world-model reach assessment](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md). That neighbor clarified why the Plan supports planning/control but not the stronger explanatory-reach claim.
- Followed the human-analogy note to [psychology-to-agent transfer](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) and [first-principles design-space analysis](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md). The neighborhood supported keeping only the Plan's concrete target-side timing rationale, not treating its Kahneman footnote as architectural evidence.
- Followed the fixed-decomposition note to its Ashby and Autogenesis cases. They exposed a coherent chain from fixed update repertoire, through Oak's broader mutable component set, to a modern framework whose taxonomy itself changed.
- Followed the Bitter Lesson note to [the original essay ingest](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md); this revealed the authorised-label gap for the Plan's explicit intellectual dependency.
- Followed GBrain to [the host-language scheduler](../../../../notes/the-practical-scheduler-is-the-host-language.md) and [orchestration/run-state persistence](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md). Those neighbors confirmed that the useful comparison is update cadence and execution locus, not generic topical similarity.
- Followed Incremental Self-Improvement to [its source ingest](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md), confirming the comparison is reward-gated self-modification under a lifelong time budget and not ordinary document memory.

## Connections Found

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) — **is-evidence-for**: the Plan independently states Sutton's production-method contrast as scalable search and learning versus human assistance and domain insight; it does not establish the note's separate form-axis conjecture.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: the learned transition model predicts successor state and reward from state-action or state-option inputs, and becomes behaviorally consequential only when continual planning uses those predictions to change value functions and policies.
- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) — **is-evidence-for**: the Plan derives foreground/background roles from finite compute, fixed-length time steps, and latency obligations, then uses Kahneman only as a comparison, giving a concrete case where target-side constraints—not resemblance—warrant the boundary.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: the roadmap first learns inside a supplied base-agent decomposition, then Oak explicitly moves features, subtasks, options, and option models into a utility-assessed replacement loop while keeping other coordinates fixed.
- [Meta V-JEPA 2 action-conditioned world model](../../../../sources/meta-v-jepa-2-action-conditioned-world-model.source-review.md) — **compares-with**: both architectures use learned action-conditioned predictions for planning, but the Plan requires temporally uniform continual learning under an average-reward sensorimotor loop, whereas V-JEPA 2 combines video pretraining, robot action conditioning, goal-embedding scoring, and model-predictive control.
- [Design for a Brain (1960)](../../../../sources/ashby-design-for-a-brain-1960.ingest.md) — **compares-with**: both put adaptive reorganization inside the agent, but Ashby's slower loop changes behavior only after a viability-bound breach, whereas the Plan makes learning and planning operate on every uniform time step and later ranks components by ongoing utility.
- [Craik, Hypothesis on the Nature of Thought (1943)](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) — **compares-with**: Craik supplies the historical translation-simulation-action account, while the Plan specifies a learned transition model, value functions, and policies as a concrete consumption path for imagined consequences.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) — **compares-with**: both study lifelong reward-maximizing agents whose learning cost counts against acting, but Schmidhuber makes self-modifying policy distributions and payoff-per-time rollback central while the Plan progressively learns representations, models, policies, and abstractions under a fixed scalar reward objective.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) — **compares-with**: GBrain separates live host-agent work from interval- or quiet-hours-triggered dream-cycle maintenance, a direct cadence contrast with the Plan's rule that learning, planning, and meta-algorithms operate on every time step.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) — **compares-with**: Oak continually reassesses and replaces instances in a feature→subtask→option→model progression; Autogenesis versions and evolves prompt/tool/agent/environment/memory resources and demonstrates that the resource taxonomy and orchestration boundary can themselves remain fixed or change across revisions.

## Bidirectional Candidates

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) ↔ source — **evidenced-by**: once the matching ingest exists, the note would benefit from this modern worked architecture in which a retained learned model reaches action selection only through a named planner→value/policy path. The return link must target the ingest, never the snapshot.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) ↔ source — **evidenced-by**: once the matching ingest exists, the note could use Oak as a conceptual case of deliberately widening an effective update space while making clear that the Plan proposes rather than empirically validates the benefit. The return link must target the ingest, never the snapshot.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

- [Ingest: The Bitter Lesson](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) — the Plan says its computational priorities “must heed” Sutton's Bitter Lesson, so the specific reader need is **rests-on**, not adjacency. The sources contract authorises `rests-on` only for a notes destination, not sources→sources. Extend that destination rule if this kind of source-side intellectual dependency should be representable; otherwise reject the edge rather than downgrade it to `see-also`.

## Raw Text Candidates

None

## Rejected Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — the Plan uses learned prediction for control, but does not represent a candidate commitment's generality or test its predictions across the intervention/shift class that the stronger explanatory-reach claim requires.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — the Plan develops continual learning within learned numerical representations and algorithms; it does not compare or jointly evolve the KB note's natural-language, symbolic, and distributed-parametric forms.
- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — the Plan's “front load” means study difficult issues first in their simplest setting, not commit the least-flexible choice first; the shared word names different ordering rules.
- [The Vision of Autonomic Computing](../../../../sources/the-vision-of-autonomic-computing.ingest.md) — both are broad research agendas for adaptive agents, but the MAPE-K comparison remained too general after more specific cadence, learned-model, and mutable-update-space candidates were found.
- [AriGraph](../../../../agent-memory-systems/reviews/AriGraph.md) — its temporary semantic graph and episodic observations alter retrieval and planning inside a run, but they are not the continually learned action-conditioned transition model or long-lived adaptive architecture described by the Plan.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — adaptation and agent-memory keywords overlap, but this is a plan for Commonplace's shipped surfaces and creates no concrete traversal benefit from the Alberta research agenda.

## Index Membership

None

## Synthesis Opportunities

- The Alberta Plan, [Ashby's two-timescale ultrastability](../../../../sources/ashby-design-for-a-brain-1960.ingest.md), and [GBrain's scheduled dream cycle](../../../../agentic-systems/reviews/gbrain.md) jointly suggest that **continual adaptation and temporal uniformity are separate design axes**. Per-step learning, violation-triggered reorganization, and scheduled consolidation are rival cadence choices with different latency, coordination, and credit-assignment costs. The existing [representational-form coevolution note](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) names asynchronous pace mismatch across forms but does not own this cadence decomposition.

## Maintenance Observations

- The off-authorisation Bitter Lesson dependency exposes a collection-contract gap: source-side analyses can declare that they `rest-on` a note but cannot express the same reader need when the best local target is another tracked source analysis. Decide at contract-maintenance time whether sources→sources `rests-on` is a recurring legitimate edge or whether such dependencies should always be mediated by a theory note.

## Flags

- The matching authored surface, `kb/sources/the-alberta-plan-for-ai-research.ingest.md`, was absent during discovery. Apply candidate outbound edges only after that ingest exists; never edit or link durably to the snapshot.
- The paper makes several independent claims across research vision, base-agent architecture, and a twelve-step roadmap. If many candidates are applied, place them next to the corresponding ingest analysis rather than as one undifferentiated related-links footer.
