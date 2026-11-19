---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/maybe-we-shouldnt-be-reviewing-all-this-code.md"
source_has_frontmatter: true
date: "2026-09-03"
depth: standard
---

# Connection Report: Maybe We Shouldn't Be Reviewing All This Code

**Source:** [Maybe We Shouldn't Be Reviewing All This Code](../../../../sources/.snapshots/maybe-we-shouldnt-be-reviewing-all-this-code.md)

## Discovery Trace

**Setup and source read:**
- Read the [connect-report type](../../../../types/connect-report.md), [sources collection contract](../../../../sources/COLLECTION.md), and the complete snapshot. The snapshot argues that AI-generated code makes universal pull-request review a throughput bottleneck; deterministic checks should be automated, design and knowledge-transfer judgment should move earlier, and late human review should be reserved for exceptional risk.
- The source collection authorizes prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. It excludes `kb/work/` and `kb/instructions/`. The snapshot carries no tags, so no tag-README pass was available. External prospecting was skipped; only the DX article already linked by the snapshot was evaluated.

**Curated heads:**
- Read [Notes](../../../../notes/README.md), [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). The notes and sources heads established the relevant theory and prior-source surfaces. The reference and external-system heads exposed no collection-specific target stronger than the theory and source comparisons below.

**Title and description listings:**
- Generated the complete title surface for every authorized local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, substituting `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- Generated each destination's complete description surface with `rg '^description:' kb/<destination>/ --glob '*.md'`. In notes this flagged the verification boundary, human-effort relocation, semantic-work relocation, review-cost, maintenance-capacity, and program-theory clusters. In sources it flagged the Horthy lights-off/lights-on pair, professional-developer control, Fluent, Warp, and Naur. Reference results were Commonplace-specific review machinery; agent-memory and agentic-system results mentioned review only as one subsystem detail.

**Body search:**
- `rg -n -i 'code review|pull requests?|review by exception|shift (the )?judg|feedback loops?|human (judg|review)|review (queue|bottleneck)|verification (queue|bottleneck)|engineers? to understand systems|understand systems, not diffs|cheap (code|generation)|agent.generated code|AI.*code' kb/notes --glob '*.md'` surfaced the retained note candidates below and several generic human-review mentions rejected as keyword-only.
- `rg -n -i 'code review|pull requests?|review by exception|feedback loops?|human (judg|review)|review (queue|bottleneck)|verification (queue|bottleneck)|cheap (code|generation)|AI.*code' kb/reference --glob '*.md'` found Commonplace review procedures and ADRs, but none bears on the source's software-development claim strongly enough for a `see-also` edge.
- `rg -n -i 'code review|pull requests?|review by exception|feedback loops?|human (judg|review)|review (queue|bottleneck)|verification (queue|bottleneck)|cheap (code|generation)|AI.*code' kb/agent-memory-systems kb/agentic-systems --glob '*.md'` found incidental review stages in system analyses; none makes code-review placement its operative claim.
- `rg -n -i 'code review|pull requests?|review by exception|feedback loops?|human (judg|review)|review (queue|bottleneck)|verification (queue|bottleneck)|engineers? to understand systems|cheap (code|generation)|agent.generated code|AI.*code|cognitive and intent debt' kb/sources --glob '*.md'` identified the source comparisons below and weaker current-practice or whole-factory reports.

**Link following:**
- Opened [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md), [Warranted transfer leaves people the hardest-to-warrant decisions](../../../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md), [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md), and [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md). Kept the first five where the source supplies a concrete mechanism or boundary; rejected maintenance capacity because the source does not measure harmful inflow or repair capacity.
- Followed the program-understanding branch through [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) and [Naur binds program theory to humans by equating machine execution with formulated criteria](../../../../notes/naur-equates-machine-execution-with-formulated-criteria.md). Kept the source-to-source comparison because Laycock's pairing and joint-design prescription directly instantiates Naur's close-work transfer channel; rejected the narrower recognizer argument.
- Opened [Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md), [Professional Software Developers Don't Vibe, They Control](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md), [Fluent](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md), [Warp's self-improving agents](../../../../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md), and [The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md). Kept Horthy's report as the closest independent workflow comparison; the others concern current practice, a broader factory, instruction promotion, or reviewer prompting rather than the timing and allocation of review.
- Read [notes collection rules](../../../../notes/COLLECTION.md) before proposing reverse edges and verified every retained candidate path.

## Connections Found

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **is-evidence-for**: Laycock gives a software-development instance of the note's mechanism: valuable meaning-dependent feedback is moved to collaborative design and pairing, while deterministic checks are codified, rather than judgment being made to disappear.
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- **is-evidence-for**: the source predicts that higher agent code throughput moves scarce senior attention from routine diff inspection to architecture, security boundaries, blast radius, unfamiliar critical systems, and low-confidence cases.
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) -- **compares-with**: review by exception selects exactly the high-stakes, weakly checked, or uncertain residue the note predicts, but the essay proposes that allocation rather than supplying before-and-after evidence for the selection effect.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **compares-with**: both locate the bottleneck in checking rather than generation; Laycock adds that the response is to automate deterministic properties, move other judgment earlier, and stop treating universal late review as the unit of confidence.
- [Cheap generation breaks text volume as an effort signal](../../../../notes/cheap-generation-breaks-text-volume-as-an-effort-signal.md) -- **is-evidence-for**: the essay explicitly applies the generation/verification asymmetry to rapidly growing code diffs, where reviewer effort no longer scales with author-side production effort.
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) -- **compares-with**: Naur argues that system understanding transfers through close work with theory holders rather than completed artifacts alone; Laycock independently turns that claim into pairing, collective design, and the maxim that engineers must understand systems rather than diffs.
- [Why Software Factories Fail: Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md) -- **compares-with**: both reject large late generated-code reviews and move human judgment upstream; Horthy uses staged artifacts and short vertical slices, while Laycock emphasizes pairing, team design, automated constraints, and exceptional late review.
- [What are code reviews even for?](https://newsletter.getdx.com/p/what-are-code-reviews-even-for) -- **see-also**: this is the explicit opposing essay Laycock answers, so it is the shortest route to the disagreement over whether code review should retain its knowledge-transfer and ownership functions.

## Bidirectional Candidates

- [Why Software Factories Fail: Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md) <-> source -- **compares-with**: a return edge would expose two independently stated versions of moving maintainability judgment upstream, along with their different controls for the remaining review span.
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) <-> source -- **compares-with**: a return edge would give Naur's theory-transfer account a current agentic-coding application centered on pairing and shared system understanding.

## Reverse-edge Candidates

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -> source -- **evidenced-by**: the ingest can serve as a practitioner application of relocating semantic judgment upstream while codifying deterministic checks.
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -> source -- **evidenced-by**: the essay supplies a current software-development case in which increased implementation throughput leaves senior humans the exceptional architectural and risk decisions.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) -- the shared throughput vocabulary is real, but Laycock discusses review allocation and team understanding rather than defect incidence, exposure, or repair-queue stability; the verification and relocation notes are more specific.
- [Naur binds program theory to humans by equating machine execution with formulated criteria](../../../../notes/naur-equates-machine-execution-with-formulated-criteria.md) -- the snapshot bears on program-theory transfer, not the note's specific argument about trained recognizers breaking Naur's human-only inference.
- [Professional Software Developers Don't Vibe, They Control](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) -- the study observes that professionals currently review generated code, but does not separate late pull-request review from the earlier planning and supervision that Laycock claims should replace it.
- [How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) -- Fluent also isolates human judgment at selected transitions, but its larger proposal-selection and retained-expertise loop makes it a less discriminating comparison than Horthy's review-placement workflow.
- [How Warp builds self-improving agents on Claude](../../../../sources/how-warp-builds-self-improving-agents-on-claude.ingest.md) -- its mandatory PR review governs promotion of instruction edits, a different authority transition from universal review of generated product code.
- [The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md) -- it tests explicit reviewer probes versus undirected self-review, not whether human judgment should occur before implementation or only on exceptional changes.
- [ADR 005: Quality check placement](../../../../reference/adr/005-quality-check-placement.md) -- the title matched review-placement searches, but the ADR records Commonplace's historical validation/review architecture rather than a transferable software-development comparison.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- review stages appear in the analyzed harness, but code-review timing is not the analysis's operative claim; linking would be topical rather than explanatory.

## Index Membership

None

## Synthesis Opportunities

- This source and [Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md), read through [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), support a candidate transferable claim: when generation outpaces late verification, preserve judgment by moving it to the earliest decision surface that has its inputs and bound the remaining unchecked span by risk. Horthy's ingest already recommends this note; Laycock adds pairing, collective design, executable constraints, and review-by-exception as a second practitioner route.

## Maintenance Observations

None

## Flags

- The Meta and DX growth figures are reported second-hand in the essay. They motivate the bottleneck but should not be treated as primary empirical evidence unless their original sources are separately captured.
