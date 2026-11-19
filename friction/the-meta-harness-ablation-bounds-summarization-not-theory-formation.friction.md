# Friction check: The Meta-Harness ablation does not identify episode-backed theory formation

**Note:** kb/notes/the-meta-harness-ablation-bounds-summarization-not-theory-formation.md
**Central claim (one sentence):** The Meta-Harness ablation constrains consumer-blind compressed feedback that replaces execution traces, but it does not identify the effect of adding a reviewed, scoped causal conjecture while retaining the episodes from which it was formed.

## Filter
**Verdict:** SURVIVES

The two commitments can coexist: the observed disadvantage of compressed feedback can constrain how condensed artifacts are used, while the absence of an episode-retaining theory arm leaves the effect of that distinct intervention unidentified.

## Signal — thinnest joints
1. **“The result is adverse evidence for any learning process that inserts condensed natural-language artifacts into an optimizer's information environment.”** — UNSUPPORTED — The large reported contrast is between raw traces and scores plus summaries, which changes episode access rather than merely inserting an artifact; the summaries arm also has mixed evidence against scores only (slightly higher median accuracy but lower best-found accuracy), so this experiment does not support the claim about *any* insertion process.
2. **“LLM summaries were not neutral compression; they actively hurt in the tested setting. The claim that a reviewed, scoped, episode-backed conjecture behaves differently is openly a bet.”** — THIN — Lower best-found accuracy supports caution, but the slightly higher median than scores only and the simultaneous removal of traces make “actively hurt” stronger than the isolated comparison warrants; the burden-of-proof conclusion remains reasonable only when tied to the narrower summarize-and-discard regime.
3. **“It is ampliative by commitment, not derivation, so it may have explanatory-reach—the ability to keep explaining beyond the cases that produced it.”** — THIN — Being an ampliative commitment makes reach possible but supplies no reason that a particular conjecture will possess it; the following reach-assessment requirement properly treats that property as something still to establish.
4. **“Comparable attribution tasks should preserve episode access by default.”** — THIN — The observed trace advantage supports this default for closely matching proposer tasks and compression procedures, but extending it to fixing sessions or critique pipelines depends on an unstated account of which task and consumer features make them comparable.
5. **“Without a traces-only, no-report arm, the reports' contribution could be positive, null, or harmful.”** — HOLDS — Because the full-trace arm bundles raw traces with reports, its aggregate result cannot determine the reports' marginal contribution; each stated sign remains compatible with the comparison described.

## For the human
Look first at the claim that the ablation is adverse evidence about inserting any condensed artifact: concretize whether the supported target is insertion, replacement of episodes, this fixed summarizer, or only their bundled treatment.
