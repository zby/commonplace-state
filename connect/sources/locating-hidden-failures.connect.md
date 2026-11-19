---
description: "Discovery context for Traverse failure localization and Scout trajectory selection, bounded to the captured abstract and editorial page"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/locating-hidden-failures.md"
source_has_frontmatter: true
date: "2026-09-20"
depth: standard
---

# Connection Report: Locating Hidden Failures Makes Long-Horizon Agents More Reliable

**Source:** [Captured abstract and editorial assessment](../../../../sources/.snapshots/locating-hidden-failures.md)

The future authored surface is the matching ingest. All entries are candidate edges; no library edges were changed. Discovery followed `cp-skill-connect/SKILL.md` through repository-local indexes, lexical searches, and one-hop reading. The source is a secondary publication containing the abstract, not the full paper.

## Discovery Trace

- Read source and reports collection contracts, connect-report type, and the complete target snapshot. Read the notes collection contract for reverse-edge authorization. Source-authorized destinations are notes, reference, agent-memory-systems, agentic-systems, sources, and already-known external pages. Instructions and work are excluded.
- Read each destination's `README.md`; the notes head routed to the evaluation and observability tag heads, both read. The source has no tags, so no matching-tag completeness shortcut applied.
- Generated the complete title surface once with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The combined response was truncated; focused title/description and body queries below supplied the evaluated shortlist rather than treating that response as exhaustive inspection.
- Across all five local destinations, ran `rg -n -i '^(#|description:).*(trajector|failure|recover|feedback|verif|judge|evaluat)' ... --glob '*.md'` and `rg -l -i 'first (mistake|error)|trajectory.*(diagnos|evaluat)|process.validity|silent.*fail' ... --glob '*.md'`. These identified the endpoint-health note, diagnostic-richness note, trajectory proposal, AutoResearchEval, AgentScope, TRACE, and Agent-S.
- **Notes:** Fully read endpoint-health, reasoning-production, evaluation-automation, and diagnostic-richness notes. Kept endpoint-health as a bounded comparison, and evaluation-automation as a reported empirical instance of human-verified failure annotations preceding a specialized verifier. Diagnostic-richness was kept as a comparison rather than direct proof of outer-loop learning. Followed endpoint-health's link to diagnostic-richness and the source ingests' links back to these notes. Rejected direct evidential use for reasoning-production because agent action failure localization does not establish answer-confirmation bias in argument grading.
- **Reference:** `rg --files kb/notes kb/reference | rg 'trajector|process.*evaluat|evaluat.*process|error.*correct|observab|reasoning-production|evaluation-automation'` located the exact trajectory-proposal path after an initial guessed filename failed. Read the proposal and kept it as the concrete local evaluation-design companion; the source does not validate its adoption criteria.
- **Sources:** Fully read AutoResearchEval, AgentScope, and TRACE ingests. Kept the first two for complementary failure taxonomies, evidence surfaces, and diagnosis endpoints. TRACE is a useful secondary comparison but omitted from the primary shortlist to avoid duplicating the diagnosis-versus-intervention distinction already supplied by AgentScope.
- **Agent-memory-systems:** Read Agent-S and checked `rg -n -i 'BBON|best.of|trajectory|^type:' kb/agent-memory-systems/reviews/Agent-S.md`. Its fact-caption pipeline and comparative trajectory selection supply a concrete comparison to Scout, without conflating ranking with durable memory learning.
- **Agentic-systems:** Read Agno AgentOS and ran `rg -n -i 'first mistake|verifier|trajectory' kb/agentic-systems/ --glob '*.md'`. Agno provides observation and recovery mechanisms but no sufficiently close comparative localization experiment; no outbound candidate retained. AI Agents in Depth discusses first-error attribution but would add a broad methodological companion already covered more directly by the proposal and notes.
- **External:** No web prospecting. The captured original page is already known and qualifies for the ingest's source-identity edge. The editorial's unrelated ScienceIDE nominee was rejected.

## Connections Found

- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: both separate endpoint success from route properties; the source reports harmful or fabricated-success routes, while the note analyzes successful fallback and infrastructure health. Do not claim the source measures the note's fallback mechanism.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — **is-evidence-for**: the reported human-verified failure corpus, failure taxonomy, trained verifier, and selection gains provide a bounded instance of turning inspected failures into discriminative evaluation. The abstract does not test whether that sequence is necessary.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: locating an error supplies information missing from final success, but Scout's reported selection gains concern choosing runs, not improving a later proposer from diagnostic evidence.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: this existing proposal supplies the local experiment needed before adopting trajectory judging; Traverse motivates failure localization and harmful-success cases without satisfying Commonplace's calibration, cost, or adoption conditions.
- [Diagnosing Agent Failures via Behavioral Abstractions](../../../../sources/diagnosing-agent-failures-via-behavioral-abstractions.ingest.md) — **compares-with**: compare a trained specialized verifier with a structured prompted diagnosis pipeline, and distinguish Traverse's first-mistake target from AgentScope's greatest-downstream-impact target before comparing localization results.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) — **compares-with**: both report trajectory-level failure taxonomies and failures hidden by outputs; AutoResearchEval adds artifact-aware judging and recognized-but-unrepaired flaws, whereas Traverse's abstract emphasizes first-error localization and rare self-detection. Their populations and annotation protocols differ.
- [Agent-S](../../../../agent-memory-systems/reviews/Agent-S.md) — **compares-with**: Scout and Agent-S BBON both use trajectory evaluation to choose candidate runs; BBON derives fact captions from screenshots/actions, while Scout is reported as a trained 4B failure verifier. Neither selection result alone establishes online prevention or durable agent learning.
- [Original captured publication](https://arxivb.org/abs/2609.17930) — **derived-from**: the future ingest analyzes this abstract-and-editorial publication, whose capture does not include full methods or experimental tables.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) could cite the future tracked ingest with **evidenced-by** for the limited human-annotation-to-verifier example. Author only after the ingest exists and source support is retained or explicitly requires its snapshot. No durable edge should target the snapshot or this cache report.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md): a plausible adjacent comparison, but the retained source does not diagnose conclusion-agreement substitution or mathematical reasoning evaluation; the sharper endpoint-health comparison is sufficient.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md): trace availability and restart mechanisms are not evidence of effective failure localization or equivalent to Scout's measured intervention.
- [TRACE](../../../../sources/trace-trajectory-attribution-for-automated-context-engineering.ingest.md): useful but lower-priority comparison between recommendation-only attribution and run selection; not needed alongside the more direct AgentScope comparison.

## Index Membership

None. Existing note and source links supply navigation; a broad tag-head addition is not justified for this secondary capture alone.

## Synthesis Opportunities

None. Endpoint-versus-path health and diagnosis-versus-selection are already represented in existing notes and comparisons.

## Maintenance Observations

None

## Flags

- The captured page combines paper abstract and automated editorial interpretation. Keep their claims separately attributed; online prevention and efficient active-loop deployment are editorial possibilities, not demonstrated results in this capture.
- A 4B verifier outperforming six frontier judges on localization does not establish that model scale is generally irrelevant, that all judging is weak, or that self-reflection cannot improve.
- Selection among completed candidate runs can improve final task success without preventing irreversible harm already incurred while generating them. Preserve this distinction in the ingest's practical recommendation.
- The abstract reports environment/task dependence of recovery rather than framework dependence, but the capture lacks the experimental controls needed to independently assess that attribution.
- No split signal: the shortlist spans evaluation, observability, and adjacent implementations of the same trajectory-diagnosis problem, rather than three independent claim areas needing separate source analyses.
