---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - It cannot work, and the reason is exact rather than merely practical.
  reason: This is an announcement sentence. The heading 'Why notation cannot repair
    it' already says that notation cannot work, and 'exact rather than merely practical'
    only raises the stakes without content. If it is deleted, the paragraph moves
    directly from the temptation to the derived-copy rule and reads as well or better.
  level: warn
- scope: passage
  quotes:
  - Change the premise and the conclusion moves, which is where the claim earns its
    boundaries.
  reason: This is a stock scope-section opener. The next sentence states the premise
    change (lossless short sources) and its effect, so deleting this one loses nothing.
  level: warn
- scope: passage
  quotes:
  - worth stating plainly
  reason: This is a 'worth noting' variant. The clause it sits in carries real content
    (the linked note asserts the complement), so the sentence survives deletion testing.
    The phrase itself could be cut.
  level: info
- scope: passage
  quotes:
  - So a snapshot of a long source is not a copy
  reason: This uses the 'not X — it is Y' elevation shape. It survives the deletion
    test because it introduces the term 'extraction' and leads into the layer list
    ('it stratifies:').
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/2c322b2ce954d0ae908b3c8c/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/2c322b2ce954d0ae908b3c8c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: bcff828f4ddc413d82dfd67967e04c0a
completed-at: '2026-11-16T22:11:38Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-stock-phrases.md
raw-output-sha256: 39176f0787f20b38d8a4a01b4eaee8fd81b9a3274e02926cebc0cec743845bc2
format: 2
---

# Review

Two sentences fail the deletion test. Both are framing moves: one announces an argument, and the other opens the Scope section. In each case, the surrounding text already makes the point. The other pattern matches carry content. They are recorded as info for possible trimming. 'Notation can express the fidelity bound. It cannot move it.' looks like a closing summary, but it adds the distinction between expressing the bound and moving it, so it is not filler.
