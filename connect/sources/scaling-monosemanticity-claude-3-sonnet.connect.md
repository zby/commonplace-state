---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/scaling-monosemanticity-claude-3-sonnet.md"
source_has_frontmatter: true
date: "2026-11-03"
depth: standard
---

# Connection Report: Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**Source:** [Scaling Monosemanticity (snapshot)](../../../../sources/.snapshots/scaling-monosemanticity-claude-3-sonnet.md)

The source is an immutable snapshot. No tracked `scaling-monosemanticity-claude-3-sonnet.ingest.md` exists yet. Every outbound candidate below is meant for that future ingest report, which is the authored link surface under `kb/sources/COLLECTION.md`. Never link to the snapshot itself.

Source claims this report used: sparse autoencoders (SAEs) trained on Claude 3 Sonnet's middle-layer residual stream give interpretable, causally steerable features, with 1M, 4M and 34M dictionaries. The training loss (MSE plus L1) is only a proxy for interpretability ("Inability to Evaluate"). Feature coverage is incomplete and depends on concept frequency: a concept is more than 50% likely to get a feature at roughly 1/(alive features). Rarer concepts can still be represented compositionally. Getting "all the features" would likely cost more compute than training the model. Features beat neurons, and beat few-shot probes, for interpretability and steering. Safety-relevant features exist, but "knowing about lies" is not lying: what matters is when they activate. Dictionary learning "amortizes" the cost of finding directions.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` "Outbound links". Allowed destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources. `kb/work/` and `kb/instructions/` are excluded. The `external` destination is authorised only for `derived-from` and `see-also`, and only for targets already in hand. No external prospecting was done. The `derived-from` external edge to `https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html` (the snapshot's `source`) is implicit in the future ingest's `source` field.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (435 titles), filtered with `rg -i 'proxy|goodhart|parametric|weights|probe|inspect|blackbox|...|interpret|monitor'`. Flagged: opacity-depends-on-the-inspection-question-and-budget, inspectable-artifact-not-supervision-defeats-the-blackbox-problem, knowledge-storage-does-not-imply-contextual-activation, definitions/representational-form, reflective-coverage-is-graded-across-representational-forms, parametric-reproduction-cannot-replace-an-authoritative-record, evaluation-automation-is-phase-gated-by-comprehension, oracle-strength-spectrum, minimum-viable-vocabulary-is-the-naming-set-that-most-reduces, weight-resident-methodologies-compress-behavior-in-context.
- Descriptions read with `rg -N '^description:'` for the flagged notes and for candidate sources: verbalizable-representations-global-workspace-llms, reading-between-the-dots-decoding-hidden-computation, conceptual-blending-humans-and-language-models, an-enigma-of-artificial-reason-production-evaluation-gap-lrms, gentle-coding-research, tulving-pearlstone-availability-versus-accessibility, emergent-analogical-reasoning-transformers, llm-agents-are-not-always-faithful-self-evolvers, grunwald-mdl-tutorial.

**Topic indexes:**
- `kb/tags/` listing. Heads read: learning-theory (`complete: true`, so no by-tag rg), artifact-analysis (`complete: true`, inclusion condition read), observability (inclusion condition read), llm-reliability (description). The snapshot has no `tags:`. Tag heads were used only to check fit for a future ingest's optional `tags:`.

**Body search** (all excluding `kb/work/**` and `kb/reports/cache/**`):
- `rg -il "interpretab" kb` -- hits: verbalizable-representations, reading-between-the-dots, several scientific-discovery ingests (model-discovery, dreamcoder, pathway-equations, hypothesis-generation: "interpretable" used about symbolic models, rejected as keyword-only), ace review, sutskevers-list chapters (incidental).
- `rg -il "monosemantic"`, `"sparse autoencoder"`, `"dictionary learning"`, `"Golden Gate"` -- no hits. The KB has no prior treatment of SAEs.
- `rg -il "superposition"` -- only conceptual-blending-humans-and-language-models.ingest.md (lines 63, 90-91, 114, 235: its superposition step cites only toy-model work).
- `rg -il "steering"` -- agent/goal-steering senses only (goal-prioritization head, reviews). Rejected as a different sense.
- `rg -il "sycophan"` -- gentle-coding-research.ingest.md, a provider-communication report. Behavioral sycophancy only. Rejected.
- `rg -il "linear probe"` -- an-enigma-of-artificial-reason ingest. Incidental.
- `rg -il "Zipf"` -- two agentic-system-analyses runtime files (unrelated tooling). Rejected.
- `rg -l -i 'mechanistic|sleeper agent|representation engineering|steering vector|feature steering|transformer-circuits|logit lens|probing classifier'` -- adds tulving-pearlstone, emergent-analogical-reasoning-transformers, llm-agents-are-not-always-faithful-self-evolvers and others with incidental "mechanistic" use.
- `rg -n -i 'probe|probing|interpretab|distributed-parametric'` over representational-form, knowledge-storage, inspectable-artifact and reflective-coverage. This found the representational-form rule "Probe distributed-parametric artifacts behaviorally" (line 33) and inspectable-artifact's claim that weights expose no separately addressed instruction-level rules (line 18).
- `rg -n -i 'long.tail|training.data frequen|rare (fact|concept)|pretraining frequen|tail knowledge'` and `rg -n -i 'amortiz' kb/theory`. These led to minimum-viable-vocabulary ("naming amortizes recognition cost"). Nothing in the KB on training-frequency thresholds.
- `rg -l -i 'proxy (metric|objective|signal)|goodhart' kb/theory` -- inspectable-artifact, maintainability-oracles brainstorm, notes-need-quality-scores, quality-signals, verifiability-gradient. These cover proxy quality in KB curation, not the SAE proxy-loss problem. Read evaluation-automation instead.

**Link following:**
- verbalizable-representations ingest, Connections Found: it already routes an Anthropic interpretability paper to representational-form, knowledge-storage-does-not-imply-contextual-activation and inspectable-artifact. This confirmed the cluster and the framing that such work is "not context engineering".
- opacity-depends-on-the-inspection-question-and-budget, read in full. It names scale, the reference's form and obfuscation as inspection obstacles relative to a question, a path and a budget. Its Relevant Notes lead to axes-of-artifact-analysis and inspectable-artifact. It has no interpretability evidence yet.
- knowledge-storage-does-not-imply-contextual-activation, first 30 lines read. Its "storage" layer explicitly includes model weights.
- minimum-viable-vocabulary, read in full. It has an open question on selection criteria for names.
- evaluation-automation-is-phase-gated-by-comprehension, first 40 lines read.

**Other destinations:**
- `kb/agentic-systems/`, `kb/agent-memory-systems/`: the source studies model internals, not agent runtimes or memory systems. No trigger match. Skipped after the body searches above returned only agent-steering senses.
- `kb/reference/`: describes Commonplace itself. No trigger. Skipped.

## Connections Found

- [Opacity depends on the inspection question and budget](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) -- **is-evidence-for**: the strongest landing. SAEs are a tool that makes part of distributed-parametric content cheaper to inspect, and the paper reports the budget dependence the note asserts. Coverage grows with dictionary size and compute: about 60% of London boroughs get features at 34M. The authors estimate that getting "all the features" would cost more compute than training the model. Even within that budget, the reconstruction explains only at least 65% of the variance. So opacity here is relative to the question and to an affordable inspection budget, and better tools shift it.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **defined-in**: a future ingest that calls SAE features a partial decomposition of *distributed-parametric* content needs this term. Optional second use as **is-evidence-for**: the definition's default "Probe distributed-parametric artifacts behaviorally" (line 33) gets a counter-example. Here the inspection route is unsupervised decomposition plus clamping, not behavioral probing alone. Like the J-space ingest, this complicates the rule without overturning it.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- **is-evidence-for**: SAE features give partially addressable units inside weights: a feature can be read from its top activations and clamped to change behavior. That lets someone inspect and change one feature at a time, which the note ties to readable artifacts. The units still lack what the note's readable scripts and validators have: stable discrete rules, completeness and provenance. A ~65% variance floor, dead features and feature splitting show this. The ingest should state the narrowing explicitly.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- **compares-with** on the presence-versus-causal-use axis: the paper's safety discussion makes the same distinction inside the model. The existence of a deception or bioweapons feature is unremarkable ("knowing about lies" vs lying). The interesting question is when it activates. Missing features also do not mean missing information, because concepts can be represented compositionally. This is an analogy at the model-internal level, not evidence about context loading. Use compares-with, not is-evidence-for.
- [Verbalizable Representations Form a Global Workspace in Language Models](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) -- **compares-with** on the axis "instrument for reading Claude-internal concepts". Both are Anthropic Transformer Circuits papers on Claude models. This one uses an unsupervised SAE dictionary at one middle layer with clamping-based steering. The J-space paper uses a token-aligned Jacobian lens with swaps and ablations, and claims a workspace that selectively mediates flexible cognition. Comparing them shows how the KB's "probeable parametric state" evidence depends on the instrument.
- [Reading between the dots: decoding hidden computation](../../../../sources/reading-between-the-dots-decoding-hidden-computation.ingest.md) -- **compares-with** on the axis "internal readouts as a monitoring surface". The SAE deception case study (detecting and correcting deception via features) and its list of failure modes ("illusions from suboptimal dictionary learning") parallel that ingest's claim that monitorability depends on the observation surface, and its unsupervised-does-not-mean-assumption-free caveat.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost for a bounded observer](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) -- **compares-with** on the axis "which concepts earn a dedicated entry in a size-bounded dictionary". The SAE result is empirical: a fixed-size learned dictionary gives dedicated entries to concepts above a frequency threshold of about 1/N. Rarer concepts are reached by composing entries ("large non-capital city" + "in New York state"). This speaks to the note's open question on name-selection criteria, but only as a cross-domain analogy. Keep it only if the ingest states that limit. Weakest kept candidate.

## Bidirectional Candidates

- [Verbalizable Representations Form a Global Workspace in Language Models](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) <-> source -- **compares-with**: the J-space ingest's Limitations call the Jacobian lens a partial instrument. A return link would let a reader compare the earlier dictionary-learning instrument and its own stated limits: cross-layer superposition, shrinkage and incompleteness.

## Reverse-edge Candidates

- [Opacity depends on the inspection question and budget](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) → future ingest -- **evidenced-by** (under theory's own `COLLECTION.md` rules; check its authorised set): the "Scale" section asserts that tools extend affordable inspection and that no single size makes every question opaque. Its only external evidence is cryptographic. An SAE example would give it a distributed-parametric case with measured budget dependence.
- [Representational form](../../../../theory/definitions/representational-form.md) → future ingest -- evidence for qualifying line 33, "Probe distributed-parametric artifacts behaviorally". Only if the definition's maintainers decide to name decomposition-based inspection.
- [Conceptual blending in humans and language models](../../../../sources/conceptual-blending-humans-and-language-models.ingest.md) → future ingest -- **compares-with** (sources→sources): that ingest notes its superposition-to-"generic compromise" step "cites only toy-model superposition work". This paper is large-model evidence that superposition-based feature decomposition works in a production model. Caveat: the paper does not test compromise between blended features, so the link fills the scale gap, not the compromise gap.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../theory/evaluation-automation-is-phase-gated-by-comprehension.md) -- the paper's "Inability to Evaluate" (loss as a proxy for interpretability) and its order of human inspection then automated interpretability look similar. But the paper does not show a proxy-gaming failure or a gate. Linking would claim support it does not give.
- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) -- the SAE objective is a soft-oracle proxy, but this is a generic illustration that adds no mechanism to the spectrum.
- [Grünwald MDL tutorial](../../../../sources/grunwald-mdl-tutorial.ingest.md) -- the MSE+L1 tradeoff looks like a two-part code, but the paper never frames it as description length. The link would import an interpretation. The tutorial ingest is also currently untracked.
- [Reflective coverage is graded across representational forms](../../../../theory/reflective-coverage-is-graded-across-representational-forms.md) -- SAE observation and steering are external research tooling, not a system's reflective self-representation. Wrong frame.
- [Parametric reproduction cannot replace an authoritative record](../../../../theory/parametric-reproduction-cannot-replace-an-authoritative-record.md), [Weight-resident methodologies provide context-efficient behavioral compression](../../../../theory/weight-resident-methodologies-compress-behavior-in-context.md) -- both concern weights as a store of behavior or records. The paper adds nothing about authority or methodology compression.
- [Tulving–Pearlstone availability versus accessibility](../../../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) -- "no feature ≠ no information" sounds like availability vs accessibility, but the mechanisms differ: dictionary resolution vs retrieval cues. Route through knowledge-storage instead.
- [Gentle-Coding research catalog](../../../../sources/gentle-coding-research.ingest.md) -- covers behavioral sycophancy and evaluator bias, while the paper has a sycophancy *feature*. Keyword overlap only.
- Scientific-discovery ingests with "interpretable" hits (model-discovery-agent-bayesian-experiment-design, dreamcoder-wake-sleep-bayesian-program-learning, pathway-equations-of-reasoning, hypothesis-generation-and-updating-in-large-language-models) -- they mean interpretable symbolic models, a different sense.
- `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/reference/` -- no candidate. The paper is about model internals, and the paper's sense of "steering" does not match these collections' agent-steering sense.

## Index Membership

- [observability](../../../../tags/observability-README.md) -- candidate optional `tags:` value for the future ingest. The paper explains how an instrument makes hidden model state visible and why it cannot yet show all of it (dark matter, incompleteness, cross-layer superposition). That meets the inclusion condition: "why available evidence cannot expose it, or how that evidence becomes inspectable". Sources do not join generated member listings.
- [artifact-analysis](../../../../tags/artifact-analysis-README.md) -- only if the ingest draws a consequence for the form field, such as qualifying how distributed-parametric content is inspected. Otherwise omit.

## Synthesis Opportunities

The future ingest, the J-space ingest, opacity-depends-on-the-inspection-question-and-budget and inspectable-artifact-not-supervision-defeats-the-blackbox-problem together suggest a claim no note states yet. Interpretability instruments give distributed-parametric content a graded, budget-bound partial addressability: units can be read and clamped, but they are incomplete, depend on the instrument, and have no stable identity across dictionaries. That sits between behavioral probing and artifact inspection. The representational-form definition currently treats it as a binary (behavioral probing). Do not write this during connect. It may belong in the log first, under the Quality bar.

## Maintenance Observations

- The snapshot contains NUL bytes inside quoted dataset examples (for example around lines 307, 455 and 469). Plain `rg` therefore treats the file as binary and prints "binary file matches" instead of lines; searches need `rg -a`. This affects agents searching or grounding quotes against this snapshot. Whether the capture should strip NULs is a decision for `cp-skill-snapshot-web`; the snapshot must not be edited after the ingest pins its checksum.
- No tracked ingest exists for this snapshot, so none of these candidates can be authored until `cp-skill-ingest` runs.

## Flags

- The source is far from the KB's core scope (KB methodology). Its value is evidence for existing theory about inspection, opacity and form. Treat it like the verbalizable-representations ingest: "not context engineering".
- Tension to keep visible, not resolve: the paper weakens representational-form's "probe behaviorally" default, while inspectable-artifact holds that weights lack addressable rules. Both can stand if SAE features count as partial, instrument-relative units, but a writer should not cite the source for either side without that qualification.
- Split candidate: no. It is a single source with one cluster.
