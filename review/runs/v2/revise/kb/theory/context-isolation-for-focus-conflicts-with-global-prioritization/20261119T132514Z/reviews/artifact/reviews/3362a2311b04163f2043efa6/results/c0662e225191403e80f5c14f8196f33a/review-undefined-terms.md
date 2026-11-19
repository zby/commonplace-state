---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - compounding the oracle asymmetry analyzed in
  reason: '"Oracle asymmetry" is a KB-specific concept used without a gloss. Only
    the link explains it, so a reader cannot tell what is asymmetric (for example,
    that tests reward a present guard but cannot penalize an unneeded one) without
    following it. Add a short inline paraphrase.'
  level: warn
- scope: passage
  quotes:
  - misclassify severity under unsafe substitution
  reason: '"Unsafe substitution" comes from the linked summary note and is not defined
    here. The sentence depends on it, but the reader cannot infer that it means acting
    on a summary as if it were the source when the summary lacks the needed detail.
    Gloss it inline.'
  level: warn
- scope: passage
  quotes:
  - intent, tolerances, concern depth, or budget
  reason: '"Concern depth" appears once, in a list of compressed priority proxies,
    with no definition or context that makes its meaning inferable. The other list
    items are plain language. Define it or replace it with a plain description.'
  level: warn
- scope: passage
  quotes:
  - consistent with [bounded-context orchestration](./bounded-context-orchestration-model.md)
  reason: The bounded-context orchestration model is invoked only by a link. The surrounding
    sentence partly conveys the idea (separate bounded calls with an interface between
    them), so the reader can follow. A brief gloss would still help.
  level: info
- scope: passage
  quotes:
  - recorded on a discoverable surface or in a typed stop record
  reason: '"Discoverable surface" and "typed stop record" are KB-internal phrasings.
    Context makes them roughly inferable (a place a later pass can find, and a structured
    record of why a run stopped), but a short gloss would remove the guesswork.'
  level: info
- scope: passage
  quotes:
  - 'Claim mode: universal'
  reason: '"Claim mode" is a KB convention without a gloss. The stated conditions
    and refutation criteria that follow make its practical meaning inferable, so this
    is minor.'
  level: info
- scope: passage
  quotes:
  - '[ADR 138](../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md)
    unbundles'
  reason: The acronym ADR is not expanded (architecture decision record). The sentence
    describes what the record decides, so the reader can still follow it.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/3362a2311b04163f2043efa6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: c0662e225191403e80f5c14f8196f33a
completed-at: '2026-11-19T13:26:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/outputs/review-undefined-terms.md
raw-output-sha256: 2d63a0ee1cb95fd5bda8734b3f272d13754fe3e7bcdd3c34c179775884051047
format: 2
---

# Review

## Summary

The note defines its central terms well. "Context isolation" and "global prioritization" are each defined in the sentence that introduces them. "Narrow-deep" and "wide-shallow" are defined by their function. "Scale-bearing local facts" comes with concrete examples. The active vocabulary term "unresolved frontier" has both a link and an inline gloss.

The warnings concern three borrowed concepts whose meaning sits only behind a link or is not given at all. "Oracle asymmetry" and "unsafe substitution" both come from linked notes. "Concern depth" is used without any definition. Each appears in a sentence whose force depends on the term, so a reader without KB context loses part of the argument there. The info findings mark KB phrasings the surrounding context mostly recovers.
