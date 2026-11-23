---
description: "Discovery report for the harness-transfer preprint: candidate links for learned orchestration, local execution checks, and strategy retention."
type: types/connect-report.md
source: "kb/sources/language-model-harnesses-compositional-generalizers.ingest.md"
source_has_frontmatter: true
date: "2026-11-20"
depth: standard
---

# Connection Report: Language Model Harnesses Can Be Compositional Generalizers

**Source:** [Ingest: Language Model Harnesses Can Be Compositional Generalizers](../../../../sources/language-model-harnesses-compositional-generalizers.ingest.md)

## Discovery Trace

The ingest separates three results: transfer after short-task training across tested length and domain shifts; improved scheduling after supervised training on teacher-guided synthetic traces within a fixed RLM runtime; and a gated-chain result that changes both training and runtime. The first two gave the strongest connection signal. The chain result does not isolate recursion.

**Topic indexes:**

- Read the `README.md` heads for `theory`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. The agentic-systems head surfaced Fractal as a code-grounded RLM comparison. The historical survey head surfaced the trace-learning comparison, whose inputs are traces of agent runs rather than teacher-guided examples for held-out task strategies. Reference offered system and evaluation navigation, not a Commonplace choice documented as using the preprint's mechanism. The source landing documents the ingest collection but is not a paper roster.
- The source has no `tags:` field, so no source-tag head or by-tag description scan was required. The tag index and the subsequently read `computational-model` head exposed the scheduling cluster, not source membership. `sources` is outside the participating set, and the sources contract provides no formal label to tag heads. No web prospecting: the preprint is already cited in the ingest; it is not a new external candidate.

**Titles and description listing scan:**

- For each of `theory`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`, generated titles with `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`, scanning via `rg -i 'decompos|partition|orchestrat|recursive|recursion|compositional|transfer|surrogat|inference|weight|RLM|Tendril|Fractal|programmatic|context operation|context-operation|fixed boundary|trace.learning|sub.call|merge|parallel'`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` in each of those six destinations, filtering with `rg -i 'recursive language model|\bRLM\b|compositional generaliz|offload|surrogate|decompos|trace.{0,15}learn|model weights|context.operation'`. Theory yielded the persistence note (its claim about losing strategies needs qualification), the fixed-decomposition and context-operation notes (what stayed fixed), and the already-linked scheduling and design-space notes. Sources yielded the similar-title July blog, LongCoT-mini and λ-RLM. Fractal was the strongest agentic-systems match. Tendril and the trace-learning survey were screened for comparison; shared code generation or weight retention alone did not supply the same transfer question. Reference and tags did not yield a formal edge that would help the ingest reader.

**Body search:**

- Across the six destinations ran `rg -l --glob '*.md' -i 'compositional generaliz|surrogate (train|task|trace)|in.distribution|OOLONG'` and `rg -l -i 'ephemeral orchestrator|programmatic sub.calls|locally (familiar|solvable)|offloaded context' ... --glob '*.md'`. These confirmed the closely related July account, the RLM implementation neighborhood, and the need to distinguish strategy repetition from correct local execution. The source records are not independent corroboration just because they have different URLs.
- Theory: `rg -l -i 'local (results|execution)|root (trace|trajectory)|selection (strategies|polic(y|ies))|effective update space|weight.learned|learned decomposition' kb/theory --glob '*.md'` surfaced the persistence note again. Its case for inspectable, test-gated code is distinct from its stronger premise that a fresh query must rediscover the strategy.
- Reference: `rg -l -i 'bounded.context|sub.agent isolation|model.authored|decomposition' kb/reference --glob '*.md'` led to the ablation proposal. It tests a different objective (useful, warranted KB work per unit of human judgment), so neither the preprint's scores nor its controls answer the proposal's question.
- Historical memory systems: `rg -l -i '\bRLM\b|distill.*weights|model.authored orchestrat' kb/agent-memory-systems --glob '*.md'` returned the trace-learning survey and reviews such as Voyager and Self-Training-LLM. The literature overlap is retention form, not evidence on cross-length orchestration; no reverse link proposed from a frozen account.
- Agentic systems: `rg -l -i 'predictrlm|model.authored (code|orchestrat)|programmatic sub.calls' kb/agentic-systems --glob '*.md'` confirmed Fractal. Its review describes a workspace and resumable turns; it does not evaluate the trained policy in the preprint. No inbound citation as evidence about Fractal.
- Sources: `rg -l -i 'sub.calls|decomposition policy|surrogate (train|task|trace)' kb/sources --glob '*.md'` recovered the July account and LongCoT-mini. The July account is useful for comparing what the two source records cover. LongCoT-mini's prompt intervention is useful in the design-space note, but the distinct tasks and bundled controls do not support a direct comparison of effects.
- Tags: `rg -l -i 'compositional|orchestrat|offload' kb/tags --glob '*README.md'` pointed back to `computational-model` and neighboring heads, not an eligible member entry. No similarity scores were produced by these searches.

**Link following:**

- Followed the ingest's scheduling, design-space, and fixed-decomposition links. From the design-space note followed MASS and LongCoT-mini: MASS supplies a different way to select training traces for an orchestrator's weights; LongCoT-mini is already used there as the contrasting prompt-guidance case. The fixed-decomposition note's ACM comparison supplies the stronger example of a narrow operation set; the RLM result does not demonstrate a missing operation.
- Followed the July ingest to the RLM ephemerality note and Fractal. Read the separate strategy-persistence claim against the RLM note's existing allowance for learning in weights; proposed the inbound qualification at the stronger claim rather than both places. The context-operation note separates policy quality from what operations permit, but its comparison holds model and budget fixed; changing model weights is not a pure policy swap under that premise. The transfer-rationale note links the scheduling heuristics and distinguishes observed transfer across varied tasks from a test of which task property caused it. The preprint does the former and does not test retained rationale.

### Candidate origins

- kb/sources/language-model-harnesses-are-compositional-generalizers.ingest.md — titles, descriptions, body-search
- kb/sources/sakana-mass-multi-agent-self-supervision.ingest.md — link-following
- kb/agentic-systems/reviews/fractal.md — curated-head, titles, descriptions, body-search, link-following
- kb/theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md — known, titles, descriptions, body-search, curated-head, link-following
- kb/theory/decomposition-heuristics-for-bounded-context-scheduling.md — known, titles, descriptions, curated-head, link-following
- kb/theory/orchestration-strategies-and-run-state-have-opposite-persistence.md — titles, descriptions, body-search

## Connections Found

- [July practitioner account of harness generalization](../../../../sources/language-model-harnesses-are-compositional-generalizers.ingest.md) — **compares-with**: compare the evidence for RLM transfer after short-task reinforcement learning. The earlier account describes the same general setup and base model; the preprint adds a broader test range, a root-versus-local-execution diagnostic, and surrogate training. Treat experiment overlap as possible, not as replication.
- [Multi-Agent Self-Supervision](../../../../sources/sakana-mass-multi-agent-self-supervision.ingest.md) — **compares-with**: compare how training traces for learned orchestration are obtained. The preprint uses teacher-guided surrogates designed for target strategies; MASS searches written workflows and distills self-ranked executions after removing the workflow text. The comparison is about trace selection, not which system performs better.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — **compares-with**: compare what the RLM program can access outside the root prompt: offloaded benchmark inputs in the preprint versus a mounted workspace and retained session history in Fractal. The review lets the reader inspect a shipped version of model-authored scheduling without assuming that the transfer results apply to it.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Agent orchestration occupies a multi-dimensional design space](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md#decomposition-policy-artifact) → source — **evidenced-by**: gives readers of the decomposition-policy section a measured case where training changes which scheduling programs are generated without changing the runtime that executes them (§4.2). It adds teacher-guided surrogates alongside prompt tips and MASS's workflow-search distillation. The comparison is between training packages, not an isolated effect of any one trace-design choice.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md#empirical-grounding) → source — **evidenced-by**: qualifies what can be inferred from a repeatable split. In the reported OOLONG trace pair, RLM batches labeling calls and counts their outputs in code; Pi can repeat a similar root plan and still produce wrong counts on the longer task. A scheduler designer can use the contrast to check what the local calls returned separately from whether the schedule ran as planned. This is not a tested verification intervention or evidence that open-ended synthesis admits the same split.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../theory/orchestration-strategies-and-run-state-have-opposite-persistence.md#where-it-lands) → source — **evidenced-by**: qualifies the claim that discarding an executable means paying for strategy discovery again on each task. The paper reports reuse of a learned scheduling strategy without a saved executable; it does not show the strategy is individually inspectable, that search is eliminated, or that weights beat a tested code library on cost or trust. A reader deciding what to retain needs that distinction before considering the proposed cache.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — the ingest already uses the distinction. The fixed-runtime result is a success within an admitted space, not a case where a needed correction is outside it; the existing examples are sharper for the note's reader.
- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — already distinguishes disposable programs from possible weight learning. Prefer one qualification at the persistence-economics note, where fresh rediscovery is a premise of the design recommendation. The preprint does not independently establish a general post-return lifecycle for RLM implementations.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — learning from traces and retaining weights are shared features, but the historical comparison concerns loops fed by agents' own runs, not the design of surrogates to teach a specified strategy.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The July ingest says only the root LLM was trained. The preprint distinguishes which tokens enter the loss from which calls use the updated policy. Keep those descriptions scoped to their respective records; the July phrasing is not evidence that the preprint held a separate child model fixed. Preserve both source identities and check overlap before treating the records as separate experiments.

## Flags

- For any future theory citation that depends on the preprint's findings, retain targeted evidence through `cp-skill-ground` or require the pinned snapshot. The ingest's Quotes section is currently empty. Do not infer same-cost training from lower inference tokens or a recursion effect from the gated-chain package.
