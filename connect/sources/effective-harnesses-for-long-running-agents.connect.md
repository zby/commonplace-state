---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/effective-harnesses-for-long-running-agents.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Effective harnesses for long-running agents

**Source:** [Effective harnesses for long-running agents](../../../sources/effective-harnesses-for-long-running-agents.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i 'context|session|progress|artifact|continu|workflow|compaction|state|verification|incremental|environment|harness|memory|handoff'`; retained the session-history, statelessness, readable-artifact, oracle-accumulation, and scaling-frontier notes for closer reading.
- Ran `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'context|session|progress|artifact|continu|workflow|compaction|state|verification|incremental|environment|harness|memory|handoff'`; retained Claude Context Guard and Claude Workstream Kit as concrete comparison systems.

**Topic indexes:**
- The context-engineering, learning-theory, agent-memory, and workshop-layer routes in `kb/notes/tags-README.md` all matched parts of the source. The most specific settled claims were loaded instead of proposing a broad index spray.

**Body search:**
- Ran `rg -n -i "long-running agents|claude-progress|feature_list|compaction isn" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`; this found the code-grounded Claude Context Guard review and no prior durable coverage of this exact Anthropic report.
- Ran `rg -l -i "persistent progress|progress file|feature list|incremental progress|context windows" kb/sources --glob '*.ingest.md'`; adjacent ingests covered context windows and dynamic harnesses but not the initializer/progress-file/feature-ledger combination.

**Link following:**
- Followed the session-history note into bounded-context selection and artifact-first handoff; the source supplies a practitioner instance of retaining state in files and git rather than inheriting only a compacted transcript.
- Followed the readable-artifact note into oracle accumulation and the scaling-frontier note; the source's JSON feature ledger, end-to-end browser checks, and Opus 4.5 example fit those mechanisms without establishing their general effectiveness.
- Followed Claude Context Guard and Claude Workstream Kit; both implement richer variants of the source's file-native recovery pattern, so they are useful comparisons rather than evidence for Anthropic's effectiveness claims.

## Connections Found

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- **is-evidence-for**: Anthropic reports that compaction alone leaves ambiguous half-finished state, while a progress file and git history let a fresh session reconstruct selected work state.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- **is-evidence-for**: the initializer and repeated startup procedure externalize orientation that a fresh agent does not carry between sessions.
- [Oracle accumulation improves the selection environment for every later candidate](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- **is-evidence-for**: a persistent feature ledger starts every requirement as failing and turns passing status into an end-to-end verification claim, though the report does not show longitudinal oracle growth.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- **is-evidence-for**: the report's frontier model still needed progress state, structured requirements, incremental work, and external verification for a production-scale long-horizon task.
- [Claude Context Guard](../../../../agent-memory-systems/reviews/claude-context-guard.md) -- **compares-with**: both use progress, feature, git, and startup artifacts for cross-session recovery; Context Guard adds a broader safeguard-file contract and audit procedure.
- [Claude Workstream Kit](../../../../agent-memory-systems/reviews/claude-workstream-kit.md) -- **compares-with**: both keep project-scoped active work outside chat history; Workstream Kit narrows startup context through an active pointer and adds explicit lifecycle closure.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) → source -- **evidenced-by**: practitioner evidence that compaction is not a sufficient handoff and that selected progress artifacts outperform guessing from inherited conversational state.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) → source -- **evidenced-by**: the initializer/startup protocol is a concrete architecture for restoring orientation to a cold session.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) → source -- **evidenced-by**: Opus 4.5 on a harder long-horizon assignment still required explicit state, task decomposition, and verification scaffolding.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A functioning knowledge base needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) -- rejected as a direct source connection because the source demonstrates a coding-work ledger but does not argue the library/workshop distinction or promotion lifecycle.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- rejected as direct evidence because the harness retains readable state but does not implement an improvement loop that revises the artifacts from experience.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) -- rejected because the progress and feature files provide continuity, but the report does not test record substitution or governance guarantees.

## Index Membership

None.

## Synthesis Opportunities

The session-history, statelessness, and workshop-layer notes together suggest a sharper distinction between **context continuation** and **work continuation**: compaction continues a token stream imperfectly, while a work ledger reifies task state, completion criteria, and next action for a fresh executor. The source supplies one practitioner case, but the synthesis should wait for comparison across the existing continuity systems.

## Maintenance Observations

None.

## Flags

- Practitioner evidence only: no baseline, run count, cost data, or failed harness variants are reported.
