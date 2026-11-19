---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/tombros-sanderson-query-biased-summaries.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Advantages of Query Biased Summaries in Information Retrieval

**Source:** [Advantages of Query Biased Summaries in Information Retrieval](../../../../sources/.snapshots/tombros-sanderson-query-biased-summaries.md)

## Discovery Trace

**Curated heads:**

- Read [top-level note navigation](../../../../tags/README.md), [links](../../../../tags/links-README.md), [document system](../../../../tags/document-system-README.md), [context engineering](../../../../tags/context-engineering-README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), and [agentic systems](../../../../agentic-systems/README.md). The links head exposed the direct navigation/pointer cluster; the document-system and context-engineering heads exposed grain and sufficiency candidates. The other heads supplied no source-specific target.

**Full title listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`. The note surface flagged [pointer design tradeoffs](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md), [link-following and search](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [an insufficient summary precedes the source](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md), [addressability grain](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md), and [types give agents structural hints](../../../../notes/types-give-agents-structural-hints-before-opening-documents.md). The sources surface flagged [Teevan et al.](../../../../sources/teevan-perfect-search-engine-orienteering.ingest.md) and [Pirolli](../../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md). No reference or external-system title described this paper's experimental contrast closely enough to retain.

**Description listing scan:**

- `rg -n "^(title|description):.*(summary|surrogate|pointer|query|search|relevance|snippet)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' --glob '!**/dir-index.md' --glob '!**/*-README.md'` reinforced the pointer, navigation, sufficiency, and type-metadata candidates. System-review descriptions were rejected because their implementation inventories do not make claims about this controlled human relevance-judgment contrast.

**Body search:**

- `rg -n "query[- ]biased|query[- ]specific|document surrogate|static (summary|pointer)|relevance judg|full text" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!kb/sources/.snapshots/**'` found no prior Tombros and Sanderson capture or citation. It located the query-specific branch of the pointer taxonomy and several generic relevance-judgment uses; only the former was a direct evidential target.
- `rg -n "pointer-design-tradeoffs|link-following-and-search|insufficient-summary|types-give-agents|design-for-the-first-time-human|addressability-grain" kb/notes/tags-README.md kb/notes/links-README.md kb/notes/document-system-README.md kb/notes/context-engineering-README.md kb/reference/README.md kb/agent-memory-systems/README.md kb/agentic-systems/README.md` confirmed the candidates' curated neighborhoods and showed that the grain and sufficiency notes belong to a different comparison ledger.

**Link following:**

- Followed [pointer design tradeoffs](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) to [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [link-following and search](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), and [an insufficient summary precedes the source](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md). The experiment directly varies a query-specific versus fixed surrogate and measures a human relevance decision, making the first two strong. The sufficiency note fixes a required-reliability condition the experiment does not test, so it was rejected as evidence.
- Followed [addressability grain](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) to the same pointer and sufficiency cluster. Tombros and Sanderson measure human judgments, documents examined, and full-text opens; they do not hold a read-volume currency and matched answer-bearing unit fixed, so the grain connection is only topical.
- Compared the source with [Teevan et al.](../../../../sources/teevan-perfect-search-engine-orienteering.ingest.md). Teevan studies which paths people take; Tombros and Sanderson vary the surrogate presented at a direct-search result. Keeping those axes separate prevents a better direct-jump pointer from being mistaken for evidence that local navigation is unnecessary.

## Connections Found

- [pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) -- **is-evidence-for**: the experiment varies a query-biased, query-time surrogate against a fixed title-plus-leading-sentences surrogate and reports higher human relevance-judgment recall, precision, and speed plus fewer full-text opens. It bears directly on the query-specificity branch, without establishing the note's complete taxonomy, LLM costs, or availability and accuracy axes.
- [link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) -- **is-evidence-for**: in the paper's ranked-result setting, adding query-specific contextual clues improved human selection from a long-range search surface and sharply reduced full-document consultation. This supports the bounded claim that search-result pointers must carry decision-relevant context, while the target must own the transfer to LLM agents and its specific title/description prescription.
- [The Perfect Search Engine Is Not Enough](../../../../sources/teevan-perfect-search-engine-orienteering.ingest.md) -- **compares-with**: Teevan et al. observe local-step versus direct-jump search strategies, whereas Tombros and Sanderson experimentally change the surrogate shown after a direct search. The comparison separates route choice from pointer quality.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [an insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- rejected as evidence: the experiment reports fewer full-text opens in one timed relevance task, but it does not fix or verify the reliability threshold the note requires before a summary licenses stopping.
- [addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) -- rejected as a comparison mismatch: the experiment does not measure matched answer-bearing units in one read-volume currency.
- [types give agents structural hints before opening documents](../../../../notes/types-give-agents-structural-hints-before-opening-documents.md) -- rejected as an unsupported transfer: query-biased sentence extracts are not type metadata, and the participants are not agents selecting among typed KB artifacts.
- [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -- rejected as redundant: Pirolli already anchors its proximal-cue decision model, while the narrower Tombros result lands more precisely in the two retained targets.
- Generic query and relevance-judgment hits in external system reviews -- rejected as implementation vocabulary without a useful source-to-system comparison.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The main experiment used two independent groups of ten, mainly postgraduate conversion-course students, a five-minute relevance-judgment task, TREC queries and Wall Street Journal documents, and a baseline whose displayed text length initially differed. The appendix's same-length rerun addresses the length confound but does not widen the population or task.
