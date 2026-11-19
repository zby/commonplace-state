---
description: "Pre-ingest connections for Corral's outcome-process gap, evidence uptake, and limited scaffold comparison"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/ai-scientists-results-without-scientific-reasoning.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: AI Scientists Produce Results Without Reasoning Scientifically

**Source:** [Corral paper](../../../../sources/.snapshots/ai-scientists-results-without-scientific-reasoning.md)

Pre-ingest discovery using `cp-skill-connect`; accepted links belong in the future name-paired ingest.

## Discovery Trace

- Read all 7,719 snapshot lines, including environment descriptions, statistical models, graph extraction and motif examples, intervention protocol, limitations, and references. Loaded sources, notes, and reports contracts and the connect-report type. No source tags.
- Reused collection README heads and the fresh title surface generated during this serial discovery session: `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Combined output was truncated; focused description searches resolved candidates. Evaluation and learning-theory heads lack completeness marks.
- Notes/source discovery used description matches for scientific, reasoning process, trajectory-aware, activation, and scaffold/model terms, plus the earlier falsification and independent-evaluation query. Fully read reasoning-production, process/output structure, experimental contrast, contextual activation, and AutoResearchEval ingest. The last supplies a useful comparison about diagnosed failures that do not change action.
- Reference discovery followed the process-validity link into the trajectory-aware evaluation proposal and read it fully. It supplies a concrete destination for the source's graph-annotation limitations and bounded motivation for inspecting trajectories.
- Agent-memory-systems discovery reused its README and the refinement/repair/verification description query; Reflexion was read in the preceding pass. Its persistent lesson mechanism is absent from Corral, so no direct evidence relation is retained. Agentic-systems title/description screening surfaced general harness comparisons but no closer mechanism than the reference proposal; no target retained there. Source-authorized external destination is the supplied original paper URL; no external search.
- Candidate bodies and authored links, rather than lexical overlap, selected the final connections. Instructions and workshops remain outside source link authorization. No similarity scores were used.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: Corral's two minimal scaffolds explain little variance within its fitted design; the experiment leaves retrieval, persistent memory, explicit planning, and multi-agent orchestration untested. This is a concrete attribution boundary, not evidence that all scaffolding is ineffective.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: many annotated evidence observations have no subsequent graph link to judgment or hypothesis revision, illustrating the need to check evidence use separately from exposure. Support is limited to visible annotated uptake; absent edges do not prove absent behavioral use.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — **compares-with**: successful task endpoints coexist with weak annotated hypothesis testing. This motivates checking the actual route independently, while the note's evaluator-substitution mechanism is not tested by Corral.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) — **compares-with**: both diagnose scientific-agent trajectories and distinguish noticing evidence or flaws from changing action. Corral's typed visible graphs differ from AutoResearchEval's artifact-aware failure judge; both require calibration and do not identify a universal model-level cause.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: the proposal is the concrete local experiment destination. Corral motivates route inspection and adds reasons to test missing-edge false positives, opportunity-conditioned motif rates, and independent human adjudication before adopting a trajectory judge.
- [Original paper](https://arxiv.org/abs/2604.18805) — **derived-from**: the future ingest derives from this source.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) could author **evidenced-by** to the future ingest, qualified as graph-annotated visible evidence uptake rather than a causal memory-utilization intervention. Notes contract authorizes the relation; use retained quotes or `(snapshot required)`.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md): Corral separates outcomes from trace properties but does not independently manipulate process and output prescriptions. It cannot establish the two-lever effect.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md): Corral has no cross-task retention, and replaying a prefix also reexecutes tools to reconstruct environment state. This is not a test of stored reflective lessons.

## Index Membership

None

## Synthesis Opportunities

None. Existing activation and experimental-contrast notes own the strongest transferable claims. A future calibrated evidence-to-action assay could compare Corral and AutoResearchEval, but their annotations are not presently a shared metric.

## Maintenance Observations

None

## Flags

- Preserve the experiment boundary: three model versions, eight computational domains, ReAct XML versus native tool calls, short fixed call budgets, flat histories, no cross-task retention, retrieval, summarization, explicit planners, or multi-agent mechanisms. The reported 1.5% scaffold variance is model/design-dependent, not a universal engineering ceiling or a causal training-only remedy.
- Main text reports reasoning 41.4% and environment scope 30.1%; Appendix G.5 reports combined model identity 45.2% (90% interval 41.4–48.8) and environment scope 32.5%. These are different decompositions; do not silently merge them.
- Main aggregate motif rates include 68% evidence non-uptake and 26% refutation revision. Appendix H opening instead gives 88% non-uptake for two models and 4%/1% revision, whereas H.16's three-model table broadly supports main aggregates. Explicitly flag this inconsistency rather than select one as unambiguous truth.
- Epistemic graphs cover 626 ReAct-only brief traces. Claude annotates overlapping windows; uncertain edges are omitted. Quote checks emitted 25,369 warnings, mainly quotation mismatch; detailed methods retain warnings despite prose suggesting invalid cases are discarded. Missing edges measure annotation visibility as well as behavior.
- Appendix H's isomer non-uptake example explicitly says it is looking back at the supplied list before testing a candidate. A fixed-belief example changes an invalid potential path to the valid file. These examples caution against equating absent `informs` or `updates_to` edges with absent use or correction.
- Human calibration distinguishes 773 manually labeled behavioral traces from graph review of 25 traces. Appendix reports three graph reviewers, versus looser two-reviewer wording elsewhere. High agreement and prevalence-adjusted agreement coexist with very low Cohen kappa under label imbalance. Do not substitute aggregate agreement for per-motif validity.
- Prefix interventions replay tool calls into consistent environment state and may leave little of the problem unsolved. They do not isolate reusable textual knowledge. Pass^k measures all-trial consistency, not pass@k best-of-k success. Some motifs depend on whether a trajectory had an opportunity for that act; absence need not be an error.
