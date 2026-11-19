---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/persona-assigned-llms-motivated-reasoning.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning

**Source:** [Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](../../../../sources/.snapshots/persona-assigned-llms-motivated-reasoning.md)

The source is an immutable snapshot. Under the sources `COLLECTION.md`, the snapshot never authors links. Every outbound candidate below is a recommendation for the matching ingest, `kb/sources/persona-assigned-llms-motivated-reasoning.ingest.md`. That ingest did not exist when this report was written.

**Source reading (claims used for judging candidates).** Dash, Reymond, Spiro and Caliskan (arXiv 2506.20020 v2) give 8 LLMs a persona through the system prompt: "Adopt the identity of {persona}. Answer the questions while staying in strict accordance with the nature of this identity". The study uses 8 personas over 4 attributes. It runs two human-subject reasoning tasks. On headline veracity discernment, personas lower discernment by up to 9% (High School persona) and by 3% on average. On gun-control numeric evidence, political personas are up to 90% more likely to answer correctly when the ground truth fits their induced identity. The skin-cream control shows β values near 0. In 46% of open-source answers the persona says its identity explicitly ("As a Republican, I must emphasize..."). Prompt debiasing fails. Chain-of-thought (CoT) gives a non-significant −0.39% change, and accuracy prompting lowers performance by a significant 2.93%. The authors say the "motivation" mechanism may be unlike the human one. Limitations: two tasks, binary demographic personas, no reasoning-trained models, and only prompt-level mitigations tested.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links. Destinations to prospect are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. Authorised labels by destination:
- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
- theory/definitions: `defined-in`
- sources, agentic-systems: `compares-with`, `see-also`
- reference: `see-also`
- agent-memory-systems: `is-evidence-for`, `compares-with`, `see-also`
- external: `derived-from`, `see-also`

External prospecting was skipped. The only known external target is the paper's own URL (https://arxiv.org/abs/2506.20020), which the future ingest should carry as `derived-from`.

**Title/description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 433 titles. Flagged: context contamination, error correction/decorrelation, human-writing-structures transfer, psychology-to-agent transfer, systematic prompt variation, LLM context scoping, out-of-spec output, structured-prompt gains.
- `rg '^description:' kb/sources/ --glob '*.ingest.md' | rg -i 'persona|role|sycophan|bias|identity|motivat|debias|myside|political|steer|framing'`. Flagged: peters-chin-yee generalization bias (accuracy prompts worsen), many-ai-analysts (persona steering), language-models-dont-always-say-what-they-think (Turpin, CoT unfaithfulness under bias), Lampinen content effects, validity–plausibility conflation, prompt-stability (personality variants), semantic leakage, gentle-coding (sycophancy routing), competing-biases-llm-confidence, position-bias. Rejected as off-topic: optimal-ordered-problem-solver, shifting-inductive-bias, no-free-lunch (these use "bias" in the inductive-bias sense).

**Topic indexes:**
- `kb/tags/llm-reliability-README.md` was read. Its inclusion condition covers diagnosing output deviation and testing correction machinery. The source tests prompt-level correction of a deviation, so the tag is a plausible fit (see Index Membership). The head led to the error-correction and systematic-prompt-variation notes.
- `kb/tags/context-engineering-README.md` was read. It covers prompt assembly and scoping. The fit is weaker: persona assignment is a prompt-assembly choice, but the paper does not study context selection.
- `kb/tags/failure-modes-README.md` (`complete: true`) was read. It covers KB-level failure modes, so it does not apply. Its by-tag rg was skipped.

**Body search:**
- `rg -il 'persona' kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources --glob '*.md'`. Hits are mostly agent-memory reviews that mention persona files (not reasoning bias). Also hit: systematic-prompt-variation (PromptSE personality variants), a-bare-writing-prompt (open question about expert-persona prompting), and verification-needs-a-typed-target (Exo's persona prompt has no check).
- `rg -n -i 'persona' kb/theory --glob '*.md'`. No theory note studies persona-induced reasoning bias. That gap is the source's distinct contribution.
- `rg -il 'sycophan|motivated reasoning|belief bias|content effect|identity-congruent|role prompt|role-play|roleplay' kb/theory kb/sources kb/reference kb/tags`. Hit: context-contamination, llm-context-is-composed-without-scoping, error-correction, human-writing-structures, structured-prompt-gains, topology-isolation, plus the content-effects / validity–plausibility / semantic-leakage / GSM-DC / metaphor ingests.
- `rg -l -i 'chain-of-thought|step by step|instruction-level mitigation|telling the model|prompt.based mitigation|debias' kb/theory`. Hit: structured-prompt-gains, error-correction, human-writing-structures, context-contamination, process-structure-and-output-structure. These are the notes that make claims about CoT or instruction-level mitigation.
- `rg -n -i 'chain-of-thought|CoT' kb/sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md` confirmed the ingest's "CoT partially restores content-independent reasoning" claim. The source contradicts this for persona-induced bias.
- `rg -n -i 'accuracy prompt|prompt' kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md` confirmed: "do not introduce any inaccuracies" gives OR 1.90 (worse), and "step by step" has no significant effect. This is the same pattern as the source.
- `rg -n -i 'persona' kb/sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md` confirmed five analyst personas (plausible / implausible / confirmation-seeking framings) that steer conclusions.

**Link following:**
- context-contamination → its Relevant Notes (semantic leakage, Lampinen content effects, llm-context-is-composed-without-scoping, soft-degradation). This confirms the cluster on content influence despite instruction. The note's open question ("whether an explicit neutrality reminder can inoculate against a *present* verdict") is directly addressed by the source's accuracy-prompt result.
- error-correction § "Content bias: an empirically measured correlation source" → structured-prompt-gains and process-structure. These notes say CoT/process structure partly decorrelates content bias. The source is a bounding case.
- systematic-prompt-variation → PromptSE ingest → out-of-spec-output and llm-output-deviation-requires-three-way-diagnosis. Persona variation is already treated there as a semantics-preserving diagnostic perturbation. The source shows identity personas are not semantics-preserving for evidence evaluation.

## Connections Found

All are candidates for the future `kb/sources/persona-assigned-llms-motivated-reasoning.ingest.md`.

- [Context contamination operates below an agent's compliance reasoning](../../../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- **is-evidence-for**: the note leaves open whether an explicit counter-instruction can neutralize a stance already in context. Here an accuracy prompt applied alongside a present persona did not reduce identity-congruent errors and lowered veracity discernment by 2.93%. This supports "instruction does not enforce isolation" at the level of task accuracy, across 8 models. Caveat: the persona was a sanctioned instruction ("strict accordance with this identity"), not a contaminant the model was told to ignore. The counter-instruction therefore competes with a standing instruction. The ingest should say so.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **is-evidence-for**: persona assignment is a second measured source of correlated, directional error, beside content bias. Repeated samples under one persona (100 per prompt) lean the same way, so voting within a persona amplifies the lean. CoT did not remove it. This qualifies the note's suggestion that process structure partly decorrelates content-driven error.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for**: the paper adds a human failure mode that LLMs share: motivated reasoning / myside bias, which predicts veracity discernment in models as it does in humans, while analytical reasoning does not. It also bounds the note's claim that structured prompting "pushes toward content-independent reasoning": step-by-step prompting gave no significant mitigation here.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../theory/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- **is-evidence-for**: for verification, persona-framed variants do not supply independent noise. Identity personas move answers in a predictable direction on politically loaded evidence and leave a neutral control (skin cream) roughly unchanged. Persona variation is therefore a biased decorrelation lever, and its bias depends on the content. For diagnosis, the result shows identity personas are not semantics-preserving perturbations on such tasks.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -- **is-evidence-for**: the paper runs exactly the note's "does the agent exhibit this failure?" test for one principle. It ports two human-subject motivated-reasoning tasks and finds the failure, while the authors note the mechanism may differ. This is a worked positive case at the level of behavior, not of mechanism.
- [Peters & Chin-Yee — LLM generalization bias](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) -- **compares-with**: shared axis is prompt-level mitigation of a systematic bias. In both studies an accuracy-emphasis prompt made the bias worse (OR 1.90 there, −2.93% discernment here), and "step by step" had no significant effect. Two independent replications of the same pattern strengthen any later claim that accuracy prompting is not a reliable debiasing control.
- [Many AI analysts, one dataset — agentic data-science multiverse](../../../../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md) -- **compares-with**: shared axis is a prompt-assigned persona steering conclusions on fixed evidence. The multiverse study uses framing personas (hypothesis plausible / implausible / confirmation-seeking) in autonomous analysis. This source uses socio-demographic identity personas on short reasoning items. The two together show persona steering at both task scales.
- [Language models don't always say what they think (Turpin et al.)](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) -- **compares-with**: shared axis is whether a biasing input gets verbalized in the reasoning. Turpin's models almost never mention the biasing feature (1 of 426). Here 46% of open-source answers explicitly invoke the induced identity. Persona bias is often visible in the trace, yet CoT still does not correct it. That distinguishes "unfaithful CoT" from "faithful but motivated CoT".
- [Ingest: Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- **compares-with**: shared axis is human-like bias on human-subject reasoning tasks and whether CoT mitigates it. Lampinen finds belief-congruent content effects that CoT partly reduces. This source finds identity-congruent effects induced by a persona that CoT does not reduce. Content bias comes from the item; persona bias comes from an instruction about the reasoner.

## Bidirectional Candidates

- [Peters & Chin-Yee — LLM generalization bias](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) <-> source -- **compares-with**: the return link is useful because a reader of either ingest looking at the accuracy-prompt backfire should find the independent replication.
- [Language models don't always say what they think (Turpin et al.)](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) <-> source -- **compares-with**: the verbalized-vs-hidden bias contrast helps a reader of Turpin avoid generalizing "biases are not verbalized" to persona-induced bias.

## Reverse-edge Candidates

Theory notes author their own links to source ingests under the theory collection's rules. Once the ingest exists, these notes could cite it:

- [Context contamination operates below an agent's compliance reasoning](../../../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) → future ingest -- **evidence**: an addition to its Scope and limits or Open Questions. It is a multi-model test of a counter-instruction applied alongside a present stance, with the sanctioned-instruction caveat.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) → future ingest -- **evidence**: a second named correlated-error source beside content bias, and a limit on the CoT-as-decorrelator suggestion.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → future ingest -- **evidence**: a shared failure mode (myside bias), plus a null result for step-by-step structure against it.
- [A bare writing prompt does not determine its intended contribution](../../../../theory/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) → future ingest -- **evidence (cautionary)**: its Empirical Question names "expert-persona prompting" as a lever to test. This source shows identity personas can lower accuracy on evidence evaluation, a cost the experiment design should measure. The fit is weak because the source tests demographic personas, not expert personas.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) -- rejected. A persona leaking into evidence evaluation looks like unscoped context, but the instruction explicitly told the model to answer "in strict accordance" with the identity. The effect is therefore instructed scope, not leakage across a boundary. Citing it as scoping evidence would mislead. [Semantic leakage](../../../../sources/semantic-leakage-lms-gonen.ingest.md) remains the clean evidence for that note.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- rejected. Whether an identity-congruent wrong answer is out of spec depends on whether the persona instruction or the task's ground truth sets the spec. The paper does not settle this, so a load-bearing label would be ambiguous.
- [Structured prompt gains do not establish distribution selection](../../../../theory/structured-prompt-gains-do-not-establish-distribution-selection.md) -- rejected. The source reports a null CoT effect, which says nothing about what mechanism structured-prompt gains have. The CoT bounding point is better carried by error-correction and human-writing-structures.
- [Human analogies suggest functions, not component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- rejected. The authors' remark that the mechanism may differ is incidental. The paper says nothing about component boundaries.
- [LLM validity–plausibility conflation (content effects steering)](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) -- rejected as a compares-with. It gives a representation-level mechanism for item-content bias. The source does no probing, and the persona channel differs, so no shared axis is clean enough. A future synthesis could revisit it if persona steering is shown to act through the same directions.
- [Prompt Stability in Code LLMs (PromptSE)](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- rejected. Its "personality" variants are expressive-style templates on code tasks, not identity assignment on evidence evaluation. The overlap is mostly the keyword. The useful contrast is already routed through systematic-prompt-variation.
- [Gentle-coding research catalog](../../../../sources/gentle-coding-research.ingest.md) and [Competing biases in LLM confidence](../../../../sources/competing-biases-llm-confidence.ingest.md) -- rejected. They share the sycophancy and bias neighbourhood but no specific axis. The catalog is an unverified routing list. Competing-biases studies answer ownership under advice, not identity.
- [Compound Engineering plugin review](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected. Its "multi-persona review" uses expertise or role personas inside a review harness. The source tests socio-demographic identities and does not establish that role personas bias reviewers. A link would invite a transfer the evidence does not support.
- Agent-memory-system reviews that mention persona files (e.g. continuity, hermes-agent, synapptic) -- rejected. In those reviews, persona means a stored identity or profile file, with no claim about reasoning bias.

## Index Membership

- [llm-reliability](../../../../tags/llm-reliability-README.md) -- the future ingest could carry `tags: [llm-reliability]`. It measures a systematic interpreter deviation induced by the prompt and tests two prompt-level correction attempts, which both fail. That meets the head's "tests ... the machinery that prevents, detects, or corrects" condition. Sources do not join generated member listings, so this is a search tag only.

## Synthesis Opportunities

Peters & Chin-Yee (generalization bias in science summaries) and this source (persona-induced motivated reasoning) independently show that an accuracy-emphasis prompt worsens a systematic bias and that "step by step" leaves it unchanged. Context contamination adds that an instruction to ignore content already in context does not enforce isolation. Together these three suggest a theory claim: telling a model to be accurate or neutral is not a debiasing control and can backfire, so bias controls must change what is in the context (exclusion, alternative framings) rather than add exhortation. The mechanism (why accuracy prompts backfire) is not explained in either paper. Under the KB quality bar this belongs in the log until the mechanism is understood.

## Maintenance Observations

- The error-correction note and the human-writing-structures note both present CoT as a partial corrective for content-driven bias, based only on Lampinen. This source and Peters & Chin-Yee give null CoT results for two other bias sources. Those notes' CoT claims should be scoped to item-content effects when next revised.
- The tracked ingest for this snapshot does not exist yet. All outbound candidates above depend on it being written.

## Flags

- Tension: Lampinen (CoT partly reduces content effects) vs this source (CoT does not reduce persona-induced effects). Flagged, not resolved. The bias sources differ (item content vs instruction about the reasoner).
- Caveat to carry into any use of the source: the persona instruction explicitly asks for identity-consistent answers. The "motivated reasoning" may partly be instruction compliance, and the paper does not separate the two.
