---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/agentic-systems/claude-code-dynamic-workflows.md"
source_has_frontmatter: true
date: "2026-06-12"
depth: standard
---

# Connection Report: Claude Code dynamic workflows

**Source:** [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md)

The source is a descriptive analysis in `kb/agentic-systems/` (register: descriptive, goal fidelity + economy). Its `COLLECTION.md` outbound section authorises four destinations:

- `→ kb/sources/` — `derived-from`, `evidence`, `see-also`
- `→ kb/notes/` — `rationale`, `see-also`; **"links usually run inverse (theory links in via `evidence`)"** — so reverse edges from theory notes are first-class here
- `→ kb/agent-memory-systems/` — `part-of`/`contains`, `compares-with`, `see-also` (only when the analysed system has a memory subsystem reviewed there)
- `→ kb/reference/` — `see-also` (only when a design element has a direct Commonplace analogue)

The source is already densely linked (7 footer links + several inline). Outbound capacity to `notes` is deliberately narrow per the contract, so most of the new signal below is **reverse-edge** candidates: theory notes that should cite this shipped instance.

## Discovery Trace

**Curated heads:**
- `kb/agentic-systems/README.md` — source is the only analysis listed; no sibling candidates.
- `kb/notes/tool-loop-README.md` — the cluster hub. Already cross-links the source bidirectionally ("shipped instance" entry under Related approaches). No `complete:`/`covered_by:` marks present, so by-tag rg was run.
- `kb/notes/computational-model-README.md` — Scheduling & Orchestration cluster. No `complete:` mark; by-tag rg run.
- `kb/agent-memory-systems/README.md` — scanned; coverage is memory-subsystem reviews only, no orchestration/workflow surface. Destination trigger does not fire — skipped.

**Description listing scan (by tag, notes destination):**
- `rg -l '^tags:.*\btool-loop\b' kb/notes/ | xargs rg '^description:'` — 12 notes; source already links 7 of the relevant ones. New unlinked candidates flagged: `the-chat-history-model-trades-context-efficiency-for-implementation`, `stateful-tools-recover-control-by-becoming-hidden-schedulers`, `codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers`, `apparent-success-is-an-unreliable-health-signal-in-framework-owned`.
- `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ | xargs rg '^description:'` — ~40 notes. New candidates flagged: `any-symbolic-program-with-llm-calls-is-a-select-call-program`, `agent-orchestration-occupies-a-multi-dimensional-design-space`, `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence`, `agent-runtimes-decompose-into-scheduler-context-engine-and-execution`, `feasibility-is-the-heaviest-forks-net-load`.

**Body search:**
- `rg -l 'agentic-systems/claude-code-dynamic-workflows' kb/notes/` — existing reverse edges already present in: `llm-frameworks-should-keep-the-tool-loop-optional` (evidence), `orchestration-strategies-and-run-state-have-opposite-persistence` (evidence), `tool-loop-README` (see-also). These are not new.
- `rg -l 'worktree' kb/notes/ kb/reference/` — `kb/reference/review-architecture.md` (worktree in review subsystem); evaluated for the `→ reference` "direct Commonplace analogue" trigger — see Off-authorisation note. `make-authority-explicit.md` is a memory-requirements note, off-topic.
- `rg -l 'structured.output|validated structured' kb/notes/` — `the-practical-scheduler-is-the-host-language` (already linked); `structured-output-is-easier-for-humans-to-review` is a review-UX note, not orchestration — rejected.
- `rg -l 'token ceiling|budget' kb/notes/` — `feasibility-is-the-heaviest-forks-net-load` flagged (see candidate); others are KB-maintenance/distillation, off-topic.
- `rg -ln 'sub-agent|worktree|dynamic workflow' kb/reference/` — `review-architecture.md`, `available-types.md`, `adr/025`; none is a direct design analogue of the workflows API.

**Link following:**
- From `tool-loop-README` one hop: reached `agent-orchestration-occupies-a-multi-dimensional-design-space` and `any-symbolic-program-with-llm-calls-is-a-select-call-program` — both in the orchestration cluster the source instantiates but does not yet cite.
- From `the-practical-scheduler-is-the-host-language` (already linked): reached `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence`, a placement-of-symbolic-work comparison the source is a natural data point for.

**Sources destination:**
- `rg -l 'workflow|claude code|ultracode' kb/sources/` — the two grounding snapshots (`claude-code-dynamic-workflows-docs.md`, `a-harness-for-every-task-dynamic-workflows.md`) are already linked as `derived-from` / `see-also`. No further source candidates.

## Connections Found

Outbound from the source to `notes` is contract-restricted to `rationale` and `see-also`, and the contract says to prefer promoting a novel claim over authoring theory here. The mapping/argument the source needs is already carried by its existing `rationale`/`see-also` footer. Two additions clear the bar as `see-also` (adjacent companion the reader of this analysis benefits from, without over-spraying a frontloaded-ish descriptive note):

- [any-symbolic-program-with-llm-calls-is-a-select-call-program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — **see-also**: the source's mapping table ("Ordinary JS control flow plays `select`", "script variables hold `K`") is a direct instance of this lemma; a reader checking "is host-language control flow really a valid `select`/call program?" gets the proof here. (Consider `rationale` if the author wants to ground the mapping claim rather than merely point adjacent.)
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — **see-also**: the "What the runtime withholds" section reads each restriction (audience, substrate, capability surface, persistence) as an independent design axis; this note names that exact independence (scheduler placement, persistence, coordination form, return artifacts vary independently). Useful adjacency for a reader generalising the four withholdings.

## Bidirectional Candidates

None. The two strongest theory relationships are better authored from the note side (`evidence`) than as return links from this descriptive analysis — see Reverse-edge Candidates.

## Reverse-edge Candidates

These notes should cite this shipped instance from their own side. **Contract note:** the `kb/notes/COLLECTION.md` labels table lists `evidence`/`derived-from` destinations as `reference, agent-memory, sources` — it does **not** yet name `agentic-systems`. The three notes that already link in use `evidence` anyway, so this is an established-in-practice but unwritten authorisation (flagged under Maintenance Observations). Each candidate below assumes that `evidence → agentic-systems` is intended.

- [any-symbolic-program-with-llm-calls-is-a-select-call-program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) → source — **evidence**: dynamic workflows are a shipped program whose non-LLM steps (JS control flow, `pipeline`/`parallel`, deterministic transforms over agent returns) are exactly the symbolic-over-`K` steps this lemma converts; a concrete real-world witness for the abstract claim.
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source — **evidence**: the four "withheld" axes (audience, substrate, capability-surface granularity, persistence) populate this note's design-space dimensions with one coherent point, demonstrating the dimensions vary independently in a real harness.
- [rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence](../../../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) → source — **evidence**: this note compares placements of symbolic work (ephemeral REPL, typed combinators, generated tools, durable callables). Dynamic workflows are a fifth placement — sandboxed guest-language script, ephemeral within a session but whole-script-promotable — that the comparison currently omits. (Note is `status: seedling`; `evidence` is additive, fine.)
- [stateful-tools-recover-control-by-becoming-hidden-schedulers](../../../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) → source — **evidence**: weaker. The workflows runtime is the *opposite* design (control exposed beneath the loop, not relocated into an exceptional stateful tool), so it reads as a contrasting reference point rather than corroboration. Surface only if the note wants a foil; otherwise skip.

## Off-authorisation Candidates

- [review-architecture](../../../../reference/review-architecture.md) — the source's `isolation: 'worktree'` primitive has a surface echo in the review subsystem's worktree use, which would be a `→ reference` `see-also` under the "direct Commonplace analogue" trigger. Judged **too thin** to author: the workflows worktree is a parallel-mutation isolation knob, the review worktree is a checkout-management detail; the shared word is `git worktree`, not a shared design decision. Recommend reject (keyword-level, fails the articulation test for an agent's benefit).

## Raw Text Candidates

None. The source has frontmatter; all candidates evaluated are typed notes.

## Rejected Candidates

- [structured-output-is-easier-for-humans-to-review](../../../../notes/structured-output-is-easier-for-humans-to-review.md) — matched the `schema`/structured-output query, but the note is about human review UX; the source's `schema` option is a stop-condition/validated-call mechanism. Different concern.
- [the-chat-history-model-trades-context-efficiency-for-implementation](../../../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) — tool-loop-tagged neighbour, but the source's persistence story (journal/save split) is already covered by the linked `orchestration-strategies-and-run-state` note; this one adds nothing the source needs.
- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) — plausible taxonomy fit, but the source already frames itself through the bounded-context orchestration model, not the scheduler/context-engine/execution taxonomy; linking both would blur which lens the analysis uses. Rejected to avoid lens confusion.
- [feasibility-is-the-heaviest-forks-net-load](../../../../notes/feasibility-is-the-heaviest-forks-net-load.md) — `budget` query hit, but the source's `budget` is a token *ceiling* primitive, not the per-fork feasibility-load argument; no concrete reader gain.
- [apparent-success-is-an-unreliable-health-signal-in-framework-owned](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — a tool-loop cluster member reachable from the README, but the source does not make claims about observability; forcing the link would assert a relationship the analysis does not carry.

## Index Membership

- [kb/agentic-systems/README.md](../../../../agentic-systems/README.md) — already lists the source. No change needed.
- [kb/notes/tool-loop-README.md](../../../../tags/tool-loop-README.md) — already lists the source under "Related approaches". No change needed.
- [kb/notes/computational-model-README.md](../../../../tags/computational-model-README.md) — does **not** currently list the source. A future maintainer of this tag-README could add it under "Scheduling & Orchestration" as the shipped instance of the cluster (connect does not edit indexes).

## Synthesis Opportunities

None new. The "shipped partial instance qualified on audience/substrate/granularity" synthesis already lives in `llm-frameworks-should-keep-the-tool-loop-optional` and the `tool-loop-README`; the source is the descriptive feeder for it, which is the intended division of labour.

## Maintenance Observations

- **Collection-contract gap (durable):** `kb/notes/COLLECTION.md`'s labels table authorises `evidence`/`derived-from` to destinations `reference, agent-memory, sources` but not `agentic-systems`, which postdates the table. Three notes already author `evidence → kb/agentic-systems/claude-code-dynamic-workflows.md` (`llm-frameworks-should-keep-the-tool-loop-optional`, `orchestration-strategies-and-run-state-have-opposite-persistence`) and a `see-also` from `tool-loop-README`. All reverse-edge candidates in this report depend on the same unwritten authorisation. Recommend adding `agentic-systems` to the `evidence`/`derived-from`/`see-also` destination cells in `kb/notes/COLLECTION.md` so the inverse-direction linking the `agentic-systems` COLLECTION.md explicitly expects ("links usually run inverse") is sanctioned from the notes side. Promotion target for a later maintenance step.

## Flags

- Not a split candidate: the source is a single coherent feature analysis; its multiple theory links are the intended inverse-edge pattern, not independent assertions warranting a split.
- No genuine **outbound** candidates beyond the two `see-also` additions — this is expected and correct for a frontloaded-ish descriptive analysis whose primary edges run inbound. The substantive new signal is the four reverse-edge candidates, all gated on resolving the contract gap above.
