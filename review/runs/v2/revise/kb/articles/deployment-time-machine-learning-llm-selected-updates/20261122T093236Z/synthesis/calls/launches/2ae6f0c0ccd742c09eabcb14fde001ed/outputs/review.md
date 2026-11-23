---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["The process itself is not new", "The loop itself is not new."]
    reason: "The introduction states the bet twice, in two different forms. Between the comparison claim and the bolded bet it stacks a scope restriction, a novelty disclaimer, the PRODIGY precedent and a reinforcement-learning analogy, then repeats the disclaimer inside the bet. The fuller form of the bet (deciding the open cases, double-loop, declared objective fixed) appears only after the precedents, so a reader leaves the opening with the hedges as vivid as the claim and must reconcile the two statements later. A revision could cut the precedent, analogy and duplicate disclaimer from the opening, because later sections carry them, put the comparison claim directly before the bet, and state the bet once in its full form so the later passage refers back to it rather than restating it."
  - scope: document
    quotes: []
    reason: "In 'Proof, formula, judgment', the robust-comparison material from the 'Robust comparison' paragraph to the consistency paragraph states the agreement rule twice (stochastic dominance, then the preference-model method) and its narrowing effect twice. It then spends three consecutive paragraphs on overlapping points: the judge compares a pair and may leave it open, reversibility lets the system act on an open comparison, and such action is a decision, not a demonstrated improvement. This is the mechanism the bet depends on, so the repetition dilutes the central explanation. A revision could teach the mechanism once (one statement of the rule, its narrowing, its stated limit for open-ended work, and its application to a change), then give one paragraph on what the model must do instead of computing value functions. That paragraph would absorb the two sentences of new content in the recap paragraph."
outcome: report
---

# Simplification synthesis: Deployment-Time Machine Learning

## Opportunities

### 1. Lead the opening with one full statement of the bet

- Location: introduction, from "The case argued here is the one where the changes are edits to the system's own readable, addressable store" through "The loop itself is not new."; and the restatement in "Proof, formula, judgment" beginning "We bet that a fixed-weight language model can do that work autonomously".
- Combines: core-claim-obscured (all three findings: opening clutter, duplicated disclaimer, two forms of the bet); marginal-value-redundancy ("The loop itself is not new.").
- Preserve or decide: The author must decide which form of the bet the article commits to up front. The later form adds deciding the cases the comparison leaves open and the double-loop label, with the declared objective held fixed. These are substantive scope choices, not wording. Moving them to the opening changes what the article promises. Leaving them in the precedents section means the opening should explicitly point forward. The author must also decide whether an ML-research audience needs the "not new" positioning in the opening, or whether the precedents section can carry it alone. One disclaimer should survive somewhere, because the article's claim is the bet, not the loop. The readable-store scope restriction must stay visible early, because the table and the Bitter Lesson argument depend on it.

### 2. Teach the robust-comparison mechanism once

- Location: "Proof, formula, judgment", from "**Robust comparison.**" through "such cycles are something a test can look for."
- Combines: detail-overhang (stochastic dominance and Greco et al. as parallel statements; the unused "possible" preference); marginal-value-redundancy (the "procedure need not assign every version a number" paragraph recapping the introduction, the reversibility sentence and the success section).
- Preserve or decide: Preserve the distinctions that do argumentative work: the improvement relation is stricter than the method's "at least as good"; in open-ended work an objection can add a criterion and widen the set, which can overturn an earlier verdict; a better alternative (trial with a cheap way back) can close an otherwise open comparison; consistent answers can still neglect a required cost; and preference cycles are a testable failure. Decide whether stochastic dominance stays as the familiar anchor for ML readers or is dropped in favour of the decision-analysis framing, and whether "possible" preference is needed at all. Decide which section owns "a decision, not a demonstrated improvement". It currently appears here and again in the success section, and one occurrence can refer to the other.

Not raised: the Gödel machine paragraph (detail-overhang WARN, marginal-value-redundancy WARN) and the Harness Evolution passage (branch-bloat INFO, detail-overhang INFO) are local compressions. They do not change how a reader grasps the central claim. The Gödel compression should keep the point that the machine can rewrite its utility under proof, because the single-loop/double-loop progression is read against it.
