---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:58Z'
findings:
- scope: passage
  quotes:
  - Ordinary information hiding swaps two implementations that share the same execution
    substrate and caller model
  reason: This section opening repeats the opening paragraph's contrast ('Unlike ordinary
    code-to-code information hiding ... this boundary crosses two different execution
    regimes ... so the abstraction leaks asymmetrically'). The opening states it as
    a thesis; the section develops it and leads into the two bullets, so the paragraph
    cannot be deleted outright. This is setup followed by development, which is a
    weak signal.
  level: info
- scope: passage
  quotes:
  - Moving code back to a prompt behind an unchanged call site works only where the
    caller's latency budget, cost budget, and error handling can absorb model execution
  reason: 'The Scope bullet repeats the closing paragraph of the previous section
    (''call sites that may move back to prompts must be written for fallible, higher-latency
    calls''). The two sit at a section boundary in different roles: one is a prescription,
    the other a scope limit. The bullet adds the examples of tight inner loops and
    deterministic paths, so the overlap is partial.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/883addfafe15da25be1b25d7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-redundant-restatement.md
raw-output-sha256: fe3d7265efbd37a5319d2df0503aad1f74f5f86f7762fbd10731ff121783d548
---

# Review

## Summary

No section opens with a full re-explanation that could be deleted, and no
closing paragraph previews a later section's enumeration in full.

- "The mechanism" opens with new content: the llm-do runtime.
- "Scope" opens directly with its bullets.
- "Why this matters for constraining" opens with the friction argument that
  separate invocation surfaces create, which is new.
- "The connection to typed callables" opens by summarising the linked note,
  which is new to this note.

Two partial overlaps sit at section boundaries. Both are setup-plus-development
or prescription-plus-limit pairs, so they are recorded as info. The opening
paragraph also previews the three swap moves in one sentence, but that is a
thesis sentence, not a paragraph at a section boundary, and the gate does not
flag it.
