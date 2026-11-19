---
description: "Pre-drafting discovery for APEX-MEM: temporal evidence retention, retrieval-time resolution, hybrid query tools, and limits on causal and cost claims."
type: types/connect-report.md
source: kb/sources/.snapshots/apex-mem.md
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: APEX-MEM

**Source:** [APEX-MEM: Agentic Semi-Structured Memory with Temporal Reasoning for Long-Term Conversational AI](../../../../sources/.snapshots/apex-mem.md)

This is a pre-drafting discovery report, not an authored connection set. The snapshot is immutable. Candidate outbound edges belong in the future `kb/sources/apex-mem.ingest.md`, which was absent during discovery. Reverse edges likewise await that tracked ingest; none should target the snapshot. The source has frontmatter, so this is not a provisional raw-text pass.

The paper describes event-anchored facts, entity/property canonicalization, append-only temporal history, and a ReAct reader combining schema inspection, entity lookup, read-only SQL, and hybrid search. The strongest reusable signals concern preserving historical evidence while selecting current context, and separating access from temporal/quantitative transformation. Reported benchmark gains do not separately identify the effect of append-only storage.

## Discovery Trace

**Setup and complete title surface**

- Read the invocation skill, `kb/types/connect-report.md`, the complete 2,588-line snapshot, `kb/sources/COLLECTION.md`, and `kb/reports/COLLECTION.md`. Read the report schema before writing.
- Generated a fresh complete title listing for each permitted local destination using `rg -N --no-heading -m1 '^# ' "kb/$d/" --glob '*.md'`, with `d` equal to `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. Recovered the truncated listing in successive reads.
- Read all six destination `README.md` files. Source authorization excludes work and instructions as destinations; neither was prospected. Operational skill reads are not destination prospecting.
- Ran description scans per destination with `rg '^description:' "kb/$d/" --glob '*.md' | rg -i 'memor|temporal|supersed|evidence|retriev|ontolog|schema|graph' | head -65`, then a narrower pass with `rg '^description:' "kb/$d/" --glob '*.md' | rg -i 'temporal|lifecycle|access burden|preserv.*evidence|end.to.end|query.time' | head -12`. These bounded description scans supplemented, rather than replaced, complete title recall. No semantic-search scores were available.
- Ran the cross-destination body query `rg -n -i 'append.only|query.time|retrieval.time|eager.update' kb/{notes,reference,agent-memory-systems,agentic-systems,tags,sources} --glob '*.md' | head -100`. Subsequent focused reads below decided candidates; the broad query was not treated as exhaustive body coverage.

**Notes**

- Titles/descriptions flagged the evidence-preservation requirement, lifecycle requirement, access/transformation distinction, end-to-end evaluation, superseded-choice distinction, and experimental-contrast note. Read each fully.
- Ran `rg -n 'Graphiti|temporal|provenance'` over the preservation, lifecycle, and superseded-choice notes, and `rg -n 'SQL|search|transformation' kb/notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md`.
- Followed preservation's link to the session-history note and read it fully: useful background, but a separate edge would duplicate the more specific preservation candidate. Followed access/transformation's link to end-to-end evaluation: kept because answer accuracy, query failures, and agent overhead matter beyond retrieval.
- Followed the superseded-choice note's lifecycle link: retained as a comparison, not a contradiction. Historical truth and refuted belief have different standing; timestamp order does not decide truth.
- Read `kb/notes/COLLECTION.md`'s outbound rules for reverse edges. Kept two source-grounding suggestions under `evidenced-by`, explicitly as bounded cases rather than corroboration of a universal claim.

**Reference**

- Read the reference landing and scanned titles/descriptions for memory coverage, storage, and lifecycle. Ran `rg -n -i 'temporal|lifecycle|preserve evidence' kb/reference/agent-memory-coverage.md kb/reference/commonplace-agent-memory-gap-plan.md`.
- Read agent-memory coverage fully. Rejected an outbound edge: a list of Commonplace gaps is not a direct design dependency of APEX-MEM, and a broad adjacent link adds little to this ingest. The gap plan remained a lower-priority search hit, not an adopted candidate. No reverse design-origin claim was inferred.

**Agent-memory systems**

- Read the historical survey landing, generated the full title surface, and scanned descriptions. Graphiti was the strongest direct comparator.
- Ran `rg -n -i 'temporal|append.only|invalidat' kb/agent-memory-systems/reviews/graphiti.md`; read the complete review. Its retained superseded edges distinguish history preservation from when invalidation is decided. Kept a named-axis comparison, not the paper's broad implication that other temporal graphs discard history.
- Ran `rg -n -i 'overwrite|update|contradict' kb/agent-memory-systems/reviews/mem0.md | head -8`. The inspected review describes an ADD-only inferred write path at its own pin. Used this only as a version-bound warning; did not treat it as a reproduction of the paper's Mem0 baseline.
- This collection is frozen historical evidence. No return-link maintenance or new survey membership is proposed.

**Agentic systems**

- Read the landing, generated complete titles including archives, and scanned `rg '^description:' kb/agentic-systems/reviews/ --glob '*.md'`.
- Ran `rg -n -i 'temporal|canonical|GraphSQL' kb/agentic-systems/reviews --glob '*.md' | head -35` and `rg -n -i 'schema|retriev|SQL' kb/agentic-systems/reviews/semantic-engine.md`.
- Read Semantic Engine fully. Rejected it: SQLite and embeddings overlap, but its corpus-staging search lacks the temporal fact-resolution and answer-agent mechanism at issue. Archived memory reviews did not provide a stronger candidate than the directly read Graphiti review and source ingests; no archive or retained-result edge was selected.

**Tags**

- Read the tags landing and collection contract, plus the agent-memory and context-engineering heads. Ran `rg -n -i 'temporal|lifecycle|evidence' kb/tags/agent-memory-README.md kb/tags/context-engineering-README.md`.
- The snapshot has no tags, so no source-tag expansion was applicable. Neither consulted head declares `complete: true`; no completeness-based search skip was claimed.
- The heads routed discovery to requirements and context-access theory, but sources are outside participating tag collections. No index membership is recommended. The sources contract names tags as a scan surface but supplies no sources→tags relationship label; no standalone tag-head edge had enough additional reader value to warrant an authorization extension.

**Sources**

- Read the sources landing and generated complete titles. Focused description/body scans located MemoryLACE, LifeFuse-Mem, LongMemEval, and the Graphiti ingest.
- Ran `rg -n 'temporal|Graphiti|acquisition|compact merge'` over those four ingests and read them fully. Kept MemoryLACE for the location of lifecycle decisions, LifeFuse-Mem for temporary-versus-lasting change and acquisition-controlled retention, and LongMemEval for benchmark interpretation and stage diagnostics.
- Followed the Graphiti ingest's link to the code-grounded review; selected the review instead of duplicating its older architectural summary. Followed MemoryLACE's links to preservation and lifecycle requirements, reinforcing the two most concrete theory destinations.

**External**

- Evaluated only the primary arXiv URL already supplied by the snapshot, under `derived-from`. Open-web prospecting was skipped. Bibliography entries were not expanded into additional external candidates.

## Connections Found

All local edges below are candidates for the future authored ingest, not for the snapshot.

- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) — **is-evidence-for**: APEX-MEM separates retained event/fact history and utterance evidence from query-selected context. This gives the requirement a concrete conversational-memory design case. It does not establish exhaustive capture fidelity or isolate the causal benefit of append-only storage.
- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) — **is-evidence-for**: event timestamps, validity intervals, and reader-side temporal queries make historical state operational rather than leaving supersession as an unused label. The case bears on temporal validity only; no redaction, retirement, or relaxation capability is established.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **is-evidence-for**: hybrid Search and EntityLookup locate relevant inputs, while GraphSQL supplies joins, date calculations, and aggregation. Table 3 and Appendix A report distinct category effects when tools change. This illustrates the diagnosis within one system, not a clean separation of tool functions or proof that SQL alone causes temporal gains.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: answer accuracy, extraction quality, SQL failure/recovery, and tool-call overhead expose different failure and cost boundaries around retrieval. This is a bounded QA case; upkeep and non-QA behavioral activation are not evaluated, and the cost tables need reconciliation before numerical reuse.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) — **compares-with**: compare historical validity with present epistemic standing. Alice's earlier restaurant preference can remain a true time-indexed report after her preference changes; that is not equivalent to retaining a false belief as current knowledge. This distinction limits transfer from conversational timelines to methodology revision.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **see-also**: use this specific methodological companion when assessing Appendix F. Cross-system temporal scores vary multiple mechanisms; the paper does not run a matched append-only-versus-eager-update intervention. Tool ablations answer narrower questions about tool availability.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: both retain temporal facts and provenance with hybrid access, but Graphiti's pinned implementation decides invalidation during ingestion while APEX-MEM emphasizes conflict resolution by the query agent. The useful axis is decision timing, not a false history-preserving/history-destroying dichotomy.
- [MemoryLACE](../../../../sources/memorylace-lifecycle-aware-consolidation-evidence-retrieval.ingest.md) — **compares-with**: both retain separate evidence and recover historical context. MemoryLACE assigns activity and lifecycle relations before retrieval, then expands linked evidence; APEX-MEM emphasizes append-only event storage and reader-side resolution. Compare write-time commitments, historical access, and temporal interpretation separately, without ranking systems across different benchmarks.
- [LifeFuse-Mem](../../../../sources/lifefuse-mem-lifecycle-aware-state-fusion.ingest.md) — **compares-with**: both address conflicting evolving memory, but protecting a durable value against a temporary exception differs from choosing a lasting replacement. LifeFuse-Mem's acquisition-controlled tests suggest a stronger evaluation of APEX-MEM's anti-overwrite story, without transferring neural-state mechanisms or privileged lifecycle labels to its graph.
- [LongMemEval](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) — **compares-with**: the benchmark ingest distinguishes indexing, retrieval, temporal selection, and reading. It helps interpret APEX-MEM's question-conditioned online construction and reported LongMemEval answer score without mistaking aggregate QA improvement for proof of one graph mechanism or autonomous memory-policy learning.
- [Original APEX-MEM paper](https://arxiv.org/abs/2604.14362) — **derived-from**: the future ingest analyzes this primary source already in hand; local snapshot bytes provide its reading copy, not a durable citation destination.

## Bidirectional Candidates

None. No return edge is useful merely to mirror the ingest's comparison list; the two theory-side source uses below are independently motivated.

## Reverse-edge Candidates

These are conditional future edits under the notes collection's `evidenced-by` authorization. The endpoint must be the tracked APEX-MEM ingest after it exists, never this cache report or the snapshot. No absent endpoint is emitted as a Markdown link.

- [Retire, Redact, Supersede, And Relax Memory](../../../../notes/agent-memory-requirements/retire-redact-supersede-relax.md) → future APEX-MEM ingest — **evidenced-by**: add a bounded second temporal-memory case in which query-time resolution, rather than ingestion-time invalidation, determines the answer. This qualifies the design space; it does not corroborate every lifecycle requirement or establish append-only superiority.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) → future APEX-MEM ingest — **evidenced-by**: the Search/GraphSQL ablation is a concrete mixed-access/query example. State the tested tool bundles and opposing overall/temporal effects, rather than claiming the experiment isolates abstract access and transformation burdens. Retain supporting quotes or require the pinned snapshot before durable use.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) — the relevant retention/loading distinction is already carried by the more specific preservation requirement. APEX-MEM's ReAct loop still appends tool history within a query, so a broader anti-transcript link could overstate what the paper changes.
- [Graphiti ingest](../../../../sources/graphiti-temporal-knowledge-graph.ingest.md) — useful discovery bridge, but its manual architecture summary adds less than the selected code-grounded review for the precise invalidation-timing comparison.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — Commonplace's gap inventory is not a sufficiently specific companion for this paper's ingest. No adoption or implemented analogue is inferred.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) — shared SQLite/vector-search ingredients do not give a useful temporal reasoning comparison; it is an exploration pipeline, not a conversational fact-resolution agent.

## Index Membership

None. Sources do not participate in tag membership. The frozen memory survey must not acquire a new entry through this pass. Any future system-analysis membership requires its own authorized workflow, outside this invocation.

## Synthesis Opportunities

None. Existing preservation, lifecycle, access/transformation, and end-to-end evaluation notes already host the main higher-order claims. The source adds comparison cases and test designs rather than requiring a new synthesis note.

## Maintenance Observations

None. Source-specific numerical inconsistencies and evidential limits are ingest drafting flags below, not library-maintenance tasks.

## Flags

- **Append-only is not independently ablated.** Appendix F explicitly offers indirect cross-system evidence. Do not turn the temporal accuracy gap into a causal estimate of retaining history or assert that all comparator systems overwrite it. The pinned Graphiti review retains invalidated edges; the separately pinned Mem0 review describes an ADD-only inferred write path. These local versions do not reconstruct the paper's baseline versions.
- **Temporal interpretation remains semantic.** Extracted validity dates, canonical identities, inferred properties, and reader selections can be wrong. Case 3's missing restaurant/location link shows that retained history does not repair missing relations. Separate genuine preference changes, temporary exceptions, same-scope conflicts, and retractions of false claims.
- **Tool gains are not monotonic by category.** Table 3 moves overall accuracy from 79.45% to 87.00% when Search is added, but temporal accuracy moves from 82.29% to 79.17%. State the metric and model; do not summarize this as every tool improving every capability.
- **Cost accounting is unresolved.** Table 9 lists APEX-MEM total consumption near 30,000 tokens/query while Table 10 totals 81,604. Their amortized graph-construction entry is 13,557 in both; it is 16.6% of the latter, not the former. Do not reuse a single efficiency ratio without resolving denominators and settings; competing-system figures include estimates.
- **Other internal reporting tensions need explicit qualification.** LOCOMO Table 1 distinguishes overall from overall without adversarial questions, while prose calls 88.88% overall. SealQA prose identifies O3 at 34.6% as the strongest baseline although Table 5 also lists GPT5 at 38.6%. Table 11's SQL execution/error totals are not all arithmetically consistent. Preserve table-specific scope rather than silently normalizing figures.
- **Online construction changes the evaluation boundary.** LongMemEval and SealQA construct graphs from question-relevant documents using a relevance threshold; LOCOMO constructs from all sessions. Do not describe every setting as one complete question-independent graph or an online learning policy optimized from feedback.
- **Split-candidate signal for downstream organization.** More than five theory connections span temporal memory, context/query architecture, and evaluation, and the source makes independent architecture, benchmark, and cost claims. Keep the source identity in one ingest, but separate those analytical strands and avoid one omnibus extracted theory note. Never split or edit the immutable snapshot in this pass.
