---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Any locator design must encode the layer."
    reason: "'Layer' occupies two roles in the note. It is a region of the snapshot artifact ('the snapshot's verbatim block', 'its paraphrase summary'), and it is a fidelity grade of a passage, a property that also covers 'second-hand', which is not a snapshot region but a fact about the source chain. Reading 1: the locator must record which snapshot region a span came from, a structural fact that a position in the snapshot file already determines. Reading 2: the locator must carry a fidelity grade that position cannot determine, including second-hand status. The choice changes what the corollary contributes: under reading 1 a richer position suffices and 'position-only' locators are not underspecified; under reading 2 the locator must carry an independent assertion. The author must decide whether a layer is a region of the snapshot or a grade of a passage and say which one the locator encodes."
    level: warn
  - scope: passage
    quotes:
      - "This is the citation-fidelity instance of a general rule"
    reason: "The passage presents the fidelity bound as an instance of the linked rule. That rule concerns an artifact's production history, whereas this note concerns the content of an external source that still exists. Whether the note applies the history rule, or extends it by analogy to source content, decides what it inherits. The neighbouring 'recoverable only by returning to the authoritative artifact' points toward analogy rather than instantiation. This is plausible but may be immaterial, because the note's own argument does not depend on the history rule."
    level: info
outcome: warn
---

# Review

The note separates fidelity from authority well. It defines both terms, attributes the authority claim to the linked trace-memory note, and states how the two compose. That passage passes.

The material conflation is in the corollary. Earlier sections introduce layers as kinds of material in a snapshot: a verbatim block, a paraphrase summary and second-hand text. The corollary then treats "the layer" as a provenance grade that a locator encodes alongside position. These are an object (a region of the artifact) and a property (a grade of a passage), and the two readings give different conclusions about whether position-only locators are underspecified. The sentence "Two spans at the same file offset can differ … by a full layer" makes sense only under the property reading, but the example illustrating it uses the region reading.

The "instance of a general rule" passage is noted as INFO. Instance versus analogy affects what is inherited, but nothing in the central argument rests on that choice.
