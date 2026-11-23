---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Unmet Traits instruction: the note cites external material outside the
    project (Kirsch''s essay at https://www.blackhc.net/essays/future_of_software/,
    linked both in the body and as evidenced-by in Relevant Notes), but frontmatter
    declares only `traits: [title-as-claim]` and omits `has-external-sources`, leaving
    external-source semantic review unrouted.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/types/note.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/types/note.md
note-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/ddc8542cd7614969a112d9371bb4d5e3/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/c36d07b734c33d44c91303d3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: ddc8542cd7614969a112d9371bb4d5e3
completed-at: '2026-11-20T14:59:03Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/ddc8542cd7614969a112d9371bb4d5e3/outputs/review.md
raw-output-sha256: 68d4a9b6cc6b2187f2db8546ed4430e39095b40fca16a91328493ef81ae561aa
format: 2
---

# Review

## Assessment

The note conforms overall to `kb/types/note.md`: it presents a transferable theoretical claim with a compressed prose title, places the main claim and mechanism in the opening sections, keeps design rationale out of imperative procedure, links to adjacent notes with stated relationships, and separates its assumptions and boundary conditions into a dedicated `## Scope` section.

Its one type-conformance gap is in trait routing. Because `kb/types/note.md` uses `traits` to route semantic review rather than structural validation, declaring `has-external-sources` is needed whenever a note cites material outside the project; adding it brings the note into full conformance with the type spec.
