---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Direct memory fails when it becomes generic capture rather than a role-specific artifact. A note can be accurate but hard to find. An instruction can steer behavior incorrectly. A check can fossilize a temporary workaround."
    reason: "The section's lead sentence names generic capture as the failure. Each following example, however, is a role-specific artifact (a note, an instruction, a check) that fails for a different reason: findability, wrong guidance, or premature hardening. The section closes with a broader criterion ('good only when it becomes useful future context or useful future behavior'). The examples fit that closing criterion better than the lead sentence. This is likely drift rather than outright contradiction, because 'fails when' can be read as one sufficient condition. A human should confirm whether generic capture is meant as the failure mode or as one of several."
    level: info
outcome: pass
---

# Review

## Summary

Key claims:

- The opening says direct creation is the context-efficient path when understanding is live, and that it is not blank-page writing: destinations expose creation contracts.
- Methods lists destinations and write-time support. This is consistent with the "not blank-page" claim and the opening's artifact kinds.
- Failure Modes gives a framing sentence, three examples and a closing criterion.
- The Evaluation Questions match the opening (live context and provenance), the creation-contract claim (validation before promotion), and the closing criterion (a future agent can find and apply the artifact).

No pairwise contradiction appears. Key terms do not drift between sections. The one tension is inside Failure Modes: the lead sentence frames failure narrowly, while its examples and closing line frame it broadly. It is recorded as INFO for human confirmation.
