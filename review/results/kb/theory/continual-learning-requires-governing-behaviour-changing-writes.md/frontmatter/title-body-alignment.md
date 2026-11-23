---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
note-sha256: e70eede547409cec537816ffcddfa6bb4f70d9987e9032ec40acab356ca874e3
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 108398db49d74079985f02aa4af94d87
completed-at: '2026-11-22T21:51:07Z'
findings:
- scope: passage
  quotes:
  - The same edit hand-authored in reaction to an incident is maintenance
  reason: 'The body establishes a further condition the title does not show: governance
    counts as continual learning only when the system''s own loop does the selecting.
    Governance by people outside the loop is called maintenance. The title states
    a necessary condition, so this does not contradict it. Still, the body''s discriminator,
    autonomous evidence-responsive selection, is a substantial part of what the note
    establishes, and the title omits it. If the note wants that point to be retrievable
    from the title, consider a qualifier such as ''self-governing'' or ''autonomously
    governing''.'
  level: info
contract: verdict
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/108398db49d74079985f02aa4af94d87/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/222683c35d85d92b304352a7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/108398db49d74079985f02aa4af94d87/outputs/review-title-body-alignment.md
raw-output-sha256: 8d6c232dff17a587f1311ad727cf99083259797549e0facbb079dc1b3da09777
---

# Review

## Summary

The body supports the H1 claim. It argues that persistence does not decide which retained item shapes behaviour or with what force. It locates behavioural authority in consumption paths rather than stored bytes. It then describes the required governance: choosing, validating, assigning an authority path and coordinating writes across representational forms. That is the title's claim that continual learning requires governing behaviour-changing writes and not just storing content.

The body confines itself to deployed systems ("Continual learning in a deployed system"), while the title is unqualified. The description supplies that scope, and the body treats deployment as the field's normal setting, so this is not a material scope drift. The only notable gap is the autonomy condition recorded in the info finding.
