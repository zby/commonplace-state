---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The only operation that raises fidelity is re-capture."
    reason: "Unresolved scope of the operation 're-capture'. Reading 1: it means rerunning the ingest or snapshot step that produces the captured artifact. Reading 2: it means any return to the authoritative artifact to extract the source's words, which the Scope section's 'return to the authoritative artifact and quote-mine it' suggests and which could happen during authoring or review. The choice is material. Under reading 1, an author or a review gate that reads the sibling PDF and replaces a paraphrase with an exact quote raises fidelity without re-capture, which falsifies the opening claim that 'no review gate can promote a passage'. Under reading 2 that claim survives, but only because any such promotion counts as re-capture. The recommendation also changes: under reading 1 load-bearing passages must be promoted at ingest, while under reading 2 they can be repaired downstream by consulting the original."
    level: warn
  - scope: passage
    quotes:
      - "Two spans at the same file offset can differ in provenance quality by a full layer"
    reason: "Unresolved comparison basis: the offset of which file? Reading 1: an offset in the snapshot file. A span from the verbatim block and a span from the paraphrase summary then occupy different offsets, so a position-only locator does distinguish them and the corollary's argument fails. Reading 2: an offset in the authoritative source. Both spans then refer to the same source location, and only a layer field can distinguish them. This premise carries the conclusion 'Any locator design must encode the layer', and only reading 2 supports it."
    level: warn
outcome: warn
---

# Review

Two load-bearing assertions remain materially open.

The opening's "only re-capture raises fidelity" carries the note's distinctive prediction: downstream notation, locators and gates cannot help. Whether that prediction is substantive or definitional depends on what counts as re-capture. The Scope section's recommendation ("promoted … at capture time, or the author must return to the authoritative artifact") puts both readings next to each other without choosing between them.

The corollary rests on an example whose truth depends on which file the offset indexes. The corollary is a design recommendation for locator schemas, so the unresolved choice changes the intervention as well as the argument.

Other assertions passed this gate. "Fidelity" and "authority" are defined in the second paragraph. The three layers each come with an operational test: string match, no quotation marks with the PDF as reference, and a named intermediary. The Scope section states what changes for lossless sources.
