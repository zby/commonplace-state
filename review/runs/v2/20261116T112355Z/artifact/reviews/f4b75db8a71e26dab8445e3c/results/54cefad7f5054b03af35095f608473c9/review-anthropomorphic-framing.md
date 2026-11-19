---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - understanding is already available during work
  - while understanding was live
  - structure the agent already had
  reason: 'The note grounds its central efficiency claim in the agent''s ''understanding''
    and in structure the agent ''had'', which attributes a held mental state to the
    agent. The mechanism the note actually uses is technical: the relevant context,
    provenance and caveats are present in the agent''s working context and are lost
    once that context ends. The note does not argue about cognitive status, so ''when
    the needed context is already loaded during work'', ''while that context was still
    loaded'' and ''structure already present in the working context'' would state
    the claim without implying internals it does not defend.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/agent-memory-requirements/create-memory-directly.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: fe3aada7aec4ce0d85e704be3bf70dc5d6242099ac82171dd77187fb75b4e33f
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/f4b75db8a71e26dab8445e3c/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/f4b75db8a71e26dab8445e3c/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 54cefad7f5054b03af35095f608473c9
completed-at: '2026-11-16T11:25:01Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/54cefad7f5054b03af35095f608473c9/outputs/review-anthropomorphic-framing.md
raw-output-sha256: b292d01d277850dcada0e800eedc0e55594d186f16593c5ad92f3923f65d868c
format: 2
---

# Review

## Summary

The note mostly uses technical language: it speaks of context, provenance, caveats, artifacts, routing and validation. Its load-bearing condition, however, is phrased as the agent's "understanding" being "available" or "live", and as "structure the agent already had". Those phrases attribute a persistent mental state to the agent. The note's own wording in the same paragraph ("while the relevant context, provenance, and caveats are still live") shows that the intended mechanism is the content of the working context, so the cognitive phrasing is replaceable without loss.

Other agent references ("help the agent choose", "Can a future agent find and apply the artifact", "An instruction can steer behavior") are ordinary descriptions of tool use and system behaviour and are not flagged.
