---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/githens-manage-innovation-programs-rolling-wave.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Manage Innovation Programs With a Rolling Wave

**Source:** [Manage Innovation Programs With a Rolling Wave](../../../../sources/.snapshots/githens-manage-innovation-programs-rolling-wave.md)

## Discovery Trace

**Collection rules:** Read `kb/sources/COLLECTION.md`. The target is an immutable snapshot, so the candidates below are for the matching ingest's future authored surface; no durable artifact should link to `.snapshots/`. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and sources. Work and instructions are excluded. External prospecting was skipped because no additional external target was supplied.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags`, so no matching tag README or by-tag scan applied.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over notes, reference, agent-memory systems, agentic systems, and sources, scanning 376, 157, 174, 12, and 328 headings respectively.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over the same destinations, scanning 374, 156, 172, 10, and 328 descriptions respectively. Notes and sources produced the only candidates that survived evaluation.

**Body search:**

- `rg -n -i '^description:.*(uncertain|adapt|iterat|progress|planning|replan|horizon|decompos|learning|development|deployment|option)' kb/<destination>/ --glob '*.md'` -- kept the executor-boundary, bounded-lesson, and changing-requirements notes; reference and external-system matches were generic learning or planning mentions.
- `rg -n -i '(uncertainty reduction|rolling wave|progressive elaboration|planning horizon|plan[-– ]do)' kb/<destination>/ --glob '*.md'` -- found the direct stale-plan mechanism in notes and the PDSA/PDCA source cluster; no reference, agent-memory, or agentic-system artifact passed the articulation test.
- `rg -n -i 'PDSA|PDCA|Deming cycle|plan-do-study|plan-do-check' kb/sources/ --glob '*.md'` -- kept one representative PDSA ingest for a named comparison and rejected its two near-duplicate siblings.
- `rg -n -i 'development.{0,80}deployment|deployment.{0,80}development|tool.{0,30}(fit|scope|context)|where.{0,30}(lesson|method|practice).{0,30}stop' kb/notes/ kb/sources/ --glob '*.md'` -- confirmed that Githens's development/deployment boundary is a worked comparison for boundary-stated lessons rather than evidence about agent-memory abstraction itself.

**Link following:**

- Followed [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) to its optionality-ordering premise. Githens supplies a direct practitioner instance: later planning is deliberately deferred because execution produces information the initial planner lacks.
- Followed [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) through its transfer-boundary neighborhood. The article's explicit development-not-deployment limit is a worked comparison, not evidence for the note's agent-memory mechanism.
- Followed the local planning-and-learning neighborhood through MCDP 1 and the three PDSA/PDCA ingests. MCDP 1 shares information-timed planning detail; the PDSA source distinguishes prediction-and-study learning from rolling-wave phase replanning.

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: Githens gives a mature practitioner account of high-level initial structure, detailed near-horizon work, explicit replanning dates, and later elaboration as execution reduces uncertainty. It supports the note's stale-plan mechanism, not a comparative claim that rolling wave outperforms alternatives.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **compares-with**: the article states its method's stopping boundary explicitly—rolling wave fits uncertain development and may slow relatively linear deployment—providing a worked method-scope comparison without testing the note's agent-memory abstraction rule.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- **compares-with**: Githens groups new requirements, demand shifts, technology, weak requirements, and invalid assumptions under development uncertainty; the note separates world change from late-discovered interpretation error, clarifying two different things rolling-wave replanning may absorb.
- [MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) -- **compares-with**: both accounts keep long-horizon purpose visible while withholding advance precision from choices whose premises arrive later; Githens uses time-bucket replanning and progressive WBS elaboration, while MCDP 1 gives live-state choices to competent local executors.
- [Foundation and History of the PDSA Cycle](../../../../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md) -- **compares-with**: both use repeated plan-and-act cycles for learning, but PDSA requires prediction and study against observation whereas rolling wave centers staged uncertainty reduction and plan elaboration. The contrast prevents every iterative plan-do process from being treated as the same learning mechanism.

## Bidirectional Candidates

- [MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) <-> future Githens ingest -- **compares-with**: readers of either source benefit from comparing time-based progressive planning with intent-based local discretion on the shared axis of when information becomes available.
- [Foundation and History of the PDSA Cycle](../../../../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md) <-> future Githens ingest -- **compares-with**: the return path would distinguish a prediction-and-study improvement cycle from phase-gated replanning that learns without requiring an explicit hypothesis test.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- both defer commitment, but the note specifically concerns repeated LLM behavior being codified into deterministic semantics; equating that with schedule elaboration would over-transfer the mechanism.
- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- rolling wave orders detail by information horizon and uncertainty, not by an explicit estimate of each choice's feasible-set size.
- [ADRP 6-0: Mission Command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md) -- it passes the topical comparison test, but MCDP 1 is the narrower planning-horizon match; keeping both would duplicate the same military-doctrine axis.
- [Evolution of the PDCA Cycle](../../../../sources/evolution-of-the-pdca-cycle.ingest.md) and [Circling Back—Clearing Up Myths About the Deming Cycle](../../../../sources/circling-back-clearing-up-myths-about-the-deming-cycle.ingest.md) -- these duplicate the retained PDSA comparison's authors, lineage, and prediction-study distinction without adding a separate traversal need.

## Index Membership

None. The sources README does not enumerate individual ingests, and the target is a local snapshot rather than a library artifact.

## Synthesis Opportunities

None.

## Maintenance Observations

- No matching `kb/sources/githens-manage-innovation-programs-rolling-wave.ingest.md` existed during discovery. Until that authored surface exists, the sources contract forbids durable links to this hidden snapshot.

## Flags

- **Evidence limit:** this is a 2001 practitioner report with examples and attributed practitioner statements, not a controlled comparison. It supports the coherence and stated mechanism of rolling-wave planning, not causal superiority.
- **Applicability limit:** the source explicitly restricts the method to uncertain, design-heavy development and warns that it can make linear deployment slower and less efficient.
