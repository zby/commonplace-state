---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This note extends that callable structure to tools. llm-do implements this pattern
  reason: '''This pattern'' may refer to the linked note''s typed-callable structure
    (llm-do as an instance of the prior account) or to this note''s extension of it
    to tools (llm-do as the object to which the current note applies its own contribution).
    The adjacent description of llm-do covers both `.agent` files and Python tools,
    and the closing sentence says the unified interface makes the callable view practical.
    Together these largely settle the reading as the extension. The blur is plausible
    but immaterial to attribution.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/089738397da010cdbb6d8905/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: bcdab9a9707244b8a3b307957cd61085
completed-at: '2026-11-20T11:12:21Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/bcdab9a9707244b8a3b307957cd61085/outputs/review-conceptual-role-conflation.md
raw-output-sha256: ca541c01dffd072000b32c0cf19e0228f5611f13f6ce4788ffeed90afae9ad18
format: 2
---

# Review

## Summary

I inspected the passages that import, apply or extend concepts:

- **Information hiding** is applied to the prompt–code binding. The note then distinguishes ordinary code-to-code hiding from this boundary, so the concept, the prior practice and the new application keep separate roles.
- **The English account** is attributed to the linked note with explicit content: an instruction permits a set of readings, and extraction is a separate intervention. The note's own movement claim follows in a separate sentence.
- **Constraining, codification and relaxing** are applied to the three `ticket_classifier` moves. The note does not redefine them. "Codification as refactoring" applies the concept to one case and does not redefine it.
- **Typed callables:** The note summarizes the prior account with its limitation and states its own contribution as "extends ... to tools". The referent of "this pattern" is slightly loose (INFO), but context resolves it without changing attribution or contribution.

No passage meets the materiality threshold.
