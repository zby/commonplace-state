---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/trace-trajectory-attribution-for-automated-context-engineering.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: TRACE: TRajectory Attribution for Automated Context Engineering

**Source:** [TRACE: TRajectory Attribution for Automated Context Engineering](../../../../sources/.snapshots/trace-trajectory-attribution-for-automated-context-engineering.md)

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md` and `kb/cache/types/connect-report.md`. The snapshot is immutable; the matching ingest report is its authored outbound surface. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and sources. Links into work and instructions are excluded.
- Read the complete snapshot and the curated heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- The snapshot has no tags. Topic routing instead used the curated note heads for context engineering, KB maintenance, deploy-time learning, self-improving systems, evaluation, observability, agent memory, and LLM reliability.
- Read `kb/notes/COLLECTION.md` and `kb/agent-memory-systems/COLLECTION.md` while checking possible return edges. No return edge is proposed before the matching ingest exists, because durable artifacts must not link to an immutable `.snapshots/` path.
- No semantic search scores were available; all screening was lexical, followed by full-artifact evaluation.

**Full title listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over notes, reference, agent-memory systems, agentic systems, and sources. The fresh listings covered 359 note titles, 139 reference titles, 173 agent-memory titles, 12 agentic-system titles, and 290 source titles.
- The note titles surfaced the diagnostic-richness, trace-authority, candidacy-versus-verdict, evaluation-phase, automation-boundary, and KB-learning clusters. The system and source titles surfaced TRACE's closest comparators: ACE, Meta-Harness, Trajectory-Informed Memory Generation, AutoResearchEval, and the self-healing harness loop.

**Description listing scans:**

- `rg -n -i '^description:.*(trajectory|trace-extracted|dissatisfaction|implicit signal)' kb/notes --glob '*.md'` and `rg -n -i '^description:.*(diagnostic|root cause|causal attribution|fault attribution|failure)' kb/notes --glob '*.md'` — kept the diagnostic-richness, trace-authority, and candidacy-evidence candidates after reading their claims and scope limits.
- `rg -n -i '^description:.*(stale|staleness|content gap|maintenance|verification|verify|exploration)' kb/notes --glob '*.md'` and `rg -n -i '^description:.*(deploy-time|continual learning|readable artifact|system-definition|context layer)' kb/notes --glob '*.md'` — kept the bounded KB-learning and evaluation-phase comparisons; rejected closed-loop continual-learning claims because TRACE does not apply or outcome-test its recommended context changes.
- `rg -n -i '^description:.*(trajectory|trace|change candidate|feedback|session|context remediation|root cause)' kb/reference --glob '*.md'` — evaluated the trajectory-aware workflow-evaluation proposal and Commonplace gap-plan material; neither is a direct description target for this source.
- `rg -n -i '^description:.*(trajectory|trace|feedback|context|skill|harness|self-improv)' kb/agent-memory-systems --glob '*.md'` — kept the trace-learning survey and ACE; evaluated the lightweight Trajectory-Informed review as a one-hop companion.
- `rg -n -i '^description:.*(trajectory|trace|feedback|context|self-improv|evaluation|retention)' kb/agentic-systems --glob '*.md'` — found no whole-system analysis whose actual claim was a stronger target than the retained note and memory-system candidates.
- `rg -n -i '^description:.*(trajectory|trace|dissatisfaction|root cause|feedback loop|context layer|context engineering|harness)' kb/sources --glob '*.md' --glob '!**/.snapshots/**'` — kept the Meta-Harness, Trajectory-Informed Memory Generation, AutoResearchEval, and self-healing-harness ingests as named comparisons.

**Body searches:**

- `rg -n -i 'dissatisfaction|user correction|trajectory mining|trace-extracted|execution trace' kb/notes --glob '*.md'` — confirmed that TRACE's implicit-correction trigger and full-trace attribution bear directly on the trace-learning and diagnostic-richness claims.
- `rg -n -i 'diagnostic richness|root cause|hypothesis to verify|candidacy evidence|authoritative source' kb/notes --glob '*.md'` — kept the candidacy-evidence note because TRACE separates a root-cause candidate from active source-file inspection and later human approval.
- `rg -n -i 'content gap|stale content|CREATE|UPDATE|path health|silent fail' kb/notes --glob '*.md'` — surfaced final-task/path-health and KB-learning candidates; the former was rejected because TRACE's worked answer is corrected by the user rather than accepted as a successful final outcome.
- `rg -n -i 'readable artifact|context layer|deploy-time|behavio(u)?r-changing write' kb/notes --glob '*.md'` — confirmed that TRACE reaches recommendation over readable context artifacts but stops before a governed behaviour-changing write.
- `rg -l -i 'execution trace|trajectory attribution|root cause|dissatisfaction|user correction|context source|context layer|active exploration|human review' kb/reference --glob '*.md'`, with analogous searches over `kb/agent-memory-systems`, `kb/agentic-systems`, and `kb/sources` — screened actual bodies rather than relying on metadata. The strongest retained comparisons were the trace-learning survey, ACE, and the four source ingests below.

**Link following:**

- Followed [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) to the trace-learning survey, Meta-Harness, Agentic Harness Engineering, and HALO. TRACE adds a different evidence regime: dissatisfaction-triggered attribution plus active inspection of authoritative context files, with a controlled active-versus-passive exploration ablation but no applied-fix rerun.
- Followed [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) to the checked-outcome and automated-KB-learning notes. TRACE operationalizes failure capture and investigation, but its evaluated endpoint is a recommended edit, not a verified durable rule or observed downstream improvement.
- Followed [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) to the automation-boundary and diagnostic-richness notes. TRACE attempts to automate comprehension in a soft-signal setting, but validates that attempt on a small synthetic corpus with gold fault labels.
- Followed [ACE](../../../../agent-memory-systems/reviews/ace.md) to the trace-learning survey and Trajectory-Informed Memory Generation. ACE supplies the closest implemented generator/reflector/curator loop, while TRACE separates detector, root-cause attribution, and source-exploring recommendation and retains a human application gate.

## Connections Found

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: TRACE's active-exploration ablation reports substantially better KB operation selection when the recommender reads authoritative context files instead of trusting upstream candidate locations, while its full-trace attribution design shows why terminal feedback alone is too thin for repair. The evidence is bounded by synthetic traces and bundled agent treatments.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — **is-evidence-for**: TRACE provides the note's requested second staged case outside idealization review: a dissatisfaction signal routes a trace to diagnosis, root-cause output remains a candidate for source-file inspection, and a recommendation still requires human approval before application.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **compares-with**: TRACE cleanly implements the early `fail` and `investigate` transitions and adds source exploration before recommending a mutation, but it does not apply the edit, rerun the task, or show that a generalized context rule earned verification authority.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — **compares-with**: TRACE attempts to automate comprehension from user dissatisfaction, complete trajectories, and context-source inspection in a softer domain than Meta-Harness; its synthetic gold-labelled evaluation supports feasibility without establishing that real production corrections can replace manual taxonomy and judge calibration.
- [Automating KB learning is an open problem](../../../../notes/automating-kb-learning-is-an-open-problem.md) — **compares-with**: TRACE targets a bounded subset of the proposed learning loop by recommending `CREATE`, `UPDATE`, or `DELETE` operations over knowledge-base and other context files, but stops before accepted application, downstream task testing, retirement, or open-ended question-answering evaluation.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — **is-evidence-for**: TRACE adds a source-grounded trajectory-to-recommendation subtype with an implicit user-correction trigger, whole-trace reverse attribution, active context-file exploration, multiple readable context targets, and human-gated promotion. Its paper-only evidence tier and absent applied-update loop should remain explicit.
- [ACE](../../../../agent-memory-systems/reviews/ace.md) — **compares-with**: both split task feedback into specialized analysis and curation roles over readable context, but ACE automatically adds playbook content under task correctness feedback and measures later task performance, whereas TRACE diagnoses user dissatisfaction across prompts, KBs, tool prompts, and skills and emits file-specific recommendations for human review.
- [Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — **compares-with**: both use rich execution evidence to improve the context or harness around a fixed model; Meta-Harness searches executable candidates under hard benchmark oracles and runs them, while TRACE begins from explicit or implicit dissatisfaction and evaluates attribution and recommendations without applying the proposed context change.
- [Trajectory-Informed Memory Generation for Self-Improving Agent Systems](../../../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) — **compares-with**: both use three-stage trajectory analysis to produce inspectable, non-weight context artifacts, but the IBM system distills outcome-labelled runs into reusable tips and tests prompt-time reuse, while TRACE attributes one dissatisfaction event to existing context sources and recommends file CRUD behind a human gate.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) — **compares-with**: both diagnose failures by inspecting evidence beyond the final answer; AutoResearchEval applies an artifact-aware taxonomy and measures diagnostic agreement, while TRACE works backward from a user correction to a context-layer cause and proposed repair. Neither study isolates actual downstream improvement from applying the diagnosis.
- [The Self-Healing Agent Harness](../../../../sources/the-self-healing-agent-harness-2048912026018484317.ingest.md) — **compares-with**: both turn post-deployment dissatisfaction into engineering work, but the practitioner loop claims an operational path through tickets, fixes, re-grading, and rollout gates, whereas TRACE contributes the explicit trajectory-attribution and context-source-recommendation middle stages and evaluates them synthetically.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — rejected as load-bearing evidence: TRACE's worked procurement answer has apparently successful tool calls, but the user explicitly corrects the final answer; it therefore does not instantiate the note's narrower condition in which intended-path and fallback success share the same accepted terminal outcome.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) and [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — rejected as direct evidence: TRACE selects readable context files and proposes mutations, but its evaluated system does not install, regression-test, retain, or read back the changes, so calling it a continual-learning loop would erase the governance boundary those notes defend.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — rejected in favor of the narrower phase-gated-evaluation comparison: the human approval gate is architecturally consistent with the general principle, but TRACE does not compare automated application against human verification or identify approval as the causal boundary.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — rejected as a direct reference edge: both inspect trajectories, but the proposal specifies Commonplace's evaluation of workflow transformations, while TRACE evaluates dissatisfaction attribution and recommendation quality in an external context-engineering system.
- [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — rejected as a direct comparison because TRACE does not yet cross the first boundary that paper measures: its recommendations are not applied as harness updates, so there is no update-versus-uptake result to compare.
- [Agentic-system collection](../../../../agentic-systems/README.md) — no individual whole-system analysis survived full-artifact screening; TRACE is presently better represented as a paper-grounded context/trace-learning method than as evidence about one reviewed runtime or orchestration framework.

## Index Membership

None

## Synthesis Opportunities

- TRACE, the candidacy-evidence note, and the governed-write notes together expose a four-transition repair ladder: dissatisfaction licenses diagnosis; trace evidence licenses a root-cause candidate; authoritative-source inspection licenses a proposed edit; only applied outcome evidence can license retention as an improvement. TRACE evaluates the middle transitions but labels recommendation quality as end-to-end fix effectiveness. A future note could make the transition-specific warrants explicit without treating recommendation, application, and benefit as one outcome.

## Maintenance Observations

None

## Flags

- Evidence boundary: the paper's `End-to-End Fix Effectiveness` is an LLM-judge assessment of the recommendation against synthetic ground truth, not an applied context mutation followed by a rerun or renewed user feedback. The ingest should preserve that distinction.
- Split candidate: the paper makes independent contributions about dissatisfaction detection, trajectory-level root-cause attribution, and active context-source exploration/recommendation across evaluation, trace learning, and KB maintenance. Promotion should extract one claim at a time even if one ingest analyzes the full paper.
- External-validity boundary: 75 synthetic traces from six fault templates support component measurement, but the reported production deployment is proprietary and not independently inspectable; even the detector's perfect result does not distinguish TRACE from the vanilla baseline, which was also perfect on this set.
