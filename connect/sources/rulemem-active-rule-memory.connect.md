---
description: "RuleMem connection candidates for rule-guided evidence retrieval, inference, and admission checks."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/rulemem-active-rule-memory.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: RuleMem

**Source:** [RuleMem](../../../../sources/.snapshots/rulemem-active-rule-memory.md)

## Discovery Trace

- Applied the already-read sources collection outbound contract, reports collection contract, and connect-report type. Read the full snapshot, recovering the initially truncated table/method interval through bounded reads of lines 470–1155. The source is immutable; the prospective ingest owns any authored links.
- Used the collection heads already read in this preparation session: notes, reference, agent-memory-systems, agentic-systems, sources, and the agent-memory curated head. The snapshot has no tags; no complete-tag omission applies.
- Generated fresh complete title surfaces using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each destination: 429 notes, 162 reference, 175 agent-memory, 20 agentic-system, and 402 source titles. Screened the generated titles with `rule|induc|retriev|abstrac|premise|ExpeL|Workflow Memory`; retained access/transformation, rule-selection, rule-maturity, ExpeL, and AWM candidates.
- Ran `rg '^description:.*(rule|induc|retrieval|reasoning|abstraction|oracle)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. Notes supplied the burden distinction, episode retention, and operation-specific verification. Agent-memory supplied ExpeL, workflow memory, and graph retrieval comparisons. Sources supplied the AWM paper and older Horn-clause theory refinement. Reference hits were mostly framework validation and instruction projection, not empirical rule induction.
- Ran `rg -n 'RPC|perplexity|Horn clause|rule induction'` across the same destinations. RPC mostly meant remote procedure calls; these lexical collisions were rejected. Older Horn-clause ingests concerned formal theory repair, a different mechanism from RuleMem's prompt-interpreted clauses.
- Ran `rg -n 'rule|Horn|premise|induc'` on `kb/reference/instruction-generation.md` and agentic-system reviews for Prime Agent, Eigenius, and Compound Engineering. Instruction-generation concerns installation/projection. Compound Engineering retains readable solutions, but neither supplies a closer rule-body retrieval or perplexity-filter comparison than ExpeL; no reference or agentic-system candidate retained.
- Read the access/transformation note, rule-selection note, episode-retention note, trace-memory authority note, ExpeL review, AWM source ingest, and representational-form definition. Followed the access note's link to the already-read end-to-end knowledge-access synthesis and the authority note's activation relation. Kept specific mechanism connections over generic memory overlap.
- External prospecting skipped. The supplied arXiv URL is already known and is the sole external connection.

## Connections Found

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **is-evidence-for**: RuleMem reports evidence recall separately from incorrect answers when supporting facts were retrieved, and uses distinct guided-recall and explicit-reasoning interventions. This is bounded empirical support for diagnosing access and inference separately, not a measurement of their full costs.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **compares-with**: RuleMem separates extracting facts, inducing rules, admission filtering, and consumption. Its RPC score is a likelihood-based proxy for rule support; the interview failure demonstrates that admitted rules can still override explicit contrary evidence. This comparison tests the difference between a filtering operation and warranted generalization.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **compares-with**: RuleMem retrieves rule heads by query similarity and uses bodies as inferred evidence cues. These are semantic relevance operations, not deterministic routing on a previously encoded case identifier; the shared word “rule” must not hide that distinction.
- [ExpeL](../../../../agent-memory-systems/reviews/expel.md) — **compares-with**: both retain natural-language rules abstracted from prior experience alongside concrete records. ExpeL broadly inserts rules and retrieves task examples; RuleMem selects rule heads, recalls body-supporting facts, and filters candidate rules through conditional likelihood. This makes rule selection and admission the useful comparison axes.
- [Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md) — **compares-with**: both replace instance-specific traces with variable-bearing reusable guidance; AWM primarily supports web action sequences while RuleMem supports evidence selection and conversational inference. Their benchmark outcomes and acceptance signals should remain separate.
- [Representational form](../../../../notes/definitions/representational-form.md) — **defined-in**: helps classify the natural-language Horn-clause template without mistaking its logical notation for a symbolic execution guarantee. RuleMem explicitly uses LLM filtering for variable binding and structured prompts for inference.
- [RuleMem](https://arxiv.org/abs/2609.03915) — **derived-from**: original external paper from which the prospective ingest is worked out.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) could cite the future name-paired ingest with **evidenced-by**, authorized by the notes collection. The supporting passage would be RuleMem's separate recall and post-retrieval reasoning diagnostics; inspect their evaluation limitations before adopting this edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md): RuleMem retains facts and consults dialogue during mining, but the paper does not demonstrate a durable rule-to-episode revision path or recovery comparison. Storage of both forms alone is insufficient support.
- [Knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md): relevant, but the narrower burden distinction captures the source's concrete diagnostic contribution with less generic overlap.
- [Instruction generation](../../../../reference/instruction-generation.md): projection and installation of shipped skills is not rule induction from conversational evidence.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Natural-language clauses, embedding selection, and LLM-based semantic unification do not establish sound formal deduction. The figure's employment/location-to-residence example also illustrates why a plausible rule requires an applicability boundary.
- The claimed successful case asks about Caroline but retrieves and answers about Melanie. Preserve this source inconsistency when assessing evidence quality; do not silently repair its entities.
- The captured paper refers to appendices for prompts, extended benchmarks, and configurations, but the retained document ends after references. Do not infer those absent details.
- RPC measures conditional likelihood changes, not entailment or causal validity. Aggregate ablation gains do not certify every admitted rule.
