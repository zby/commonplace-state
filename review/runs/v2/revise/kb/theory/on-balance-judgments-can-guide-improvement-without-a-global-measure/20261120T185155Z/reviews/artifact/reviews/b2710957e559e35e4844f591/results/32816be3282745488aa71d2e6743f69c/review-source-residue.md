---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 98643ed5cb9f96c25b62fc1fb6f075494b25c507e49ef7a7b4c51343a115fa7f
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 010b6595056ba8f2bc32a244120b52e4c464357f17cbe7d3fede758464f8391b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/artifact/reviews/b2710957e559e35e4844f591/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews
launch: 32816be3282745488aa71d2e6743f69c
completed-at: '2026-11-20T18:53:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure/20261120T185155Z/reviews/calls/launches/32816be3282745488aa71d2e6743f69c/outputs/review-source-residue.md
raw-output-sha256: 79124d2c646fe46c9e07134e08ae67954688e9cde10c5c06c34f7fb0c859ed72
format: 2
---

# Review

## Summary

The title and description state a general claim about judging improvement. The note uses two narrower domains, Python releases and library opening hours, and frames both as illustrations:

- **Python examples.** The opening poses the Python question and introduces the text-handling example with "Consider". The 3.11 section is explicitly titled "A release judgment". It also says "These checks give reasons for the judgment, not a survey".
- **Library case.** The library case is marked "This is a hypothetical case" and is followed by an explicit statement of what transfers to a KB decision.

"What analysis can settle" continues to use interpreter, timing and dependency vocabulary. Those sentences instantiate general points that the section states abstractly ("deciding whether the saving is worth someone else's porting effort is a judgment about value"; "investigate an unknown only if a plausible answer could reverse the choice"). The vocabulary works as an illustration, not as leaked framing.

The Commonplace sections state their objective in KB terms. No domain-specific framing overcommits the general claim.
