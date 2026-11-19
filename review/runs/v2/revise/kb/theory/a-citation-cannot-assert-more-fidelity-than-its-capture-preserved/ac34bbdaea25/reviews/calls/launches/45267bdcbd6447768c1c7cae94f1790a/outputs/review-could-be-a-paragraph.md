---
type: types/review-result.md
findings: []
outcome: pass
---

# Review

## Summary

Collapsing the note into one paragraph would lose several separately load-bearing elements, so the multi-section structure is justified.

## What a one-paragraph version would lose

The headline ("fidelity is fixed at capture; only re-capture raises it") fits in a sentence, but the note does more than state it:

- **The fidelity/authority distinction.** It reconciles the claim with the linked note saying authority is earned after capture, and gives the composition rule (capture sets a ceiling; authority is earned beneath it). This is a non-obvious inference, not background.
- **Why the layering is forced.** Finite context and copyright are inherited constraints; provider output filters are flagged as contingent. This support path carries the claim that no rival design avoids the layers.
- **The mechanism for "notation cannot repair it".** A paraphrase has no mechanical derivation rule, so marking it `verbatim` produces a trusted hand-maintained copy with a stronger trust signal. This step turns a practical observation into a principled impossibility.
- **The locator corollary.** Two spans at the same offset can differ by a full layer, so a position-only locator is underspecified. This is a design consequence a reader would act on.
- **The boundary case.** For losslessly capturable sources the layers collapse and position becomes the binding constraint again, which also scopes the corollary.

A single paragraph could hold all of these only by compressing each into a clause, losing the inference steps and the boundary condition. The note is not over-complex for its content.
