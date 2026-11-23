---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The body presents LLM-selected updates without a single score as an empirical bet with no completed end-to-end automated run, not as a demonstrated capability. The noun-phrase H1 does not assert success, so this is not claim drift, but the title does not signal the bet status that the body stresses. Stated for precision if the title is revised: the body establishes that selection-based learning over a readable store can use a robust comparison instead of a scalar score, and bets that a fixed-weight LLM can build the preference model and make that comparison."
    level: info
outcome: pass
---

# Review

The H1 is "Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score". It promises three things: a learning paradigm placed at deployment time, updates selected by an LLM, and selection without a single scalar score.

The body delivers all three:

- **Deployment time:** the routing-line example shows the system adapting across tasks without weight changes. The comparison table places updates at "Deployment time, taking effect on the next task that reads the store", and the body says this marks a lifecycle position, not a speed.
- **Machine learning:** the body positions selection-based learning against direct gradient training. It discusses precedents (Gödel machine, PRODIGY, EURISKO) and why earlier systems did not make it "a general machine learning paradigm", and it answers the Bitter Lesson objection. This supports framing the article as a machine-learning paradigm.
- **LLM-selected, without a single score:** the central argument is that a robust comparison across a preference model can replace one scalar weighting. The bet is that a fixed-weight LLM can build that preference model and make the comparison.

There is no scope drift. The body narrows itself to "one case: a readable store, edited by selected changes". The title's "updates" covers that case without overclaiming weight updates, because the body keeps weights fixed throughout. The evidence and limits sections qualify the claim and do not change it.

The one info finding notes that the title does not mark the claim as a bet. This does not fail the gate, because the title is a topic phrase and does not assert that the capability works.
