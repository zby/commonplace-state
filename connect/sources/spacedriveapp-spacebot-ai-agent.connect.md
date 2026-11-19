---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/spacedriveapp-spacebot-ai-agent.md"
source_has_frontmatter: true
date: "2026-04-20"
depth: standard
---

# Connection Report: Spacebot: AI Agent for Teams and Communities

**Source:** [Spacebot: AI Agent for Teams and Communities](../../../sources/spacedriveapp-spacebot-ai-agent.md)

## Discovery Trace

**Index scan:**
- Read [sources index](../../../sources/dir-index.md) -- flagged [Spacebot ingest](../../../../sources/spacedriveapp-spacebot-ai-agent.ingest.md) as the companion analysis artifact and [What Survives in Multi-Agent Systems](../../../../sources/voooooogel-multi-agent-future.ingest.md) because it already mentions Spacebot as the closest production forking example.
- Read [notes index](../../../notes/dir-index.md) -- flagged [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [agent runtimes decompose into scheduler context engine and execution substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md), [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md), [agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md), [three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md), and [flat memory predicts specific cross-contamination failures](../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md).
- Read [agent memory systems index](../../../agent-memory-systems/dir-index.md) and [reviews index](../../../agent-memory-systems/reviews/dir-index.md) -- flagged [Spacebot](../../../../agent-memory-systems/reviews/spacebot.md) as the now-durable downstream review and [agentic memory systems comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) as the collection-level synthesis this system extends.
- Scanned [instructions files](../../../instructions/dir-index.md) by listing `kb/instructions/**/*.md` -- no durable instruction target was kept; Spacebot is descriptive source material rather than an operation this KB can execute directly.

**Topic indexes:**
- Source frontmatter tags are `[web-page]`, which has no curated tag index. Read [computational model](../../../notes/computational-model-index.md) because the snapshot's process/cortex architecture maps to scheduler and scoping notes. Kept the scheduler, runtime-decomposition, tool-loop, context-efficiency, and scoping cluster; rejected generic prompt/programming notes that do not gain from this source.
- Read [tool loop](../../../notes/tool-loop-index.md). Kept it as index membership only: Spacebot illustrates exposed sub-loops and symbolic orchestration, but the more precise durable targets are the bounded orchestration and scoping notes.

**Semantic search:** qmd unavailable for this run. `command -v qmd` returned `/home/zby/.npm-global/bin/qmd`, but `qmd --index "$COMMONPLACE_QMD_INDEX" update` failed with `SqliteError: unable to open database file` for index `commonplace`; used grep-only fallback.

**Keyword search:**
- `rg -n "Spacebot|spacebot|cortex|branch|branches|worker|workers|compactor|message coalescing|model routing|memory bulletin|hybrid recall|Reciprocal Rank Fusion|concurrent|non-blocking|multi-user" kb/ --glob "*.md"` -- found the target snapshot, the existing Spacebot review, the prior ingest, the multi-agent-future ingest, and workshop references. Kept the review and multi-agent-future ingest; rejected workshop-only references as non-durable context for this source ingest.
- `rg -n "scheduler|orchestration|bounded|scoping|scope|context efficiency|memory|flat memory|three-space|Tulving|agent runtimes|coordination" kb/notes kb/agent-memory-systems kb/sources --glob "*.md"` -- found the scheduler, context efficiency, scoping, runtime decomposition, orchestration design-space, and memory-separation notes. Kept candidates whose mechanism is instantiated by the snapshot; rejected broad learning-theory and runtime notes where the match was only vocabulary overlap.

**Link following:**
- Followed [Spacebot review](../../../../agent-memory-systems/reviews/spacebot.md). Its relevant notes identify the same core cluster and add stronger evidence from code inspection: process-type separation, Rust-owned scheduling, branch isolation, compaction thresholds, typed unified memory, message coalescing, memory bulletin, and model routing.
- Followed [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) to [LLM-mediated schedulers are a degraded variant of the clean model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), [tool loop](../../../notes/tool-loop-index.md), and [topology, isolation, and verification form a causal chain](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md). Kept the clean-model and topology/isolation implications; rejected LLM-mediated scheduling as a primary target because Spacebot mostly bypasses that failure mode rather than contradicting a specific note.
- Followed [three-space agent memory](../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) to [flat-memory failure predictions](../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md). Kept both because Spacebot's typed unified memory is a concrete middle-ground test case.

## Connections Found

- [Spacebot](../../../../agent-memory-systems/reviews/spacebot.md) -- **grounds**: the snapshot is the source artifact for the durable related-system review; the review expands the README's architectural claims with code-level findings and should be the preferred downstream traversal target.
- [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -- **exemplifies**: Spacebot's cortex/process architecture is a concrete instance of symbolic scheduling over bounded LLM calls, with channels and branches as bounded contexts and workers as deterministic execution.
- [agent runtimes decompose into scheduler context engine and execution substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) -- **exemplifies**: Spacebot visibly separates scheduler (cortex), context engine (branches, compactor, memory bulletin), and execution substrate (shell/file/browser/code workers).
- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) -- **exemplifies**: branches fork channel context into independent frames and return only a conclusion, giving a production example of architectural scoping rather than flat context accumulation.
- [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **exemplifies**: Spacebot attacks both volume and complexity costs through message coalescing, compaction, branch isolation, model routing, and memory bulletins.
- [agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **extends**: Spacebot adds a point where scheduler placement, process-type isolation, coordination form, and boundary-return artifact are all explicit runtime choices, not just prompt roles.
- [three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy-may-be-decorative.md) -- **extends**: Spacebot's typed-but-unified memory occupies a middle position between flat memory and separate knowledge/self/operational spaces.
- [flat memory predicts specific cross-contamination failures that are empirically testable](../../../notes/flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) -- **enables**: Spacebot offers a concrete test case for whether typed categories and graph edges inside one store mitigate search pollution, identity scatter, and insight trapping.

## Bidirectional Candidates

- [Spacebot](../../../../agent-memory-systems/reviews/spacebot.md) <-> source -- **grounds**: the review should retain this source as provenance for its README-level claims.
- [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) <-> source -- **exemplifies**: a future revision could add Spacebot as a production exemplar, preferably pointing to the review rather than the raw snapshot.
- [agent runtimes decompose into scheduler context engine and execution substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md) <-> source -- **exemplifies**: Spacebot gives unusually clean component boundaries for the runtime taxonomy.

## Raw Text Candidates

None

## Rejected Candidates

- [tool loop](../../../notes/tool-loop-index.md) -- useful index neighborhood but too broad as a direct connection; Spacebot connects more specifically through bounded orchestration, runtime decomposition, and scoping.
- [What Survives in Multi-Agent Systems](../../../../sources/voooooogel-multi-agent-future.ingest.md) -- already mentions Spacebot as the closest production forking example, but the relationship is better handled by that ingest's own discussion than by making this source a separate durable target.
- [agent orchestration needs coordination guarantees, not just coordination channels](../../../notes/agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) -- plausible but weaker than the design-space note; the snapshot shows isolation and process separation, but does not analyze the guarantee taxonomy.
- [topology, isolation, and verification form a causal chain for reliable agent scaling](../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) -- relevant by implication, but the snapshot does not discuss verification, so the connection would overstate the source's evidence.

## Index Membership

- [related systems](../../../../agent-memory-systems/README.md) -- Spacebot belongs as an external related system; this is now satisfied by [the Spacebot review](../../../../agent-memory-systems/reviews/spacebot.md).
- [computational model](../../../notes/computational-model-index.md) -- Spacebot is a concrete runtime example for scheduler placement, scoping, and context-efficiency mechanisms.
- [tool loop](../../../notes/tool-loop-index.md) -- Spacebot helps illustrate when a framework exposes sub-loops and symbolic orchestration, but the index should probably route through the Spacebot review rather than this snapshot.

## Synthesis Opportunities

- Spacebot, Slate, and the bounded-context orchestration notes support a synthesis that production agent frameworks are converging on code-owned scheduling plus bounded, isolated LLM calls, with variation in what returns across the boundary.
- Spacebot's typed unified memory, three-space memory separation, and flat-memory failure predictions suggest a more precise middle-ground hypothesis: type labels and graph edges may mitigate some flat-store failures without requiring physically separate memory spaces, but only if retrieval and promotion policies use those labels.

## Flags

- Load-bearing links to [bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [agent runtimes decompose into scheduler context engine and execution substrate](../../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution-substrate.md), [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md), and the memory-separation notes point to seedling/speculative notes. Treat Spacebot as evidence/example, not proof that those theories are settled.
- The dedicated [Spacebot review](../../../../agent-memory-systems/reviews/spacebot.md) is now the preferred durable analysis target; the ingest report should avoid duplicating review-level code claims not present in the snapshot.
