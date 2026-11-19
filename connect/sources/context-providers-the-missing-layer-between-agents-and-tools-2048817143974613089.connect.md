---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/context-providers-the-missing-layer-between-agents-and-tools-2048817143974613089.md"
source_has_frontmatter: true
date: "2026-04-27"
depth: standard
---

# Connection Report: Context providers: the missing layer between agents and tools

**Source:** [Context providers: the missing layer between agents and tools](../../sources/context-providers-the-missing-layer-between-agents-and-tools-2048817143974613089.md)

## Discovery Trace

**Index scan:**
- Read [sources collection rules](../../sources/COLLECTION.md) -- snapshots are immutable; strongest authored surface is the ingest report, with authorised labels to `kb/notes/`, `kb/sources/`, and `kb/agent-memory-systems/`.
- Read [notes dir-index](../../notes/dir-index.md) -- flagged [subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md), [tool loop](../../notes/tool-loop-index.md), [agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md), [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md), and [skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md).
- Read [agent-memory-systems dir-index](../../agent-memory-systems/dir-index.md) -- flagged [Tendril](../../agent-memory-systems/reviews/tendril.md), [Agent-S](../../agent-memory-systems/reviews/Agent-S.md), [OS-Copilot](../../agent-memory-systems/reviews/OS-Copilot.md), and [SkillWeaver](../../agent-memory-systems/reviews/SkillWeaver.md) as nearby executable/tool-surface systems.

**Topic indexes:**
- Read [computational-model index](../../notes/computational-model-index.md) through search output -- tool-loop, scoping, sub-agent, and unified calling convention notes form the active cluster.
- Read [learning-theory index](../../notes/learning-theory-index.md) through search output -- executable tools and deploy-time constraining are adjacent, but this source is primarily context-engineering evidence rather than learning-theory evidence.

**Body search:**
- `rg -n "context provider|ContextProvider|tool surface|too many tools|tool instructions|tool schema|tool loop|MCP|sub-agent|subagent|query_.*update_|Slack|Google Drive|Notion|context pollution|source-specific|tool-use logic|tool choice|tools" kb/notes kb/agent-memory-systems kb/reference --glob '*.md'` -- kept the notes and reviews above; rejected broad `tools` hits where the source only shared vocabulary.
- `find kb/notes -maxdepth 1 -name '*tool*' -o -name '*context*' -o -name '*agent*'` -- confirmed the tool-loop/context cluster and did not surface a pre-existing "context provider" note.

**Link following:**
- Followed [subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) to [tool loop](../../notes/tool-loop-index.md) and [semantic sub-goals that exceed one context window become scheduling problems](../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md). The source is most directly an implementation pattern for the "different capability surfaces" forcing case.
- Followed [tool loop](../../notes/tool-loop-index.md) to [agent is a tool loop](../../notes/agent-is-a-tool-loop.md) and [conversation vs prompt refinement in agent-to-agent coordination](../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md). These are context, not primary links.
- Followed [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) to scoping and sub-agent isolation notes. The source provides practitioner evidence for scoping by source/tool provider.

## Connections Found

- [Subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) -- **evidence**: Context Providers are a concrete source-scoped version of the claim: the main agent should not carry one giant tool surface when child/source tasks need different capability surfaces.
- [Tool loop](../../notes/tool-loop-index.md) -- **evidence**: The source supplies a practitioner pattern for exposing/relocating the loop: a parent agent delegates to source-specific sub-agents behind two high-level tools rather than directly owning every raw tool.
- [Agent context is constrained by soft degradation, not hard token limits](../../notes/agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) -- **evidence**: The reported "three walls" are exactly soft-degradation symptoms: context pollution, overlapping scopes, and tool instructions crowding out the agent's main job.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: The source treats context surface area as the primary architectural constraint and reports that smaller main-agent context can offset sub-agent overhead.
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) -- **evidence**: Source-specific sub-agents impose scoping around Slack, Drive, GitHub, and other tool surfaces that would otherwise collide in one flat context.
- [Skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **compares-with**: The source distinguishes skills from Context Providers: skills package task instructions, while Context Providers hide source-specific tool logic behind a delegated query/update surface.
- [Tendril](../../agent-memory-systems/reviews/tendril.md) -- **compares-with**: Both reduce visible tool surfaces, but Tendril keeps a stable tool-making interface while Context Providers wrap each external source behind query/update sub-agents.

## Bidirectional Candidates

- [Subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) <-> source -- **evidence**: The return link would give the theory note a concrete practitioner case where changing tool surface by source forces sub-agent boundaries.
- [Tendril](../../agent-memory-systems/reviews/tendril.md) <-> source -- **compares-with**: Both are tool-surface compression patterns worth comparing from the system-review side.

## Reverse-edge Candidates

- [Subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md) → source -- **evidence**: The source corroborates the note's claim that child tasks need fresh capability surfaces, but with "source provider" rather than "task phase" as the boundary.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) → source -- **evidence**: The source provides practitioner evidence that reducing always-visible tool instructions can improve latency and quality even after adding sub-agent hops.
- [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md) → source -- **evidence**: The source is a live engineering example of imposing scope by spawning source-specific sub-agent frames.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Apparent success is an unreliable health signal in framework-owned tool loops](../../notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) -- rejected: shares the tool-loop topic, but the source focuses on tool-surface compression and scoping, not hidden failure recovery.
- [Traditional debugging intuitions break when tool loops can recover semantically](../../notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover-semantically.md) -- rejected: not about debugging or semantic recovery.
- [Agent-S](../../agent-memory-systems/reviews/Agent-S.md) -- rejected as a primary comparison: Agent-S introspects/constructs procedural prompts and delegates code execution, but does not wrap many third-party sources behind query/update provider agents.
- [OS-Copilot](../../agent-memory-systems/reviews/OS-Copilot.md) and [SkillWeaver](../../agent-memory-systems/reviews/SkillWeaver.md) -- rejected as primary comparisons: both learn executable tools from trajectories; this source is about runtime context-provider wrapping rather than learning tool libraries.

## Index Membership

- [Context engineering index](../../notes/context-engineering-index.md) -- possible source reference for source-scoped sub-agent delegation as a context-efficiency pattern.
- [Tool loop](../../notes/tool-loop-index.md) -- possible source reference for tool-surface compression and loop exposure.

## Synthesis Opportunities

- Context Providers suggest a sharper note: **"tool surfaces should be scoped by source when source-specific operational rules dominate"**. It would combine [subtasks that need different tools force loop exposure in agent frameworks](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md), [LLM context is composed without scoping](../../notes/llm-context-is-composed-without-scoping.md), [skills are instructions plus routing and execution policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md), and [Tendril](../../agent-memory-systems/reviews/tendril.md).

## Flags

- The source is a strong practitioner report but has no public linked benchmark data in the snapshot. Treat token/latency claims as directional until the linked examples or code are inspected.
