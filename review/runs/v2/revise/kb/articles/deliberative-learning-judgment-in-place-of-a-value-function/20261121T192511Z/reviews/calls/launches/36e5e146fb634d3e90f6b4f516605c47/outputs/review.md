---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "weights-only continual learning wins those domains"
    reason: "The falsification sentence claims more than its evidence supports. If automated language-model judgment fails to keep its hazards below its gains, the bet fails. That does not show that weights-only continual learning wins: human-judged deliberative learning, hybrids or other methods remain possible. The contract asks for each claim at the scope its evidence supports. Stop at 'the bet fails', or name weights-only continual learning as the main rival rather than the winner."
    level: warn
  - scope: passage
    quotes:
      - "its scorer saw a failure mode in a quarter of runs that never reached the proposer"
    reason: "This parenthetical carries the article's counter-reading of the Harness Evolution study, but its attachment is ambiguous. 'that never reached the proposer' can modify 'runs' or 'a failure mode'. A reader with no KB context cannot tell whether the runs or the scorer's observation failed to reach the proposer. State it literally, for example: 'in a quarter of runs, the scorer detected a failure mode that was never passed to the proposer'."
    level: warn
  - scope: passage
    quotes:
      - "The initial human scaffolding must serve as a launchpad that computation comes to supply and revise, not a permanent ceiling of hand-crafted rules."
    reason: "This sentence restates the previous sentence's condition through the launchpad and ceiling metaphors. It adds no new mechanism. It also strains the metaphor, because computation does not 'supply' a launchpad. The Review section requires replacing a metaphor when plainer language would lose nothing. Either delete it or state the literal criterion: automated proposals and judgments must come to produce and revise the instructions, types and gates that people first wrote."
    level: warn
  - scope: passage
    quotes:
      - "An unknown is worth investigating only if a plausible answer could reverse the choice."
    reason: "This decision rule appears without a link to the surrounding argument. That argument defines on-balance improvement and then explains acting under an open verdict. The article neither applies the rule to the routing-line example nor uses it later, so a reader cannot see what it supports. Either connect it, for example to show why the judge in the example did not investigate the context-load cost further, or leave it to the linked theory note."
    level: info
  - scope: passage
    quotes:
      - "A single validator or utility formula weighs nothing"
    reason: "The aside between the dashes, about how well the word 'deliberative' fits, separates 'weighs nothing' from its contrast 'yet it still separates proposing from judging'. It also concerns naming, not the mechanism. The Review section prefers moving such an interruption. Put the naming remark after the main point, or into its own sentence."
    level: info
  - scope: passage
    quotes:
      - "Treating the paradigm as already validated would invert the order of proof."
    reason: "This repeats the previous sentence's limit (no completed end-to-end automated run) by negating a broader claim. The contract asks for each material qualification to be stated once. Consider deleting it."
    level: info
outcome: warn
---

# Review

## Summary

The article conforms to the `kb/articles/` contract overall. It is placed at the collection root as a draft. It opens with a draft banner that makes no stability promise and says where to send comments. The title is a reader-facing headline, and the description is a retrieval filter. The body has no footer link tables or graph-traversal glosses. Links go to theory, sources, companion articles and external primary sources, are woven into prose, and end with a welcome "Where to go next" section. No link goes into `kb/work/` or into report state.

The central Review tests are largely met. A reader with no KB context can state the article's two-level claim, its support (the PRODIGY, EURISKO and Gödel-machine precedents, plus the Bitter Lesson argument) and its limits (no completed automated run, and four named hazards). The routing-line example comes before the abstraction, the prose says explicitly what it establishes ("That sequence establishes three things"), and later sections return to it for open verdicts and reversibility. Costs and the current evidence state are given plainly, beside the claims they limit.

The warnings are local. One falsification sentence claims more than the article's evidence supports. One parenthetical about the external study has an ambiguous attachment at the point where the article's counter-reading depends on it. One metaphorical sentence restates the bootstrap condition without adding content. The info findings name a decision rule with no link to the argument, an aside that interrupts a sentence's contrast, and one repeated qualification. None of these is systematic, so the outcome is WARN rather than FAIL.
