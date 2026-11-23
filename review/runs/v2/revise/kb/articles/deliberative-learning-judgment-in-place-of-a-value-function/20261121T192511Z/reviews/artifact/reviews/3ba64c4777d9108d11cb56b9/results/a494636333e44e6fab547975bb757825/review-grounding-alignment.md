---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - It kept search-control rules only while a fixed utility formula estimated positive
    time saved
  reason: 'The PRODIGY paragraph rests on an unquoted link to kb/sources/minton-utility-of-ebl-aaai88.ingest.md,
    and the link text does not carry the (snapshot required) marker. That ingest''s
    ## Quotes section says ''No source quotes have been retained yet.'' It therefore
    supplies no source material for the claims that PRODIGY kept rules only while
    a fixed formula estimated positive time saved, that it updated each rule''s estimate
    from later use, or that it dropped rules whose estimate turned negative. This
    paragraph is the article''s evidence for targeted correction in a fixed-formula
    learner. Without retained extracts, material support is absent.'
  level: fail
- scope: passage
  quotes:
  - its own data located the stall in what the proposer was not shown
  - strongest gains came from editing a natural-language lessons file
  reason: 'These claims about the Harness Evolution study have evidential weight.
    They are used to turn the study''s conclusion against itself. They rely on an
    unquoted link to kb/sources/harness-evolution-ceiling-weight-training.ingest.md,
    and the link text has no (snapshot required) marker. That ingest''s ## Quotes
    section retains no quotes. Nothing permitted as support covers ''a quarter of
    runs'', the stall''s location or the claim that the strongest gains came from
    the lessons file. Material support is absent.'
  level: fail
- scope: passage
  quotes:
  - EURISKO's symbolic heuristics remained brittle and repeatedly needed Lenat to
    intervene
  reason: 'The EURISKO ingest''s retained quotes cover only the H12'' episode: the
    heuristic was eliminated, new heuristics were synthesized, and one was kept permanently.
    None of them says that EURISKO''s heuristics were brittle or that Lenat repeatedly
    intervened. The article uses this characterization to say what limited the precedent,
    and the permitted support does not cover it.'
  level: fail
- scope: passage
  quotes:
  - after a badly generalized heuristic wasted effort
  reason: 'The retained quotes support elimination of H12'' and a kept restriction
    (''never replace AND by OR in an If slot''). The article adds two things the quotes
    do not state: the heuristic was ''badly generalized'' and it ''wasted effort''.
    The quotes also describe the restriction as a prohibition, while the article calls
    it ''penalizing''. The double-loop reading survives these changes. The added detail
    is plausible but not grounded.'
  level: info
- scope: passage
  quotes:
  - That buys a formal optimality guarantee relative to those axioms at a steep price
  - no general real-world domain has the full axiomatization required
  reason: The linked Gödel-machine note claims rigor relative to a formalization.
    It also explicitly declines to infer anything about the reachable space or practical
    performance from the admission restriction. It does not claim an optimality guarantee,
    and it does not state that no real-world domain can be fully axiomatized. It also
    calls proof the 'initial admission route', while the article says 'every self-rewrite
    requires' a proof. The article cites the note for a stronger and broader claim
    than the note makes.
  level: warn
- scope: passage
  quotes:
  - Adaptation takes effect immediately at deployment time without waiting for a retraining
    run
  reason: The linked deployment-time adaptation note separates lifecycle phase from
    update latency. It says that 'During deployment' locates the change in the lifecycle
    but 'does not by itself make the change fast'. The article cites the note for
    immediacy, which the note explicitly withholds.
  level: warn
- scope: passage
  quotes:
  - Retained knowledge is inspectable now
  reason: The linked inspectability note limits its claim to readable rules 'at an
    affordable inspection cost'. It notes that large or obfuscated code can obstruct
    inspection and that a prompt's consequences can be opaque. The article states
    inspectability without that condition and adds 'at volumes people could not read',
    which the target does not claim at that scope.
  level: warn
- scope: passage
  quotes:
  - he and Khurram Javed argue that forming new concepts requires continual weight
    updating
  reason: The evidential link goes to an external interview page, which this review
    did not open. The linked Bitter Lesson note in the preceding paragraph says the
    interview treats continued weight updating as necessary for structuring and generating
    new concepts. That is consistent with the article's paraphrase. The direct source
    passage remains unchecked.
  level: info
- scope: passage
  quotes:
  - false-positive acceptance becomes operative
  reason: The target's claim is that nothing downstream of evaluation catches a false-positive
    acceptance. The article's 'until later evidence catches it' brings in a separate
    correction route, and the target's title claim does not supply it. The transfer
    is plausible and does not carry the argument.
  level: info
outcome: fail
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/3ba64c4777d9108d11cb56b9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: a494636333e44e6fab547975bb757825
completed-at: '2026-11-21T19:30:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/a494636333e44e6fab547975bb757825/outputs/review-grounding-alignment.md
raw-output-sha256: 73275281919bbbf895d77f9417db884cd2b4a9039558a1aa9da4635b4c9790ad
format: 2
---

# Review

Most links to library notes represent their targets accurately. These include
the deliberative-learning definition, the on-balance and reversibility notes,
the Bitter Lesson production-method note, the bootstrap condition, compounding,
operative change and objective revision. The article's summary of the
on-balance standard matches the target's statement that every reasonable
measure must favor the successor. The single-loop and double-loop reading of
PRODIGY with Minton follows the definition.

The failures concern unquoted source ingests. Neither the Minton ingest nor the
Harness Evolution ingest retains any quotes. Neither link carries the
`(snapshot required)` marker, so the gate's only permitted support route
provides nothing. The PRODIGY paragraph and the reading of the Harness
Evolution study are both evidential, so the result is FAIL. The EURISKO ingest
retains quotes for the H12′ episode, but they do not cover the article's
broader characterization of EURISKO as brittle and dependent on Lenat.

Three library citations claim more than their targets do:

- **Gödel machine:** the article claims an optimality guarantee and says no
  real-world domain can be fully axiomatized; the target says neither.
- **Deployment-time adaptation:** the article says adaptation takes effect
  immediately, but the target explicitly separates lifecycle phase from
  latency.
- **Inspectability:** the article drops the target's affordability condition.
