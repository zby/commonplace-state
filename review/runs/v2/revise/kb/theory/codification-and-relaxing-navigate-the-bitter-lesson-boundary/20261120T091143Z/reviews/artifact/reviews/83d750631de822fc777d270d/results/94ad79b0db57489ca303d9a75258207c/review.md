---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - They formalized subproblems — edge detection, corner detection — without a working
    "seeing" system to extract from.
  reason: 'DEFEATED — premise (no stated mode, so universal): the vision researchers''
    decompositions were theorized with no working seeing system to extract from and
    no evidence of successful composition; this is the contrast on which spec mining''s
    advantage rests — counterexample: biological vision was a working seeing system,
    and early vision features were partly extracted from it; Hubel and Wiesel''s orientation-selective
    V1 cells and the explicitly biologically motivated Marr–Hildreth edge operator
    are a checkable case of decomposition mined from observed working behavior that
    still failed to compose into machine seeing; learned CNNs also rediscover edge-like
    first-layer filters, so the extracted regularity was partly load-bearing and what
    failed was the composition above it — the spec-mining contrast survives only if
    ''working system'' is narrowed to the system being codified, observed at its composed
    behavior on the deployment task, not a different substrate whose components are
    theorized to transfer — LOCAL — instance'
- scope: passage
  quotes:
  - a narrower bet with better odds, because you've already observed the behavior
    composing successfully
  reason: 'DOUBTFUL — premise (comparative tendency): observing a working system makes
    an extracted regularity more likely to be load-bearing than top-down theorizing,
    so spec mining ''avoids'' the vision-feature failure mode, as the description
    and the spec-mining footer link put it — reason: observing the system compose
    shows that the system works, not that the extracted pattern is what makes it work;
    working ML systems commonly rely on shortcut or Clever-Hans features, so mining
    their behavior can codify the accident; the body concedes ''it''s still a bet'',
    which conflicts with ''avoiding'' in the description and footer; no comparative
    evidence is given for ''better odds'' — fix by stating the improvement as conditional
    and replacing ''avoids'' with ''reduces'' — LOCAL — instance'
- scope: passage
  quotes:
  - Since you can't reliably tell which regime you're in until scale tests the distinction
  reason: 'DOUBTFUL — premise (universal as stated, softened by ''reliably''): the
    regime is unknowable before scale tests it, and ''most practical codification
    happens in the blurry zone'' (an unevidenced prevalence claim) — counterexample:
    constitutive requirements such as schemas, chess rules and numerical contracts
    are identifiable ex ante, as the note''s own heuristic 1 does; the linked fixed-artifact
    note names non-scale evidence for the requirement–objective link (outcome data,
    predictive tests, ablations, composition); scale is therefore one test among several,
    and identification is a matter of degree — fix by restating as ''often cannot
    tell without end-to-end evidence, of which scaling comparisons are one kind''
    — LOCAL — instance'
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget.
  reason: 'DEFEATED — premise (universal as stated): high epiplexity marks structure
    that is safe to codify and low epiplexity marks likely accidents — counterexample:
    epiplexity is defined relative to a computational bound, so high epiplexity cannot
    certify independence from ''the observer''s computational budget''; a simple exact
    rule such as a fixed arithmetic contract or a constant-format schema has little
    learnable structure for a bounded learner yet is the note''s own safest arithmetic-regime
    codification, so the heuristic mis-sorts the paradigm safe case; what makes a
    regularity ''accidental'' in this note is its relation to the objective, which
    an information measure over observed data does not address — fix by restricting
    the claim to what the measure discriminates (structure vs. randomness at a given
    budget) or removing it as support for codification safety — LOCAL — instance'
- scope: passage
  quotes:
  - This means codification bets in the arithmetic regime are not merely safe-for-now;
    the step-by-step structure that codification encodes is the kind of regularity
    that persists under scaling.
  reason: 'DOUBTFUL — premise (universal: ''permanent advantage''): the induction-bias
    result shows that arithmetic-regime codification persists under scaling — reason:
    the study compares learned architectures (recurrent vs. transformer inductive
    bias) on synthetic modular-addition state tracking, not symbolic code extraction
    against model calls; the linked fixed-artifact note records that the authors bound
    it to a limited model and task set, so ''permanent'' and ''not a temporary one
    that scale dissolves'' extrapolate past the tested range; within the note''s own
    framework arithmetic-regime safety is already definitional (''the spec IS the
    problem''), so the evidence is both mismatched and unnecessary — fix by restating
    as evidence that some step-structured inductive biases retained an advantage over
    the tested scale range — LOCAL — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — unstated premise (the ''codify for current leverage, not permanence''
    heuristic needs this as a general condition): extracted components stay cheap
    to relax later, so codifying now and relaxing on signal dominates waiting — reason:
    codified interfaces commonly accrete dependents that rely on their exact observable
    behavior (Hyrum''s law), and schemas, APIs and validators become load-bearing
    for other code; the replacement then must reproduce accidental behavior or migrate
    consumers, so relaxing can cost more than the original leverage gained; the note
    prices extraction (maintenance cost) but not the reversal — fix by naming relaxing
    cost as a condition of the heuristic, e.g. keep codified components behind narrow
    interfaces — LOCAL — prevalence'
- scope: passage
  quotes:
  - Watch for composition failure as a relaxing signal.
  reason: 'DOUBTFUL — premise (universal as stated): composition failure of codified
    conventions signals that the decomposition should be relaxed — counterexample:
    the linked fixed-artifact note states that incompatible interfaces, inconsistent
    composed specifications, omitted resource limits and execution defects produce
    the same symptom, and that these must be diagnosed before attributing failure
    upward; relaxing in response to an integration defect discards a correct decomposition;
    and re-decomposing into different codified parts is an alternative to relaxing
    — fix by adding the diagnostic precondition — LOCAL — instance'
- scope: passage
  quotes:
  - distribution shift, paraphrase brittleness, and isolation-vs-integration gaps
    reveal when a codified component encodes an accident rather than a spec
  reason: 'DOUBTFUL — premise (universal as stated): these signals discriminate an
    accidental regularity from a genuine spec — counterexample: an exact spec also
    breaks under distribution shift when the adopted requirement itself changes (a
    new input format, a revised contract), and isolation-vs-integration gaps arise
    from integration defects as above; the signals detect a mismatch between component
    and current use, not which side is the accident — fix by stating them as triggers
    for diagnosis rather than as revealing the cause — LOCAL — instance'
- scope: passage
  quotes:
  - Edge detection was codified (hand-coded algorithms), relaxed (replaced by learned
    features), and may re-codify as an accelerator inside a learned architecture.
  reason: 'DOUBTFUL — premise (universal: ''runs in both directions''): the codify–relax
    trajectory reverses, shown by these examples — reason: the reverse-direction examples
    (FlashAttention, tokenizers, a future edge accelerator) are exact implementations
    of operations whose specs are fixed, i.e. arithmetic-regime extractions placed
    inside a learned system; none shows a relaxed vision-feature decomposition returning
    as a codified decomposition of the larger capability; the edge-detection re-codification
    is speculative (''may''); the evidence supports ''arithmetic-regime pieces persist
    inside learned systems'', which is narrower than bidirectional movement across
    the boundary — LOCAL — instance'
- scope: passage
  quotes:
  - '"This endpoint returns X given Y" survives longer than "always process requests
    in three stages."'
  reason: 'DOUBTFUL — premise (tendency: ''the more ... the more likely''): specs
    describing what to produce relax less than specs describing how — reason: what-specs
    can be proxy theories too; Canny''s output contract (an edge map with stated optimality
    criteria) is a what-spec, yet it is the note''s central vision-feature example;
    conversely, how-specs that are constitutive of the objective (protocol handshake
    ordering, legally mandated processing stages) are durable; the operative variable
    is whether the requirement is constitutive of the objective, which what/how only
    correlates with — these instances dent the stated tendency without prevalence
    evidence that it reverses — LOCAL — instance'
- scope: passage
  quotes:
  - practical systems will always be hybrids
  reason: 'HOLDS — premise (universal): no realistic system is purely codified or
    purely learned — the hunt found no defeater; even end-to-end model systems depend
    on tokenizers, harness code and validators, and the note''s own adoption caveat
    removes the obvious objection that a model package is ''learned'' rather than
    codified'
- scope: passage
  quotes:
  - the spec fully captures the subproblem, so implementing it need not lose generality
    within that declared scope
  reason: 'HOLDS — premise (conditional on a declared scope): when the spec is constitutive
    of the subproblem, an exact implementation loses no required behavior inside that
    scope — the hunt found no defeater; the premise is near-definitional and the note
    fences it with ''within that declared scope'' and ''relative to that numerical
    contract'', so a subproblem whose inclusion in a larger decomposition is itself
    conjectural is correctly treated as a separate path'
outcome: report
description: Retained report review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/94ad79b0db57489ca303d9a75258207c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/83d750631de822fc777d270d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 94ad79b0db57489ca303d9a75258207c
completed-at: '2026-11-20T09:17:26Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/94ad79b0db57489ca303d9a75258207c/outputs/review.md
raw-output-sha256: 5292aea8ec9ce5107682afee4ad3bcd9c7dabd327363078571249b32e24572cd
format: 2
---

# Premise decomposition: Codification and relaxing navigate the bitter lesson boundary

**Register:** claim
**Central commitment (one sentence):** Because one cannot reliably tell in advance whether a codified decomposition is an exact spec or a proxy theory, practical systems should codify for current leverage and relax when scale makes general components viable, with spec mining from a working system improving the odds over top-down decomposition.

## Premises and counterexamples

The commitment has three load-bearing parts. First, an epistemic premise: the regime cannot be identified ahead of time. Second, a policy premise: provisional code extraction plus later relaxing is the right response, which silently requires that relaxing stays affordable and that the relaxing signals point at the right cause. Third, a comparative premise: spec mining beats the vision researchers' approach because it starts from a working system. The Ebrahimi and Finzi paragraphs, the bidirectional-trajectory examples and the three working heuristics are supporting premises the argument consumes for its safety bounds and its operational advice.

No failure is `GLOBAL`. Codifying under uncertainty and relaxing on signal survives every counterexample found. Each repair adds a boundary condition or narrows evidence. The two defeats are local to their supporting passages. The vision-history defeat damages the spec-mining contrast, which the description puts forward as part of the commitment. The epiplexity defeat removes one supporting argument for codification safety but not the codify-and-relax mechanism. The unstated reversibility premise is the most consequential silent assumption: heuristic 1 recommends codifying "not for permanence" without pricing what makes later relaxing expensive.

## For the human

Look first at the vision-history premise: biological vision was a working system that edge detection was partly mined from. The spec-mining contrast needs to say which "working system" counts, namely the deployed system observed at its composed behavior.
