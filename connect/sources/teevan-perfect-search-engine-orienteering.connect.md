---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/teevan-perfect-search-engine-orienteering.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: The Perfect Search Engine Is Not Enough

**Source:** [The Perfect Search Engine Is Not Enough](../../../../sources/.snapshots/teevan-perfect-search-engine-orienteering.md)

## Discovery Trace

**Description listing scan:**

- Read scoped title and description listings across `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The scan flagged [link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md), [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md), [design for the first-time human except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md), and [knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md). The first two survived body inspection; the others were rejected as adjacent or downstream.

**Topic indexes:**

- Read [top-level note navigation](../../../../tags/README.md), [links](../../../../tags/links-README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), and [agentic systems](../../../../agentic-systems/README.md). Only the links index exposed the same direct local-navigation/search cluster; the system indexes yielded no source-specific target.

**Body search:**

- `rg -n "perfect search engine|orienteering|Teevan|local steps|keyword" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' --glob '!kb/sources/.snapshots/**'` found no prior Teevan ingest or citation. Generic keyword-search hits in system reviews were rejected because they describe implementations rather than the local-step/direct-jump distinction.
- `rg -n "link-following|local navigation|long-range|search results|query-time|pointer" kb/notes --glob '*.md' --glob '!**/dir-index.md'` recovered the five note candidates above plus broad pointer mentions. Body inspection kept the two claims to which the study supplies a direct human comparison and rejected matches that merely share retrieval vocabulary.
- `rg -n "link-following-and-search|agents-navigate-by-deciding|pointer-design-tradeoffs|design-for-the-first-time-human|knowledge-access-architecture" kb/notes/tags-README.md kb/notes/*-README.md kb/reference/README.md kb/agent-memory-systems/README.md kb/agentic-systems/README.md` confirmed that the first two candidates form the curated links cluster rather than an accidental lexical match.

**Link following:**

- Followed [link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) to [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) and [pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md). The first target makes the closest transfer: Teevan et al. distinguish contextual local steps from direct keyword jumps, while the note maps a similar contrast onto KB link-following and search. The agent-navigation note is useful for comparison but already rests on Pirolli for its proximal-cue model. The pointer note makes a different fixed/query-time/crafted representation claim, so Teevan is not direct evidence for its four-axis taxonomy.
- Followed the navigation cluster into [design for the first-time human except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) and [knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md). Both are broader syntheses whose load-bearing claims are not tested by this known-item-search study.

## Connections Found

- [link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) -- **is-evidence-for**: Teevan et al.'s diary study distinguishes contextual, local-step orienteering from direct keyword jumps during human known-item search. That bears directly on the note's local-navigation versus long-range-search distinction, while leaving the note's LLM-agent transfer and metadata prescriptions to be argued locally.
- [agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -- **compares-with**: the study describes humans repeatedly choosing contextual steps toward a known item, providing a bounded human comparison for the note's agent follow/skip model without establishing the agent mechanism or token-cost account.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) -- rejected as adjacent: Teevan et al. compare search behavior, not fixed, query-time, and crafted pointer representations across the note's four axes.
- [design for the first-time human except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) -- rejected as an unsupported transfer: the source studies human information seeking but does not compare human and LLM access costs or whole-document loading.
- [knowledge-access architecture must be evaluated end to end](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) -- rejected as too broad: one discovery-stage study cannot support the note's whole-path evaluation model.
- Keyword-search descriptions in external system reviews -- rejected as implementation matches that do not help a reader recover the behavioral distinction in this source.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Scope the source to human known-item seeking in the observed desktop, email, and Web settings. It does not test LLM agents, KB metadata requirements, or open-ended exploratory search.
