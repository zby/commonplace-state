---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Adaptation takes effect immediately at deployment time without waiting for a retraining run"
    reason: "The sentence presents immediate deployment-time adaptation as a payoff of storing retained content in readable, addressable artifacts. The mechanism is the update path: artifact revision run within the deployed system's operating cadence. The linked note explicitly separates lifecycle phase, update latency and representational form, and says 'during deployment' does not by itself make a change fast. Readability is neither necessary nor sufficient for this payoff (online weight training also updates during deployment), so the framing misattributes the mechanism and overstates the speed."
    level: warn
  - scope: passage
    quotes:
      - "cheap to revert"
    reason: "The worked example frames reversibility as how cheaply the line can be reverted, and the later on-balance paragraph cites this example as the use of 'reversibility to limit future loss'. The linked reversibility note says the time to edit an instruction does not bound how long it remains in use. What bounds the loss is how soon a mistake is detected and corrected, which losses stop at correction, and what has come to depend on the change. Framing the bound as revert cost points the reader at the wrong mechanism, using the note's own routing-instruction case."
    level: warn
  - scope: passage
    quotes:
      - "the bottleneck was always"
    reason: "The section claims that the bottleneck in all three precedents was what played the value-function role. Its own EURISKO paragraph, however, credits EURISKO with double-loop criterion revision and attributes its limit to brittle symbolic heuristics and repeated human intervention, which are problems of representation and credit assignment. 'Always' frames every precedent through the judge slot, which excludes mechanisms the section itself reports."
    level: warn
  - scope: passage
    quotes:
      - "Deployment time, taking effect on the next task that reads the store"
    reason: "The table presents update timing as a structural axis separating deliberative learning from weight training. Timing is a lifecycle property: weights can be updated online during deployment, and a store can be edited offline. The row emphasizes the typical case rather than a defining contrast."
    level: info
  - scope: passage
    quotes:
      - "weights-only continual learning wins those domains"
    reason: "Failure of automated language-model judgment would defeat this bet. It would not by itself establish that weights-only learning wins, since human-judged or hybrid loops would remain. The conclusion is framed as a two-way contest that the stated test does not decide."
    level: info
outcome: warn
---

# Review

## Summary

Three passages misidentify the mechanism behind a claim. The first payoff of readable storage credits form with a speed benefit that comes from the update path. The routing-line example, reused as the article's illustration of reversibility, frames reversibility as cheap reverting rather than as bounded detection and correction. That is the mistake the linked reversibility note warns against. The precedents section says the value-function role was "always" the bottleneck, but its own EURISKO paragraph points to brittle representation and human intervention. Two further framings emphasize one case without strictly excluding others and are recorded as info.
