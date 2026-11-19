---
description: "APEX-MEM connection discovery: hybrid query tools, temporal-history interpretation, and limits on storage-policy attribution."
type: types/connect-report.md
source: kb/sources/apex-mem.ingest.md
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: APEX-MEM — Temporal Graph Memory and Retrieval-Time Resolution

**Source:** [APEX-MEM ingest](../../../../sources/apex-mem.ingest.md)

Discovery only. No proposed edges have been authored. Produced with `cp-skill-connect/SKILL.md`, connect-report type, current repository state, and model `gpt-6.1-sol`. Judgments concern the ingest's retained analysis; the underlying paper was not independently checked in this pass.

## Discovery Trace

### Scope and authorization

Read the source collection contract and complete ingest before discovery. Sources authorize notes, reference, legacy agent-memory systems, agentic systems, tags, other sources, and already-known external targets; instructions and work are excluded. Notes permit `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` for definitions, and sparse `see-also`. System comparisons permit `compares-with`; source comparisons permit `compares-with`. Tags are named as a search destination but have no authorized source-to-tag relationship label. No broad source-link spray is proposed.

### Curated heads and title/description scans

- Read each destination's `README.md`: notes, reference, agent-memory-systems, agentic-systems, tags, sources. Read the agent-memory and context-engineering tag heads for their retention/activation and bounded-context boundaries. Neither declares `complete: true`. The ingest has `domains`, not `tags`, so there was no source-tag membership query or completeness-based skip.
- Generated the complete fresh title surface once for each of the six destinations using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered the truncated combined title output by ranged reads. Titles surfaced the access/transformation note, evidence-preservation requirement, experimental-contrast note, supersession/standing note, Graphiti, MemoryLACE, LifeFuse-Mem, and LongMemEval.
- Scanned scoped descriptions with `rg '^description:' kb/{notes,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md' | rg -i 'temporal|append.only|transformation burden|preserv.*evidence|fixed decomposition|lifecycle|truth.maintenance'`. A second filter, `'access burden|end.to.end|experimental contrast|fixed.*decomposition|superseded choices'`, recovered adjacent diagnostic claims. No semantic-search scores were available.

### Per-destination searches and evaluations

- **Notes:** `rg -n -i 'GraphSQL|temporal accuracy|append.only|eager|invalidation|temporary overwrit' kb/{notes,reference,agent-memory-systems,agentic-systems,sources}/ --glob '*.md' --glob '!reports/**' --glob '!reviews-archive/**' | head -100` was an initial bounded sample, not exhaustive body recall. Then ran `rg -n -i 'access burden|transformation burden|SQL|temporal'` over the access/transformation, end-to-end evaluation, and lifecycle notes. Fully read those notes, preservation, supersession/standing, fixed decomposition, experimental contrast, and the theory-builder and addressable-theory definitions. Kept the concrete tool case, retention/selection case, causal-attribution premise, and historical-versus-refuted-claim distinction. The definitions and fixed-decomposition note are already explicitly linked by the ingest; no duplicate new edge is recommended. End-to-end evaluation is stronger in the inbound direction.
- **Reference:** `rg -l -i 'temporal|append.only|GraphSQL|evidence retention' kb/reference/ --glob '*.md'` surfaced review-state history and grounding machinery. Read ADR 036 completely; rejected a link because review-baseline retention and historical conversational QA serve different consumers. The landing's memory-coverage and gap-plan entries describe shipped Commonplace state; this paper does not establish those states or close their governance gaps. No reference candidate survived.
- **Agent-memory-systems:** Title/description discovery surfaced the Graphiti review's explicit temporal invalidation. Followed the Graphiti ingest to the full code-grounded Graphiti review and read it. Kept a comparison about *when* resolution happens while old evidence survives, not graph-versus-file preference or a performance ranking. The collection landing says this survey is frozen; no return edge or roster addition is proposed.
- **Agentic-systems:** Read the curated landing and generated all titles, including archived accounts; scoped description filtering found no stronger current temporal-policy comparator. Ran `rg -l -i 'temporal graph|fact invalidation|retrieval.time resolution' kb/agentic-systems/reviews/ --glob '*.md'`: no matches. Current authored accounts concern other runtime mechanisms; no useful direct candidate survived. Did not substitute archived system scores for matched storage-policy evidence.
- **Tags:** Read the landing, both relevant heads, and `tags/COLLECTION.md`. Sources are outside the participating collections. Heads helped route to memory requirements and context theory, but source tag membership is not available and a generic tag link would add little beyond the specific claims selected below. No tag candidate survives the articulation test, so none is routed merely to fill Off-authorisation Candidates.
- **Sources:** Title/description scans identified MemoryLACE, LifeFuse-Mem, Graphiti, and LongMemEval. Ran `rg -n -i 'lifecycle|temporal|contradiction'` over their four ingest paths and read all four completely. Kept MemoryLACE for lifecycle expansion versus time interpretation, LifeFuse-Mem for acquisition-controlled temporary-exception testing, and LongMemEval for separating benchmark access stages and acquisition scope. The Graphiti ingest routes to its stronger code-grounded review; avoid two outbound links for the same comparator.
- **External:** No web prospecting. The source URL already in hand, `https://arxiv.org/abs/2604.14362`, is the ingest's existing provenance and supports `derived-from`; no new external edge is needed.

### One-hop link following and reverse checks

- Access/transformation links to end-to-end knowledge-access evaluation; fully read the latter and retained its return-to-source opportunity because the mixed tool-ablation result bounds what an aggregate retrieval gain establishes.
- Preservation links to session-history policy; the preservation note itself already states the capture/loading distinction needed here, so no extra session-history edge is necessary.
- Supersession/standing links to the lifecycle requirement; fully read the latter. Kept the narrower standing distinction rather than treating APEX-MEM as evidence for untested redaction and retirement operations.
- Graphiti ingest links to the implementation-grounded review; that review explicitly retains invalidated edges, defeating an append-only-versus-destructive-overwrite caricature.
- Read `notes/COLLECTION.md` for all proposed note-to-source directions. `evidenced-by` permits qualification and bounding as well as corroboration; the suggestions below are explicitly bounded cases, not tests corroborating the universal notes.
- Ran `rg -n 'APEX|apex-mem' kb/{notes,sources,reference,agent-memory-systems,agentic-systems,tags}/ --glob '*.md'`. Only the source ingest matched; none of the proposed return links is already present.

## Connections Found

The first two outbound connections already appear in the ingest. Retain them; the new authoring opportunity is the independently useful return path, not a duplicate source link.

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **is-evidence-for**: APEX-MEM provides a bounded mixed-tool case: GraphSQL adds joins and temporal calculations, while Search adds evidence access. Adding Search raises overall accuracy from 79.45% to 87.00% but lowers temporal accuracy from 82.29% to 79.17% within the fixed Haiku graph/extraction setup. The tools overlap; this illustrates, rather than independently isolates, the two burdens. Existing outbound connection.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **is-evidence-for**: retained event/fact history and utterance support can remain available while query-time reading selects context. This is a feasibility case for retention separate from loading, not evidence of complete raw-trace capture or append-only superiority. Existing outbound connection.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **rests-on**: the ingest's rejection of append-only causal attribution depends on distinguishing a tool-access intervention inside a fixed graph from the unrun storage-policy contrast. This gives readers the rule for interpreting Appendix F and the tool ablation consistently.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — **see-also**: clarifies the ingest's distinction between a preference that was true earlier and withdrawal of a false assertion. Retaining evidence of what was said need not preserve the retracted claim's current subject-matter authority. This is an interpretive companion, not an evaluation of APEX-MEM's untested truth-maintenance behavior.
- [MemoryLACE ingest](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md) — **compares-with**: both retain evidence for query-time reasoning, but MemoryLACE assigns activity and lifecycle relations during consolidation and separately ablates history expansion and temporal awareness. Comparing the intervention boundaries helps design a test of resolution timing without confusing retrieval with interpretation; cross-paper scores do not isolate storage policy.
- [LifeFuse-Mem ingest](../../../../sources/lifefuse-mem-lifecycle-aware-state-fusion.ingest.md) — **compares-with**: LifeFuse-Mem's acquisition-before-conflict measurement and temporary-exception protocol provide a concrete evaluation comparator for the ingest's proposed storage-policy experiment. Its neural state, supplied lifecycle labels, and privileged checkpoint readout are not equivalent to APEX-MEM's temporal graph.
- [LongMemEval ingest](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — **compares-with**: the benchmark account separates indexing, retrieval, and reading, while APEX-MEM's LongMemEval graph construction uses question-relevant documents. Following this comparison helps readers ask what acquisition/relevance filtering the reported answer score includes instead of treating it as evidence for a complete question-independent store.
- [Graphiti code-grounded review](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: Graphiti performs ingestion-time invalidation while retaining old fact edges and episode provenance; APEX-MEM emphasizes deferred resolution. This is a concrete comparator showing that early lifecycle decisions need not destroy history. It supplies no matched evidence that either timing policy is better.

## Bidirectional Candidates

- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) → source — **evidenced-by**: add the fixed-pipeline APEX-MEM tool-ablation case to illustrate and bound the distinction, retaining both the overall gain and temporal loss and the overlap between tool functions. The source already links outward to this note. A future source citation needs `(snapshot required)` until sufficient verbatim support is retained.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) → source — **evidenced-by**: add an implementation-design case for retained temporal assertions plus selective consumption. The return link gives the requirement's reader a concrete non-file memory design, without asserting exhaustive capture or causal superiority. The source already links outward to this note; use `(snapshot required)` for verification.

## Reverse-edge Candidates

- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → source — **evidenced-by**: the aggregate improvement with a temporal-category decline supplies a bounded case for task-relative outcome evaluation rather than a single overall retrieval/QA proxy. It does not test activation or upkeep. Prefer an example under the existing access/transformation argument, with `(snapshot required)`, not a claim of general corroboration.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [ADR 036: Review acceptance is current state, not append-only history](../../../../reference/adr/036-review-acceptance-is-current-state-not-append-only-history.md) — shared append-only terminology does not establish a shared workload. Review readers need the current acceptance baseline; conversational QA may require a past fact. Linking them directly would invite an unwarranted conflict between consumer-specific retention policies.
- [Graphiti ingest](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — useful discovery route, but the code-grounded review is the stronger endpoint for the retained invalidation mechanism. Avoid duplicate comparator links.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — existing ingest link is appropriate, but the missing restaurant/location relation does not establish an unrecoverable information omission. No new evidential return edge is justified by that failure alone.

## Index Membership

None

Sources are outside the tag contract's participating set. The legacy survey is frozen, and the source landing is a role-oriented guide rather than a source roster. No index addition is warranted.

## Synthesis Opportunities

None

The existing access/transformation, lifecycle, and supersession/standing notes already cover the relevant distinctions. The cross-source material motivates a controlled comparison, not a new general claim about the best resolution policy.

## Maintenance Observations

None

## Flags

- Source verification is pending for future durable uses: the ingest's Quotes section is empty. Candidate evidence additions should cite its tracked ingest with `(snapshot required)` or first retain minimum quotes through the grounding procedure. This report does not retain quotes or inspect the snapshot.
- Preserve the source's numerical caveats: 88.88% LOCOMO excludes adversarial questions in Table 1; token-cost and execution-count discrepancies prevent precise efficiency reuse. No connection licenses a benchmark or cost ranking.
- No split recommendation: this is one source's integrated ingest, and the retained connections concern temporal conversational memory and its evaluation. Do not promote its architecture, storage-policy hypothesis, and tool-ablation result as equally established independent claims.
