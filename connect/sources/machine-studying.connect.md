---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/machine-studying.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Machine Studying

**Source:** [Machine Studying](../../../sources/machine-studying.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md` and `kb/notes/tags-README.md`; the deploy-time-learning, context-engineering, failure-modes, evaluation, and agent-memory clusters were plausible. The source has no `tags`, so no matching tag README or by-tag `rg` pass was required.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The memory-systems comparison and source casebook supplied candidates; reference supplied no direct shipped-system analogue.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# '` and `rg '^description:'` over each authorised local destination: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- The title pass surfaced whole-system learning, retrieval-versus-action, frontloading, dynamic-cheatsheet, wiki, token-space-learning, and skill-distillation candidates. The reference candidates described Commonplace navigation or ingest mechanics rather than an evidential or comparative role for this source, so none were kept.

**Body search:**

- `rg -n -i 'expertise|machine studying|cheatsheet|search.{0,40}(knowledge|expert|behavio)|retrieval.{0,40}(action|behavio|expert)|model.{0,20}harness|inference.{0,20}(compute|budget)' kb/notes --glob '*.md'` -- kept the whole-system-learning, frontloading, continual-learning, and action-capacity notes; rejected generic occurrences of human expertise and unrelated inference budgets.
- `rg -n -i 'deploy-time learning|frontload|expertise|cheatsheet|corpus.{0,30}(study|learn)|search.{0,30}knowledge' kb/reference --glob '*.md'` -- found only operational adjacency, not a direct Commonplace-system comparison.
- `rg -n -i 'cheatsheet|machine studying|expertise|corpus.{0,40}(study|learn|wiki|skill)|retrieval.{0,40}(action|behavio|expert)|amortiz' kb/agent-memory-systems --glob '*.md'` -- kept Dynamic Cheatsheet and the implemented LLM Wiki; rejected systems whose only overlap was generic retrieval.
- `rg -n -i 'expertise|machine studying|cheatsheet|corpus.{0,40}(study|learn|knowledge)|retention|project knowledge|optimization loop' kb/agentic-systems --glob '*.md'` -- kept Compound Engineering as a task-conditioned project-learning comparison.
- `rg -n -i 'machine studying|cheatsheet|expertise|corpus.{0,40}(study|learn|wiki|skill)|retrieval.{0,40}(action|behavio|expert)|amortized context|token-space' kb/sources --glob '*.md'` -- kept the four closest source analyses and rejected broad continual-learning papers without a corpus-to-operative-artifact comparison.
- `rg -n -i 'weighted area|area under.{0,30}(compute|cost|budget)|performance.{0,40}inference.{0,20}(compute|budget)|quality.{0,20}cost curve|compute.{0,20}accuracy curve|fixed budget|inference budgets' kb/notes kb/agent-memory-systems kb/reference --glob '*.md'` -- found no existing treatment of the source's nested study-compute and inference-compute evaluation surface.

**Link following:**

- Followed the whole-system note through fixed decomposition, representational-form coevolution, and the readable-artifact loop. This confirmed that the source is evidence for the system boundary but not for the KB's preference for any one retained form.
- Followed the action-capacity note through contextual activation and memory-effect evaluation. StudyBench's retrieval-controlled literature task supplies a sharper reach-versus-selection case, while still not isolating an individual retained artifact's causal uptake.
- Followed frontloading through context efficiency and the execution-cost mechanism. The DSPy cheatsheet result is a local empirical instance: the note helps most at cheap budgets and loses its edge after forced long search.
- Followed the corpus-to-artifact source cluster through Knowledge-Centric Self-Improvement, Passive Skill Distillation, Continual Learning in Token Space, Karpathy's LLM Wiki, Dynamic Cheatsheet, and Compound Engineering. The useful discriminant is whether downstream tasks, rewards, or traces are available during preparation; Machine Studying withholds them by definition.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the source defines an agent as model plus harness, permits studying to alter either, and compares parametric and prompt-artifact interventions under one end-to-end outcome.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) -- **is-evidence-for**: the DSPy cheatsheet precomputes a repository map, improves the cheapest inference budgets, and loses its advantage when the unmodified agent is forced to spend enough search compute to rebuild that map.
- [Claw learning loops must improve action capacity, not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -- **is-evidence-for**: the literature task separates reaching relevant papers from selecting them for use, showing comparable retrieval with materially different downstream judgment.
- [Continual learning's open problem is governing behaviour change, not storing knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: corpus availability remains constant at test time, yet different preparation methods change cost and action quality; storage and access alone do not constitute the measured improvement.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpretation of StudyBench must separate learned mappings inside the supplied corpus, ReAct tools, note slot, model, and exam from the untested adequacy of those fixed representations and partitions.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: the reported variants identify their literal treatment bundles, not self-supervision, synthetic training, retrieval, or natural-language memory as general classes.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) -- **compares-with**: both treat external knowledge as the persistent improvement substrate, but KSI learns from task outcomes and cross-task forums while Machine Studying forbids downstream-task information during preparation.
- [Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) -- **compares-with**: passive skill distillation amortizes repeated reasoning from task trajectories, whereas Machine Studying asks for corpus-only preparation before the task distribution is known.
- [Continual Learning in Token Space](../../../../sources/continual-learning-in-token-space.ingest.md) -- **compares-with**: both place editable context beside weights as a learning surface; Machine Studying adds a benchmark and treats learned context as one candidate studying paradigm rather than the primary definition of continual learning.
- [LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: Karpathy supplies a concrete raw-to-wiki architecture for the source's amortized-context-management paradigm but no controlled evidence that it increases the source's compute-weighted expertise measure.
- [Dynamic Cheatsheet](../../../../agent-memory-systems/reviews/dynamic-cheatsheet.md) -- **compares-with**: both inject a compact natural-language cheatsheet, but Dynamic Cheatsheet curates from downstream attempts while StudyBench's preparation receives only the domain corpus.
- [llm-wiki (Pratiyush)](../../../../agent-memory-systems/reviews/Pratiyush--llm-wiki.md) -- **compares-with**: this implementation realizes precompiled file memory and bounded pull surfaces, providing a system-level comparison for the source's wiki-like studying proposal.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: Compound Engineering retains project knowledge and measured task-specific improvements, while Machine Studying isolates the harder preparation regime in which no downstream evaluation is yet known.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -> source -- **evidenced-by**: a future note edit could cite the source's explicit model-plus-harness definition and mixed studying surfaces as a bounded empirical case.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) -> source -- **evidenced-by**: the low-budget cheatsheet gain and forced-search catch-up are direct evidence for amortizing repeated discovery work.
- [Claw learning loops must improve action capacity, not just retrieval](../../../../notes/claw-learning-loops-must-improve-action-capacity-not-just-retrieval.md) -> source -- **evidenced-by**: retrieval-controlled paper selection measures a downstream competence gap after relevant items have already been reached.
- [Continual learning's open problem is governing behaviour change, not storing knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -> source -- **evidenced-by**: the benchmark keeps the corpus accessible and measures whether preparation changes later behavior and cost.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- rejected as a direct edge because the literature comparison varies closed models and inferred training recency, not the read-back or uptake of a specific retained memory artifact; the action-capacity note states the supported level more closely.
- [Charting the knowledge-access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) -- strong thematic alignment, but the source does not compare access architectures broadly enough to bear on this exploratory taxonomy beyond the narrower retrieval-versus-selection result already captured.
- [Navigation](../../../../reference/navigation.md) -- shares `grep`, indexes, and bounded reading, but is shipped-system documentation rather than a peer design or evidential target for this source.
- [getsentry/skills](../../../../agent-memory-systems/reviews/getsentry-skills.md) -- the corpus-to-skill overlap is real, but the closer Skill Synthesis source and Dynamic Cheatsheet system already cover the task-conditioned and prompt-artifact comparisons without adding a static marketplace detour.

## Index Membership

None.

## Synthesis Opportunities

- The source's nested evaluation suggests a missing methodology claim: corpus-to-artifact learning should be evaluated on a surface with at least three axes -- downstream quality, preparation cost, and per-task inference cost. [Frontloading](../../../../notes/frontloading-spares-execution-context.md) supplies the amortization mechanism, while [memory effect evaluation](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) supplies the outcome obligation. A fixed-budget score misses both expensive preparation and repeated inference savings.

## Maintenance Observations

None.

## Flags

- **Split candidate:** the source independently contributes a problem definition, a nested efficiency metric, a three-paradigm taxonomy, and several preliminary experiments across coding and literature tasks. Any durable promotion should separate the evaluation-surface claim from the intervention evidence rather than treating the article as one indivisible thesis.
- **Experiment boundary:** the studier's accessible signals include corpus text/code, repository reads, synthetic questions or self-sampled traces depending on the arm, and test-time task/search history. Its operations are LoRA weight updates or one prepended natural-language cheatsheet; the acting harness is fixed to ReAct plus `grep`, `glob`, and `read_file` (or BM25 in the literature task). The model family, corpus representation, tool/action basis, note slot, distiller, exam, grading, budget discount, and task partitions remain outside the effective update space.
