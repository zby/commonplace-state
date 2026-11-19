---
description: "Pre-ingest connection discovery for Emerging Trends in AI Agent Evaluation: evaluation validity, trajectory evidence, judge calibration, reliability, and local comparison sources"
type: types/connect-report.md
source: "kb/sources/.snapshots/emerging-trends-ai-agent-evaluation.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: Emerging Trends in AI Agent Evaluation

**Source:** [Emerging Trends in AI Agent Evaluation](../../../../sources/.snapshots/emerging-trends-ai-agent-evaluation.md)

**Purpose and boundary:** Pre-ingest discovery only. The snapshot has frontmatter and was read completely, including references and Appendix A. Its central argument is that evaluation must cover the model–scaffold–tools–environment system, trajectories, deployment interactions, and evaluator choices rather than final-answer accuracy alone. Its mechanisms include component controls, repeated runs, human-validated judges, trace inspection, and explicit limits on generalization. It is an opinionated survey with illustrative citations and public-material snowball sampling, not a comprehensive systematic review or a new controlled evaluation.

All edges below are candidates, not authored state. The snapshot is immutable. Outbound recommendations belong in a future name-paired ingest; no such ingest was found by basename or source-identity search. Reverse recommendations must likewise target that tracked ingest once it exists, never the snapshot. The source link above is report-local input navigation, not a proposed durable citation.

**Method identity:** Repository-local discovery under `kb/instructions/cp-skill-connect/SKILL.md` and `kb/types/connect-report.md`; LLM judgments by `openai / gpt-6.1-sol` as reported by the runtime environment. No agents, external searches, MCP services, benchmark executions, or quantitative candidate scores were used.

## Discovery Trace

### Authorization and breadth

Read [sources contract](../../../../sources/COLLECTION.md) before discovery. Prospected theory, reference, historical agent-memory-systems, agentic-systems, tags, and sources. Excluded instructions and work. Used `compares-with` for named comparison axes, and sparing `see-also` for concrete Commonplace companions. No `abstracted-from` origin was inferred merely from thematic agreement, and survey recommendations were not treated as independent empirical corroboration.

The contract names tags as a scan destination but supplies no sources→tags relationship label. Tags were used as routing surfaces, not forced into outbound links. The [tags contract](../../../../tags/COLLECTION.md) also excludes sources from tag membership. The source has no `tags:` field, so no source-tag expansion was applicable. Neither topic head read below declares `complete: true`. The reserved external destination was not prospected; only the already-loaded original source URL was evaluated.

### Shared search procedure

Read each destination's `README.md`: [theory](../../../../theory/README.md), [reference](../../../../reference/README.md), [historical memory systems](../../../../agent-memory-systems/README.md), [agentic systems](../../../../agentic-systems/README.md), [tags](../../../../tags/README.md), and [sources](../../../../sources/README.md).

Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all six destinations. Reviewed the theory listing; for the other five, narrowed the generated surfaces with `rg -i 'evaluat|benchmark|reliab|judge|monitor|harness|saturat|log analysis|causal|inspect|cost|security|observab'`. This surfaced the trajectory proposal, calibration neighborhood, reliability paper, benchmark-auditing paper, and harness comparisons. Agentic-systems supplied no matches through this title filter; its description listing supplied candidates instead.

For each of the six destinations, ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'evaluat|benchmark|judge|monitor|causal attribution|reliability|trajectory'`. Then ran these actual body queries separately over every destination:

- `rg -l -i 'construct validity|model.{0,4}scaffold|pass@k|pass∧k|log analysis|outcome.only|trajectory.aware' kb/<destination>/ --glob '*.md'`
- `rg -l -i 'holdout|judge calibration|benchmark contamination' kb/<destination>/ --glob '*.md'`

These are bounded lexical searches, not semantic-recall guarantees. Candidate acceptance used full-document reading, not the presence of a matching word. Brief matches would have been resolved to their owning documents; no brief furnished a retained candidate.

### Theory

Read the [evaluation head](../../../../tags/evaluation-README.md) and [observability head](../../../../tags/observability-README.md) after the tags landing. Their curated groups routed to the experimental-contrast note, intended-path-health note, judge-comprehension note, reliability mapping, and trajectory proposal. Fully read the first four theory candidates and followed the intended-path-health note one hop to [diagnostic richness](../../../../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md), which was also fully read.

A focused check used `rg -n 'path deviation|outcome|diagnostic'` over the intended-path-health and diagnostic-richness files. Kept intended-path health for outcome/path non-identifiability, experimental contrast for component attribution, and comprehension for judge validation. Kept the reliability mapping as a comparison with qualifications, not as an established conversion of stochastic testing into proof. Diagnostic richness was evaluated but not retained as another outbound recommendation: the survey discusses evaluation diagnosis, not an intervention showing better subsequent proposals.

Read the complete [theory contract](../../../../theory/COLLECTION.md) for the reverse-edge pass. Its sources-directed `evidenced-by` permits qualification or bounding, while corroboration requires an attempted refutation. The proposed reverse theory edge below explicitly uses the former meaning.

### Reference

The landing, title scan, description scan, and body queries converged on [trajectory-aware evaluation](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) and [calibrating semantic gates](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md). Fully read both. The calibration proposal links the trajectory proposal and the comprehension note, closing a one-hop neighborhood rather than exposing a missing generic evaluation document.

Ran `rg -n -i 'calibrat|uncertainty|human|repeated'` on the calibration proposal. Its separate fixture-regression and field-calibration claims fit survey §§1d and 1h directly. Kept both proposals as unadopted local companions, not shipped capability. Read the complete [reference contract](../../../../reference/COLLECTION.md) before recommending a reverse source edge. Archived harness-capture and workflow proposals were not promoted: the live trajectory proposal is the useful current destination, and the reference contract excludes incoming library links to the proposal archive.

### Historical agent-memory-systems

The landing identifies this corpus as frozen. The descriptions surfaced [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md), Auto-Harness, Autocontext, and several trace-learning agents. Fully read Meta-Harness and checked its metric and leakage passages with `rg -n -i 'Pareto|cost|hold.out|leak' kb/agent-memory-systems/reviews/meta-harness.md`.

Kept one historical comparison because its accuracy/context frontier and distinct Terminal-Bench pass-rate objective give concrete examples for survey §1c; a broad spray across trace-learning systems would add no independent reader benefit. Followed the review/theory neighborhood to the [Meta-Harness paper ingest](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md). The latter was fully read for context but was not retained as a second edge to the same mechanism. No refresh or new source link into the frozen review is proposed.

### Agentic-systems

The landing names authored reviews and warns about the current comparison population. The description scan surfaced `fragility-grid`, `jaz-evals`, and other archived analyses. Fully read [fragility-grid](../../../../agentic-systems/reviews-archive/fragility-grid.md). Its pinned collector measures configuration sensitivity, but explicitly excludes full statistical methods and empirical results, and infers no autonomous-agent boundary. Rejected it as a main connection: it would distract from the survey's agent-specific causal and trajectory questions. Its one-hop exact-analysis pointer was re-filtered out for the same reason rather than expanding into a large historical run.

### Sources

The title and description scans surfaced reliability, benchmark auditing, CRUX, judge lifecycle, adaptive holdout reuse, and many harness papers. Fully read the reliability, automated-benchmark-auditing, CRUX paper, and adaptive-holdout ingests. Followed the CRUX paper ingest one hop to its earlier web-report ingest; they represent the same study and must not be counted as independent evidence. Followed the calibration proposal to the Netflix judge-lifecycle ingest and fully read it. Also fully read the Meta-Harness paper ingest through the theory/review neighborhood; retained the historical review rather than two overlapping edges.

Ran `rg -n 'emerging-trends-paper|Emerging Trends in AI Agent Evaluation' kb/sources/ --glob '*.md'`; no tracked matching ingest was found. Basename lookup also found none. The source's §1c explicitly cites the reliability paper, while CRUX's detailed two-case study and ABA are useful comparisons, not assumed exact citations of this survey. Rejected a second CRUX representation and a second Meta-Harness representation as redundant traversal.

### Tags and external

The tags title, description, and body searches converged on evaluation and observability. Both heads were read fully and used to reach documents. Membership is not proposed because sources do not participate in the tag namespace; no unavailable source→tags label was invented.

No open-web discovery occurred. The original PDF URL already present in the snapshot is the only proposed external source edge.

## Connections Found

These are outbound recommendations for the future ingest, not the snapshot.

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) — **compares-with**: the survey's §§1a and 1i show that identical successful outcomes can hide shortcuts or contamination; the note distinguishes intended-path success, equivalent fallback, and guarantee degradation. Following it helps a KB evaluator decide which path signals must be retained separately from artifact quality. Neither text says every fallback is harmful.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: survey §1e distinguishes model, scaffold, budget, environment, and interaction effects; the note turns that into an attribution-grain check. It helps a future ingest avoid assigning a whole-system result to a memory rule, instruction, or model without the relevant contrast.
- [Evaluation automation is phase-gated by comprehension](../../../../theory/evaluation-automation-is-phase-gated-by-comprehension.md) — **compares-with**: survey §§1h–1i recommend manual inspection, representative human-coded holdouts, and explicit judge-bias measurement; the note orders observed failures, failure taxonomy, and judge validation before optimization. The shared axis is what must be established before trusting automated review, not evidence that the survey experimentally validates the note's exact sequence.
- [Reliability dimensions map to oracle-hardening stages](../../../../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) — **compares-with**: survey §§1c–1d separate repeated-run consistency, perturbation robustness, and deployment-specific reliability. The note maps those questions onto evaluation engineering. The survey also bounds the mapping: repetition and pass∧k do not establish robustness, and repeatability alone does not turn a stochastic evaluator into a correctness oracle.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: the survey's §§1h–1i motivate evaluating actual trajectories and checking the judge itself; this live proposal supplies a local blinded output-only versus trajectory-aware comparison, false-positive accounting, evidence localization, and cost measurements. It is a candidate experiment, not an adopted requirement.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — **see-also**: survey §§1d and 1h call for repeated runs and representative human validation, including cases an automated judge passed. This proposal distinguishes known-case regression from live detection-rate evidence, giving a Commonplace operator a concrete place to assess those recommendations.
- [Meta-Harness historical review](../../../../agent-memory-systems/reviews/meta-harness.md) — **compares-with**: survey §1c recommends joint quality/cost reporting; this pinned review contrasts a classification accuracy/context-length frontier with a Terminal-Bench pass-rate-centered frontier. It makes the choice of optimization axis inspectable without asserting that the system satisfies the survey's complete evaluation agenda. Historical scope remains unchanged.
- [Towards a Science of AI Agent Reliability ingest](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) — **compares-with**: survey §1c cites this underlying reliability study. The ingest supplies the four-dimensional decomposition and its fixed-scaffold, two-benchmark limits, letting a reader distinguish the survey's general recommendation from the narrower empirical study.
- [Automated Benchmark Auditing ingest](../../../../sources/automated-benchmark-auditing-ai-agents-llms.ingest.md) — **compares-with**: survey §1b recommends auditing broken tasks and incorrect grading. ABA supplies concrete prompt/environment/grader audits and sampled confirmation, while its ingest separates auditor flag rate from confirmed prevalence and score sensitivity from capability gain. This is a usable comparison for designing KB evaluation checks, not proof that all flagged cases are defects.
- [CRUX two-case paper ingest](../../../../sources/crux-open-ended-ai-research-paper.ingest.md) — **compares-with**: survey §1l treats detailed open-world cases as complementary to typical-performance benchmarks. The CRUX ingest exposes the cost, human interventions, original-author grading, tiny population, and jointly changed model/scaffold that bound one such research evaluation. It prevents a future ingest from treating case-study rigor as population coverage or component attribution.
- [Adaptive data analysis and holdout reuse ingest](../../../../sources/generalization-adaptive-data-analysis-holdout-reuse.ingest.md) — **compares-with**: survey §1f warns against repeated optimization on holdouts; this ingest explains how feedback makes later candidates depend on reused data and which bounded-information protocols can restore guarantees under explicit assumptions. It supplies the mechanism behind an evaluation-exposure policy without transferring its formal theorems directly to semantic LLM review.
- [Netflix judge-lifecycle ingest](../../../../sources/lifecycle-llm-judge-recommendation-explanations.ingest.md) — **compares-with**: survey §1h asks how judges are validated and monitored; this case separates boundary-enriched regression, human-labelled production monitoring, and manual promotion/rollback. It adds an inspectable lifecycle example while preserving whole-pipeline attribution and the fact that the production drift-recovery branch had not fired.
- [Original survey PDF](https://sage.cs.princeton.edu/trends/emerging-trends-paper.pdf) — **derived-from**: the future ingest's source analysis is worked out from this already-supplied original source. No external retrieval or independent verification was performed during this connection pass.

## Bidirectional Candidates

None. Independent inbound reader needs are listed below rather than proposing mirrored links by default.

## Reverse-edge Candidates

Conditional on a tracked ingest being authored; none may point durably to the snapshot.

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) → future ingest — **evidenced-by**, qualifying context: survey §§1a and 1i locate outcome/path ambiguity within construct validity and explain why incomplete logs cannot certify clean execution. This would bound the note's telemetry implication, not claim independent experimental corroboration of its deduction. Authorized by the theory contract.
- [Trajectory-aware evaluation proposal](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → future ingest — **evidenced-by**, qualifying context: survey §§1h–1i provide an external methodological account of judge validation, false negatives, and missing trace evidence. This can bound what a positive local trajectory-judge result would establish; the survey is not evidence that Commonplace has implemented or validated that proposal. Authorized by the reference contract.

## Off-authorisation Candidates

None. Tag heads were discovery routes, not articulated document-edge candidates requiring an authorization extension.

## Raw Text Candidates

None. All retained document candidates have frontmatter. Untyped collection landings were used for navigation only.

## Rejected Candidates

- [fragility-grid review](../../../../agentic-systems/reviews-archive/fragility-grid.md) — its configuration grid is adjacent to robustness testing, but the inspected boundary is non-agent multiple-choice collection and resume. It excludes the full statistical analysis and adds little to the stronger experimental-contrast and reliability destinations.
- [Diagnostic richness constrains outer-loop learning quality](../../../../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md) — useful one-hop context, but survey §1i concerns diagnosing evaluations, not an intervention on proposer learning. Retaining it as additional evidence would blur diagnosis and demonstrated repair; the outcome/path note already provides the direct traversal benefit.
- [Earlier CRUX web-report ingest](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) — rejected as a second edge, not as bad evidence. The paper ingest explicitly identifies it as another representation of the same study and carries the needed limitations.
- [Meta-Harness paper ingest](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — rejected as a second recommendation to the same neighborhood. Its trace-access ablation concerns optimizer proposal quality rather than evaluation validity directly; the historical code-grounded review already supplies the concrete metric-frontier comparison.

## Index Membership

None. Sources are excluded from participating tag collections, and the sources landing does not enumerate individual ingests. Do not add the snapshot or future ingest as a tag member merely because evaluation and observability heads were useful during discovery.

## Synthesis Opportunities

None. The loaded notes already distinguish final outcome from path health, bundle effects from component attribution, and judge construction from optimization. The survey supplies breadth and comparison material, but this standard pass did not establish a missing higher-order claim that warrants a new note.

## Maintenance Observations

- The [reliability ingest](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) has stale downstream advice: it says no dedicated augmentation/automation note exists even though its linked [reliability mapping](../../../../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) now points to a standalone treatment. Its next action also names `kb/notes/` and recommends linking a snapshot, contrary to the current sources contract. These are later maintenance candidates only; nothing was repaired here.

## Flags

- **Broad-source extraction candidate:** More than five connections span trajectory observability, experimental attribution, reliability, judge governance, and contamination. The survey makes multiple independent assertions. Keep the captured survey intact and its identity in one ingest; if later writing extracts claims, separate those contribution clusters rather than importing the entire survey into one theory note.
- **Unresolved reliability tension:** The local reliability mapping describes repetition and safety constraints as hard-oracle moves. Survey §§1c–1d distinguish repeated success from environmental robustness, and §§1h–1i deny that clean monitoring proves absence of failures. Preserve this qualification; this discovery pass neither resolves the mapping nor establishes that a particular safety bound is decidable.
- **Pre-ingest gate:** No library edge is ready to author until the ingest exists. Source-dependent durable claims must cite that ingest and meet quote/snapshot-required grounding rules. No quotes were retained and no source analysis was written in this run.
- **Scope limit:** Part 3's funding, public-sector, legal, and disciplinary agenda was read but not expanded into links based only on general social relevance. The retained candidates change how a Commonplace reader designs or interprets KB evaluation.
