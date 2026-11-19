---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/asi-bench-at-the-dawn-of-artificial-superintelligence.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: ASI-Bench: At the Dawn of Artificial Superintelligence

**Source:** [ASI-Bench: At the Dawn of Artificial Superintelligence](../../../../sources/.snapshots/asi-bench-at-the-dawn-of-artificial-superintelligence.md)

The snapshot is immutable. The outbound candidates below are for a future matching authored source surface, normally an ingest, rather than edits to the snapshot.

## Discovery Trace

**Source reading:**

- Read the complete snapshot and extracted its matched B1–B4 guidance design, Agent×Model evaluation unit, project-level executable tasks, reference artifacts and scoring, aggregate results, cost measurements, and stated scope. The central result is a large B1→B2 loss when full procedures are withdrawn, smaller B2→B3 and B3→B4 differences, and material variation between harnesses using the same model.
- Read the source collection contract and retained only authorised destinations and labels. Local prospecting covered notes, reference, sources, agent-memory-systems, and agentic-systems. Work and instructions were excluded. External prospecting was skipped because no external target was supplied and external is not an open-web prospecting surface.
- No semantic search or scoring tool was used, so no numeric candidate scores were available.

**Curated heads and complete listings:**

- Read the destination heads at "kb/notes/README.md", "kb/reference/README.md", "kb/sources/README.md", "kb/agent-memory-systems/README.md", and "kb/agentic-systems/README.md". Also read the relevant notes topic heads "kb/notes/evaluation-README.md" and "kb/notes/llm-reliability-README.md".
- The source has no tags, so no matching tag README or by-tag description scan applied.
- Generated each authorised destination's complete title surface once with "rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'". Generated each complete description surface once with "rg '^description:' kb/<destination>/ --glob '*.md'".

**Notes:**

- Ran "rg -n -i 'methodological guidance|procedural guidance|guidance gradient|method operationalization' kb/notes/ --glob '*.md'"; no direct term match survived.
- Ran "rg -n -i 'autonom(y|ous).*benchmark|benchmark.*autonom(y|ous)|measuring autonomy' kb/notes/ --glob '*.md'", "rg -n -i 'harness.*(model|capabil)|model.*harness|client fixed' kb/notes/ --glob '*.md'", and "rg -n -i 'fixed (task|objective|evaluation)|fixed.*(task|objective|evaluation)' kb/notes/ --glob '*.md'". These led to the retained client-fixed, treatment-grain, and known-target benchmark candidates.
- Ran "rg -n -i 'scaffold|underspecif|procedure' kb/notes/ --glob '*.md'" and retained the underspecified-instructions note because the matched guidance withdrawal supplies concrete evidence about the value of narrowing a procedure, with an explicit causal caveat.
- Ran "rg -n -i 'distractor|irrelevant context' kb/notes/ --glob '*.md'" and retained the soft-degradation note as a bounded comparison rather than general evidence against interference.
- Ran "rg -n -i 'incomplete (guidance|method)|partial guidance|constrain.*search.*guidance|guidance.*overhead|anchoring|anchor.*guidance|method name' kb/notes/ kb/sources/ --glob '*.md'". This supported the synthesis opportunity about guidance completeness and alignment; it did not justify a new direct note edge.

**Reference:**

- Ran "rg -n -i 'methodological guidance|guidance gradient|autonomous research' kb/reference/ --glob '*.md'", "rg -n -i 'ablation|held.*fixed' kb/reference/ --glob '*.md'", and "rg -n -i 'harness.*model|model.*harness' kb/reference/ --glob '*.md'".
- The ablation-baselines proposal was the closest hit, but it specifies a Commonplace review design rather than explaining ASI-Bench or receiving evidence from it. No reference candidate passed the reader-need test.

**Agent-memory systems:**

- Ran "rg -n -i 'scientific research|research agent' kb/agent-memory-systems/ --glob '*.md'", "rg -n -i 'harness.*model|model.*harness' kb/agent-memory-systems/ --glob '*.md'", and "rg -n -i 'methodological guidance|procedural guidance|instruction guidance' kb/agent-memory-systems/ --glob '*.md'".
- Retained Agentic Harness Engineering because ASI-Bench's same-backbone harness comparisons provide an empirical counterpart to that review's fixed-model, editable-harness mechanism. Other research-agent hits described systems but did not add a sharper traversal need.

**Agentic systems:**

- Ran "rg -n -i 'model.*harness|harness.*model' kb/agentic-systems/ --glob '*.md'", "rg -n -i 'benchmark|evaluation' kb/agentic-systems/ --glob '*.md'", and "rg -n -i 'guidance|underspecif|scientific research' kb/agentic-systems/ --glob '*.md'".
- Retained AI Agents in Depth because its model-plus-Harness evaluation prescription is directly instantiated by ASI-Bench's Agent×Model configurations and same-model harness differences.

**Sources:**

- Ran "rg -n -i 'methodological guidance|procedural guidance|guidance gradient|autonomous scientific research' kb/sources/ --glob '*.md'", "rg -n -i 'instruction surfaces|specification detail|guidance' kb/sources/ --glob '*.md'", and "rg -n -i 'harness.*model|model.*harness' kb/sources/ --glob '*.md'".
- Ran "rg -n -i 'distractor|irrelevant context' kb/sources/ --glob '*.md'" and "rg -n -i 'project-level|long-horizon.*scient' kb/sources/ --glob '*.md'".
- Retained SWE-bench Science for its scientific-task guidance ablation, CRUX for its contrasting authentic open-ended evaluation design, GSM-DC for its controlled distractor result, and AutoResearchEval for its complementary trajectory-and-artifact failure analysis. DiscoverPhysics was evaluated but rejected because its counterfactual anti-recall design is less diagnostic of ASI-Bench's guidance and autonomy claims than the retained comparisons.

**Link following:**

- Followed the client-fixed and treatment-grain notes to their linked benchmark, autonomy, and prompt-variation neighbourhoods. This surfaced the known-target benchmark note and confirmed that the technical autonomy definition should not be conflated with ASI-Bench's guidance levels.
- Followed the underspecified-instructions note to the executor-choice boundary note; the latter was rejected because ASI-Bench does not test which individual choices are safely determinable.
- Followed the soft-degradation note into its irrelevant-context evidence, which exposed the bounded B3/B4 versus GSM-DC tension.
- Followed Agentic Harness Engineering and AI Agents in Depth through their harness-evaluation discussions, and followed the retained source ingests through their benchmark comparisons. These checks did not reveal a more specific local target than those retained below.

## Connections Found

- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](../../../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — **is-evidence-for**: ASI-Bench holds the objective, data, required artifacts, and evaluation fixed while varying methodological help. Its design therefore supplies a concrete instance of difficult client-side choices being exported from the measured autonomy, without invalidating the benchmark's narrower comparison.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: B1→B2 removes a bundle of equations, procedures, and parameters, while B2→B3 removes the remaining named-method guidance. The paper's method-operationalization interpretation is warranted only at those treatment grains.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **is-evidence-for**: all 60 tasks have predefined objectives, reference-generation artifacts, and executable scoring. ASI-Bench measures whether agents can reach verifiable scientific artifacts under controlled guidance, not prospective problem selection, value judgement, or acceptance of a new result.
- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — **is-evidence-for**: withdrawing full procedural detail while preserving the task and evaluation causes a large performance loss, giving concrete evidence that narrowing the procedural search space matters. The comparison does not isolate semantic ambiguity from missing technical knowledge or execution burden.
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — **compares-with**: ASI-Bench's factually correct distractor condition has essentially the same aggregate score as B3 (26.99 versus 26.62). This bounded null result helps delimit when irrelevant context does not produce the interference reported elsewhere; it is not evidence that contamination is harmless in general.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) — **compares-with**: ASI-Bench evaluates several harnesses with the same model backbone and reports material score differences. That finding is an empirical counterpart to Agentic Harness Engineering's treatment of the harness around a fixed model as an editable system target.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) — **compares-with**: the book argues that evaluation should target the model-plus-Harness system using typed tasks, resets, trajectories, and verifiers. ASI-Bench operationalizes that unit as Agent×Model configurations and exposes same-backbone harness effects.
- [SWE-bench Science full paper on scientific-software repairs](../../../../sources/swe-bench-science-arxiv-2608-19799.ingest.md) — **compares-with**: both sources evaluate agents on executable scientific tasks and vary supplied guidance. ASI-Bench finds a large aggregate benefit from complete procedures, whereas SWE-bench Science finds auxiliary guidance can help one configuration and hurt another, making completeness and harness alignment salient comparison variables.
- [Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) — **compares-with**: ASI-Bench trades authenticity for breadth and controlled, executable known-target scoring across 60 tasks. CRUX uses only two unpublished questions but retains original-expert judgement and genuine unknown-to-the-agent research, exposing a different oracle-versus-authenticity tradeoff.
- [How Is LLM Reasoning Distracted by Irrelevant Context?](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — **compares-with**: ASI-Bench's B3/B4 comparison finds no aggregate penalty from one plausible irrelevant-information block, while GSM-DC varies distractor count and placement and finds systematic degradation. Together they identify distractor dose, placement, task horizon, and harness as boundary variables rather than supporting an unconditional robustness claim.
- [How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) — **compares-with**: ASI-Bench isolates levels of methodological guidance and scores final artifacts, while AutoResearchEval inspects artifacts and trajectories to localize failures by stage. The two evaluation surfaces distinguish a treatment effect from a diagnosis of where the induced failures occur.

## Bidirectional Candidates

- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](../../../../notes/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) ↔ source — **evidenced-by**: ASI-Bench is a worked case in which the benchmark supplies task choice, objectives, data, and acceptance criteria while assigning methodological execution to the agent.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) ↔ source — **evidenced-by**: the B1–B4 construction is a useful concrete example of why an interpretation must stay at the level of the bundle actually removed.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) ↔ source — **evidenced-by**: ASI-Bench's reference artifacts and fixed scoring make it a project-level instance of known-target reachability presented with a broader discovery claim.
- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) ↔ source — **evidenced-by**: the B3/B4 result is a useful bounded null case for the note's claim, provided the link preserves the benchmark's single distractor treatment and aggregate scope.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) — rejected because B1 supplies guidance that the agent must still execute; it does not precompute and insert a result whose inputs were already known.
- [Fix what the executor cannot determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — rejected because ASI-Bench measures performance and cost under bundles of guidance, not whether a particular choice is safely determinable from authority and evidence.
- [Measuring autonomy well enough to see it improve is an open problem](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — rejected because that note defines autonomy as technical actor allocation by function, whereas ASI-Bench uses methodological autonomy for the amount of guidance withheld. A direct edge would encourage vocabulary conflation.
- [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — rejected because same-model harness score differences concern evaluation of deployed behaviour, not evidence-responsive updating or learning.
- [Ablation baselines should preserve the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — rejected because the reference proposal governs Commonplace review objectives; the shared ablation vocabulary does not create a concrete reader need.
- [DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Discovery](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — rejected because its counterfactual physics construction tests anti-recall inference, while the retained CRUX, SWE-bench Science, and AutoResearchEval comparisons bear more directly on ASI-Bench's known-target, guidance, and diagnosis choices.

## Index Membership

None

## Synthesis Opportunities

- **Partial guidance can constrain search without paying down procedural reconstruction.** ASI-Bench's B2 condition is only modestly better than B3 but is the most expensive in tokens and time, while [SWE-bench Science](../../../../sources/swe-bench-science-arxiv-2608-19799.ingest.md) finds that auxiliary guidance helps one configuration and harms another. Together with [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), these results motivate a bounded hypothesis that guidance value depends on completeness and alignment with the executing harness, not mere presence. Establishing that claim would require matched ablations that vary completeness and alignment separately.

## Maintenance Observations

None

## Flags

- **Split candidate:** the snapshot supports at least five note connections across benchmark inference, instruction specification, known-target discovery, and context interference, and it makes several independent empirical claims. The immutable snapshot should remain intact, but a future authored source analysis should keep those claims separate rather than presenting “methodological autonomy” as one undifferentiated result.
- **Unresolved tension:** ASI-Bench's B3→B4 aggregate null result and GSM-DC's distractor degradation point in different directions. They are not a contradiction because distractor dose, placement, task structure, model, and harness differ; a matched dose-and-depth test is needed before generalizing either result.
