---
description: "Connection discovery for MOOSEDev's typed project memory: answer operators, benchmark path observability, lifecycle comparisons, and capture truth limits."
type: types/connect-report.md
source: kb/sources/ontology-grounded-project-memory.ingest.md
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Ontology-Grounded Project Memory for Coding Agents

**Source:** [Ingest: Ontology-Grounded Project Memory for Coding Agents](../../../../sources/ontology-grounded-project-memory.ingest.md)

This is discovery against the accepted ingest and current repository documents, not an independent evaluation of MOOSEDev. Only this report is written. Candidate edges below require a future author's decision. The source already links the access/transformation and intended-path-health notes; those two outbound entries assess retention and labelling, not missing links.

## Discovery Trace

### Setup and search surface

Read the source in full, `kb/sources/COLLECTION.md`, `kb/types/ingest-report.md`, `kb/types/connect-report.md` and its schema, and `kb/reports/COLLECTION.md`. The source permits prospecting theory, reference, historical agent-memory systems, agentic systems, tags, and other sources. Its label table supplies no source-to-tags label. Instructions and workshops were excluded. External targets are allowed only from context already in hand.

Read each of the six destination `README.md` files. Generated a fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each destination. Large combined outputs were supplemented with a compact rendering of the same query's titles and a read of the initial theory-listing segment. No generated site listings or external search services were used. Brief matches count toward their parent document, not a separate link target.

For each destination, scanned description matches using:

```bash
rg '^description:' kb/<destination>/ --glob '*.md' \
  | rg -i 'ontolog|structur.*quer|quer.*structur|supersess|supersed|lifecycle|enumerat|fallback|access burden|capture.*decision|rationale|Mem0|Graphiti|temporal'
```

For each destination, ran these body queries (bounded result samples, not exhaustive body reads):

```bash
rg -n -i 'complete.set|exhaustive|enumeration|structural quer' kb/<destination>/ --glob '*.md' | head -35
rg -n -i 'supersession|misleading.*(commit|rationale)|raw.grep|OWL|SHACL' kb/<destination>/ --glob '*.md' | head -25
```

The unbounded `OWL` alternative also matched ordinary words such as knowledge. Refined it with word boundaries and bounded long-line previews:

```bash
rg -n -i '\b(SPARQL|SHACL|OWL)\b|supersession|raw.grep|commit.history' kb/<destination>/ \
  --glob '*.md' --max-columns 240 --max-columns-preview | head -18
```

No relevance scores were available. Candidate decisions use document claims and caveats, not keyword counts. All candidate paths were checked for existence before report creation.

### Theory

- **Indexes:** Read the collection landing and the agent-memory, context-engineering, and observability tag heads. The source carries no `tags`; these were topic-guided reads, not inherited tag membership. None of these heads declares `complete: true`; no completeness-based search shortcut was taken.
- **Description/title evaluation:** Access/transformation and intended-path health directly match the ingest's two settled contributions. Context-operation interface, trace authority, and decision-surface capture distinguish operator access, record truth, and capture position. The broad end-to-end architecture synthesis is relevant but less discriminating.
- **Body evaluation:** Enumeration searches found relevance-versus-enumerated-processing distinctions; the refined query separated actual graph/query machinery from incidental vocabulary. Supersession hits alone did not justify a broad lifecycle-note spray.
- **Full reads and one-hop traversal:** Read access/transformation and intended-path health from the source's links. Followed access/transformation to the end-to-end architecture synthesis, then its context-operation-interface link. Read the latter fully. From the agent-memory head, read decision-surface capture, then followed its trace-authority link and read that note fully.
- **Decision:** Keep four outbound targets, two of which are already linked. Recommend return paths from access/transformation and intended-path health. Recommend a separate inbound edge from decision-surface capture to qualify its capture-position argument. Do not infer that the benchmark proves ontology necessity, interface inexpressibility, or capture-error prevalence.
- **Direction authority:** Read `kb/theory/COLLECTION.md` fully. It permits `evidenced-by` to sources for observations that corroborate, qualify, or bound a claim; origin alone is not corroboration. Proposed inbound uses below explicitly qualify or illustrate rather than claim independent corroboration.

### Reference

- **Indexes and descriptions:** The landing points to design-rationale management, storage architecture, agent-memory coverage, and the gap plan. The description scan and supersession query found all four surfaces.
- **Full evaluation:** Read design-rationale management in full. Its distributed rationale surfaces and lack of enforced end-to-end continuity give a concrete comparison with MOOSEDev's typed decision/provenance/supersession records. Keep one sparse `see-also` edge. The source does not establish anything about Commonplace's current implementation or justify replacing its storage.
- **Rejected breadth:** Coverage and the gap plan are current Commonplace inventories, not the strongest reader destination for interpreting this paper. No reverse reference edge is proposed.

### Agent-memory systems

- **Indexes and descriptions:** Read the historical collection landing and its collection contract. Titles/descriptions surfaced Cortex, Graphiti, Mem0, and the Operational Ontology Framework. This collection is frozen; existing reviews are citable only at their recorded boundaries.
- **Body evaluation:** The refined query found Cortex's executable ontology and SPARQL supersedes inference. This is a mechanism match, not merely shared graph storage.
- **Full evaluation:** Read Cortex in full. Keep `compares-with` on executable relationship semantics and bounded retrieval versus structural graph views. Its implementation-grounded account and MOOSEDev's author-reported benchmark have different evidence bases.
- **Rejected breadth:** Graphiti's temporal fact invalidation is a plausible descriptive match, but MemoryLACE supplies the more discriminating lifecycle-and-answering comparison. The framework's artifact templates do not supply comparable runtime/query evidence. No reciprocal mutation candidate is proposed into this frozen collection.

### Agentic systems

- **Indexes and descriptions:** Read the landing and collection contract. The description scan surfaced the archived synchronous OSS Mem0 account and EvoOntology. The landing states the current comparison population is empty; archived records are not current comparison inputs.
- **Full evaluation:** Read the archived Mem0 account in full. Keep `compares-with` because it separates the inspected synchronous OSS retrieval and update routes from the paper's tested Mem0 configuration. It prevents treating a configuration-specific benchmark as a universal Mem0 capability statement.
- **One-hop evaluation:** The Mem0 account names an exact retained historical analysis. The compact account already states the needed scope, so no separate edge to that archived result is needed. EvoOntology's source ingest supplies a clearer paper-to-paper comparison than another archived system account.
- **Direction:** No reverse edge into a frozen historical result is proposed. No new analysis or system publication was commissioned.

### Tags

- **Indexes and search:** Read `kb/tags/README.md`, `kb/tags/COLLECTION.md`, and the agent-memory, context-engineering, and observability heads in full. Ran the same title, description, and body queries above. The heads routed discovery to capture, authority, operator-interface, and hidden-path claims.
- **Decision:** No formal source-to-tag edge: sources' outbound table authorizes no such label. No articulated head target needs an authorization extension merely to repeat topic navigation. Sources are outside participating tag collections, so adding this ingest to a generated member list would be incorrect. No index membership is proposed.

### Other sources

- **Indexes and descriptions:** Read the sources landing. The title and description scans surfaced MemoryLACE, EvoOntology, Graphiti, APEX-MEM, LongMemEval, the Mem0 ingest, and minimum viable ontology.
- **Full evaluation:** Read MemoryLACE and EvoOntology in full. Keep MemoryLACE on lifecycle-linked evidence, temporal interpretation, and its reported counting weakness versus MOOSEDev's complete-set operators. Keep EvoOntology on revisable access operations versus MOOSEDev's supplied typed capture/query pipeline; both bundle several mechanisms, so neither settles ontology necessity.
- **Rejected breadth:** Minimum viable ontology is a vocabulary-orientation proposal, not an evaluation of typed project-memory queries. The older Mem0 ingest is not preferred over the pinned OSS account because their documented add/update mechanisms differ by observation boundary. Graphiti/APEX-MEM and LongMemEval would add broader retrieval/temporal comparisons without sharpening the chosen two paper-to-paper axes.
- **Direction:** Source-to-source `compares-with` is authorized in both directions, but the new ingest does not yet earn a return link in every neighboring source. No source-side return edge is proposed merely for symmetry.

### External

The original arXiv URL is already present in the source metadata. No additional external target was supplied. External prospecting was skipped; no web browsing or MCP search was performed. No redundant provenance edge is proposed.

## Connections Found

- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **is-evidence-for**: MOOSEDev's comparable relevance coverage but different complete-set answers gives a bounded case for evaluating available operators and accepted answer semantics separately from finding records. Already linked in the ingest; retain its pipeline-level qualification, not an ontology-superiority reading.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) — **is-evidence-for**: the reported memory-server outage and raw-storage grep fallback makes checking the actual benchmark tool path necessary before attributing answer quality to the memory system. Already linked; the incident illustrates path ambiguity, not its prevalence.
- [A context-operation interface bounds the projections its policy can realize](../../../../theory/context-operation-interface-bounds-context-policy.md) — **compares-with**: compare top-k record selection with explicit filtering, enumeration, and traversal as different context-operation interfaces. The paper's achieved answers do not prove that every legal trace of the competing interface would fail.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **is-evidence-for**: the reported misleading commit message contaminated both a bootstrapped rationale and a gold answer. This bounds what historical provenance and structured capture license; neither independently checks the rationale's truth.
- [Cortex](../../../../agent-memory-systems/reviews/cortex.md) — **compares-with**: compare executable typed relationships and SPARQL supersession reasoning with MOOSEDev's typed project-memory query pipeline. Cortex shows an inspected mechanism; MOOSEDev supplies author-reported task results, not a shared benchmark. The target remains a frozen June 2026 account.
- [Mem0 synchronous OSS memory](../../../../agentic-systems/reviews-archive/mem0.md) — **compares-with**: compare the pinned OSS account's semantic-candidate retrieval and explicit revision APIs with the paper's benchmark configuration. The review is historical and does not identify the benchmark's exact Mem0 version, providers, or managed-platform behavior.
- [MemoryLACE](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md) — **compares-with**: compare active-entry selection plus historical/conflict expansion with MOOSEDev's explicit structural queries. MemoryLACE separates historical retrieval from temporal interpretation and reports poor counting; the comparison motivates matched answer-operator tests rather than a cross-paper performance ranking.
- [EvoOntology](../../../../sources/evoontology-self-evolving-ontology.ingest.md) — **compares-with**: compare an outcome-gated loop that revises semantic content, schema, and access tools with a supplied typed project-memory pipeline. Both make access operations consequential, but their bundled interventions do not isolate the benefit of formal ontology representation.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — **see-also**: compare MOOSEDev's explicit rationale/provenance/supersession records with Commonplace's distributed rationale surfaces and unenforced continuity. This is a concrete architecture analogue, not evidence that Commonplace has adopted or needs MOOSEDev's substrate.

## Bidirectional Candidates

Return directions use the theory collection's authorization, independently of the outbound labels above.

- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) → source — **evidenced-by**: add a bounded empirical illustration of why answer operators and semantics must be specified. Relevance parity alongside complete-set differences makes the distinction inspectable; capture/query confounding prevents attributing the effect to one representation. This is an illustrative, qualifying case, not a claim of independent corroboration.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) → source — **evidenced-by**: retain the server-outage/raw-grep incident as an author-reported example of why answer scores do not identify the tool path. It would add a concrete benchmark case beside the note's generic helper-fallback examples, without estimating incident frequency or asserting that every fallback weakens guarantees.

## Reverse-edge Candidates

- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../theory/structure-inference-needs-capture-at-the-decision-surface.md) → source — **evidenced-by**: qualify the note's capture boundary with the paired bootstrap observations: seven supersession chains were reportedly recovered from history, while a misleading message corrupted a rationale and the gold answer. These distinguish recovering candidate relationships from verifying their reasons. They belong near the note's necessary-not-sufficient boundary and continuum question; they neither refute the capture-position claim nor prove bootstrap reliability. Authorized by `kb/theory/COLLECTION.md` for a source that qualifies or bounds an assertion.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — a valid broader interpretation, but its access/transformation and interface checkpoints are already reached through the more discriminating targets. Do not add another general architecture edge merely because the source leaves capture and upkeep costs unresolved.
- [EvoOntology](../../../../sources/evoontology-self-evolving-ontology.ingest.md) as evidence that formal ontology is necessary — reject that inference, while keeping the narrower comparison above. Its intervention changes content and access tools together; MOOSEDev likewise lacks an otherwise-equivalent typed-record baseline without OWL.

## Index Membership

None

Sources are not participating members of generated tag indexes. The existing source landing explains the collection rather than enumerating ingests, and the historical system tables and current analysis comparison population must not absorb a paper ingest as a system-analysis row.

## Synthesis Opportunities

None

The operator-versus-representation distinction and the capture-versus-authority distinction already have notes. A matched-corpus experiment would test them more sharply; this pass does not identify a missing higher-order claim that warrants another synthesis artifact.

## Maintenance Observations

None

## Flags

- **Grounding before durable evidence use:** the accepted ingest retains no quotes. A future author making a source-dependent factual claim should retain the supporting extracts through the grounding procedure or explicitly require the pinned snapshot. This pass inspects the ingest analysis only; it has not rechecked the paper, benchmark repository, proprietary engine, transcripts, or scores.
- **Split-candidate signal:** counting note-typed system/reference targets as well as theory targets, this source connects to at least five notes across query architecture, observability, and capture/authority, and makes independent assertions. Keep those contributions separate if promoting theory: do not use the outage anecdote to establish graph superiority or the bootstrap error to estimate an error rate. The ingest can remain one source record; the signal concerns bundled downstream claims, not dividing the paper's source identity.
- **Scope comparison claims:** Mem0 observations differ by revision and product surface. Cortex and the selected Mem0 account are historical, not current comparison inputs. None of the suggested edges implies a new system analysis, matrix entry, or architecture adoption.
