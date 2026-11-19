---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/sutskevers-list/chapters/03-resnet-revolution.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: ResNet revolution

**Source:** [ResNet revolution](../../../sources/sutskevers-list/chapters/03-resnet-revolution.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg -n -i '^description:.*(benchmark|human-level|metric|objective|scale|architecture|residual|validation|robustness)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. Flagged objective/proxy, exact-requirement, scaling, evaluation, and Bitter Lesson notes.

**Topic indexes:**
- Read the foundations, evaluation, learning-theory, and self-improving-systems heads. The chapter's best fit is the objective/proxy and scaling boundary; its “human-level” discussion is evaluation evidence, not a self-improvement attribution.

**Body search:**
- Ran `rg -n -i '(residual|human.level|top-5|benchmark|metric|objective|robustness|scale what|architecture)' kb/notes kb/reference --glob '*.md'`. Broad ResNet mentions were rejected unless the target made a claim the chapter could materially bear on.

**Link following:**
- Followed [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) into the target-to-objective gap; kept it because ImageNet top-5 accuracy is checked while its warrant as “human-level vision” is not.
- Followed [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) and [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md).
- Read [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md); retained it as a qualified comparison because residual connections make depth trainable but do not settle frontier robustness.

## Connections Found

- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **is-evidence-for**: the “human-level ImageNet” claim checks a top-5 benchmark threshold but not the linking claim that this metric warrants human-level visual competence, robustness, or understanding.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for**: ResNet's benchmark result can be locally exact while the ImageNet taxonomy, annotator comparison, and top-5 criterion remain conjectured proxies for the broader objective.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **is-evidence-for**: residual structure did not oppose scale; it made deeper optimization work. The case selects against the slogan that compute alone wins and supports the note's distinction between useful structure and unearned reach.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- **compares-with**: residual connections absorb a depth-training obstacle on fixed benchmarks, while adversarial, demographic, and distributional failures reopen the reliability gap at the capability frontier.

## Bidirectional Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) <-> source -- **is-evidence-for**: “human-level ImageNet” is an unusually clear public example of target achievement being mistaken for objective warrant.

## Reverse-edge Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -> source -- **evidenced-by**: the chapter's benchmark critique can serve as a worked external instance.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) -- the objective language overlaps, but the source evaluates a model and benchmark rather than attributing self-improvement to a pathway.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- rejected because ImageNet is a capability benchmark, not a hidden-target discovery benchmark.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- source material for benchmark-to-capability overclaim and robustness limits.
- [Learning theory](../../../../tags/learning-theory-README.md) -- empirical support for architecture as an enabler of scale rather than its opposite.

## Synthesis Opportunities

- “Scale what?” can be made operational by separating resources from the architecture that converts resources into an optimizable signal path and from the metric that certifies the result. Chapters 2, 3, and 6 jointly support this decomposition.

## Maintenance Observations

None

## Flags

- The chapter combines architectural history with a benchmark-validity critique; future promotion should keep those claims separate rather than treating one as evidence for the other.

