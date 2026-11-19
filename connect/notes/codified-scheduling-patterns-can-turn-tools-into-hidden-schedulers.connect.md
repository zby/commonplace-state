---
description: "Discovery report for possible KB connections from Cross-task transition policy remains scheduling behind a tool interface"
type: kb/cache/types/connect-report.md
source: "kb/notes/cross-task-transition-policy-remains-scheduling-behind-tools.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Cross-task transition policy remains scheduling behind a tool interface

**Source:** [Cross-task transition policy remains scheduling behind a tool interface](../../../../notes/cross-task-transition-policy-remains-scheduling-behind-tools.md)

## Discovery Trace

**Description listing scan:**
- Read the source collection's outbound-linking rules and regenerated the complete H1 title surface for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 354 entries under `notes`, 135 under `reference`, 173 under `agent-memory-systems`, 12 under `agentic-systems`, 504 under `sources`, and 44 under `instructions`.
- Re-read the by-tag description surfaces for `computational-model`, `context-engineering`, and `tool-loop`. The final note's closest theoretical neighbours remain the optional-tool-loop, stateful-tool, host-language scheduler, capability-surface, and runtime-role notes.
- Re-ran destination-scoped description searches for `(schedul|orchestrat|tool loop|control surface|progression|workflow)`. The memory collection still concerns retained workflow memory rather than progression ownership; Commonplace reference and instruction artifacts remain wrong-register targets for this theoretical claim.

**Topic indexes:**
- Re-read `kb/notes/README.md`, `tags-README.md`, `computational-model-README.md`, `context-engineering-README.md`, and `tool-loop-README.md`. The source remains correctly placed in the tool-loop cluster, but that head's visible title and “hiding them in tools” summary now lag the reframed claim.
- Re-read the authorised destination heads (`reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`). `agentic-systems/claude-code-dynamic-workflows.md` remains the clearest concrete test of the revised distinction between scheduler role and concealed role.

**Body search:**
- `rg -n -i "architectural role|decision authority|transition authority|cross-task transition|distinct task goals|workflow tool|tool interface|hidden scheduler|optional tool loop|capability surface" kb/notes --glob '*.md'` — confirmed that the revised note now authors the optional-tool-loop and host-language-scheduler connections and that existing stateful-tool and capability-surface links still serve distinct reader needs.
- Ran the same query over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. Kept Claude Code dynamic workflows as a concrete exposed-workflow case; rejected generic tool-interface, memory, governance, and Commonplace-procedure matches.
- `rg -n --fixed-strings 'codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md' ...` — found two inbound citers, both of which still repeat the incumbent title and a stronger hidden/forced-placement summary.

**Link following:**
- Re-read the final note's authored neighbours. `llm-frameworks-should-keep-the-tool-loop-optional.md` now supplies the qualification that a framework abstraction can be escaped; `the-practical-scheduler-is-the-host-language.md` supplies the explicit alternative placement. Both initial connection candidates were consumed by the revision.
- Followed `subtasks-that-need-different-tools-force-loop-exposure-in-agent.md` and `agent-is-a-tool-loop.md`. They establish capability-surface changes and child-loop construction, but do not alter the final note's narrower responsibility test.
- Re-read `agentic-systems/claude-code-dynamic-workflows.md`: its Workflow tool is explicitly described as orchestration to operators and authors, so it remains a useful witness that a tool-shaped scheduler need not be hidden from every audience.

## Connections Found

- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **evidenced-by**: a shipped workflow tool explicitly exposes its orchestration role, witnessing the revised distinction between being callable through a tool interface and concealing scheduler authority; its different operator/model audiences also bound the note's binary hidden/exposed language.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [LLM frameworks should keep the tool loop optional](../../../../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) -- the final note now links it inline at the precise qualification point; no additional candidate remains.
- [The practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) -- the final note now authors this connection in its footer.
- [Stateful tools recover control by becoming hidden schedulers](../../../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) -- already linked and still owns the narrower covert-runtime case.
- [Subtasks that need different tools force loop exposure in agent frameworks](../../../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) -- already linked; its fresh-capability-surface argument is adjacent but not the same role-classification claim.
- [Agent runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- broader analytical decomposition; the final note's authored neighbours provide more specific traversal.
- [Decision authority is independent of agent count](../../../../sources/multi-agent-analytics-control-plane-2087241401649996149.ingest.md) -- similar authority-over-shape reasoning, but the source concerns worker count rather than tool interfaces and would be an analogy rather than direct evidence.

## Index Membership

- [Tool loop](../../../../tags/tool-loop-README.md) -- already lists the source, but its entry needs visible-title and summary reconciliation after the keep-reframe rename.
- [Computational model](../../../../tags/computational-model-README.md) -- the source remains tag-addressable through the complete generated membership; no new curated-head entry clears the small-head threshold.

## Synthesis Opportunities

None.

## Maintenance Observations

- Both inbound citers preserve the old title text. The tool-loop head also states that codification forces policy into hidden placement, and the semantic-sub-goals note calls codified experience a forcing cause. Those premises no longer match the revised note and must be reconciled during the required rename follow-up.

## Flags

- Hidden/exposed status is audience-relative: the same workflow may expose controls to operators while remaining opaque to the model. The note's binary wording is usable only after the consuming audience is fixed.
