# Friction check: Generation confidence does not by itself certify soundness

**Note:** `kb/notes/llm-generation-confidence-tracks-typicality-not-soundness.md`
**Central claim (one sentence):** Generation confidence measures probability under the model's distribution rather than soundness itself, so it can inform correctness decisions only within separately established task-specific evidence, while high-assurance acceptance requires another validated operation.

## Filter
**Verdict:** SURVIVES
The note asks three properties to hold at once: confidence does not entail soundness, confidence may still correlate with soundness on a defined task, and high-assurance acceptance requires evidence beyond confidence. These properties can coexist because the first denies an intrinsic guarantee, the second permits an empirical association, and the third imposes a stronger decision standard.

## Signal — thinnest joints
1. **“The boundary of reliable automation therefore tracks the availability of a verifier”** — UNSUPPORTED — The preceding argument concerns high-assurance acceptance, but “reliable automation” also includes the note's own confidence-based review prioritization and abstention; it does not establish that verifier availability determines the whole automation boundary, nor that availability is sufficient.
2. **“High-assurance acceptance still needs a separately validated operation”** — UNSUPPORTED — Showing that generation confidence does not entail soundness establishes the absence of an intrinsic guarantee, not the necessity of a separate per-output operation; a validated confidence policy could in principle meet a probabilistic assurance threshold unless “high-assurance” or “acceptance” is defined to require claim-specific verification.
3. **“When task-specific evaluation establishes adequate calibration and discrimination, confidence can prioritize review or trigger abstention”** — THIN — Calibration and discrimination describe predictive behavior, but the inference to a useful policy also needs an operating threshold, error costs, and an applicability or distribution-stability condition; “adequate” currently hides those commitments.
4. **“Where correct continuations are more strongly represented than errors, probability may rank them above incorrect alternatives. Where misconceptions or common fallacies are more strongly represented, the ranking can reverse.”** — THIN — “More strongly represented” is not operationalized, so it does not yet identify a measurable condition that supports the claimed ordering rather than merely redescribing it after the fact.
5. **“a human may stall at a weak ‘because,’ but next-token probability does not perform the missing validity check”** — HOLDS — A conditional token probability can correlate with valid inference, but without a separately established relation it is not itself a test of whether the premise supports the conclusion; the human-stall example does not need a stronger claim.

## For the human
Look first at the leap from non-entailment to the claimed necessity of a separate verifier: define the assurance standard that makes the necessity follow, or narrow the claim to a strong practical requirement.
