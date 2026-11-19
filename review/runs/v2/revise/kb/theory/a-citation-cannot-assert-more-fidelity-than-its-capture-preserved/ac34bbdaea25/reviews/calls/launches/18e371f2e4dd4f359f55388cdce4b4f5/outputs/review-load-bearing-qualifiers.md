---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Any framework whose consumer is an LLM and whose sources are real documents faces both"
    reason: "The LLM-consumer condition carries the finite-context-window argument for why layering is forced. The central claim, that a citation cannot assert more fidelity than its capture preserved, does not use it: the derivation-rule argument in 'Why notation cannot repair it' applies to any citation of a lossy capture, including human scholarship. The title and opening are already stated generally, so the qualifier does not narrow the central claim. It is intentional domain scoping of a supporting argument, recorded as INFO."
    level: info
outcome: pass
---

# Review

Qualifiers extracted from the title, description, opening and main argument:

- **"at capture" / "at ingest".** This is load-bearing. The claim locates where fidelity is fixed, and the argument relies on the absence of downstream derivation rules.
- **"by forced constraints" (description).** The deletion test leaves the non-increase argument intact: even if layering were a design choice, a paraphrase would still lack a derivation rule. The phrase explains why layers exist but does not narrow the central claim. Its scope adequacy is a matter for other gates.
- **Long or lossy sources.** This is load-bearing. The Scope section shows that removing the qualifier makes the bound vacuous for lossless captures, so it marks a true boundary.
- **LLM consumer.** It is used only to support "forced" and does not appear in the title or the central claim. INFO.

The title-level claim is not narrower than its argument. No qualifier artificially restricts the central claim's reach.
