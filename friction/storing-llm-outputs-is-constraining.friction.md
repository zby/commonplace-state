# Friction check: Selecting an LLM output fixes a result, not its interpretation

**Note:** kb/notes/storing-llm-outputs-is-constraining.md
**Central claim (one sentence):** Selecting, persisting, and giving operative force to one LLM output fixes which version later consumers receive and creates an artifact-testing target distinct from the generator, but it does not determine a unique interpretation of the selected text.

## Filter
**Verdict:** SURVIVES

## Signal — thinnest joints
1. **“Weak or delayed oracles cannot support the same candidate-filtering strategy.”** — UNSUPPORTED — Weakness or delay alone does not rule out candidate filtering: several weak checks can be combined, and a delayed check can still gate adoption when the decision horizon permits. The note must specify the latency or discrimination threshold built into “the same” strategy for impossibility to follow.
2. **“Once a result is selected and made operative, it becomes a stable testing target distinct from the process that generated it.”** — THIN — Selection and behavioral authority establish which result matters, but neither alone makes its bytes stable. The earlier persistence-and-versioning condition supplies stability only if tests and later consumers resolve the same pinned version; this sentence drops that load-bearing condition from its antecedent.
3. **“Artifact checks can also serve as a selection gate when they are sufficiently discriminative, timely, and economical.”** — THIN — These properties make repeated filtering feasible, but discrimination must be relative to the actual acceptance objective and contract. A fast, cheap check that reliably separates candidates on a proxy can still select the wrong artifact.
4. **“A generally reliable generator can still produce a bad sample, while a good artifact says nothing about what another run will produce.”** — THIN — The examples establish that neither test guarantees the other target, which is enough for non-substitution, but “says nothing” is too strong: a representative artifact observation can provide some evidence about the generator even though it cannot characterize its output distribution.
5. **“Selection participates in constraining when adoption excludes interpretations carried only by rejected candidates or gives one resolution downstream force.”** — HOLDS — Either condition narrows which interpretations remain available or authoritative on the consumption path without implying that the selected text itself has only one legitimate reading.

## For the human
Look first at the stable-target step: state explicitly that testing and consumption address the same persisted, version-pinned artifact, because operative selection by itself does not prevent target drift.
