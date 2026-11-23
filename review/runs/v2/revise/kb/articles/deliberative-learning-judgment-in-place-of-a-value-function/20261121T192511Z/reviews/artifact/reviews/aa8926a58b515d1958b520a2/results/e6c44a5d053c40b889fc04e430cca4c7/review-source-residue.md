---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - directing design proposals to the right folder and type contract
  reason: '''Type contract'' and the later ''temporary workshop'' are Commonplace-internal
    vocabulary inside an example that is otherwise presented as any deployed agent
    system that maintains a knowledge base. The passage is framed as an illustrative
    case (''Suppose ...''), so this does not overcommit the general claim. An external
    reader may still stop on these undefined terms. Neutral wording, such as ''the
    right folder and document template'' and ''a scratch area for in-progress work'',
    would keep the example generic.'
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/aa8926a58b515d1958b520a2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: e6c44a5d053c40b889fc04e430cca4c7
completed-at: '2026-11-21T19:26:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/e6c44a5d053c40b889fc04e430cca4c7/outputs/review-source-residue.md
raw-output-sha256: f48db72b5ac754e6e1144d2d868b83c2a45554029e08df5232faa4a24daecdf9
format: 2
---

# Review

## Summary

The title and opening claim generality: deliberative learning is presented as a
learning paradigm for any system that edits a readable, addressable store.
Material specific to Commonplace is explicitly framed:

- "Our knowledge base defines ..." is attributed.
- "as Commonplace currently is" marks the bootstrap condition as applying to
  this project.
- The current-evidence paragraph names Commonplace.
- The companion drafts are labeled as the narrower theory-builder special case.

The routing-line example is introduced as an illustration, so it is an
illustrative case and not residue. It is marked "Suppose ..." and set in "a
deployed agent system". Only a little internal vocabulary leaks into that
example. This is recorded as INFO because it affects readability, not the scope
of the claim.
