---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "If a maintainer must inspect each adopted instruction and reverse harmful changes, the broader process still requires human work."
      - "Optional observation is different from monitoring on which the process relies."
    reason: "The note leaves the mechanism of post-adoption dependency open. Elsewhere it tests dependency by waiting: a person is needed 'for the process to proceed', and the non-blocking case qualifies because the process 'neither waited for that assessment nor relies on it to continue.' Post-adoption monitoring does not make adoption wait. That leaves two reasonable readings of 'monitoring on which the process relies' and 'must inspect'. (a) A rule or schedule requires the inspection to happen, such as a mandatory review step or a gate on the next cycle. (b) The system's quality or safety depends on a human catching and reversing harmful changes, even though nothing blocks without that human. The choice is material. Under (b), the week-later assessment in the Non-blocking assessment case becomes relied-on monitoring whenever a harmful finding would lead to a rollback. That collapses the note's central contrast. It also changes which human activities the description says automation 'must address'. Under (a), that assessment stays optional observation. The text does not say which test separates optional observation from relied-on monitoring."
    level: warn
outcome: warn
---

# Review

## Summary

Most of the note's load-bearing assertions are resolved locally. The opening distinction defines its consequence: required evaluation "requires a person for the process to proceed", while measuring assessment "can observe a process that runs without one". The two hypothetical cases fix the scope (one KB instruction), the timing (before adoption versus a week later) and the dependency test (whether the agent must wait). The closing clauses of "The same activity can perform different roles" address edge cases: a non-binding recommendation that the agent must wait for, and human-authored rules applied by a program. The Scope bullets set explicit boundaries: required intervention, not influence; a written requirement versus actual execution; stop removal versus quality.

## The unresolved choice

The section "Name the process being automated" extends dependency from adoption to "continued operation". This is where the note leaves an argument-relevant mechanism open. Up to that point, the test is waiting: does the process stop until a human acts? Post-adoption monitoring with rollback never makes adoption wait, so this passage needs a different test. It does not state one. "Must inspect" and "monitoring on which the process relies" could mean a procedural requirement, or a dependence of outcome quality on human correction. The second reading would also cover the earlier non-blocking assessment whenever its findings could trigger a rollback. The note therefore cannot yet say reliably which human activities count as stops that automation must address. That is the practical consequence its description promises.

The gate reports this choice and does not choose for the author. The author might state the test for relied-on monitoring. Alternatively, the author might limit the extension to monitoring that a rule makes mandatory, or explain how the Non-blocking assessment case avoids it.
