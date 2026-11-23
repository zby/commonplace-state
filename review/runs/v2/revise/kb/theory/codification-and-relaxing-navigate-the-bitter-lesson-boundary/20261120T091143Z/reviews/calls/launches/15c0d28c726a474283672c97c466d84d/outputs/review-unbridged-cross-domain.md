---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling."
    reason: "The source domain is architectural inductive bias and supervision formats in trained sequence models on state-tracking tasks. The argument domain is committing an interpreted rule to a script, test or validator in a practical system. The note goes directly from 'transformers fail to share solutions across lengths' to 'codification bets persist under scaling.' It does not state the shared mechanism. Why would a training-time advantage of step-by-step architectures show that an extracted script will not later be relaxed in favor of a model call? 'The step-by-step structure that codification encodes' asserts the correspondence; it does not argue for it. The note should state the bridge, for example that both concern whether a compositional procedure can be recovered from data at scale, or present the result as an analogy."
    level: warn
  - scope: passage
    quotes:
      - "High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer's computational budget."
    reason: "Epiplexity measures structure that a computationally bounded observer (a learner) can extract from data. The note turns this into a criterion for when a human or agent can safely commit a regularity to code. That transfer needs a stated link. Who is the observer in a codification decision? Why does structure that is learnable within bounds make an extracted rule less likely to be an accident? The follow-on claim, that low-epiplexity apparent regularities 'may be accidents visible only at current scale,' adds an inference about scale that the summary does not show the framework makes. If the link is only analogical, say so."
    level: warn
  - scope: passage
    quotes:
      - "Two formal results help bound when codification bets are safe."
    reason: "INFO. This framing sentence says both results 'bound' codification safety. That overstates what is at most indirect support from machine-learning theory until the bridges above are supplied."
    level: info
outcome: warn
---

# Review

## Summary

The note's argument concerns design decisions in practical, agent-operated systems: when to extract a rule into code and when to relax it. Its two cited empirical and formal results come from machine-learning theory. One is about learnable information for bounded observers; the other is about inductive bias in trained sequence models. Each is presented as direct support ("help bound," "This means"). Neither has a stated mechanism linking a property of model learning to the persistence of hand-extracted or mined code artifacts. The arguments may be repairable, but as written each transfer relies on a resemblance between "structure" in the two domains.

The bitter-lesson history (vision features, edge detection) is used as an illustrative trajectory, not as evidence for a cross-domain claim, so it is not flagged here.
