---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A bounded, recoverable downside on one side; a silent, unbounded one on the other
    — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky.
    An unenforced copy is always one missed edit away from the catastrophic state,
    with nothing watching.
  reason: This closing paragraph restates the asymmetry the preceding paragraph already
    set out (one bounded recomputation vs. silent, unbounded wrongness, already announced
    as 'the rule rides entirely on that'). Its one new job is the 'forbidden rather
    than merely risky' stance. Fold that phrase into the end of the previous paragraph
    and drop the recap and the 'one missed edit away' sentence.
  level: warn
- scope: passage
  quotes:
  - Machine-followable suffices; human visibility is not required once the validator
    carries the interrupt.
  reason: This repeats the earlier statement that the validator is the edit-time surface
    and 'lineage only needs to sit where a machine can follow it, not where a human
    will see it.' The precondition is fully stated by its first two sentences. Keep
    the point in only one place.
  level: warn
- scope: passage
  quotes:
  - A checkable claim is enforced as a check or not asserted at all.
  reason: The bullet's closing sentence restates its own opening imperative ('Never
    write the unenforced natural-language version of a checkable claim') and adds
    nothing to it. Cut it.
  level: warn
- scope: passage
  quotes:
  - applied not only to caches but to every derived copy of recomputable truth
  reason: 'Defensive redundancy: calling the rule ''the general form'' of the cache
    maxim already means it reaches beyond caches. The trailing clause restates that.
    Cut it, or merge the maxim into the opening or the asymmetry section, where it
    would frame the rule instead of sitting alone after the instances.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/bed2718fc50eb4dbf365f39f/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/bed2718fc50eb4dbf365f39f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 88cbb10750904127ac9d62fab0efdb32
completed-at: '2026-11-16T22:20:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/88cbb10750904127ac9d62fab0efdb32/outputs/review.md
raw-output-sha256: c97b112d2e40e9f6ab68f29530a44df0ec40e47617bcd78fcf7966fe3c5bc000
format: 2
---

# Review

The note's main structure earns its space. The opening rule, the regime boundary (managed staleness vs. Level A enforcement), the third class from enforcement, the four preconditions and the four instances each do separate work. The instances section is not a recap. It maps the instances onto distinct application states and supports the claim that the rule generalizes.

The redundancy is local. Two closing restatements repeat the openings of their own units: the asymmetry section's second paragraph and the "never write" bullet. One point appears twice, in two sections: lineage needs only to be machine-followable. The final cache-maxim line ends with a clause that its own "general form" phrase already entails. Each fix is a cut or a fold of a few words. None removes an argument step.

Non-obvious passes. The "Checked copies degrade gracefully" bullet echoes the asymmetry but adds the lifecycle-exit consequence, so it passes. The amortization remark in instance 1 applies precondition 4 to a concrete case instead of restating it, so it also passes.
