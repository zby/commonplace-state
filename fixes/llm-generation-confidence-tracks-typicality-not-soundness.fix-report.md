## Fix Report: llm-generation-confidence-tracks-typicality-not-soundness

Source review run: 2301 (3 warns)

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | prose/anthropomorphic-framing | new-pattern: anthropomorphism-removal | Reframed "a model tuned to please will suppress an inconvenient judgment even where it could produce one" to output-policy language: "that tuning can bias outputs toward agreement even where internal features could support a correction" | fixed |
| 2 | prose/orphan-references | grounding: unsourced addition softened | Softened the unsourced empirical claim "there is evidence models encode some truthfulness signal internally" to an explicitly unsettled possibility ("models may encode some truthfulness signal internally, though that is an unsettled empirical question this note does not adjudicate"); no citation invented | fixed |
| 3 | accessibility/undefined-terms | new-pattern: term-gloss | Glossed `sycophancy` inline on first use: "deployment tuning that rewards agreement with the user over correction" | fixed |

### Warning-to-fix mapping

- **#1 (anthropomorphic-framing):** the sycophancy sentence gave the model agency ("will suppress an inconvenient judgment"); reworded as a property of deployment tuning biasing outputs.
- **#2 (orphan-references):** an empirical-sounding claim had no citation; softened to an explicitly unsourced possibility consistent with the note's `status: speculative` and its own opening caveat. The fix-system rule (no unverified citations) ruled out inventing a source.
- **#3 (undefined-terms):** `sycophancy` was used without a gloss; folded a short definition into the same reworked sentence as #1.

### Deferred items
- (none)

### New patterns
- **anthropomorphism-removal:** a sentence ascribes intent/agency to the model (holding, withholding, suppressing a judgment). Fix: restate as a property of training/tuning or output policy.
