---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/types/note.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/types/note.md
note-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/ef3075ff23e542b2878024e561faad03/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/e460168770f43570d3f5cc29/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: ef3075ff23e542b2878024e561faad03
completed-at: '2026-11-19T13:27:13Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/ef3075ff23e542b2878024e561faad03/outputs/review.md
raw-output-sha256: e6d5fddc3040fb33adfecb94c381af7f7b81fc2ea7b05a5915997932a538117b
format: 2
---

# Review

## Summary

The note does what the `note` type spec's authoring instructions ask. Structural frontmatter checks are left to the validator.

## Writing shape

- **Main claim near the top.** The first paragraph states the mechanism: context isolation loads deep task material and excludes competing work, while global prioritization needs that competing work as its comparison set. The second paragraph narrows the claim to prioritization, not judgment in general. The third gives the claim mode and a refutation condition. Sections that elaborate the claim come after these paragraphs.
- **Title as compressed handle.** The title names both forces and the relation between them, and the body develops exactly that relation. The catalog gates judge whether the title works as a proposition.
- **Links to adjacent notes.** The inline links carry argumentative weight. For example, the intent note supports the claim that static priority rules fail, the summary note explains how compression hides emergencies, and ADR 138 illustrates unbundled stops. The Relevant Notes footer gives each link a relation label and says why it matters, including rival mechanisms marked as contrasts.
- **Design rationale, not imperative procedure.** The execution/triage split is presented as an architectural consequence of the claim, and the Commonplace mechanisms are explicitly scoped as illustrations. The note gives no operating steps.
- **Limits under `## Scope`.** The section states the applicability conditions: bounded context, and a competing workload that does not fit beside task context. It also covers the case where the conflict disappears (small single-thread tasks), the restriction to relational rather than intrinsic checks, the boundary with choosing objectives, and the evidential limit of the cited practitioner account and mechanisms.
- **Open Questions.** The section follows the template and lists unresolved points that track directly to the residual-friction section.

## Description

The description says why a reader would retrieve this note. It names the specific mechanism (isolation removes competing work) and the subtopics (priority flattening, splitting execution from triage). That separates it from nearby notes that treat isolation as enabling focus or verification. It fits in one sentence, as the spec suggests.
