---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Opposed recompute factors do not decide documentation segmentation

**Source:** [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md)

The source collection is `kb/notes/`. Its outbound contract authorises `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, `instructions`, and the reserved `external` destination. It excludes `kb/work/` and makes note-to-instruction edges exceptional and normally inverse.

## Discovery Trace

**Target and collection setup:**

- Verified the final source bytes before discovery and again before writing: SHA-256 `c2b8f577a87020bddf285bff1614802778f24fd967ff8aa05081a01bd034715d`.
- Read the complete connect-report type, the complete source, and the outbound-linking section of `kb/notes/COLLECTION.md`.
- Read `kb/notes/README.md`, [document-system-README](../../../../tags/document-system-README.md), and [context-engineering-README](../../../../tags/context-engineering-README.md). Both matching tag heads already list the source. Neither declares `complete: true`, so neither by-tag search was skipped.

**Notes destination:**

- Ran the complete 359-title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`.
- Ran by-tag description listings with `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `context-engineering` query.
- Ran `rg -n -i "(audience|consumer).*(split|segment|speciali[sz])|(split|segment|speciali[sz]).*(audience|consumer)" kb/notes/ --glob '*.md'`, `rg -n -i "(cache|materiali[sz](ation|ed)?).*(maintenance|drift|recompute|reconstruct)|(maintenance|drift|recompute|reconstruct).*(cache|materiali[sz](ation|ed)?)" kb/notes/ --glob '*.md'`, and `rg -n -i "(shared|single).*(source|authority|artifact).*(view|surface|consumer)|(view|surface).*(shared|single).*(source|authority|artifact)" kb/notes/ --glob '*.md'`.
- Kept the reliable-substitution, addressability, query-burden, semantic-work, change-topology, and dual-audience candidates below after full reads. Rejected local-materialisation, directory, and structural-entrenchment matches where an existing source edge already carries the useful surface or the split mechanism differs.

**Types destination:**

- Read `kb/types/README.md`; ran the complete 10-title surface, `rg '^description:' kb/types/ --glob '*.md'`, and `rg -n -i "audience|consumer|documentation|cache|recomput|reconstruct|maintenance|split|segment|materiali[sz]" kb/types/ --glob '*.md'`.
- `generated-index` and `tag-readme` instantiate checked derived surfaces, but the source already links ADR 025 and the LLM-cache note. Neither type adds independent evidence for the audience-specialisation decision.

**Reference destination:**

- Read the complete `kb/reference/README.md`; ran the complete 140-title surface and `rg '^description:' kb/reference/ --glob '*.md'`.
- Ran `rg -n -i "(human|agent|audience|consumer).*(documentation|docs|view|surface|site)|(documentation|docs|view|surface|site).*(human|agent|audience|consumer)" kb/reference/ --glob '*.md'`, plus focused generated-view and recomputation searches.
- `navigation.md` and `documentation-site.md` repeat the concrete human-site/agent-query choice already represented by the source's authored ADR 025 edge, so they were rejected as redundant direct links.

**Agent-memory-systems destination:**

- Read the complete `kb/agent-memory-systems/README.md`; ran the complete 173-title surface and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Ran `rg -n -i "(human|agent).*(view|surface|interface|document|wiki|markdown)|(view|surface|interface|document|wiki|markdown).*(human|agent)" kb/agent-memory-systems/ --glob '*.md'`, a generated-view/source-authority search, and a progressive-disclosure/recompute search.
- Followed [AI-Context-OS](../../../../agent-memory-systems/reviews/AI-Context-OS.md) and [napkin](../../../../agent-memory-systems/reviews/napkin.md) in full. AI-Context-OS passed because its generated tool-specific adapters explicitly remain subordinate to one canonical Markdown store; Napkin's staged retrieval is useful but less specific to audience-specialised views.

**Agentic-systems destination:**

- Read `kb/agentic-systems/README.md`; ran the complete 12-title surface, the whole description listing, and `rg -n -i "documentation|docs|human|agent-facing|view|surface|recomput|cache|maintenance" kb/agentic-systems/ --glob '*.md'`.
- Swamp's repeatable workflow codification and the other whole-system analyses do not exercise documentation-cache segmentation, so no candidate passed.

**Sources destination:**

- Read `kb/sources/README.md`; ran the complete 289-title surface and `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran `rg -n -i "README files for humans|AI context files|human.{0,80}agent.{0,80}(file|document|context)|agent.{0,80}human.{0,80}(file|document|context)" kb/sources/ --glob '*.md'`, a cache-tier/materialisation query, and a statelessness/repeated-reconstruction query.
- Read the strongest empirical hits in full. The OSS context-file study establishes that audience-specific files occur but does not compare their behavioral benefit or second maintenance surface. DeLM measures workload-dependent shared-summary value within a run, not maintained audience-specific documentation. Both were rejected as evidence for this source's decision rule.

**Instructions destination and reverse-edge pass:**

- Read `kb/instructions/README.md` and the complete outbound contract in `kb/instructions/COLLECTION.md`; ran the complete 47-title surface, the whole description listing, and `rg -n -i "audience|consumer|documentation|cache|recomput|reconstruct|maintenance cost|split|segment|materiali[sz]|source of truth|compiled view" kb/instructions/ --glob '*.md'`.
- Inspected `maintain-curated-indexes.md`, `write-instruction.md`, and the compression bundle. Their tag-splitting, procedure-promotion, and note-compression decisions use different triggers, so no inverse `rests-on` candidate passed.

**Link following and inbound check:**

- Followed the source's authored edges through [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md), [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md), [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md), [Serving multiple consumers does not require one retrieval interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md), and [ADR 025](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md). Their one-hop neighbourhoods exposed the missing sufficiency, grain, burden, semantic-work, change-topology, and audience-profile distinctions.
- `rg -n "opposed-recompute-factors-do-not-decide-documentation-segmentation|Opposed recompute factors do not decide documentation segmentation" kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` found the two tag-head entries and authored inbound links from `llm-recompute-cost-inverts-the-store-vs-recompute-default`, `addressability-grain-sets-a-matched-selective-read-floor`, and `an-insufficient-summary-precedes-the-source-rather-than-replacing`. Existing edges were not reported as candidates.
- No semantic-search scores were available. External prospecting was skipped: no user-supplied external target remained after preferring the tracked local source ingest, and connect does not search the open web.

## Connections Found

- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **extends**: supplies the stopping rule inside “equivalent reconstructions avoided”; a cache receives full credit only when it licenses a reliability-compliant stop, and partial credit only for fallback work it actually removes.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — **contrasts**: isolates one retrieval-cost component inside the source's total ledger, preventing a finer addressed unit from being mistaken for positive cache value or sufficient reason to segment content.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **grounds**: gives the system-relative decomposition needed to measure two cost classes the source explicitly includes in both source reconstruction and document consultation.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — **mechanism**: explains documentation caching as upstream amortisation of meaning-dependent work while preserving the source's warning that use-time savings were paid elsewhere rather than made free.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — **extends**: supplies a concrete maintenance-side condition for segmentation: a split can localise revision only when its units match sparse change and have an explicit, bounded impact closure; translation, routing, consistency, and coordination remain costs.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **contrasts**: establishes the genuine dual-audience pressure, while the source rejects the stronger inference that categorical statelessness or access-speed claims alone order cache value or warrant a second content layer.
- [AI-Context-OS](../../../../agent-memory-systems/reviews/AI-Context-OS.md) — **evidenced-by**: provides a code-grounded external witness for one canonical Markdown store serving tool-specific generated adapters and bounded context views without making each adapter an independent claim authority.

## Bidirectional Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → source — **contrasts**: readers of its fixed “remembers” versus “starts fresh every session” profile need the source's project-conditional recurrence model and separate specialisation-cost test before treating tier separation as warranted.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — a useful conjectural instance, but the source already links the broader per-consumer materialisation argument, and this target has no outcome evidence yet.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — shares horizon and switching-cost language, but governs structural permanence across changing question sets rather than audience-specific cache content.
- [Why directories despite their costs](../../../../notes/why-directories-despite-their-costs.md) — directory registration and routing taxes concern topology, not whether specialised audience content repays another maintained surface.
- [napkin](../../../../agent-memory-systems/reviews/napkin.md) — strongly demonstrates staged agent retrieval over a human-readable vault, but AI-Context-OS is the sharper witness for generated consumer-specific adapters remaining subordinate to one authority.
- [Ingest: Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) — observes human README versus agent context-file separation and maintenance stagnation, but measures neither behavioral specialisation value nor the marginal cost of a second layer.
- [Ingest: Decentralized Multi-Agent Systems with Shared Context](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) — measures workload-dependent benefits and upfront costs for within-run shared gists, but does not exercise durable audience-specific documentation or its maintenance horizon.
- [Maintain curated indexes](../../../../instructions/maintain-curated-indexes.md) — its split decision is driven by topical clusters and navigability thresholds, so a reverse `rests-on` edge would transfer the audience-specialisation mechanism by analogy rather than identity.
- [Navigation](../../../../reference/navigation.md) and [Documentation site](../../../../reference/documentation-site.md) — both restate the human-site versus agent-query materialisation already represented by the source's authored ADR 025 edge.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md), [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md), [Keep Lineage And Compiled Views From Drifting](../../../../notes/agent-memory-requirements/keep-compiled-views-aligned.md), [Serving multiple consumers does not require one retrieval interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md), [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md), [Promote Only When Future Value Exceeds Maintenance Cost](../../../../notes/agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md), and [ADR 025](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) — all are already authored source edges and were used only as neighbourhood anchors.

## Index Membership

None. The source is already curated in both matching tag heads, [document-system-README](../../../../tags/document-system-README.md) and [context-engineering-README](../../../../tags/context-engineering-README.md).

## Synthesis Opportunities

None. The source already carries the higher-order synthesis that cache economics and documentation segmentation are related but separately decided.

## Maintenance Observations

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) states a categorical persistence profile and presents tier separation as the primary response. The source treats recurrence as project-conditional and segmentation as an independent economic decision. The older note should be qualified or explicitly scoped when next maintained.

## Flags

- **Split candidate threshold met; split not presumed.** The source makes two independently citable assertions—crossed benefit factors do not order net cache value, and cache value does not decide segmentation—and this pass found more than five useful note connections across reliability/retrieval accounting, semantic-work placement, change topology, and audience design. A future writer should test whether separate notes improve composability while preserving the inferential bridge that blocks the move from audience cache ordering to audience-specific documentation.
