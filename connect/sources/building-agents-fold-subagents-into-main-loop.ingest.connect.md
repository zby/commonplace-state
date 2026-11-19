---
description: "Connection discovery for Anthropic's subagent-consolidation guidance: decomposition tradeoffs, context isolation, and task-level migration checks"
type: types/connect-report.md
source: "kb/sources/building-agents-fold-subagents-into-main-loop.ingest.md"
source_has_frontmatter: true
date: "2026-11-17"
depth: standard
---

# Connection Report: Building agents: When to fold subagents into your main agent loop

**Source:** [Building agents: When to fold subagents into your main agent loop](../../../../sources/building-agents-fold-subagents-into-main-loop.ingest.md)

Discovery-only judgment by `gpt-6-astra`, following `cp-skill-connect`. Only this report is an output. Existing source links are distinguished from proposed additions below. Source claims were assessed from the complete ingest, not independently checked against the original article.

## Discovery Trace

### Coverage and queries

Read the source and source collection contract, the connect-report type, and the report collection contract. Prospected all six named local destinations: theory, reference, agent-memory-systems, agentic-systems, tags, and sources. Instructions and work were excluded. The source has no tags, so no source-tag membership search was required. No semantic search or external browsing was used.

For each of those six destinations, generated the complete title surface with `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`. Recovered the truncated theory/reference portion from the tool's saved output. Read each destination's `README.md`.

For each destination, ran these scoped searches:

- `rg '^description:.*(decompos|subagent|sub-agent|progressive disclosure|integration|single.loop)' kb/<destination> --glob '*.md'`
- `rg -l 'lossy|context.coupled|fold.*agent|isolation.*verification' kb/<destination> --glob '*.md'`

Additional theory search: `rg -l 'subagent|decomposition|progressive disclosure' kb/theory/ --glob '*.md' | head -25` (a bounded supplemental sample, not the complete title scan).

Additional source search: `rg -l -i 'multi-agent pipelines|scaling agent systems|scaffolding obsolete' kb/sources/*.ingest.md`.

No numeric retrieval scores were produced.

### Per-destination evaluation

- **Theory:** The source already names decomposition heuristics and operational relaxing signals. Read both in full; retain them as existing connections worth preserving, with restricted evidential scope. Titles exposed the flat-context scoping note, the causal-chain conjecture, and final-task-success note. Description/body searches re-exposed the scoping and causal-chain notes. Followed the decomposition note's causal-chain link, and that note's scoping link; read both targets fully. Keep scoping as a comparison between information preservation and isolation, not as a contradiction. Reject causal-chain corroboration: the enterprise comparisons do not independently vary topology, isolation, and verification. Read final-task-success fully but reject the stronger evidence link because the shipping example reports a lost required dependency, not successful equivalent fallback. Read the theory collection contract for the proposed return edge.
- **Reference:** README, full titles, descriptions and body queries exposed architecture and historical code-scheduled workflow material. No candidate supplied a more direct reader benefit than the theory notes: the source does not evaluate Commonplace's chosen workflow architecture. No reference edge retained.
- **Agent-memory-systems:** README identifies this as frozen historical coverage. Titles and description search exposed OpenSage and getsentry/skills. Inspected OpenSage's opening and Core Ideas: it has both skills and dynamic subagents, but that coexistence is not a comparison of folding context-coupled specialists. Reject the generic product connection; no memory-system edge retained.
- **Agentic-systems:** README exposed Claude Code dynamic workflows; titles and descriptions re-exposed it. Read the full review. Keep a comparison on where intermediate state lives and which work remains isolated. Its symbolic coordination and final-result-only return path make the source's retained parallel-work exception concrete; neither artifact establishes a winning architecture across tasks.
- **Tags:** README and full titles expose context-engineering, computational-model and evaluation heads. Read the context-engineering head; it is selective, not `complete: true`. No by-tag completeness skip applies. The source has no assigned tags. A broad head link would be less useful than the specific theory destinations. No tag edge or membership recommendation retained.
- **Sources:** Titles exposed the multi-agent analytics report and controlled scaling study; focused searches re-exposed both. Read both fully. Followed the analytics report's existing scaling-study link. Keep the analytics comparison for shared diagnostic state versus fact-returning workers, and the scaling comparison for task-contingent coordination costs and the distinction between controlled experiments and deployment anecdotes. Other tool-count and skill-package hits were less direct.
- **External:** The original article URL is already present as source provenance. It is an authorized `derived-from` destination, but no duplicate body edge is proposed. External prospecting was skipped; no new web targets were sought.

### Candidate origins

- kb/theory/decomposition-heuristics-for-bounded-context-scheduling.md — known, titles, body-search, link-following
- kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md — known, titles
- kb/theory/llm-context-is-composed-without-scoping.md — titles, body-search, link-following
- kb/agentic-systems/reviews/claude-code-dynamic-workflows.md — titles, curated-head, descriptions
- kb/sources/multi-agent-analytics-control-plane-2087241401649996149.ingest.md — titles, body-search, descriptions
- kb/sources/towards-a-science-of-scaling-agent-systems.ingest.md — titles, body-search, descriptions, link-following

## Connections Found

- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — **is-evidence-for**: preserve the existing connection. The source contributes a bounded practitioner test candidate for the note's open stopping question: fold one context-coupled boundary, then compare repeated task outcomes, cost, and required-chain completion. It neither establishes a threshold nor validates symbolic routing removal in general.
- [Operational signals that a component is a relaxing candidate](../../../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **is-evidence-for**: preserve the existing connection specifically to integration testing. The shipping-dependency regression shows why latency improvement cannot substitute for checking complete production chains. It does not establish that the original boundary encoded a bad theory or that mandatory process constraints may be dropped.
- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) — **compares-with**: the source favors retaining interacting evidence in one loop; the target explains what isolation is lost when instructions share a frame. Reading them together distinguishes loading less initially from enforcing separation after skills have loaded, sharpening the source's instruction-conflict exception.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — **compares-with**: compare intermediate-state placement and parallel execution. The reviewed workflow keeps intermediate results in script variables and returns only the final result to the parent; the source favors keeping context-coupled reasoning in the main loop while preserving disposable parallel work. This helps choose which information must cross a boundary, without treating the vendor's two accounts as mutually exclusive prescriptions.
- [Why Multi-Agent Pipelines Fail for Complex Analytics](../../../../sources/multi-agent-analytics-control-plane-2087241401649996149.ingest.md) — **compares-with**: both diagnose lossy handoffs among judgment-bearing specialists. The analytics redesign retains narrow fact-returning workers under one diagnostic owner, showing that centralizing reasoning need not eliminate every worker. Both remain practitioner reports with unisolated interventions.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **compares-with**: compare coordination benefit by task structure and evaluation design. The controlled study supplies a counterweight to deployment anecdotes: extra agents help some task families and hurt others, with overhead and verification varying across topologies. Its numeric thresholds should not become defaults for the source's migration procedure.

## Bidirectional Candidates

- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) → source — **evidenced-by**: a return link would help a scheduler designer find a practical candidate test for excessive decomposition. Under the theory collection's rules, frame this evidence as qualifying the heuristic: preserving interfaces sometimes favors merging, and repeated task-level evaluation must retain mandatory-chain and separate-verifier checks. This is not independent corroboration of the full heuristic set. Ground the exact source use before authoring it.

## Reverse-edge Candidates

None. The strongest useful inbound edge is the return link recorded above.

## Off-authorisation Candidates

None. The source contract names tags as a prospecting destination but provides no tag label; no sufficiently useful tag candidate required escalating that gap in this run.

## Raw Text Candidates

None.

## Rejected Candidates

- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — the source neither isolates the proposed dependency chain nor measures verification decorrelation. Its separate-verifier exception is not a causal test; the scoping comparison carries the useful distinction more directly.
- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) — the source motivates checking required paths, but does not document the target's decisive case of successful equivalent fallback concealing a broken intended path. Do not promote this analogy into evidence.
- [OpenSage](../../../../agent-memory-systems/reviews/OpenSage.md) — the inspected Core Ideas establish coexistence of skills, subagents and summarization, not evidence about merging specialists. A generic architecture link would add little beyond the more precise workflow comparison.

## Index Membership

None. The source landing is organizational rather than an editorial source roster. Source tags do not confer membership in the participating collections of the tag system.

## Synthesis Opportunities

None. The existing decomposition note already owns the information-preservation versus orchestration-cost tradeoff; a new synthesis would duplicate it before the proposed migration test has evidence.

## Maintenance Observations

None.

## Flags

- The source's Quotes section is empty. Before a theory edit relies on the article's reported examples, retain exact supporting quotations through the authorized grounding workflow or explicitly require the pinned snapshot. This connect run does neither.
- The six outbound candidates concentrate on decomposition and its evaluation, rather than three independent topic areas; no split recommendation is warranted.
- Do not infer a universal single-agent preference, a portable latency gain, or permission to discard mandatory rules from the migration guidance.
