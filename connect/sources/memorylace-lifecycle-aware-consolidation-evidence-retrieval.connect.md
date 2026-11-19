---
description: "MemoryLACE connection candidates for lifecycle management, evidence retention, temporal graph comparison, and end-to-end memory evaluation"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/memorylace-lifecycle-aware-consolidation-evidence-retrieval.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: MemoryLACE

**Source:** [MemoryLACE](https://arxiv.org/abs/2609.03201), captured locally as the source named above. Candidate outbound edges belong in the paired ingest, never in the immutable snapshot.

## Discovery Trace

- Read the complete extracted paper, the sources collection contract, and the connect-report type. No source tags were supplied, so no tag-completeness mark applied.
- Read curated `README.md` heads for notes, reference, agent-memory-systems, agentic-systems, and sources. Generated the fresh title surface using `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`; the broad output was truncated, so followed with a filtered title pass for `supersed|contradict|memory|hindsight|simplemem|zep|provenance|retriev|evidence`.
- Across those five destinations, ran `rg '^description:' ... --glob '*.md' | rg -i 'supersed|contradict|temporal|hindsight|graphiti|a-mem|evidence.*histor|histor.*evidence'` and body search `rg -n -i 'supersession|linked.merge|lifecycle expansion|contradiction.*update' ... --glob '*.md'`. Broad body results were truncated; narrowed reads below determined acceptance rather than treating truncated search as exhaustive.
- Notes: read lifecycle management, evidence preservation, superseded choices, and end-to-end knowledge access. Followed the evidence-preservation link to session-history/default-context and the superseded-choices link to lifecycle requirements. Kept lifecycle and selective historical retrieval as direct mechanisms; kept the choices/beliefs distinction as a comparison boundary, not a claim of experimental confirmation.
- Reference: read agent-memory coverage. Its lifecycle gap is useful orientation, but the paper does not show any Commonplace implementation change; rejected an evidential edge to shipped-system claims.
- Agent-memory-systems: inspected Hindsight and Graphiti reviews, including their fact/observation and temporal-invalidation descriptions. Kept comparisons of architecture and history handling. Historical code reviews and this paper have distinct observation dates and versions; no equivalence between their exact evaluated implementations is assumed.
- Agentic-systems: README and title/body searches surfaced GBrain's confidence, temporal-validity, and supersession discussion. Rejected it as a weaker architecture comparison than Graphiti because MemoryLACE supplies no harness scheduling or governance evaluation.
- Sources: read the LongMemEval ingest. Kept the explicit comparison of temporal selection, representation, retrieval, and downstream evaluation. A-MEM appeared in the title/description search but adds less than the lifecycle and graph comparison targets for this source.
- External: the supplied arXiv URL is the primary-source candidate. No open-web connection prospecting was performed. No official implementation URL was identified in the paper text.

## Connections Found

- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: active-head selection, retained supersession chains, and temporal-awareness ablations supply a bounded conversational-memory case where lifecycle state actually changes retrieval and answer quality. They do not test redaction, relaxation, or the full requirement set.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **is-evidence-for**: default linked merge retains atomic texts and provenance while active-anchor retrieval and bounded expansion select historical evidence for the current question. The compact-merge ablation exposes a task-dependent cost of losing individual evidence.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — **compares-with**: MemoryLACE distinguishes historical states from current states and leaves unresolved conflicts active; the note clarifies why supersession is different from refutation and why historical retention does not restore current authority.
- [Knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: lifecycle expansion, temporal awareness, reranking, and evidence packing affect downstream QA differently, while failures on counting and recommendation show that better evidence access does not supply every required transformation.
- [Hindsight](../../../../agent-memory-systems/reviews/hindsight.md) — **compares-with**: compare bounded local lifecycle consolidation with fact/observation/reflective memory on historical evidence handling and maintenance cost. Paper runtime comparisons apply to its experimental setup, not automatically to the review's pinned code revision.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: both preserve changing facts and provenance, but Graphiti uses entity/fact edges and validity windows while MemoryLACE centers sparse lifecycle relations between atomic natural-language entries and grouped retrieval units.
- [LongMemEval](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — **compares-with**: LongMemEval separates indexing, temporal retrieval, and reading; MemoryLACE adds local evolution relations and evaluates on BEAM and StructMemEval. Compare failure mechanisms and measurement designs, not numerical scores across different benchmarks.
- [Original paper](https://arxiv.org/abs/2609.03201) — **derived-from**: primary evidence for the eventual ingest.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Lifecycle requirement](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) could cite the future paired ingest with **evidenced-by**, authorized by notes/COLLECTION.md, for a tested example of operational supersession and temporal retrieval. Ground the chosen claim before authoring the edge.
- [Evidence-preservation requirement](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) could cite the future paired ingest with **evidenced-by** for the linked-merge versus compact-merge comparison, preserving its task-dependent boundary. The eventual edge must target the ingest, never the snapshot or this report.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Agent memory coverage](../../../../reference/agent-memory-coverage.md): the lifecycle gap motivates interest but MemoryLACE is not evidence of Commonplace's shipped capabilities.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md): temporal fields overlap, but the paper does not evaluate the runtime-control and governance claims that distinguish this review.
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md): useful neighbor followed from the preservation requirement; the more specific preservation link avoids duplicating the same connection at a second level.

## Index Membership

None. This is an ingest input, not a completed external-system analysis suitable for the system-review roster.

## Synthesis Opportunities

The lifecycle requirement, evidence-preservation requirement, and MemoryLACE suggest testing retrieval as selection of connected evidence units rather than independent snippets. This is a candidate experiment, not a general claim that sparse graphs dominate richer representations.

## Maintenance Observations

The sources README still describes ordinary capture as plain WebFetch, while its collection contract and current snapshot skill specify Trafilatura and PDF routing. This is a documentation inconsistency only; no file was changed.

## Flags

- The paper supports conversational-memory and structured-QA comparisons; it does not establish general KB governance or theory-revision quality.
- No implementation was inspected or executed. Table text is retained in the default PDF extraction order; numerical reuse should check row/column interpretation carefully.
