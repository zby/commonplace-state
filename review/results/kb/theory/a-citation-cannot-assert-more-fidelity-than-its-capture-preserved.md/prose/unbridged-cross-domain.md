---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/unbridged-cross-domain.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion: kb/instructions/review-gates/prose/unbridged-cross-domain.md
criterion-sha256: 5f22f140a9b058b4c1ec8918857159da174cbb456c8294d47fa56c0f0021ec7f
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 304ff2b910374d728798b623f2a4a074
completed-at: '2026-11-18T16:02:23Z'
findings: []
contract: verdict
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/b343c87ef1efcaf6b20da2d2/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/b343c87ef1efcaf6b20da2d2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/304ff2b910374d728798b623f2a4a074/outputs/review-unbridged-cross-domain.md
raw-output-sha256: 9138fbbaf74928ab29e253cb10abad2e795a25d362ecdeae92e2ad1d5b183e8d
---

# Review

## Summary

The note cites one empirical result: the casebook-corpus mismatch profile, cited through ADR 046. According to the linked ADR, it came from a prototype run of the same quote check over a sibling casebook corpus. The evidence is therefore about quotation alterations caught by a wording check, and the note uses it to argue that permissive normalization would hide real alterations. Source and argument share a domain: both concern exact quotations checked against source text. The mechanism, editorial alterations producing string differences, does not depend on what the corpus is about, so no bridge is needed.

The remaining citations (ADR 073 and ADR 094) are design decisions about the same checking problem, not evidence from another domain. The Scope section explicitly says that transfer beyond agent-operated KBs rests on reasoning, not on external evidence. That is the disclosure the gate asks for when evidence does not cover the claimed reach.
