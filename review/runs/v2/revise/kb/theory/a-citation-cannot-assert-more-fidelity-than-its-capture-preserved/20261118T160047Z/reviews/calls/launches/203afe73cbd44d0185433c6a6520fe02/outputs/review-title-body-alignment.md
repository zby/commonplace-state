---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "Scope drift: the title covers only the capture boundary, which is one paragraph of one section. Most of the body is a general account of quote checking: four separable questions with only wording answered mechanically, what makes 'exact' meaningful through normalization rules, occurrence versus location and uniqueness, checking cost against reliance risk, multi-read context retrieval, and exactness versus second-hand provenance across intermediary chains. The description itself announces 'Quote checking in general'. Body now establishes: a quote check answers only the wording question, and its pass means agreement with whatever evidence it used under a stated normalization and uniqueness rule; attribution, context and truth stay unverified."
    level: warn
  - scope: passage
    quotes:
      - "A pass means \"agrees with the evidence this check used\". That evidence may be the original, a capture (a retained copy of the source bytes taken at one time), an intermediary's retained extract, or nothing."
    reason: "Claim drift: the title says what a citation can assert and names the capture as the bound. The body says a citation asserts that words occur in a named source, and what is limited is what a check can verify. That verification is relative to the evidence used, which may be the original, a capture, an intermediary's extract or nothing, not always a capture. Body now establishes: a check's pass certifies agreement only with the evidence it compared against, and no mechanism verifies that this evidence faithfully represents the original."
    level: warn
outcome: warn
---

# Review

The H1 says a citation cannot assert more fidelity than its capture preserved. The body supports a version of this claim. The section "Which evidence a pass is relative to" says the binding stops at the capture and that missing bytes report as unverified. So the title is not false to the body.

The title is narrower than the body, and it phrases the claim along a different axis. The body opens with what a citation asserts. It then spends most of its length on what a quote check can and cannot establish: wording only (not attribution, context or truth), relative to a normalization rule, unambiguous only under a uniqueness constraint, and relative to whichever evidence was used. The capture is one possible evidence base among several, and the body also discusses intermediary extracts and the absence of any evidence. A title that tracks the body would name quote checking, or the relativity of a pass to its compared evidence, rather than citation fidelity bounded by a capture.
