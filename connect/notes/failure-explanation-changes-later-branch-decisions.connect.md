---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/failure-explanation-changes-later-branch-decisions.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Failure explanations as later branch control

**Source:** [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the four heads matching the source tags: `foundations-README.md`, `learning-theory-README.md`, `deploy-time-learning-README.md`, and `self-improving-systems-README.md`. None declares `complete: true`; `learning-theory-README.md` declares `covered_by`, which is a routing guarantee rather than complete membership, so all four by-tag description scans were still required. The deploy-time-learning head exposed feedback quality as the closest index placement. The self-improving-systems head placed the claim between retrieval, addressable revision, and later operative dependence.
- Read the destination heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The memory-system and source heads led to retained-failure-learning cases; the other destination heads supplied no direct candidate.

**Title and description listing scans:**

- Generated a complete fresh title surface for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`, where `<destination>` was each of `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Generated the complete description surface for the same seven destinations with `rg '^description:' kb/<destination> --glob '*.md'`. The notes surface exposed the activation, intent-control, backtracking, controller-evaluation, second-order revision, mediation-trace, rationale-faithfulness, and oracle-accumulation candidates evaluated below.
- Ran the required by-tag scans for `foundations`, `learning-theory`, `deploy-time-learning`, and `self-improving-systems` with `rg -l '^tags:.*\bTAG\b' kb/notes --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These scans retained the activation, controller, revision, and mediation cluster. They also exposed broader learning and compounding notes that were rejected when their claimed outcome exceeded or preceded the source's later-branch-choice test.

**Body search:**

- `rg -n -i 'failure explanation|failed branch|disappointing branch|informative failure' kb/notes --glob '*.md'` and `rg -n -i 'later branch decision|branch decision|branch choice|scope.*priority|probe.*abandon' kb/notes --glob '*.md'` -- retained backtracking and controller evaluation as the two immediate search-control neighbors.
- `rg -n -i 'correct.*inert|critique.*inert|behaviorally inert|rationalization|rationalisation' kb/notes --glob '*.md'` and `rg -n -i 'retained.*failure|failure.*retained|lesson.*later|failed attempt.*later' kb/notes --glob '*.md'` -- retained contextual activation, second-order lessons, and the rationale-faithfulness distinction.
- `rg -n -i 'diagnostic richness|diagnos.*learning|explanation.*causal path|explanation.*later' kb/notes --glob '*.md'`, `rg -n -i 'change.*later (choice|decision|operation)|affect.*later (choice|decision|operation)' kb/notes --glob '*.md'`, and `rg -n -i 'retriev.*lesson|contextual activation|consumption path|mediation trace' kb/notes --glob '*.md'` -- separated explanation quality, exposure, causal uptake, and later benefit. The diagnostic-richness note contributes to synthesis but does not by itself answer the source's uptake question.
- `rg -n -i 'counterfactual.*(choice|decision|alternative)|withhold.*(choice|decision)|replace.*(choice|decision)|distinguish.*live alternative|changes? which .*alternatives|behavioral.*counterfactual' kb/notes --glob '*.md'` -- confirmed that the intent-control note and mediation-trace note provide the closest existing counterfactual decision tests.
- `rg -n -i 'branch decision|search control|behavioral authority|causal path|failure explanation|retained lesson' kb/types --glob '*.md'` returned no type-level candidate.
- `rg -n -i 'branch decision|search control|failure explanation|retained lesson|critique.*(action|revision)|decision.*rationale|rationale.*decision' kb/reference --glob '*.md'` surfaced descriptive rationale-retention material, but no Commonplace reference artifact supplies a distinct case or mechanism for the source claim.
- `rg -n -i 'failed (attempt|trajectory)|failure (lesson|explanation|reason)|retained lesson|memory.*(later|future)|causal.*(behavior|action)|faithfulness tested' kb/agent-memory-systems --glob '*.md'` surfaced ReasoningBank, G-Memory, and several related memory implementations. Their reviewed paths establish retention and injection, but their own faithfulness fields say that no fired-memory intervention or post-action audit establishes a changed later decision.
- `rg -n -i 'failed branch|failure explanation|critique.*(plan|revision|action)|backtrack|abandon.*branch|later decision|retained lesson' kb/agentic-systems --glob '*.md'` supplied no agentic-system case closer than the tracked source evidence.
- `rg -n -i 'correct critique|behaviorally inert|uncorrected self-awareness|failed branch|failure explanation|retained lesson|critique.*(plan|revision|action)|later decision' kb/sources --glob '*.md'` retained CRUX and AutoResearchEval as negative empirical anchors. It also surfaced KSI, Recuris, and AutoSaddler as positive architecture or aggregate-outcome cases whose evidence does not identify one retained explanation as the cause of a later branch choice.
- `rg -n -i 'critique.*(block|revise|resolve)|review.*(block|revise|resolve)|unresolved.*(failure|finding|warning)|failure.*disposition|branch decision|search control' kb/instructions --glob '*.md'` found review and fix procedures, but none adds a general ordering, default, or stopping condition that operationalizes this methodology note closely enough for `operationalized-from`.
- External prospecting was skipped because no external target was supplied or already loaded. The relevant evidence already has tracked local ingests.

**Link following:**

- Followed both authored source links. The lightweight-control note supplies the branch-allocation boundary, while the theory-mediated note already supplies the full interpretation-retention-read-back-continuation ladder and links onward to program theory and mediation traces. A direct program-theory edge was therefore rejected as redundant, while the mediation-trace edge remained useful because the source explicitly conditions its claim on a causal path.
- Followed backtracking and search-controller evaluation one hop. They distinguish enacting a changed branch choice from evaluating whether repeated routing choices produce useful consequences. Both add a non-redundant reader path.
- Followed contextual activation, intent control, second-order lessons, selective revision, and the mediation trace one hop. Together they separated four questions: was the explanation available, did it enter the decision, did it faithfully locate the failure, and did the later choice actually change?
- Followed the diagnostic-richness and oracle-accumulation neighborhoods. Diagnostic richness is an upstream constraint on explanation quality; oracle accumulation develops the different lesson and maintained-check delivery wires. Neither directly establishes the source's retained-explanation-to-choice edge, though diagnostic richness contributes to the synthesis opportunity below.
- Read the full CRUX and AutoResearchEval ingests. CRUX records fifteen self-review rounds in which central concerns led mainly to caveats or narrower claims rather than project-level replanning. AutoResearchEval reports uncorrected self-awareness in 660 of 800 analyses and the same 82.5% review-to-revision shortfall as a severe-flaw-recognized-but-shipped pattern. Their scopes and confounds remain those stated in the ingests.
- Read the ReasoningBank and G-Memory reviews and the relevant KSI, Recuris, and AutoSaddler ingest sections. Each positive system moves failure-derived material into a later context or reports aggregate benefit, but none supplies the specific causal audit required by the source claim.
- Searched inbound links with `rg -n --fixed-strings 'failure-explanation-changes-later-branch-decisions.md' kb --glob '*.md'`. The only hit was `kb/work/theory-mediated-self-improvement-series/shared-model.md`; `kb/work/` is excluded by the notes collection contract, so no library artifact already authors a return path.
- Read the full claims, scopes, caveats, and relevant-link surfaces of every retained candidate. All retained and rejected targets below have frontmatter, and all 21 candidate and index paths were verified to exist.

**Per-destination disposition:**

- `notes` (including `notes/definitions`): seven outbound candidates passed the articulation and label tests. Six warrant useful return paths. No source term required a `defined-in` edge.
- `types`: no type contract supplies a case, definition, or mechanism specific to failure explanations changing branch decisions.
- `reference` (including `reference/definitions`): rationale-retention documentation describes Commonplace surfaces but does not establish later causal uptake, so no candidate passed.
- `agent-memory-systems`: ReasoningBank and G-Memory passed the structural-retention screen but failed the source's changed-decision evidence threshold; they remain useful rejections rather than connections.
- `agentic-systems`: no inspected system record supplied a closer or better-bounded case than the source ingests.
- `sources`: CRUX and AutoResearchEval passed as bounded negative evidence. KSI, Recuris, and AutoSaddler did not identify a specific retained failure explanation as the cause of a later branch decision.
- `instructions`: no procedure met the narrow `operationalized-from` trigger.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **exemplifies**: a retained failure explanation is a concrete case of knowledge that can be correct, stored, and even visible without becoming active; the source makes changed branch choice the task-specific activation surface.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- **contrasts**: prospective intent and retrospective failure explanation are different control inputs, but both acquire local force only by changing admissibility, priority, further search, or stopping among live alternatives.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **mechanism**: restoring an earlier usable state and redirecting search is one concrete way a retained explanation can change continuation or abandonment rather than remain commentary.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) -- **mechanism**: addressable prior commitments make the source's rejection, rescoping, and revised-test outcomes available as explicit operations instead of only indirect behavioral change.
- [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) -- **enables**: a contemporaneous citation supplies the minimum checkable record for auditing whether the retained explanation entered the later decision's causal path, while the source's changed-choice test remains the stronger evidence of load-bearing use.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **extends**: changing one later branch choice establishes operative control, not that the control is good; controller evaluation adds the distributional test over valuable candidates, discriminating evidence, informative failures, and recovery under matched conditions.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **contrasts**: rationale faithfulness and behavioral uptake are independent gates—a faithful explanation can remain inert, while an operative but unfaithful explanation can redirect search at the wrong premise.
- [Ingest: Can AI Agents Conduct Open-Ended AI Research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) -- **evidenced-by**: across fifteen self-review rounds, agents surfaced concerns later emphasized by expert reviewers yet mostly narrowed claims or added caveats instead of changing project plans, abandonment decisions, or project-level search.
- [Ingest: How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) -- **evidenced-by**: the study reports severe flaws recognized but left unrepaired in 660 of 800 analyses, a bounded large-sample instance of critique existing in the trajectory without governing the later delivery decision.

## Bidirectional Candidates

- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) <-> source -- **contrasts** in both directions: one note tests prospective intent and the other retained failure explanation, making the shared live-alternative discrimination criterion and the different temporal roles explicit.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) <-> source -- source to backtracking is **mechanism**; backtracking to source is **extends**, because the failure-explanation note specifies which retained contrary evidence can justify returning and redirecting rather than merely making restoration available.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) <-> source -- source to second-order lessons is **mechanism**; second-order lessons to source is **extends**, because the source supplies the later-choice criterion that distinguishes an available reject/rescope/revise operation from an operative lesson.
- [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) <-> source -- source to the trace is **enables** for record-based audit; the trace to source is **extends**, because a changed later branch decision is the stronger behavioral evidence that the cited explanation was load-bearing rather than decorative.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) <-> source -- source to controller evaluation is **extends**; controller evaluation to source is **mechanism**, because retained explanations convert informative failures into changed future routing, one route by which a controller's downstream consequences can improve.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) <-> source -- **contrasts** in both directions: the two notes isolate rationale fidelity and behavioral uptake as failure surfaces that neither readability nor later action collapses into the other.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- rejected as an upstream delivery failure. The source also covers an explanation that is retained and available yet leaves every later branch decision unchanged; contextual activation spans both boundaries more directly.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- rejected as a broader neighboring formulation whose action-model scope adds no failure-specific test beyond the closer intent-control and contextual-activation candidates.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected as a direct edge because it governs what explanation can be formed from the evidence, not whether a formed explanation changes a later branch; retained below only as part of a higher-order synthesis.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- rejected because its lesson/check wire distinction develops retention and delivery at a broader level, while it does not establish that a particular natural-language explanation caused a later choice.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- rejected as a redundant direct edge: the source's existing theory-mediated-self-improvement link already leads to this broader longitudinal program-modification application.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- rejected because the source permits a changed choice in the same episode and claims operative search control, while compounding requires a later improvement episode, a displaced productivity measure, and a causal contribution to gain or cost.
- [Ingest: Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) -- rejected despite its positive transfer result and traced claim splitting: the ingest explicitly leaves individual retained-claim causal faithfulness unresolved, so bundle-level gains do not establish the source's explanation-to-branch edge.
- [ReasoningBank](../../../../agent-memory-systems/reviews/reasoning-bank.md) -- rejected because the code-grounded review establishes failed-trajectory lesson induction, retrieval, and system-message injection but explicitly finds no with/without or post-action audit showing that selected memory changed behavior.
- [G-Memory](../../../../agent-memory-systems/reviews/g-memory.md) -- rejected because it extracts failure reasons, synthesizes insight rules, and pushes them into later prompts, yet its review finds no fired-memory faithfulness test and notes that reward feedback cannot identify which insight the agent followed.
- [Ingest: Recursive Experiential–Working Memory Evolution](../../../../sources/recursive-experiential-working-memory-evolution.ingest.md) -- rejected because code confirms that a failed trajectory can produce a procedure card supplied on the next attempt, but structural supply and aggregate paper outcomes do not trace that card to a changed later branch decision.
- [Ingest: AutoSaddler: Automatic Harness Optimization with Durable Updates](../../../../sources/autosaddler-automatic-harness-optimization-with-durable-updates.ingest.md) -- rejected because its diagnosis ablation supports the value of richer failure investigation within one optimizer, but does not identify a retained explanation as the cause of a particular later scope, probe, continuation, or abandonment choice.

## Index Membership

- [Deploy-time learning](../../../../tags/deploy-time-learning-README.md) -- add under **Feedback and signal quality**: the source supplies the missing uptake test between a diagnostically correct explanation and feedback that actually governs later search.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- add under **What reflection adds**: the source states the operative-use criterion for an addressable failure lesson after retrieval and before any claim that later operation depends on the revision.

## Synthesis Opportunities

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md), and the source together imply a three-gate failure-feedback pipeline not yet named in one artifact: retained evidence must support a discriminating diagnosis, the rationale must faithfully identify the premise or scope that broke, and that explanation must enter the causal path strongly enough to change later search. Passing any one gate does not establish either of the others.

## Maintenance Observations

None

## Flags

None
