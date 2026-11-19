---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The layering is not a design choice — [a framework rule with a boundary-preserving
    rival is not an inherited constraint](./a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md),
    and no rival capture design drops the layering while preserving the commitments
    the framework has already made.
  reason: The paragraph that supplies the note's premise opens with the inherited-constraint
    test from a related note, then gives the plain causes (finite context, copyright),
    then names and dismisses a third, provider-contingent barrier; the reader meets
    the meta-argument and a discarded cause around the two causes that do the work.
    Lead with context limits and copyright, then add the rival-design test as a trailing
    justification for calling the layering forced, and shrink the provider-filter
    caveat to a brief aside or drop it.
- scope: document
  quotes: []
  reason: 'The Scope section mixes two jobs: a boundary (lossless short sources make
    the bound vacuous) wrapped in an announcing opener and a recap closer, and a practical
    rule (provenance quality is decided before any note is written) that is the note''s
    most usable form of its claim but sits last under a heading that does not name
    it. The re-capture remedy is also stated three times (opening, history paragraph,
    practical paragraph). Cut the opener and closer, separate or retitle the practical
    consequence so its role is visible, and let one statement of the re-capture remedy
    carry the point.'
outcome: report
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/synthesis/artifact/reviews/da7dd4ade5c90b8f46fd2a8b/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/synthesis/artifact/reviews/da7dd4ade5c90b8f46fd2a8b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/synthesis
launch: faee3a0afa3743a9981aae2c4689a09d
completed-at: '2026-11-16T22:13:42Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/synthesis/calls/launches/faee3a0afa3743a9981aae2c4689a09d/outputs/review.md
raw-output-sha256: 1ec3392d97f95340f294f975a3ebbd3e1206894fc702f678e740a69f860a0c19
format: 2
---

# Simplification synthesis: A citation cannot assert more fidelity than its capture preserved

The note is already tight. The core claim is stated in the title and the first paragraph, and every section serves it; branch-bloat passed with no findings. The two opportunities below combine several small findings into revisions of one premise paragraph and one section. Neither changes the thesis. Each makes the role of a passage clearer.

## Opportunities

### 1. Lead the forced-layering premise with its causes

- Location: "Capture is layered because it is forced to be", first paragraph, from "The layering is not a design choice" through "provider-contingent rather than inherited".
- Combines: core-claim-obscured (info: related-note machinery precedes the plain causes); detail-overhang (info: the provider-filter caveat adds nothing to the support route).
- Preserve or decide: Keep the claim that the layering is *forced*, not chosen. The rival-design test is what licenses that word, so a revision should move it, not delete it. The author must decide whether the provider-filter caveat is worth keeping as an answer to the objection that filters were overlooked, or whether it can go. One possible order: context limits and copyright → therefore extraction, not copy → (the rival-design test confirms this is inherited) → the layer list.

### 2. Separate the scope boundary from the practical rule and drop the wrappers

- Location: "## Scope", both paragraphs; also "recoverable only by returning to the authoritative artifact and capturing again" in "Why notation cannot repair it".
- Combines: marginal-value-redundancy (warn: the announcing opener "Change the premise and the conclusion moves…"; warn: the recap closer "The claim bites exactly where capture is lossy…"; info: the third statement of the re-capture remedy); core-claim-obscured's non-defect suggestion to echo "provenance quality is decided *before any note is written*" nearer the opening.
- Preserve or decide: Keep the lossless-source boundary and its consequence that position again becomes the binding constraint for a structured span locator. The corollary depends on that limit. Keep the operational rule: promote load-bearing passages at capture time or re-mine the authoritative artifact. The author must choose where the practical rule belongs. It could stay at the end under a heading that names it, or move toward the opening as the operational form of the thesis. The author must also choose which one statement of the re-capture remedy to keep. If "wherever the sources are long" is wanted, it can fold into the boundary sentence (one possible resolution).
