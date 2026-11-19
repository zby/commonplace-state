---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: e7330664386a4e51978e1708e32e6969
completed-at: '2026-11-18T16:03:33Z'
findings:
- scope: passage
  quotes:
  - argues for results computed before an LLM call, extended here to persisted artifacts
  reason: 'The link text ''frontloading spares execution context'' is a full clause,
    and it serves as the subject of a reduced relative clause: ''the saving [frontloading
    spares execution context] argues for results computed before an LLM call''. On
    a first pass, ''argues for results'' reads as the frontloading note advocating
    results computed before a call. ''The saving'' is then left without a role. The
    intended reading is ''the saving that [the note] argues for, in the case of results
    computed before an LLM call''. Splitting the sentence removes the garden path,
    for example: ''The frontloading note argues for this saving for results computed
    before an LLM call; this note extends it to persisted artifacts.'''
  level: warn
- scope: passage
  quotes:
  - A check that fully recomputes the result on every use largely defeats it
  reason: The intended antecedent of 'it' is 'that saving' in the previous sentence.
    Within this sentence, 'the result' and 'use' are nearer nouns. Context resolves
    the reference quickly, but replacing 'it' with 'the saving' would remove the pause.
  level: info
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/25bbefcd90faedea5e5f417a/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/25bbefcd90faedea5e5f417a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/e7330664386a4e51978e1708e32e6969/outputs/review-parsing-ambiguity.md
raw-output-sha256: 1879399f92e68c3d12b4b03b36b2f6d761c99b4e63db91a2e9109ab8d43a92d6
---

# Review

## Summary

The first paragraph contains one plausible misparse. A link whose text is a whole clause becomes the subject of an unmarked relative clause, and the verb "argues for" then attaches to "results" instead of to "the saving". One pronoun in the same paragraph is also recorded as INFO.

The other sentences parse cleanly. In particular, "a claim that authorizes stopping" attaches to the nearest noun as intended. The negation in "not as state already in the KB" and in "not free or current" has clear scope.
