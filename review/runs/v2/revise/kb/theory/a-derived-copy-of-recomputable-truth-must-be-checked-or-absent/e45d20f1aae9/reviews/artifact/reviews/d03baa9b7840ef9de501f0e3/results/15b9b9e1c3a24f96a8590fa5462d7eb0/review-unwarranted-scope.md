---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The spread is what shows it generalizes
  reason: Four surfaces within one system, one of which is another note's stated requirement
    rather than an exercised surface, are offered as showing generality. The central
    claim's generality is actually carried by the derivation, so this supporting claim
    overreaches what the instance list itself exercises.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
note-sha256: 6a9c8733d3906b1ae0ad19bb313466b162dbf7388a77276b26d65c5e003a0d8a
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d03baa9b7840ef9de501f0e3/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/d03baa9b7840ef9de501f0e3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-unwarranted-scope.md
raw-output-sha256: 2bb21af922bbe38bea33cb18cf8abaf14905a5d300e5ce4ef2e8f4b85e885454
format: 2
---

# Review

**Claimed scope.** Any artifact, in any system, that carries a copy of information mechanically recomputable from a ground-truth source.

**Support on the page.** The main support is a derivation from two premises. (1) A trusted false copy suppresses the recomputation that would expose it, while an absent copy costs a bounded recomputation. (2) Where derivation is mechanical, the check is deterministic and near-free, citing the text-testing pyramid's Level A. The note adds results inherited from linked work (indexes suppressing retrieval, LLM recompute cost, managed-staleness lineage) and worked instances within Commonplace.

**Exercised domain versus claimed scope.** The derivation covers every case where its premises hold. The note states those conditions explicitly as the four preconditions: a mechanical derivation rule, machine-locatability, ground truth at validation time, and a validator that bottoms out. It also routes out cases where they fail, namely judgment-verified dependents and execution-produced values. This is a stated transfer relation: the mechanism is argued to hold wherever the preconditions hold, independent of artifact format or system. Whether the premises always hold, for example whether validator infrastructure is cheap in a system that lacks one, is a matter of sufficiency outside this gate.

The only overreach is the supporting remark that the instance spread itself "shows" generalization (INFO).
