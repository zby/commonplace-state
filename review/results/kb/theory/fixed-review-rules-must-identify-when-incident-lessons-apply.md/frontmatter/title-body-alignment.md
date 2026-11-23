---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: 95a96b6ebc805d6224f792a284db83f897cf0cba8ca3a08efe1eecb659fb79f4
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 83b0772e8ccc44e7a507e7f3b9b27092
completed-at: '2026-11-23T11:40:02Z'
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  reason: 'Claim drift on who identifies applicability. Grammatically, the title makes
    the rule (''it'') the thing that must identify when a lesson applies. The body
    says the opposite: the rule only says where to look and ''does not tell the reviewer
    which earlier failure bears on the page at hand''. The reviewer recognizes the
    connection, and the rule stays unchanged. What the body establishes is that a
    fixed instruction to consult past incidents can carry new lessons without itself
    changing, provided the reviewer recognizes the structural feature of the earlier
    failure (here, shared origin behind supposedly independent support) rather than
    matching surface details such as source names. The title should place the identification
    with the reviewer and keep the point that the rule need not change.'
  level: warn
- scope: passage
  quotes:
  - The incident shows what the review must distinguish, not that the review rule
    must change.
  reason: The body's conclusion is that incidents refine what the review must distinguish
    while the rule stays fixed. The title does not carry this point. It states a necessary
    condition ('only if') but omits the body's main positive claim, so a reader of
    the title alone would not learn that the rule need not change.
  level: info
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/7626ce045d873bdd65a2da62/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/83b0772e8ccc44e7a507e7f3b9b27092/outputs/review-title-body-alignment.md
raw-output-sha256: c9bc990a97833c49d635ebd3c2cc9b45b9ce190a05188cb8d6b8092845138f35
---

# Review

The body is short and consistent. A standing rule such as "check past incidents" tells the reviewer where to look but not which earlier failure applies. The citation example shows that a lesson transfers through a structural feature (shared origin behind supposedly independent support), which a lookup by source name would miss. The test of success is whether the reviewer separates apparent corroboration from independent support. The incident changes what the review must distinguish, not the rule.

The H1 broadly matches this topic, but it gives the identifying role to the wrong agent. "It can identify" refers back to the rule, while the body explicitly denies that the rule identifies anything and gives that work to the reviewer. A version such as "A fixed review rule can absorb new incident lessons when the reviewer recognizes the failure's structural feature" would match the body.
