---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/stock-phrases.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 01fe5fea193e21d064468eb1b1c7495441fe3ca291ba101f15b3da55209e5241
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/adb8f4e0f938ada49e21e579/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-stock-phrases.md
raw-output-sha256: 29b27edb0944422fc438b3448f27740a1d269d14d82a678e8039c99d195169e0
format: 2
---

# Review

I applied the deletion test to the sentences that resemble stock patterns.

- "The practical consequence is that interface parity alone is not enough for safe swapping." This is a summary lead-in, but it states the section's prescriptive conclusion. Without it, the following sentence gives two requirements with no stated reason for imposing them. It survives deletion.
- "A unified interface is what makes that boundary movable without rewriting callers." This ties the English-account paragraph to the note's claim. Deleting it leaves that paragraph unconnected to the interface. It survives.
- "The unified interface is what makes this callable view practical across prompts and code rather than merely analogical." This adds the contrast between a practical and an analogical callable view, which the paragraph does not otherwise state. It survives.
- "That effect is an expectation, not an observed result." This is an epistemic qualifier on the preceding prediction, not filler.

No sentence uses an elevation move, an "it's worth noting" phrase, a near-verbatim "in other words" restatement, or an "at its core" or "key insight" opener.
