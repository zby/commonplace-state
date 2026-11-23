---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 96c4eea5828c4089a10b19a54bdfd799
completed-at: '2026-11-20T09:44:59Z'
findings:
- scope: passage
  quotes:
  - 3. **Codify** — extract `sanitize_filename()` to Python. The agent still handles
    ambiguous cases. The call site doesn't change.
  reason: The mechanism section says one name resolves to either a neural or a symbolic
    implementation. Step 3 instead splits the work between a newly named function
    (`sanitize_filename()`) and the agent that remains. Either the call site now targets
    a different name, which contradicts 'the call site doesn't change', or the agent
    calls the function internally, so the agent keeps the call site and no swap happens
    at the caller. The text does not settle which, so the step may be inconsistent
    with the dispatch model it illustrates.
  level: info
- scope: passage
  quotes:
  - 4. **Extend via relaxing** — new requirements emerge (handle Unicode, detect dates).
    Add an LLM call for the new cases.
  reason: Elsewhere 'relax' means moving rigid code back to an LLM, replacing the
    code (opening paragraph, and the test-run example). Here it means adding an LLM
    call beside existing code for new cases. This is likely drift in the term's meaning
    that needs author confirmation.
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/0ef65192040044cefc37ea2d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/96c4eea5828c4089a10b19a54bdfd799/outputs/review-internal-consistency.md
raw-output-sha256: b1440d24de15b0809c8d661a2a234f462a1b46b2b69a002e65851d19c8a223cb
---

# Review

Key claims by section:

- **Opening:** a unified interface makes the boundary movable, so refactoring is local.
- **Mechanism:** name-based dispatch lets one name resolve to either kind of implementation, and each link can be refactored independently.
- **Constraining:** without unification each codification step breaks call sites; with it, the four-step progression keeps call sites stable. The routing-rule example keeps the name and the label set fixed while switching to a prompt.
- **Scheduler:** imperative Python makes neural/symbolic refactoring use ordinary refactoring moves.
- **Typed callables:** both kinds of component have defined interfaces.

I found no direct pairwise contradiction. Two passages show likely drift that needs confirmation:

- Step 3 does not fit cleanly with one-name-one-implementation dispatch.
- "Relaxing" shifts between replacing code with an LLM and supplementing code with one.

There is no compressed summary for the body to mismatch. The description matches the body.
