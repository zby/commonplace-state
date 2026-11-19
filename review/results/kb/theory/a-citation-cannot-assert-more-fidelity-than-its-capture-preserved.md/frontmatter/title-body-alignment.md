---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 407aca7c49aa59c074fe5ba49bd6068ac014d92505a36ed563b9da15216e4247
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 203afe73cbd44d0185433c6a6520fe02
completed-at: '2026-11-18T16:01:30Z'
findings:
- scope: document
  quotes: []
  reason: 'Scope drift: the title covers only the capture boundary, which is one paragraph
    of one section. Most of the body is a general account of quote checking: four
    separable questions with only wording answered mechanically, what makes ''exact''
    meaningful through normalization rules, occurrence versus location and uniqueness,
    checking cost against reliance risk, multi-read context retrieval, and exactness
    versus second-hand provenance across intermediary chains. The description itself
    announces ''Quote checking in general''. Body now establishes: a quote check answers
    only the wording question, and its pass means agreement with whatever evidence
    it used under a stated normalization and uniqueness rule; attribution, context
    and truth stay unverified.'
  level: warn
- scope: passage
  quotes:
  - A pass means "agrees with the evidence this check used". That evidence may be
    the original, a capture (a retained copy of the source bytes taken at one time),
    an intermediary's retained extract, or nothing.
  reason: 'Claim drift: the title says what a citation can assert and names the capture
    as the bound. The body says a citation asserts that words occur in a named source,
    and what is limited is what a check can verify. That verification is relative
    to the evidence used, which may be the original, a capture, an intermediary''s
    extract or nothing, not always a capture. Body now establishes: a check''s pass
    certifies agreement only with the evidence it compared against, and no mechanism
    verifies that this evidence faithfully represents the original.'
  level: warn
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/cd2a4ba03a344eb9675795c6/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/cd2a4ba03a344eb9675795c6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/203afe73cbd44d0185433c6a6520fe02/outputs/review-title-body-alignment.md
raw-output-sha256: 29b910f3c250ab7a228f983c266c23b86136d8c5c6b9b29731a7e52cf83c1e27
---

# Review

The H1 says a citation cannot assert more fidelity than its capture preserved. The body supports a version of this claim. The section "Which evidence a pass is relative to" says the binding stops at the capture and that missing bytes report as unverified. So the title is not false to the body.

The title is narrower than the body, and it phrases the claim along a different axis. The body opens with what a citation asserts. It then spends most of its length on what a quote check can and cannot establish: wording only (not attribution, context or truth), relative to a normalization rule, unambiguous only under a uniqueness constraint, and relative to whichever evidence was used. The capture is one possible evidence base among several, and the body also discusses intermediary extracts and the absence of any evidence. A title that tracks the body would name quote checking, or the relativity of a pass to its compared evidence, rather than citation fidelity bounded by a capture.
