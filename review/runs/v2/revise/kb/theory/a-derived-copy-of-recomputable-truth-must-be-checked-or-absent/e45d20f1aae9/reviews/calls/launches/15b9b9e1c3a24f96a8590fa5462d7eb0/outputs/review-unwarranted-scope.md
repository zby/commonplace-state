---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The spread is what shows it generalizes"
    reason: "Four surfaces within one system, one of which is another note's stated requirement rather than an exercised surface, are offered as showing generality. The central claim's generality is actually carried by the derivation, so this supporting claim overreaches what the instance list itself exercises."
    level: info
outcome: pass
---

# Review

**Claimed scope.** Any artifact, in any system, that carries a copy of information mechanically recomputable from a ground-truth source.

**Support on the page.** The main support is a derivation from two premises. (1) A trusted false copy suppresses the recomputation that would expose it, while an absent copy costs a bounded recomputation. (2) Where derivation is mechanical, the check is deterministic and near-free, citing the text-testing pyramid's Level A. The note adds results inherited from linked work (indexes suppressing retrieval, LLM recompute cost, managed-staleness lineage) and worked instances within Commonplace.

**Exercised domain versus claimed scope.** The derivation covers every case where its premises hold. The note states those conditions explicitly as the four preconditions: a mechanical derivation rule, machine-locatability, ground truth at validation time, and a validator that bottoms out. It also routes out cases where they fail, namely judgment-verified dependents and execution-produced values. This is a stated transfer relation: the mechanism is argued to hold wherever the preconditions hold, independent of artifact format or system. Whether the premises always hold, for example whether validator infrastructure is cheap in a system that lacks one, is a matter of sufficiency outside this gate.

The only overreach is the supporting remark that the instance spread itself "shows" generalization (INFO).
