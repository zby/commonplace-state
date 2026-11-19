---
description: "Discovery candidates for folding subagents into a shared loop: decomposition boundaries, model-dependent simplification, and evaluation limits"
type: types/connect-report.md
source: "kb/sources/.snapshots/building-agents-fold-subagents-into-main-loop.md"
source_has_frontmatter: true
date: "2026-11-17"
depth: standard
---

# Connection Report: Building agents: When to fold subagents into your main agent loop

**Source:** `kb/sources/.snapshots/building-agents-fold-subagents-into-main-loop.md` (local captured article; source identity and durable navigation are in the ingest below).
**Authored surface:** [Matching ingest](../../../../sources/building-agents-fold-subagents-into-main-loop.ingest.md). All outbound suggestions below belong there, never in the immutable snapshot. Many are already discussed in that ingest; this report distinguishes useful existing coverage from prospective additions.

Discovery performed by `gpt-6-astra` under `cp-skill-connect`, with no delegation or external search. The source is a vendor practitioner report, not a controlled architecture comparison. Its central mechanism is preserving cross-step information while deferring skill and tool loading; its boundaries retain separate agents for measured degradation, disposable parallel work, and tool or instruction conflicts.

## Discovery Trace

### Surfaces and queries

Read the source and reports collection contracts, the connect-report type, the complete snapshot, and its matching ingest. Read the theory collection contract for return-edge authorization. Prospecting covered all six destinations named by the source contract: theory, reference, historical agent-memory-systems, agentic-systems, tags, and sources. Excluded instructions and work. The snapshot has no `tags:` field; no by-tag membership query was needed.

Read each destination's `README.md`. Generated the complete title surface once per destination with:

```bash
rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'
```

The combined output exceeded the tool display limit; recovered the omitted theory, reference and historical-system portions from the tool's output log. Then scanned scoped descriptions with the actual pipeline below, separately for each of the six destinations:

```bash
rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'subagent|sub-agent|decompos|progressive disclosure|scaffold|single.agent|context.*isolat|handoff'
rg -l -i 'lossy (summar|handoff)|fold.*subagent|divid.*context|shared context|progressive disclosure' kb/<destination>/ --glob '*.md'
```

Additional focused searches:

```bash
rg -n -i 'subagent|sub-agent|fold|decompos|skill' kb/reference/adr/097-agentic-analysis-drops-decisions-that-change-no-result.md
rg -n -i 'shared context|progressive disclosure|single.agent|sub.agent' kb/tags/context-engineering-README.md kb/tags/computational-model-README.md
rg -n -i 'subagent|sub-agent|coordination|single.agent' kb/agent-memory-systems/reviews/claude-workstream-kit.md kb/agentic-systems/reviews/claude-code-dynamic-workflows.md
rg -n 'building-agents-fold-subagents' kb/theory/
```

The last search found no existing theory citation to this ingest. No semantic ranking or scores were used.

### Per-destination evaluation

- **Theory:** Titles exposed decomposition heuristics, the fixed-difficulty/frontier distinction, operational simplification signals, flat-context scoping, and end-to-end knowledge-access evaluation. Descriptions strengthened the decomposition and fixed-difficulty candidates; body search surfaced the evaluation and scoping neighborhoods. Read the five candidate notes in full. Kept decomposition, simplification signals, scoping, and fixed-difficulty comparison. Rejected knowledge-access evaluation as a less direct match than the component-removal protocol. Followed the ingest's links to decomposition, operational signals, and scoping; followed the fixed-difficulty note's link to operational signals. The same neighborhood independently converges on conditional rather than universal reduction of agents.
- **Reference:** README and titles exposed review architecture, scenario architecture, and ADR 097 on dropping decisions that change no result. Descriptions also exposed the sub-agent model-selection regression. The body search mostly found navigation and proposal material. No candidate supplied a sufficiently direct source-specific reader need: an external deployment report is not evidence for Commonplace's chosen workflow state. No reference edge retained.
- **Agent-memory-systems:** Read the historical survey README, which explicitly freezes this corpus. Titles exposed Claude Workstream Kit; fully read its review after the source-adjacent scaffolding theme suggested a check. Its fresh-context verifier is compatible with the article's explicit verification exception, not a counterexample. Active-work lifecycle is not the article's main contribution. No historical review edge retained; progressive-disclosure matches alone did not justify a broad comparison list.
- **Agentic-systems:** The curated head exposed Claude Code dynamic workflows, later rediscovered in titles and descriptions. Read the full review. Kept the contrast between model-written symbolic orchestration over isolated agents and a model executing the plan in its own main loop. The ingest already discusses this comparison. Other memory-table and archive body hits were not promoted merely for mentioning shared context.
- **Tags:** Read the tag index and generated titles. Context engineering and computational model are useful routing areas, but the source has no tags and the source contract supplies no formal source-to-tags label. Focused body checks of their heads produced no matching lines. No index-membership change proposed: do not index a local snapshot or infer membership from topic words.
- **Sources:** Titles exposed Towards a Science of Scaling Agent Systems, Claude Workstream Kit's scaffolding announcement, and other harness accounts. Descriptions narrowed the controlled scaling study as the strongest comparison. Read its ingest fully. Kept it because it supplies task-dependent architecture comparisons against which to assess the article's unpublished enterprise observations. Read the matching ingest as the authored companion, not as an additional edge candidate. Followed its links to the kept theory and system targets. Broader harness and shared-memory hits were redundant with these more discriminating comparisons.
- **External:** The original URL is already supplied in the snapshot and ingest. Its existing source-identity role is sufficient; no redundant candidate is needed. Other linked vendor resources were not browsed. External authorization does not license web prospecting.

### Candidate origins

- kb/theory/decomposition-heuristics-for-bounded-context-scheduling.md — titles, descriptions, link-following
- kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md — titles, link-following
- kb/theory/llm-context-is-composed-without-scoping.md — titles, link-following
- kb/theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md — titles, descriptions
- kb/agentic-systems/reviews/claude-code-dynamic-workflows.md — curated-head, titles, descriptions, link-following, body-search
- kb/sources/towards-a-science-of-scaling-agent-systems.ingest.md — titles, descriptions, link-following

## Connections Found

These are candidates for the ingest's authored connection surface. Existing prose coverage should be retained or tightened, not duplicated as extra footer links.

- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — **is-evidence-for**: the article's recommendation to merge specialists sharing data or chaining outputs bears on preserving cross-item interactions and avoiding lossy interfaces. Its fold-one-at-a-time tests offer a practitioner approach to the note's unresolved stopping condition. This is bounded operational testimony, not validation of every heuristic. Already discussed in the ingest.
- [Operational signals that a component is a relaxing candidate](../../../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **is-evidence-for**: the article reports a shipping workflow that broke after a merge despite lower latency, and recommends chain-covering repeated end-to-end tests. This materially illustrates why component removal must be assessed in integration, without establishing that all process rules are defective. Already discussed in the ingest.
- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) — **compares-with**: compare shared-context continuity against selected-input frames. Deferring skill loading reduces initial volume but does not establish local scope among supplied instructions. This comparison prevents reading the article as a universal argument against separate contexts. The ingest already makes the comparison, but its characterization of the current note needs refreshing.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) — **compares-with**: the article describes collapsing existing enterprise workflows as models improve; the note distinguishes that setting from assigning harder new work. This is an additional comparison beyond the ingest's existing set. The article provides no matched cross-generation frontier measurement, so it cannot establish the note's recurrence hypothesis.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — **compares-with**: compare where planning executes and where intermediate results live. Dynamic workflows put a model-authored script and worker results outside the conversation; the article's target loop keeps planning and tool results in the main model context. Same-vendor designs occupy different task and control boundaries rather than forming a simple contradiction. Already discussed in the ingest.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **compares-with**: compare the conditions under which coordination overhead outweighs additional agents. The controlled study reports task-dependent outcomes, whereas the article offers unpublished enterprise comparisons and migration heuristics. Neither licenses a universal agent-count rule or a transferable numeric threshold. Already discussed in the ingest.

## Bidirectional Candidates

- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) → [matching ingest](../../../../sources/building-agents-fold-subagents-into-main-loop.ingest.md) — **evidenced-by**: qualify the open stopping-condition question with the article's practitioner test: fold one boundary, cover production chains and hard rules, repeat runs, and inspect task-level regressions. The theory contract authorizes this label for sources. Use it as a bounded proposal for detecting overhead, not as corroboration of a universal threshold. The ingest has no retained quotes; future authoring must retain sufficient quotations through grounding or mark its ingest citation `(snapshot required)`.

## Reverse-edge Candidates

None. The useful return edge is recorded above rather than duplicated here.

## Off-authorisation Candidates

None. Tags were a routing surface, but no specific formal tag edge passed the articulation test.

## Raw Text Candidates

None.

## Rejected Candidates

- [Knowledge-access architecture must be evaluated end to end](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — its retrieval-to-outcome distinction is compatible with skill activation checks, but the article's concrete regression concerns merging workers, not an isolated knowledge-access intervention. The operational-signals target is more precise.
- [Claude Workstream Kit](../../../../agent-memory-systems/reviews/claude-workstream-kit.md) — its retained active state and fresh-context verifier do not test the article's proposed domain-worker folds. Verification is explicitly an exception in the source, so treating this review as a contradiction would mislead.
- [Sub-agent model-selection regression](../../../../reference/harness-sub-agent-model-selection-regression.md) — a search hit on worker orchestration, but execution-provenance failure is not the article's mechanism or architectural comparison.

## Index Membership

None. Keep any future durable navigation attached to the ingest, not the local snapshot.

## Synthesis Opportunities

A future investigation could combine the decomposition heuristics, the controlled scaling study, and this practitioner's migration protocol into a task-relative stopping test. It would distinguish interaction loss, coordination cost, separate-context benefit, and hard-rule regressions. The missing contribution is a tested decision procedure, not another generic statement that architecture depends on the task. No synthesis artifact is proposed for immediate creation.

## Maintenance Observations

The matching ingest describes the scoping note as calling subagents “the canonical architectural move” for enforcing scope and refers to its flat-versus-bounded paragraph. The current note instead distinguishes selecting a frame's inputs from establishing scope among supplied instructions. A later authorized maintenance pass should refresh that representation; this report did not change either artifact.

## Flags

- Preserve the source's evidence limits: vendor-selected examples, unpublished task comparisons, model-specific guidance, and one reported intermittent regression. Shared-context benefit is asserted rather than causally isolated.
- Do not collapse independent verification into the main loop on this source's authority: the article explicitly retains verification as a suitable subagent use.
- No split recommendation: the retained connections form a tightly related architecture/evaluation cluster, not five unrelated claims across three topic areas.
- Only this report was authored. Existing working-tree edits were left untouched.
