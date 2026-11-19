---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: bc277cf6d61d4be6914a3ce31a323912
completed-at: '2026-11-16T22:32:02Z'
findings:
- scope: passage
  quotes:
  - its role is to preserve the task-relative relationship across the transition
  - the navigational value of
  reason: 'The linked note claims that a link''s position and introducing prose encode
    its commitment level, producing a weighted graph. It gives that graph''s navigational
    use as traversal priority: follow strong links before weak ones. This note presents
    bearing preservation during a change of scope as ''the navigational value'' of
    that encoding. The target''s table of relationship words does say that prose tells
    the reader what role the linked note plays, so the support is plausible. The transfer
    from commitment strength and traversal priority to preserving the relationship
    across a scope transition is not articulated, and ''the navigational value'' also
    claims more than the target''s own account of it.'
  level: warn
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/c3fbc67b07fd561c12c17560/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/c3fbc67b07fd561c12c17560/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/bc277cf6d61d4be6914a3ce31a323912/outputs/review-grounding-alignment.md
raw-output-sha256: 557a3d53d46ae527ec804c1b07323541db25cc98e82eff4486b5679dead8258a
---

# Review

## Summary

All links resolve to library notes in `kb/theory/`. Each was checked by reading its title and opening.

- **Title as claim enables traversal as reasoning.** The target says claim titles make the first disclosure layer usable, so agents can choose what to load. This supports "a reader can inspect a chain of assertions before choosing which bodies to load." Aligned.
- **Link-following and search impose different metadata requirements.** The target contrasts local steps that carry source context with long-range search that lacks it. The note uses the target only to say that both routes can take part in a switch. Aligned.
- **Link strength is encoded in position and prose.** This is a modest extension that is not articulated (WARN above).
- **Pointer design tradeoffs in progressive disclosure.** The target names exactly the four axes the note cites. It describes pointers "at increasing resolution", with cheap ones scanned first, which supports the cost gradient. Aligned.
- **Recognition, not linking, is the hard problem.** The target makes recognition the expensive step and requires co-presence. The note claims only that switching helps assemble views and "does not perform the recognition". Aligned and appropriately bounded.
- **Footer links.** These comprise agents-navigate, addressability grain and end-to-end evaluation. The note's one-sentence paraphrase of grain ("the smallest amount one access path can retrieve for a matched target") matches the target's definition. The other footer relations are adjacent and make no stronger support claim.

The only issue is the link-strength attribution.
