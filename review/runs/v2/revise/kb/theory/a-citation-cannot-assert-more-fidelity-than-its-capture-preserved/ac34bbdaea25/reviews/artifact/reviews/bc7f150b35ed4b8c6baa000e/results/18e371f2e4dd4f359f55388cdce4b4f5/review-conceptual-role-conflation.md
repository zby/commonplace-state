---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Any locator design must encode the layer.
  reason: '''Layer'' occupies two roles in the note. It is a region of the snapshot
    artifact (''the snapshot''s verbatim block'', ''its paraphrase summary''), and
    it is a fidelity grade of a passage, a property that also covers ''second-hand'',
    which is not a snapshot region but a fact about the source chain. Reading 1: the
    locator must record which snapshot region a span came from, a structural fact
    that a position in the snapshot file already determines. Reading 2: the locator
    must carry a fidelity grade that position cannot determine, including second-hand
    status. The choice changes what the corollary contributes: under reading 1 a richer
    position suffices and ''position-only'' locators are not underspecified; under
    reading 2 the locator must carry an independent assertion. The author must decide
    whether a layer is a region of the snapshot or a grade of a passage and say which
    one the locator encodes.'
  level: warn
- scope: passage
  quotes:
  - This is the citation-fidelity instance of a general rule
  reason: The passage presents the fidelity bound as an instance of the linked rule.
    That rule concerns an artifact's production history, whereas this note concerns
    the content of an external source that still exists. Whether the note applies
    the history rule, or extends it by analogy to source content, decides what it
    inherits. The neighbouring 'recoverable only by returning to the authoritative
    artifact' points toward analogy rather than instantiation. This is plausible but
    may be immaterial, because the note's own argument does not depend on the history
    rule.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/bc7f150b35ed4b8c6baa000e/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/bc7f150b35ed4b8c6baa000e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:28Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 276697cc7fbaddd3d60db2e2086449c7e61ecf6daeefe2baebd734195e69dcbf
format: 2
---

# Review

The note separates fidelity from authority well. It defines both terms, attributes the authority claim to the linked trace-memory note, and states how the two compose. That passage passes.

The material conflation is in the corollary. Earlier sections introduce layers as kinds of material in a snapshot: a verbatim block, a paraphrase summary and second-hand text. The corollary then treats "the layer" as a provenance grade that a locator encodes alongside position. These are an object (a region of the artifact) and a property (a grade of a passage), and the two readings give different conclusions about whether position-only locators are underspecified. The sentence "Two spans at the same file offset can differ … by a full layer" makes sense only under the property reading, but the example illustrating it uses the region reading.

The "instance of a general rule" passage is noted as INFO. Instance versus analogy affects what is inherited, but nothing in the central argument rests on that choice.
