---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Each callable receives only its declared arguments rather than the caller's full
    conversation history
  reason: 'The section headed ''The mechanism'' describes llm-do''s particular design:
    one callable namespace, context isolation through declared arguments, and per-run
    binding chosen by the programmer. The heading presents this as the general mechanism
    rather than as one implementation. Context isolation, for example, is not required
    for caller-invariant swapping. Retitling the section or marking llm-do as an example
    (e.g. ''One implementation: llm-do'') would keep the general claim from appearing
    to depend on llm-do''s choices. Readers can still see that llm-do is a concrete
    instance, and the opening paragraph states the claim independently, so the risk
    is low.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/3351ca9d6f3c322c739dd67e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 4f52c19882c441eea0d54fdb1b33e2de
completed-at: '2026-11-20T11:09:58Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/4f52c19882c441eea0d54fdb1b33e2de/outputs/review-source-residue.md
raw-output-sha256: 213018a67f133f5d08e3ae808dc97e00fd2e1627a810c5d642b6ce45e5c68833
format: 2
---

# Review

## Summary

The title and opening paragraph claim generality: any unified interface over
prompt-backed and code implementations. Most of the specific material is framed
as illustration:

- `ticket_classifier` is introduced with "such as" and a "Suppose the team..."
  scenario.
- llm-do's `.agent` files are introduced with "llm-do implements this pattern".

The one narrower element is the mechanism section. It presents llm-do's specific
runtime choices under a generic heading. This is recorded as info rather than
warn, because the general claim is stated independently and llm-do is
recognisable as an instance.
