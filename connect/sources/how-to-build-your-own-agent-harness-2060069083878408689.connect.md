---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.md"
source_has_frontmatter: true
date: "2026-05-29"
depth: standard
---

# Connection Report: How to build your own agent harness??? (Mike Piccolo / iii)

**Source:** [How to build your own agent harness???](../../sources/how-to-build-your-own-agent-harness-2060069083878408689.md)

The source is an **immutable snapshot** (`type: kb/sources/types/snapshot.md`). Per `kb/sources/COLLECTION.md`, snapshots never author outbound links; the active outbound surface would live in a matching `.ingest.md` (none exists yet — see Flags). The dominant authoring signal here is therefore **reverse-edge**: which notes/sources should point *at* this snapshot under their own COLLECTION.md rules, and the `compares-with` edges a future ingest report would carry. `Connections Found` below is framed as recommendations for that future ingest report's outbound surface; `Reverse-edge Candidates` is the load-bearing section.

Authorised labels for `sources` outbound (ingest/source-review only): `evidence`→notes, `derived-from`→notes, `rationale`→notes, `compares-with`→sources/agent-memory, `defined-in`→notes/definitions, `see-also`→any. Linking into `kb/work/` and `kb/instructions/` is prohibited.

## Source claim

A production agent harness is not one importable framework but ~13-15 separable jobs (provider routing, credential vault, model catalog, turn FSM/orchestrator, skill serving, system-prompt assembly, streaming, policy check, approval gate, budget tracking, hook fanout, session tree, compaction, event stream, OTel tracing). iii ships each as an independently-versioned **worker** on a shared engine bus, connected by one primitive (`iii.trigger()` over a uniform WebSocket protocol). "Build your own harness" then collapses into "swap/add a worker that registers the same function ids." Thin-vs-thick stops being a fork and becomes a slider (a count of installed workers); a major internal rewrite of one worker (FSM 11→7 states) is self-contained because neighbours talk only through bus-level function ids.

## Discovery Trace

**Index scan:**
- Read [notes dir-index](../../notes/dir-index.md) — flagged: agent-runtimes-decompose, agent-orchestration-occupies-a-multi-dimensional-design-space, always-loaded-context-mechanisms-in-agent-harnesses, subtasks-that-need-different-tools, stateful-tools-recover-control, unified-calling-conventions, mcp-bundles-stateless-tools, methodology-enforcement-is-constraining, agent-orchestration-needs-coordination-guarantees, codification-and-relaxing, enforcement-without-structured-recovery, generate-instructions-at-build-time, tool-loop-index.
- Read [sources dir-index](../../sources/dir-index.md) — flagged the harness cluster: the-anatomy-of-an-agent-harness, harness-engineering-is-cybernetics, harness-engineering-leveraging-codex, what-is-an-agent-harness, components-of-a-coding-agent-raschka, externalization-in-llm-agents-unified-review, scaling-managed-agents-decoupling-brain-from-hands, voooooogel-multi-agent-future, spacedriveapp-spacebot-ai-agent, the-self-healing-agent-harness, natural-language-agent-harnesses.
- Read [agent-memory-systems dir-index](../../agent-memory-systems/dir-index.md) — no direct match (memory-system focus; this source is a harness/orchestration substrate, not a memory store). No `compares-with` edge into agent-memory.

**Topic indexes:**
- Source tag is `x-article` only (no conceptual tags), so no conceptual tag indexes applied. Consulted [tool-loop-index](../../notes/tool-loop-index.md) and [computational-model-index](../../notes/computational-model-index.md) as the topically-adjacent hubs.

**Body search:**
- `rg "harness" kb/notes/` — surfaced always-loaded-context-mechanisms, agent-runtimes-decompose, methodology-enforcement, entropy-management; confirmed the harness vocabulary cluster.
- `rg "swap|replaceable|interchang|independently versioned" kb/notes/` — thin set; operational-signals-that-a-component-is-a-relaxing-candidate, skills-are-instructions-plus-routing-and-execution-policy. The KB has little explicit "independently-versioned/replaceable component" theory — a genuine gap (see Maintenance Observations).
- `rg "orchestrat|scheduler|control plane|bus|protocol|wire" kb/notes/` — bounded-context-orchestration-model, llm-mediated-schedulers, codified-scheduling-patterns, unified-calling-conventions, agent-orchestration-needs-coordination-guarantees, subtasks-that-need-different-tools. No KB note uses an "engine bus / function-id routing" framing — the source's most distinctive mechanism.
- `rg "iii|Piccolo|approval gate|policy::check|credential vault|budget tracker"` — no existing KB coverage of iii or its worker registry; no duplicate.

**Link following:**
- From [the-anatomy-of-an-agent-harness ingest](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md): confirmed the "harness engineering trilogy/quartet" framing (Lopopolo practice, cybernetics theory, Anatomy taxonomy, What-is-an-agent-harness taxonomy) and the productive tension with voooooogel on whether orchestration logic survives. This source is a natural new member of that source cluster.
- From [agent-runtimes-decompose](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md): the note already maps practitioner harness taxonomies onto scheduler / context-engine / execution-substrate; iii's worker list is another taxonomy to map, and turn-orchestrator vs provider/auth/streaming workers split cleanly across those three components.

## Connections Found

*(Recommendations for a future `.ingest.md` outbound surface; the snapshot itself authors nothing.)*

- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) — **evidence**: iii's worker list is another independent practitioner harness decomposition; its turn-orchestrator (scheduler), system-prompt-assembly/skill-serving/compaction (context engine), and provider/auth/sandbox workers (execution substrate) map onto the note's three components, supporting "taxonomies keep converging."
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — **evidence**: iii fixes scheduler placement (symbolic external runtime), exposes the policy/budget/approval workers as separable system-definition artifacts, and the FSM-rewrite-without-neighbour-change story is evidence that scheduler placement and persistence vary independently of the rest of the stack.
- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — **evidence**: the policy worker reading `iii-permissions.yaml` and matching `function_id` against a rule set before every tool call is a concrete codified-enforcement point on the constraining gradient.
- [enforcement-without-structured-recovery-is-incomplete](../../notes/enforcement-without-structured-recovery-is-incomplete.md) — **evidence**: iii's allow/deny/needs_approval outcomes plus fail-closed-on-timeout (`gate_unavailable`) and the approval-gate park/resume are a worked recovery layer over enforcement (corrective/fallback/escalation), exactly the missing column the note describes.
- [always-loaded-context-mechanisms-in-agent-harnesses](../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) — **evidence**: iii's per-turn system-prompt assembly (mode paragraph + identity preamble + default-skills appendix, with on-demand `directory::skills::get`) is a concrete harness implementation of layered always-loaded context plus progressive skill disclosure.
- [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — **evidence**: iii's single calling convention (every worker registers function ids on one bus; the orchestrator calls `models::list`/`provider::<name>::stream`/`policy::check_permissions` without knowing the implementation) is a production instance of name-based dispatch making components swappable without changing call sites.
- [generate-instructions-at-build-time](../../notes/generate-instructions-at-build-time.md) — **rationale**: the thin-vs-thick "slider is a count of installed workers in config.yaml" is a composition-time configuration argument, parallel to the build-time-vs-runtime parameterisation tradeoff; weaker than the above — flag as candidate, not strong.

## Bidirectional Candidates

None. The snapshot is immutable and authors no links; return-link reasoning is folded into Reverse-edge Candidates.

## Reverse-edge Candidates

*(Notes/sources that should author a link TO this snapshot under their own COLLECTION.md rules. This is the primary deliverable for an immutable snapshot.)*

- [agent-runtimes-decompose-into-scheduler-context-engine-and-execution](../../notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md) → source — **evidence**: the note already lists four convergent practitioner harness sources; iii is a fifth and the only one shipping the decomposition as separately-versioned runtime components rather than as a descriptive taxonomy, strengthening "the perimeter becomes usable once split into components."
- [agent-orchestration-occupies-a-multi-dimensional-design-space](../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → source — **evidence**: iii occupies a distinctive point (external symbolic scheduler, cross-session versioned workers, bus/shared-state coordination, fail-closed policy guarantee) the note's open map does not yet cite.
- [unified-calling-conventions-enable-bidirectional-refactoring](../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) → source — **evidence**: iii is independent production evidence that a uniform calling convention lets components move/swap without touching call sites — the note currently grounds this only on llm-do.
- [the-anatomy-of-an-agent-harness ingest](../../sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md) → source — **compares-with**: a future ingest of this source should cite the Anatomy/cybernetics/Lopopolo harness cluster as parallel coverage; conversely the Anatomy ingest's source-to-source set could note iii as the "decomposed-and-shipped" counterpart to its descriptive taxonomy.

## Off-authorisation Candidates

- [subtasks-that-need-different-tools-force-loop-exposure-in-agent](../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) — iii's turn-orchestrator dispatching every tool call through `dispatchWithHook` and treating worker replacement as first-class connects to "loop exposure / who owns the next step's action alphabet," but the only fitting reader-need is *contrast/relation between mechanisms*, and the authorised `sources→notes` set (`evidence`/`derived-from`/`rationale`) does not cleanly cover a same-mechanism-different-substrate comparison where the source neither corroborates nor grounds the claim. Suggest: a future ingest can frame it as weak `evidence` (production framework also exposes the dispatch point) or reject as merely topically adjacent.
- [stateful-tools-recover-control-by-becoming-hidden-schedulers](../../notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) — iii's `harness::trigger` meta-worker and the turn-orchestrator are arguably "the scheduler made explicit rather than hidden in a stateful tool," an interesting inverse, but no `sources→notes` label expresses "interesting inverse/contrast." Suggest: reject for the source's outbound surface; better captured as a Maintenance/synthesis observation than forced under `evidence`.
- [mcp-bundles-stateless-tools-with-stateful-runtime](../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) — iii's "every worker is a persistent WebSocket process registering functions" is an alternative to MCP's stateless-tools-on-stateful-server tradeoff; the relation is contrast, not corroboration, so no authorised label fits cleanly. Suggest: a future ingest could argue weak `evidence` that the stateful-runtime tax is a recurring design choice, or reject.

## Raw Text Candidates

None.

## Rejected Candidates

- [tool-loop-index](../../notes/tool-loop-index.md) — index/hub, not a claim; iii relates to the underlying tool-loop notes, not the index itself.
- agent-memory-systems collection (all) — iii is a harness/orchestration substrate, not a memory or knowledge store; no `compares-with`→agent-memory edge is genuine. The OTel session/message/function tracing is observability, not agent memory.
- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — the source does not engage the survive-vs-relax / bitter-lesson question (it argues *composability*, not which layers stronger models will absorb); a `voooooogel`-style tension would be invented, not present in the text.
- [agent-orchestration-needs-coordination-guarantees-not-just](../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — tempting via the fail-closed policy gate, but the source's coordination is single-turn worker dispatch, not the multi-agent shared-substrate composition the note is about; would be a keyword match on "coordination."

## Index Membership

- No conceptual index membership for the snapshot itself (snapshots are not indexed beyond the auto-generated [sources dir-index](../../sources/dir-index.md), which already lists it). A future ingest report would naturally sit alongside the other harness-cluster ingests there.

## Synthesis Opportunities

The harness-source cluster (this source + Anatomy + What-is-an-agent-harness + cybernetics + Lopopolo + Raschka + externalization-survey + scaling-managed-agents + spacebot) now spans: descriptive taxonomies, a cybernetic framing, a practice report, and — new with iii — a *shipped, independently-versioned, bus-routed* decomposition. The uncaptured higher-order claim: **the harness decomposition is converging not just descriptively but architecturally — practitioners now ship the components as separately-versioned, hot-swappable units behind a uniform calling convention.** This would extend `agent-runtimes-decompose` (which currently argues only analytic separability) toward an empirical "the industry is operationalising the split" claim, and connect to `unified-calling-conventions`. Do not create the note during connect.

## Maintenance Observations

- **Collection-contract gap (recurring):** three strong same-mechanism-different-substrate candidates (subtasks/loop-exposure, stateful-tools-as-hidden-scheduler, mcp-stateless-tools) had no fitting `sources→notes` label because the authorised set covers corroboration (`evidence`), abstraction (`derived-from`), and design-rest (`rationale`) but not *contrast/parallel-mechanism* from a source into a note. This is the second harness source to hit it (cf. the Anatomy ingest's productive-tension framing, which it could only express in prose, not as a labelled edge). A `contrasts`/`parallels` label for `sources→notes`, or explicit guidance to file such relations as weak `evidence`, would help. Best-effort signal only.
- **Theory gap:** the KB has rich scheduler/context-engine/substrate decomposition theory but no note on *component replaceability / independent versioning behind a uniform calling convention* as a first-class harness property. iii is the clearest exemplar; `unified-calling-conventions` is the nearest note but is about neural↔symbolic refactoring, not operational hot-swap of harness layers.
- **No ingest report exists** for this snapshot (see Flags) — the snapshot currently has no authored outbound surface in the KB.

## Flags

- **Missing authored companion:** there is no `how-to-build-your-own-agent-harness-2060069083878408689.ingest.md`. Until one exists, none of the `Connections Found` edges can be authored anywhere (snapshots are immutable). Recommend running `cp-skill-ingest` on this snapshot to create the ingest report that would carry these outbound edges.
- **Split candidate:** the source connects to five-plus notes across orchestration, enforcement/policy, context-loading, and calling-convention topic areas, and makes more than one independent assertion (decomposition-into-jobs; bus/function-id routing; thin-thick-as-slider; self-contained-internal-rewrite). A future ingest should expect to spread edges across several notes rather than route to one.
