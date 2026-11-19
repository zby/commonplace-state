---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/seed-programmed-autonomous-general-learning.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Seed-Programmed Autonomous General Learning

**Source:** [Seed-Programmed Autonomous General Learning](../../../../sources/.snapshots/seed-programmed-autonomous-general-learning.md)

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^description:' kb/notes --glob '*.md' | rg -i 'bootstrap|reflect|cumulative|autonom|generality|causal|learning'` flagged the bootstrap, reflection, fixed-decomposition, and generality notes kept below. Factory-learning and continual-learning notes were evaluated but rejected because their software-production and governance mechanisms are more specific than this paper's cognitive-architecture theory.
- Title scans over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` using `rg -N --no-heading -m1 '^# '` found no stronger reference or system-analysis destination than the notes retained below.

**Topic indexes:**
- Read `kb/notes/tags-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/self-improving-systems-README.md`. The learning-theory and self-improving-system clusters supplied the retained candidates.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. Their current-system and external-system entries did not provide an appropriately scoped target for this source-side theory.

**Body search:**
- `rg -n -i 'seed.program|bootstrap|cumulative learning|autonomous general|micro.ampliative|causal.relational|reflection|self.supervis|causal relations|analogy' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` found the four retained notes and several implementation-specific reflection systems.
- `rg -n '^([0-9]+\\.|[0-9]+\\.[0-9]+|Conclusion|References)|generality|autonom|cumulative|seed-program|causal|correlation|analogy|micro-ampliative|self-supervis|knowledge representation|reflection|AERA|constructiv'` over the snapshot identified the paper's explicit hypotheses, seed conditions, cumulative-modeling mechanism, reflection requirement, AERA examples, and conclusions.

**Link following:**
- Followed the bootstrap note into the Bitter Lesson and fixed-decomposition neighborhood; the direct bootstrap note is the useful comparison, while the broader production-method notes add an extra debate not required to understand this source.
- Followed the reflection note into reflective-system, accumulation, and governance neighbors; `reflection-buys-addressability.md` best matches the paper's claim that fine-grained self-inspection permits selective knowledge revision while preserving Commonplace's sharper distinction between reflection and accumulation.

## Connections Found

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **compares-with**: the paper supplies a concrete seed-programming theory in which a small initial ontology, drives, and causal-relational models bootstrap knowledge that was not hand-specified, while the note states the scaling condition such a bootstrap must meet.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- **is-evidence-for**: the paper argues that fine-grained self-inspection and self-modeling let a learner selectively compare, revise, and reorganize existing knowledge, and reports AERA implementations as initial evidence for that addressable reflective mechanism.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: the paper makes seed observables, transducers, representational granularity, and feature overlap explicit limits on what later learning can ground or distinguish, furnishing a cognitive-architecture case of an effective update space set by initial decomposition.
- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) -- **compares-with**: the paper treats generality as multidimensional and couples it to autonomy and practical action, whereas the note separates generality from reliability, speed, cost, and further-learning capacity; reading them together prevents a single-axis interpretation of learning progress.

## Bidirectional Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) <-> source -- **is-evidence-for**: after the ingest exists, the note could cite the paper's S0/S1 seed-to-acquired-model examples as a concrete, bounded instance of a bootstrap intended to outgrow its initial task knowledge.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) <-> source -- **is-evidence-for**: after the ingest exists, the note could cite the paper's CRM self-reference and surgical-update account as an implemented architecture claiming selective internal addressability.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Claw learning loops must improve action capacity, not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- rejected because the shared insistence on practical action is broad; the note's Claw-specific contextual-competence claim is not materially tested by AERA's cognitive-learning examples.
- [Factory-learning mechanisms should be compared on the same causal job](../../../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) -- rejected because both discuss experience-responsive retention, but the target's software-factory comparison dimensions and project-theory question are outside this paper's evaluated setting.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- rejected because the paper's causal-model theory is explanatory in ambition, but it does not directly test Commonplace's premise-variation criterion for explanatory-reach.

## Index Membership

- [Learning theory](../../../../tags/learning-theory-README.md) -- the eventual ingest would add a primary-source theory and implementation case for seed bootstrapping, cumulative learning, reflection, and autonomy.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the eventual ingest would contribute a cognitive-architecture account of reflective, bounded recursive self-improvement through fine-grained causal-relational models.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The paper makes several independent assertions across seed design, causal learning, reflection, knowledge representation, and autonomy. The ingest should preserve that structure rather than compressing it into one undifferentiated claim.
