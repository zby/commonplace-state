---
description: "Connection discovery for MOOSEDev's ontology-grounded project memory: structural query workloads, lifecycle filtering, capture fidelity, and evaluation-path verification."
type: types/connect-report.md
source: "kb/sources/.snapshots/ontology-grounded-project-memory.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: Ontology-Grounded Project Memory for Coding Agents

**Source:** [Ontology-Grounded Project Memory for Coding Agents](../../../../sources/.snapshots/ontology-grounded-project-memory.md)

Discovery commissioned for an ingest, using `cp-skill-connect` and the `connect-report` type. Judgment producer: `openai/gpt-6.1-sol`. Repository-local discovery only; no agents, external search, or implementation execution.

The snapshot is immutable. All outbound recommendations below belong to the future name-paired ingest, `kb/sources/ontology-grounded-project-memory.ingest.md`, not to the snapshot. That ingest did not exist at discovery time. Reverse-edge recommendations likewise require the tracked ingest before authoring a durable source citation. The snapshot link above identifies this cache report's local input; it is not a recommended library citation.

The source describes small OWL ontologies with SHACL validation, typed project records, lifecycle and provenance edges, symbolic traversal and ranking, and narrow model interpretation/synthesis. Its reported advantage concerns completeness, absence, and supersession, not general relevance retrieval. Commit-history bootstrap and benchmark failure analysis supply separate capture and observability findings. These are author-reported results from a proprietary engine, not independent replication or evidence of long-term comprehension-debt reduction.

## Discovery Trace

### Shared setup and recall surfaces

- Read the complete snapshot, `kb/sources/COLLECTION.md`, `kb/types/snapshot.md`, `kb/types/connect-report.md` and its schema, and `kb/reports/COLLECTION.md`. The source contract authorizes prospecting theory, reference, agent-memory-systems, agentic-systems, tags, and other sources; it excludes work and instructions. The source has frontmatter but no tags, so discovery is not provisional and there is no source-tag-driven completeness shortcut.
- Read all six destination landings: `kb/theory/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/tags/README.md`, and `kb/sources/README.md`.
- Generated each complete title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, for each of the six destinations above. Recovered the truncated combined output before candidate selection. Brief matches would be attributed to their document, not the brief; none became a retained candidate here.
- Scanned descriptions for each destination using `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'ontolog|supersess|supersed|lifecycle|rationale|graph|retrieval|ground.truth|intended.path|primary.source|typed record|memory.*evaluat'`.
- Ran both body queries over each destination, with `rg -l -i '<query>' kb/<destination>/ --glob '*.md'`: `supersession|set.completeness|no recorded rationale|SHACL|MOOSEDev` and `silent.*fallback|primary.sources|capture.*discipline|decision.surface|top.k`. These are path-returning body searches, not semantic scores. No search scores are available.

### Theory

- Broad prospecting was warranted by the structural-query comparison, historical retention/current guidance distinction, commit-based extraction, and failed benchmark paths.
- Title/description scans selected access-versus-transformation, end-to-end access evaluation, raw accumulation, superseded choices, decision-surface capture, and intended-path health. Read each completely, plus the lifecycle requirement and automatic-injection hypothesis.
- Read `kb/theory/COLLECTION.md` for reverse-edge authorization. Its `evidenced-by` label permits source observations that qualify or bound a claim; an illustration is not automatically corroboration.
- Additional recall: `rg -l '^tags:.*\bagent-memory\b' kb/theory/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r '' | rg -i 'ingress|capture|lifecycle|supers|memory.*evaluat|govern'`, and the corresponding `evaluation` query filtered with `retrieval|contrast|oracle|judge`. The selective heads do not declare completeness, so no by-tag search was skipped on that basis.
- Followed intended-path health to diagnostic richness, and superseded choices/decision-surface capture to history checkability; read both linked notes completely. Diagnostic richness is an adjacent mechanism, but the paper does not ablate proposer diagnostic access, so no extra evidence edge was retained. History checkability helps interpret bootstrap limits but adds less than the more specific decision-surface connection.
- Kept access transformation, end-to-end evaluation, lifecycle filtering, ingress structure, capture limits, and intended-path health. Rejected a generic automatic-injection evidence claim: code-touch push and constraint gating are proposed next steps, not evaluated mechanisms.

### Reference

- Prospecting focused on Commonplace's rationale continuity, lifecycle, and retrieval architecture; the contract permits only `see-also` here.
- The description scan and body searches selected `design-rationale-management.md`, `agent-memory-coverage.md`, the gap plan, and lifecycle-related ADRs. Read design-rationale management completely; it explicitly identifies missing end-to-end continuity across distributed records.
- Retained that one document as the specific operational companion. Did not retain a broad storage-architecture or ADR spray: a proprietary graph's benchmark does not settle Commonplace's canonical substrate or mandate a lifecycle enum for ordinary notes.

### Agent-memory-systems

- The landing identifies this collection as frozen historical coverage. Prospecting therefore sought a named mechanism comparison, not an update to its survey or counts.
- Title/description and body results selected kgai, Graphiti, Mem0, Cortex, and the Operational Ontology Framework. Read kgai completely: its head-only context, retained supersession chain, explicit history lookup, and capture-only Stop hook give a particularly close comparison.
- Retained kgai on current-guidance versus preserved-history behavior, not as an outcome benchmark. Graphiti was followed through its tracked ingest, which contrasts nondeterministic reprocessing with kgai's deterministic rebuild. Kept that ingest as the temporal-model comparison rather than adding a second broad graph review edge.
- Mem0 remains an important baseline-configuration caveat, handled through its tracked ingest. Cortex and the ontology templates were not promoted from description-level hits: ontology vocabulary alone does not establish the paper's structural query capabilities or benchmark contrast.

### Agentic-systems

- Broad title scan plus the two body queries found archived EvoOntology and Mem0 reviews, retained historical analyses, and comparison tables. Read the EvoOntology archived review completely.
- EvoOntology distinguishes host-led revision of content/schema/tools from supplied-score admission and content-only recovery. That is a useful contrast with MOOSEDev's small supplied ontologies, but the tracked EvoOntology paper ingest gives the more direct source-to-source experimental comparison and was selected instead.
- No edge into this collection was retained. Archived Mem0 analyses and historical comparison tables cannot establish which Mem0 configuration the MOOSEDev benchmark ran; importing them as baseline evidence would confuse source boundaries. No search was expanded into the separate, unauthorized `agentic-system-analyses` collection.

### Tags

- Read `kb/tags/COLLECTION.md`, `kb/types/tag-readme.md`, and the agent-memory, evaluation, and type-system heads completely. Their selective picks helped route the theory pass; none declares `complete: true`.
- Agent-memory and evaluation are strong candidates for source-scoped search tags on the future ingest. Type-system is narrower: describing OWL classes is not itself a treatment of document contracts, so it is not recommended without an ingest argument about capture/validation structure.
- Sources are outside participating tag membership. No snapshot tagging, generated membership, or direct tag-head addition is proposed. The source collection's label table supplies no source-to-tags formal label; tags were used for routing rather than forced into outbound connections.

### Sources

- The landing, complete title scan, description filter, and both body queries selected MemoryLACE, Graphiti, Palantir/decision traces, Mem0, EvoOntology, and Three Dimensions That Matter To An Agent Memory Store. Read all six ingests completely.
- Followed the Palantir ingest's decision-surface link into theory and the Graphiti ingest's kgai comparison into the historical code-grounded review. MemoryLACE's counting failure and temporal-expansion ablations make it a stronger comparison than a generic graph-memory source.
- Retained those six on distinct named axes. The minimum-viable-ontology source was rejected from its description: its pedagogical naming-set problem is not this paper's executable relational query problem.

### External

- No external prospecting. The original arXiv URL is already supplied in the snapshot and supports `derived-from` for the future ingest. The paper's linked benchmark repository was not inspected; it is a verification follow-up, not independent support for the numerical claims.

## Connections Found

These are candidate edges from the future ingest. `is-evidence-for` below means a bounded reported case, not independent corroboration of the entire target argument.

- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **is-evidence-for**: the source separates relevance retrieval parity from large differences in enumeration, absence, and relationship traversal. This gives a concrete workload comparison for choosing explicit filtering/traversal operators instead of treating every question as nearest-neighbor retrieval. It does not isolate OWL reasoning from the rest of the graph/query pipeline.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: similar relevance coverage coexists with very different structural answer scores, and complete enumeration can cost substantially more tokens. The source supplies a bounded case against using relevance metrics as a proxy for answer quality; it does not measure complete construction, maintenance, and long-term behavioral costs.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: MOOSEDev makes lifecycle state operative by excluding superseded records from current guidance while retaining traversable supersession links. Its reversal trials bear on currency, not the target's separate redaction, relaxation, or full temporal-query requirements; Mem0 tied the graph on the tested reversal.
- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) — **is-evidence-for**: typed capture supplies categories, relationships, provenance, validation, and lifecycle state that structural queries consume. The paper explicitly reports capture discipline as a dependency and adoption cost. This is an implementation-shaped example of ingress work, not a controlled estimate of each ingress feature's contribution.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../theory/structure-inference-needs-capture-at-the-decision-surface.md) — **compares-with**: commit-by-commit bootstrap recovered seven supersession chains, but a misleading commit message contaminated both a rationale and a gold answer. Compare what preserved history can recover with the target's conditions on rationale-bearing capture; successful extraction does not establish faithful reasons or reconstruct an unrecorded why.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) — **is-evidence-for**: the reported memory-server outage caused agents to grep raw storage, initially producing an apparent relevance loss rather than an obvious tool-path failure. This is a specific reported example of why evaluations must verify the intended tool fired, not infer path health from an answer or score.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — **see-also**: compare distributed proposal/ADR/contract records without enforced end-to-end continuity against typed rationale, component, provenance, and supersession relations that support queries such as accepted decisions without recorded rationale. This identifies an inspectable capability to evaluate, not an already-approved Commonplace architecture change.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) — **compares-with**: both keep historical decisions and supersession chains while serving current heads separately. kgai adds an append-only log and deterministic projection/replay contract, but its capture hook does not enforce decision compliance; the MOOSEDev paper proposes edit gating as future work. Neither connection warrants treating graph records as enforced constraints on code.
- [MemoryLACE](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md) — **compares-with**: both retain lifecycle relationships and recover history selectively. MemoryLACE tests bounded expansion and temporal interpretation over conversational memories and reports poor counting; MOOSEDev reports strong complete-set and absence answers with explicit symbolic query access. This motivates comparing available operators and answer semantics, not ranking the two systems across unmatched corpora.
- [Graphiti](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — **compares-with**: distinguish current-guidance filtering and supersession links from validity-window and point-in-time temporal queries. The graph substrate alone establishes neither faithful extraction nor reproducible rebuilding; the Graphiti ingest explicitly keeps replay equivalence unresolved, and the MOOSEDev paper supplies no comparable rebuild experiment.
- [Palantir Ontology vs Decision Traces](../../../../sources/palantir-ontology-vs-decision-traces.ingest.md) — **compares-with**: MOOSEDev combines small domain ontologies declared upfront with history-extracted project instances. This makes schema origin and instance capture separate comparison axes rather than treating ontology-first and trace-first as mutually exclusive system categories. Gupta's source is a conceptual framing, not evaluated support for MOOSEDev's mechanism.
- [Mem0: Universal Memory Layer for AI Agents](../../../../sources/mem0-memory-layer.ingest.md) — **compares-with**: the reported baseline uses native extracted memories and top-k access, while the existing source describes reconciliation and optional graph storage. Preserve the tested configuration boundary: poor set completeness in this benchmark does not show that every Mem0 configuration, graph augmentation, or retrieval interface is incapable of enumeration.
- [EvoOntology: A Self-Evolving Ontology Layer for Data Agents](../../../../sources/evoontology-self-evolving-ontology.ingest.md) — **compares-with**: MOOSEDev reports structural query benefits with small supplied ontologies; EvoOntology evaluates revisions to content, schema, and access tools. They test different interventions. Using a typed graph does not itself establish ontology-learning or self-improvement, and EvoOntology's compound gains do not isolate ontology representation superiority.
- [Three Dimensions That Matter To An Agent Memory Store](../../../../sources/three-dimensions-agent-memory-store-2054246434506199529.ingest.md) — **compares-with**: the source's structural workloads give a concrete challenge to the essay's blanket anti-graph conclusion, while relevance parity and capture friction preserve its demand that complexity earn its cost. The contrast is workload-specific evidence versus a universal architectural recommendation, not proof that graphs always win.
- [Original paper](https://arxiv.org/abs/2608.13662v1) — **derived-from**: the future ingest's source analysis is worked out from this pinned paper version, not from independent inspection of the proprietary engine or the linked benchmark repository.

## Bidirectional Candidates

None. Useful incoming evidence uses are listed separately below; reciprocal edges should not be added merely to mirror source-side recommendations.

## Reverse-edge Candidates

All three are authorized by `kb/theory/COLLECTION.md` as `evidenced-by` to sources. A future writer must cite the tracked ingest once present, never the ignored snapshot, and retain adequate quotes or explicitly require the snapshot for semantic checking.

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) → future ingest — **evidenced-by**: add the memory-server-down/raw-grep incident as a reported illustration of the path-observation problem. It supplies a concrete evaluation failure; it is not prevalence evidence or an independent test designed to refute the note.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → future ingest — **evidenced-by**: relevance parity alongside different structural answer quality and enumeration token cost can bound what retrieval-only metrics license. Do not describe this as an evaluation of all the synthesis's maintenance and activation checkpoints.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md) → future ingest — **evidenced-by**: retained supersession chains plus exclusion from current guidance illustrate that preserving a choice event and removing an expired prescription from active context are compatible. This demonstrates one implementation-shaped possibility, not the target's full choice-versus-belief distinction or the truth of bootstrapped rationale.

## Off-authorisation Candidates

None. No formal source-to-tags edge was manufactured; candidate source-scoped search tags are considered below instead.

## Raw Text Candidates

None. All retained candidate artifacts have frontmatter. Untyped collection landings were used as navigation, not promoted to claim connections.

## Rejected Candidates

- [Agent statelessness means the context engine should inject context automatically](../../../../theory/agent-statelessness-means-the-context-engine-should-inject-context.md) — not retained as evidence: entity-exact code-touch push and constraint gating are the paper's next steps, not deployed and evaluated injection behavior.
- [History has one chance to become checkable](../../../../theory/history-has-one-chance-to-become-checkable.md) — useful one-hop premise for understanding capture limits, but an additional source-side edge would duplicate the more specific decision-surface comparison. Commit-history extraction does not recover facts absent from retained history.
- [Diagnostic richness constrains outer-loop learning quality](../../../../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md) — regradable transcripts and traces help audit an evaluation, but the paper does not test how diagnostic evidence changes an outer-loop proposer's later candidates. Do not substitute shared trace vocabulary for the target's mechanism.
- [EvoOntology archived review](../../../../agentic-systems/reviews-archive/evoontology.md) — read and evaluated, but not retained as a second edge for the same system. The paper ingest is the direct experimental comparison; the archived review has a separate code-inspection boundary and a broken migrated vocabulary link.
- [Minimum Viable Ontology / Domain Maps](../../../../sources/this-tweet-had-me-thinking-what-s-the-minimum-viable-ontology.ingest.md) — rejected at description resolution: a minimal vocabulary for newcomer orientation does not explain typed lifecycle queries or complete answer-set construction.

## Index Membership

None for direct membership or index edits. Sources are outside the tag collection's participating set. For the future ingest's explicit source-scoped search, consider `agent-memory` and `evaluation`: the source substantively treats persistent project-memory governance and benchmark design/failure analysis. These are suggestions for the ingest author, not snapshot tags or instructions to add the source to a tag head. The relevant heads were read; no membership has been authored.

## Synthesis Opportunities

A testable comparison design, rather than an immediate new note: use this paper, [MemoryLACE](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md), and [kgai](../../../../agent-memory-systems/reviews/kgai.md) to separate two capabilities often conflated as graph memory: selecting current guidance and producing complete, temporally scoped answer sets. Compare top-k retrieval, bounded history expansion, and explicit enumeration over the same records, with matched lifecycle state and answer semantics. This could sharpen the existing [access/transformation distinction](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md), rather than duplicating it. Current cross-system results do not isolate that causal claim.

## Maintenance Observations

- The fully read [archived EvoOntology review](../../../../agentic-systems/reviews-archive/evoontology.md) contains `../../notes/definitions/conjectural-learning.md`; the resolved path `kb/notes/definitions/conjectural-learning.md` does not exist. Record for a later explicit migration/maintenance pass; no repair was made here. This is one checked broken link, not an audit of the archive.

## Flags

- **Authored surface pending:** no matching tracked ingest existed at discovery time. The report can be consumed by the commissioning ingest, but no durable incoming citation should target the local snapshot. No proposed edges have been authored.
- **Split signal for downstream extraction, not the snapshot:** the source connects to more than five artifacts across memory/query design, historical capture/rationale, and evaluation observability, and makes multiple independent assertions. Keep the captured paper intact and the ingest unified; consider separate theory contributions only if each mechanism earns one. In particular, do not import benchmark hygiene as a premise of a graph-superiority claim.
- **Evidence boundary:** the benchmark changes representations, capture, and query capabilities together. The paper reports content-matched BM25 comparisons, but the loaded source does not establish an OWL-versus-otherwise-equivalent-relational-query ablation. Treat the results as task/configuration comparisons, not proof that formal ontology or graph storage is uniquely required.
- **Absence scope:** absence queries can establish missing recorded relations within an adequately captured corpus; they do not establish that a real-world rationale or constraint never existed.
- **Outcome and cost limits:** relevance parity is explicit; full enumeration may be much more expensive. The longer-term comprehension-debt claim remains a live-trial objective, and small-local-model benefits, automatic push, and edit gating remain proposed directions. No quoted metric here has been independently reproduced.
