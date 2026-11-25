---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0a82a91c92e249c49d04fe5b4ad579a9/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/f745f484c0baae6a101df351/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 0a82a91c92e249c49d04fe5b4ad579a9
completed-at: '2026-11-25T05:24:27Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0a82a91c92e249c49d04fe5b4ad579a9/outputs/review-claim-to-section-ratio.md
raw-output-sha256: be86b8e6836946b0abd2069bdaa555b3b303a5b74a116c0684326264fffe6e30
format: 2
---

# Review

## Summary

The note has three sections (Stakes, Current answer, Unsettled) and carries far more distinct non-obvious claims than that. Stakes argues that mixed natural-language and code systems lack the static reachability checks code has, and that bloat compounds through three distinct channels; it also states retirement conditions for the query. Current answer gives five separate mechanisms, each with its own warrant. Unsettled lists six separate open problems: no reachability oracle, cross-boundary co-bloat, missing retirement triggers, useful redundancy versus bloat, brevity-induced encoding distortion, and additive bias.

Each section does work of a different kind: motivation and retirement condition, current practice, and open frontier. These are the standard parts of a standing query. No section restates another section's framing. Sections do not outnumber claims, so the gate passes.
