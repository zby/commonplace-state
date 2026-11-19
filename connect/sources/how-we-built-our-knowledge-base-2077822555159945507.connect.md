---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/how-we-built-our-knowledge-base-2077822555159945507.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: How we built our knowledge base

**Source:** [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md)

## Discovery Trace

**Source read:** Read the snapshot frontmatter and body. The source is a Cerebras practitioner report about an internal knowledge base used by employees, automations, and agents. Core mechanisms: source-native ingestion from Slack, GitHub, Jira, docs, code, and custom databases; one Postgres embeddings/metadata table; Slack thread refetch and LLM distillation; burst embeddings for high-signal subthread messages; code indexing through CocoIndex; custom data-source scripts; planner/tool fan-out; RRF, reranking, and context expansion; MCP retrieval primitives; UI planner/executor/synthesizer; projects and default scoping.

**Collection rules:** Read `kb/sources/COLLECTION.md`. Snapshots are immutable; the authored surface is the ingest report. Allowed durable links from source analyses include `evidence` / `derived-from` / `rationale` to notes, `compares-with` to sources and agent-memory/agentic-system coverage, `defined-in` to definitions, and sparse `see-also`.

**Description listing scan:**
- `rg -n "^description:.*(retriev|context|search|memory|agent|source|distill|MCP|index|embedding|vector|tool|scope|project|knowledge|activation|storage|Slack|semantic)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- surfaced the agent-memory and context-engineering cluster, especially [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Import External Knowledge Into Internal Form](../../../../notes/agent-memory-requirements/import-external-knowledge.md), [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md), [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md), and [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md).
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The agent-memory-systems README explicitly treats systems without inspectable repos as lightweight coverage candidates, and names CocoIndex as an operational layer beneath a KB.

**Body search:**
- `rg -n "single source of truth|raw accumulation|ingress|stored knowledge|contextual activation|activation gap" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- kept raw-accumulation and activation notes; rejected broad failure-mode index hits.
- `rg -n "CocoIndex|incremental.*index|fresh vector|derived indexes|target state|live mode" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- kept [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md), because the source gives a production deployment of the reviewed indexing substrate. It also surfaced [files-not-database](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md), but the source uses Postgres as the central store and is not clean evidence for that note.
- `rg -n "reciprocal rank fusion|\bRRF\b|rerank|hybrid search|IDF|full-text|lexical search|vector search" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- surfaced many hybrid-retrieval systems including Engraph, GBrain, Graphiti, LACP, and Zikkaron. Kept this as synthesis context rather than one-to-one candidates because hybrid lexical/vector/RRF retrieval is now common in the review corpus.
- `rg -n "MCP.*retrieval|retrieval.*MCP|query_<source>|ContextProvider|source-scoped|tool fan|planner.*executor|fan-out|search_slack|search_code" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- kept [Context providers](../../../../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) as a source comparison, because both systems reduce exposed tool surface by source/task routing; rejected generic MCP-system hits without source-specific retrieval design.
- `rg -n "project-scoped|scoped search|default project|organization.*memory|enterprise|governance|access control|authorization|multi.*consumer|multiple consumers|source-scoped|data source" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- kept the multi-consumer and import-path notes; kept [Databricks memory scaling](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) as the closest enterprise-memory source comparison.

**Link following:**
- Followed [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md) from the agent-memory-systems README. The Cerebras source gives an observed user of CocoIndex's code-indexing path, but the edge is comparison/evidence about deployment, not a replacement for the code-grounded review.
- Followed [Databricks memory scaling](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) from source search. Both are enterprise practitioner reports where memory value depends on retrieval, distillation, governance, and scope; Cerebras is more architecture-specific, Databricks more evaluation/scaling framed.
- Followed [Context providers](../../../../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md). The source-provider pattern is adjacent to Cerebras' planner/tool fan-out and MCP retrieval primitives, but Cerebras uses explicit retrieval tools and source descriptors rather than wrapping each source behind a provider sub-agent.

## Connections Found

- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- **evidence**: Cerebras Knowledge is not one memory component; its reported value comes from storage, ingestion/distillation, retrieval/activation, authorization/audit, UI and MCP consumption, and scoped defaults working together.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **evidence**: the report explicitly rejects a single-platform source-of-truth migration and instead adds ingress work: connector metadata, Slack thread refetch, summaries, resolutions, code references, burst thresholds, recency, IDF, reranking, and project scope.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **evidence**: the architecture distinguishes collecting everything into a query-ready table from actually activating useful evidence via planning, per-source retrieval tools, fused ranking, reranking, context expansion, and project defaults.
- [Import External Knowledge Into Internal Form](../../../../notes/agent-memory-requirements/import-external-knowledge.md) -- **evidence**: the system imports Slack, code, docs, and custom team databases into one query interface without asking teams to move their source-of-work platforms.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) -- **evidence**: the same corpus is served to humans through a web UI, to agents through MCP primitives, to automations through a common table/interface, and to teams through project-scoped defaults.
- [CocoIndex](../../../../agent-memory-systems/reviews/cocoindex.md) -- **compares-with**: Cerebras gives production practitioner evidence for using CocoIndex as the incremental code-embedding substrate inside a broader enterprise knowledge system.
- [Databricks memory scaling](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) -- **compares-with**: both sources are enterprise agent-memory practitioner reports; Databricks emphasizes measured memory-scaling gains, while Cerebras exposes a concrete retrieval architecture and source-ingestion design.
- [Context providers](../../../../sources/context-providers-the-missing-layer-between-agents-and-tools.ingest.md) -- **compares-with**: both treat source boundaries as context-engineering boundaries, but Cerebras exposes low-level retrieval tools plus a planner, while ContextProvider proposes source-scoped sub-agent wrappers.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -> [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) -- **evidence**: add only if the note wants another production example spanning storage, activation, learning/ingress, governance, and action surfaces.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -> [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) -- **evidence**: the source's "meet data where it lives" design is a concrete example of raw collection being insufficient without shaping ingress artifacts and retrieval handles.
- [Import External Knowledge Into Internal Form](../../../../notes/agent-memory-requirements/import-external-knowledge.md) -> [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) -- **evidence**: external organizational systems are imported into a uniform internal query interface while preserving source-specific collection behavior.
- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) -> [How we built our knowledge base](../../../sources/how-we-built-our-knowledge-base-2077822555159945507.md) -- **evidence**: Cerebras explicitly serves humans, automations, MCP clients, and a full web UI over the same knowledge substrate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Navigation](../../../../reference/navigation.md) -- rejected as too local to Commonplace's file-navigation procedure; Cerebras' hybrid RAG retrieval is a useful contrast, but the edge would not help a reader acting on shipped Commonplace navigation rules.
- [Engraph](../../../../agent-memory-systems/reviews/engraph.md) -- rejected as a direct candidate because hybrid search, RRF, reranking, and MCP surfaces appear across many reviewed systems; use this source as broader synthesis evidence unless a future note specifically compares enterprise hybrid-retrieval architectures.
- [Files beat a database for agent-operated knowledge bases](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -- rejected because Cerebras centralizes embeddings and metadata in Postgres. It may be a counterpoint in a future storage-substrate comparison, but not corroborating evidence.

## Index Membership

- [Lightweight coverage](../../../../agent-memory-systems/lightweight/README.md) -- candidate: Cerebras Knowledge is an internal enterprise agent-memory/context-engineering system with no inspectable repo but unusually detailed architecture prose; it fits doc-grounded lightweight coverage better than a notes-only source.

## Synthesis Opportunities

Cerebras plus Databricks imply a higher-order enterprise-memory claim: enterprise memory succeeds when source-native ingestion, distillation, retrieval fusion, access governance, and scope defaults scale together. This is close to the Databricks ingest recommendation, but Cerebras adds enough architectural detail to support a more implementation-facing note or lightweight system review.

## Maintenance Observations

The snapshot tool captured large runs of zero-width or mojibake-like hidden characters from the linked article body. The visible content is usable and validation passes after adding `genre`, but future X/article snapshot cleanup may need a source-preserving normalization pass.

## Flags

- Split candidate: the source contains multiple independent architecture claims (enterprise ingress, Slack retrieval, code indexing, MCP/UI surfaces, projects/scoping). Prefer lightweight system coverage or a focused note over trying to promote every detail from the ingest report.
