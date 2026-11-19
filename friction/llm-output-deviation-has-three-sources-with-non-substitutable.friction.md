# Friction check: LLM output deviation requires three-way diagnosis because remedies target different relations

**Note:** kb/notes/llm-output-deviation-has-three-sources-with-non-substitutable.md
**Central claim (one sentence):** For a fixed assembled input, unwanted LLM output should be diagnosed separately as `V` exceeding `I`, `D` escaping `V`, and `D` being too dispersed, because prompt narrowing, error correction, and sampling control each primarily repair one of those relations and therefore do not substitute as complete repairs.

## Filter
**Verdict:** SURVIVES
The claim can commit to one consistent thing: after the input is fixed, three diagnostic relations can coexist, share cross-effects, and still justify different first repair surfaces; “non-substitutable” only needs to mean “not a guaranteed complete repair for the other relations,” not “changes only one knob in isolation.”

## Signal — thinnest joints
1. **“Any system that runs `specification → interpreter → sampled execution` raises the same questions, whether the interpreter is an LLM, a contractor working from a brief, or a compiler for a language with implementation-defined behavior.”** — THIN — The note has shown the three relations inside its LLM setup, but it does not map the contractor and compiler cases carefully enough to show that the same `V`/`D` structure, especially the sampled-`D` part, carries over unchanged.
2. **“Hold public meaning fixed and vary only surface style or the ordering of equivalent candidates: systematic performance change reflects interpreter sensitivity because `V` did not move.”** — THIN — This uses “same public meaning” as if it settled `V`, but that is exactly the contested step when form changes alter salience, parsing, or pragmatic force for the interpreter.
3. **“It does not measure underspecification, because if public meaning is fixed, `V` is fixed too.”** — THIN — The inference is only as good as the previous identification of public-meaning preservation with a fixed admissible set, so the exclusion of underspecification is not established independently.
4. **“Materially different auditor-accepted analyses support a plural `V`, conditional on that auditor.”** — THIN — Accepted variety is evidence that the auditor tolerated multiple outputs, but the step from “auditor accepted both” to “the specification admits a plural `V`” still depends on treating that auditor as the operative validity boundary rather than as another noisy interpreter.
5. **“Rejected noncompliant runs illustrate mass outside `V`, including pilot runs that hallucinated results or recalled published findings.”** — THIN — Observing bad realized runs shows some failure cases, but the sentence slides from sampled rejections to a claim about `D`'s support without saying how much of the distribution or which fixed-input cell those examples actually characterize.

## For the human
Look first at the note's diagnostic tests and external generalization: the core non-substitutability claim survives, but the bridges from “same meaning” to fixed `V` and from auditor behavior to `V`/`D` are where the author's missing concretization shows most.
