---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Removing approval waits can leave required human evaluation in place"
    reason: "'Approval' narrows the title claim without doing work in the argument. The mechanism depends only on there being a wait, meaning that execution blocks until a person acts. The body itself extends it to non-approval waits: 'A non-binding recommendation still creates a dependency if the agent must wait for it', and a habitual wait for human input. The deletion test ('Removing human waits can leave required human evaluation in place') leaves the argument unchanged. Approval is the motivating case, so it belongs as the example, not as a restriction in the central claim."
    level: warn
  - scope: passage
    quotes:
      - "a maintainer a weekly sample review and rollback of harmful changes"
    reason: "'Evaluation' in the title may also be narrower than the argument. The wait-versus-specified-task distinction does not use any property of evaluation, and the note's own example includes rollback, which is a remedial action, not an assessment. 'Evaluation' is plausibly intentional topical scoping, since the note is about evaluation roles, so this is INFO."
    level: info
outcome: warn
---

# Review

## Summary

The note supplies the qualifiers "approval" (on waits), "required" and "human" (on evaluation), and "evaluation".

- **"Required"** is load-bearing. Removing it loses the contrast with optional assessment, which the note develops at length.
- **"Human"** is load-bearing. The note concerns what work still requires a person.
- **"Approval"** does no work. The reasoning uses only the blocking property of a wait, and the body explicitly covers recommendation waits and habitual input waits. The narrower title may lead readers and downstream notes to cite the claim as specific to approval steps.
- **"Evaluation"** is probably intentional topical scoping, though the mechanism would carry over to any specified human task. It is recorded as INFO.
