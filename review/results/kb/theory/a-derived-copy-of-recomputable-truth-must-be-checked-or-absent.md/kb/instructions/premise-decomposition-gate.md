---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 7637b6ab0e834bee966ca20c736a9f60
completed-at: '2026-11-16T22:23:02Z'
findings:
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: 'DOUBTFUL — Premise (universal): every hand-maintained copy that is not
    machine-checked falls into the trusted state, so the only valid states are checked
    or absent. — An advisory copy is a third state the dichotomy leaves out: a hand-maintained
    hint that consumers use only to rank or start a search and always verify, such
    as a dated ''as of 2026-06, about 40 members'' count or a retrieval cue that only
    orders results. It is neither checked nor absent, yet it does not suppress recomputation,
    so the asymmetry argument does not reach it. The note''s own second instance (compiled
    retrieval cues) sits near this case. The title says ''must be checked or absent'',
    but the argument only supports forbidding the *trusted* copy. — LOCAL: rescued
    by scoping the commitment to copies that consumers rely on instead of re-deriving,
    or by naming advisory, explicitly untrusted copies as allowed in a Scope section.
    — instance'
- scope: passage
  quotes:
  - An unenforced copy is always one missed edit away from the catastrophic state,
    with nothing watching.
  reason: 'DEFEATED — Premise (universal, ''always''): every unenforced copy can become
    false through a missed edit. — Counterexample: a copy of an immutable source,
    such as values copied from a released, version-pinned artifact or the decision
    text of a superseded ADR that will never be edited. No edit to the source can
    occur, so no missed edit can make the copy stale. Separately, ''nothing watching''
    is false wherever code review or a co-located edit discipline covers both copies,
    although that only weakens the risk and does not remove it. — LOCAL: the asymmetry
    survives for copies of mutable sources; add that condition to the scope. — instance'
- scope: passage
  quotes:
  - since trusting an unchecked copy now saves nothing
  reason: 'DEFEATED — Premise (universal): once derivation is mechanical, verification
    is near-zero cost and runnable on every pass, so trusting an unchecked copy saves
    nothing. — Counterexample: a coverage percentage or a benchmark figure in a README
    is mechanically recomputable but needs a full test or benchmark run to re-derive.
    Its check is deterministic and binary but not near-zero cost, so checking it on
    every pass costs something real. Mechanical derivability and cheap derivability
    are separate properties, and the note''s four preconditions name only the first.
    — LOCAL: add a cost condition, or allow ''checked'' to mean checked at a scheduled
    gate such as CI. The commitment itself can stand. — instance'
- scope: passage
  quotes:
  - converting staleness into a validation failure at check time instead of a silently
    wrong snapshot discovered mid-task
  reason: 'DOUBTFUL — Premise (unstated as a condition): the validator runs before
    consumers read the copy, so a checked copy is never consumed while stale. — The
    note says the check is ''runnable on every pass'', not that it runs on every pass.
    When validation is invoked on demand or only in CI, a source edit can make a checked
    copy stale between runs, and an agent reading in that window gets the trusted-but-false
    snapshot the rule forbids. The claim that dropping a checked copy ''never'' costs
    correctness depends on the same timing. — LOCAL: state that ''checked'' requires
    the validator to sit on a path that runs before consumption, such as a pre-commit
    or edit-time hook. — instance'
- scope: passage
  quotes:
  - its unit cost of correctness-assurance is far lower than N independently hand-maintained
    instances would be
  reason: 'DOUBTFUL — Premise (tendency, ''expected to bottom out''): a centralized,
    reviewed and amortized validator ends the regress of unchecked claims. — Amortization
    lowers the cost of assurance but not the effect of an error. A validator bug is
    a correlated failure across every copy it protects. A sweep that silently skips
    one participating collection would pass every `complete` mark that omits members
    from that collection, and the passing check adds a stronger trust signal than
    an unchecked hand copy carries. The note names this risk only for derivation rules
    that need judgment, not for mechanical ones that are wrong. — LOCAL: rescued by
    requiring the validator itself to be tested against known-false copies, so that
    a passing check means something. — instance'
- scope: passage
  quotes:
  - costs the consumer one bounded recomputation
  reason: 'DOUBTFUL — Premise (universal): an absent copy costs only a bounded recomputation
    and never wrongness. — This assumes the consumer recomputes once the copy is gone.
    An agent whose hot-path skill no longer inlines a contract list may guess the
    list from memory instead of reading the contract, and that is also silent wrongness.
    The cost can also be large: the linked note on LLM recompute cost is cited precisely
    because recomputation is dear to a model. Absence is the safer failure, but it
    is not wholly bounded or wholly correct. — LOCAL: the asymmetry needs ''absent
    copy plus an instruction that names where to recompute'', which the read-live
    branch already supplies. — instance'
- scope: passage
  quotes:
  - The spread is what shows it generalizes
  reason: 'DOUBTFUL — Premise (evidential): four surfaces in different states of application
    show that the rule generalizes. — All four surfaces come from one repository.
    Only one, the `complete` mark, is reported as enforced and shipped. The memory
    instance is a requirement stated in another note. The hot-path instance is hypothetical
    (''would dominate''). The template instance states a byte-identity requirement
    but does not say a check exists. The spread shows that the rule can be applied
    to four surfaces, not that enforcement has paid off across them. — LOCAL: the
    commitment rests on the asymmetry argument, not on the instances; weaken ''shows
    it generalizes'' to ''illustrates its range''. — instance'
- scope: passage
  quotes:
  - natural-language summaries and judgments do not — there is no comparison a machine
    can run
  reason: 'HOLDS — Premise (universal): natural-language summaries and judgments have
    no deterministic re-derivation, so they fall outside the checked branch. — The
    hunt looked at LLM-based comparison, which can compare them. The note already
    assigns that to Level B judgment and the managed-staleness regime, so it is not
    a deterministic re-derivation, and no counterexample was found inside the stated
    boundary.'
- scope: document
  quotes: []
  reason: 'HOLDS — Unstated premise (universal): fidelity to the ground-truth source
    is the property that matters, so checking the copy against the source is enough
    even when the source itself might be wrong. — The hunt looked at sources that
    are themselves wrong. A copy that faithfully mirrors a wrong source is correct
    relative to the rule''s question, and source error is a separate problem that
    the copy neither creates nor hides. No counterexample was found inside the rule''s
    scope.'
contract: report
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/687931c0ed7d2476a52eb94f/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/687931c0ed7d2476a52eb94f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/7637b6ab0e834bee966ca20c736a9f60/outputs/review.md
raw-output-sha256: 546d4481bd716f494224d7468b86e808c05fefc19c96a8594cf01a3d4221d5b4
---

# Premise decomposition: A derived copy of recomputable truth must be checked or absent

**Register:** claim
**Central commitment (one sentence):** A copy of information that can be mechanically recomputed from a ground-truth source must either be re-derived and compared by a validator or not exist, because a hand-maintained copy that consumers trust risks silent, unbounded wrongness while absence costs only a bounded recomputation.

## Premises and counterexamples

The commitment rests on one argument with two halves.

The first half is the **asymmetry**: an absent copy has a bounded cost, a false copy has an unbounded one, and an unenforced copy is always one missed edit away from becoming false. These premises carry the prohibition, so most findings target them.

The second half is **feasibility**: the check is cheap enough and trustworthy enough to make the checked branch the dominant option. It depends on three things:

- derivation is mechanical and near-zero cost;
- the validator runs before the copy is consumed;
- the validator ends the regress.

The dichotomy "checked or absent" consumes one more premise: that no third state is safe. Advisory copies that consumers never rely on are the case the dichotomy appears to miss.

The evidence premise, that the four instances show the rule generalizes, is listed because the note says it carries generalization. The commitment does not depend on it.

The failures look local. Each can be rescued by a scope condition:

- mutable sources;
- copies consumers rely on;
- a cost bound or scheduled check;
- validator placement before consumption;
- tests for the validator itself.

None of them, alone, forces the commitment to be withdrawn. Taken together, though, they suggest that the actual commitment is narrower than the title: trusted copies of mutable sources whose check is cheap and runs before consumption.

## For the human

Look first at the "no safe middle" dichotomy. The argument supports forbidding *trusted* hand-maintained copies, but the title also forbids advisory copies that consumers always verify, and the note's own retrieval-cue instance sits close to that third state.
