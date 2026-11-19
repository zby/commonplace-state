---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md"
source_has_frontmatter: true
date: "2026-06-03"
depth: standard
---

# Connection Report: A harness for every task: dynamic workflows in Claude Code

**Source:** [A harness for every task: dynamic workflows in Claude Code](../../../sources/a-harness-for-every-task-dynamic-workflows-in-claude-code-2061907337154367865.md)

This source is an **immutable snapshot** (`type: snapshot`) with no `.ingest.md` companion yet. Per `kb/sources/COLLECTION.md`, snapshots never author outbound links; the active outbound surface is the matching `.ingest.md`, which does not exist. So every "Connections Found" item below is a candidate for whoever authors that ingest, and the highest-value signal is **reverse-edge**: which library notes should add `evidence` links pointing at this snapshot. The snapshot is a first-party Anthropic practitioner account (Thariq Shihipar, Sid Bidasaria) of *dynamic workflows* in Claude Code — Claude writing its own ephemeral JavaScript harness on the fly to spawn and coordinate sub-agents. This is the concrete shipped instance of patterns the KB's orchestration cluster theorizes.

## Discovery Trace

**Index scan:**
- Read [notes dir-index](../../../notes/dir-index.md) — flagged the orchestration/scheduler cluster: `rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents`, `orchestration-strategies-and-run-state-have-opposite-persistence`, `agent-orchestration-occupies-a-multi-dimensional-design-space`, `agent-orchestration-needs-coordination-guarantees-not-just`, `bounded-context-orchestration-model`, `the-practical-scheduler-is-the-host-language`, `synthesis-is-not-error-correction`, `topology-isolation-and-verification-form-a-causal-chain-for-reliable`, `decomposition-heuristics-for-bounded-context-scheduling`, `conversation-vs-prompt-refinement-in-agent-to-agent-coordination`, `diagnostic-richness-constrains-outer-loop-learning-quality`, `brainstorming-how-to-test-whether-pairwise-comparison-can-harden`.
- Read [agent-memory-systems dir-index](../../../agent-memory-systems/dir-index.md) — no dynamic-orchestration system review; closest is the comparative-review note, which is memory-agency focused, not orchestration. No `compares-with` target here.

**Topic indexes:**
- Source `tags: [x-article]` only — no conceptual tag to cross to a tag index. Used the `computational-model` / `tool-loop` cluster surfaced by the dir-index scan instead.

**Body search (`rg` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`):**
- `rg -i "goal drift|self-preferential|agentic laziness|lossy summar"` — no note names these three failure modes verbatim; this is a **coverage gap** (see Maintenance Observations). The source defines them precisely.
- `rg -i "adversarial verif|adversarial review|verifier per|panel of verifiers|refuter"` → `synthesis-is-not-error-correction.md` (adversarial debate as a topology). Confirms the source's "adversarial verification" / "panel of verifiers and refuters" pattern lands on the voting/verification cluster.
- `rg -i "fan-out|fan out|synthesize.*result|barrier"` → `bounded-context-orchestration-model`, `agent-orchestration-needs-coordination-guarantees-not-just`, `decomposition-heuristics-for-bounded-context-scheduling`. The source's "fan-out-and-synthesize … synthesize step is a barrier" is a direct match.
- `rg -i "tournament|pairwise|comparative judgment|bracket"` → `brainstorming-how-to-test-whether-pairwise-comparison-can-harden`. The source's Sorting use-case ("comparative judgment is more reliable than absolute scoring", pairwise-comparison pipeline, "deterministic loop holds the bracket") is first-party corroboration of that brainstorm's central hypothesis.
- `rg -i "ephemeral orchestrat|model writes|tailor-made|on the fly|REPL|RLM"` → `rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents`, `orchestration-strategies-and-run-state-have-opposite-persistence`, `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence`, `agent-orchestration-occupies-a-multi-dimensional-design-space`. Strongest cluster — dynamic workflows ARE "the model writes the orchestrator rather than being it."
- `rg -i "worktree|clean context|context isolation"` → `topology-isolation-and-verification…`, `llm-context-is-composed-without-scoping`. The source's per-agent worktree isolation and "own clean context window so they don't cross-contaminate" map onto the isolation layer.
- `rg -i "mine.*session|corrections|distill.*rule|CLAUDE.md rule"` → no note directly covers mining sessions into CLAUDE.md rules; nearest theory is `spec-mining-as-codification` and `distillation-is-transformation-not-selection`. Partial; routed as candidates, not strong reverse-edges.
- `rg -i "quarantine|untrusted|high-privilege"` → `the-four-field-record-exposes-an-efficiency-security-and-sovereignty`, `llm-context-is-composed-without-scoping`. The source's "quarantine" pattern (untrusted-content readers barred from high-privilege actions) is a security-layer match but no authored security-of-orchestration note exists. Logged as gap.

**Sibling-source scan (`rg` over `kb/sources/`):**
- Confirmed a dense peer family for `compares-with`: `recursive-language-models-…`, `slate-moving-beyond-react-and-rlm`, `the-mismanaged-geniuses-hypothesis-…`, `voooooogel-multi-agent-future`, `meyerson-maker-million-step-llm-zero-errors`, plus the harness-engineering cluster (`how-to-build-your-own-agent-harness`, `the-anatomy-of-an-agent-harness`, `natural-language-agent-harnesses`).

**Link following:**
- From `rlm-…` followed `Relevant Notes` → `orchestration-strategies-and-run-state-have-opposite-persistence` (RLM discards both `select` and `K`) and `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence`. The source's note that workflows can be **saved** (press "s", check into `~/.claude/workflows`, distribute via a skill) is the missing promotion path these notes call for — strong evidence for the "ephemeral orchestrators should be promotable" argument.

## Connections Found

*(Candidates for a future `.ingest.md` of this snapshot. The snapshot itself stays immutable; these are not authored anywhere by connect.)*

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — **evidence**: dynamic workflows are a shipped, first-party instance of "the model writes the orchestrator rather than being it" — Claude emits a JS harness that spawns/coordinates sub-agents, with interrupt-and-resume.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — **evidence**: the source's save-and-share mechanism (save a workflow, check into `~/.claude/workflows`, distribute via a skill as a template) is exactly the promote-the-recurring-`select`-strategy path this note argues for, against RLM's discard-both default.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) — **evidence**: the source's distinct named patterns — fan-out-and-synthesize (a barrier that merges complementary outputs) vs. tournament/voting and adversarial verification (selection/error-correction) — are first-party confirmation of the synthesis-vs-voting design distinction.
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — **evidence**: the Sorting use-case asserts "comparative judgment is more reliable than absolute scoring" and runs a pairwise-comparison pipeline, corroborating the brainstorm's hypothesis from a production setting (note: still a vendor claim, not a controlled test).
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — **evidence**: dynamic workflows occupy a specific combination — model-authored symbolic scheduler on an exact substrate (JS file), ephemeral-but-promotable persistence, model-chosen coordination form, model-chosen model/worktree per sub-agent — a concrete point the design-space map can cite.

## Bidirectional Candidates

None. The source is an immutable snapshot; it cannot carry authored return links, and it has no `.ingest.md` companion to hold them yet. Return paths would live in the ingest if one is authored.

## Reverse-edge Candidates

*(Library notes that should add a link TO this snapshot under their own COLLECTION.md rules. This is the primary deliverable for an immutable snapshot.)*

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) → source — **evidence**: a production system (Claude Code dynamic workflows) implementing the same model-authors-the-orchestrator move on an exact JS substrate; strengthens the seedling beyond the single RLM/REPL example.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) → source — **evidence**: the save/share-via-skill workflow is real-world support for promoting the recurring `select`-strategy while run-state stays ephemeral.
- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) → source — **evidence**: practitioner taxonomy that keeps fan-out-and-synthesize separate from tournament/adversarial verification, matching the note's central distinction.
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) → source — **evidence**: independent first-party statement of the pairwise-over-scalar claim and a deployed pairwise pipeline. Because the note is a seedling testing a hypothesis, treat this as corroborating opinion, not a settled result — flag accordingly when authoring.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source — **evidence/exemplifies**: a new concrete combination for the map (model-authored scheduler, promotable persistence, model-selected coordination + model/worktree routing).
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) → source — **evidence**: the source motivates workflows precisely by the three failure modes that appear in a single long context window (agentic laziness, self-preferential bias, goal drift after compaction) and prescribes decomposition + isolated context windows + adversarial verifiers — a practitioner statement of the topology→isolation→verification chain. Strong but the note is `status: speculative`; treat the snapshot as supporting illustration, not as resolving the chain-vs-simpler-account question.
- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) → source — **evidence**: the source's "Helpful patterns" (classify-and-act, fan-out-and-synthesize, adversarial verification, generate-and-filter, tournament, loop-until-done) are a practitioner catalogue of decomposition/aggregation heuristics this note collects.

## Off-authorisation Candidates

These pass the articulation test but `kb/sources/` authorises no label that fits the source→destination pair (the snapshot's only authoring surface would be an ingest; even there the label set is `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, `see-also`). Each is really a **reverse-edge from another collection** whose own COLLECTION.md governs the label — listed here so an ingest author or maintainer can route them:

- [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — the source's clean structured handoffs between fan-out and synthesize agents exemplify prompt-refinement over conversation; useful but a weaker, more diffuse match than the cluster above. Suggest: let the note author decide whether to cite the snapshot as `evidence` under `kb/notes/` rules, or reject as too generic.
- [diagnostic-richness-constrains-outer-loop-learning-quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — the source's Evals/Memory use-cases (spin off comparison agents to grade outputs against a rubric; verifier-per-rule) bear on inspectable failure evidence for outer-loop learning, but indirectly. Suggest: evaluate when authoring; likely a `see-also` at best.
- Security-of-orchestration ("quarantine") angle — the source's quarantine pattern (untrusted-content readers barred from high-privilege actions) has no authored home note. Suggest: this is a **collection-content gap**, not a label gap (see Maintenance Observations), not an edge to author now.

## Raw Text Candidates

None. All candidate targets are typed notes.

## Rejected Candidates

- [agent-orchestration-needs-coordination-guarantees-not-just](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — strong keyword overlap (coordination, contamination, amplification), but the note's load-bearing move is *which guarantee* prevents *which* failure; the source describes patterns without committing to a guarantee taxonomy. The design-space and synthesis-vs-voting notes already carry the useful edges; adding this one risks a redundant "related" link.
- [llm-context-is-composed-without-scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — the source's per-agent clean context windows touch scoping, but the note's claim is about flat-concatenation pathology; the snapshot neither demonstrates nor contradicts it. Covered transitively via the topology-isolation note.
- [agent-memory-systems comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) — the source's "mine sessions into CLAUDE.md rules" brushes memory, but the review is about memory-agency dimensions, not orchestration; no concrete reader gain.
- `spec-mining-as-codification` / `distillation-is-transformation-not-selection` — the session-mining-to-rules use-case is a distillation instance, but the snapshot only mentions it as one example prompt among many; too thin to anchor an `evidence` edge without an ingest that foregrounds it.

## Index Membership

None to author from connect. If an `.ingest.md` is created, the natural home is the `computational-model` / tool-loop cluster (e.g. `tool-loop-index`, `computational-model-index`) — but index membership for the snapshot itself is not connect's to write, and snapshots are not typically indexed alongside notes.

## Synthesis Opportunities

The source bundles several KB threads that are currently separate notes but no single note states the combined claim: **a production agent harness now lets the model author an ephemeral-but-promotable orchestrator that simultaneously supplies topology (decomposition patterns), isolation (worktrees/clean contexts), and verification (adversarial verifiers, tournaments, voting) — i.e. all three legs of the reliability chain plus a promotion path, in one shipped system.** That is a higher-order claim implied jointly by `rlm-…`, `orchestration-strategies-and-run-state-…`, `topology-isolation-and-verification-…`, and `synthesis-is-not-error-correction`. Do not author it during connect; flag as a candidate synthesis if an ingest is written.

## Maintenance Observations

- **Coverage gap (collection content, not label):** No note names the three failure modes the source defines crisply — *agentic laziness* (stopping after partial progress), *self-preferential bias* (preferring one's own results when judging), *goal drift* (lossy compaction dropping "don't do X" constraints). Several notes (`topology-isolation-…`, `synthesis-is-not-error-correction`, `diagnostic-richness-…`) circle these without a shared vocabulary. A future note could name and source them from this snapshot. Promotion candidate for a later maintenance pass.
- **No ingest companion:** This snapshot has no `.ingest.md`. Until one exists, none of the strong reverse-edges above can be reciprocated from a source-side outbound surface; the edges must be authored from the note side. If this source is worth citing as evidence in ≥3 notes (it is), authoring an ingest would consolidate the outbound surface — worth flagging to the maintainer.
- **Security-of-orchestration gap:** the "quarantine" pattern (privilege separation between untrusted-content readers and high-privilege actors in a workflow) has no home in `kb/notes/`; it sits between context-engineering and the four-field security axis. Durable enough to note for later.

## Flags

- **Split candidate:** the source touches ≥5 notes across ≥3 areas (orchestration/scheduling, error-correction/verification, evaluation/pairwise) and makes multiple independent assertions (failure-mode taxonomy, pattern catalogue, save/share promotion). If an ingest is authored, expect it to fan out to several notes rather than one.
- **Seedling/speculative targets:** `rlm-…`, `orchestration-strategies-and-run-state-…`, `agent-orchestration-occupies-a-multi-dimensional-design-space`, `synthesis-is-not-error-correction`, and `brainstorming-how-to-test-whether-pairwise-comparison-can-harden` are seedlings; `topology-isolation-and-verification-…` is speculative. The `evidence` label is additive and safe, but the source is a first-party vendor account, not an independent or controlled result — frame the evidence as corroborating practitioner testimony, not validation.
