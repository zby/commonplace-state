# Friction check: Learning inside a fixed decomposition inherits its mistakes

**Note:** kb/notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md
**Central claim (one sentence):** If a fixed decomposition excludes a required distinction, response, or mapping from a learner's effective update space, optimization within that space cannot repair the exclusion.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **“If only a costly or approximate construction is available, the decomposition may impose a sample-efficiency, robustness, or execution penalty. That is an empirical handicap, not an impossibility.”** — THIN — Cost alone need not make a response unexpressible, but approximation can: if the objective requires the exact response, showing that only an approximation is constructible leaves the required correction outside the effective space rather than establishing a merely empirical handicap.
2. **“Here the fixed choice produces an observed failure: the supplied summary treatment underperforms raw traces. This result shows that the summarize-and-discard representation lost useful distinctions for this proposer and task.”** — THIN — Underperformance supports the claim that the summary treatment was worse in this experiment, but it does not by itself isolate lost distinctions as the cause rather than misleading additions, presentation effects, stochastic variation, or another interaction between the summarizer and proposer.
3. **“Changing the model behind the same explicit interface becomes informative only after comparing the models’ effective update spaces.”** — THIN — Comparing effective update spaces is necessary to infer whether the fixed decomposition admits a correction, but model changes can still be informative about performance, optimization, or capability without that comparison; the sentence leaves its intended object of inference implicit.
4. **“Successful optimization changes downstream variables while the fixed signals, actions, and hypothesis class remain controlled conditions. Improvement therefore shows that the compound configuration sufficed in that context; it does not isolate which fixed choices were necessary or preferable.”** — HOLDS — Observed improvement warrants the narrow claim that the full configuration could produce that improvement in the tested context, while unchanged fixed choices and absent alternatives prevent attributing necessity or comparative superiority to any one of them.
5. **“If every signal and history available to a learner represents two situations identically, even though the objective requires different actions, every policy over that information must treat them alike.”** — HOLDS — Once every available conditioning variable is stipulated to be identical, neither a deterministic policy nor a stochastic action distribution over those variables can respond differently to the two situations.

## For the human
Look first at the treatment of approximation as a merely empirical handicap, because whether approximation remains inside the effective update space depends on whether the objective itself requires the exact response.
