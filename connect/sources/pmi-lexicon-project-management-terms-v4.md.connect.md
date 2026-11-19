---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/pmi-lexicon-project-management-terms-v4.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: PMI Lexicon of Project Management Terms, Version 4.0

**Source:** [PMI Lexicon of Project Management Terms, Version 4.0](../../../../sources/.snapshots/pmi-lexicon-project-management-terms-v4.md)

This snapshot is immutable. Every outbound candidate below is for its matching future ingest surface, not for an edit to the snapshot.

## Discovery Trace

**Description listing scan:**

- Ran complete `rg '^description:'` scans over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. The note scan retained the executor-detail and codification-planning claims; the sources scan retained the existing Githens rolling-wave ingest. Reference, agent-memory, and agentic-system descriptions had no candidate matching the source's specific information-timed planning mechanism.

**Topic indexes:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no tag README or by-tag scan applied.
- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# '` for all five authorised local destinations (376 note titles, 157 reference titles, 174 agent-memory titles, 12 agentic-system titles, and 330 source titles). Only the same note and source cluster survived articulation.

**Body search:**

- `rg -n -i "progressive elaboration|rolling wave|rolling-wave|progressively elaborat|near.term.*detail|future.*higher level|detail.*information|coarse.*fine|defer.*detail" ...` -- found the Githens ingest and the executor-detail note; unrelated coarse/fine retrieval hits were rejected.
- `rg -n -i "progressive|rolling|wave|defer|detail|planning|uncertain|relearn|information arrives|commit early|premises" ...` -- retained the codification note's explicit information-arrival planning consequence; broad planning and progressive-disclosure hits lacked the same mechanism.
- `rg -n '^description:.*(progress|rolling|defer|detail|plan|uncertain|information|iteration|elaborat)' ... -i` -- confirmed the retained candidates and exposed keyword-only progressive-constraining, memory, and control-plane matches that failed articulation.

**Link following:**

- Followed the neighborhood of [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) through its frontloading, competent-executor, underspecification, and ordering links. Those links explain adjacent costs or prerequisites but do not need this project-management definition directly.
- Followed [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) through its verification and methodology-boundary links. Only its section on when planning information arrives matches the lexicon definitions.
- Followed [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) through its executor-detail, requirements-change, boundary, and PDSA comparisons. The lexicon is a useful comparison because it supplies the authoritative term distinction without Githens's additional prescriptive machinery.

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: PMI's paired definitions give an authoritative project-management instance of the note's information-timing rule: detail increases as information improves, and near-term work is detailed while future work remains higher-level.
- [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) -- **is-evidence-for**: the lexicon corroborates the note's narrower planning consequence that advance detail should be deferred when decision-relevant information is expected during execution; it does not bear on the note's broader codification-selection claim.
- [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) -- **compares-with**: PMI defines rolling-wave planning narrowly as near-term detail plus higher-level future work and places it beside progressive elaboration, while Githens expands that technique into a practitioner program-management method with relearning points, gates, WBS/Gantt elaboration, baselines, and approvals. Comparing them prevents the prescriptive package from being mistaken for the term's defining mechanism.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → matching future ingest -- **evidenced-by**: a reader checking the note's plan-specific instance gains an authoritative definition of the established planning pattern; this remains independently useful even if the ingest also links outward to the note.
- [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) → matching future ingest -- **evidenced-by**: the source corroborates only the note's scoped information-arrival planning paragraph, so any future citation should state that limit explicitly.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- rejected as keyword-only: it defers symbolic commitment until behavior repeats across runs, not planning detail until project information becomes available.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- rejected: the lexicon defines adaptive, iterative, and planning terms but does not support this note's causal distinction between world change and interpretation error.
- [Foundation and History of the PDSA Cycle](../../../../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md) -- rejected: iterative cadence is too broad; PDSA's prediction-and-study learning mechanism is materially different from progressive elaboration and rolling-wave planning.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Apply accepted candidates only to the matching future ingest surface; never add links or annotations to this checksum-bound snapshot.
