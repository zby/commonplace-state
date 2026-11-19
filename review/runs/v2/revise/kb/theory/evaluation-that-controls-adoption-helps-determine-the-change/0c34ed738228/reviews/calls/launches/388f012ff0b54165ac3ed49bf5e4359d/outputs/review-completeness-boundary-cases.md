---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Both cases involve reading results and forming a verdict. Only the first verdict controls the adoption being examined."
    reason: "The note's two roles are judgment that controls adoption (required approval) and assessment of an already-adopted change. A non-binding pre-adoption review falls between them: a maintainer reads the test results before adoption and recommends acceptance or rejection, but approval is not required and the agent may adopt anyway. Under the note's criterion (whether approval was required), this judgment does not control adoption. But it is also not assessment after adoption, and it can still shape which instruction enters use. The Scope bullet about other influence covers only a later evaluator. The note's stated purpose is deciding whose contributions explain an improvement, so this common case (advisory code review, non-blocking comments) falls outside the claimed coverage."
    level: warn
  - scope: passage
    quotes:
      - "The difference is what the judgment controls, not whether a person or a program makes it."
    reason: "Delegated gating is a strained case. Suppose a maintainer writes the acceptance criteria in advance and an automated check applies them to each proposal. The program's judgment controls adoption. The maintainer made no judgment about this change, yet the maintainer fixed what could pass. The framework can map this case if the account names the program's verdict as the controlling judgment and treats the criteria as a separate contribution. The note does not say how a judgment that sets the gate relates to one that applies it."
    level: info
outcome: warn
---

# Review

## Summary

The note sets out a two-way distinction: judgment that controls whether a change enters use, and assessment of a change that is already adopted. It defines control by whether approval was required for adoption. I tested five boundary cases against that criterion.

- **Simplest case: required approval that is granted.** It maps cleanly to control.
- **Post-adoption assessment that triggers a rollback.** The note explicitly treats this as a causal role in a different transition.
- **One evaluator who approves and later assesses.** The section on one episode containing both roles handles this.
- **Advisory pre-adoption review.** This case falls between the two roles. The judgment comes before adoption and can influence it, but it is not required. The note's binary does not cover it, and its scope caveat covers only later evaluators. This is the warning finding.
- **Criteria authored in advance and applied by a program.** This case can be mapped, but only with difficulty.

The taxonomy is short and fits its argumentative role. Adding a third category may not be the right fix. The note could instead say that judgments which are not required but come before adoption fall outside its claim.
