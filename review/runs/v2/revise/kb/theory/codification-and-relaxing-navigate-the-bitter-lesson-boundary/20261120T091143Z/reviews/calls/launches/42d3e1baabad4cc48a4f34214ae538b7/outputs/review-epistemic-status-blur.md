---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling'
    reason: 'Spread of support. The reported result concerns architectural induction bias in sequence models on calculator-class state tracking. The conclusion is about codification bets in the arithmetic regime generally, which in this note means committing rules to scripts, tests, schemas or validators. The step from an architecture finding to the durability of code-extraction bets is the note''s inference, but "This means" presents it with the confidence of the experimental result, and "persists under scaling" reads as established.'
    level: warn
  - scope: passage
    quotes:
      - 'High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer''s computational budget'
    reason: 'A proposed application (epiplexity as a guide to which codifications are safe) is stated declaratively under a sentence that calls these "formal results" that "help bound when codification bets are safe". The formal standing of the information-theoretic framework is spread to the note''s own claim about codification safety; nothing marks the latter as a proposal.'
    level: warn
  - scope: passage
    quotes:
      - 'They were betting that theorized components would compose into the target capability, with no evidence of successful composition.'
    reason: 'A historical claim about vision researchers'' epistemic position ("maximum disadvantage", "no evidence") is stated as fact without support on the page. It is illustrative rather than central, so it is recorded as INFO.'
    level: info
  - scope: passage
    quotes:
      - 'survives longer than'
    reason: 'An empirical-sounding comparative (what-specs outlast how-specs) is asserted without evidence. It sits in a section headed "Working heuristics", which partly marks its status, so it is recorded as INFO.'
    level: info
outcome: warn
---

# Review

Much of the note calibrates status well. The central bet framing is marked: "That scale in fact selects on this property is conjectural, not established." Edge detection "may re-codify". Low-epiplexity patterns "may be accidents". Heuristic 1 says the three-phase workflow is "probably" a vision feature. The opening premise, that regimes cannot be told apart until tested, is presented as the note's reasoning and is carried consistently into the title and description.

The failure is concentrated in the evidence paragraphs near the end of "Every code-extraction codification is a bet". Two external results are introduced as formal bounds on codification safety. In each case, the note's transfer from the source's domain (information measures; sequence-model architectures) to code-extraction codification inherits the confidence of the cited result. The epiplexity passage gives no marker. The Ebrahimi passage's "This means" signals inference but asserts the conclusion as settled. A reader cannot separate what the papers established from what the note conjectures about codification.
