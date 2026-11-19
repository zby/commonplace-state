---
description: "Discovery report for possible KB connections from the Memento-Skills paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/memento-skills-let-agents-design-agents.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Memento-Skills: Let Agents Design Agents

**Source:** [Memento-Skills: Let Agents Design Agents](../../../sources/memento-skills-let-agents-design-agents.md)

## Discovery Trace

**Description listing scan:**
- Read the `kb/notes/` tag hub and the curated heads for `self-improving-systems`, `deploy-time-learning`, and `agent-memory`; then ran the complete `#` title listing and a scoped description scan over `kb/notes/` for `skill|deploy|external|artifact|reflect|self-improv|routing|retriev|transfer|domain|learn`. Kept the readable-artifact, retrieval-as-reflection, and evaluate-memory-by-effects claims; rejected broader continual-learning and abstraction notes when the paper supplied only a local example rather than evidence for their full mechanism.
- Read `kb/reference/README.md`, ran the complete reference title listing, and scanned descriptions for `skill|router|retriev|learning|memory`. The hits describe Commonplace's shipped skill loading and connection machinery; none needs this external paper to understand the shipped system, so no reference candidate was kept.
- Read `kb/agent-memory-systems/README.md`, ran the complete title listing, and scanned descriptions for `skill|trace|learn|workflow|memory`. Followed Voyager, SkillRL, SkillNote, and the trace-learning comparison. Voyager passed as the clearest executable-skill-library comparison; SkillRL is represented more directly by its source ingest, while SkillNote's registry governance is adjacent but not a close experimental comparison.
- Read `kb/agentic-systems/README.md`, ran the complete title listing, and scanned descriptions for `skill|router|retriev|learn|evolv|reflect`. The results concern whole harnesses and orchestration rather than skill-memory learning, so none passed the articulation test.
- Ran the complete ingest-report title listing and a source-description/body scan for `Memento-Skills|SkillOpt|SkillRL|trajectory-informed|externalization|self-evolving agents`. Kept SkillOpt, SkillRL, Trajectory-Informed Memory Generation, and the self-evolver faithfulness paper as comparisons on mutation unit, update substrate, retrieval, and causal uptake.

**Topic indexes:**
- `kb/notes/self-improving-systems-README.md` surfaced reflection, proposal-selection, retrieval failure, and oracle-bounded autonomy.
- `kb/notes/deploy-time-learning-README.md` surfaced the readable-artifact loop, deploy-time adaptation, diagnostics, and evaluation.
- `kb/notes/agent-memory-README.md` surfaced effects-based evaluation, activation, trace extraction, and memory governance.
- `kb/agent-memory-systems/README.md` surfaced the external system landscape; no tag README applied because the snapshot carries no `tags` field.

**Body search:**
- `rg -n -i 'skill library|skills as memory|deploy-time learning|behavio(u)?ral.*rout|domain align|cross-task transfer|reflective.*skill|external.*memory|mutable.*artifact' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` -- confirmed the three note candidates and the Voyager comparison; generic memory and architecture hits were rejected as topical only.
- `rg -n -i 'Memento-Skills|SkillOpt|SkillRL|trajectory-informed|externalization|self-evolving agents' kb/sources/ --glob '*.ingest.md'` -- found the four settled sibling-source comparisons.
- `rg '^description:'` scans in each authorized local destination were used to evaluate triggers before full-file reading; `kb/reference/` and `kb/agentic-systems/` produced no accepted candidates.

**Link following:**
- Followed the readable-artifact loop into deploy-time learning and diagnostic richness. Memento-Skills directly instantiates the first, but its unit-test rollback gate is too thinly evaluated to bear the diagnostic-richness claim by itself.
- Followed retrieval-as-reflection into behavioral authority. The router's top-1 and end-to-end comparisons make retrieval operativeness concrete, while the paper does not test whether a retrieved skill is ignored after injection.
- Followed evaluate-memory-by-effects into the self-evolver faithfulness source. The sources complement one another: Memento-Skills measures routing and outcome effects, whereas the faithfulness paper warns that stored condensed experience can remain behaviorally inert.
- Followed Voyager into the trace-learning comparison. Both make learned skills executable; Memento-Skills adds in-place failure-driven rewriting, discovery, rollback, and behavior-trained routing.

## Connections Found

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: Memento-Skills is a concrete frozen-model loop whose retained policy is a mutable folder combining natural-language specifications, prompts, and executable code, updated from deployment feedback.
- [Retrieval failure is reflection failure](../../../notes/retrieval-failure-is-reflection-failure.md) -- **is-evidence-for**: behavior-aligned routing improves both top-1 route hits and end-to-end execution over lexical and generic embedding retrieval, showing that the retrieval wire must select artifacts for behavioral utility rather than surface similarity.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- **is-evidence-for**: the paper evaluates both offline retrieval quality and downstream trajectory success and reports when learned skills fail to transfer because they are not retrieved on structurally dissimilar tasks.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: both turn experience into executable skill memory around a frozen LLM; Memento-Skills adds failure attribution, in-place multi-file rewriting, skill discovery, rollback tests, and behavior-trained routing beyond Voyager's success-gated code promotion and embedding retrieval.
- [SkillOpt](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) -- **compares-with**: both optimize readable external policy from scored execution, but SkillOpt validation-selects edits to one compact prose skill while Memento-Skills routes, rewrites, and expands a multi-skill natural-language-plus-code library online.
- [SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- **compares-with**: both learn skill banks from trajectories, but SkillRL co-trains model weights to consume natural-language skills whereas Memento-Skills freezes the LLM and adapts the external skill artifacts plus a separate routing model.
- [Trajectory-Informed Memory Generation](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) -- **compares-with**: both learn reusable operational guidance from success and failure, but TIMG retrieves distilled tips while Memento-Skills mutates executable multi-file skills and attributes each failure to a selected skill.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with**: that paper shows condensed experience can be present but behaviorally inert; Memento-Skills attempts to close the uptake gap with behavior-trained routing and executable skills, though it does not run direct memory-perturbation faithfulness tests.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- **evidenced-by**: the paper is a direct natural-language-plus-symbolic, frozen-model instantiation of the claimed tractable loop.
- [Retrieval failure is reflection failure](../../../notes/retrieval-failure-is-reflection-failure.md) → source -- **evidenced-by**: the routing ablation quantifies how a semantically plausible but behaviorally wrong retrieval wire reduces later execution success.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source -- **evidenced-by**: Memento-Skills separately measures route hits and final task success rather than treating a growing skill library as sufficient evidence of learning.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected: the failure-attribution and trace inputs are an example, but the paper does not ablate diagnostic richness or establish its general bottleneck claim.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- rejected: domain-aligned transfer and targeted rewriting bear on scope, but the system does not require explicit applicability boundaries and therefore does not test the note's discriminator.
- [SkillNote](../../../../agent-memory-systems/reviews/skillnote.md) -- rejected: both use persistent skills, but SkillNote's registry, ratings, and explicit promotion path answer a governance problem Memento-Skills largely leaves open; the overlap alone would not improve traversal.

## Index Membership

None

## Synthesis Opportunities

- Memento-Skills, [retrieval failure is reflection failure](../../../notes/retrieval-failure-is-reflection-failure.md), and the [self-evolver faithfulness study](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) together suggest a sharper claim: a reflective artifact loop needs both behavior-aligned selection and causal uptake after selection; route-hit and memory-perturbation tests measure different breaks in that wire.

## Maintenance Observations

None

## Flags

- The paper reports strong gains but leaves skill-library governance largely unmeasured: conflict resolution, provenance from trace to rewritten file, retirement, catastrophic cross-skill interaction, and safety beyond one generated unit test are open boundaries.
