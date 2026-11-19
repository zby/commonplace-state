---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/longmemeval-benchmarking-chat-assistants-long-term-memory.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

**Source:** [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](../../../../sources/.snapshots/longmemeval-benchmarking-chat-assistants-long-term-memory.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/tags-README.md`, `kb/notes/agent-memory-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The agent-memory head routed discovery toward end-to-end evaluation, activation, retrieval signals, compression, and lifecycle rather than storage alone.
- No source tags required a complete tag-README shortcut. Ran `rg -l '^tags:.*\bagent-memory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` to enumerate the tagged note surface.

**Full title and description scans:**

- Generated full H1 listings with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`.
- Ran whole-destination `rg '^description:' ... --glob '*.md'` scans. The strongest description-level candidates were the end-to-end knowledge-access note, the effects-based memory-evaluation requirement, the rule-ready-signal note, the insufficient-summary note, and the raw-accumulation note. `kb/reference/` exposed no Commonplace-specific design record that this external benchmark directly informed. `kb/agentic-systems/` exposed no whole-system analysis with a stronger connection than the memory-system reviews.

**Body search:**

- `rg -n -i '(LongMemEval|long-term interactive memory|multi-session reasoning|knowledge updates|fact-augmented key|time-aware query|retrieval.*reading|indexing.*retrieval)' ...` found direct LongMemEval mentions in the Virtual Context and Zikkaron reviews and in the Context as an Environment ingest.
- `rg -n -i '(oracle retrieval|retrieval alone|retrieval accuracy|downstream (task|answer|qa)|time-aware|temporal reasoning|summary.*information loss|information loss.*summary|memory recall|fact.*key|key expansion|value granularity|round granularity)' ...` found the matching evaluation, summarization, and selection claims and ruled out several merely topical memory-system records.
- Read the candidate artifacts rather than accepting keyword overlap. The paper separately measures retrieval and answer quality, reports reading failures under oracle retrieval, varies session/round/fact representations, and shows that time-range inference can help or harm retrieval depending on the selector model.

**Link following:**

- Followed the end-to-end knowledge-access note to context-operation reach and access-versus-transformation distinctions; retained the end-to-end note because LongMemEval directly instantiates its staged measurement claim, while the interface-reach note requires unrun rival operation interfaces.
- Followed the insufficient-summary note to addressability grain; retained insufficiency because the paper measures answer loss after compression, but rejected grain because it does not measure matched answer-bearing read volume.
- Followed the effects-based memory requirement through the agent-memory requirements map. LongMemEval supplies answer and retrieval effects but not behavioral uptake, governance, lineage, maintenance, or lifecycle effects.
- Followed direct LongMemEval mentions into Virtual Context, Zikkaron, and Context as an Environment. The first two need benchmark-grounding return links; Context as an Environment merits a two-way comparison because it reports a LongMemEval score under a different context-operation architecture.

## Connections Found

- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: LongMemEval separately reports retrieval metrics and end-to-end QA, then shows that reading strategy changes QA even under oracle retrieval, providing a bounded empirical instance of failures at distinct access-path stages.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: the benchmark measures recall and downstream answer quality rather than stored-memory existence, while its QA-only scope also makes the note's broader behavioral, lineage, maintenance, and lifecycle requirements visible as untested dimensions.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **is-evidence-for**: time-aware retrieval succeeds when GPT-4o infers a valid date range and fails when a weaker model invents ranges for questions without temporal cues, illustrating the difference between an encoded signal and inferred relevance.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **is-evidence-for**: replacing sessions or rounds with summaries or facts generally loses answer-relevant information, while fact decomposition helps the narrower multi-session subset; the result is a task-relative compression case rather than a universal anti-summary claim.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) — **is-evidence-for**: full histories contain the evidence yet long-context readers lose 30–60% relative to oracle evidence sessions, so retained chat volume alone does not ensure usable recall and reasoning in this benchmark regime.
- [Context as an Environment](../../../../sources/context-as-an-environment.ingest.md) — **compares-with**: both use LongMemEval to study long-horizon memory, but LongMemEval's own design experiments use a fixed indexing/retrieval/reading pipeline while Scroll exposes model-authored computation over retained history; compare benchmark lineage, operation interface, model, and retrieval budget before interpreting scores.
- [Graphiti: Temporal Knowledge Graph for AI Agents](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — **compares-with**: LongMemEval narrows retrieval through an inferred query-time range, while Graphiti attaches validity intervals to retained facts; they operationalize temporal memory on query and stored-state sides respectively, with different lineage and evaluation boundaries.

## Bidirectional Candidates

- [Context as an Environment](../../../../sources/context-as-an-environment.ingest.md) <-> source — **compares-with**: the later paper reports a LongMemEvalS result and should point back to the benchmark's own task construction, scoring, and baseline design so readers can distinguish benchmark definition from a cross-system score claim.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) <-> source — **evidenced-by** from the note side: LongMemEval is a clean empirical case because it exposes recall, answer generation, oracle retrieval, and reading-strategy results separately.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) <-> source — **evidenced-by** from the note side: the benchmark supports the retrieval-versus-answer split while also bounding that evidence to conversational QA rather than behavior-changing memory generally.

## Reverse-edge Candidates

- [Virtual Context](../../../../agent-memory-systems/reviews/virtual-context.md) → source — **evidenced-by**: its claim that LongMemEval-style results test end-to-end memory usefulness rather than per-artifact truth should link the benchmark specification and experimental decomposition, which support that boundary without validating Virtual Context's generated facts.
- [Zikkaron](../../../../agent-memory-systems/reviews/Zikkaron.md) → source — **evidenced-by**: its discussion of reported LongMemEval results should link the primary benchmark paper for task and metric meaning while preserving the review's warning that Zikkaron's advertised scores were not reproduced.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) → source — **evidenced-by**: the time-range extraction ablation supplies a concrete selector failure mode when the query lacks a usable temporal cue.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) → source — **evidenced-by**: the value-representation experiment is a bounded case where lossy compression does not reliably substitute for retained dialogue, with the multi-session exception preserving the claim's task-relative qualification.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — rejected because LongMemEval varies storage units and downstream QA, not the matched one-unit read volumes required by the note's claim.
- [A-MEM: Agentic Memory for LLM Agents](../../../../sources/a-mem-agentic-memory-for-llm-agents.ingest.md) — rejected as a direct connection because both are memory benchmark papers but use different systems and benchmarks; without a named shared design contrast, the relationship would be merely topical.
- [A context-operation interface bounds the projections its policy can realize](../../../../notes/context-operation-interface-bounds-context-policy.md) — rejected as direct evidence because LongMemEval varies choices inside one indexing/retrieval/reading frame and does not compare rival operation interfaces; the fixed-interface limitation may still belong in the ingest's limitations.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — rejected because the paper did not inform the shipped Commonplace plan and no authorised source-to-reference label expresses generic topical similarity.

## Index Membership

None. Source ingests are retrieved through `kb/sources/`; the agent-memory tag index is a note index, not a bibliography.

## Synthesis Opportunities

None. The higher-order claim that retrieval success does not establish end-to-end knowledge use already exists in the end-to-end knowledge-access note and the effects-based memory requirement.

## Maintenance Observations

None.

## Flags

- The paper has two distinct contributions—benchmark construction and memory-design experiments. The ingest should keep their evidence and limitations separate, but they remain one source observation and do not require separate artifacts.
