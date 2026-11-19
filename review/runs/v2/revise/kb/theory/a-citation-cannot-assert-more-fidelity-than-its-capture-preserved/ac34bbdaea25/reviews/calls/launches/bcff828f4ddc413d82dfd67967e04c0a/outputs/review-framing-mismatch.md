---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Two spans at the same file offset can differ in provenance quality by a full layer"
    reason: "Within one snapshot, a single file offset identifies one passage. That passage lies either in the verbatim block or in the paraphrase summary, so two spans at the same offset cannot come from different layers. The real mechanism is different: a bare position does not show the consumer which layer it falls in. Spans that look alike as positions, such as nearby offsets or the same section, can sit in different layers, and the consumer cannot tell them apart without resolving the snapshot. The current framing places the problem in an impossible collision rather than in what the locator exposes."
    level: warn
  - scope: passage
    quotes:
      - "The claim bites exactly where capture is lossy, which is to say wherever the sources are long."
    reason: "This equates lossy capture with long sources. The note's own mechanism covers cases that framing excludes. The second-hand layer arises from intermediaries, such as a news article quoting an order that is no longer served, whatever the source length. Copyright trims can also apply to short sources. Saying the claim applies 'wherever the sources are long' leaves out those cases."
    level: warn
  - scope: passage
    quotes:
      - "If a source is short enough to capture losslessly"
    reason: "This is the same narrowing seen from the other side. The text says a short source collapses the layers to one, but brevity removes only the verbatim/paraphrase split. A short capture can still be second-hand, so the bound does not become vacuous merely because the source is short."
    level: warn
  - scope: passage
    quotes:
      - "Any framework whose consumer is an LLM and whose sources are real documents faces both"
    reason: "The copyright barrier applies to copyrighted sources, not to all 'real documents'. Public-domain material, much court and government material, and a project's own documents do not face it. The framing overstates the generality of one of the two forcing reasons. This matters to the section's 'forced' claim, but it does not exclude cases the mechanism covers."
    level: info
outcome: warn
---

# Review

The core mechanisms are framed at the right level. Fidelity is non-increasing because only verbatim text has a mechanical derivation rule. Notation can express the bound but cannot move it, and re-capture is the only repair. The problems appear where the note maps its mechanism onto concrete cases. The locator corollary places the problem in a same-offset collision that cannot happen within one snapshot. The Scope section uses source length as a stand-in for lossiness, which drops the second-hand layer and short copyrighted sources from a claim whose mechanism covers them.
