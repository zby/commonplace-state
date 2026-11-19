---
note: kb/theory/a-software-factory-is-family-scoped-lifecycle-production-machinery.md
note-sha256: f4dee748bce52437ff68f4d869d0e6fc751634016e471a7f12b0ccae36fadadd
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: cd19b8152c3a4ddba2bcb9027004f35b
completed-at: '2026-11-12T08:32:21Z'
---
### Summary

The note conforms overall: it states its main distinction near the top, uses a claim-bearing title and a discriminating description, develops transferable design rationale, and links to adjacent notes. It does not follow the required heading convention for known limits.

### Findings

- WARN: The Writing Shape instructions require known assumptions, applicability conditions, and failure cases under `## Scope`. The note has no such section, although `## Evidence limits` explicitly limits what the sources support and how their tooling context transfers. Its opening also bounds the reconstruction to the 2003 and 2007 accounts. These are known limits, so the omission exception does not apply.

### Suggested Revision

Rename `## Evidence limits` to `## Scope` and retain its evidence and transfer qualifications. Include the historical applicability boundary there if needed while preserving the opening definition.

## Result: WARN
