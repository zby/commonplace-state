---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Three mechanisms in Commonplace illustrate this split at different scales
  reason: Commonplace is named as the home of the three illustrative mechanisms, but
    its first mention does not say what it is. A later possessive ("Commonplace's
    discoverable field of possible further work") and the phrase "local design examples"
    only hint at it. A reader outside this KB cannot tell that it is the agent-operated
    knowledge-base framework the note belongs to. Add a brief inline identification
    at first mention.
  level: warn
- scope: passage
  quotes:
  - the various [Claudes] also do that
  reason: Inside the quotation, the bracketed "[Claudes]" refers to agent instances
    by product name without saying what Claude is. The surrounding sentence mentions
    an Anthropic write-up about coding agents, so the meaning is inferable. Saying
    in the lead-in that Claude is Anthropic's model would remove the gap.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/accessibility/unidentified-references.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/accessibility/unidentified-references.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 422847c587793f494bfa140e10c46772cc1decaf72d3a611ec83daa39da288c3
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/72b2319b10f51069147aaebc/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: c0662e225191403e80f5c14f8196f33a
completed-at: '2026-11-19T13:26:27Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/c0662e225191403e80f5c14f8196f33a/outputs/review-unidentified-references.md
raw-output-sha256: 9f5f189648db43b8896da7a0d84254b26e340b35c7697163aff2e11470a502e6
format: 2
---

# Review

## Summary

Most named references are adequately identified. Nostalgebraist is introduced as the author of "a practitioner account that motivated this analysis", which says what kind of source it is. The Anthropic material is identified as "a public Anthropic write-up about internal coding-agent use". ADR 138 is cited with an inline description of what it decides.

The main gap is Commonplace. The note uses the name as the setting for its illustrative mechanisms but never says, at first mention, that it is the KB framework the note belongs to. A reader who reaches the note from outside the KB would not know what kind of system it is. The bracketed "[Claudes]" in the quotation is a minor, inferable gap.
