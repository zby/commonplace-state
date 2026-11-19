---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A model may need several reads to check a source that exceeds its context budget."
    reason: "This three-sentence paragraph makes one boundary point: an exact excerpt can omit the context needed to judge support, so the checker must retrieve that context. The opening setup about a context budget and the closing remark that the full source can stay outside the model's context are operational detail. The point could be one sentence attached to the preceding paragraph on retained, accessible and used material. It is flagged INFO, not WARN, because the paragraph is short and links the four-question split to a concrete checking situation."
    level: info
outcome: pass
---

# Review

## Summary

The note is dense, and most of its detail carries a premise or a boundary condition for the main claim: a quote check certifies wording only relative to the evidence it used. No detail clearly needs compressing in place. One paragraph is probably a little long; it is reported as INFO.

## Non-obvious passes

- **The source-identity paragraph** has many sentences: checksum binding, failure on mismatch, the binding stopping at the capture, pins, and context changes going undetected. Each sentence sets a separate limit on what a pass establishes, which is the title claim. Compressing it would remove boundaries rather than restate them.
- **The casebook corpus sentence** under normalization is a single sentence. It explains why a permissive rule is dangerous, so it is a grounding premise, not an illustration that has grown too long.
- **The semantic-hops sentences** in the second-hand provenance paragraph go slightly beyond exact quotes. They contrast exact chains, where each check covers only its own pair, with semantic chains that compound judgment. They end in a practical recommendation and take only two sentences, so their length fits their role.
- **The Scope list** gives one line per exclusion or open question. That length is proportionate.
