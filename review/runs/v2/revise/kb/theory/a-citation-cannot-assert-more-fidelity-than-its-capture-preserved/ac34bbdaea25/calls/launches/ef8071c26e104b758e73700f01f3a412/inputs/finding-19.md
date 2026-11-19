---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: bcff828f4ddc413d82dfd67967e04c0a
completed-at: '2026-11-16T22:11:38Z'
findings:
- scope: passage
  quotes:
  - The layering is not a design choice
  reason: 'After the dash, the sentence inserts a title-as-claim link as a bare clause:
    ''a framework rule with a boundary-preserving rival is not an inherited constraint''.
    Nothing signals its role. A plausible first reading asserts that clause of the
    layering, as if the layering had a boundary-preserving rival and so was not inherited.
    That is the opposite of the intended point. The intended reading, that the link
    names the test the layering passes, has to be reconstructed from the next clause.'
  level: warn
- scope: passage
  quotes:
  - what was not preserved verbatim then is permanently downgraded
  reason: '''then'' can be read as temporal (''at ingest'') or as consequence (''therefore'').
    The next words, ''recoverable only by…'', also make ''permanently'' look contradictory
    unless the reader takes ''permanently'' to mean ''within this capture''.'
  level: info
- scope: passage
  quotes:
  - A position-only locator would render them identical, which is the one distinction
    a consumer of the citation most needs.
  reason: The 'which' clause attaches grammatically to 'render them identical', so
    the sentence literally calls the identity a distinction. Readers will probably
    recover the intended meaning, that the erased difference is the distinction consumers
    need, but the reference is loose.
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/da50eb5867209036dc93f8e4/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/da50eb5867209036dc93f8e4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/bcff828f4ddc413d82dfd67967e04c0a/outputs/review-parsing-ambiguity.md
raw-output-sha256: 13c5852a19b85fa3669970bca7518d3b1985bcd1ac84ac7489275e4b85fb832c
---

# Review

Most sentences parse cleanly. Negation scope in 'This is a claim about fidelity, not authority' and 'is out of scope rather than in conflict' is clear. The pronouns in the Scope section ('that design', 'it') resolve to their nearest plausible antecedents. The warn finding is the title-as-clause construction: placed after a dash with no connective, the linked rule reads as something said about the layering, and that reading reverses the argument. Adding a connective that names the link's role (for example, 'by the rival test in …') would remove the ambiguity.
