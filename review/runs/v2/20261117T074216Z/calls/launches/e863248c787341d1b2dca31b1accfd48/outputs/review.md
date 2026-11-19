---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Optional observation is different from monitoring on which the process relies."]
    reason: "UNSUPPORTED — Here the note changes its dependency test without saying so. Earlier, a process depends on a human activity when it must wait for it before adoption. After adoption nothing waits, so the note switches to 'relies on'. It never says what makes post-adoption monitoring relied on rather than optional. The non-blocking case asserts that the process does not rely on the week-later assessment. That assessment could still trigger a rollback, as the monitoring example describes. Without a criterion, the note cannot place a periodic review that sometimes reverses changes. The line between the two roles is stated but not derived."
  - scope: passage
    quotes: ["Bypassing a required check is not evidence that its function has been automated or is unnecessary."]
    reason: "THIN — The claim is absolute: bypassing is 'not evidence'. A bypassed check followed by no observed harm is at least weak evidence that the check may be unnecessary. The defensible claim is that bypassing alone is insufficient evidence. The note gives no reason for the stronger claim that bypassing is no evidence at all."
  - scope: passage
    quotes: ["Describing the whole episode as evaluation obscures which human activities the system needs."]
    reason: "THIN — The implicit ground is the previous sentence: one episode can contain both approval and later assessment. That shows a single label could hide the distinction, not that it does. The note gives no case where the label caused someone to misjudge which human stop to automate. The claim is plausible, but the harm is asserted rather than shown."
  - scope: passage
    quotes: ["Conversely, a program can apply human-authored acceptance rules without requiring a new human judgment for each change."]
    reason: "HOLDS — The sentence follows from the note's own test: no person is waited on for each change. It leaves open whether keeping those rules correct is itself a human dependency in continued operation. The Scope section partly covers this by separating check adequacy from the dependency question."
  - scope: passage
    quotes: ["The process depends on human intervention even if the maintainer always approves."]
    reason: "HOLDS — This follows directly from the stated setup: the agent adopts only after approval, so the process must wait for a person whatever the approval rate. The question of whether the stop can be removed goes to the linked note, which is appropriate."
outcome: report
---

# Friction check: Evaluation required for adoption is part of the operating process

**Central claim (one sentence):** Human evaluation that a system must wait for before adopting a change is part of its operating process, while human assessment that only measures an already-adopted change need not be.

## Filter
**Filter:** SURVIVES

The claim makes three commitments. Role is decided by dependency, not by the activity's name. Any required wait creates a stop, even if the input is non-binding. Optional assessment creates no stop. These commitments are consistent. Extending the test to post-adoption monitoring does not split the claim, because monitoring that the process relies on counts as a dependency. That extension still needs its own criterion; see the first finding.

## Thinnest joints

The weakest joint is where the note moves from adoption to continued operation. The adoption case has a clear test: does the process wait? The monitoring case replaces this with an undefined test, "relies on". That undefined test decides whether the non-blocking example really creates no dependency. The next two joints overstate small steps. One turns "insufficient evidence" into "no evidence". The other asserts that a label obscures the distinction without showing the harm. The last two joints follow from the note's own definitions and hold.

## For the human
Look first at the monitoring paragraph: what criterion separates relied-on monitoring from optional observation once no process waits?
