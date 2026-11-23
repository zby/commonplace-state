---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 27dd0e2ad0aa1eef13fef3b88753cda33e00dc316cb3c0fa762816596b8b500c
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 985fe2ad5cc646c0af0e7ad2510f9b5b
completed-at: '2026-11-22T09:33:12Z'
findings:
- scope: document
  quotes: []
  reason: 'The body presents LLM-selected updates without a single score as an empirical
    bet with no completed end-to-end automated run, not as a demonstrated capability.
    The noun-phrase H1 does not assert success, so this is not claim drift, but the
    title does not signal the bet status that the body stresses. Stated for precision
    if the title is revised: the body establishes that selection-based learning over
    a readable store can use a robust comparison instead of a scalar score, and bets
    that a fixed-weight LLM can build the preference model and make that comparison.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/985fe2ad5cc646c0af0e7ad2510f9b5b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/d87c66b365638607cc837e3d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/985fe2ad5cc646c0af0e7ad2510f9b5b/outputs/review-title-body-alignment.md
raw-output-sha256: 9a67b1e5b6e0b359308a7714c96e5459eb217979a43743847f52d60f10bb5504
---

# Review

The H1 is "Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score". It promises three things: a learning paradigm placed at deployment time, updates selected by an LLM, and selection without a single scalar score.

The body delivers all three:

- **Deployment time:** the routing-line example shows the system adapting across tasks without weight changes. The comparison table places updates at "Deployment time, taking effect on the next task that reads the store", and the body says this marks a lifecycle position, not a speed.
- **Machine learning:** the body positions selection-based learning against direct gradient training. It discusses precedents (Gödel machine, PRODIGY, EURISKO) and why earlier systems did not make it "a general machine learning paradigm", and it answers the Bitter Lesson objection. This supports framing the article as a machine-learning paradigm.
- **LLM-selected, without a single score:** the central argument is that a robust comparison across a preference model can replace one scalar weighting. The bet is that a fixed-weight LLM can build that preference model and make the comparison.

There is no scope drift. The body narrows itself to "one case: a readable store, edited by selected changes". The title's "updates" covers that case without overclaiming weight updates, because the body keeps weights fixed throughout. The evidence and limits sections qualify the claim and do not change it.

The one info finding notes that the title does not mark the claim as a bet. This does not fail the gate, because the title is a topic phrase and does not assert that the capability works.
