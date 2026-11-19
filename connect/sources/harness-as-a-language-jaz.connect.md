---
description: "Connection discovery for JAZ's recursive invoke primitive, programmable history, and prompt-guided adaptation."
type: types/connect-report.md
source: kb/sources/.snapshots/harness-as-a-language-jaz.md
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: Harness as a Language

**Source:** [Paper](https://arxiv.org/abs/2609.26891). The immutable snapshot's prospective authored surface is its paired ingest.

## Discovery Trace

- Read the full snapshot, sources collection contract, connect-report type, and reports contract. Read collection README entry points for notes, reference, agent-memory-systems, agentic-systems, tags, and sources. Read computational-model, context-engineering, and continual-learning tag heads; continual-learning has `complete: true`, so no by-tag sweep was needed there.
- Generated the title surface using `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'`. The broad output exceeded display limits; narrowed its display with `rg -i 'harness|recursive|codeact|letta|ace|context.operation|scheduler|calling convention|fractal|symbolic|scop'`.
- Notes: description search for `context-operation|host language|calling convention` selected the context-operation interface, practical scheduler, and unified-calling notes. Read all three, plus code-complements-weight-prompt. Followed the interface note's link to the RLM walkthrough ingest and the computational-model head's scheduler links. Kept concrete interface and composition comparisons; did not add every general symbolic-execution premise.
- Agent-memory-systems: description search for `ACE review|Letta` and the curated README located both experimental comparators. Read their runtime and core-idea sections. Kept comparisons of search interfaces and adaptation schedules; the retained reviews concern different pinned observations, so they cannot verify the paper's baseline configuration.
- Agentic-systems: searched `JAZ|programmatic|__history__|lossless|bounded call` in Fractal and Claude Code dynamic workflows, alongside ACE and Letta. Read Fractal fully and followed its session-continuity and RLM comparison. Kept Fractal for the exact-history-as-input distinction; the dynamic-workflows hit supplies adjacent orchestration but is less specific.
- Sources: searched descriptions for `RLM|ACE|Letta|recursive|Recursive`; read the RLM walkthrough ingest reached from the interface note. Kept the comparison between making initial inputs programmable and making ongoing interaction history programmable.
- Reference: scanned descriptions with `rg -i 'context|orchestrat|harness|call'`; results concerned Commonplace's installation, review execution, and proposed context assembly. No shipped-system reference gives a closer reader need than the theory notes.
- Tags: inspected computational-model and context-engineering as navigation candidates. Sources has no authorized ordinary edge label to tags, so these are index-membership suggestions only.
- Read notes/COLLECTION.md for independent inbound authorization. Existing theoretical claims can use the paper as a bounded architectural case, without claiming experimental corroboration of their full generality.
- External prospecting skipped. The already supplied paper URL is the primary source; no open-web candidate search was performed.

## Connections Found

- [Context-operation interface](../../../../notes/context-operation-interface-bounds-context-policy.md) — **is-evidence-for**: the contrast between direct history programming and the evaluated search-tool interface supplies a bounded case of different permitted context projections, with achieved retrieval distinct from structural availability.
- [Practical host-language scheduler](../../../../notes/the-practical-scheduler-is-the-host-language.md) — **is-evidence-for**: recursive returning invocations compose through ordinary Python control and live variables; the paper's in-process experiments also illustrate the note's lifetime boundary rather than establishing durable execution.
- [Unified calling conventions](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — **compares-with**: JAZ accepts callables and arbitrary objects through ordinary calls, giving a concrete comparison with the note's claimed requirement for name-based dispatch. It does not by itself demonstrate call-site-preserving refactoring.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — **compares-with**: both expose retained trace material to code, but Fractal's cross-turn session history and JAZ's current REPL history have different capture and persistence boundaries.
- [Letta](../../../../agent-memory-systems/reviews/letta.md) — **compares-with**: compare tool-mediated recall and compaction with programmable complete history; distinguish the review's pinned system from the paper's configured benchmark baseline.
- [ACE](../../../../agent-memory-systems/reviews/ace.md) — **compares-with**: compare a prescribed reflector/curator playbook loop with agent-selected batches and prompt/tool changes, keeping the paper's 42-task ACE adaptation cap visible.
- [RLM walkthrough](../../../../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) — **compares-with**: distinguishes programmatic access to large supplied inputs from access to the agent's own prompt and continuing interaction history.
- [Original paper](https://arxiv.org/abs/2609.26891) — **derived-from**: primary source for the eventual analysis.

## Bidirectional Candidates

- [Context-operation interface](../../../../notes/context-operation-interface-bounds-context-policy.md) → paired ingest — **evidenced-by**: a reader assessing the interface claim gains a concrete recall failure and an intervention that exposes history; this qualifies the claim's application and does not prove a general performance ordering. A future citation needs `(snapshot required)` until relevant quotes are retained.
- [Practical host-language scheduler](../../../../notes/the-practical-scheduler-is-the-host-language.md) → paired ingest — **evidenced-by**: a reader gains a paper-described implementation of returning recursive calls and live-variable state, bounded to the tested in-process setting. Use `(snapshot required)` until grounded quotes exist.

## Reverse-edge Candidates

None beyond the independently justified return links above.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Code complements weights and prompts](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md): correct general background, but the scheduler and history-interface connections give the reader a more specific mechanism.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md): useful neighboring orchestration surface, but less specific than Fractal for history access; avoid a broad harness list.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md): potential source example for the returning-call and host-language orchestration cluster.
- [Context engineering](../../../../tags/context-engineering-README.md): potential example of history exposure and selective projection; membership is a future editorial decision.

## Synthesis Opportunities

None. Existing interface and scheduler notes already own the main abstractions.

## Maintenance Observations

- The unified-calling note states that uniform calling requires name-based dispatch. JAZ supplies a candidate challenge to that necessity claim through object-valued callable arguments, but the exact refactoring property would need investigation before revising the note.

## Flags

- Keep in-process history retention distinct from cross-restart persistence.
- Connections are candidates only. No library links were authored by this pass.
