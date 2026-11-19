---
description: "Discovery for MerchantBench's persistent operation, delayed evidence, and observed procedural-memory limits"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/merchantbench-long-term-coherence.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: MerchantBench

**Source:** [MerchantBench](../../../../sources/.snapshots/merchantbench-long-term-coherence.md)

## Discovery Trace

- Read all 2,467 snapshot lines in five bounded consecutive reads, including simulator equations, framework settings, tool inventories, complete embedded prompts, and visibility tables. The study combines delayed order consequences with a fixed terminal objective; it reports activity decay, policy errors, and skill creation in the evaluated Hermes configuration.
- Read source/report contracts and README heads for notes, reference, agent-memory-systems, agentic-systems, and sources. Reused the batch's freshly generated complete title listings: `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. No source tags, hence no tag completeness shortcut.
- Description scan used `rg -l -i 'delayed feedback|false memor|memory.*effect|persistent polic|policy revision|coherence' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | xargs -r rg '^description:'`. The broad result was output-limited; shortlisted targets were then read in full rather than relying on clipped descriptions.
- Notes: fully read effects-based memory evaluation, governing behavior-changing writes, program theory under delayed feedback, active work state, and experimental contrasts. Kept effects, governance, and active-state comparisons. Rejected program-theory evidence because this simulator tests operating policies rather than open-ended program modification with a theory intervention.
- Reference: title/head scan plus `rg -n -i 'delayed feedback|coherence|memory.*effect|policy revision' kb/reference/ --glob '*.md'` found closure-prose and link-vocabulary uses with no concrete merchant-policy connection. No edge retained.
- Agent-memory-systems: fully read the Hermes review after identifying it by title and description; its version-pinned mechanism account complements paper-reported runs without establishing that the code revisions are identical.
- Agentic-systems: the same broad scan, followed by `rg -n -i 'policy revision|delayed feedback|memory.*effect' kb/notes/agent-memory-requirements/ kb/agentic-systems/ --glob '*.md'`, found mostly workflow/state persistence overlap. No separate main-system comparison added because the specific Hermes memory target is more useful.
- Sources: fully read PAST-Bench, then followed its links to effects-based evaluation and experimental contrasts. `rg -n -i 'Hermes|persistence|WITH/WITHOUT'` over PAST-Bench and the Hermes review confirmed the distinction between persistence intervention and an observational skill-use trace.
- Link following: effects-based evaluation → experimental contrasts separated creation, recorded use, and outcome attribution. Governance → behavioral authority identified why erroneous operating rules are consequential. PAST-Bench → effects evaluation supplied a concrete matched persistence control missing from MerchantBench.
- External: retained only the supplied arXiv URL; no external search. Instructions and work excluded. Candidate paths checked before writing. Notes' contract authorizes the reverse evidence candidate below.

## Connections Found

- [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: the paper records skill creation, patches, and later uses separately from business performance, and describes erroneous retained policies; it supplies a bounded case showing why artifact counts cannot establish beneficial learning.
- [Governing behavior-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — **is-evidence-for**: the reported false traffic-concentration belief persisted alongside destructive shelf contraction, illustrating the risk of promoting local inference into later operating policy. The trace is suggestive evidence, not a controlled attribution of loss to that memory.
- [Active work state](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — **compares-with**: misremembering the simulation endpoint led an agent to stop filling shelves with 83 days left, exposing current horizon and unfinished obligations as distinct from accumulated procedure memory.
- [Hermes Agent review](../../../../agent-memory-systems/reviews/hermes-agent.md) — **compares-with**: the paper adds observed skill creation, revision, reuse and divergent model behavior to a code-grounded description of the underlying memory/skill machinery. Compare deployment boundaries explicitly; do not import the review's commit identity into the benchmark.
- [PAST-Bench](../../../../sources/past-bench-personal-agents-pdf.ingest.md) — **compares-with**: PAST-Bench varies retained-state access across fresh sessions, while MerchantBench measures continuous operation with delayed outcomes and compares whole frameworks. Together they clarify which claims need persistence controls and which need long-horizon outcome measurement.
- [Original paper](https://arxiv.org/abs/2607.28956) — **derived-from**: primary external source for the eventual ingest.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → eventual tracked ingest — **evidenced-by**: an empirical case for keeping creation counts, use counts, policy quality and terminal outcomes distinct, with the lack of a memory-specific ablation stated beside the use.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Holding a program theory under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) — delayed attribution is shared, but merchant operation is not the note's program-modification test; no theory replacement or withholding contrast is run.
- [An experiment identifies only its actual contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — useful analytical discipline, but a separate footer edge would add little beyond the explicit framework-bundle caveat.

## Index Membership

None

## Synthesis Opportunities

None. Effects-based memory evaluation already owns the actionable distinction.

## Maintenance Observations

None

## Flags

- The 365-day horizon is simulated; the human participants completed their runs over five calendar days. Do not describe the experiment as year-long real deployment.
- Three runs per configuration and three human participants bound the stability and population claims. The best reported LLM mean is 27.3% of the human mean, not a general capability ratio.
- Hermes versus ReAct changes prompts, tools, code execution, memory/skills, and compression policy together. The aggregate difference does not identify the skill mechanism's benefit.
- Reported trace examples and skill-use sidecars do not establish content-specific causal uptake or reliable correction of erroneous policies.
- The simulator supplies its objective, action basis and environment dynamics; learning inside it does not establish revision of those choices.
- Author links in the eventual tracked ingest; immutable snapshot bytes stay untouched.
