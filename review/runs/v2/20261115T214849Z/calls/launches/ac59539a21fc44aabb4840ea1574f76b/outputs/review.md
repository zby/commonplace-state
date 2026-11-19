---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["that is why hand-maintained-and-trusted is *forbidden* rather than merely risky"]
    reason: "UNSUPPORTED — The asymmetry shows only that a false copy's worst case is worse than an absent copy's cost. Moving from 'can cause silent, unbounded wrongness' to 'forbidden' needs an expected-cost comparison: how often hand-maintained copies actually drift, and what building and running a validator costs. The note gives neither. It also calls the absent-copy cost 'one bounded recomputation', yet it later says omission pays a real hot-path or build-time cost, and its linked grounds say recomputation is dear to a model. So 'bounded' does not mean small, and the asymmetry alone does not license a categorical ban."
  - scope: passage
    quotes: ["natural-language summaries and judgments do not — there is no comparison a machine can run, so they stay as live reads or are omitted"]
    reason: "UNSUPPORTED — This passage concludes that copies failing the derivation-rule precondition must be live reads or omitted. But the regime section says that, outside the deterministic end, a hand-maintained dependent artifact 'is not forbidden; it is unavoidable' and falls under managed staleness. A natural-language summary of a source is that kind of dependent artifact. The note does not establish why failing precondition 1 sends a summary to omission rather than to managed staleness. As written, it extends the ban beyond the recomputable scope the claim declares."
  - scope: passage
    quotes: ["Enforce-or-omit stops being aspirational and becomes the rule, since trusting an unchecked copy now saves nothing"]
    reason: "THIN — The reason given is that Level A checks are near-zero cost to run. 'Saves nothing' also needs the validator to already exist, or to be cheap to write and wire in. The note's own instances contradict this: one surface is 'not yet applied', and an open question asks for 'the cheapest general mechanism' for checkable regions. Trusting an unchecked copy therefore saves the authoring cost of the validator. The joint conflates the cost of running a check with the cost of building one."
  - scope: passage
    quotes: ["a validator is centralized, versioned, reviewed on every change, and amortized across every copy it protects, so its unit cost of correctness-assurance is far lower than N independently hand-maintained instances would be"]
    reason: "THIN — Amortization lowers the per-copy cost of trusting the validator. It does not establish that the validator is correct, and 'reviewed on every change' is asserted rather than shown. A validator that wrongly passes gives exactly the silent, trusted-false signal the rule exists to prevent, and it does so for every copy it covers. For a single-pair case such as the two template copies, nothing is amortized. The regress is made cheaper, but the note does not show that it bottoms out."
  - scope: passage
    quotes: ["The spread is what shows it generalizes"]
    reason: "THIN — The four surfaces sit in one system and show that the rule can be applied in different states. They do not show that it generalizes. Only two of the four are actually enforced, and the third ('would dominate') is a counterfactual. None tests the 'forbidden' strength of the claim. Showing that the rule can be applied in several places does not show that it holds or transfers."
outcome: report
---

# Friction check: A derived copy of recomputable truth must be checked or absent

**Central claim (one sentence):** A copy of information that can be recomputed mechanically from a ground-truth source must either be re-derived and compared by a validator or not exist; a hand-maintained copy that consumers trust is forbidden.

## Filter
**Filter:** SURVIVES

The claim wants three properties at once: correctness (no silently stale copy), the economy of a frontloaded copy, and no trust in hand-maintained artifacts. These can coexist because the checked branch keeps both the copy and its correctness. The validator is itself a hand-authored artifact that consumers trust, which strains the third property. The note sees this regress and scopes it in precondition 4, so the claim still concretizes to one consistent commitment. The strain shows up below as a thin joint, not as a contradiction.

## Thinnest joints

The two weakest joints carry the claim's normative strength and its scope. The step from the failure asymmetry to "forbidden" lacks the frequency and enforcement-cost terms a categorical ban needs. Precondition 1 sends non-mechanical summaries to omission, which conflicts with the note's own statement that judgment-dependent artifacts are legitimately hand-maintained under managed staleness. Next is "saves nothing", which treats running a check and authoring a validator as the same cost; this bears directly on the "forbidden" strength. The validator-regress argument is weaker than it reads because amortization is about cost, not correctness. The generalization claim rests on in-system examples that show the rule can be applied, not that it holds. Other joints mostly hold: checked copies degrading gracefully, and omission as the fallback.

## For the human
Look first at the "forbidden rather than merely risky" step. Decide whether the ban is meant as categorical or as a cost-weighted default, then fix precondition 1's treatment of summaries to match the managed-staleness scope.
