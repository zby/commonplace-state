---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Traditional debugging intuitions break when tool loops can recover semantically

**Source:** [Traditional debugging intuitions break when tool loops can recover semantically](../../../notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover.md)

## Discovery Trace

**Source and contract setup:**

- Read the source artifact, `kb/cache/types/connect-report.md`, and `kb/notes/COLLECTION.md` in full. The source has frontmatter and belongs to `kb/notes/`.
- The notes contract authorizes prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; it excludes `kb/work/`. The reserved `external` destination is authorized only for targets already in hand, not as a search surface.
- Source claim decomposition: ordinary software trains programmers to treat end-to-end success as evidence that the intended mechanism worked; a goal-holding LLM can synthesize a replacement route after a tool failure; the resulting good artifact hides the failed path, delays repair, and makes runtime observability necessary. The note is narrower than its parent health-signal note because its contribution is the programmer's inherited heuristic and resulting false confidence.

**`kb/notes/`:**

- Curated heads read: `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/computational-model-README.md`, `kb/notes/kb-maintenance-README.md`, and `kb/notes/observability-README.md`. None of the three matching tag READMEs declares `complete: true`, so no by-tag search was skipped. The observability head and the tool-loop head reached from the computational-model head already list the source. The KB-maintenance head lists the parent health-signal note rather than this narrower consequence.
- Complete title surface generated with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (354 headings).
- Whole description surface generated with `rg '^description:' kb/notes/ --glob '*.md'`. By-tag description surfaces were generated for each source tag with `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`, and the same command with `kb-maintenance` and `observability` substituted.
- Body searches run: `rg -n -i "semantic recover|semantic fallback|tool fallback|agent workaround|workarounds" kb/notes/ --glob '*.md'`; `rg -n -i "final success|end-to-end success|successful outcome|apparently healthy|degraded execution" kb/notes/ --glob '*.md'`; `rg -n -i "debugging intuition|fail(s|ed|ure)? soft|hidden (failure|path)|failure.*hidden|runtime health|execution path" kb/notes/ --glob '*.md'`; and `rg -n -i "trajectory|trace.*(debug|failure|recover)|observab" kb/notes/ --glob '*.md'`.
- Kept [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md): it supplies the missing mechanism and failure economics behind the source's false-confidence phenomenon. Its existing return edge already says that it extends the source, so the useful new source-side edge is `mechanism`, not a mirrored `extends`.
- Kept [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md): it distinguishes recovery from a broken tool path from recovery of an unacknowledged specification gap while preserving the same hidden-success surface, which is exactly the reader need for `contrasts`.
- Evaluated [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md), [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md), [LLM debugging starts with retry-versus-rewrite triage](../../../../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md), and [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md). They were rejected as direct edges for respectively explaining a different traditional bracket, helping only after a failure is visible, diagnosing bad LLM outputs rather than successful recovery, and addressing later learning rather than the programmer's false inference.
- Existing source links to the parent health-signal note, tool-loop head, teaching error messages, structured recovery, and tool-boundary unit testing were checked and not re-proposed.

**`kb/reference/`:**

- Curated head read: `kb/reference/README.md`. No destination-local READMEs matching the source's three tags exist. The same three guarded by-tag description commands were run under `kb/reference/`; they surfaced maintenance proposals but no direct source-side evidence target.
- Complete title and description surfaces generated with `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (135 headings) and `rg '^description:' kb/reference/ --glob '*.md'`.
- Body searches run with the same four query families used for notes, substituting `kb/reference/`. A focused query, `rg -n -i "debugging intuition|fail(s|ed|ure)? soft|hidden (failure|path)|failure.*hidden|runtime health|execution path|trajectory-aware" kb/reference/ --glob '*.md'`, surfaced [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md).
- Kept that proposal as a reverse-edge candidate. Its rationale is that a plausible final artifact can conceal failed tool calls, stale input, worker-lifecycle violations, or invalid recovery. Under the reference contract, the primary theory-ward direction is `rests-on`; adding that edge from the proposal to this source would explain why output-only inspection predictably reassures operators.
- [Harness sub-agent model selection regression](../../../../reference/harness-sub-agent-model-selection-regression.md) was evaluated and rejected: it documents provenance misattribution in a specific harness regression, not semantic recovery hiding a broken route.

**`kb/agent-memory-systems/`:**

- Curated head read: `kb/agent-memory-systems/README.md`. No matching tag READMEs exist. Complete title and description surfaces were generated with `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (173 headings) and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`. Guarded by-tag description queries for the three source tags found no source-specific cluster; the only observability-tag hit was the broad trace-learning analysis.
- Body searches used the same four query families, plus `rg -n -i "inefficient(-but-| )successful|failures, workarounds|final solution|final score alone|trace.*root.cause" kb/agent-memory-systems/ --glob '*.md'`.
- Evaluated [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md), whose doc-grounded taxonomy separates inefficient-but-successful trajectories from clean successes, and [cq](../../../../agent-memory-systems/reviews/cq.md), whose code-grounded trace source retains failures, workarounds, and final solutions separately. Both are useful implementations of path-aware learning, but neither establishes the source's human-cognition claim; their signal is downstream of the more direct evidence candidates retained below.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md), [HALO](../../../../agent-memory-systems/reviews/halo.md), and the trace-learning comparison were followed one hop. They support diagnostic-richness theory rather than the narrower inherited-debugging-intuition claim, so no edge was kept.

**`kb/agentic-systems/`:**

- Curated head read: `kb/agentic-systems/README.md`. No matching tag READMEs exist. Complete title and description surfaces were generated with `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (12 headings) and `rg '^description:' kb/agentic-systems/ --glob '*.md'`; guarded by-tag description queries were also run for all three source tags.
- Body searches used the same recovery, success, debugging, trajectory, and observability query families. A focused query, `rg -n -i "final score alone|trace.*failure|recovery|observab" kb/agentic-systems/ --glob '*.md'`, surfaced [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md), [Eigenius](../../../../agentic-systems/reviews/eigenius.md), and [Swamp](../../../../agentic-systems/reviews/swamp.md).
- Agno's trace APIs and Swamp's post-execution reports show concrete observability surfaces, but do not show successful semantic workarounds misleading programmers. Eigenius documents a weaker recovery path that can mark a task complete without the normal output-and-trace commit, but its deterministic startup recovery is outside the source's semantic tool-loop mechanism. All three were rejected as direct candidates.

**`kb/sources/`:**

- Curated head read: `kb/sources/README.md`. No matching tag READMEs exist. Complete title and description surfaces were generated with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` (504 headings) and `rg '^description:' kb/sources/ --glob '*.md'`. Guarded by-tag description queries for the three source tags returned no relevant source cluster.
- Broad body searches used the same recovery, final-success, debugging, and trajectory families. Focused searches then ran as `rg -n -i "camouflage.*failure|automatic systems should fail obviously|successful automated systems" kb/sources/ --glob '*.md'`, `rg -n -i "inefficient(-but-| )successful|failed tool call|grade the outcome, not the trajectory" kb/sources/ --glob '*.md'`, and `rg -n -i "outcome.*trajectory|trajectory.*outcome|final (artifact|answer).*failure|good (artifact|output).*failure" kb/sources/ --glob '*.md'`.
- Kept [Ironies of Automation](../../../sources/ironies-of-automation.md): Bainbridge's human-factors paper reports that automatic control can camouflage system failure and argues that automated systems should fail obviously. This is historically prior, cross-domain evidence for the human monitoring mechanism, with the important limitation—made explicit in its ingest—that transfer from process control to LLM tool loops is analogical rather than directly tested.
- Kept [Ingest: The Self-Healing Agent Harness](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md): the practitioner report and local analysis distinguish outcome grading for user-facing product quality from trajectory monitoring for infrastructure health and degraded execution. That boundary corroborates the source's correction without implying that every strange successful path is a defect.
- [Ingest: Trajectory-Informed Memory Generation](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) was evaluated but rejected as a third evidence edge: its successful/failed/inefficient outcome classes are relevant, but the associated system review already showed that this is path-aware learning evidence rather than direct support for the cognitive claim.

**`kb/instructions/`:**

- Curated head read: `kb/instructions/README.md`. No matching tag READMEs exist. Complete title and description surfaces were generated with `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` (44 headings) and `rg '^description:' kb/instructions/ --glob '*.md'`; all three guarded by-tag description queries returned no relevant cluster.
- Body search run: `rg -n -i "semantic recover|tool fallback|workaround|final success|successful outcome|degraded execution|debugging intuition|runtime health|execution path|trajectory|observab|failed tool|failure" kb/instructions/ --glob '*.md'`.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) mentions avoiding a false-confidence failure, but there the risk is an agent collapsing an explicitly non-verdict critique into a verdict. It is not semantic recovery around a failed tool path, so neither `operationalized-from` nor a reverse `rests-on` edge passed the articulation test. Health-check and review procedures were likewise too general.

**External:**

- Open-web prospecting was skipped as required. The target itself supplied no external target. External URLs encountered inside local source artifacts were not proposed because the corresponding local snapshots provide the inspectable, preserved evidence surface.

**Link following:**

- Followed every existing source link one hop. The parent health-signal note led to the silent-disambiguation analogue, LLM-mediated scheduler degradation, runtime decomposition, and memory-extraction consequence; only the analogue added an independently useful source-side edge.
- Followed the goal-holding-interpreter neighborhood through underspecification, soft degradation, oracle accumulation, and codification. These confirmed that its contribution is the mechanism and recurring workaround tax, not merely topical overlap; it already links back to the source.
- Followed the Bainbridge ingest to its automation-boundary notes. They did not provide a closer account of semantic tool-loop recovery, but the ingest's stated transfer limitation prevented overstating the snapshot as direct LLM evidence.
- Followed the Self-Healing Agent Harness ingest to the parent apparent-success note and its evaluator/oracle cluster. This confirmed that the retained value is the outcome/trajectory boundary, not a duplicate health-signal claim.
- Followed the trajectory-aware proposal to its reasoning-production and checked-outcome premises. Those premises remain distinct; this source would add the missing operator-cognition premise rather than duplicate an existing edge.

## Connections Found

- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) — **mechanism**: explains how retaining the goal lets an interpreter consume a failure through re-routing, leaving a successful outcome on top while recurring workaround cost and maintenance debt stay hidden
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — **contrasts**: separates recovery from a broken operational path from recovery of an unacknowledged specification gap, two neighboring mechanisms that produce the same falsely reassuring success surface
- [Ironies of Automation](../../../sources/ironies-of-automation.md) — **evidenced-by**: supplies a historically prior human-factors case in which automation camouflages failure and makes obvious failure presentation a design requirement; this corroborates the monitoring mechanism analogically, not as direct LLM evidence
- [Ingest: The Self-Healing Agent Harness](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) — **evidenced-by**: a practitioner report distinguishes grading final outcomes for product quality from monitoring trajectories for infrastructure health and degraded execution, directly bounding the note's correction

## Bidirectional Candidates

None. The goal-holding-interpreter note already carries the independently useful return edge to the source; the other retained candidates do not need reciprocal links merely for symmetry.

## Reverse-edge Candidates

- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → source — **rests-on**: the proposal assumes that a plausible final artifact can hide failed tools, invalid recovery, and workflow violations; this source explains why output-only success also predictably reassures the operator and delays maintenance

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md) — explains why classical developers can usually ignore interpreter non-conformance when diagnosing a wrong output, but the source concerns a different inference: a good final outcome being mistaken for evidence that the intended path stayed healthy
- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) — helps localize a failure once it is visible, but does not restore the failure signal erased by a successful workaround
- [LLM debugging starts with retry-versus-rewrite triage](../../../../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — routes bad-output diagnosis between sampling and specification; it does not address successful semantic recovery or infrastructure health
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — makes trace evidence useful to later proposers, but is downstream of the source's narrower claim about inherited programmer judgment
- [Trajectory-Informed Memory Generation](../../../../agent-memory-systems/lightweight/trajectory-informed-memory-generation.md) — distinguishes inefficient successes from clean successes, but its doc-grounded system description does not establish that programmers over-trust those outcomes
- [cq](../../../../agent-memory-systems/reviews/cq.md) — retains failures, workarounds, and final solutions as separate trace inputs, an implementation witness for observability rather than evidence for the source's cognitive claim
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — provides trace and observability APIs beyond final scores, but the analysis does not show semantic recovery hiding a failed path or misleading programmers
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — documents weaker recovery that can still mark a task complete, but the recovery is deterministic restart behavior rather than a model synthesizing a new route
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — its false-confidence warning concerns automated judgment of non-verdict review output, not tool-loop recovery

## Index Membership

None. The source is already curated in the Observability and Tool loop heads; the Computational model head routes to Tool loop, and the KB-maintenance head intentionally foregrounds the broader parent health-signal note.

## Synthesis Opportunities

- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../notes/traditional-software-can-bracket-executor-conformance-llm-systems.md), [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md), and the source jointly imply a two-bracket account of inherited debugging intuition: classical practice can usually assume executor conformance, and a failed prescribed path normally cannot synthesize a replacement from the retained goal. LLM systems remove both assumptions. A synthesis could distinguish wrong-output diagnosis from good-output health inference rather than treating “traditional debugging intuition” as one undifferentiated heuristic.

## Maintenance Observations

- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) is centrally about hidden failure, detection, and maintenance economics but carries only `learning-theory` and `llm-reliability` tags. Review whether `observability`, `computational-model`, or `kb-maintenance` membership is warranted; its absence from those tag sweeps currently hides a close mechanism note from the source's three principal discovery routes.

## Flags

None.
