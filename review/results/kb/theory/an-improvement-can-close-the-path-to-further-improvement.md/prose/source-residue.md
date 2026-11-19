---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 0366cb851ef44475ed808292e3919e8d5559c86b5d72261a6cdd8d5c82ee0aab
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: da2abf58c95c467aa546b90132222627
completed-at: '2026-11-17T07:22:33Z'
findings:
- scope: passage
  quotes:
  - Conversely, keeping the old files does not preserve the capability if the successor
    no longer permits or consumes their changes.
  reason: This sentence is in the general section on non-regression, but 'old files'
    comes from the hypothetical agent's file-based instructions. Outside the example,
    the general point is that keeping the old components or artifacts does not preserve
    the capability. The residue is mild because the preceding paragraph ties it back
    to the example.
  level: info
- scope: passage
  quotes:
  - A maintainer may restore a path that the agent itself no longer has.
  reason: The Scope list states general limits for 'a system', but this bullet uses
    the example's 'agent'. 'The system itself' would match the opening's claimed generality.
    This is minor because agent systems are the KB's primary domain.
  level: info
contract: verdict
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/667fce3d82f6bcc75fc2879a/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/667fce3d82f6bcc75fc2879a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/da2abf58c95c467aa546b90132222627/outputs/review-source-residue.md
raw-output-sha256: f0aac178f28cbbb8ce7e965b08a1accf50f52af74a8d3e794e8673fa80880851
---

# Review

The title and opening state the claim for any system that improves itself: "A system can improve at its current work while losing the ability to improve itself again." The agent-specific vocabulary (instruction changes, files, maintainer) is introduced inside an example that is explicitly marked "Consider a hypothetical agent", so most of it is framed correctly.

Two phrases carry the example's vocabulary into general statements, as recorded in the findings. Neither commits the claim to file-based agents. Each one reads as a loose reference back to the example, so both are INFO.
