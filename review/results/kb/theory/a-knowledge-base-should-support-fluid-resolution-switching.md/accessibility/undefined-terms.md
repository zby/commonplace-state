---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 98a5f8cfffdf4b047e30b99e468369884adceced7c1678bd3b8b267a7b309283
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: 9cecc704cfd84bf685c4cfca7b890d03
completed-at: '2026-11-16T22:29:07Z'
findings:
- scope: passage
  quotes:
  - without reducing the connection to an untyped jump
  reason: '"Untyped jump" draws on the idea of typed links, but the note never says
    what typing means. A reader can roughly infer "a link whose relation is unstated"
    from the preceding sentence about why the target matters. A short gloss such as
    "a bare jump that states no relation" would remove the guesswork.'
  level: info
contract: verdict
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/041abad49b79fb3e7e6c8fee/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/041abad49b79fb3e7e6c8fee/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/9cecc704cfd84bf685c4cfca7b890d03/outputs/review-undefined-terms.md
raw-output-sha256: 1fdb3b8fdcf49e6f671f907f924c9f0b028ea38f64a71cc4ccc98f01419a8085
---

# Review

## Summary

The note defines or glosses its technical terms where they first appear.
"Resolution-switching" and "resolution" are defined in the opening paragraph.
"Resolution-switching fluidity" is defined in the sentence that introduces it.
"Addressability grain" gets an inline gloss: "the smallest amount one access
path can retrieve for a matched target". The opening explanation of
"progressive disclosure" defines it as a cost gradient from cheaper pointers to
more expensive views. "Pointer" can be read from that list of titles,
descriptions and link phrases. "Title-as-claim" is preceded by "A claim title
carries the assertion". "Bidirectional navigability" restates the earlier
"inexpensive in both directions".

None of the active vocabulary terms declared in `AGENTS.md` appears in the
body. "Context engineering" appears only as a frontmatter tag, and "discovery"
is used in its ordinary sense. The only borderline term is "untyped jump". Its
meaning can be inferred from context, so it is recorded as an INFO finding.
