---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/bounded-context-orchestration-model.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: Bounded-context orchestration model

**Source:** [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md)

## Discovery Trace

**Collection rules and curated heads:**

- Read `kb/notes/COLLECTION.md`; it authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`, excludes `kb/work/`, and reserves `external` for already-known targets. Its labels permit ordinary theory edges within notes, evidence and lineage edges to descriptive collections, and rare `operationalized-from` edges to instructions.
- Read `kb/notes/README.md`, `kb/notes/computational-model-README.md`, and the destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The `computational-model` head is selective rather than `complete`, so the by-tag `rg` sweep was required.
- Follow-up traversal read `kb/notes/context-engineering-README.md` and `kb/notes/tool-loop-README.md`. The source is already in the computational-model head and already linked from the tool-loop head; neither produced a missing index membership.

**Complete title and description surfaces:**

- Generated the complete fresh title surface for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over each of those destinations. The relevant descriptions clustered around host-language scheduling, run-state persistence, semantic overflow, coordination/aggregation, code-grounded dynamic workflows, and scheduler/scaling papers. The types destination had no plausible trigger; reference and agent-memory matches were implementation-local or subsystem-level rather than clearer instances of the source model.
- Ran the tag-specific description scan `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. It surfaced the host-language scheduler, run-state/strategy persistence, semantic-overflow scheduling, design-space, aggregation, chat-history, feasibility, and intermediate-regime candidates.

**Body search:**

- `rg -n -i 'orchestrat|schedul|select.?call|bounded call' kb/<destination>/ --glob '*.md'` — kept only matches that developed the source's state/selection model, its comparison rule, or its parallel-merge boundary; generic uses of “orchestrator” and “scheduler” were rejected.
- `rg -n -i 'explicit (scheduler )?state|resumable|state projection|completed call|call completes' kb/<destination>/ --glob '*.md'` — confirmed the host-language/reified-state boundary and the code-grounded dynamic-workflows mapping; reference review state and unrelated persistence mechanisms did not pass the articulation test.
- `rg -n -i 'invariant|objective|comparison criter|feasib' kb/<destination>/ --glob '*.md'` — kept the controlled scaling report because it supplies actual comparison dimensions; rejected generic validation invariants and the heaviest-fork specialization as recoverable through existing source links.
- `rg -n -i 'streaming|event-driven|mutable environment|parallel.{0,40}(merge|arbitrat)|arbitrat' kb/<destination>/ --glob '*.md'` — kept the synthesis-versus-selection rule for completed parallel calls; no event-driven extension of the model was found.
- `rg -n '\]\([^)]*bounded-context-orchestration-model\.md\)|bounded-context orchestration model|select/call'` across all authorised destinations established the existing inbound neighborhood and prevented proposing duplicate target-side edits.
- External prospecting was skipped. No new external target was supplied, and the collection contract treats `external` as authorisation for sources already in hand rather than a search surface.

**Link following:**

- Followed the source's existing links through `any-symbolic-program-with-llm-calls`, `decomposition-heuristics`, `llm-mediated-schedulers`, `tool-loop`, `agent-runtime-analysis`, and `topology-isolation-and-verification`. Their neighborhoods exposed narrower consequences while also showing which routes the source already supplies.
- Read the full bodies of the host-language scheduler, persistence-economics, semantic-overflow, design-space, synthesis/error-correction, feasibility, intermediate-regime, stateful-tool, cross-task-transition, and conversation/refinement notes. The retained candidates below add a distinct reader destination; the rejected ones either duplicate an existing route or specialize another already-linked note.
- Read the full Claude Code dynamic-workflows analysis and the scheduler-theoretic, controlled-scaling, and λ-RLM ingest reports. These were evaluated as shipped, formal-design, controlled-empirical, and formal-plus-benchmark evidence respectively rather than treated as interchangeable authority.
- Read the outbound rules of `instructions`, `sources`, `agentic-systems`, `agent-memory-systems`, `reference`, and `types` before evaluating reverse edges. The full-pass procedure was also read in full because notes→instructions is exceptional and requires the procedure to add concrete ordering, defaults, or stopping conditions.
- Verified every retained and rejected path with filesystem existence checks before writing this report.

## Connections Found

- [The practical scheduler is the host language, not a reified select](../../../../notes/the-practical-scheduler-is-the-host-language.md) — **extends**: turns the abstract `select(K)` normal form into a minimal returning-call API and states the lifetime and capacity conditions that force operative `K` to become external, checkpointable state.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — **extends**: applies the model's `select`/`K` split to cross-task lifecycles, distinguishing reusable scheduling policy from task-specific accumulated state.
- [Semantic sub-goals that exceed one context window become scheduling problems](../../../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — **extends**: develops the model's recursive-decomposition remark into the specific overflow condition that forces symbolic partition, collection, and staged aggregation.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) — **extends**: supplies the decision rule behind the model's brief parallelism case—redundant calls require selection or voting, while complementary calls require assembly.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — **extends**: places scheduler location inside a larger comparison surface of persistence, coordination form, guarantees, policy representation, and return artifacts, sharpening the source's warning that the normal form does not rank architectures.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — **evidenced-by**: gives a code-grounded shipped mapping in which `agent()` is the bounded call, JavaScript control flow is `select`, and script variables plus the resume journal carry `K`, while documenting which control decisions the runtime withholds.
- [Ingest: A Scheduler-Theoretic Framework for LLM Agent Execution](../../../../sources/scheduler-theoretic-framework-llm-agent-execution.ingest.md) — **evidenced-by**: independently formalises policy over a ready set, non-deterministic LLM nodes, and explicit state transition, while adding ready-set cardinality as vocabulary for the parallelism case; it is design support, not empirical validation.
- [Ingest: Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **evidenced-by**: controlled comparisons show that extra bounded calls help or hurt according to decomposability, verification, aggregation, and coordination overhead, supporting local strategy comparison under stated criteria rather than a global ordering.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — **operationalized-from**: the procedure fixes concrete ordering, isolation, state capture, barriers, merge ownership, and stopping rules for a parent coordinating bounded reviewer calls—choices the general model deliberately leaves open.

## Bidirectional Candidates

None. Each retained note and the dynamic-workflows analysis already carries an independently useful link to the source; no additional target-side edit is needed.

## Reverse-edge Candidates

None. The strongest descriptive and source candidates already link to the source. Instruction-side `rests-on` was considered under the collection's usual inverse posture, but the full-pass relationship is more useful in the authorised source→instruction direction because it exposes a concrete operationalization to a theory reader.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) — a genuine intermediate regime, but the source already routes readers to the broader LLM-mediated-scheduler boundary and to the conjectural error-correction mechanism; another source edge would mostly duplicate those paths.
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) — a valid downstream rule, but it is already recoverable through the source's `llm-mediated-schedulers`, context-efficiency, and tool-loop links.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../../../notes/feasibility-is-the-heaviest-forks-net-load.md) — a genuine specialization, but the current context-efficiency, soft-degradation, and decomposition-heuristics chain already routes a reader to the per-fork result.
- [Full-identity keys decouple a batch protocol from its packing axis](../../../../notes/full-identity-keys-decouple-a-batch-protocol-from-its-packing-axis.md) — useful for one batched protocol, but its identity-key claim is not a general requirement of the source model's parallel-call case.
- [Deterministic write-context assembly](../../../../reference/proposals/deterministic-write-context-assembly.md) — uses deterministic context assembly in a project-local design, but neither tests nor uniquely instantiates the general select/call model.
- [Tendril](../../../../agent-memory-systems/reviews/tendril.md) — its retained capability registry concerns tool discovery and execution authority; it is a weaker scheduler instance than the code-grounded whole-system analysis retained above.
- [Ingest: The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) — strong formal and benchmark evidence for typed symbolic control over bounded leaves, but redundant here with the source's existing clean-model examples plus the retained scheduler-theoretic and controlled-scaling reports.
- [Evaluate scenarios](../../../../instructions/evaluate-scenarios/SKILL.md) — operationalizes the downstream heaviest-fork feasibility claim, which it already cites, rather than the broader select/call model.

## Index Membership

None. The source is already curated in the computational-model head and already linked from the tool-loop head; the context-engineering head deliberately routes through the computational-model index and the narrower semantic-overflow note.

## Synthesis Opportunities

None. The apparent higher-order claim across the host-language scheduler, persistence economics, and dynamic workflows—run-state and reusable scheduling policy have different lifecycles—is already owned by the persistence-economics note.

## Maintenance Observations

None.

## Flags

- **Possible split candidate:** the retained connections cross more than three areas and expose two independently citable commitments: the select/call normal form and the rule that strategy comparisons require preserved invariants plus an ordering criterion. A future writer should test whether the comparison commitment can stand as its own note without making the normal-form note less useful; this report does not recommend an automatic split.
