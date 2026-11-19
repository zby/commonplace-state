---
description: "Discovery report for possible KB connections from Software Factories: Emerging Architectures and Why Frontier Labs Should Care"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/software-factories-emerging-architectures-a-2094075909242294713.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Software Factories: Emerging Architectures and Why Frontier Labs Should Care

**Source:** [Software Factories: Emerging Architectures and Why Frontier Labs Should Care](../../../../sources/.snapshots/software-factories-emerging-architectures-a-2094075909242294713.md)

The snapshot is immutable. The candidates below are for its authored companion ingest report.

## Discovery Trace

**Description listing scan:**

- Read the curated heads for `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. No `x-article-README.md` exists for the snapshot's tag.
- Generated the full title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each authorised local destination. The main candidate clusters were orchestration topology, scheduler/context/state separation, active work state, session boundaries, verification, whole-system analyses, and prior software-factory sources.
- Enumerated descriptions with `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`, filtered by `software factor|outer loop|orchestrat|ephemeral|isolat|durable state|work state|session|verification|reviewer|acceptance criteria|human checkpoint|autonom|worker|sandbox|permission|workflow|replaceab|commodit|agent harness|factory`. This surfaced the runtime-analysis and orchestration-design notes, Swamp and Compound Engineering analyses, workflow-memory reviews, and the existing factory/harness ingest cluster.
- Reference hits mostly describe Commonplace's own review subsystem. `review-architecture.md` and ADR 067 resemble the post's bounded-worker pattern, but a system-specific `see-also` edge would not give a reader enough beyond the transferable notes, so they were rejected.

**Topic indexes:**

- Read `kb/notes/computational-model-README.md` and `kb/notes/tool-loop-README.md`. They supplied the scheduler-placement, bounded-worker, persistence, and boundary-return vocabulary.
- Read `kb/notes/llm-reliability-README.md`, `kb/notes/evaluation-README.md`, and `kb/notes/observability-README.md`. They supplied the verification-boundary and independent-check candidates.
- Read `kb/notes/agent-memory-README.md` and `kb/agent-memory-systems/README.md`. They separated live work state and workflow memory from session history.
- Read `kb/agentic-systems/README.md` and `kb/sources/README.md`. Swamp, Compound Engineering, and Claude Code dynamic workflows passed the whole-system comparison test; prior software-factory and durable-harness ingests supplied the strongest source comparisons.

**Body search:**

- `rg -n -i 'software factor(y|ies)|outer loop|factory owns|automation loop' ...` found the three-part Horthy series, Fluent, and the outer-loop runtime notes.
- `rg -n -i 'ephemeral (worker|agent)|disposable worker|work state|run state|session history|state.*outside.*agent|outlive.*worker|worker.*execution unit' ...` found the active-work-state, session-history, persistence-economics, repo-centric-stack, and long-running-harness candidates.
- `rg -n -i 'independent review|acceptance criteria|verification.*stage|review and verification|generat.*implementation.*correct|boundary of automation|human checkpoint' ...` found the topology/isolation/verification and automation-boundary notes plus the Fluent and Horthy comparisons.
- `rg -n -i 'commodit|replaceable worker|worker replaceab|interchangeable worker|outer.loop ownership|open stack|integrated stack|model.*harness.*factory' ...` found no existing note that captures the post's platform-power claim about factory owners routing work among interchangeable workers.

**Link following:**

- Followed the runtime-separation note into bounded orchestration and inspectable external state. The post independently maps factory responsibility onto scheduling, per-worker context, and external state/action services.
- Followed the orchestration-design-space note into persistence horizons, coordination guarantees, and return artifacts. The post supplies several real product configurations without establishing that its six patterns are exhaustive.
- Followed the active-work-state and session-history notes into workstream closure and clean handoff. The post's work items, branches, acceptance criteria, and independent reviewer are current-state artifacts rather than inherited conversation.
- Followed the topology/isolation/verification note into its causal caveat. Foreman and Fluent show all three mechanisms coexisting, but the post does not vary them independently and therefore cannot establish the proposed dependency chain.
- Followed the software-factory-failure source to its lights-back-on and SlopCodeBench continuations. They supply the adverse and human-steered cases missing from this post's market survey.
- Followed the Compound Engineering and Swamp whole-system analyses to their memory-subsystem reviews. Their inspected implementations show how durable workflow artifacts and operational state can underwrite the post's more abstract factory pattern.

## Connections Found

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **is-evidence-for**: the post independently describes the factory as owning progression, worker context and permissions, and durable external work state while the model supplies bounded semantic work.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **is-evidence-for**: Factory, Warp, and Foreman vary across scheduler ownership, worker configuration, persistence, coordination form, and review artifacts rather than forming one autonomy ladder.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **is-evidence-for**: work items, repositories, branches, acceptance criteria, shared knowledge, and eval results preserve what is live after any disposable worker ends.
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- **is-evidence-for**: Foreman's independent reviewer consumes the branch and acceptance criteria without inheriting the implementer's conversation, making the handoff artifact rather than transcript the interface.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- **is-evidence-for**: the surveyed factories co-locate staged decomposition, isolated workers, and independent review; this supports coexistence in deployed designs but does not test the note's causal ordering.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **is-evidence-for**: the post treats verification as a core factory function and observes that shipped or previewed systems still stop at selected human checkpoints instead of providing end-to-end autonomous completion.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) -- **compares-with**: the post separates disposable worker sessions from versioned factory definitions and durable work state, while the note further distinguishes cross-task strategy value from task-specific run-state value.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- **compares-with**: Swamp is an inspected instance of the post's control-plane pattern, with declarative DAGs, centrally retained state and policy, remote disposable workers, approval gates, reports, and audit.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: the analysis classifies an inspected human-inclusive, artifact-mediated software factory whose workflow, evaluation, and retention boundaries can test the post's cross-vendor synthesis.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: its model-authored, session-local orchestrator is a useful contrast to factory-owned persistent outer loops, while its isolated sub-agents and independent return artifacts instantiate the worker layer.
- [Compound Engineering Plugin memory-system review](../../../../agent-memory-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: the code-grounded review shows the workflow-shaped repository memory beneath one software factory, including strategy, plans, solutions, review artifacts, and routed read-back.
- [Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) -- **compares-with**: both reject the finished-software-without-supervision fantasy, but Horthy supplies a failed lights-off deployment and a maintainability-oracle mechanism rather than a market architecture survey.
- [Why Software Factories Fail: Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md) -- **compares-with**: Horthy's staged human reviews and short vertical slices give one concrete operating shape for the post's claim that present factories relocate rather than remove human judgment.
- [How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) -- **compares-with**: Fluent supplies a detailed alternative with shaped work items, isolated attempts, deterministic testing, independent reviewers, and retained expertise.
- [Building a Repo-Centric Modular Agent Stack](../../../../sources/building-a-repo-centric-modular-agent-stack-2085784422339768686.ingest.md) -- **compares-with**: it makes the governed project substrate and explicit role contracts the basis for replacing models, sessions, and interfaces, closely matching the post's externalized-state and interchangeable-worker pattern.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) -- **compares-with**: Anthropic's practitioner report gives a narrower implementation of work continuity across fresh sessions through requirements, progress state, commits, and end-to-end checks.
- [The Agent Loop Architecture](../../../../sources/the-agent-loop-architecture-2067677007140278630.ingest.md) -- **compares-with**: this source names the durable outer production loop around model/tool cycles and separates checkpointed run-state, reusable skills, and diagnostic history that the factory post groups together.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. Durable reverse links should target the tracked ingest after it exists, never this ignored snapshot.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- the post says humans remain at selected checkpoints but provides no workload, effort, or intervention-frontier evidence needed for the note's stronger claim.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- the post strongly supports a whole-system capability boundary, but it does not show an evidence-responsive learning loop over the whole deployed system.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- the post lists permissions, sandboxes, and review stages but does not identify which guarantee prevents which cross-worker failure.
- [Echel](../../../../agent-memory-systems/reviews/echel.md) -- its task packets and evidence gates articulate the same state/handoff family, but the repo-centric-stack and active-work-state candidates provide a more direct traversal route for this source.
- [What is an Agent Harness](../../../../sources/what-is-an-agent-harness-2046980769747533830.ingest.md) -- its nine-part harness taxonomy overlaps the post's worker layer, but the runtime-separation note and inspected whole-system comparisons make the architectural relation more precise.
- [Why Software Factories Fail: Benchmarking the new frontier](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) -- useful empirical continuation, but already reachable from the stronger Part I and Part II comparison edges and too detailed for this architecture survey's authored surface.
- [Review system architecture](../../../../reference/review-architecture.md) -- Commonplace's parent-owned dispatch and hermetic workers are a local analogue, but a direct reference link would expose implementation detail without improving the general architectural comparison.

## Index Membership

None

## Synthesis Opportunities

- The post, [Building a Repo-Centric Modular Agent Stack](../../../../sources/building-a-repo-centric-modular-agent-stack-2085784422339768686.ingest.md), and the open-stack comparisons suggest a claim not yet represented in the KB: control of the outer loop can create platform power by controlling task routing, state, permissions, evaluation, and the choice among otherwise replaceable model-and-harness workers. This needs evidence across integrated and open factories before promotion.

## Maintenance Observations

None

## Flags

- Split candidate: the source makes independent claims about orchestration topology, worker lifecycle, durable state, vendor-stack integration, verification, present autonomy limits, and frontier-lab strategy. An ingest can retain the survey as one source record, but later theory extraction should not force all seven into one note.
