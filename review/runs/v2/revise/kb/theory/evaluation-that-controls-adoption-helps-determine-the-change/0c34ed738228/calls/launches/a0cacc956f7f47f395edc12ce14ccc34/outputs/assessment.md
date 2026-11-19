# Assessment: Evaluation that controls adoption helps determine the change

**Proposed purpose (no operator purpose was named):** A KB maintainer or agent attributing a system's improvement should be able to tell which evaluator judgments count as contributions to selecting a revision and which only assess a revision already in use.

## Decision: stop before any pass

The highest-value change is not a text pass. It is a change to the central claim's support. Three depth 1 reports independently find the same weak step:

- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/critique-note.md`: "partially lands". The note moves from formal position (approval was required) to causal contribution (approval "helps select"). A required approval that would pass any candidate selects nothing. The critique proposes either making the claim conditional on the judgment being sensitive to candidates, or restating it as a claim about adoption authority. It also proposes that the examined transition be fixed in the declared comparison, because under a boundary-defined successor (which the parent better-factory note allows) a post-adoption assessment with rollback authority counts as selection.
- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/premise-decomposition-gate.md`: the gate premise is DOUBTFUL (rubber-stamp counterexample). "Required" is a determinate process fact only when it is read counterfactually, not as the stated rule. An unstated premise puts selection only in per-change judgments and misses the authors of standing adoption rules, whom the note's own second case relies on.
- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/composition-friction-gate.md`: rates the requirement-to-selection step UNSUPPORTED, and the bridge from selection to explaining an improvement THIN.

The depth 2 finding `semantic/underspecified-assertions` finds the same ambiguity in "helps determine" (structural versus counterfactual reading), and `semantic/completeness-boundary-cases` adds advisory pre-adoption review as an uncovered case.

These proposals change what the note claims. The passes cannot make that change: they do not change claims. Any of the three repairs (add a counterfactual condition, restate the claim as one about adoption authority, or add standing adoption rules as a third form of control) would rewrite the opening, the first case, the "one episode" section and the Scope. The text passes would edit has not been settled.

**Claim at issue:** "A human approval required for adoption is part of the process that selected the revision." The same step recurs in "Whether approval was required for that adoption is a fact about the process. A different description cannot turn required approval into assessment after adoption."

**Route:** `commonplace-review run rewrite kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md --commission FILE`, with the commission prepared with `cp-skill-write-multistage`. The operator first decides which repair to adopt.

**Dependents:** The role report (`kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/role`) finds one dependent, `kb/theory/README.md`. It cites the title and a one-line gloss calling the note a supplement to the better-factory comparison that separates selection from later assessment. No dependent uses the note's other claims or terms. A rewrite that changes the title, as the claim-strength finding also recommends, or that changes the supplement framing must update that index entry. The note declares itself a supplement to `kb/theory/a-better-factory-claim-compares-operative-states.md`. The critique's transition point depends on that note's boundary-defined successor, so the rewrite should be checked against it.

## Ranked changes (for the rewrite, not run as passes)

1. **State when a gate counts as selection.** Add a condition that the verdict could have gone otherwise, or that the proposer selected in anticipation of it. Otherwise, name the claim as adoption authority. Cost: a claim change across the opening, the first case and the "one episode" section. Route: rewrite. Pass: none.
2. **Fix the examined transition in the declared comparison.** Say that the comparison fixes in advance whether the examined transition is entry into use or the operative state at a measurement boundary. Under the boundary reading, rollback authority counts as selection. Cost: one paragraph, plus the "different transition" sentences. Route: rewrite. Pass: none.
3. **Name the authors of standing adoption rules, and advisory pre-adoption review, as cases.** Either classify them or exclude them in Scope. Cost: one or two Scope bullets. Route: rewrite.
4. **Sharpen the title** (`frontmatter/claim-strength`). The title nearly restates its premise. Cost: title plus the index entry in `kb/theory/README.md`. Route: rewrite, since the new title depends on how item 1 is decided.
5. **Trim the Scope** (synthesis opportunity 1; `branch-bloat`, `marginal-value-redundancy`, `compound-bullet`). Cut the first bullet, which restates the rollback boundary. End the third bullet after the harmful-revision example. Either tie the test-optimization sentence to the distinction or rehome it. Cost: about three sentences. This would be `readability-and-flow` or `fix-strategy-taxonomy`, but the Scope will be rewritten under items 1–3, so it is deferred.
6. **Define adoption before the cases rely on it, and drop the human-specific restatement** (synthesis opportunity 2). Cost: move one sentence and cut two. Pass would be `readability-and-flow`. Deferred for the same reason.
7. **Gloss "the learner" and "declared system boundary"** (`accessibility/undefined-terms`). Cost: one inline phrase. Pass would be `fix-strategy-taxonomy`. Deferred: the Scope bullet that holds these terms may change.
8. **Remove the noun/verb ambiguity of "which system results"** (`sentence/parsing-ambiguity`). Cost: two words. Pass would be `plain-wording` or `fix-strategy-taxonomy`. Deferred: the opening sentence is the claim under rewrite.

**Sentence a hostile reviewer would attack first:** "A human approval required for adoption is part of the process that selected the revision." A rubber-stamp approval is required and selects nothing.

**What reads well:** The two hypothetical cases, "Approval before adoption" and "Assessment after adoption", make the contrast concrete in parallel form. The rewrite should keep them as the spine.

## Candidate overclaims: support or divergence

- "The difference is what the judgment controls, not whether a person or a program makes it." Divergence: this is the note's position, and the premise decomposition finds that it HOLDS. Keep.
- "An evaluator who only assesses an already-adopted change does not, through that assessment alone, determine its adoption." Divergence: the premise decomposition finds that it HOLDS. Keep.
- "A favorable assessment of a proposal that is never adopted does not establish an improvement of the deployed system." Divergence: the friction check and premise decomposition find that it HOLDS. Keep.
- "A human approval required for adoption is part of the process that selected the revision." / "A different description cannot turn required approval into assessment after adoption." Disputed. This is the stop, and it is not a must-keep item: the operator decides the repair.
- "An externally supplied selection judgment must still be acknowledged as a contribution." Disputed by inheritance, because it rests on the requirement-to-control step. It is left to the rewrite.
- "A test available to the proposing system can be optimized without improving the capability it is meant to assess; human approval does not remove the need to justify the assessment." Support, and a separate mechanism. It may be cut or rehomed.

## Stale qualifications (claim questions for the operator)

- The first Scope bullet ("does not establish that a later evaluator had no other influence") qualifies only a later evaluator. The anticipation path and advisory pre-adoption review are neither named nor excluded.
- The open question asks how to report externally supplied adoption judgments. The second Scope bullet already asserts that they "must still be acknowledged as a contribution", so the open part is narrower than stated: how to report the judgment, not whether to report it (critique, secondary objection).
- The supplement line calls the parent note "the better-factory comparison" without saying what it compares (`accessibility/undefined-terms`, info). The role report notes that the parent note does not link back.

## Findings not acted on

All eight warn findings are deferred by the stop and handed to the rewrite:

- `accessibility/undefined-terms`: deferred; the Scope bullet that holds the terms may change.
- `frontmatter/claim-strength`: deferred; the title depends on the claim repair.
- `compression-bundle/branch-bloat`: deferred; the Scope is rewritten.
- `compression-bundle/marginal-value-redundancy`: deferred; the Scope and opening are rewritten.
- `semantic/completeness-boundary-cases`: belongs to the claim repair (item 3), not a pass.
- `semantic/underspecified-assertions`: belongs to the claim repair (item 1), not a pass.
- `sentence/parsing-ambiguity`: deferred; the opening sentence is rewritten.
- `structural/compound-bullet`: deferred; the bullet is rewritten or cut.
