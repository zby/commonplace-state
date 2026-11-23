---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 65b1af7d0e1549c4b791c72683f21d7e
completed-at: '2026-11-20T09:15:13Z'
findings:
- scope: passage
  quotes:
  - 'This is not a partition into codified versus learned: an adopted model package
    can itself be a codified reference.'
  reason: 'The opening paragraph states the hybrid conclusion but spends its last
    sentence on a scope caveat, not on the note''s operative claim. It never says
    that the hybrid is navigated by codifying and later relaxing, or that each code
    extraction is a bet. The title''s verb, ''navigate'', and its second term, ''relaxing'',
    get no support in the opening. The caveat could move into the codification-scope
    paragraph, freeing the opening for one plain sentence: treat each code extraction
    as a bet, codify for current leverage, relax when scale makes a general component
    viable, and prefer mined specs because they bet from a working system.'
  level: warn
- scope: passage
  quotes:
  - Retaining a prose convention alone is not codification. Adopting a model package
    can codify an operation without providing this case's readable rules or reducing
    inference cost.
  reason: Before the regime trade-off is stated, the reader has to work through definitional
    boundary work on codification by adoption versus code extraction, plus prose conventions.
    These caveats protect terminology, but they sit in front of the claim and delay
    it. A shorter scope sentence, or a footnote-like placement after the core claim,
    would keep them subordinate.
  level: warn
- scope: passage
  quotes:
  - 'Code extraction therefore has a complement:'
  reason: Relaxing is half of the title's claim, yet it is introduced only in the
    fifth paragraph as a consequence of the regime analysis. Because it arrives after
    the setup, the codify-and-relax pairing is harder to remember as the note's thesis
    than it should be.
  level: info
- scope: passage
  quotes:
  - Transformers show sharing factor κ ≈ 1 or κ < 1 across all supervision formats
  reason: The κ figures are detailed apparatus inside a supporting-evidence paragraph.
    They do not obscure the claim on their own, but they add weight to a section that
    already sits between the bet framing and the working heuristics. The conclusion
    sentence that follows does the work. The numbers could be cut to a parenthetical
    or left in the source annotation.
  level: info
contract: verdict
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/65b1af7d0e1549c4b791c72683f21d7e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/ff9455deba3a1ae9500682c0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/65b1af7d0e1549c4b791c72683f21d7e/outputs/review.md
raw-output-sha256: 5aade34c9067e3f6dab3aae6ecb7beb9b5fb7596816105227c49ad4d6c1aafad
---

# Review

## Core claim

Stated in one sentence from the note's own commitments, the strongest claim is: you cannot tell in advance whether a spec is the problem (arithmetic regime) or a theory of a larger capability (vision-feature regime). Every code-extraction codification is therefore a bet. Practical systems should codify for current leverage and relax when scale makes a general replacement viable. Spec mining improves the bet by extracting from a working system.

The title and description carry this claim. The body's first paragraph carries only part of it: the unidentifiability premise and the "hybrids" conclusion. The rest is spread across paragraphs 3–5 and the "Every code-extraction codification is a bet" section: the bet framing, relaxing as the complement and the spec-mining advantage.

## What obscures it

- **Opening caveat.** The first paragraph ends with an adoption caveat when it should end with the codify-and-relax claim.
- **Definitional scope work.** The second paragraph separates codification by adoption from code extraction and from prose conventions. It is defensible, but it sits between the premise and the trade-off.
- **Late arrival of relaxing.** Relaxing, a title term, first appears after the regime bullets. The bet framing, arguably the most memorable formulation, waits for the second section.

Later material serves the claim reasonably well. The bidirectional trajectory, the vision-researchers contrast, spec mining, relaxing signals and the working heuristics all point back to it. The formal-results paragraphs are heavier than needed but do not change the shape.

## Simplest repair

Rewrite the opening paragraph so it states the full claim plainly. Because the regime can't be identified before scale tests it, each code extraction is a bet: codify for current leverage, relax when scale makes a general component viable, and prefer mined specs over theorized ones. Then compress the adoption and prose-convention caveats into one scope sentence placed after that claim.
