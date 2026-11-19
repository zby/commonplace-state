---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 64ed06d4308d4add9543b3330fcc273b
completed-at: '2026-11-16T22:21:37Z'
findings:
- scope: passage
  quotes:
  - so its unit cost of correctness-assurance is far lower than N independently hand-maintained
    instances would be
  reason: 'UNSUPPORTED — the regress worry is about whether the validator''s re-derivation
    is correct, but the stated reason answers only cost per copy. Amortization also
    correlates failure: one validator bug passes every protected copy at once, under
    a stronger trust signal than a hand-maintained copy carries. ''Reviewed on every
    change'' is asserted, not shown, and nothing explains why being centralized and
    versioned would not equally rescue a hand-maintained copy. The claim that the
    validator ''bottoms out'' needs a reason why a wrong validator fails loudly, and
    the note gives none.'
- scope: passage
  quotes:
  - It is the general form of "a cache must never be the only copy"
  reason: 'UNSUPPORTED — that maxim protects against losing the source: keep ground
    truth so the cache can be rebuilt. This note''s rule assumes the source survives
    and governs whether a stale copy may be trusted. Generalizing the maxim would
    give ''keep the source'', not ''check the copy or delete it''. The analogy is
    asserted without showing that the two rules share a mechanism.'
- scope: passage
  quotes:
  - that is why hand-maintained-and-trusted is *forbidden* rather than merely risky
  reason: THIN — the asymmetry shows that a false copy can be worse than an absent
    one. It does not show that the expected cost is worse. Getting to 'forbidden'
    would need staleness rates and the cost of recomputation, and the note's own linked
    claim that recompute is dear to a model makes the absent side's cost non-trivial.
    'Unbounded' is asserted ('can cause'), not established. In this section, asymmetry
    alone carries the categorical conclusion. The stronger ground, that checking is
    nearly free, arrives only in the next section.
- scope: passage
  quotes:
  - since trusting an unchecked copy now saves nothing
  reason: THIN — Level A makes each validation run nearly free, but the copy still
    has to have its validator written and its region marked (preconditions 2 and 4).
    Skipping that authorship is what an unchecked copy saves. The joint treats run
    cost as total cost, so the step from 'checks are cheap' to 'enforce-or-omit becomes
    the rule' is under-argued. The same gap underlies the claim that enforcement 'would
    dominate' for hot-path skills.
- scope: passage
  quotes:
  - The spread is what shows it generalizes
  reason: THIN — all four instances come from one system. Only the tag-README mark
    and the template duplication actually test checked-or-absent. The hot-path case
    is a conjecture that enforcement would dominate. The compiled-memory instance
    comes from a note that asks for provenance, regeneration and staleness detection,
    which sits nearer the managed-staleness regime than the enforce-or-omit rule.
    A spread of application states shows that the rule can be applied, not that its
    prohibition is correct.
contract: report
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/70bcc56fb2cb8f30220c1d61/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/70bcc56fb2cb8f30220c1d61/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/64ed06d4308d4add9543b3330fcc273b/outputs/review.md
raw-output-sha256: eae6130e791acd6d66f10dde52cfb494b693379d2dab36366339c517cff0406a
---

# Friction check: A derived copy of recomputable truth must be checked or absent

**Central claim (one sentence):** A copy of information that can be mechanically recomputed from a ground-truth source must either be re-derived and compared against that source by a validator, or not exist; a hand-maintained copy that consumers trust is forbidden.

## Filter
**Filter:** SURVIVES

The note wants three things at once: frontloaded copies for context economy, correct copies, and no reliance on hand maintenance. A deterministic validator lets all three hold together. The note avoids the apparent clash with its managed-staleness neighbour by limiting the rule to cases where the check is Level A. In judgment-checked regimes it explicitly allows hand-maintained dependents. The one place where concretization strains is precondition 4. A validator is itself a hand-maintained, trusted artifact, so the prohibition holds only if validators are a different kind of thing. The note asserts that difference rather than deriving it. That is a thin joint, not a dissolution.

## Thinnest joints

The validator-regress joint ranks first because the whole rule depends on it: if the validator does not bottom out, the "checked" state is the forbidden state moved one layer down, as the note itself admits. The reason given answers a different question (cost, not correctness). The cache-maxim analogy ranks second. It is less load-bearing, but its reason does not match: the maxim is about losing the source, not about trusting a stale copy. The asymmetry-to-"forbidden" step and the "saves nothing" step are the two halves of the main justification. Each is thin alone, and they cover each other only partly: asymmetry needs cheap checking to justify a categorical rule, and cheap checking ignores the cost of writing the validator. The instance spread ranks last because it is presented as evidence of generality, not as the ground of the rule. Unranked joints that hold include the graceful-degradation consequence and precondition 3, which is close to definitional.

## For the human
Look first at precondition 4: say why a wrong validator fails loudly while a wrong hand-maintained copy fails silently, or limit the prohibition to validators that are themselves checked.
