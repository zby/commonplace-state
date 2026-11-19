# Assessment: A better-factory claim compares operative states under an antecedent assessment relation

**Proposed purpose (operator named none):** A KB maintainer or agent who must state or audit whether a revised factory got better. After reading, they should be able to name the four declarations that make such a claim determinate and check whether each was fixed before the development rather than read off the record.

**Decision: stop. No passes are planned.** The highest-value changes are to claims, not to text. Passes cannot change claims. Several claims are wrong, or are unsupported as written, and fixing them will restructure the argument. Text that a rewrite will replace is not worth a pass.

## Claims that are wrong or unsupported (rewrite route)

1. **Scope bullet 5:** "A real episode can be described either way, and the description determines where the evaluator sits." The premise-decomposition report rates this DEFEATED. The internal-consistency and framing-mismatch findings flag the same sentence. It contradicts the body's causal account: "falls on opposite sides depending on whether it gated the successor". A human gate cannot be moved off the causal path by describing the episode differently. This is the sentence a hostile reviewer would attack first. It reopens the post-hoc freedom the note exists to close.
2. **"Passing the comparison establishes improvement between the two states."** The critique (attack partially lands) shows this is false unless the comparison is matched. The two states are measured at different times, so environmental drift and the successor's own effect on later work confound the result. The note applies the contrast principle only to attribution, not to the improvement comparison itself.
3. **Unstated requirement for the predecessor side.** In the measurement route, the predecessor is superseded and usually cannot be re-run. Antecedence as stated fixes the dimensions and thresholds. It does not fix the predecessor's baseline, the measurement instances or the procedure. So "Fixing the dimensions and thresholds in advance is what makes the comparison capable of failing" is unsupported as stated (premise decomposition; critique).
4. **"exceed a specified target"** leaves its baseline unstated (underspecified-assertions, warn). If the target is absolute, a successor identical to the predecessor can pass a "better-factory" comparison. The choice determines when the central claim is true.
5. **The preserved path "falls out of scope indexing".** The premise decomposition rates this DOUBTFUL and the friction check rates it THIN. It follows only if the declared thresholds include factory development as a checked dimension. That is an added condition, not a consequence. The synthesis also asks the author to decide whether this section belongs to the contribution or should be rehomed.
6. **"Antecedence here is the pairwise-comparison form of the condition…"** Grounding alignment and concept attribution both flag this. The linked note's antecedence is an identifiability condition that needs no declaration. This note's condition is stronger: prior declaration in time. Claiming the two are identical misstates the linked note, so the sentence must be reworded as a strengthening.
7. **"either unmeetable or vacuous"** (friction check, the thinnest joint). The dichotomy is asserted without argument, yet it is the only justification given for scope indexing.

Rewrite route: `commonplace-review run rewrite kb/theory/a-better-factory-claim-compares-operative-states.md --commission FILE`, with the commission prepared using `cp-skill-write-multistage`.

## Depth 1 proposals that change what the artifact is

- The critique (`kb/reports/state/review/results/kb/theory/a-better-factory-claim-compares-operative-states.md/kb/instructions/critique-note.md`) proposes conditioning the central improvement claim on a matched comparison. It also proposes adding a predecessor-baseline requirement to what antecedence fixes. Both change the claims.
- The premise decomposition (`…/kb/instructions/premise-decomposition-gate.md`) proposes a declared scope proxy as a condition of the "determinate" thesis. It also proposes extending antecedence to the measurement procedure and instance set, and removing or qualifying Scope bullet 5.
- The synthesis (run dir `kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/synthesis`) proposes restructuring the note around the four declarations. It may also rehome the preserved-path section and the compounding contrast, which is a split. It leaves the title's scope to the author.

## Terms that dependents rely on

The role report (run dir `kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/role`) names two dependents:

- `kb/theory/factory-learning-is-experience-responsive-retention-that-improves.md` links with the text "antecedent better-factory comparison".
- `kb/tags/software-factory-README.md` cites the note for what an improvement claim compares and for the relation being fixed in advance.

Two possible changes reach those dependents:

- **The artifact's own TODO:** "remove or update to use software house instead of software factory".
- **The load-bearing-qualifiers finding** that "factory" is not load-bearing in the title.

Either change renames the compared object, and with it the title. The operator must decide the term together with the dependents' link text and tag membership. A pass must not make this change.

The rewrite should keep what the dependents rely on: the separation from retention, operative states as relata, and the antecedent relation. The finer structure reaches no dependent.

## Divergence items (must keep)

These sentences are divergence, not support. A later rewrite or pass may sharpen them but must not drop them:

- A better-factory claim is a separate claim from retention, because retention has no quality requirement.
- The relata are the predecessor and the operative successor. A discarded candidate never enters the comparison.
- The assessment relation is declared before the development it judges.
- Evaluator location is a separate declaration from the learner boundary.
- Passing the comparison does not establish that the factory learned. The experience link is established only by manipulating it.

The candidate overclaim "Passing the comparison establishes improvement between the two states" is support and may be narrowed, as the critique asks.

## Stale qualifications (claim questions for the operator)

- **Scope bullet 6.** It holds back the fourth part, evaluator location, but its stated reason (the preserved path) comes from the second part, scope indexing. The reason does not match the part it withholds.
- **Scope bullet 5.** It contradicts the body, as described above.
- **The "Neither claim entails the other" heading.** The section covers two different pairs of claims.
- **The `TODO!` line.** It sits in the body of a settled note.

## Ranked text-level changes deferred until after the rewrite

These apply only to text expected to survive, so none is planned now:

1. The relation-relative caveat is stated four or five times; state it once. Cost: a few cuts. Pass: readability-and-flow (detail-overhang, marginal-value-redundancy).
2. The opening lists the claim's parts and the next paragraph lists them again. The title names only two of the four declarations. Cost: retitle and rework the opening. Pass: opening-and-title (title-body-alignment).
3. Several imported terms are unglossed: software factory, learner boundary at first use, open production family, factory development, redesign class. Cost: short inline glosses. Pass: fix-strategy-taxonomy (undefined-terms) or readability-and-flow.
4. Four long sentences need splitting. Cost: sentence splits. Pass: readability-and-flow (clause-packing).
5. Two phrasings: "goes soft" and the "not an extra virtue bolted onto" elevation sentence. Cost: one swap and one deletion. Pass: plain-wording (mannered-prose, stock-phrases).
6. "This is also why the oracle problem…" overstates its link to the preceding point (framing-mismatch, branch-bloat). Cost: trim the paragraph. Pass: readability-and-flow.

## Findings not acted on, with reasons

All 14 findings are deferred to the rewrite. Findings 7, 8, 9, 10 and 12, and the evaluator and factory-scope items in 13, are claim-level and belong to the rewrite. Findings 1–6, 11 and 14, and the oracle item in 13, would edit text the rewrite will replace.

## What reads well

The candidate/operative-successor distinction and the two routes to a successor are clear, well defined and correctly grounded in the operative-change note.
