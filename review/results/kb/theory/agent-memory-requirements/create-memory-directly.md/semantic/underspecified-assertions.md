---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/agent-memory-requirements/create-memory-directly.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/agent-memory-requirements/create-memory-directly.md
note-sha256: fe3aada7aec4ce0d85e704be3bf70dc5d6242099ac82171dd77187fb75b4e33f
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
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
  - When current work reveals a stable claim, procedure, policy, index entry, validation
    rule, or tool extension, the natural operation is to write the useful artifact
    while the relevant context, provenance, and caveats are still live.
  reason: 'The trigger condition ''stable'' leaves a threshold unresolved, and the
    threshold decides when the requirement applies. Reading A: stable means the working
    agent judges, within the current session, that the lesson will not change. Then
    direct creation covers most in-session insights. Reading B: stable means corroborated
    beyond the single episode, for example by recurrence or validation. Then many
    lessons should wait, and that pushes them toward the later trace-extraction path
    the note contrasts itself with. The choice changes the recommended intervention:
    write now or defer. It also changes the evidence needed to justify a write. The
    note''s own failure example, ''A check can fossilize a temporary workaround'',
    shows that stability judgments matter, but nearby context does not say which threshold
    applies.'
  level: warn
contract: verdict
target-sha256: cc1a3803800712b9e251cb1f6c948e31f777af92c4d633bc4f6ee2944280bbea
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/0ac9ddf48da4bc1eedbd18b8/inputs/target/kb/theory/agent-memory-requirements/create-memory-directly.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/0ac9ddf48da4bc1eedbd18b8/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/46f7e46ad52a4cef93827df87f98030b/outputs/review-underspecified-assertions.md
raw-output-sha256: 2e5f5ad571226318803e4bfd7fce3af0455e46e6f937f76e5d0c53e8d87a2092
---

# Review

## Summary

Most load-bearing assertions are resolved by nearby context:

- "Context-efficient" names its comparison in the next sentence: later trace extraction and its rediscovery cost.
- "Creation contract" is explained by the preceding sentence: the right artifact shape and quality contract at write time.
- The closing criterion, "useful future context or useful future behavior," is broad but exact.

The unresolved choice is the stability threshold in the opening trigger. That sentence decides when an agent should create memory directly instead of deferring. Under one reading the requirement covers almost every in-session insight. Under the other it covers only corroborated lessons and hands the rest to later extraction. The gate does not choose between these readings. The author may define the threshold, narrow the trigger, or state that the in-session judgment is meant.
