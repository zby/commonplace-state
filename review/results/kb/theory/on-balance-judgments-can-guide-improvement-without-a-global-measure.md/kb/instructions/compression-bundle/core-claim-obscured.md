---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 0205603a70c3449cb2839af267d72f68
completed-at: '2026-11-20T18:54:49Z'
findings:
- scope: passage
  quotes:
  - Neither needs a score for every Python release before choosing the next one to
    use.
  reason: 'The body''s first statement of the title claim comes only at the end of
    the second paragraph. It is phrased as a remark about two programmers, not as
    the general thesis that an on-balance judgment rests on reasons and needs no global
    score. The Python 2 text-handling detail before it and the random.py paragraph
    after it are three examples in a row before the first heading. The title carries
    the claim, so readers can find it. Adding one plain sentence after the opening
    example would make the general claim easier to remember: reasons naming what changed,
    for whom and why it matters can justify preferring a successor without a global
    score.'
  level: info
- scope: passage
  quotes:
  - investigate an unknown only if a plausible answer could reverse the choice
  reason: 'The note''s most usable rule is the reversal test for which uncertainties
    justify investigation. The description promises it, but it first appears in the
    middle section. Its applications in the AGENTS.md example come two sections later.
    A one-clause preview near the opening would make the second half of the claim
    prominent: act on the judgment and investigate only unknowns that could reverse
    it. This would keep the rule from reading as one point among several.'
  level: info
- scope: passage
  quotes:
  - Suppose a public library can staff either Tuesday morning or Saturday morning,
    but not both.
  reason: 'The library-hours case appears inside the section titled as a Python 3.11
    release judgment. It introduces a separate point: whose work the decision serves,
    as opposed to uncertainty. It is defensible support, but its placement interrupts
    the worked release judgment. The note''s own summary says that what transfers
    from it is the question of whose loss a higher total can hide. Moving or folding
    that point into the ''Who gains, and who bears the loss?'' bullet would keep the
    release section focused on the main claim.'
  level: info
contract: verdict
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/0205603a70c3449cb2839af267d72f68/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/e66c0374b06a1ee684806384/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/0205603a70c3449cb2839af267d72f68/outputs/review.md
raw-output-sha256: ee48c59c14ea0bfb7f05fbd65a69df486bcdb91042aa65a4123673db3fb7839a
---

# Review

## Summary

The core claim is stated plainly in the title: reasons about which work changed, for whom and why it matters can justify preferring a change without a global score. The description adds a second element: investigate an uncertainty only if a plausible answer could reverse the choice. The later sections mostly serve this claim. The 3.11 release table shows reasons replacing a score. "What analysis can settle" separates evidence from weighting. The Commonplace section declares the objective that its own judgments use. The final section applies the reversal test to an `AGENTS.md` line.

The note's shape makes the claim less memorable than it should be. It does not hide the claim. The body opens with three concrete examples before any general sentence says what they show. The investigation rule from the description arrives mid-note. The library-hours digression sits inside the Python release section. None of these needs a WARN, because the title, the second paragraph and the bolded rule each make the claim findable on one reading. The simplest repair is to add one general sentence after the opening Python example that states both halves of the claim. Placing the library case beside the "who bears the loss" bullet would also help.
