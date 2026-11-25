---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "What makes a mixed prose-and-code store harder to debug than ordinary software is not the lack of gradients, but three properties that weaken ordinary debugging tools"
    reason: "Boundary case between the enumerated items: a well-isolated rule set executed by a sampling LLM can still give different outcomes on identical inputs. That executor nondeterminism weakens reproduction independently of any bad rule. It fits only strainedly under 'Noisier, diffuse failures', whose stated cause is a bad rule quietly degrading other tasks, not the stochastic executor itself."
    level: info
  - scope: passage
    quotes:
      - "Credit assignment here means attributing a failure to retained artifacts in the deployed system's store, not explaining internal activations inside the frozen model's weights."
    reason: "Adjacent boundary case: a failure caused by a model-version or harness change outside the store, with no store edit. The framework presupposes the culprit is an upstream store edit ('which upstream edit (or combination of edits)'). The scope excludes explaining activations but does not say whether deciding store-versus-model responsibility is part of the problem. Ordinary debugging handles dependency upgrades, so the case can be mapped, but the note leaves that mapping to the reader."
    level: info
outcome: pass
---

# Review

## Summary

The note's main enumeration is the three properties that make a mixed prose-and-code store harder to debug than ordinary software. Its secondary lists are the naive workarounds and the debuggability levers. I tested these boundary cases:

- **Simplest instance.** A few isolated rules. The note covers this explicitly ("debugging is trivial") and repeats it under Scope (the flat lookup table).
- **Most extreme instance.** A store of hundreds of densely coupled prose artifacts. Implicit coupling and context saturation cover it, and the closing sentence acknowledges that the scale ceiling is below backpropagation's.
- **Fully codified store.** The note maps this back to ordinary software debugging.
- **Case between items.** Stochastic execution of the same store. It can be fitted under the third property only strainedly.
- **Adjacent concept.** A failure caused by a change in the frozen model or harness rather than in the store. The scope sentence neither includes nor excludes this case.

Neither strained case clearly falls outside the claimed coverage. The three-item list is short and proportionate to its argumentative role. A brief scope clarification would handle both cases better than a fourth category.
