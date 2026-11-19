---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A bounded, recoverable downside on one side; a silent, unbounded one on the other"
    reason: "The closing paragraph of the asymmetry section opens by restating the asymmetry that the preceding paragraph has just established. It is a summary of its own section rather than a preview of the next, and it goes on to add the conclusion (forbidden rather than risky; one missed edit away). Setup followed by summary is a weaker signal."
    level: info
outcome: pass
---

# Review

Opening paragraphs at section boundaries:

- **The asymmetry that forces the rule** opens with new content (the cost comparison), not a restatement of the introduction.
- **Where the rule applies** opens with the general managed-staleness regime, which is new material.
- **What enforcement buys** opens with the frontloading versus fix-what-the-executor-can't-determine tension, which is new material.
- **What "checked" requires** opens with a one-sentence transition into the enumerated preconditions, which is acceptable.
- **Consequences** opens with "Checked copies degrade gracefully", which reuses the asymmetry's cost of a recomputation but advances it to a lifecycle consequence.
- **Instances across four surfaces** opens with a sentence that names the four application states before the list. It is a one-sentence transition, not a full duplicate of the enumeration.

Closing paragraphs before headings do not preview the following sections. The only near-restatement is the summary line at the end of the asymmetry section, recorded as INFO.
