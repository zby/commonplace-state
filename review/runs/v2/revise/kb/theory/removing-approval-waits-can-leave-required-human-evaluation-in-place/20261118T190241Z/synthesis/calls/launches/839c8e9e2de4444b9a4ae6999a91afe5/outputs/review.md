---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The note states a secondary caveat several times: an unfulfilled specified task is not evidence that the task is necessary. It appears in the lead ('Whether a specified task is useful or necessary is a separate question'), in the blocking-versus-unfulfilled paragraph ('not by itself evidence that the system would fail or degrade'), after the weekly-review example ('This example establishes a gap against the specification, not that skipping review causes harm') and implicitly in the Scope bullet on habitual waits. Each repetition gives the caveat a share of the reader's attention that the central wait/requirement distinction should have. One possible direction is to state the caveat once, where blocking dependency and unfulfilled requirement are defined, and to cut the post-example sentence. Retained statements elsewhere would then have to do work the definition paragraph does not."
outcome: report
---

# Simplification synthesis: Removing approval waits can leave required human evaluation in place

The four checks broadly agree that the note is compact. The claim comes first. The cases, the revision paragraph and the Scope bullets each support the claim or set a boundary. Branch-bloat and core-claim-obscured found nothing. Detail-overhang and marginal-value-redundancy both flagged the same repeated caveat. Taken together, these findings justify one fold across the whole note. The other flagged items are local wording choices and do not reach the threshold:

- the anticipatory list of fates in the Required approval case;
- the restating clause before the link to the factory-claim note.

## Opportunities

### 1. State the necessity caveat once

- Location: the lead paragraph ("Whether a specified task is useful or necessary is a separate question"), the second paragraph ("not by itself evidence that the system would fail or degrade without the task"), "Name the process being automated" ("This example establishes a gap against the specification, not that skipping review causes harm.") and the second Scope bullet ("not evidence that the evaluation is needed to meet a stated requirement").
- Combines: marginal-value-redundancy (warn, post-example sentence); detail-overhang (info, same sentence and recurrence across the lead, the definition paragraph and Scope).
- Reader problem: The note's contribution is the difference between a wait and a requirement. The disclaimer that a requirement does not show necessity recurs up to four times. Each recurrence makes the secondary point compete with the central distinction. It can also make the note seem more concerned with not overclaiming than with its own claim.
- Direction: Keep one authoritative statement, most naturally in the second paragraph, where blocking dependency and unfulfilled requirement are defined. Cut the sentence after the weekly-review example. Then decide whether the lead's version is still needed as a one-clause signpost. One possible resolution would leave the lead with "a claim of full automation must say which tasks it preserves and which requirements it retires." The usefulness question would then sit only in the definition paragraph.
- Preserve or decide:
  - Keep the Scope bullet on habitual waits. Its main job is a different boundary: an unwritten wait still blocks. Only its trailing clause overlaps the caveat.
  - Keep the closing sentence about retiring an unnecessary review. It makes a separate point: retirement changes requirements and is not automation.
  - The author must decide whether the caveat belongs in the lead as part of the note's headline commitments. It may need to stay there if readers are likely to take "required human evaluation remains" to mean "human evaluation is needed." It can move down if it is only a guard. The artifact does not settle that choice, so the synthesis leaves it open.
