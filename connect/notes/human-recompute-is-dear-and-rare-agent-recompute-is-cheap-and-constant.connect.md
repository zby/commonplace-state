---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: Opposed recompute factors do not decide documentation segmentation

**Source:** [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md)

## Discovery Trace

**Setup, scope, and authorization:**

- Verified the source before discovery with `sha256sum kb/notes/human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md`; it matched the closing SHA-256 `57efa8605dfcc76c0294cf958497e8baffbd55476d2ee4285af6262cdc379a0d`.
- Read the complete source, `kb/types/note.md`, `kb/cache/types/connect-report.md`, and `kb/notes/COLLECTION.md`. The source has frontmatter and asserts three linked decisions: whether a documentation cache has positive net value, whether crossed per-reconstruction saving and recurrence factors order two audiences, and whether specialization value repays a second maintained content surface.
- The notes collection authorizes local prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`, and excludes `work`. Its destination-filtered label sets are: notes — `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`, `evidenced-by`; types — `evidenced-by`; reference — `defined-in`, `evidenced-by`, `derived-from`, `abstracted-from`, `see-also`; agent-memory-systems, agentic-systems, and sources — `evidenced-by`, `derived-from`, `abstracted-from`, `see-also`; instructions — `operationalized-from`, `see-also`. `defined-in` was restricted to definition subtrees. No candidate was assigned a label outside these sets.
- External targets are authorized, but external is not a prospecting surface and no external target was supplied or already loaded, so external prospecting was skipped.
- Read `kb/instructions/COLLECTION.md` for the notes collection's first-class inverse-direction check. Instructions may link to notes only via the meta-reader `rests-on` label. Read `kb/agent-memory-systems/COLLECTION.md` and `kb/agent-memory-systems/types/agent-memory-system-review.md` before treating a code-grounded review as evidence.

**Curated heads, complete title surfaces, and description listings:**

- Read `kb/notes/README.md`, `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.
- Generated each authorized local destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and the same exact query over `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The scans returned 359, 10, 140, 173, 12, 289, and 47 title lines respectively.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` and the same whole-destination description listing over each of the other six authorized local destinations. Repository-local `rg` supplies no semantic scores, so no scores were available to record.
- Read the source's matching curated tag heads `kb/notes/document-system-README.md` and `kb/notes/context-engineering-README.md`. Neither declares `complete: true`, so neither by-tag fallback was skipped.
- Ran `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the exact `context-engineering` counterpart. Repeated both exact by-tag description queries over `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; only notes and reference produced tagged descriptions. No matching tag-README files existed in those other destinations.
- The source is already curated in both matching tag heads. No additional index membership survived.

**Notes prospecting and candidate evaluation:**

- Ran `rg -n -i 'recomput|cache value|reconstructions avoided|audience-specific|documentation segmentation' kb/notes/ --glob '*.md' --glob '!human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md'` and `rg -n -i 'stateless|first-time human|access cost|maintenance surface|specialization value|materializ' kb/notes/ --glob '*.md' --glob '!human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant.md'`.
- Ran the inbound-link query `rg -n 'human-recompute-is-dear-and-rare-agent-recompute-is-cheap-and-constant\.md' kb/ --glob '*.md' --glob '!reports/**'`. It found existing inbound edges from [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) and [Addressability grain, not compression ratio, decides whether a summary layer helps](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md), plus the two curated tag memberships. Those two inbound edges make the source-side routes useful independently; they are not reverse-edge candidates because the reverse edges already exist.
- Opened the full bodies of the two inbound notes, [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md), [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md), [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md), [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), and [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md).
- Kept five note candidates because they add distinct reader value: the broader dual-audience boundary, a one-source/multiple-access design response, a structural addressability test, the substitution precondition inside net reconstruction saving, and the model-specific three-path cache comparison. Rejected the checked-copy rule as too narrow for ordinary judgment-maintained prose and the local-materialization conjecture as an untested point-of-use intervention rather than a content-segmentation result.

**Other destination prospecting:**

- Types: ran `rg -n -i 'recomput|cache|audience|consumer|maintenance surface|materializ' kb/types/ --glob '*.md'` and opened [Tag README](../../../../types/tag-readme.md). Its validated-cache rule concerns safe derived marks, not whether audience-specialized documentation pays, so no type candidate survived.
- Reference: ran `rg -n -i 'recomput|cache economics|audience-specific|consumer-specific|dual-audience|documentation.*(human|agent)|materializ' kb/reference/ --glob '*.md'` and `rg -n -i 'generated (index|view)|build-time-only|maintenance (surface|burden)|source of truth|access cost' kb/reference/ --glob '*.md'`. [ADR 025](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) is already linked from the source as its bounded Commonplace witness; [Navigation](../../../../reference/navigation.md) repeats the same implemented access-path choice and was rejected as redundant.
- Agent-memory systems: ran `rg -n -i 'recomput|cache economics|audience-specific|dual-audience|human-facing|agent-facing|multi-consumer|multiple consumers' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'documentation.*(maintenance|agent|human)|stateless.*(session|agent)|materializ.*(view|source)|single source of truth|maintenance surface' kb/agent-memory-systems/ --glob '*.md'`, and `rg -n -i '^description:.*(documentation|human|consumer|cache|materializ|maintenance|stateless)' kb/agent-memory-systems/ --glob '*.md'`. Opened [LLM-WIKI-MCP](../../../../agent-memory-systems/reviews/LLM-WIKI-MCP.md), [napkin](../../../../agent-memory-systems/reviews/napkin.md), and [ATLAS](../../../../agent-memory-systems/reviews/atlas.md). Kept LLM-WIKI-MCP because its code-grounded review explicitly finds three consumption surfaces over one Markdown vault; rejected Napkin and ATLAS because they show shared human/agent storage or staged retrieval less directly and do not add evidence about a second maintained content surface.
- Agentic systems: ran `rg -n -i 'recomput|cache|audience|consumer|documentation|materializ|maintenance surface|stateless' kb/agentic-systems/ --glob '*.md'`. Eigenius cache hits concern execution memoization, and Swamp's retained workflows concern repeatable automation; neither bears on documentation-audience segmentation, so no candidate survived.
- Sources: ran `rg -n -i 'recomput|cache economics|audience-specific|dual-audience|human-facing|agent-facing|multi-consumer|multiple consumers' kb/sources/ --glob '*.md'`, `rg -n -i 'documentation.*(maintenance|agent|human)|stateless.*(session|agent)|materializ.*(view|source)|single source of truth|maintenance surface' kb/sources/ --glob '*.md'`, and `rg -n -i '^description:.*(human bottleneck|documentation|consumer|cache|recomput|materializ|maintenance|stateless)' kb/sources/ --glob '*.md'`. Opened [Ingest: Human Bottlenecks](../../../../sources/fernando-borretti-human-bottlenecks.ingest.md), [Ingest: How we built our knowledge base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md), [Ingest: Build Systems à la Carte](../../../../sources/build-systems-a-la-carte.ingest.md), and [Ingest: Harness Handbook](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md). None supplies the source's missing crossed-factor magnitudes or specialization economics; the Cerebras report's multi-consumer case is also weaker and less direct than the retained code-grounded LLM-WIKI-MCP review.
- Instructions: ran `rg -n -i 'recomput|cache|audience|consumer|materializ|maintenance cost|future value|stateless' kb/instructions/ --glob '*.md'`. The first-class inverse pass found no procedure whose ordering, defaults, or stopping conditions depend on this source. [Maintain Curated Indexes](../../../../instructions/maintain-curated-indexes.md) implements the already-linked ADR 025 decision rather than operationalizing this note's measurement or segmentation test.

**Link following and path checks:**

- Followed the LLM-recompute neighborhood to the checked-copy, insufficiency, addressability, and frontloading notes; followed addressability to access mode, pointer design, and documentation recovery; followed the dual-audience note to access mode and stateless routing; and followed LLM-WIKI-MCP's review neighborhood to its source-of-truth, context-budget, and other-consumer findings. These hops confirmed a tight chain rather than keyword-only overlap.
- Did not repropose the source's existing links to multiple-consumer interfaces, ADR 025, observer-relative information value, documentation recovery, or future-value promotion.
- Verified every path listed below exists relative to this report before completion.

## Connections Found

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **contrasts**: that note establishes the broad dual-audience tension and uses load-bearing methodology/execution tier separation as one response, while the source covers only recoverable cache content and shows that crossed reader-profile directions alone do not justify segmenting it.
- [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) — **extends**: it develops the source's distinction between content segmentation and access paths into a concrete response—consumer-specific sublinear materializations over one maintained source.
- [Addressability grain, not compression ratio, decides whether a summary layer helps](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) — **contrasts**: the source leaves crossed audience profiles unordered until magnitudes are measured, whereas addressability grain supplies a structural condition that can decide whether a selective layer helps in a particular case.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **extends**: it makes substitution at the required reliability an explicit precondition of the source's net saving per reconstruction; if consultation does not prevent or materially narrow source reconstruction, the document adds cost instead of saving it.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **extends**: it specializes the general cache ledger for model-facing derived values by distinguishing model-side recomputation, external on-demand derivation, and persisted checked materialization, then adds substitution and safety conditions.
- [LLM-WIKI-MCP](../../../../agent-memory-systems/reviews/LLM-WIKI-MCP.md) — **evidenced-by**: the code-grounded review finds human-facing shell commands, an in-process context engine, and MCP tools consuming one Markdown vault while SQLite, caches, and views remain rebuildable, corroborating the bounded feasibility of consumer-specific access without a second maintained content authority.

## Bidirectional Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) ↔ source — **contrasts**: a return route would bound that note's broad tier-separation response by distinguishing load-bearing audience-specific artifacts from recoverable cache content whose split still needs measured specialization value.
- [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) ↔ source — **extends**: a return route would add the economic stopping rule missing from its one-source/multiple-materialization heuristic—specialized content pays only when marginal audience fit exceeds incremental maintenance and drift burden.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — its enforce-or-omit rule applies where exact mechanical re-derivation is available; ordinary natural-language documentation in the source instead has judgment-based maintenance, so a direct edge could overstate the rule's scope.
- [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — it is an explicitly untested point-of-use conjecture and does not decide whether audience-specific maintained content earns its second surface.
- [Tag README](../../../../types/tag-readme.md) — validated completeness marks exemplify a safe machine-checked cache, but they do not sharpen the audience-segmentation decision and are already reached through the LLM-recompute neighborhood.
- [Navigation](../../../../reference/navigation.md) — it describes consumer-specific discovery paths, but the source already links ADR 025, the tighter decision record for the same bounded witness.
- [napkin](../../../../agent-memory-systems/reviews/napkin.md) — its progressive overview/search/read path supports model-efficient access, but LLM-WIKI-MCP more directly establishes multiple consumer surfaces over one canonical vault.
- [ATLAS](../../../../agent-memory-systems/reviews/atlas.md) — the same files serve a chat agent and a human web manager, but the review does not show distinct maintained content layers or their economics.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) — it avoids semantic recomputation by retaining symbolic workflows, but does not compare human and agent documentation or audience-specialization value.
- [Ingest: How we built our knowledge base](../../../../sources/how-we-built-our-knowledge-base-2077822555159945507.ingest.md) — Cerebras reports multiple retrieval consumers over one platform, but provides no cost, maintenance, or content-specialization comparison and is weaker evidence than the code-grounded kept system review.
- [Ingest: Build Systems à la Carte](../../../../sources/build-systems-a-la-carte.ingest.md) — it formalizes deterministic rebuild and memoization structure while explicitly omitting the check-cost economics and human comparator that drive this source.
- [Ingest: Harness Handbook](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md) — it reports agent-side localization and planner-token gains, but omits a human comparator and excludes construction, review, storage, and resynchronization cost from the savings result.
- [Maintain Curated Indexes](../../../../instructions/maintain-curated-indexes.md) — it operationalizes the existing ADR 025 index posture, not the source's cache-value measurement or audience-segmentation decision.

## Index Membership

None

## Synthesis Opportunities

- The source, [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md), [Addressability grain, not compression ratio, decides whether a summary layer helps](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md), [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md), and [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) imply a staged documentation-layer test: require positive cache value at equivalent reliability, require substitution or material narrowing, try finer-grained or sublinear access over one maintained source, and add audience-specialized content only when its marginal fit repays incremental maintenance and drift.

## Maintenance Observations

- The source H1 is now “Opposed recompute factors do not decide documentation segmentation,” while its filename and the authored link text in both curated tag heads still use “Human recompute is dear and rare; agent recompute is cheap and constant.” The paths resolve, but the visible navigation labels have drifted from the final title.

## Flags

- **Split candidate:** the note makes independently citable claims about crossed-factor ordering, audience-specialization economics, and low-traffic layers losing incidental drift-detection opportunities. Six kept candidates span the dual-audience, access/substitution, and model-cache/system-evidence neighborhoods, meeting the connect-report split-signal threshold even though the current argument is cohesive.
