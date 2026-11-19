---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - When a wide-shallow pass selects from compressed summaries, items with crisp scope
    and easy checks can look cleaner than messy, high-stakes bottlenecks, tilting
    allocation toward tractable low-value work.
  reason: The tractability-bias bullet is a side hypothesis about how any summary-based
    selector behaves. It does not depend on context isolation, the note gives it no
    mechanism or evidence, and it widens the note's attack surface. The third open
    question already states the same concern as a question. Remove the bullet and
    leave the open question, or rehome the bias as its own lead. Unlike the other
    residual-friction bullets, it does not bound the split's claim.
  level: warn
- scope: passage
  quotes:
  - Crucially, this split unbundles three decisions that naive agent workflows collapse
    into one
  reason: 'The stop/survive/act unbundling introduces a second cause of manufactured
    urgency: workflow bundling ''even when the worker''s local judgment is sound''.
    That cause is independent of missing comparison context. It links to the earlier
    claim that defaults set the failure direction, and ADR 138 illustrates it, so
    it may earn its place. Still, ''Crucially'' gives it more weight than the main
    isolation claim. Either compress it to a sentence tied to the failure-direction
    default, or move it to a separate note on decision bundling in stop workflows.
    Where it should go is unclear.'
  level: info
- scope: passage
  quotes:
  - Local over-specification.
  reason: The third manifestation has no source support. It leans on a different mechanism,
    test-oracle asymmetry from the linked guard note, which the footer marks as a
    contrasting rival mechanism. Because the bullet 'compounds' that mechanism, it
    is unclear how much of the over-guarding it attributes to missing comparison context.
    It could stay as a short boundary contrast or be cut to a link. Its role is unclear
    rather than clearly harmful.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/587ce601c4a34d20b598a27b1ca7240a/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/29f876796d63c0dbb13ffd98/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 587ce601c4a34d20b598a27b1ca7240a
completed-at: '2026-11-19T13:27:46Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/587ce601c4a34d20b598a27b1ca7240a/outputs/review.md
raw-output-sha256: 20ab9e870644533c5b39cebb086a08774773db6ded02c8dd714f6bdbdc772cef
format: 2
---

# Review

## Summary

The note's main claim is that isolating an agent's context for task focus removes the live comparison set that global prioritization needs. The description also commits the note to explaining priority flattening and the trade-off in splitting execution from triage. The opening, the failure-direction section, the critique of standing rules, the two-view split, and the Scope section all support that claim. Two of the residual-friction bullets also support it: "compression hides emergencies" and "within-episode micro-prioritization" bound where the split stops working.

One branch needs action. The tractability-bias bullet is a separate hypothesis about compressed-summary selection in general. It has no tie to context isolation and no support, and the third open question already repeats it. Leaving it only as that open question would remove the redundancy and protect the main argument.

Two branches have unclear roles. The three-decision unbundling is introduced with "Crucially" but describes a workflow-bundling cause of urgency that does not depend on isolation. The local over-specification bullet relies on a rival mechanism the note itself marks as contrasting. Both could stay if they were tightened into short bounds on the main claim, or they could be rehomed. The criterion does not settle which.
