---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A classifier that returns the same queue labels can still route a ticket to a
    different queue
  reason: '''Returns the same queue labels'' plausibly reads as ''returns the same
    label for each ticket'', which contradicts ''route a ticket to a different queue''.
    The intended reading is ''draws from the same label set'' or ''has the same output
    vocabulary''. Something like ''A classifier with the same set of queue labels
    can still route a ticket to a different queue'' removes the conflict.'
  level: warn
- scope: passage
  quotes:
  - an agent combines its own system prompt with that declared signature
  reason: '''That declared signature'' has no prior antecedent; the preceding clause
    mentions ''declared arguments''. A reader may wonder whether the agent receives
    the signature or the argument values. The intended reading is recoverable, so
    this is minor.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/0babc055454f477eb0eb488d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-parsing-ambiguity.md
raw-output-sha256: 24bb591e6205cf891e723ca9aa50f4bd4cf8645c49052d6bcabc541d6b6fe2bc
format: 2
---

# Review

Most sentences have a single natural parse. "Call boundaries must enforce schemas before codification" attaches its time phrase as intended, because the preceding bullet establishes the timing. Pronouns and "that boundary" in the opening paragraphs resolve to the prompt–code boundary.

One sentence in Scope has a plausible unintended reading. "Returns the same queue labels" first reads as identical outputs, which makes the rest of the sentence self-contradictory. Stating that the label set is unchanged removes the ambiguity.

A minor antecedent gap in "The mechanism" ("that declared signature" after "declared arguments") is recorded as info.
