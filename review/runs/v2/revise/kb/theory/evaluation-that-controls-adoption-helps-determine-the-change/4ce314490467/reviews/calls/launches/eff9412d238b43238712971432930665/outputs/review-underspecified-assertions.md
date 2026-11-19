---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A claim of full automation must say which tasks it preserves and which requirements it retires."
    reason: "'Preserves' could mean tasks still performed, now automatically, or tasks still assigned to a person. The second reading would conflict with calling the process fully automated. The later sentence 'distinguish tasks performed automatically from tasks no longer required' mostly resolves this toward the first reading, so the ambiguity is probably not material."
    level: info
  - scope: passage
    quotes:
      - "Suppose adoption is automatic, but the process specification assigns a maintainer a weekly sample review"
    reason: "The note does not say whether 'process specification' means only written rules or also established expectations that nobody wrote down. The Scope section settles the unwritten case for waits but not for non-blocking tasks. An unwritten but expected review would count as a retired requirement under the broader reading but not under the narrower one. The reviewer cannot show that this changes the note's central inference."
    level: info
outcome: pass
---

# Review

The note's load-bearing assertions are its definitions: an actual wait is a blocking dependency, and a specified task can go undone while execution continues. Its recommendations are that a full-automation claim must name the tasks it preserves and the requirements it retires, and that retiring a review is a change in requirements rather than automation. Its boundaries are that the claim concerns required intervention, not every influence, and that habitual waits count as waits.

The definitions state their criteria: whether execution waits for a person, and whether the specification assigns the task. The worked cases supply the operational consequence of each. The paragraph on subsequent revisions resolves when an optional study turns into a dependency: when a new human assessment is made a condition of each revision.

Two possible ambiguities remain. One is what "preserves" means. The other is whether an unwritten expectation counts as part of the specification. Neither is shown to change the note's truth conditions or recommendation enough to reach WARN.
