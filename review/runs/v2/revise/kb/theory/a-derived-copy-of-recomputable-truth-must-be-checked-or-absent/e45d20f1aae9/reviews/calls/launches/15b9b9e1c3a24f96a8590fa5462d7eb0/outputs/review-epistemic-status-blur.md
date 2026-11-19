---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a validator is centralized, versioned, reviewed on every change, and amortized across every copy it protects"
    reason: "This empirical-sounding generalization about validators carries precondition 4's argument that the regress bottoms out. It is stated as established fact, with no evidence or citation. Whether validators are in fact reviewed on every change is a property of a particular development process, not of validators as such. Its status as an assumption or design expectation is not recoverable from the wording."
    level: warn
  - scope: passage
    quotes:
      - "An unenforced copy is always one missed edit away from the catastrophic state"
    reason: "The preceding paragraph establishes the harm modally ('A *false* copy can cause silent, unbounded wrongness'); this sentence restates it as 'always' and 'catastrophic' without new support. The derived consequence takes on more confidence than its premise carries."
    level: info
  - scope: passage
    quotes:
      - "would dominate, recovering the context economy without the drift"
    reason: "The claim that enforcement would dominate omission for hot-path contract values is a projection about an unbuilt mechanism; the Open Questions section asks for the 'cheapest general mechanism' for such regions. The conjectural status is recoverable, but only by connecting two distant passages."
    level: info
outcome: warn
---

# Review

The note is mainly a normative derivation. From an asymmetry premise and a check-cost premise it concludes that a recomputable copy must be checked or absent. Most of it presents that status honestly. The harm is stated modally ("can cause"). The check-cost boundary is tied to a cited pyramid. The four preconditions are a qualitative decomposition the note owns. Instance states are labelled (enforced, resolved by omission, not yet applied).

The WARN concerns precondition 4. The argument that the validator regress terminates rests on a factual description of how validators are maintained, given in the same declarative register as the derivation. A reader cannot tell whether "reviewed on every change" is observed practice, a requirement the note imposes, or an assumption. Yet precondition 4's conclusion inherits the confidence of that description.
