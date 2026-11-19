---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'costs the consumer one bounded recomputation: run the query, read the source,
    do the work the copy would have saved.'
  - Dropping one costs consumers a recomputation, never correctness
  reason: 'The asymmetry premise assumes that recomputation is reliable. For model
    consumers, the linked note on LLM recompute cost says model-side derivation can
    involve ''reasoning unreliably'' and ''can fail''. An absent copy can therefore
    cost correctness: the consumer runs a partial search, stops, and has no signal
    that anything is wrong. That is the same silent failure the note attributes only
    to the false copy. The note needs to state that the absent branch is bounded and
    correct only when the recomputation itself is reliable, for example when code
    derives the value, or else weaken ''never correctness''.'
- scope: passage
  quotes:
  - can cause silent, unbounded wrongness when it tells consumers to stop looking
  reason: '''Unbounded'' is not supported by the linked grounding. The indexes note
    limits itself to a conditional control-flow mechanism and calls it ''not a prevalence
    claim''. A stale hand-maintained copy is wrong by at most the drift since its
    last edit, and that amount is often small and estimable. The asymmetry that the
    note says ''forces'' the rule is therefore one of expected cost, not of category:
    bounded versus unbounded.'
- scope: passage
  quotes:
  - since trusting an unchecked copy now saves nothing
  reason: 'This counts only the cost of running the check, which is Level A and near
    zero. It omits the cost of building it: writing the validator, marking a machine-locatable
    region and handling false failures. Precondition 4 answers that cost by amortization
    ''across every copy it protects'', but a singleton copy with a low drift rate
    has nothing to amortize over. In that case trusting the copy can save the cost
    of building the validator, so the claim that trust ''saves nothing'' does not
    hold in general.'
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: Only 'maintained by hand and trusted' is forbidden. A hand-maintained copy
    that is used as an advisory hint, and that consumers do not treat as authoritative,
    is neither checked nor absent, yet the rule does not forbid it. The linked indexes
    note calls this 'Separate orientation from enumeration'. The two-state framing
    should either admit this third state or define trust so that it covers it.
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/critique-note.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: 6a402875150a2649f57275adda6ca69ae7669f0b06ef57a14b0685e5ff6ab220
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/ca7846d1ed8d4ad05fc3e50c/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/ca7846d1ed8d4ad05fc3e50c/observation.json
contract-sha256: 9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T132933Z
launch: ec32e06b88564a8fa69c598655e7467f
completed-at: '2026-11-15T13:30:48Z'
raw-output: kb/reports/state/review/runs/v2/20261115T132933Z/calls/launches/ec32e06b88564a8fa69c598655e7467f/outputs/review.md
raw-output-sha256: ee0d486624684c42d7c850e89d65f00fe2748518d7ffe090ae01bbcec69d888a
format: 2
---

# Critique: A derived copy of recomputable truth must be checked or absent

**Note:** kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
**Central commitment:** A copy of information that can be mechanically recomputed from a ground-truth source must be either checked by a validator against that source or absent. Hand-maintained-and-trusted is forbidden, not merely risky, because absence costs a bounded recomputation while a false copy causes silent, unbounded wrongness.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a pragmatic cache-and-reliability engineer, of the kind who works with bounded staleness and error budgets. They accept the note's preference ordering and reject its absolute form. The "forbidden" verdict depends entirely on the asymmetry section, where the note says the rule "rides entirely on that". The asymmetry needs two premises, and neither holds in general for the consumers this KB serves.

1. **The absent branch is not reliably correct.** The note says an absent copy costs "one bounded recomputation" and that dropping a checked copy costs "a recomputation, never correctness". This is true when code recomputes the value. The note's own linked grounding, *LLM recompute cost shifts the store-vs-recompute balance*, says that model-side derivation involves "reasoning unreliably" and "can fail". Suppose the `complete` mark were removed. An agent that must establish tag membership itself may run a narrow `rg`, accept a partial result and stop, with no signal that anything is wrong. That is silent wrongness on the absent side. Omission therefore moves the failure from a stale artifact to a fallible recomputation, and the second can be the larger risk.

2. **The false-copy branch is not unbounded.** A stale hand-maintained list is wrong by at most the drift since its last edit. When the source changes slowly, that error is small and can be estimated. The linked indexes note says its mechanism is conditional and "not a prevalence claim". It does not support "unbounded".

Once both premises are weakened, the choice is an expected-cost comparison. The linked LLM-recompute note frames it this way: compare the total expected costs of model-side derivation, external on-demand derivation and checked materialization. A comparison of costs gives a strong default for checked or absent. It does not prohibit the third option. The note's claim that unchecked trust "saves nothing" also counts only the cost of running the validator. It leaves out the cost of building one, including writing it, marking the region and handling false failures. For a singleton copy with a low drift rate, that cost has nothing to amortize over.

The author cannot dismiss this in one sentence. The first premise is taken from a note this note cites as grounds.

## How the note engages it

**Partially engaged.**

- The note concedes that omission has a cost: "Omission is the fallback, not the optimum" and "both pay a build-time or hot-path cost" (Consequences). That cost is latency or context, though, not correctness. The note never considers that the recomputation might itself be wrong.
- Precondition 4 answers the cost of building the validator by amortization: "amortized across every copy it protects", compared with "N independently hand-maintained instances". That answers the many-copy case. It leaves out the singleton case, which includes two of the note's own instances: the one `AGENTS.md.template` pair and a single hot-path skill list.
- Precondition 3 and the "managed staleness" section mark the scope boundary well. They separate the case where the rule applies from the case where judgment is required. They do not address fallible mechanical recomputation by a model consumer inside that scope.
- The "unbounded" characterization is asserted, not engaged. Nothing in the note bounds or measures how wrong a stale copy can be.

The attack does not overturn the prescriptive core. Where a deterministic validator is cheap and shared, a checked copy dominates both alternatives, and the tag-README and template instances show this. What fails is the justification for the absolute "forbidden" and the claim that omission is always correctness-preserving.

## Constructive findings

- State that the absent branch is bounded and correct only when recomputation is reliable: code-side derivation, or external on-demand derivation that returns the answer to the model. Say that model-side recomputation brings back a silent-failure risk on the absent side. Link this to the "external on-demand derivation" path in the LLM-recompute note as the omission form that keeps correctness.
- Replace "silent, unbounded wrongness" with a bounded description, such as wrongness proportional to undetected drift, unsignalled and able to suppress the corrective search. Then present "forbidden" as following from expected cost under the stated preconditions, not from a categorical asymmetry.
- Add a singleton clause to precondition 4. Where there is nothing to amortize over, either show that a generic validator mechanism covers the copy, as in the open question about marked regions, or accept omission as the answer for singletons. Do not imply that trust "saves nothing" there.
- Address the advisory or hint state, where a copy is maintained by hand but consumers are not allowed to stop on it. Either name it as a third valid state, which the indexes note's "separate orientation from enumeration" already permits, or define "trusted" so that the two-state claim stays exact.

## Secondary objections (optional)

- The four-instance spread is offered as what "shows it generalizes". The compiled-memory instance is only stated, with a cross-reference, and has no shipped mechanism. The hardcoded-contract instance has not yet been enforced. Two of the four therefore illustrate the rule but do not test it.
- The closing line, "a cache must never be the only copy", is a different principle. It concerns data loss when the cache is the sole holder, not staleness when a source still exists. Linking the two may confuse more than it clarifies.
