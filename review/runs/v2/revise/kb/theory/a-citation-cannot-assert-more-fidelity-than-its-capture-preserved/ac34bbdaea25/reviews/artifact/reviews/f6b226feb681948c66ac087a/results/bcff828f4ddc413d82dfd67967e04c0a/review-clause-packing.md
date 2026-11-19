---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - and no rival capture design drops the layering while preserving the commitments
    the framework has already made
  reason: 'The opening sentence of ''Capture is layered because it is forced to be''
    runs to about 45 words. It packs three separate ideas: the layering is not a design
    choice, a linked rule given as a bare 16-word title-clause after the dash, and
    the claim that no rival capture design preserves the framework''s commitments.
    The reader must hold the inserted title open while working out how it relates
    to the clauses on either side. Split it: state that the layering is not a design
    choice, then give the rival test with its link in a separate sentence.'
  level: warn
- scope: passage
  quotes:
  - comes from both epistack casebook work in the sibling
  reason: 'The evidence sentence in the footer runs to about 55 words. Its subject
    (''Evidence for the layering and for the failure of naive verbatim marking'')
    is long, and the verb ''comes'' carries two sources. After the colon, the participle
    ''run over that corpus'' separates the subject ''checker'' from its verb ''found'',
    and the sentence ends with an audit qualifier. Split at the colon: one sentence
    names the evidence sources, and a second reports the checker''s result.'
  level: warn
- scope: passage
  quotes:
  - hosted providers' output filters on mass verbatim reproduction add a third barrier
  reason: This sentence is just under the threshold, but it chains a two-condition
    subject, a semicolon, a third barrier and a contrast ('but that one is provider-contingent
    rather than inherited'). The provider-filter aside could be its own sentence.
    Only borderline.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/clause-packing.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/clause-packing.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f6b226feb681948c66ac087a/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/f6b226feb681948c66ac087a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: bcff828f4ddc413d82dfd67967e04c0a
completed-at: '2026-11-16T22:11:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-clause-packing.md
raw-output-sha256: 5495d0edd88849fe73309631363933d05a8653852872bf16000f8c280346c1b0
format: 2
---

# Review

Most sentences in the note stay within two or three ideas. The long appositive definitions of *Authority* and *Fidelity* each open one long dependency between subject and verb, and the gate treats one such dependency as tolerable. The two flagged sentences are different: each combines more than three ideas with an interruption that the reader must hold open. In the first, the interruption is the linked title inserted after a dash. In the second, it is a long compound subject plus a participle placed between subject and verb. A split at the existing seam (the dash or the colon) fixes each sentence and loses no relation.
