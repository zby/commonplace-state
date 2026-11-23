---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/orphan-references.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/prose/orphan-references.md
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:58Z'
findings:
- scope: passage
  quotes:
  - where tool-description selection degrades even when names are namespaced
  reason: 'The open question presupposes an empirical result: tool selection degrades
    with many tool descriptions, even with namespacing. No source or observation is
    given. Because it sits inside an open question and gives no figure, the risk is
    low. A citation, or rewording it as a suspected effect, would let the reader evaluate
    the premise.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/6ce888c3771a2d56d12a0d4b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-orphan-references.md
raw-output-sha256: 72a43f84d00ee5c98b9ac2c8809eeea097523afdd0df632b7ee30427cdbed862
---

# Review

## Summary

The note has no numbers, percentages or named studies. Its concrete claims about
llm-do link to the project repository. Its one causal prediction, that separate
invocation surfaces discourage incremental refactoring, is labelled an
expectation rather than an observed result. "A prompt-backed callee often
absorbs loosely phrased ... arguments" is a general behavioural claim. It is
stated as the reason for the coupling risk, not as a measured frequency. The
only unsourced empirical premise is the tool-selection degradation assumed in
the first open question. It is non-specific and sits in a speculative section,
so it is recorded as info.
