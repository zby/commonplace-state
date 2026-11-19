---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/continual-harness-online-adaptation-foundation-agents.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Continual Harness: Online Adaptation for Self-Improving Foundation Agents

**Source:** [Continual Harness](../../../sources/continual-harness-online-adaptation-foundation-agents.md)

## Discovery Trace

**Curated heads:**
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/self-improving-systems-README.md`, `kb/notes/deploy-time-learning-README.md`, and `kb/notes/agent-memory-README.md`. These routed the paper toward readable-artifact learning, representational-form coevolution, diagnostic evidence, fixed update spaces, and memory-as-learning rather than storage alone.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. No direct shipped-Commonplace analogue or existing embodied-agent whole-system analysis was strong enough to retain; the code-grounded Agentic Harness Engineering review supplied a useful cross-domain comparison.
- The source has no `tags` field, so no by-tag `rg` sweep was available to skip or run.

**Full title and description scans:**
- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`, then filtered candidate titles with `rg -i 'harness|self-improv|adapt|learn|reflect|memory|skill|agent|feedback|trajectory|runtime|deploy|experience|failure|revision|codif|update space|decomposition|context'`.
- Generated description surfaces with `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`, then filtered with `rg -i 'harness|self-improv|adapt|co-learn|reflect|feedback|trajectory|runtime|deploy|experience|failure|revision|skill|memory|update|decomposition|diagnostic'`.

**Body search:**
- `rg -l -i 'continual harness|harness refinement|self-refin(e|ing)|co-learning|co-evolv|reset-free' ...` retained Co-Harness, Self-Harness, readable-artifact learning, and representational-form coevolution; generic self-refinement papers were rejected because they do not revise the same mixed harness surface online.
- `rg -l -i 'failure signatures|trajectory (window|data)|trajectory.*refin|diagnostic.*trajectory|outer-loop learning' ...` retained diagnostic richness and Agentic Harness Engineering; generic trajectory-memory systems were rejected because they distill tips or memories rather than revise a full harness in place.
- `rg -l -i 'prompt.*sub-agent.*skill.*memory|prompt.*skills.*memory|harness.*memory.*skills|behavior-determining organization' ...` confirmed that the paper's four mutable components span natural-language and symbolic behavior-determining artifacts. Broad memory-system matches were rejected when they lacked harness-wide revision.
- `rg -l -i 'capability floor|model capability|stronger models.*scaffolding|scaffolding.*stronger models' ...` retained the scaffolding-scaling note as a qualification: stronger models may need less fixed scaffolding yet exploit a revisable harness more effectively.

**Link following:**
- Followed the deploy-time-learning head into [readable-artifact learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), and [diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md).
- Followed their worked cases to [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md), [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md), and [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md). Co-Harness is the closest weight-plus-harness comparison; Self-Harness is the closest same-model harness-editing comparison; Agentic Harness Engineering is useful for trace staging and regression-gated adoption.
- Applied [learning inside a fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): the mutable space includes prompt, sub-agent definitions, skills/code, memory, and in the co-learning stage model weights; fixed choices include frame/text-map observations, button actions, the four-part partition, meta-tool API, refiner schedule/context, model family, reward construction, milestone metric, and Pokémon environments.
- External prospecting was skipped: `external` is authorized only for already-known targets, and no external target beyond the captured paper was supplied.

## Connections Found

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: the paper keeps natural-language prompt/memory, symbolic skills/tools, and distributed-parametric weights as separately mutable but coupled state in one reset-free trajectory loop.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: prompt, sub-agent, skill, and memory artifacts are edited in place at deployment tempo, and the pathfinding oracle supplies a bounded validation case for one symbolic skill.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: the Refiner consumes recent trajectory windows, identifies failure signatures, and applies component-specific edits, though the paper does not ablate this evidence surface against poorer alternatives.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting the gains requires separating mutable prompts, agents, skills, memory, and weights from the fixed observation/action interface, component partition, refinement protocol, objective, and benchmark.
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- **is-evidence-for**: the Flash-Lite failure and Pro Pareto gain qualify the substitution story by showing that stronger models can extract more marginal value from an adaptive harness even on the same task.
- [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: both couple model-weight updates to mixed-form harness changes, but Continual Harness refines during a continuous embodied episode while Co-Harness alternates regression-gated repair and fine-tuning across benchmark rounds.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both use the target model to help improve its harness, but Continual Harness adopts edits mid-episode without a reject-capable candidate gate and additionally updates model weights.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: both turn trace evidence into mixed prompt/tool/skill/memory changes, while AHE stages debugger reports and regression-gates versions instead of directly editing a live embodied run.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) → source -- **evidenced-by**: this is a second all-three-form case after Co-Harness and differs by coupling harness edits and model updates to one reset-free environment trajectory.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- **evidenced-by**: the paper supplies an empirical mixed natural-language/symbolic loop whose retained artifacts change during use.
- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) → source -- **evidenced-by**: the model-capability ablation bounds the note's substitution account by distinguishing fixed expert scaffolding from a harness a capable model can continually revise and exploit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected because Continual Harness directly applies Refiner edits and soft-SFT updates; it does not expose a reject-capable candidate-selection stage.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected as a direct edge because the survey concerns memory extraction and reinjection systems; the narrower diagnostic-richness and AHE connections carry the useful comparison.
- `kb/reference/` candidates -- rejected because the paper bears on transferable methodology rather than a specific shipped Commonplace component.
- `kb/agentic-systems/` candidates -- rejected because no current whole-system analysis covers this embodied harness or a sufficiently close mechanism.

## Index Membership

None

## Synthesis Opportunities

- [Scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) and this paper together suggest separating **scaffolding as a substitute for model capability** from **revisable scaffolding as a capability amplifier**: a weak model may fail to use the latter even when a strong model needs less of the former.

## Maintenance Observations

None

## Flags

- The paper makes independent claims about human-in-the-loop harness engineering, automated online harness refinement, and joint model-harness training; any promoted theory should select one mechanism rather than importing the paper as a single undifferentiated result.
