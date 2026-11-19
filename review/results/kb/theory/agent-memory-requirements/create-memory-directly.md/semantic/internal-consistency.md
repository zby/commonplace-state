---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/agent-memory-requirements/create-memory-directly.md
note-sha256: fe3aada7aec4ce0d85e704be3bf70dc5d6242099ac82171dd77187fb75b4e33f
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 46f7e46ad52a4cef93827df87f98030b
completed-at: '2026-11-16T11:25:30Z'
findings:
- scope: passage
  quotes:
  - Direct memory fails when it becomes generic capture rather than a role-specific
    artifact. A note can be accurate but hard to find. An instruction can steer behavior
    incorrectly. A check can fossilize a temporary workaround.
  reason: 'The section''s lead sentence names generic capture as the failure. Each
    following example, however, is a role-specific artifact (a note, an instruction,
    a check) that fails for a different reason: findability, wrong guidance, or premature
    hardening. The section closes with a broader criterion (''good only when it becomes
    useful future context or useful future behavior''). The examples fit that closing
    criterion better than the lead sentence. This is likely drift rather than outright
    contradiction, because ''fails when'' can be read as one sufficient condition.
    A human should confirm whether generic capture is meant as the failure mode or
    as one of several.'
  level: info
contract: verdict
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/52a5ed3eae8da73826636f03/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/52a5ed3eae8da73826636f03/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/46f7e46ad52a4cef93827df87f98030b/outputs/review-internal-consistency.md
raw-output-sha256: f3fbda44ddb1bc3a92c906e150fa3583b98eb22c16c868524765a05b160b366b
---

# Review

## Summary

Key claims:

- The opening says direct creation is the context-efficient path when understanding is live, and that it is not blank-page writing: destinations expose creation contracts.
- Methods lists destinations and write-time support. This is consistent with the "not blank-page" claim and the opening's artifact kinds.
- Failure Modes gives a framing sentence, three examples and a closing criterion.
- The Evaluation Questions match the opening (live context and provenance), the creation-contract claim (validation before promotion), and the closing criterion (a future agent can find and apply the artifact).

No pairwise contradiction appears. Key terms do not drift between sections. The one tension is inside Failure Modes: the lead sentence frames failure narrowly, while its examples and closing line frame it broadly. It is recorded as INFO for human confirmation.
