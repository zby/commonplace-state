---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"
    reason: "Precondition 1 applies the omission resolution to natural-language summaries, which must be live reads or omitted. The regime section says that where verification is judgment, 'the hand-maintained dependent artifact is not forbidden; it is unavoidable', and places it under managed staleness. A derived summary is a dependent artifact whose verification is judgment, so one passage forbids keeping it and the other permits it. The Consequences bullet 'When a copy can't be checked, the resolution is omission' sharpens the conflict."
    level: warn
  - scope: passage
    quotes:
      - "There is no safe middle where the copy is maintained by hand and trusted by consumers."
    reason: "The opening says a copy has 'exactly two valid states'; the next sentence restricts the forbidden middle to copies that are both hand-maintained and trusted. This leaves open whether a hand-maintained, untrusted copy is invalid (per the first sentence) or permitted (per the second). This is likely drift needing confirmation."
    level: info
  - scope: passage
    quotes:
      - "When this precondition fails, the value was never a recomputable copy in the first place"
    reason: "Precondition 3 is listed as a condition under which enforcement of a recomputable copy is available. Its own text says that when it fails the value was never a recomputable copy, so it is a definitional exclusion rather than a precondition on enforcement. The framing shifts between the two roles."
    level: info
outcome: warn
---

# Review

The main line is coherent. The asymmetry, the check-price flip, the enforcement-as-third-class section and the consequences agree that recomputable copies must be checked or absent, and that omission is the costlier fallback.

The contradiction lies at the regime boundary. The note works hard to separate the deterministic end, where enforce-or-omit holds, from the judgment end, where a hand-maintained dependent artifact is "unavoidable". Precondition 1 and the third Consequences bullet then assign judgment-verified summaries to omission or live reads, which applies the deterministic-end rule to cases the regime section had placed outside it. A reader cannot tell whether an uncheckable derived summary may be kept under managed staleness or must be removed.
