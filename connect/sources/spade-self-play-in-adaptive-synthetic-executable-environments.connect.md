---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/spade-self-play-in-adaptive-synthetic-executable-environments.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: SPADE: Self-Play in Adaptive Synthetic Executable Environments

**Source:** [SPADE: Self-Play in Adaptive Synthetic Executable Environments](../../../sources/spade-self-play-in-adaptive-synthetic-executable-environments.md)

## Discovery Trace

**Collection rules and authored surface:**

- Read `kb/sources/COLLECTION.md`. The snapshot is immutable, so the matching `.ingest.md` is the prospective outbound author. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and sources; `kb/work/` and `kb/instructions/` are excluded.
- Read the snapshot in full enough to identify the method, evidence, fixed choices, and code-grounding questions. The source concerns a shared-weight designer/solver, executable generated environments, a corpus and environment-memory curriculum, hint-conditioned regret, and GRPO updates.

**Curated heads and complete listings:**

- Read `kb/notes/tags-README.md` and the `self-improving-systems`, `deploy-time-learning`, `agent-memory`, `evaluation`, `learning-theory`, `computational-model`, and `llm-reliability` tag READMEs. The validity-versus-learning-value, fixed-decomposition, experiment-contrast, and representational-form-coevolution clusters survived the articulation test.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. Voyager and Co-Harness survived; no reference or whole-agentic-system candidate did.
- Generated fresh complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'`. The scans covered 355/352 note titles/descriptions, 136/134 reference titles/descriptions, 173/171 agent-memory titles/descriptions, 12/10 agentic-system titles/descriptions, and 525/459 source titles/descriptions.

**Body searches:**

- `rg -n -i "fixed decomposition|effective update space|adaptive curriculum|environment design|self-play|hint[- ]based regret|corpus grounding|environment memory|co-evolv|learning potential" kb/notes kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- retained the fixed-decomposition note, the experiment-contrast note, Co-Harness, and Voyager; rejected broad self-play and generic trace-learning matches.
- Read `kb/notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md` after the environment-validation and hint-regret mechanism surfaced in the source. It survived because SPADE separates executable/semantic admissibility from expected learning value, while corpus grounding separately expands the upstream candidate supply.
- `rg -n -i "curriculum|environment memory|adaptive environment|self-play|training environment|generated environment|task generation|experience replay|regret" kb/agent-memory-systems --glob '*.md'` -- retained Voyager because its completed/failed-task memory also conditions curriculum choice; rejected SkillRL and generic trace-survey occurrences because their retained skill updates do not supply a close environment-design comparison.
- `rg -n -i "SPADE|adaptive environment|environment design|self-play|curriculum" kb/reference --glob '*.md'` and the same query over `kb/agentic-systems` -- found no articulated direct analogue.
- `rg -n -i "adaptive environment|environment design|generated environments|self-play|curriculum|hint.*regret|learning potential" kb/sources --glob '*.ingest.md'` -- retained Co-Harness as the strongest shared weights-plus-code comparison; no other source added a distinct reader need.

**Link following:**

- Followed the fixed-decomposition note to the proposal-selection, experiment-contrast, diagnostic-richness, and Co-Harness neighborhood. This separated SPADE's direct gradient updates from its reject-capable environment-validation substep and made the ablation-scope edge explicit.
- Followed Co-Harness to representational-form coevolution and the deployed-system learning boundary. SPADE is useful as a boundary case: executable programs affect training, but the released method retains shared weights and a small sampled environment memory rather than a separately versioned, regression-gated harness.
- Followed Voyager through its curriculum state, executable-skill promotion, and trace-learning survey links. The curriculum-memory axis was specific; the broader executable-memory and trace-learning matches were not.

## Connections Found

- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **is-evidence-for**: SPADE rejects candidates that fail parse, instantiate, reset, runtime-probe, or tool-use semantic checks before its hint-regret and difficulty reward decides whether a feasible environment lies near the learner's frontier; corpus grounding controls search breadth upstream rather than collapsing either gate into generation.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting SPADE requires separating its unusually broad learned surface (shared designer/solver weights and generated environment programs) from the still-fixed corpus sampler, six-skill partition, Gym interface, reward blend, validators, optimizer, memory schema, and benchmark selection.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: SPADE's no-memory and no-corpus arms bear on those removals, while the environment-designer adaptation controls jointly freeze or replace the designer and alter memory, so they do not isolate a designer-gradient effect.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: SPADE couples distributed-parametric updates to transient generated symbolic environments and a sampled code memory, providing a useful boundary against the note's stronger case where multiple forms remain independently retained and writable.
- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: both let generated code shape subsequent weight updates, but Co-Harness separately retains and regression-gates harness edits whereas SPADE regenerates executable curricula from an adapting shared model and a bounded example memory.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: both use retained curriculum state to condition later task generation; SPADE samples high-regret and too-easy/too-hard environment code, while Voyager records completed/failed tasks and QA context alongside a separately promoted executable skill library.

## Bidirectional Candidates

- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) <-> SPADE ingest -- **compares-with**: a return link would help readers distinguish independently retained harness repair from on-policy generation of transient executable environments during shared-weight training.

## Reverse-edge Candidates

- [Choosing what to learn requires both validity and learning-value gates](../../../../notes/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -> the matching SPADE ingest -- **evidenced-by**: SPADE extends the note's current self-training example to executable environment generation and makes candidate breadth, validity, and learning value separately inspectable.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -> the matching SPADE ingest -- **evidenced-by**: SPADE is a worked case where learning expands into environment generation but consequential interfaces, partitions, rewards, and selection procedures remain fixed above the update space.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -> the matching SPADE ingest -- **evidenced-by**: the paper's bundled designer-adaptation controls and narrower corpus/memory ablations give a concrete contrast-grain example.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as a primary classification: environment programs face validation and can be discarded, but SPADE's behavior-changing weight update is directly reward/gradient determined rather than a reject-capable proposal-selection loop.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected: the environment memory supplies selected examples, not retained failure traces, diffs, or drill-down evidence from which a separate outer-loop proposer diagnoses causes.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- rejected as redundant with the more exact fixed-decomposition and representational-form edges; SPADE still leaves the deployed evaluation harness and most training machinery fixed.
- [SkillRL](../../../../agent-memory-systems/reviews/SkillRL.md) -- rejected: shared GRPO and a dynamic skill bank are adjacent, but the skill artifacts and failure-driven updater answer a different memory question than SPADE's environment-example buffer.
- `kb/reference/` and `kb/agentic-systems/` candidates -- rejected after curated-head, title, description, and focused body scans because no target offered a direct Commonplace analogue or a whole-system comparison sharper than the retained notes and sources.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- SPADE is a current empirical case of a shared model adapting both task production and task solving while retaining a fixed outer training decomposition.
- [Learning theory](../../../../tags/learning-theory-README.md) -- the hint-conditioned regret signal, reward-shape comparison, and bundled adaptation controls are useful evidence for update-space and experiment-contrast analysis.

## Synthesis Opportunities

None. The generated-vs-retained symbolic-artifact distinction is useful here, but the existing representational-form note and Co-Harness ingest already supply the appropriate conceptual home.

## Maintenance Observations

None.

## Flags

- The source's claimed quantitative outcomes remain paper-only at the reviewed repository commit; this affects ingest evidence classification, not connection eligibility.
