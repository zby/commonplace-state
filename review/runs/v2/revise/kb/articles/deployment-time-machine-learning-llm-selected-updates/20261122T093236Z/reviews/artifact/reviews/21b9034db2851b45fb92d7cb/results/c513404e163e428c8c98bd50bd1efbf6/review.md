---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Its entire software—including its proof searcher and utility representation—is
    readable, modifiable code, and live observations enter proofs on the fly.
  - The machine is not rigid.
  reason: 'The Gödel machine paragraph is the longest of the three precedents, but
    its job in the section is one point: admission by formal proof forfeits every
    improvement that cannot be proved, and a valid proof cannot certify that the axioms
    fit the domain. The opening sentence about the software being fully readable and
    taking live observations, plus the closing four sentences on its ability to rewrite
    its own utility function, are source gloss and a fairness caveat. They each need
    about one clause, not two to four sentences. Compress the paragraph to the admission
    route, its price and a one-clause note that it can still rewrite its utility under
    proof. That keeps the source fair at about half the length.'
  level: warn
- scope: passage
  quotes:
  - Stochastic dominance is a familiar instance.
  - restricting the set to risk-averse utilities orders more pairs
  reason: Stochastic dominance is a second illustration of the agreement rule. The
    Greco–Mousseau–Słowiński account then restates the same rule, and its 'each stated
    preference removes functions from the set, so more pairs become ordered' sentence
    repeats the narrowing point the risk-averse clause has already made. The robust-comparison
    paragraph is the mechanism the bet depends on, so a worked statement earns its
    space. Two parallel statements of the rule and of the narrowing effect do not.
    Cut the stochastic-dominance example to a parenthetical pointer or drop it. The
    'possible' preference definition could go too, since the article never uses it
    again.
  level: warn
- scope: passage
  quotes:
  - scorer saw a failure mode in a quarter of runs that never reached the proposer
  reason: The Harness Evolution paragraph gives the cited study's diagnosis, its null
    remedy run and the lessons-file result in some detail. This is probably more source
    gloss than the rival-hypothesis point needs. However, the conceded null result
    and the lessons-file observation keep the reply to the weights-only reading fair
    and give it force, so compressing it risks making the response look evasive. Consider
    trimming the parenthetical, but this need not change.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/compression-bundle/detail-overhang.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/compression-bundle/detail-overhang.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c513404e163e428c8c98bd50bd1efbf6/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/21b9034db2851b45fb92d7cb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: c513404e163e428c8c98bd50bd1efbf6
completed-at: '2026-11-22T09:36:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/c513404e163e428c8c98bd50bd1efbf6/outputs/review.md
raw-output-sha256: 07717b51e5f4ce07219c502699b1080d2fa3cf1f2a022d3d15ae8e725047bf1e
format: 2
---

# Review

The article mostly keeps its detail in proportion. The routing-line walkthrough is a worked example of a mechanism that the bare definition would leave abstract, and later sections reuse it. The AlphaGo Zero/AlphaZero contrast and the direct-update boundary cases each fix a boundary of the definition in a few sentences. The PRODIGY and EURISKO precedents each stay close to the single-loop/double-loop step they illustrate. The cost ledger and the five-hazard list are concessions that keep the bet credible, and their entries are short.

There are two places to compress in place. Both are in the "Proof, formula, judgment" section, where background on precedents and on the decision-analysis method grows past its job. The Gödel machine paragraph gives more source detail than the proof-gating contrast needs. The robust-comparison explanation states the agreement rule and its narrowing effect twice: once through stochastic dominance and once through the preference-model method. One statement of each would teach the mechanism the bet depends on just as well.

The Harness Evolution paragraph is somewhat long. Its concessions do argumentative work against the weights-only rival, so it is recorded only as information.
