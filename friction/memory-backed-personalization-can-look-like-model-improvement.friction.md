# Friction check: Memory-backed personalization can look like model improvement

**Note:** kb/notes/memory-backed-personalization-can-look-like-model-improvement.md
**Central claim (one sentence):** Memory can make a system appear to have gained general model capability by restoring user-specific intent omitted from a request, so builders should distinguish the retained information, its activation, and the model's use of it in diagnosis and evaluation.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **“When memory is separately addressable and its interface semantics remain stable across models, holding one memory representation constant while changing models estimates how each model uses that fixed context.”** — UNSUPPORTED — Different outcomes from different models given the same memory can reflect any difference in their general task competence, not specifically how they use the memory; estimating memory use requires a within-model contrast with that information absent or perturbed.
2. **“For builders, separating the carrier from the interpreter improves diagnosis.”** — THIN — Architectural separation makes the stages conceptually distinct, but diagnosis also requires observations or interventions that distinguish non-retention, non-activation, and non-use; the note names those failure modes without specifying how they become discriminable.
3. **“Each retained-intent input needs a source, subject, scope, and status indicating whether it still applies and remains authoritative. Without these controls, memory can confidently supply stale or unrelated intent.”** — THIN — Stale and unrelated recall motivates provenance, scoping, and validity controls, but the examples do not establish that every retained-intent input needs every named field or that those fields are sufficient to prevent the failure.
4. **“Holding the model and request constant while varying memory conditions estimates that model's sensitivity to memory. Crossing these variations exposes compatibility and interaction within the test matrix.”** — HOLDS — Controlled memory contrasts estimate a model-conditional memory effect, and crossing model and memory conditions can reveal whether that effect changes by model, provided the outcome criterion and non-memory conditions are fixed.
5. **“When personalization is encoded in model weights, or when an external memory mechanism co-adapts with the model, treat the model and carrier as a bundled intervention and compare controlled interaction histories or update pipelines instead.”** — HOLDS — Once the carrier and interpreter cannot be varied independently without changing the system being studied, bundle-level comparisons are the coherent causal target; controlled histories or pipelines supply the corresponding intervention unit.

## For the human
Look first at the fixed-memory, changed-model comparison: add the counterfactual that separates model competence from model-specific use of the retained information.
