---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
note-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: f659852806da4ec990f8ef2014eb90d0
completed-at: '2026-11-20T09:16:22Z'
findings:
- scope: passage
  quotes:
  - This means codification bets in the arithmetic regime are not merely safe-for-now;
    the step-by-step structure that codification encodes is the kind of regularity
    that persists under scaling
  reason: 'UNSUPPORTED — The cited result concerns architectural induction bias inside
    sequence models trained on state-tracking tasks (sharing factor κ across supervision
    formats). The note turns it into a claim about extracting rules into scripts,
    tests or validators, but never connects the two. Model-internal inductive bias
    is not shown to be the same kind of thing as an externally committed procedure.
    The inference is also circular for this note: the arithmetic regime is already
    defined as the case where ''the spec IS the problem'', so the bet there is safe
    by definition and needs no empirical support. Whatever the evidence adds, it cannot
    help with the blurry zone the note says matters most. ''Permanent'' is likewise
    read from a finite set of training runs without saying what scale range they cover.'
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget
  reason: UNSUPPORTED — The note's own gloss defines epiplexity as learnable structure
    'within computational bounds', which makes it relative to an observer's budget.
    So high epiplexity cannot also be what separates real patterns from artefacts
    of that budget. Something that changes as the budget changes is the very scale-dependence
    the note warns about. The section opens by promising results that 'help bound
    when codification bets are safe', but it gives no way to estimate the epiplexity
    of a candidate rule. No bound reaches the codification decision.
- scope: passage
  quotes:
  - a narrower bet with better odds, because you've already observed the behavior
    composing successfully
  reason: 'THIN — What has been observed is the whole working system succeeding. That
    does not show the extracted regularity is a component of that success, or that
    it will still compose once frozen into a check. The next paragraph concedes this
    when it notes that a mined spec may capture an accidental regularity. The contrast
    with the vision researchers (''without a working seeing system to extract from'')
    also goes unexamined: biological vision was a working system to extract from.
    The difference in odds is therefore asserted, not shown.'
- scope: passage
  quotes:
  - Since you can't reliably tell which regime you're in until scale tests the distinction,
    practical systems will always be hybrids
  reason: THIN — Not knowing the regime does not by itself produce hybrids. That uncertainty
    is compatible with hedging toward all-learned or all-codified systems. Hybridity
    follows better from the coexistence of both regimes and from cost, which the note
    brings in only later. 'Always' goes beyond what the premise supports. The claim
    of unknowability also sits uneasily with the heuristics, which classify cases
    confidently (a numerical contract versus a three-phase workflow) before any scale
    test.
- scope: passage
  quotes:
  - If codified conventions don't compose into better systems, that's the signal to
    relax
  reason: THIN — A composition failure fits several causes besides a codified vision
    feature. The decomposition may be wrong but still codifiable at a different grain,
    the implementation may have a defect, or the integration may be poor. The heuristic
    does not separate these causes. It also does not show that a more general replacement,
    as opposed to a different extraction, is the right response. The linked relaxing
    signals (isolation-versus-integration gaps) are named earlier but not used to
    narrow this inference.
contract: report
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/f659852806da4ec990f8ef2014eb90d0/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/65ef8c5253ecbf5eec8d82a8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/f659852806da4ec990f8ef2014eb90d0/outputs/review.md
raw-output-sha256: fd79c57282a16e2cbc80e204b7db67ae40c52a4206a65666700724c00b0a92b8
---

# Friction check: Codification and relaxing navigate the bitter lesson boundary

**Central claim (one sentence):** You cannot tell in advance whether a codified decomposition is an exact spec or a proxy theory. Practical systems should therefore codify for current leverage and relax extracted components when scale or relaxing signals show they excluded needed generality, and mining specs from working systems lowers the risk of codifying an accident.

## Filter
**Filter:** SURVIVES

The note commits to three things: commit to code now, stay ready to reverse the commitment, and treat the regime as unknowable in advance. These can coexist as a policy of provisional commitment. One tension remains. The note says the regime cannot reliably be identified before scale tests it, yet the heuristics and the Ebrahimi paragraph assume that clear arithmetic-regime cases can be recognized and treated as safe. This does not split the claim apart, because unknowability can be restricted to the "blurry zone". But the note never states that restriction where it makes the claim.

## Thinnest joints
The two evidence paragraphs rank lowest. They are where the note claims its strongest support ("formal results help bound") and where the link from cited result to codification decision is missing. In the epiplexity case the gloss also conflicts with the inference drawn from it. The spec-mining joint comes next: it carries the note's practical recommendation, and the note itself admits the counter-case one paragraph later. The opening "since → hybrids" inference and the composition-failure heuristic are thin rather than unsupported. Each points at a plausible mechanism but bundles alternative causes with it. The regime definitions and the bidirectional-trajectory examples (edge detection, FlashAttention, tokenizers) were also checked. They hold reasonably well, so they are not surfaced.

## For the human
Look first at the Ebrahimi paragraph. Either show how model-internal induction bias bears on extracting rules into external code, or cut the inference, since the arithmetic regime is already safe by definition.
