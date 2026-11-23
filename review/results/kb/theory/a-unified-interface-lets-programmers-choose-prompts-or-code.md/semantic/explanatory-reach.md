---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/explanatory-reach.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 8a7af5aae568be28c3d8dbde54a66452a3bc66ab66475db0f11f79795445eb84
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
findings:
- scope: document
  quotes: []
  reason: The first half of the title, that callers need no change when the binding
    changes, follows almost definitionally from a shared name, arguments and result
    format. Its explanatory content lies in the asymmetric-leak account, which the
    title does not name and only the description states. The mechanism is present
    and constrained; the headline simply foregrounds its least informative part.
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/3f57ba17c25464cc004d6f28/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-explanatory-reach.md
raw-output-sha256: ca775311c0331450fb66eb3038f86d3639c0e105484705c4dec26c6eb372a400
---

# Review

## Summary

**Mechanism.** The note explains that a shared binding hides how the rule is implemented. The binding cannot hide which execution regime handles the call. Because LLM callers rely on natural-language descriptions and on tolerance, and code callers rely on latency, cost and deterministic failure, each swap direction exposes a different assumption.

**Variation test.** Suppose prompt-backed callees were as strict as code. Then the prompt-to-code leak would disappear, and the asymmetry claim would change. Suppose prompt calls had the latency and failure profile of functions. Then the code-to-prompt leak would disappear. The conclusion therefore depends on the premises the note uses, so it is not easy to vary.

**Falsifiability.** Two observations would contradict the claim: swaps that required call-site edits despite a shared binding, or leaks that did not differ by direction.

**Ad-hoc accommodation.** The Scope bullets on behavioral invariance, adapters and call-site headroom follow from the stated mechanism. They are not escape hatches. The headroom condition is a direct consequence of the code-to-prompt leak.

The explanation is adequate. The INFO finding concerns emphasis in the title, not a missing mechanism.
