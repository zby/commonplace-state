---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "In the arithmetic regime, the bet is safe: the spec IS the problem, and the solution is algorithmically determined. In the vision-feature regime, the bet is risky: the spec is a theory, and scale may reveal a better path. Most practical codification happens in the blurry zone between them, where you can't tell which regime you're in."
    reason: "This paragraph recaps the two regime bullets in the preceding section (arithmetic: the spec fully captures the subproblem; vision-feature: the spec is a theory of a larger capability), and its closing sentence restates the opening paragraph's claim that you can't reliably tell which regime you're in. Its only new work is recasting the regimes as safe versus risky bets, which the section heading and the next paragraph's 'maximum disadvantage' already convey. Delete it, or fold 'safe/risky bet' into one clause at the start of the vision-researcher paragraph."
    level: warn
  - scope: passage
    quotes:
      - "This is not a partition into codified versus learned: an adopted model package can itself be a codified reference."
    reason: "The note makes the point that adopting a model package can be codification three times: here, in the codification-definition paragraph ('Adopting a model package can codify an operation...') and in the relaxing paragraph ('The replacement can itself be codified by adoption...'). The relaxing-paragraph version does needed work because it says what relaxing reverses. The opening version pre-empts a misreading before codification has been defined, and the definition paragraph rules that misreading out anyway. Cut it from the opening."
    level: warn
  - scope: passage
    quotes:
      - "That scale in fact selects on this property is conjectural, not established."
    reason: "This is defensive redundancy. The previous sentence already presents the diagnosis as what 'one case-level conjecture offers', and 'not established' is entailed by 'conjectural'. If the hedge needs to be explicit, fold 'conjecturally' into the earlier sentence. Otherwise cut this sentence."
    level: warn
  - scope: passage
    quotes:
      - "This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling."
    reason: "This sentence repeats the paragraph's own opening claim that induction bias for calculator-class tasks is 'a permanent advantage, not a temporary one that scale dissolves'. It translates that claim into codification terms, which is mild uptake. The Sources footer annotation makes the same translation a third time. Fold the translation into the opening sentence and drop the closing restatement."
    level: warn
  - scope: passage
    quotes:
      - "Merely writing the convention in natural language constrains without codifying it."
    reason: "This repeats 'Retaining a prose convention alone is not codification.' from the definition paragraph. Heuristic 1 is about leverage versus permanence, and this trailing sentence does no work for that heuristic. It is unclear whether the 'constrains' contrast earns a separate restatement here. If it does, it belongs in the definition paragraph."
    level: info
  - scope: passage
    quotes:
      - "the economic gain still depends on implementation and maintenance costs"
    reason: "The preceding paragraph already conditions the gain on 'its execution and maintenance are cheaper than repeated interpretation'. This clause in the arithmetic bullet re-hedges a condition that has already been stated. It may be meant to stop readers from reading 'safe' as 'free', so it is marked INFO rather than WARN."
    level: info
outcome: warn
---

# Review

The note's main route holds up and earns most of its space:

- the exact-spec/proxy-theory boundary;
- the trade-off that code extraction makes in each regime;
- relaxing as the complement of extraction;
- codification as a bet that spec mining improves;
- the two formal results;
- the working heuristics.

The edge-detection and FlashAttention examples, the spec-mining paragraph and the relaxing-signals paragraph each change what the reader understands or can do.

The redundancy is in restatement layers that agent drafting tends to add:

- **Regime recap.** The "Every code-extraction codification is a bet" section reopens with a paragraph that restates both regime bullets and the opening's "can't tell which regime" claim.
- **Model-package caveat.** The point that a model package can be codification appears three times. Only the version in the relaxing paragraph has a distinct job.
- **Hedge and summary sentences.**
  - "Conjectural, not established" re-hedges a sentence that already calls its claim a conjecture.
  - The last sentence of the Ebrahimi paragraph repeats that paragraph's first claim.

Two smaller repetitions are marked INFO because they may guard against a likely misreading:

- the prose-convention caveat in heuristic 1;
- the maintenance-cost clause in the arithmetic bullet.

The closing line of the trade-off section ("The bitter lesson describes a trajectory, not a law of nature") passes. It turns the bidirectional examples into a stance the reader should remember.
