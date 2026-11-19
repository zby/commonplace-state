---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/continual-learning-outside-the-weights.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: Continual learning outside the weights

**Source:** [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md)

## Discovery Trace

The source has frontmatter but no `tags:` field, so there were no source-tag-matched by-tag scans. Search scores were not available from the repo-local tools.

### `kb/notes/`

- Read `kb/notes/README.md`, then the curated heads [deploy-time-learning](../../../../tags/deploy-time-learning-README.md), [learning-theory](../../../../tags/learning-theory-README.md), [self-improving-systems](../../../../tags/self-improving-systems-README.md), and [artifact-analysis](../../../../tags/artifact-analysis-README.md). `artifact-analysis-README.md` declares `complete: true`, but the source had no matching source tag, so no by-tag completeness shortcut applied.
- Generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and `rg '^description:' kb/notes/ --glob '*.md'`.
- Ran `rg -n 'continual learning|continuous learning|weight|weights|artifact layer|frozen interpreter|credit assignment|govern' kb/notes/ --glob '*.md'`.
- Opened [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md), [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), and [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md).
- Kept the first three because each completes a distinct articulation: one argues directly that continuous learning can happen outside weights, one names the deployment-time artifact path the article proposes, and one supplies the system boundary the article adopts against Sutton and Javed. Rejected `learning-is-not-only-about-generality` as already mediated through the kept notes rather than the best onward path for this article's reader.
- Existing article links already cover [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md), [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md), and [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md), so they were not retained as missing candidates.

### `kb/reference/`

- Read `kb/reference/README.md`, then generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` and `rg '^description:' kb/reference/ --glob '*.md'`.
- Ran `rg -n 'maintainer|declared frame|review gate|review gates|validator|validators|governed|admission|installation|inside the boundary' kb/reference/ --glob '*.md'`.
- Opened [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md), [Agent memory coverage](../../../../reference/agent-memory-coverage.md), [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md), and [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md).
- Kept `commonplace-declared-frame` because the article explicitly says Commonplace implements the governed form with a maintainer inside the boundary and weights outside it. Kept `agent-memory-coverage` because it is the most compact shipped-surface map for the article's claims about contracts, validators, review gates, and retained artifacts.
- Rejected `where-change-candidates-come-from-in-commonplace` and the tag-readme trace as useful but less direct: they add process texture about candidate discovery and one worked improvement episode, while the kept reference artifacts better answer the article reader's immediate "what exactly is governed here?" question.

### `kb/sources/`

- Read `kb/sources/README.md`, then generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran `rg -n 'continual learning|weights|artifact|memory|rules|govern|credit assignment|frozen' kb/sources/ --glob '*.md'`.
- Opened [Continual Learning in Token Space](../../../../sources/continual-learning-in-token-space.ingest.md), [Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md), [Why AI systems don't learn and what to do about it](../../../../sources/why-ai-systems-dont-learn-and-what-to-do-about-it.ingest.md), and [Artifacts as Memory Beyond the Agent Boundary](../../../../sources/artifacts-as-memory-beyond-agent-boundary.ingest.md).
- Kept HCL because it is the strongest direct empirical anchor for the article's central claim: frozen weights, retained prompt/memory/skill/router updates, reject-capable admission, and measured forgetting. Kept `continual-learning-in-token-space` as the strongest external companion framing of the same anti-weight-monopoly move, but narrower and memory-first.
- `why-ai-systems-dont-learn-and-what-to-do-about-it` passed the articulation test as a real competing diagnosis, but no authorized `articles → sources` label captures "explicit contrast" without downgrading it to a generic adjacency; it therefore moved to Off-authorisation Candidates. Rejected `artifacts-as-memory-beyond-agent-boundary` because environment-side RL artifacts are too indirect a corroborator for this article's governed, revisable artifact-layer claim.

### `kb/articles/`

- Read `kb/articles/README.md`, then generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/articles/ --glob '*.md'` and `rg '^description:' kb/articles/ --glob '*.md'`.
- Used the cross-collection body search `rg -n 'self-improving|theory|reflective|weights|continual learning|artifact' kb/articles/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` to identify nearby companion surfaces.
- Opened [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md) and [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md).
- Kept `when-systems-learn-theories-about-themselves` because it gives the distinct next step where the second substrate becomes reflective self-improvement rather than only a response to Sutton and Javed. Rejected `the-bitter-lesson` as a missing candidate because the source already links it directly in body and in the closing path.

### `kb/agentic-systems/`

- Read `kb/agentic-systems/README.md`, then generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Reused the cross-collection body search `rg -n 'self-improving|theory|reflective|weights|continual learning|artifact' kb/articles/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`.
- Opened [Exo](../../../../agentic-systems/reviews/exo.md).
- Kept `Exo` because it gives a concrete whole-system comparison on the article's governance axes: mutable boundary, retained artifacts, rebuild-and-restart installation, rollback, continuity, and the bounded warrant of build/test/behavior oracles.

### `kb/agent-memory-systems/`

- Read `kb/agent-memory-systems/README.md`, then generated the complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Reused the cross-collection body search `rg -n 'self-improving|theory|reflective|weights|continual learning|artifact' kb/articles/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`.
- Opened [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md).
- No agent-memory-system candidate survived. The survey is useful for trace-mining taxonomy, but this article's reader need is better served by a specific empirical frozen-weight harness case and a whole-system governance comparison than by a broad trace-learning catalogue.

### `kb/instructions/` and `kb/tasks/`

- Read `kb/instructions/README.md`.
- No `kb/instructions/` candidate passed the destination trigger. The article closes with conceptual onward paths into notes, sources, and companion articles, not with a concrete operational next step for the external reader.
- `kb/tasks/` was not prospected because there is no `kb/tasks/COLLECTION.md` or `kb/tasks/README.md` in this checkout.

### Excluded and external destinations

- Per `kb/articles/COLLECTION.md`, `kb/work/` and `kb/reports/` were excluded as durable link destinations.
- The reserved `external` destination is authorized for already-known targets, not open-web prospecting. No separate external target was supplied beyond the sources already in local context, so external prospecting was skipped.

## Connections Found

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **extends**: this is the fuller theoretical argument for the article's core move that a deployed system can keep learning through retained prompts, rules, tools, schemas, and tests without waiting for another weight-training cycle.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- **evidenced-by**: this note states the article's strongest local subclaim directly and concretely, arguing that prompts, schemas, tools, and tests already accumulate durable adaptive capacity during deployment outside weights.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **extends**: the article argues at the system boundary against Sutton and Javed's weight-centered inference, and this note supplies the decomposition argument for why prompts, retrieval, validators, tools, and runtime policy belong inside that learning unit.
- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) -- **evidenced-by**: the article's claim that Commonplace implements the governed form with a maintainer inside the boundary and provider weights outside it needs this exact boundary declaration.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- **evidenced-by**: this is the most compact shipped-system trace for the article's claim that the artifact layer is governed through contracts, validation, review, activation surfaces, and retained explicit artifacts rather than left as raw memory accumulation.
- [Harness Continual Learning: Continual Adaptation Beyond Model Parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- **evidenced-by**: HCL is the clearest source-side empirical case of frozen-weight continual learning through retained task-interface, memory, skill, and routing edits admitted by a reject-capable evaluator.
- [Continual Learning in Token Space](../../../../sources/continual-learning-in-token-space.ingest.md) -- **see-also**: this gives an external memory-first framing of the same anti-weight-monopoly move, useful precisely because it is narrower than the article's broader governed-artifact-layer account.
- [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md) -- **extends**: this companion carries the argument forward from "a second substrate exists" to the harder case where the retained theory is about the system itself and guides self-change.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo is a concrete artifact-mediated self-modification system with explicit rollback and continuity, but its unattended acceptance is bounded by build, test, and immediate-behavior oracles rather than the article's claim-level governance story.

## Bidirectional Candidates

- [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md) <-> source -- **extends**: that article depends on the same governed-artifact substrate and Commonplace boundary, but it currently does not send readers back to this explicit Sutton-and-Javed disagreement and second-substrate argument.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

- [Why AI systems don't learn and what to do about it](../../../../sources/why-ai-systems-dont-learn-and-what-to-do-about-it.ingest.md) -- the article genuinely connects to this source because both reject the sufficiency of current deployed systems while disagreeing about whether non-weight artifact learning already counts; the needed relationship is an explicit contrast, but `kb/articles/COLLECTION.md` authorizes only `evidenced-by` and `see-also` for `articles → sources`. Suggest either extending the authorized source labels to include a contrastive option or deciding that this comparison should stay routed through notes instead.

## Raw Text Candidates

None.

## Rejected Candidates

- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) -- important as the Simon criterion behind several kept notes, but the article reader is better served by the more specific deployment-time and whole-system notes that already carry that criterion into this exact disagreement.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- relevant to how Commonplace notices and drafts improvements, but less direct than the kept boundary and coverage references for this article's claim about governed retained artifacts.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- a good worked episode, but too narrow compared with the broader shipped-surface evidence in `agent-memory-coverage`.
- [Artifacts as Memory Beyond the Agent Boundary](../../../../sources/artifacts-as-memory-beyond-agent-boundary.ingest.md) -- it supports memory-as-environment and effect-based evaluation, but that is too indirect from the article's claim about a revisable, governed artifact layer for describable changes.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- broad and useful, but its main value is taxonomy of trace-mining loops rather than the narrower question this article raises about frozen interpreters, governance, and weight versus artifact learning.
- [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) -- strong fit, but already linked in the source body and closing section, so not a missing connection candidate.

## Index Membership

None. The source is already listed in `kb/articles/README.md` under the draft sequence.

## Synthesis Opportunities

None.

## Maintenance Observations

- `kb/articles/COLLECTION.md` still authorizes `kb/tasks/` as an outbound destination for concrete reader next steps, but this checkout has no `kb/tasks/COLLECTION.md` or `kb/tasks/README.md`. The destination could not be prospected and now behaves as a contract-level dead route.

## Flags

- Split candidate: the article carries at least four separable burdens — rejecting substrate continuity, defining the governed artifact layer, pricing its limits, and proposing the comparison experiment — and attracted candidates across notes, reference, sources, articles, and agentic-systems. The current draft sequence may justify that span, but it is broad enough to watch for future article splitting.
