---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This note concerns the code-extraction case: committing an interpreted rule to a script, executable test, schema, or validator whose behavior can be inspected and checked at acceptable cost."
      - "The replacement can itself be codified by adoption; what relaxing reverses is the extraction, not symbolic membership."
    reason: "Scope drift. The H1 names codification in general as one of the two navigating moves. The body narrows that move to code extraction: committing an interpreted rule to an inspectable script, test, schema or validator. It also states that codification by adoption, such as adopting a model package, falls outside this case. Relaxing is defined as reversing the extraction, not codification. The bet section is headed 'Every code-extraction codification is a bet'. What the body now establishes is that code extraction and relaxing navigate the bitter lesson boundary. Because the body declares a different scope, the title's unqualified 'Codification' is broader than what the body argues. Qualifying the title, for example with 'Code extraction and relaxing ...', would align it."
    level: warn
outcome: warn
---

# Review

## Summary

The body supports the title's central claim. The bitter lesson boundary between the arithmetic and vision-feature regimes cannot be identified in advance. Practical systems therefore commit structure, treat each commitment as a bet, and relax it when scale makes a general replacement viable. The trade-off section, the bidirectional trajectory, the bet framing, spec mining, relaxing signals and the working heuristics all serve that navigation claim, so there is no claim drift.

The mismatch is in scope. After revision, the body explicitly limits itself to the code-extraction case of codification. It excludes codification by adoption, and it defines relaxing as reversing an extraction. The H1 still says "Codification" without qualification, so it promises a broader scope than the body covers. The finding gives the narrower claim the body now establishes, so the title can be corrected to match.
