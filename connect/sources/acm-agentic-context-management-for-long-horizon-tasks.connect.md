---
description: "Discovery report for possible KB connections from ACM: Agentic Context Management for Long Horizon Tasks"
type: kb/cache/types/connect-report.md
source: "kb/sources/acm-agentic-context-management-for-long-horizon-tasks.md"
source_has_frontmatter: true
date: "2026-07-30"
depth: standard
---

# Connection Report: ACM: Agentic Context Management for Long Horizon Tasks

**Source:** [ACM: Agentic Context Management for Long Horizon Tasks](../../../sources/acm-agentic-context-management-for-long-horizon-tasks.md)

## Discovery Trace

**Collection contract:** Read `kb/sources/COLLECTION.md`. It authorizes prospecting in notes, reference, agent-memory systems, agentic systems, and other sources; it excludes instructions and work. The snapshot is immutable, so accepted outbound candidates belong on its ingest companion. Open-web prospecting was skipped; the paper and repository already named by the source were not treated as local candidates.

**Full title listings:** Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`. Context, memory, compression, retrieval, token-pressure, long-horizon, search, and coding matches led to the candidate set below. The source has no `tags`, so no by-tag README or by-tag `rg` pass applied.

**Curated heads:** Read `kb/notes/README.md`, the context-engineering and agent-memory tag READMEs, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes heads pointed to context scarcity, evidence preservation, activation, and memory-policy learning. The agent-memory head pointed to AgeMem; the full-system and reference heads supplied no direct candidate.

**Description listing scan:** Ran `rg -n '^description:.*(context|memory|compress|long-horizon|token|retriev|offload|summar|agent)' kb/<destination> --glob '*.md'` and filtered for management, working context, long horizons, token pressure, retrieval, offload, summary, memory policy, context windows, active work, and trajectories. Kept the notes and system comparisons below. Rejected generic retrieval systems and broad memory surveys whose overlap stopped at vocabulary.

**Body search:** Ran `rg -l -i 'agent-initiated|context management|manage_context|query_memory|compression timing|working context|external memory|peak token|long-horizon|long horizon' kb/<destination> --glob '*.md'` across every authorized local destination. This surfaced the same notes cluster plus AgeMem, Letta, Virtual Context, Faithful Self-Evolvers, Effective Harnesses, and several weaker long-context sources.

**Link following:** Followed the memory-policy note to AgeMem; the activation note to Faithful Self-Evolvers; the evidence-preservation note to session-history and active-work distinctions; and AgeMem/Virtual Context into their read-back, policy, and raw-evidence sections. A targeted follow-up used `rg -n '^# |^description:' kb/notes --glob '*.md' | rg -i 'decompos|proxy theor|vision feature|composition'`, then followed the reciprocal decomposition cluster through `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` and `only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md`. This established three useful comparison axes: learned versus engineered trigger policy, archival recoverability versus faithful contextual activation, and local policy success versus warrant for the hand-chosen task decomposition.

**Destination evaluations:** `kb/reference/` had no shipped Commonplace analogue specific enough to help a reader. `kb/agentic-systems/` had no whole-system analysis matching this subsystem-level paper. In `kb/sources/`, the AgeMem snapshot duplicated the stronger curated lightweight review, Paulsen only supplied upstream motivation already absorbed by notes, and λ-RLM solved long context through recursive decomposition rather than in-episode memory tools.

## Connections Found

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **is-evidence-for**: ACM supplies an independent learned-policy case whose dual teacher constraints require reference-answer and trajectory-quality signals to teach both when to compress and when not to compress.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **is-evidence-for**: ACM jointly tests one hand-chosen `manage_context`/`query_memory` split and a controller trained inside it, so success establishes local sufficiency without discriminating that split from the discarded alternatives.
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) -- **is-evidence-for**: the paper motivates its split by a short-term/long-term-memory analogy but neither derives the two operations from independently supported constraints nor tests them against rival decompositions, leaving the broader scope claim unwarranted.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) -- **is-evidence-for**: `manage_context` removes raw turns from the working set while keeping them addressable on disk through summary identifiers and `query_memory`.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **is-evidence-for**: ACM lowers peak active-context pressure and enables longer exploration, while its higher tool counts make the note's distinction between per-window feasibility and aggregate cost especially useful.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: access to the two memory tools was not enough for GPT-5.5 to invoke them often; dedicated training changed the management behavior, illustrating the gap between an available path and an activated one.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **compares-with**: ACM calls its offloaded per-question turn history long-term memory, but the material remains episode-local active evidence and lacks the cross-session pointers, gates, and closure semantics of active work state.
- [AgeMem](../../../../agent-memory-systems/lightweight/agemem.md) -- **compares-with**: both systems learn when to invoke hand-designed memory operations, but ACM concentrates on within-episode compression/retrieval with dual teacher annotations while AgeMem jointly manages cross-task LTM and STM through RL rewards.
- [Virtual Context](../../../../agent-memory-systems/reviews/virtual-context.md) -- **compares-with**: both keep raw traces addressable behind compact views and paging tools; Virtual Context uses proxy-owned threshold/retrieval policy with push and pull paths, whereas ACM makes compression an agent action and trains its timing.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with**: the faithfulness study warns that condensed experience can lose behavioral influence; ACM preserves raw turns for retrieval but does not thereby prove that its lossy working summaries or recall decisions preserve equivalent activation.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) -- **compares-with**: ACM addresses continuation within one long episode, while Anthropic's harness report shows that cross-window work continuation additionally needs explicit progress state, requirements, and verification rather than conversational compaction alone.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) → source -- **evidenced-by**: ACM is a second paper-level case of a learned controller over fixed memory operations and makes its teacher/oracle dependency unusually explicit.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) → source -- **evidenced-by**: ACM is a worked case where end-to-end gains verify one decomposition locally while leaving its rejected alternatives and transfer conditions untested.
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) → source -- **evidenced-by**: the two-tool ontology is a free-choice decomposition that earns pragmatic local value but no broader scope from evaluations that hold it fixed.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) → source -- **evidenced-by**: ACM implements the capture/loading split within a trajectory by archiving raw turns while keeping only summaries active.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) → source -- **evidenced-by**: the three-benchmark results and context-growth study provide direct evidence for reducing the per-window feasibility burden, with tool-count increases exposing the separate aggregate-cost face.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: near-zero context-tool use by an untrained strong model and greater use after dedicated training show that tool availability alone does not activate memory management.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Letta](../../../../agent-memory-systems/reviews/letta.md) -- genuine architectural overlap, but Virtual Context is the sharper same-mechanism comparison because it retains raw turns alongside compacted working views and exposes restoration paths.
- [Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for LLM Agents](../../../../sources/agentic-memory-learning-unified-long-term-and-short-term.ingest.md) -- duplicate comparison surface; the curated AgeMem lightweight review already carries the system-level judgment.
- [Maximum Effective Context Window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- supports ACM's motivation but adds little traversal value beyond the existing context-efficiency and soft-degradation notes.
- [The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) -- both address long context, but λ-RLM's recursive typed decomposition is a different mechanism and the comparison would be too broad without a focused synthesis question.

## Index Membership

None.

## Synthesis Opportunities

The source, [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and [Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) jointly imply a sharper claim: preserving the raw archive makes compression *recoverable*, not lossless at the active-context level. A summary can omit behaviorally decisive material, and a retrieval tool can remain unused or return an incomplete projection. “Lossless” should therefore be reserved for the storage path unless systematic read-back and activation faithfulness are shown.

The two decomposition notes expose a separate, already-captured methodological diagnosis rather than a new synthesis claim: ACM learns a controller over a freely chosen feature map for context management, while every evaluation holds that map fixed. The source should therefore remain a context-bound worked case until a rival operation set or constraint-changing intervention makes the decomposition itself refutable.

## Maintenance Observations

None.

## Flags

- Split candidate: the paper independently bears on context economics, memory activation, active-work taxonomy, and feedback-trained policy learning; promotion should select one claim rather than collapse all four into a broad ACM note.
- Scope warning: benchmark success tests the learned controller and the two-tool decomposition as one conjunction; it does not warrant transferring that decomposition as a general account of context management.
- Terminology tension: the paper's “lossless compression” means raw turns remain recoverable from external storage, while the in-context summary and on-demand query path are still selective and potentially lossy.
