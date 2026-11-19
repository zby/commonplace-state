---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "unless it is extended with the required control fields"
    reason: "This qualifier concedes that a retrospective-memory surface with the right control fields could carry live state. That makes the distinction one of fields and lifecycle, not of surface kind. The concession improves the explanation rather than merely dodging counterexamples, but the title still reads as a distinction of kinds. The mechanism ('what the surface stores and when it deletes') could be stated as the core claim so the qualifier is no longer needed as an exception."
    level: info
outcome: pass
---

# Review

The central claim is that active work state differs from retrospective memory and chat history. The note gives a mechanism: each surface answers a different question, and each lacks something the others provide.

- Chat history is ordered by time, so a resuming session must reconstruct the live state from a trace.
- Retrospective memory stores lessons or episodes and lacks pointers, open gates, dependencies and a success state.
- A growing instruction file lacks any deletion trigger, so done work remains ambient.

Varying a premise changes the conclusion. If chat history were organised by liveness, or if retrospective memory carried closure criteria, the distinction would weaken. The note itself acknowledges the second case. The claim is falsifiable: a system that resumes multi-session work reliably from retrospective memory alone, with no control fields, would count against it.

The one qualifier that could look like an escape hatch, "unless it is extended", actually sharpens the mechanism: the needed fields and lifecycle are what matter. The mechanism is present and reasonably hard to vary.
