---
type: types/review-result.md
findings: []
outcome: pass
description: Controller-only revalidation of retained worker output; no new judgment
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/3419da94374b47ec0349caae/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/3419da94374b47ec0349caae/observation.json
contract-sha256: 5a084df09d1b0de08e2dcd8e2316c8ae5af96860a9ebdfc00fb62dd34597653e
profile:
  harness: claude-code
  launch_model: opus
  effort: medium
  flags:
    allowed-tools: Read,Grep,Glob,Edit(kb/reports/state/review/runs/**),Write(kb/reports/state/review/runs/**)
    disallowed-tools: Bash,NotebookEdit
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T123635Z
launch: 2f43a0778bba491d9f088bec0d3ab58c
completed-at: '2026-11-15T13:09:37.271879+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/2f43a0778bba491d9f088bec0d3ab58c/outputs/review.md
raw-output-sha256: 1951f53bf27f9c8c8ced56c29c7b0e8f3cdf9d1551b948ffad55bc1e28b141e9
format: 2
---

# Review

## Summary

No sentence in the body uses the listed stock patterns ("It's worth noting", "At its core", "The key insight here is", "In other words" restatement) and fails the deletion test.

## Candidates examined

- "The two failure modes are not symmetric, and the rule rides entirely on that." This sentence opens its section and tells the reader that the asymmetry carries the rule. The rest of the paragraph depends on that framing, so deleting the sentence would lose something.
- "A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky." The first half restates the previous paragraph. The sentence still draws the inference from asymmetry to prohibition, which the previous paragraph does not state. It survives the deletion test.
- "It is the general form of 'a cache must never be the only copy' — applied not only to caches but to every derived copy of recomputable truth." This uses a "not only X but Y" construction similar to the elevation move. It still adds content: it relates the rule to a familiar caching maxim and states how far the rule extends beyond that maxim. Deleting it would remove that connection.
- "This looks like it reopens the regress, but it doesn't" (precondition 4). This sentence anticipates an objection and the following text answers it. It is argument, not filler.

None of these sentences can be deleted without losing content.
