---
description: "Connection discovery for the Traverse and Scout full paper: trajectory evidence, diagnosis calibration, recovery, and verifier selection."
type: types/connect-report.md
source: kb/sources/.snapshots/locating-hidden-failures-paper.md
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: Locating Hidden Failures Makes Long-Horizon Agents More Reliable

**Source:** [Locating Hidden Failures Makes Long-Horizon Agents More Reliable](../../../../sources/.snapshots/locating-hidden-failures-paper.md). This is a local discovery report; durable edges belong in the [full-paper ingest](../../../../sources/locating-hidden-failures-paper.ingest.md), never in the immutable snapshot. Produced with `cp-skill-connect/SKILL.md` for an ingest drafting worker; all entries below are candidates.

## Discovery Trace

The source separates human error labels, LLM failure categorization, final task outcomes, safety judgments, and trained verifier selection. Its strongest KB relevance is the need to evaluate those targets separately. It does not demonstrate online correction or durable learning by the acting agent.

Read the source collection contract, snapshot type, connect-report type/schema, and report collection contract before judging candidates. Read notes and reference outbound contracts for reverse directions. Source authority permits notes, reference, agent-memory-systems, agentic-systems, sources, and tag prospecting; instructions and work were excluded. The snapshot has no tags, so no source-tag membership sweep applied.

**Common discovery commands.** Generated fresh complete title listings using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the six local destinations below. Scanned description matches using `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/tags/ --glob '*.md' | rg -i 'diagnos|recover|trajectory|verif|failure|scout|traverse'`. Ran the cross-destination body query `rg -n -i 'first.mistake|self.detection|root.cause|trajectory.aware' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/tags/ --glob '*.md'`. Searches were lexical; no similarity scores or external search service were used. Large outputs were reread in smaller source/document ranges or as stored title strings.

- **Notes.** Read `kb/notes/README.md`; followed the evaluation, LLM reliability, and observability tag heads. Title and description scans selected final-task-success, diagnostic-richness, enforcement-without-recovery, reasoning-production, and evaluation-automation. Full reads retained all five with the bounds below. Followed final-task-success's links to diagnostic-richness and recovery; diagnostic-richness's links to the trace-learning comparison and Agentic Harness Engineering; reasoning-production's links to process/output separation; recovery's links to oracle strength and teaching errors. These neighborhoods make outcome evidence, diagnosis, and repair distinct. Generic context-efficiency and memory-retention matches were rejected because the paper's rare memory-error labels do not evaluate KB retrieval or retention designs.
- **Reference.** Read `kb/reference/README.md`, its title surface, description matches, and the full trajectory-aware workflow evaluation proposal. The evaluation tag head independently routed to that proposal. Followed its evidence link to AutoResearchEval. Kept the proposal because it already specifies the missing local experiment, including localization, false positives, length sensitivity, and cost. Calibration-fixture and review-system architecture hits were not retained: they add an indirect generic evaluation route where the specific proposal is available.
- **Agent memory systems.** Read `kb/agent-memory-systems/README.md` and the trace-learning tag head, then generated titles and description matches. Ran `rg -l -i 'recovery|verifier|diagnostic' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`. Read Agent-R and inspected the diagnostic-richness link neighborhood in the trace-learning comparison. Retained Agent-R because its first-error localization feeds revision training, making the consumer of a localization an explicit comparison axis. HALO and Agentic Harness Engineering offer trace navigation and repair pipelines, but are redundant here with diagnostic-richness and Agent-R; broad filesystem-memory systems fail the articulation test.
- **Agentic systems.** Read `kb/agentic-systems/README.md`, all titles, selected descriptions, and the shared body queries above. Read the current Reflexion HotPotQA review. Kept it because its diagnosis enters the next attempt while an outcome oracle still cannot verify the explanation. Ecdysis and other harness optimization hits are a more distant comparison to Scout's frozen-agent selection intervention; no second harness-system link is needed.
- **Sources.** Read `kb/sources/README.md`, its titles and selected descriptions. Read AgentScope's diagnosis ingest and the prior abstract-page ingest; inspected AutoResearchEval through the proposal and its ingest. Kept AgentScope for the disagreement between first mistake and greatest-impact failure, AutoResearchEval for detection without repair, and the abstract-page ingest for the newly available methods. The matching full-paper ingest is the authored companion, not an independent corroborating source or a duplicate connection. Related verifier, harness, and memory papers were rejected where they added only broad topic overlap.
- **Tags.** Read `kb/tags/README.md` and the evaluation, LLM reliability, observability, and trace-learning heads. Generated the titles and description matches and included tags in the body search. None of those heads declared `complete: true`; no completeness skip was used. Evaluation and observability are useful optional index routes. Trace-learning has a system-review-specific inclusion condition, so it is not a suggested tag for this source ingest. The sources contract names tags as a prospecting destination but supplies no outbound label to tags; keep these as index suggestions, not invented formal edges.
- **External.** Evaluated only the source URL already present in the snapshot, `https://arxiv.org/abs/2609.17930`. No external prospecting was performed.

## Connections Found

- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: both show that endpoint success leaves route properties unresolved. The paper's harmful successful runs concern safety and task errors; the note concerns prescribed paths, fallback, and infrastructure health. Preserve that difference rather than treating the paper as a test of the fallback mechanism.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: step labels and localized failures contain diagnostic information absent from final success labels. Scout tests localization and selection, whereas the note's central target is evidence available to a proposer; the paper does not independently test outer-loop repair quality.
- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) — **is-evidence-for**: the within-domain noticed-versus-unnoticed comparison in Figure 7 separates recognizing a mistake from subsequently solving the task. It bears on the note's missing-follow-through problem but does not test its proposed corrective/fallback/escalation policy or establish that noticing has no causal effect.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — **compares-with**: Traverse evaluates a distinct process-localization target on which general-purpose judges struggle; the note separates answer production from path checking. The paper does not isolate answer-confirmation bias as the cause of judge errors.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) — **is-evidence-for**: human-verified error annotations followed by specialized verifier training provide a bounded instance of constructing a discriminative evaluator from observed failure. The result neither proves the sequence necessary nor isolates the taxonomy's contribution.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: the existing proposal is the concrete local destination for testing harmful-success cases, first-error localization, false alarms, and audit cost. Scout's retrospective selection result does not meet the proposal's adoption criteria.
- [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md) — **compares-with**: both exploit first-error localization, but Agent-R uses it to synthesize actor revision training while Scout learns verifier weights and selects among completed attempts from an unchanged actor. This prevents equating a better selector with an agent that learns to repair its mistakes.
- [Reflexion HotPotQA reasoning agents](../../../../agentic-systems/reviews-archive/reflexion.md) — **compares-with**: Reflexion places a retained diagnosis into the next attempt; Scout's demonstrated selection use does not. Both require separating a correct eventual answer from validation of the failure explanation that informed the process.
- [Diagnosing Agent Failures via Behavioral Abstractions](../../../../sources/diagnosing-agent-failures-via-behavioral-abstractions.ingest.md) — **compares-with**: Traverse labels first mistakes in naturally occurring trajectories, while AgentScope selects greatest downstream impact and evaluates partly on injected failures. The comparison forces the failure target and data construction to be stated before comparing localization accuracy.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) — **compares-with**: both expose process failures hidden by endpoint judgments and distinguish noticing a flaw from repairing it. AutoResearchEval's artifact-aware bundled judge and open-ended research tasks differ from Traverse's first-error target and Scout's selector intervention.
- [Prior abstract-page ingest](../../../../sources/locating-hidden-failures.ingest.md) — **compares-with**: the full paper adds annotation definitions, candidate-pool controls, reward design, and source inconsistencies absent from the prior secondary capture. In particular, fixed candidate pools answer part of the prior ingest's selector-comparison uncertainty while leaving online prevention untested.
- [Original paper](https://arxiv.org/abs/2609.17930) — **derived-from**: the ingest's source-side reconstruction comes from this captured paper.

## Bidirectional Candidates

None. Useful return directions are stated separately below; none is proposed merely to mirror an outbound edge.

## Reverse-edge Candidates

- [Trajectory-aware evaluation proposal](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → full-paper ingest — **evidenced-by** under the reference contract: the paper bounds proposed workflow auditing with weak general-purpose localization, separate safety judgments, and a retrospective selector result. Add it as motivating and limiting evidence, not proof that the local intervention works.
- [Enforcement without structured recovery](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) → full-paper ingest — **evidenced-by** under the notes contract: Figure 7 supplies a bounded observation relevant to detection-versus-recovery, not corroboration of the complete recovery architecture. A future writer must retain the source support or mark the ingest link `snapshot required`.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — self-detection and memory-error counts do not isolate stored knowledge, retrieval, or activation; connecting them would risk importing a memory mechanism the paper does not test.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — the broad survey is useful discovery context, but Agent-R supplies the sharper comparison about where localized error evidence goes next.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — relevant generic background, already reachable through recovery and evaluation-automation; an extra direct edge adds little to this ingest.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) — optional source example for measuring localization separately from classification and final task success.
- [Observability](../../../../tags/observability-README.md) — optional source example of unsafe or flawed routes hidden by successful endpoint results. Use the tracked ingest if an index entry is later authored.

## Synthesis Opportunities

None. The existing trajectory-aware evaluation proposal already gathers the practical synthesis. A new broad note would duplicate that route before the local comparison has run.

## Maintenance Observations

- The snapshot contains unresolved publication placeholders and material internal inconsistencies. Examples include 2,620 versus 2,518 corpus counts; Figure 3's plotted silent-failure values versus caption values; Figure 7's restriction of the first-mistake analysis versus language elsewhere describing all runs with a mistake; and claims of detailed Scout localization/transfer results without a matching detailed results table. The reward discussion calls the all-correct labeling failure “over-flagging,” although that strategy misses errors. The ingest should preserve these limits rather than silently reconcile them.
- The prior abstract-page ingest and full-paper ingest represent different captured evidence boundaries. Keep both identities explicit; the full paper can resolve a stated abstract-level unknown without retroactively changing the earlier observation.

## Flags

- **Split candidate for downstream theory extraction:** five note connections span observability, diagnostic evidence, recovery, and evaluator construction. Keep this source ingest together, but do not turn those independent claims into one new omnibus theory note.
- **Causal scope:** step-to-step error association is not a controlled estimate that the first error causes every later error. Domain/harness comparisons do not establish harness irrelevance.
- **Evaluation target:** local task-error labels are not safety labels; the paper reports harm missed even by gold step labels. First-error analysis also excludes diffuse failures and must not stand in for all unsuccessful runs.
- **Intervention scope:** fixed-pool selector comparisons support selector quality under those pools. They do not demonstrate live interruption, rollback, safe candidate generation, or durable actor improvement.
- **Report status:** candidate discovery only. No library artifact, snapshot, index, or log was edited.
