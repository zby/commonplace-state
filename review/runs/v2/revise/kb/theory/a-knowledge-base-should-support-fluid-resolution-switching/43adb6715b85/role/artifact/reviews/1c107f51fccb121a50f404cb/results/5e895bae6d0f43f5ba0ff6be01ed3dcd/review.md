---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Titles, descriptions, contextual link phrases, generated summaries, and full bodies
    can form a cost gradient
  reason: 'SUPPLIED — kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md
    — needs the note to treat pointer tiers as a gradient of views that resolution-switching
    moves along (its footer: ''the tier structure defines the resolution gradient;
    query-time computation could fill gaps dynamically''). The note''s progressive-disclosure
    paragraph names the tiers as a cost gradient of intermediate views, includes generated
    summaries as one tier, and defers the trade-offs back to the pointer note.'
- scope: passage
  quotes:
  - A claim title carries the assertion. A description adds a fixed routing cue. The
    body supplies the mechanism, qualifications, and evidence.
  reason: SUPPLIED — kb/theory/short-composable-notes-maximize-combinatorial-discovery.md
    — needs a breadth/depth distinction in which titles and descriptions give a broad
    scan and full bodies are loaded selectively for depth (both its inline passage
    and its footer, 'title-level scanning for breadth, full loading for depth'). The
    note's titles/descriptions/bodies mechanism states exactly this, and its discovery
    section adds that broad views place several candidate claims in one context, which
    matches the dependent's pairing use.
- scope: passage
  quotes:
  - A claim title carries the assertion. A description adds a fixed routing cue. The
    body supplies the mechanism, qualifications, and evidence.
  reason: DUPLICATED — kb/theory/short-composable-notes-maximize-combinatorial-discovery.md
    — the dependent restates the note's title/description/body mechanism in one sentence
    ('Claim titles and descriptions give broad surface-level pairing without loading
    full bodies; full notes are loaded selectively where depth is needed'). The note
    states it more fully and grounds it in title-as-claim traversal; the dependent's
    version is better fitted to its own use because it ties the broad view to pairing
    for combinatorial discovery and adds that short notes make both modes cheaper,
    which the note does not say.
- scope: passage
  quotes:
  - Resolution here means the scope and detail exposed by a view, not an intrinsic
    abstraction rank assigned to an artifact.
  reason: PARTLY SUPPLIED — kb/theory/areas-exist-because-useful-operations-require-reading-notes-together.md
    — needs 'resolution levels a consumer must move between' among which read-together
    cohorts (areas) can be placed. The note supplies views of different scope, including
    an intermediate grouping (curated indexes) and intermediate views via progressive
    disclosure, so a bounded cohort fits its definition; but the note neither names
    areas or read-together cohorts as a view nor speaks of discrete levels, and it
    explicitly rejects a fixed abstraction rank, so 'levels' is only loosely the note's
    sense.
- scope: passage
  quotes:
  - A reader using a knowledge base alternates between broad views that expose possible
    routes and narrower views that supply detail.
  reason: SUPPLIED — kb/sources/gwern-design-of-this-website.ingest.md — needs the
    concept of resolution-switching as movement between broad and detailed views,
    for which nested previews and full tag pages are cited as practitioner feasibility
    evidence. The note's definition and its index-and-notes mechanism supply that
    concept; the ingest's own transfer bound (agents use compact heads and scoped
    queries) is consistent with the note's statement that fluidity is relative to
    the navigation operations available.
- scope: passage
  quotes:
  - its role is to preserve the task-relative relationship across the transition
  reason: SUPPLIED — kb/sources/i-like-em-thick.ingest.md — needs resolution switching
    as a movement across a bounded knowledge whole that can keep revealing load-bearing
    relationships, linked alongside link strength. The note's definition plus its
    link-context mechanism (contextual phrases preserve why two views belong together,
    citing link strength) supply this; the ingest's further claim that switching 'continues
    to reveal non-redundant' relationships is its own interpretation of thickness,
    not a claim it takes from the note.
- scope: passage
  quotes:
  - Resolution-switching helps a reader assemble those views; it does not perform
    the recognition or guarantee a discovery.
  reason: NOT SUPPLIED — kb/sources/creative-thinking-by-claude-shannon.ingest.md
    — the ingest's is-evidence-for passage uses resolution-switching in the sense
    of restating a problem from 'every possible angle' and escaping a mental rut at
    one viewpoint, and says this is 'precisely the problem resolution-switching solves'.
    The note defines resolution as scope and detail of a view, not alternative framings
    or viewpoints, and its discovery section explicitly says switching does not perform
    recognition or guarantee a discovery; the dependent uses the term in another sense
    and claims a stronger role than the note supplies.
outcome: report
description: Retained report review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/role/artifact/reviews/1c107f51fccb121a50f404cb/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/role/artifact/reviews/1c107f51fccb121a50f404cb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/role
launch: 5e895bae6d0f43f5ba0ff6be01ed3dcd
completed-at: '2026-11-16T22:34:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/role/calls/launches/5e895bae6d0f43f5ba0ff6be01ed3dcd/outputs/review.md
raw-output-sha256: 8918382323522c830101cda25b687185c4f5a0544d47d64e17d3beae60bc703c
format: 2
---

# Role in the KB: A knowledge base should support fluid resolution-switching

## Role
The note supplies the term "resolution-switching" — movement between broad and narrow views of a KB — that three theory notes and three source ingests cite when they talk about breadth versus depth of reading. Theory dependents use it as an extension target: pointer tiers form its gradient, title-scanning versus full loading are its two modes, and areas sit among its levels. Ingests cite it as the concept their sources give evidence for. No dependent argues from the note's evaluative criterion or its boundaries.
Relied on: the term resolution-switching and its definition as movement among broad and narrow views; the titles/descriptions/bodies breadth–depth mechanism; the progressive-disclosure cost gradient of pointer tiers; link context preserving relationships across a switch. Unused: the four-question evaluative criterion, "resolution-switching fluidity" as a named criterion, the complement to retrieval accuracy, the boundary with addressability grain, pointer accuracy and recall, the outbound-link-not-required boundary, the link-following/search distinction, and the open questions on measurement.

## Dependents
- `kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md` — needs pointer tiers as the resolution gradient.
- `kb/theory/short-composable-notes-maximize-combinatorial-discovery.md` — needs title-level scanning for breadth and full loading for depth (two passages, same need).
- `kb/theory/areas-exist-because-useful-operations-require-reading-notes-together.md` — needs resolution levels among which read-together cohorts can sit.
- `kb/sources/gwern-design-of-this-website.ingest.md` — needs the concept for which nested previews and tag pages are feasibility evidence.
- `kb/sources/i-like-em-thick.ingest.md` — needs switching across a bounded whole that surfaces load-bearing relationships.
- `kb/sources/creative-thinking-by-claude-shannon.ingest.md` — uses the term in a restatement/viewpoint sense the note does not hold. Its second passage was cut at 1200 characters; the visible part asks for a new note that links to this one, not a change to it.

## Duplication
`kb/theory/short-composable-notes-maximize-combinatorial-discovery.md` restates the note's titles/descriptions/bodies mechanism in one sentence. The note's version is fuller and grounded in title-as-claim traversal. The dependent's version fits its own use better, because it ties the broad view to pairing and adds that short notes make both modes cheaper.

## Untaken recommendations
None. The Shannon ingest's visible recommendation is to write a separate note that links to this one; it asks for no change to this note. Its passage was cut at 1200 characters, so any later recommendation in that passage is unseen.

## Reach
- The definition of resolution as the scope and detail of a view, and the term itself, reach all six dependents. A change to the term or its sense reaches `kb/theory/areas-exist-because-useful-operations-require-reading-notes-together.md` (which reads it as levels), `kb/sources/gwern-design-of-this-website.ingest.md`, `kb/sources/i-like-em-thick.ingest.md`, and `kb/sources/creative-thinking-by-claude-shannon.ingest.md` (which already reads it in another sense).
- The titles/descriptions/bodies breadth–depth mechanism reaches `kb/theory/short-composable-notes-maximize-combinatorial-discovery.md`.
- The progressive-disclosure cost gradient reaches `kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md`.
- The link-context mechanism reaches `kb/sources/i-like-em-thick.ingest.md`.
- The discovery boundary (switching does not perform recognition) bears on `kb/sources/creative-thinking-by-claude-shannon.ingest.md`, whose claim is stronger than this boundary allows.
- The evaluative criterion and its four questions, the boundaries section and the open questions reach no dependent.
