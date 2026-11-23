---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Enforcing input schemas strictly at the call boundary while the implementation
    is still a prompt prevents callers from accumulating this hidden coupling.
  reason: The prompt-to-code bullet diagnoses a leak and then appends a prescriptive
    remedy. The remedy could stand as its own point, but it addresses the same failure
    the bullet describes, and the paragraph after the list restates it as a practical
    consequence. It reads as elaboration of one idea more than a buried second claim.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/structural/compound-bullet.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/structural/compound-bullet.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/e2cdfda1e7ac43f1a4560729d225a459/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/517e5f973269102133733ed3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: e2cdfda1e7ac43f1a4560729d225a459
completed-at: '2026-11-20T11:10:34Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/e2cdfda1e7ac43f1a4560729d225a459/outputs/review-compound-bullet.md
raw-output-sha256: c887c8708feaa8ad6c343d61fa81c95edf67c49303bedd9bf5c77de01f45af55
format: 2
---

# Review

I checked each bullet longer than about 30 words: the two leak-direction bullets, the three Scope bullets, the three ticket_classifier moves and the Open Questions.

Each bullet develops one point with supporting detail. The code-to-prompt leak bullet gives two illustrations (loop latency and cost, then exception handling) of one claim: a signature does not express runtime assumptions. Each Scope bullet states one limit and explains it. Each ticket_classifier move describes one swap with its motive and effect. Each open question asks one question, and the third question's "or" clause states the alternative answer rather than a second question.

The only borderline case is the remedy sentence at the end of the prompt-to-code bullet, recorded as INFO above. Splitting it out is optional.
