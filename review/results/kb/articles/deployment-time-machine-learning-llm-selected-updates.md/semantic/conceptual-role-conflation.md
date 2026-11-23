---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:21Z'
findings:
- scope: passage
  quotes:
  - Often the stated purpose permits several ways to weigh the gains and losses.
  reason: The opening attributes the name 'preference model' to decision analysis
    and applies it to the set of weightings a stated purpose permits. In the source
    account, the preference model is the set of value functions compatible with preferences
    a person has stated, over fixed criteria. Two role assignments are possible. In
    one, the article inherits the source concept. In the other, it applies the source
    term to its own purpose-derived extension. The later 'analogy has a limit' paragraph
    and 'In the decision-analysis method, a person states the preferences' settle
    the relation, so the blur is not material in context. It is distant from the opening,
    however.
  level: info
- scope: passage
  quotes:
  - our agent-operated knowledge-base framework, does all three today only with people
    inside the system
  reason: 'The ladder classifies a bounded system. The passage applies it to Commonplace
    glossed as a framework, which is an artifact and not the deployed system that
    changes and selects. The intended object is recoverable from context: a deployment
    of the framework together with its operators. The blur therefore does not change
    attribution or scope materially.'
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/e75f9222eba346a0941a9be4/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 17861dda67ecb5f7111aaee1a1e7681f12dddb237eaf927551cd633d89766338
---

# Review

## Summary

I checked the passages that import, extend or apply concepts. These are selection-based learning, preference model, necessary and possible preference, robust comparison, single-loop and double-loop, self-improving system, production method versus representational form, and operative change. They generally keep the roles apart. The note says what the KB's definition requires and what it leaves open. It separates the term from the process, and attributes necessary and possible preference to Greco et al. It states where its robust comparison departs from that method: strict rather than weak, criteria open rather than fixed, and purpose rather than a person supplying the constraints. It also attributes the folk reading of the Bitter Lesson to readers rather than to Sutton.

The two remaining blurs are settled by nearby or later context and do not clear the materiality threshold.
