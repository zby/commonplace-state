---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - low-quality memory before promotion
  reason: '''Promotion'' presupposes a staging-then-promote lifecycle for memory artifacts,
    which is a feature of particular KB workflows rather than of agent memory systems
    in general. The note''s body never introduces a staging step, so the term reads
    as carried over from a narrower setting. ''Before it is adopted as memory'' or
    ''before it is written to its destination'' would keep the check general; alternatively,
    mark promotion as one possible gating step.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/agent-memory-requirements/create-memory-directly.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: fe3aada7aec4ce0d85e704be3bf70dc5d6242099ac82171dd77187fb75b4e33f
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/5ecc1e4d5e5bedef563c18a4/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/5ecc1e4d5e5bedef563c18a4/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: 54cefad7f5054b03af35095f608473c9
completed-at: '2026-11-16T11:25:02Z'
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/54cefad7f5054b03af35095f608473c9/outputs/review-source-residue.md
raw-output-sha256: 1af2f3da0abcea1eee282b4fc9c8e86caff55896f4402c1677f5b91df6c8e90f
format: 2
---

# Review

## Summary

The title and opening paragraph claim generality across agent memory systems: any system where understanding arises during work and could be written as a durable artifact. The body mostly stays at that level. Its artifact kinds (notes, decision records, skills, runbooks, validators, plugins) are presented as an open list of destination types, not as one system's inventory. "Representational form" and "authority path" are linked to the axes note that defines them, so they are framed as the note's own analytical vocabulary rather than leaked residue.

The one term that assumes a narrower workflow is "promotion" in the evaluation questions; it is minor and recorded as informational.
