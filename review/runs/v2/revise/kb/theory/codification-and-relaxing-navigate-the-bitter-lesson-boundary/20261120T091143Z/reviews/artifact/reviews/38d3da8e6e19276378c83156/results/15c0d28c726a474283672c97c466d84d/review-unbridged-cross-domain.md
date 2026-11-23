---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This means codification bets in the arithmetic regime are not merely safe-for-now;
    the step-by-step structure that codification encodes is the kind of regularity
    that persists under scaling.
  reason: The source domain is architectural inductive bias and supervision formats
    in trained sequence models on state-tracking tasks. The argument domain is committing
    an interpreted rule to a script, test or validator in a practical system. The
    note goes directly from 'transformers fail to share solutions across lengths'
    to 'codification bets persist under scaling.' It does not state the shared mechanism.
    Why would a training-time advantage of step-by-step architectures show that an
    extracted script will not later be relaxed in favor of a model call? 'The step-by-step
    structure that codification encodes' asserts the correspondence; it does not argue
    for it. The note should state the bridge, for example that both concern whether
    a compositional procedure can be recovered from data at scale, or present the
    result as an analogy.
  level: warn
- scope: passage
  quotes:
  - High-epiplexity regularities are genuinely structural — codifying them is safer
    because they reflect real patterns, not artefacts of the observer's computational
    budget.
  reason: Epiplexity measures structure that a computationally bounded observer (a
    learner) can extract from data. The note turns this into a criterion for when
    a human or agent can safely commit a regularity to code. That transfer needs a
    stated link. Who is the observer in a codification decision? Why does structure
    that is learnable within bounds make an extracted rule less likely to be an accident?
    The follow-on claim, that low-epiplexity apparent regularities 'may be accidents
    visible only at current scale,' adds an inference about scale that the summary
    does not show the framework makes. If the link is only analogical, say so.
  level: warn
- scope: passage
  quotes:
  - Two formal results help bound when codification bets are safe.
  reason: INFO. This framing sentence says both results 'bound' codification safety.
    That overstates what is at most indirect support from machine-learning theory
    until the bridges above are supplied.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/38d3da8e6e19276378c83156/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 15c0d28c726a474283672c97c466d84d
completed-at: '2026-11-20T09:13:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/15c0d28c726a474283672c97c466d84d/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 0b1d51a875527db4096a224bb50f14d1ce7455e9bb5ee5ab5d12089616aeebc1
format: 2
---

# Review

## Summary

The note's argument concerns design decisions in practical, agent-operated systems: when to extract a rule into code and when to relax it. Its two cited empirical and formal results come from machine-learning theory. One is about learnable information for bounded observers; the other is about inductive bias in trained sequence models. Each is presented as direct support ("help bound," "This means"). Neither has a stated mechanism linking a property of model learning to the persistence of hand-extracted or mined code artifacts. The arguments may be repairable, but as written each transfer relies on a resemblance between "structure" in the two domains.

The bitter-lesson history (vision features, edge detection) is used as an illustrative trajectory, not as evidence for a cross-domain claim, so it is not flagged here.
