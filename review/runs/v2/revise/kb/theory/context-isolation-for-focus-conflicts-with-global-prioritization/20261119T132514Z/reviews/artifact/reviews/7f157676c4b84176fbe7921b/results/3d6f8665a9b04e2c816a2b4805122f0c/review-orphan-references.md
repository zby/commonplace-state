---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/prose/orphan-references.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/prose/orphan-references.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 46af38b99bcdcea724a141b921ecacd0f1362d48353bd1beec126e0dc7d4309a
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/7f157676c4b84176fbe7921b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 3d6f8665a9b04e2c816a2b4805122f0c
completed-at: '2026-11-19T13:26:47Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/outputs/review-orphan-references.md
raw-output-sha256: 329b61d15f57f721b92cccacaaf6123b68c877bbf0ce99be8097bf2434460b9d
format: 2
---

# Review

## Summary

The note contains no numbers or figures. Its concrete empirical material is
the practitioner account and the Anthropic write-up quoted within it.

- Each Nostalgebraist quotation is linked to the tracked ingest and marked
  verbatim. The linked ingest retains the quoted passages with snapshot
  provenance and the URL of the Anthropic write-up. A reader can therefore trace
  the second-hand Anthropic quotation through the cited source.
- The note gives local context for how to read this material: it says the
  account "motivated this analysis" and that the account "does not isolate
  whether worker behavior or a workflow ... made interruption the default". The
  Scope section says these sources supply origin, not a controlled comparison.
  The evidence is therefore not presented with more specificity than the note
  can support.
- ADR 138, the traversal-logging note and the unresolved frontier are linked
  internal mechanisms, and each comes with a one-line description of what it
  does.

The note gives the human specialist's "ambient cross-project model" as a
reasoned contrast, not as an empirical finding that would require a citation.
