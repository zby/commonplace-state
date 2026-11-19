---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 5e0a1652cc48c71af3b9ec8a9adcaf2accca0686e05038e3e65e84efddfef63f
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: b2930f2198c00862677777da136d1e12e0ca38fede54784dff8f6b211ee73963
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: e5467b4dc521477e9424a83f9c7fa6ed
completed-at: '2026-11-12T08:23:13Z'
---
### Summary

The body supports a workshop layer for knowledge bases that support ongoing workflows. The H1 broadens this conditional design claim into a requirement for any functioning knowledge base.

### Findings

- WARN: The H1, “A functioning knowledge base needs a workshop layer, not just a library,” makes workshop support a condition of functioning at all. The body instead says the current separation “is fine for now” because the system is primarily a knowledge base, and locates the design need in “when we want to build a knowledge base that supports real workflows.” Its argument establishes the need to handle temporal work and bridge it to durable knowledge when workflow support is in scope; it does not establish that a library-focused knowledge base cannot function without that layer.

### Suggested Revision

Narrow the H1 to “A knowledge base that supports ongoing workflows needs a workshop layer.” This preserves the central claim while carrying the body’s scope condition into the title.

## Result: WARN
