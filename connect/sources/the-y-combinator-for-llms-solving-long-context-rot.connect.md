---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/the-y-combinator-for-llms-solving-long-context-rot.md"
source_has_frontmatter: true
date: "2026-06-11"
depth: standard
---

# Connection Report: The Y-Combinator for LLMs

**Source:** [The Y-Combinator for LLMs](../../../sources/the-y-combinator-for-llms-solving-long-context-rot.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/sources/COLLECTION.md`; snapshots are immutable, so authored connections should land in the adjacent ingest report or as reverse edges from notes.
- `rg '^description:' kb/notes/ --glob '*.md'` -- flagged `rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md`, `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md`, `bounded-context-orchestration-model.md`, `orchestration-strategies-and-run-state-have-opposite-persistence.md`, `scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`, `semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md`, `decomposition-heuristics-for-bounded-context-scheduling.md`, `agent-orchestration-occupies-a-multi-dimensional-design-space.md`.
- `rg '^description:' kb/reference/ --glob '*.md'` -- rejected reference docs except `link-vocabulary.md`/ADRs as methodology background; the source is evidence for theory notes, not shipped-system documentation.
- `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` -- no direct system-review target; λ-RLM is a paper/method rather than a reviewed memory system. Related reviews such as Tendril and dynamic workflow coverage are already mediated through notes/sources.
- `rg '^description:' kb/sources/ --glob '*.md'` -- flagged RLM practitioner ingest, Slate ingest, Claude Code dynamic-workflows ingest, ConvexBench ingest, coding-agents-long-context ingest, and the Mismanaged Geniuses ingest.

**Topic indexes:**
- Read [Tags](../../../../tags/README.md) -- routes this source primarily to computational-model, tool-loop, context-engineering, and agent-memory.
- Read [Links](../../../../tags/links-README.md) -- useful only for report labeling discipline; no direct content connection.
- Read [Reference](../../../../reference/README.md) -- no durable reference-doc update indicated.
- Read [Agent Memory Systems](../../../../agent-memory-systems/README.md) -- source is adjacent to agent-memory/context-engineering system reviews but not a code-inspected related-system candidate.

**Body search:**
- `rg -n "RLM|Recursive Language Models|recursive language|prompt-as-environment|REPL|open-ended|combinator|lambda|λ|fixed-point|Y-combinator|long-context rot|typed functional|symbolic control|bounded leaf|context window|split|reduce" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob '*.md'` -- kept the RLM/orchestration cluster; rejected incidental math `λ` hits and generic split/reduce hits outside orchestration.
- `rg -n "scheduler|context engine|execution substrate|symbolic collection|staged summarization|semantic subgoals|externalized|externalising|scoping|tool loop|decomposition" kb/notes --glob '*.md'` -- kept scheduler/context-engine notes and decomposition heuristics; rejected broad collection/search hits with no typed-control or long-context-recursion mechanism.
- `rg -n "λ-RLM|RLM|Recursive Language Models|long-context|context rot|recursive decomposition|REPL" kb/sources --glob '*.ingest.md'` -- kept source-level comparisons to the RLM practitioner report, Slate, dynamic workflows, ConvexBench, and coding-agents-long-context.

**Link following:**
- From [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md), followed to [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md), [LLM-mediated schedulers are a degraded variant](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md), [Ephemeral computation prevents accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md), and [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md).
- From [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](../../../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md), followed to the persistence-boundary cluster; λ-RLM adds a new point: model-planned but runtime-constrained typed combinators, not free-form ephemeral REPL code and not durable generated tools.
- From dynamic-workflows and Slate ingests, kept source comparisons around saveable orchestrators and bounded worker episodes; rejected as primary note targets because the new paper is closer to RLM's formal runtime than to product-specific orchestration UX.

## Connections Found

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -- **evidence**: the paper directly critiques standard RLM's open-ended model-written REPL control code and proposes λ-RLM as a typed-combinator replacement that preserves prompt-as-environment recursion while making control auditable.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) -- **evidence**: λ-RLM explicitly moves split/map/filter/reduce, recursion depth, and cost accounting onto deterministic symbolic operators while reserving neural inference for bounded leaf calls.
- [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -- **evidence**: the λ-RLM executor is a formal instance of a symbolic scheduler over bounded LLM calls, with planned recursion depth and explicit state outside the model window.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -- **evidence**: the paper supplies formal termination, cost, accuracy, and partition-size claims for recursive splitting under a simple cost model, strengthening the heuristic cluster with a formal candidate.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **evidence**: λ-RLM occupies a distinct design-space point: model-assisted task selection and planning, typed symbolic control, ephemeral per-run execution, and fixed combinator return artifacts.
- [RLM, Tendril, and llm-do place symbolic work at different persistence boundaries](../../../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) -- **evidence**: λ-RLM adds a fourth comparison point where symbolic work is not arbitrary model-written code or durable generated tools but a pre-verified combinator vocabulary selected by a planner.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -> source -- **evidence**: cite λ-RLM as the formal paper that turns the note's open-ended-REPL trade-off into an explicit design alternative.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) -> source -- **evidence**: cite λ-RLM as a direct formalization of the claim that bookkeeping/control should be symbolic while semantic judgment stays in bounded calls.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -> source -- **evidence**: cite the paper cautiously as a formal model for partitioning and recursion bounds; note that its empirical scope is long-context task families, not general KB maintenance work.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -> source -- **evidence**: add λ-RLM as a new point on decomposition-policy artifact and scheduler-placement dimensions.

## Off-authorisation Candidates

- [LLM-mediated schedulers are a degraded variant of the clean model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) -- λ-RLM strongly supports the "factoring into code" recovery strategy, but `sources` outbound labels do not include `extends` or `exemplifies` for notes. Treat this as evidence in the ingest report, or add a reverse-edge evidence citation from the note later.
- [Semantic sub-goals that exceed one context window become scheduling problems](../../../../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) -- λ-RLM is a concrete recursive runtime for this problem shape, but the relation is better authored from the note as an `evidence` edge than from the immutable snapshot.

## Raw Text Candidates

None

## Rejected Candidates

- [Reference README](../../../../reference/README.md) -- rejected: the paper is not a current-state Commonplace system reference.
- [Agent Memory Systems README](../../../../agent-memory-systems/README.md) -- rejected: λ-RLM is relevant to context-engineering systems, but without code inspection it belongs as a source ingest rather than a system review.
- [Slate: Moving Beyond ReAct and RLM ingest](../../../../sources/slate-moving-beyond-react-and-rlm.ingest.md) -- rejected as primary theory target: useful comparison source, but its thread-weaving architecture solves RLM weaknesses differently and should stay as `compares-with` context.
- [Claude Code dynamic workflows ingest](../../../../sources/claude-code-dynamic-workflows-docs.ingest.md) -- rejected as primary theory target: useful persistence contrast, but λ-RLM does not address saveable/reusable orchestrator promotion.
- [ConvexBench ingest](../../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) -- rejected as direct connection: both support recursive decomposition under context limits, but ConvexBench is about compositional reasoning collapse in symbolic function analysis, not RLM control semantics.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- λ-RLM should be considered for future curated coverage of symbolic schedulers, typed control, and LLM orchestration.
- [Tool loop](../../../../tags/tool-loop-README.md) -- λ-RLM is relevant as a restricted-runtime alternative to framework-owned open-ended model loops.

## Synthesis Opportunities

The RLM cluster now has enough material for a synthesis note comparing four placements of model-authored orchestration: standard RLM's arbitrary ephemeral REPL code, λ-RLM's typed pre-verified combinator runtime, Claude Code dynamic workflows' saveable JavaScript orchestrators, and Tendril/llm-do-style durable callable capabilities. The likely claim: restricting the orchestration language is an independent axis from persistence; λ-RLM improves verifiability without solving cross-session accumulation.

## Maintenance Observations

The snapshot contains raw `pdftotext -layout` artifacts and repeated title/author metadata after the frontmatter. This is acceptable for faithful capture, but if PDF capture quality becomes a recurring issue, snapshot tooling should add a cleaner PDF-to-markdown path.

## Flags

- Split candidate for later synthesis, not for this ingest: the source contributes both formal theory (termination/cost/accuracy bounds) and design-space comparison (typed runtime vs open REPL). A later note should decide whether these remain one claim or split into theory/evidence pieces.
