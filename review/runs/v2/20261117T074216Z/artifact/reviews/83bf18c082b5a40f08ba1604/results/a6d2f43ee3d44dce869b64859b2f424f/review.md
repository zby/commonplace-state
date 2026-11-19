---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Consider two hypothetical cases involving a new KB instruction.
  reason: '"KB instruction" assumes the reader knows that a knowledge base here carries
    operational instructions that agents adopt and follow. The cases that follow make
    the role inferable (an agent proposes and adopts it), so the sentence stays understandable;
    a brief gloss such as "a new written procedure the agent follows" would remove
    the residual KB-context dependency.'
  level: info
- scope: passage
  quotes:
  - That assessment creates no human stop in adoption.
  reason: '"Human stop" is coined rather than defined. Its meaning — a point where
    the process halts until a person acts — is inferable from the preceding Required
    approval case ("adopts it only after approval", "Removing that stop") and from
    the opening contrast, so a reader can keep going; an explicit one-clause gloss
    at first use would make the term self-standing.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 9528731444671204248c1c7fed0181134ac72d8ab18a30d0a486df4eae922edd
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/83bf18c082b5a40f08ba1604/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/83bf18c082b5a40f08ba1604/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: a6d2f43ee3d44dce869b64859b2f424f
completed-at: '2026-11-17T07:42:45Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/a6d2f43ee3d44dce869b64859b2f424f/outputs/review.md
raw-output-sha256: 0600544419042537c30a9c46a389b5f5d14d482529646739f09ebe59e7cd8282
format: 2
---

# Review

## Summary

The note's central terms are introduced through their own contrast rather than by link. "Operating process" and "operating dependency" are made concrete in the first paragraph: evaluation the system must wait for before adopting a change versus assessment of an already-adopted change. The two hypothetical cases then work as definitions by example for "required approval" and "non-blocking assessment". "Adoption", "rollback" and "acceptance rules" are ordinary English or standard engineering vocabulary in context.

No active vocabulary term from `AGENTS.md` (constraining, codification, frontloading, program refinement, workshop, and so on) appears in the body. The gloss-and-link requirement therefore has nothing to apply to. The two links point to related claims, and the surrounding sentences paraphrase each one ("the comparison of a system before and after an adopted change", "routine approvals do not establish that human judgment is dispensable"), so the reader does not need to follow either link to understand the sentence.

Two minor points remain. "KB instruction" relies slightly on KB context, and "human stop" is coined without an explicit gloss. In both cases the immediate context lets the reader infer the meaning, so they are recorded as info findings and do not lower the outcome.
