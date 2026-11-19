---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/pindyck-irreversibility-uncertainty-investment.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Irreversibility, Uncertainty, and Investment

**Source:** [Irreversibility, Uncertainty, and Investment](../../../../sources/.snapshots/pindyck-irreversibility-uncertainty-investment.md)

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md`. It authorises local prospecting into `notes`, `reference`, `sources`, `agent-memory`, and `agentic-systems`, excludes `work` and `instructions`, and reserves authored outbound links for ingest reports and source reviews. The snapshot is immutable, so accepted outbound candidates below are recommendations for the matching ingest rather than edits to this file.
- The authorised labels relevant to the retained candidates are `compares-with` for notes and sources. External is authorised, but open-web prospecting was skipped as required; the snapshot's NBER URL is source identity, not an additional candidate edge.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The source has no `tags:` field, so no tag README was applicable and no by-tag search was run.
- The notes head routed the search toward transferable mechanisms rather than finance as a topic. The reference head exposed no shipped-system destination matching the source's claim. The agent-memory and agentic-system heads exposed no review or whole-system analysis whose reader would gain from a real-options comparison.

**Full title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorised local destination: 376 note titles, 157 reference titles, 331 source titles, 174 agent-memory titles, and 12 agentic-system titles. The notes scan flagged costly structural entrenchment, progressive constraining, prototype standing, executor-time determination, and optionality-preserving decomposition. The sources scan flagged the Githens rolling-wave ingest; the other destination title surfaces produced no plausible target.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` for every authorised local destination: 374 note descriptions, 156 reference descriptions, 331 source descriptions, 172 agent-memory descriptions, and 10 agentic-system descriptions. This retained the costly-entrenchment and executor-time notes, and surfaced the Githens and PMI rolling-wave ingests. Apparent hits in the other collections concerned connector options, optional modules, reversible self-modification, or command configuration rather than the value of delaying a costly commitment.

**Body search:**

- Ran `rg -n -i '\birreversib|\breversib|sunk cost|costly entrench' kb/<destination>/ --glob '*.md'` across all five destinations. In notes, the useful hit was [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md), which explicitly treats replaceability as preserving adaptation options. Other hits used “irreversible” only as a generic safety adjective. In agent-memory and agentic-systems, rollback and reversible-edit passages lacked the source's commitment-timing mechanism.
- Ran `rg -n -i 'option value|value of waiting|optionality|preserv(e|ing) .*option|wait(ing)? for (new )?information|delay(ed|ing)? commitment' kb/<destination>/ --glob '*.md'` across all five destinations. This flagged the executor-time note, progressive constraining, optionality-preserving decomposition, and costly entrenchment. The decomposition note was rejected because its low-degree-of-freedom ordering is constrained-search logic, not a claim about waiting for information before an irreversible act.
- Ran `rg -n -i 'uncertaint.{0,80}(commit|invest|constrain|defer)|commit.{0,80}uncertaint|defer.{0,80}(information|evidence|stabil)' kb/<destination>/ --glob '*.md'` across all five destinations. This retained [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), whose mechanism depends on information arriving during execution, and surfaced the two rolling-wave source ingests.
- Ran `rg -n -i 'Pindyck|Dixit|irreversib|real options|option value|value of waiting|sunk cost' kb/sources/ --glob '*.md'` and `rg -n -i 'defer future detail|deferring detail|decision-relevant information|information arrives|relearning|commitment.*information|information.*commitment' kb/sources/ --glob '*.md'`. No prior Pindyck or real-options ingest was found. The second query identified the Githens and PMI records as the established information-timing source cluster.

**Link following:**

- Followed the costly-entrenchment note to progressive constraining, localized retention, and prototype standing. The first already distinguishes repeated-run stabilization from permanent entrenchment; the second concerns edit and validation locality after change; the third defines theory revision cost. Only costly entrenchment preserved the source's full decision structure: expensive commitment, changing future conditions, retained alternatives, and a countervailing current-use benefit.
- Followed the executor-time note to low-degree-of-freedom ordering and bounded-context scheduling. Those neighbors preserve optionality by decision ordering, but they do not require new information to arrive and therefore failed the articulation test for a direct source connection.
- Followed the Githens ingest to the PMI lexicon and the executor-time note. Githens was kept because its staged relearning prescription creates a substantive comparison with Pindyck's formal conditions for waiting; PMI was rejected as a redundant terminology-only target.

## Connections Found

- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- **compares-with**: Pindyck formally derives when a delayable but irreversible commitment has option value, while the note applies the same decision structure to replaceable KB structure under changing future questions. Reading them together makes the transfer conditions explicit: later information must be able to change the decision, commitment must destroy a valuable alternative, and waiting must be weighed against foregone current benefit.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with**: the note argues that execution can reveal premises an earlier author lacks; Pindyck separates passive information arrival, costly delay, and active sequential investment that itself produces information. The comparison sharpens when deferral preserves value and when early action can instead be information-gathering.
- [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) -- **compares-with**: Githens gives a practitioner method for deferring future detail to scheduled relearning points, whereas Pindyck supplies a formal model of when waiting before a sunk commitment is valuable and when foregone payoff makes delay costly. The shared axis is information-timed commitment, not the surrounding PMI governance package.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- rejected as a direct edge: both defer commitment, but the note learns a stable semantic pattern across repeated LLM runs, while Pindyck values waiting under a stochastic payoff and sunk expenditure. The costly-entrenchment target carries the shared mechanism more precisely.
- [A theory's prototype standing is its revision cost: external binding plus lost investment](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) -- rejected: “sunk investment” is a real overlap, but Pindyck's project model does not support the note's exhaustive claim that theory revision cost reduces to external binding plus discarded reconstruction investment.
- [Canonical files may defer a shared schema while database authority remains a separate commitment](../../../../notes/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) -- rejected: the source can motivate caution about commitment timing, but it says nothing about schema semantics, canonical authority, or governing write paths.
- [PMI Lexicon of Project Management Terms, Version 4.0](../../../../sources/pmi-lexicon-project-management-terms-v4.ingest.md) -- rejected as redundant: it defines progressive elaboration and rolling-wave planning but adds no argument beyond the stronger Githens comparison already retained.
- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- rejected: preserving feasible placements by constraint ordering does not depend on waiting for new information or on an irreversible expenditure.

## Index Membership

None

## Synthesis Opportunities

None. The strongest higher-order candidate—costly commitment should be delayed when later information can change the choice—already has a scoped KB treatment in the costly-entrenchment note; a new synthesis would duplicate it unless a future writer can add a decision rule that prices irreversibility, information arrival, and delay cost for KB structure.

## Maintenance Observations

- No matching `kb/sources/pindyck-irreversibility-uncertainty-investment.ingest.md` existed during discovery. Because snapshots cannot carry authored links, the retained candidates have no legal authored surface until that ingest is created.

## Flags

None
