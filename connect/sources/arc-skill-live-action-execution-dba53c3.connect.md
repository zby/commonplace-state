---
description: "Discovery report for possible KB connections from the pinned ARC skill live-action source"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/arc-skill-live-action-execution-dba53c3.md
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: ARC skill live action execution at dba53c3

**Source:** [ARC skill live action execution at dba53c3](../../../../sources/.snapshots/arc-skill-live-action-execution-dba53c3.md)

## Discovery Trace

**Description listing scan:**

- Scoped `rg '^description:' kb/notes/ --glob '*.md'` filtered for authority, prediction, surprise, control surfaces, execution, warrant, applicability, queues, and plans. Kept behavioral authority and the six-path applicability audit; rejected the world-model note because its learned-predictor claim does not describe ARC's symbolic action checks.
- Scoped `rg '^description:' kb/reference/ --glob '*.md'` with the same concept set. Kept the live behavioral-authority revision proposal because it explicitly needs bounded cases that separate applicability, path topology, and force.
- Scoped description listings over `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. No agent-memory candidate matched the file's paid-action boundary; whole-system ARC comparison would require more than this one file. ToolGate was evaluated as a source-side comparison but rejected as unnecessary for the present reader need.

**Topic indexes:**

- Read `kb/notes/tags-README.md`; the artifact-analysis and tool-loop heads were plausible routes. The proposal and its linked artifact-analysis neighborhood were more specific than broad index membership.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The reference proposal is the only current design frontier directly awaiting this case; no current external-system roster entry is justified by a single implementation file.

**Full title listings:**

- Ran `rg -N --no-heading -m1 '^# '` over each authorised local destination (`kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`) and filtered the resulting title surfaces for authority, prediction, surprise, execution, plan, revision, control, epistemic warrant, applicability, queue, and workflow concepts. This confirmed the proposal, behavioral-authority definition, six-path audit, runtime-control note, world-model note, and ToolGate ingest as the plausible cluster.

**Body search:**

- `rg -n -i "behavioral authority|action admission|prediction.*action|surprise.*(queue|batch|plan)|stale plan|plan.*applicab|operational consequence|epistemic warrant|control surface|execution timing|revision timing" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` — kept the behavioral-authority proposal and audit; rejected generic authority leads in system reviews as taxonomy reuse rather than a useful connection.
- `rg -n "prediction|surprise|provenance|remaining|discard|stale|plan" related-systems/arc-skill/skills/arc-skill/scripts/arc_skill/live.py` — confirmed that the captured revision contains per-step prediction admission, plan-source freshness checks, and suffix discard on divergence. The checkout was clean at commit `dba53c3799eab600a512dd73ed037d7ab6958c66`.

**Link following:**

- Followed the proposal to [Behavioral authority](../../../../notes/definitions/behavioral-authority.md), [Six Commonplace paths establish broad addressability, not completeness](../../../retained/six-commonplace-paths-establish-broad-addressability-not-completeness.md), and [Axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md). ARC supplies an external worked case for the proposal's unresolved decomposition, but it does not decide the ontology or validate completeness.

## Connections Found

- [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) — **is-evidence-for**: ARC's one execution file assigns different consequences at distinct points—prediction syntax admits a batch step, source hashes admit a solve plan, and a failed prediction truncates the unexecuted suffix—so one stored mechanism exposes applicability, path position, and force as separately useful distinctions.
- [Six Commonplace paths establish broad addressability, not completeness](../../../retained/six-commonplace-paths-establish-broad-addressability-not-completeness.md) — **is-evidence-for**: ARC is an external bounded comparison case in which target operation and activation condition distinguish authority paths that a broad consumer/channel/force description would merge.
- [Revise the behavioral-authority decomposition](../../../../reference/proposals/revise-behavioral-authority-decomposition.md) — **see-also**: the proposal is the live Commonplace design frontier that can use this bounded implementation case without treating it as a selected ontology.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Revise the behavioral-authority decomposition](../../../../reference/proposals/revise-behavioral-authority-decomposition.md) → source — **evidenced-by**: the proposal should retain ARC as a bounded worked case showing distinct applicability, timing, and operational consequences inside one symbolic execution path, while stating that the case does not settle the open decomposition choices.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — rejected: shared prediction vocabulary masks a different claim; ARC checks explicit symbolic predictions during execution rather than assessing a learned world model's explanatory-reach.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) — rejected: ARC exemplifies exposed checks, but this one source file does not establish the note's comparative runtime claim.
- [ToolGate: Contract-Grounded and Verified Tool Execution for LLMs](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) — rejected: both systems gate mutation and verify outcomes, but a source-to-source comparison adds no distinct reader value for the bounded behavioral-authority case.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The source is one pinned implementation file, not a whole-system ARC review. Any claim about ARC beyond live-action admission, plan freshness, prediction grading, and queue truncation needs additional pinned source.
