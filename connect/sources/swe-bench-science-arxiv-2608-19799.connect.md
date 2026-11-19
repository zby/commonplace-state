---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/swe-bench-science-arxiv-2608-19799.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connection Report: SWE-bench Science full paper (arXiv:2608.19799)

**Source:** [SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?](../../../../sources/.snapshots/swe-bench-science-arxiv-2608-19799.md)

## Discovery Trace

**Source contract and reading:**

- Read `kb/sources/COLLECTION.md` and `kb/cache/types/connect-report.md`. The snapshot is immutable; its name-paired ingest will be the authored connection surface. Authorised local destinations are notes, reference, sources, agent-memory-systems, and agentic-systems. Work and instructions are excluded.
- Read all 2,929 lines of the snapshot. Candidate-bearing material includes the public/private evaluation split, the four-category manual failure audit, and the 91-task paired auxiliary-information comparison. The paper explicitly calls the latter descriptive, says it does not establish statistical significance or a causal effect, and limits the anchoring account to case inspection.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The snapshot has no tags, so no tag-specific README was selected.
- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorised local destination: 360 titled Markdown artifacts in notes, 145 in reference, 173 in agent-memory-systems, 12 in agentic-systems, and 304 in sources.

**Description listing scan:**

- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised destination: 357 note descriptions, 144 reference descriptions, 171 agent-memory-system descriptions, 10 agentic-system descriptions, and 304 source descriptions.
- Ran `rg -n -i '^description:.*(contextual activation|diagnostic richness|fixed decomposition|experimental contrast|requirement.*objective|objective.*requirement|public.*private|visible.*test|hidden oracle)' kb/notes/ --glob '*.md'`. The exact-implementation note survived directly; contextual activation, diagnostic richness, experimental contrast, and fixed decomposition survived after body search and link following.
- Ran analogous focused description queries over reference, agent-memory-systems, agentic-systems, and sources using `(scientific|coding agent|benchmark|guidance|activation|public.*private)`. The Commonplace-specific ablation proposal, generic memory-faithfulness reviews, and whole-system analyses did not share a sufficiently specific mechanism. The same-paper AlphaXiv ingest, Harness-IF, and Agents Explore survived as source comparisons.

**Body search:**

- `rg -n -i 'scientific (information|guidance)|auxiliary information|anchoring|public tests|private tests|visible tests|hidden (tests|oracle)|exact repair|fixed decomposition|diagnostic richness|failure mechanism|contextual activation|downstream benefit' kb/notes/ --glob '*.md'` — confirmed the four strongest theory prospects and exposed the need to keep information presence, behavioral uptake, direction, and benefit separate.
- `rg -n -i 'scientific (information|guidance)|auxiliary information|coding agent|public tests|private tests|hidden oracle|ablation|fixed decomposition|anchoring' kb/reference/ --glob '*.md'` — found Commonplace-specific ablation proposals but no source-to-reference connection that improved traversal.
- The same body query over `kb/agent-memory-systems/` found many missing with/without-memory faithfulness tests, but the paper supplies task guidance rather than retained memory. The query over `kb/agentic-systems/` found generic coding-agent references without a shared runtime or control-surface mechanism.
- `rg -n -i 'SWE-bench Science|scientific guidance|auxiliary scientific|public tests|private tests|hidden oracle|exact repair|fixed decomposition|anchoring' kb/sources/ --glob '*.md' --glob '!**/.snapshots/**'` — found the provisional AlphaXiv analysis and the most discriminating instruction/guidance comparisons.

**Link following:**

- Read the complete candidate notes [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), and [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
- Followed those candidates one hop through [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), and [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md). These sharpened the boundary but were weaker direct targets than the retained candidates.
- Read [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md), [Agents Explore but Agents Ignore](../../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md), [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md), [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md), and the existing [AlphaXiv-derived SWE-bench Science analysis](../../../../sources/swe-bench-science-coding-agents-scientific-software.ingest.md). Read `kb/notes/COLLECTION.md` before proposing note-to-source return edges; `evidenced-by` authorises that direction.

## Connections Found

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **is-evidence-for**: public checks expose agent-visible engineering conformance while private cases test semantic equivalence, boundary conditions, and scientific validity, giving a bounded repository-level instance in which passing the visible requirement does not settle the larger objective.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: the auxiliary-information comparison separates supplying scientific guidance from downstream exact-repair benefit. It does not directly measure consultation or semantic uptake, so it bears most strongly on the note's final presence-to-benefit rung rather than proving an activation mechanism.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: aggregate success cannot distinguish the paper's four audited scientific-repair mechanisms, while the categorized failures expose different candidate remedies. This supports diagnostic insufficiency but does not test whether a later proposal loop improves from the categories.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the paper states that the 91-task pairs hold repository and executable context fixed while removing only separable auxiliary scientific information, then limits the result to model-specific descriptive score/cost differences. That design and caveat instantiate treatment-grain discipline.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **rests-on**: interpreting the benchmark requires separating the signals and actions available to each fixed model-harness configuration from task selection, test partition, guidance design, model/harness choice, and evaluators that no within-task repair can revise.
- [Agents Explore but Agents Ignore](../../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) — **compares-with**: solution injection measures discovery and observable interaction with a complete solution, while SWE-bench Science varies scientific guidance and measures task outcomes without measuring consultation. Together they distinguish presence, uptake, direction, and benefit.
- [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) — **compares-with**: both withhold agent-visible information in coding tasks, but Harness-IF uses atomic-rule withholding to stratify prior-aligned compliance, whereas SWE-bench Science removes auxiliary scientific information while preserving required context and measures scientific-repair outcomes.
- [AlphaXiv-derived SWE-bench Science analysis](../../../../sources/swe-bench-science-coding-agents-scientific-software.ingest.md) — **compares-with**: both observations concern the same paper, but the AlphaXiv capture combines the authored abstract with an AI overview while this author-controlled full paper exposes the construction, tables, appendices, and explicit causal/statistical caveats needed to assess the reported ablation.

## Bidirectional Candidates

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) ↔ source — **evidenced-by**: a future note edit could cite the full paper's public/private split as a bounded scientific-software instance while preserving the distinction between local conformance and objective warrant.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) ↔ source — **evidenced-by**: a future note edit could use the paired guidance comparison for the distinction between context presence and beneficial downstream effect, while stating that consultation and uptake were not measured.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) ↔ source — **evidenced-by**: a future note edit could use the four-way audit as bounded evidence that mechanism-level categories reveal distinctions aggregate scores erase, without claiming the paper evaluated a later learning loop.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) ↔ source — **evidenced-by**: the paper's explicit paired-condition definition and its refusal of causal or significance claims are a clean worked example of contrast-bounded attribution.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — rejected because SWE-bench Science's anchoring account comes from inspected cases and is not a controlled detection/refusal experiment; treating it as evidence for below-compliance influence would overstate the paper.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) — rejected because the public/private split connects more directly to the artifact-requirement-objective path in the exact-implementation note; this higher-level target distinction adds no source-specific traversal value.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — rejected because that proposal is about evaluating Commonplace itself, whereas the paper's auxiliary-information contrast does not inform its system-specific baseline design.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — rejected because semantically equivalent style perturbations test prompt sensitivity, not the marginal contribution of separately removable scientific information; Harness-IF supplies the clearer information-withholding comparison.
- Agent-memory-system faithfulness reviews — rejected as a class because the paper's scientific support blocks are task inputs, not retained cross-session memory, and the benchmark does not inspect a memory read-back mechanism.
- Agentic-system analyses — rejected as a class because model-harness configurations are outcome strata in the paper, not code-grounded analyses of the systems' execution loops or control surfaces.

## Index Membership

None

## Synthesis Opportunities

The paired guidance result, Agents Explore, and the contextual-activation note jointly expose a four-stage ladder: information is present, it is consulted or affects behavior, its influence is correctly directed, and downstream performance improves. [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) already owns this ladder, so bounded evidence integration is preferable to a new synthesis note.

## Maintenance Observations

- The existing AlphaXiv ingest recommends capturing and checking an author-controlled full paper. This separate snapshot fulfills that capture prerequisite without changing the AlphaXiv observation; any later closure should preserve the two distinct checksums and source identities.

## Flags

- The benchmark construction, manual failure taxonomy, and scientific-information comparison are independent result clusters. A future ingest should keep them separate.
- The auxiliary-information comparison covers two model-harness configurations, reports descriptive point differences, and explicitly disclaims statistical significance and causal identification. The paper's anchoring explanation is therefore a mechanism hypothesis, not an identified effect.
