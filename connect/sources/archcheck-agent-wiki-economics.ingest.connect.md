---
description: "Connection discovery for Archcheck's agent-wiki lookup experiment: substitution economics, cross-file aggregation, and freshness-review burden."
type: types/connect-report.md
source: kb/sources/archcheck-agent-wiki-economics.ingest.md
source_has_frontmatter: true
date: "2026-11-09"
depth: standard
---

# Connection Report: When does an agent wiki pay for itself?

**Source:** [Archcheck ingest](../../../../sources/archcheck-agent-wiki-economics.ingest.md)

Discovery only. No proposed edge below has been authored by this operation. The source already links the recompute and insufficient-summary notes; those two outbound recommendations assess existing connections rather than request duplicates. Instruction: `cp-skill-connect/SKILL.md`; judgment model: `openai/gpt-6.1-sol`. Inputs are the accepted ingest and current working-tree KB, including uncommitted content, not a frozen commit. No external lookup or delegation was used.

## Discovery Trace

**Authorization and scope:** Read the source and reports collection contracts and the global connect-report type. Sources permit prospecting theory, reference, historical agent-memory-systems, agentic-systems, tags, and other sources; work and instructions are excluded. The source has no tags. Its important distinctions are work displaced versus added, cross-file aggregation versus mirror pages, bundled intervention versus isolated cause, and change detection versus semantic correctness. Theory's outbound contract was additionally read for inbound candidates. No similarity scores were available.

**Curated heads:** Read all six destination `README.md` files. Followed the tags hub to `context-engineering-README.md` and `kb-maintenance-README.md`. The former routes to grain and the cache ledger; the latter routes to maintenance and documentation-sweep evidence. The maintenance head is `complete: true`; no by-tag maintenance search was run. No source-tag search was needed because the ingest is untagged. These heads were used for routing, not as destinations merely because they share a topic.

**Title and description scans:** Generated the complete fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the six destinations. Ran the scoped description query `rg -n '^(description:.*(recomput|summary|summari|fresh|wiki|maintenan|cross-file|routing|materializ|token cost)|#.*(cache|Cache))' kb/theory kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'`.

- **Theory:** Kept the two existing destinations, grain, and file-level staleness. The opposed-recompute note is more useful as an inbound evidence consumer than as another outbound explanation. The end-to-end evaluation note was read but rejected as less discriminating than the stopping-condition and cost-ledger notes.
- **Reference:** The scan and reference head identified freshness architecture. Read it in full. Its registered review-pair input model is not Archcheck's cited-source lint, so no direct system-architecture evidence claim was proposed.
- **Historical agent-memory-systems:** OpenWiki was the strongest named architectural comparator. Read its pinned review in full. The broader query `rg -l 'wiki.first|wiki-first|cross.file|source.*verif' kb/agent-memory-systems/reviews --glob '*.md'` returned many wiki systems; those keyword hits alone did not justify more links. Retained only the OpenWiki comparison, with its historical scope explicit.
- **Agentic-systems:** Read the collection head and inspected correction propagation after the description/title scan. Ran `rg -n 'freshness|stale|claim.level' kb/agentic-systems/comparisons/memory/correction-propagation.md` and `rg -n 'wiki|verification|cross.file' kb/agentic-systems/topics/memory.md kb/agentic-systems/topics/epistemic.md`. Read correction propagation in full; rejected it because its concrete subject is repair across retained representations and consumers, not the economics of map lookup or change-lint noise.
- **Tags:** Title/description scans and the two selected heads supplied routing. No formal source-to-tags label is authorized; no head needed a source-specific curated entry strongly enough to propose a contract extension.
- **Other sources:** Selected and read the OpenWiki self-correction ingest. It supplies a precise comparison on dependency granularity and reconciliation cost. Other wiki manifesto hits were weaker than this shared mechanism and were not retained.

**Focused body searches:**

- `rg -n 'cross-file|reliability.compliant|maintenance.*cost|false.positive|semantic correctness' kb/theory/{llm-recompute-cost-inverts-the-store-vs-recompute-default,an-insufficient-summary-precedes-the-source-rather-than-replacing,addressability-grain-sets-a-matched-selective-read-floor,link-graph-plus-timestamps-enables-make-like-staleness-detection,knowledge-access-architecture-must-be-evaluated-end-to-end}.md` distinguished the cache substitution condition, grain's one-unit scope, and the staleness note's explicit assumption that false-positive rereads are cheap.
- `rg -n 'source.change|stale|claim.level' kb/reference/freshness-architecture.md kb/sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md` distinguished input applicability from truth and file-granular dependencies from reported claim-evidence versioning.
- `rg -n 'aggregation|cross.file|map|wiki|maintenance|compression' kb/tags/context-engineering-README.md kb/tags/kb-maintenance-README.md` checked the curated routing language.
- `rg -n 'archcheck-agent-wiki-economics' kb/theory kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found no current inbound citations in these surfaces.

**Link following:** From the source, read recompute and insufficient-summary in full; followed their links one hop to grain and opposed-recompute and read both. Followed the context-engineering head to the same cluster, then evaluated the staleness note against the source's eight same-day flags. Followed the OpenWiki ingest to the historical OpenWiki review and freshness architecture. This narrowed the useful graph to cache economics plus freshness burden rather than a generic wiki cluster.

**External:** The original GitHub research URL already in the ingest is an authorized `derived-from` target and already carried by its `source` metadata. No additional external edge is needed. No open-web prospecting was performed.

## Connections Found

- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **is-evidence-for**: retain the existing connection as a bounded case of materialization losing when additive and winning on reported query costs when it displaces code-search work. It does not establish lifecycle value, equal future reliability, deterministic semantic checking, or superiority to on-demand symbolic derivation.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **is-evidence-for**: retain the existing connection because reported wiki-then-code traces expose fallback work left in the path. These traces illustrate the accounting boundary; they do not establish that every fallback was required for reliability or that the trusted map licensed a compliant stop for arbitrary tasks.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) — **compares-with**: contrast mirror pages larger than their small source files with the map's aggregation across files. This tells the reader why cross-file fan-out reduction must not be presented as a refutation of a matched one-unit floor or as proof that consolidation alone caused the gain.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — **is-evidence-for**: the eight same-day flags, including unrelated changes, qualify the note's assumption that false-positive review is cheap. File-level dependencies can surface review targets without checking claim correctness; the source does not quantify total review cost or test this KB's timestamp mechanism.
- [Building Self-Correcting Memory in OpenWiki](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) — **compares-with**: compare file-granularity change lint with reported claim-to-code evidence versions and page-local reconciliation. Both create recheck obligations rather than certify truth; neither ingest supplies independently reproduced lifecycle economics.
- [OpenWiki historical review](../../../../agent-memory-systems/reviews/openwiki.md) — **compares-with**: compare root agent-file entry pointers and Git-scoped documentation maintenance with Archcheck's directly routed cross-file map and change lint. Archcheck is a separate repository-local experiment, not an evaluation of the OpenWiki package or the review's pinned revision.

## Bidirectional Candidates

- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) → source — **evidenced-by**: add the bounded external losing/winning case to the decision-boundaries discussion. The evidence qualifies and illustrates the economics; it does not corroborate the note's deterministic-checking requirement or establish break-even.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) → source — **evidenced-by**: add reported wiki-plus-code traces as an illustration of additive consumption, preserving uncertainty about whether rereads were necessary and distinguishing orientation from modification.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) → source — **evidenced-by**: use the mirror-page versus cross-file-map contrast to illustrate the scope boundary between matched selective volume and aggregate reconstruction. The bundled experiment does not isolate grain as the cause.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) → source — **evidenced-by**: qualify the false-positive-cost paragraph with an external report of same-day review flags from unrelated changes. Treat this as a burden signal, not quantified refutation of the claim that review is cheap.

These are return-edge recommendations under theory's own collection rules. No reciprocal edge is proposed for the frozen historical OpenWiki review. The source-to-source comparison is authorized but does not independently require a return link.

## Reverse-edge Candidates

- [Opposed recompute factors do not decide documentation segmentation](../../../../theory/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) → source — **evidenced-by**: its common-horizon ledger can use Archcheck as a bounded example of what query-only savings leave unpriced: construction, maintenance, recurrence, and reliability equivalence. This qualifies the observation's economic reach; it is not evidence about human-agent audience segmentation or an isolated test of the crossed-factor claim.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Freshness architecture](../../../../reference/freshness-architecture.md) — the shared distinction between version applicability and truth is real, but an extra `see-also` adds little beyond the sharper lint/granularity comparisons. Archcheck does not test Commonplace's review-pair architecture.
- [Knowledge-access architecture must be evaluated end to end](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — compatible but too broad for another edge when substitution and the lifecycle ledger already provide the exact evaluation boundaries.
- [How corrections propagate through retained memory](../../../../agentic-systems/comparisons/memory/correction-propagation.md) — change detection is not demonstrated correction propagation; Archcheck does not observe repairs across retained derivatives or already-loaded consumers.

## Index Membership

None. The source is untagged and sources are outside tag-head participating collections. The topical heads were discovery aids, not automatic membership destinations.

## Synthesis Opportunities

None. The recompute, insufficiency, grain, and segmentation notes already express the combined accounting framework. This source adds a bounded case, not a missing general mechanism.

## Maintenance Observations

None.

## Flags

- The ingest's Quotes section is empty. Future source-dependent authoring must retain supporting exact quotes through the grounding workflow or explicitly require the pinned snapshot; this report does neither.
- Keep the bundled intervention and one-agent-per-cell design adjacent to any numerical result. Equal answers on the tested questions do not establish equal reliability across future use.
- No split recommendation: the connections concern two coupled areas, cache economics and freshness burden, rather than five notes across three independent topic areas.
