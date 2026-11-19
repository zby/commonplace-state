---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Many AI analysts, one dataset

**Source:** [Many AI analysts, one dataset: Navigating the agentic data science multiverse](../../../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.md)

The target is an immutable snapshot. `Connections Found` therefore recommends links for its matching ingest report; `Reverse-edge Candidates` records notes that could cite the snapshot under their own collection rules.

## Discovery Trace

**Collection contract and destination scan:**

- Read `kb/sources/COLLECTION.md`. Its outbound rules authorize prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; they exclude `kb/work/` and `kb/instructions/`. Snapshots are immutable and the ingest report carries their authored outbound surface.
- Read `kb/notes/README.md`, `kb/notes/llm-reliability-README.md`, `kb/notes/evaluation-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes indexes routed the source toward underspecification, sampling, prompt variation, oracle strength, and whole-system evaluation. The other collection heads supplied no direct casebook match.
- Ran `rg -N --no-heading -m1 '^# '` separately over all five authorized destination collections. The full title surface surfaced the notes on execution indeterminism, systematic prompt variation, fixed decompositions, the deployed-system boundary, and weakly discriminated qualities. The broad source listing surfaced Prompt Stability in Code LLMs as the closest existing empirical comparison.
- Ran `rg -n '^description:.*(prompt|indetermin|underspec|evaluation|oracle|audit|verification|sampling|variation|stability|divers|hypothesis|evidence|bias|plural|adversar|judge|review)'` over the five destinations. Kept candidates only when this experiment supplies a distinct empirical case or a material qualification.

**Body search:**

- `rg -n -i "many[- ]analyst|data science multiverse|analytic(al)? (choice|variability|dispersion)|selective reporting|specification curve|persona|prompt (choice|framing|variation|stability|sensitivity|disclosure)|model choice|auditor|underspecification|execution indeterminism" ...` — found no earlier capture of this paper. It concentrated candidates in the LLM-reliability notes and the Prompt Stability source pair.
- `rg -n -i "prompt.*(steer|sensitiv|variation|framing)|persona|underspecif|indetermin|sampling" kb/notes --glob '*.md'` — kept the semantic-underspecification and sampling notes. Rejected writing-style and context-loading notes because the study manipulates an analyst commission, not a KB writing surface.
- `rg -n -i "auditor|judge|review.*(trace|transcript)|process.*valid|diagnostic.*rich|compliance" kb/notes --glob '*.md'` — tested evaluator and diagnostic-richness candidates. Kept the verification-boundary and weak-discrimination notes; rejected diagnostic richness because the experiment does not compare alternative evidence surfaces for a later proposer.
- `rg -n -i "multiverse|many[- ]analyst|selective reporting|specification curve|analytic choice|analysis process" kb/notes --glob '*.md'` — found no dedicated analytic-multiverse note.
- `rg -n -i "multiverse|many[- ]analyst|selective reporting|specification curve|prompt stability|persona.*prompt" kb/sources --glob '*.ingest.md' --glob '*.source-review.md'` — kept Prompt Stability in Code LLMs as the only comparison with a precise shared axis.
- `rg -n -i "prompt|auditor|model partition|review.*model" kb/reference --glob '*.md'` and `rg -n -i "multiverse|analyst|auditor|prompt.*steer|persona" kb/agent-memory-systems kb/agentic-systems --glob '*.md'` — produced only implementation- or workflow-level resemblances, not useful source connections.

**Link following:**

- From [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), followed [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md), [LLM output deviation has three sources with non-substitutable remedies](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md), and the existing Prompt Stability citation. This established the useful distinction between repeated draws within a model–persona cell and systematic shifts between cells.
- From [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), followed [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) and [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md). This exposed a boundary: Negative/Positive framing is near a diagnostic perturbation, but confirmation-seeking prompts alter the commission and are not semantic-preserving variants.
- From [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), followed [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) and [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md). The first gains a concrete filter-selection case; the second is only a caution because the paper does not independently validate its AI auditor against a human process-validity standard.
- Read [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) as required for an experiment-bearing source. The experiment varies model and persona within a fixed dataset/task/scaffold/auditor decomposition; its results establish effects inside that space, not the adequacy or coverage of the space itself.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — **is-evidence-for**: fixing the dataset, hypothesis, and estimand still leaves multiple defensible projections through preprocessing, variable construction, model specification, and inference, and the paper observes conclusion reversals across those projections.
- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **is-evidence-for**: repeated runs within fixed model–persona cells expose sampling/run variation, while shifts between model and persona conditions expose distinct system-level causes; the experiment makes the separation empirical rather than merely terminological.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — **compares-with**: this paper varies behavioral framing to measure and causally steer an analysis distribution, but its confirmation-seeking variants change the analyst commission. It therefore bounds the note's diagnosis category rather than supplying a semantic-preserving prompt-stability case.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **is-evidence-for**: an AI auditor rejects 33% of runs and attenuates aggressive confirmation-seeking effects without eliminating them, so cheap autonomous analysis generation does not by itself produce reliable automated empirical science.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — **is-evidence-for**: both base-model choice and prompt/persona choice systematically change conclusions inside a shared tool scaffold, directly demonstrating that observed behavior belongs to the assembled system rather than the model checkpoint alone.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) — **is-evidence-for**: compliance screening preferentially removes aggressive specification search and overclaiming, yet support-rate shifts persist among accepted runs. The operative audit distinguishes some forms of bad analysis more strongly than it distinguishes conclusion steering.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **rests-on**: interpreting the experiment requires separating effects of the varied model/persona coordinates from the fixed datasets, hypotheses, estimands, ReAct scaffold, tool surface, run budget, decision codebook, and AI auditor.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — **compares-with**: both studies vary prompt-associated human factors under repeated sampling, but Prompt Stability aims to preserve task semantics and measures code correctness, whereas this paper deliberately changes analytical posture and measures the distribution of defensible scientific conclusions.

## Bidirectional Candidates

None — note-side return paths are listed under Reverse-edge Candidates because the target is an immutable snapshot.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) → source — **evidenced-by**: the paper is a domain-rich example where a fixed natural-language hypothesis plus estimand still admits qualitatively different valid analytic programs.
- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) → source — **evidenced-by**: within-cell repetition and between-condition manipulation supply a second empirical separation of sampling variation from prompt/model effects beside Prompt Stability.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) → source — **evidenced-by**: the paper qualifies the taxonomy with a controlled-variation case whose strongest variants alter the task commission, showing why “what is held fixed” is load-bearing to the epistemic role.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source — **evidenced-by**: autonomous analysis becomes cheap while audit remains imperfect and outcome distributions remain steerable, making verification the limiting surface inside one scientific workflow.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source — **evidenced-by**: the crossed model/persona design directly estimates two non-interchangeable system components' effects on user-visible analytic conclusions.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) → source — **evidenced-by**: the compliance gate changes which analyses survive yet leaves a substantial persona-conditioned conclusion shift, a concrete instance of selection shaped by what the operative oracle can discriminate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — rejected: the auditor does inspect transcripts, tool calls, and code, but the paper does not compare that evidence surface with output-only or score-only auditing and no later proposer learns from the audit. The source illustrates trace inspection without testing the note's causal claim.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — rejected as a committed edge: a separate model audits produced reasoning and code, but the paper does not independently establish that this auditor checks process validity rather than reconstructing plausible analyses. The note is a limitation lens, not evidence supplied by this source.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) — rejected: both discuss quality-control load, but that note's mechanism is harmful retained-artifact inflow outrunning prevention, containment, detection, and repair. This paper concerns selective reporting from analysis distributions, not maintenance debt in a growing artifact store.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — rejected: multi-persona review is a surface resemblance. The plugin coordinates software-review roles; this source estimates how analyst prompts steer scientific inference, so a direct systems comparison would not aid either reader.
- `kb/reference/` and `kb/agent-memory-systems/` candidates — rejected: scoped searches found no current shipped-system document or memory-system casebook whose design is materially explained, supported, or compared by this paper.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) — a future note promoted from this source would belong beside systematic prompt variation and prompt ablation as a controlled-variation case; the source snapshot itself is not a tag-index member.
- [LLM reliability](../../../../tags/llm-reliability-README.md) — the paper supplies a particularly clean experiment separating within-condition sampling dispersion, between-prompt steering, and auditor filtering.

## Synthesis Opportunities

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md), and [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) together imply an evaluation decomposition not yet stated as one claim: **agentic multiverse experiments should report within-condition sampling dispersion, between-condition interpretation effects, and outside-condition coverage limits separately**.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), and this source suggest a more tentative claim: **when candidate analyses become cheap, distributional reporting may be part of the verifier rather than merely a transparency add-on**. The source motivates but does not test that intervention, so promotion would need another source or an experiment.

## Maintenance Observations

None

## Flags

- **Fixed-decomposition boundary:** analysts could condition on the dataset, hypothesis, prespecified estimand, persona prompt, model priors, full run history, and tool outputs; they could compose Python/shell/file-editing operations and broad analytic decisions. Their effective hypothesis class was the mapping expressible by four selected LLMs inside one ReAct/Inspect scaffold. Datasets, hypotheses, estimands, persona family, model family, tools, run cap, output protocol, auditor model/prompt, compliance criteria, and decision codebook remained fixed. The paper isolates model/persona effects inside that setup; it does not validate the setup as a representative decomposition of human or possible AI analysis.
- **Auditor evidence boundary:** the snapshot reports AI-auditor filtering but no independent human-labelled validation of auditor discrimination. Accepted-run results support “dispersion survives this audit,” not “all retained analyses are methodologically sound.”
- **Split candidate:** the source carries at least three independently useful results—baseline analytic dispersion, causal steering by model/persona, and partial mitigation by auditing. The ingest report should keep their evidence and limitations distinct.
- **Paper-only mechanism evidence:** the paper names a public code repository, but this ingest was not requested through the code-grounded paper branch. Implementation details and numerical reproduction therefore remain paper-reported.
