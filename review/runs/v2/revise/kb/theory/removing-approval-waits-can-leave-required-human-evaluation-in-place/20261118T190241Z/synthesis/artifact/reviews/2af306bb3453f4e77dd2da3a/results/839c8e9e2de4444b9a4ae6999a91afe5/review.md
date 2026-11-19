---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'The note states a secondary caveat several times: an unfulfilled specified
    task is not evidence that the task is necessary. It appears in the lead (''Whether
    a specified task is useful or necessary is a separate question''), in the blocking-versus-unfulfilled
    paragraph (''not by itself evidence that the system would fail or degrade''),
    after the weekly-review example (''This example establishes a gap against the
    specification, not that skipping review causes harm'') and implicitly in the Scope
    bullet on habitual waits. Each repetition gives the caveat a share of the reader''s
    attention that the central wait/requirement distinction should have. One possible
    direction is to state the caveat once, where blocking dependency and unfulfilled
    requirement are defined, and to cut the post-example sentence. Retained statements
    elsewhere would then have to do work the definition paragraph does not.'
outcome: report
description: Retained report review of kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/synthesis/artifact/reviews/2af306bb3453f4e77dd2da3a/inputs/target/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/synthesis/artifact/reviews/2af306bb3453f4e77dd2da3a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/synthesis
launch: 839c8e9e2de4444b9a4ae6999a91afe5
completed-at: '2026-11-18T19:04:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place/20261118T190241Z/synthesis/calls/launches/839c8e9e2de4444b9a4ae6999a91afe5/outputs/review.md
raw-output-sha256: 9f2fabea66205795d126192c30a2ff60c742e270b6ddb4572ea989c5ef2be879
format: 2
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
