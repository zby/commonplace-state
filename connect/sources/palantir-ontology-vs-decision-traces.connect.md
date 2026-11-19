---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/before-llms-palantir-was-competing-with-snowflake-and-databricks-po-2006384049485484145.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: Palantir Ontology vs Decision Traces

**Source:** [before-llms-palantir-was-competing-with-snowflake-and-databricks-po-2006384049485484145.md](../../../sources/before-llms-palantir-was-competing-with-snowflake-and-databricks-po-2006384049485484145.md)

## Discovery Trace

**Description listing scan:**
- Read source collection routing in `kb/sources/COLLECTION.md`: authored surface should be the ingest report, with `evidence`, `derived-from`, `rationale`, `defined-in`, `compares-with`, or sparse `see-also` links; no `kb/work/` or `kb/instructions/` links.
- Read destination heads: `kb/notes/agent-memory-README.md`, `kb/notes/artifact-analysis-README.md`, `kb/agent-memory-systems/README.md`, `kb/reference/README.md`, and `kb/agentic-systems/README.md`.
- `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' | rg -i 'trace|lineage|provenance|ontology|graph|relationship|decision|context|memory|activation|symbol|world model|trajectory'` -- kept the trace-derived, artifact-analysis, symbol-availability, Graphiti, and Databricks candidates; rejected broad reference docs and generic context-engineering notes as too general.

**Topic indexes:**
- `agent-memory-README.md` routes the source into memory as context engineering plus learning, not storage alone.
- `artifact-analysis-README.md` routes the source into lineage, representational form, and memory operational axes.
- `agent-memory-systems/README.md` routes graph and trace-derived systems into Graphiti and the trace-derived learning survey.
- `reference/README.md` and `agentic-systems/README.md` did not expose a tighter target than the notes and memory-system reviews.

**Body search:**
- `rg -n "trace-derived|decision trace|decision traces|decision receipt|receipts|provenance|lineage|trajectory|trajectories|commit surface|approvals|exception path|write-time" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- kept trace-derived extraction, raw accumulation, lineage, Graphiti, and Databricks memory scaling.
- `rg -n "ontology|world model|context graph|knowledge graph|typed relationships|named entities|structured.*substrate|language-shaped|lineariz|traverse|symbol availability|symbolic context" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- kept symbolic context engineering, Graphiti, Cortex as a rejected graph-system near miss, and Databricks as a source-level comparison.
- `rg -n "Palantir|Snowflake|Databricks|JayaGup10|2006384049485484145|context graph" kb/sources kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- found the target snapshot and an existing Databricks memory-scaling ingest; no prior Palantir-specific analysis.

**Link following:**
- Followed candidate note links from trace-derived extraction to the trace-derived related-systems survey, and from memory operational axes to raw accumulation, activation, and lineage notes.
- Followed Graphiti review links to its source ingest; kept Graphiti as the closest concrete temporal context-graph system, but used the code-grounded review as the stronger durable target.
- Followed Databricks memory-scaling ingest because the source explicitly names Databricks while making an enterprise memory/trace argument adjacent to the tweet.

## Connections Found

- [Use Trace-Derived Extraction As Meta-Learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) -- **evidence**: the source's workflow-first strategy says startups can learn entities and relationships bottom-up from decision traces, matching trace-derived extraction as an after-the-fact memory path whose value depends on signal quality and review.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) -- **evidence**: the source separates capture at decision surfaces, derivation into an ontology, activation by traversal/prompt assembly, and authority through policy/approval/outcome records.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **evidence**: the source argues that state alone lacks a legible "why"; decision receipts are ingress work that adds handles, provenance, relationships, and scope.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) -- **evidence**: the source's named entities, typed relationships, constraints, and "what interacts with what" are the symbols that make deterministic traversal and prompt assembly possible.
- [Lineage](../../../../notes/definitions/lineage.md) -- **defined-in**: the source's write-time provenance and decision receipts are a concrete lineage substrate for later invalidation, review, and derivation.
- [Trace-derived memory earns authority per operation, not at capture](../../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) -- **see-also**: the source names trace capture as the missing piece, while this seedling note explains why captured records must still be verified, distilled, and activated before they become trusted knowledge.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) -- **compares-with**: Graphiti is a concrete temporal context-graph system where episodes are transformed into entities, relationships, validity windows, and retrieval surfaces.
- [Memory Scaling for AI Agents](../../../../sources/databricks-memory-scaling-ai-agents.ingest.md) -- **compares-with**: the Databricks source complicates the tweet's product framing by presenting Databricks itself as pursuing trace and organizational-memory scaling, not only SQL throughput.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Use Trace-Derived Extraction As Meta-Learning](../../../notes/agent-memory-requirements/use-trace-derived-extraction.md) -> source -- **evidence**: if the tweet's framing becomes load-bearing, this note could cite it as a concise practitioner statement of trace-first ontology construction.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -> source -- **evidence**: the "state but not legible why" phrase is a sharp example of accumulation failing without provenance-bearing ingress.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context engineering](../../../../notes/definitions/context-engineering.md) -- rejected as too broad; the source is not defining routing/loading/scoping generally, but a trace-derived ontology path.
- [Cortex](../../../../agent-memory-systems/reviews/cortex.md) -- rejected as a secondary graph-system candidate; it has an authored ontology and RDF reasoning, but Graphiti is a tighter match for event/episode-derived temporal context graphs.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- rejected because its visualization warning about implied ontology is adjacent but not specific to decision traces.
- [Graphiti: Temporal Knowledge Graph for AI Agents](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) -- rejected as a primary durable target in favor of the code-grounded Graphiti review; still useful background.

## Index Membership

- [Agent memory](../../../../tags/agent-memory-README.md) -- future promotion, if any, should land in the trace-derived/agent-memory cluster rather than product-strategy coverage.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) -- useful as source context for graph-memory and trace-derived system comparisons, not as a new system review.

## Synthesis Opportunities

- A note titled "Trace-first ontologies are derived views, not starting schemas" could connect trace-derived extraction, lineage, raw accumulation, and symbolic context engineering. The claim: a workflow-first decision-trace system is still an ontology strategy, but the ontology is a derived artifact whose authority depends on capture quality, derivation policy, review, and activation.
- A smaller synthesis tension: platform-first ontologies buy coherence with high upfront integration cost; trace-first ontologies lower initial cost but shift difficulty to trace quality, conflict resolution, privacy/governance, and evaluation of inferred entities/relations.

## Maintenance Observations

None

## Flags

- The captured snapshot basename is too long to safely reuse for a validator-compliant `.ingest.md` companion. Use a shorter ingest-report slug with `source_snapshot` pointing to the captured file.
