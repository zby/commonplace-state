---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/sutskevers-list/chapters/02-the-alexnet-moment.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: The AlexNet moment

**Source:** [The AlexNet moment](../../../sources/sutskevers-list/chapters/02-the-alexnet-moment.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg -n -i '^description:.*(feature|representation|bitter lesson|decomposition|learned|fixed|scale|requirement|architecture|data)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. Flagged the fixed-decomposition, Bitter Lesson, exact-requirement, design-space, and representational-form-coevolution notes.

**Topic indexes:**
- Read the foundations and learning-theory heads. The chapter is a strong worked case for expanding the effective update space, not merely a generic history of computer vision.
- Read the evaluation and self-improving-systems heads. Evaluation contributes benchmark caveats; the reflective cluster is not the right primary home because the learned representation remains distributed-parametric and indirectly addressable.

**Body search:**
- Ran `rg -n -i '(fixed decomposition|representation|inductive bias|scale|benchmark|objective|ablation|architecture|data)' kb/notes --glob '*.md'`. Followed the exact feature-pipeline and Bitter Lesson hits rather than broad architecture matches.

**Link following:**
- Read [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) fully; it already names handcrafted vision features as the information-omission case.
- Followed it to [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) and [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md).
- Read [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md); kept it because it explicitly uses the SIFT/HOG-to-representation-learning transition as its model case.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: AlexNet moved feature selection from a fixed handcrafted pipeline into the trainable update space, allowing task error to revise representations that SIFT/HOG-style systems froze upstream.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for**: handcrafted feature extractors could be implemented exactly while the upstream requirement that their outputs preserved everything vision needed remained unvalidated.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: the chapter supplies the historical mechanism already invoked by the note—end-to-end learning extended the same optimizer across representation and classifier rather than merely improving the downstream classifier.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **is-evidence-for**: AlexNet displaced hand-designed features whose scope across ImageNet categories had not been earned, while retaining strong architectural structure such as convolution, locality, augmentation, and an externally fixed benchmark.

## Bidirectional Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) <-> source -- **is-evidence-for**: the chapter is a detailed secondary account of the note's named vision-feature case.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) <-> source -- **is-evidence-for**: the source elaborates the representational-form transition that grounds the note's mainstream direction.

## Reverse-edge Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -> source -- **evidenced-by**: the chapter collects the feature-pipeline mechanism, benchmark result, and architecture/training interventions in one worked history.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) -- relevant in spirit, but the fixed-decomposition note captures the source's causal contribution more directly.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- rejected: end-to-end gradient learning expands update scope but does not make the learned representation directly readable or selectively revisable.

## Index Membership

- [Learning theory](../../../../tags/learning-theory-README.md) -- strong empirical source for the fixed-decomposition and representational-form-coevolution cluster.
- [Constraining](../../../../tags/constraining-README.md) -- historical case for relaxing a proxy theory while retaining warranted architectural constraints.

## Synthesis Opportunities

- AlexNet suggests a precise formulation of “end to end”: move a consequential, error-sensitive boundary inside the effective update space while leaving independently useful constraints fixed. The existing fixed-decomposition and coevolution notes may already cover this; promote only if a second domain adds a distinct mechanism.

## Maintenance Observations

None

## Flags

- Reported ablations vary activations, dropout, augmentation, layer count, and GPU partitioning, but do not vary ImageNet's label taxonomy, top-5 objective, raw-pixel input, or convolutional inductive bias; the result validates only the varied region.

