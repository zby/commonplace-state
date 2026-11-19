---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/backtracking-keeps-lightweight-search-control-provisional.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Backtracking keeps lightweight search control provisional

**Source:** [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the source's tag heads: `foundations-README.md`, `computational-model-README.md`, and `self-improving-systems-README.md`. None of the three tag heads declares `complete: true`, so no by-tag description scan was skipped. The self-improving-systems head placed the source beside proposal-selection and repeatable-revision mechanisms; the computational-model head exposed the checkpoint, branch, and re-entry aspect as a scheduling concern.
- Read the destination heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The agentic and source heads led to the strongest implementation cases; the other heads supplied no direct candidate.

**Title and description listing scans:**

- Generated the complete notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'`. It exposed the productive-deferral, entrenchment, localized-retention, failure-feedback, controller-evaluation, addressability, revision-continuity, and prototype-standing candidates evaluated below.
- Generated complete title surfaces with the same command for `kb/types`, `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, `kb/sources`, and `kb/instructions`.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` for every authorised local destination: `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran the required by-tag description scans for `foundations`, `computational-model`, and `self-improving-systems` using `rg -l '^tags:.*\bTAG\b' kb/notes --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These scans retained the controller-evaluation and failure-feedback cluster and rejected broad rollback, revision, and recovery matches that do not preserve a provisional branch choice.

**Body search:**

- `rg -n -i 'backtrack|backtracking|rollback|roll back|rewind|restore.*state|return path' kb/notes --glob '*.md'` -- retained productive deferral, localized retention, and the entrenchment distinction. It also exposed many rollback uses concerned with withdrawing an accepted operative change; those were rejected when their authority boundary did not match lightweight search control.
- `rg -n -i 'reversib|irreversib|de facto commitment|commitment.*cost|costly.*recover' kb/notes --glob '*.md'` -- kept the current-task entrenchment note and localized-retention condition; rejected the theory-only prototype-standing formulation as narrower and redundant.
- `rg -n -i 'checkpoint|snapshot|branch history|branch choice|branch decision|redirect.*search' kb/notes --glob '*.md'` and `rg -n -i 'contrary evidence|failed branch|failure explanation|abandonment|abandon.*branch' kb/notes --glob '*.md'` -- kept the failure-explanation and controller-evaluation notes because they specify how evidence changes a later branch and how the resulting controller can be assessed.
- `rg -n -i 'option value|preserv.*option|lock-in|entrench|sunk cost|path depend' kb/notes --glob '*.md'` -- retained productive deferral as the general option-evidence-convergence test and current-task entrenchment as the dependency-cost consequence.
- `rg -n -i 'recovery|continuity|revision path|repeatable operative|state transition' kb/notes --glob '*.md'` -- confirmed the source's existing program-theory link already reaches the broader repeatable-operative-path note, so another direct edge would not sharpen traversal.
- Across `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, `instructions`, and `types`, ran `rg -n -i 'backtrack|backtracking|rollback|roll back|rewind|restore.*state|checkpoint|branch history|branch decision|reversib|irreversib|entrench|return path|contrary evidence' kb/<destination> --glob '*.md'`. Follow-up queries for `rewind.*(sandbox|state)|record of what was tried|failed attempt`, `rollback stack|restore.*distribution|reversible promotion`, `archived anchor|restore.*workspace|re-anchoring|state-matched checkpoint`, and `co-version|atomic.*checkpoint|checkpoint boundary|control state.*executable` retained Exo and ScienceFlow, exposed Apodex's incomplete restoration boundary for synthesis, and rejected promotion rollback cases that act after operative adoption rather than on a provisional search branch.
- External prospecting was skipped because no external target was supplied or already loaded. The relevant external evidence already has tracked local analyses.

**Link following:**

- Followed both authored source links. The lightweight-control neighborhood led to the general prior-allocation and proposal-selection claims; the program-theory neighborhood led to theory retention, delayed evaluation, and repeatable operative revision. Those paths already supply the source's general search and continuity context.
- Followed the productive-deferral, failure-explanation, search-controller, entrenchment, and localized-retention neighborhoods one hop. Productive deferral maps almost exactly onto preserved state, contrary evidence, and a return response; failure explanation and controller evaluation add feedback and assessment roles; entrenchment and localized retention explain when an attempted branch becomes expensive to reverse.
- Followed Exo into its memory-system companion and ScienceFlow into its Apodex comparison. Exo and ScienceFlow both restore mutable work without erasing the attempt record. Apodex's non-atomic Task Board, Agent Bus, and filesystem checkpoint exposes the missing complementary requirement: mutually dependent control and executable state must resume at the same logical point.
- Searched inbound links with `rg -n --fixed-strings 'backtracking-keeps-lightweight-search-control-provisional.md' kb --glob '*.md'`. The only hit was in `kb/work/`, which the source collection excludes; no library artifact already authors a return path.
- Read the full claims, caveats, and relevant-link surfaces of every retained candidate. All retained and rejected targets below have frontmatter, and every listed path was verified to exist.

**Per-destination disposition:**

- `notes` (including `notes/definitions`): five outbound candidates passed the articulation and label tests. Three also warrant useful return paths. No term required a `defined-in` edge.
- `types`: no type contract bears directly on backtracking, restoration state, or provisional branch authority.
- `reference` (including `reference/definitions`): storage and review records mention rollback, but only as Commonplace implementation behavior or unadopted recovery designs; none supplies a distinct reader path for the general claim.
- `agent-memory-systems`: Incremental Self-Improvement has a rollback stack, but its retained policy modifications are operative promotions rather than lightweight branch choices, so the closer primary-source record was also rejected on the same authority mismatch.
- `agentic-systems`: Exo passed as a code-grounded implementation case. Agno describes a desired future rollback loop rather than a shipped one, and other checkpoint hits concerned replay or crash recovery without evidence-triggered branch redirection.
- `sources`: ScienceFlow passed as the strongest code-grounded restoration-and-redirection case. Apodex contributes to a synthesis opportunity rather than a direct edge; the Schmidhuber, Symbolic Learning, and CRUX sources were rejected for the specific reasons below.
- `instructions`: no procedure adds ordering, defaults, or stopping conditions to this methodology strongly enough to warrant `operationalized-from`.

## Connections Found

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- **exemplifies**: backtracking instantiates the general test by keeping an earlier state exercisable, using contrary evidence to reopen the branch choice, and coupling return to a redirect response.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **extends**: identifies one form of contrary evidence that becomes operative only when retention changes the later scope, priority, probe, continuation, or abandonment decision.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **extends**: supplies the downstream comparison for judging whether provisional branch control and its recovery paths produce useful candidates, evidence, informative failures, or improved recovery.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- **extends**: develops the source's de facto commitment warning into a distinction between reversible trial use and dependencies or migration costs that make later replacement expensive.
- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **mechanism**: states the matching, explicit-dependency, and bounded-impact conditions under which restoring a retained artifact state remains a local operation rather than requiring system-wide reconstruction and validation.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **evidenced-by**: the inspected harness implements sandbox rewind while retaining an ordered event record, allowing an agent to restore mutable state, inspect the failed attempt, and redirect instead of repeating it.
- [Ingest: ScienceFlow: A Long-horizon Agent for ML Research, Scientific Discovery and Beyond](../../../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md) -- **evidenced-by**: code inspection confirms archived workspace restoration and continue-or-redirect decisions while the raw Stage ledger and cumulative resource accounting remain outside the restoration boundary.

## Bidirectional Candidates

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) <-> source -- source to productive deferral is **exemplifies**; productive deferral to source is **mechanism**, because backtracking supplies one concrete way to preserve the option and enact the convergence response after discriminating evidence arrives.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) <-> source -- source to failure explanation is **extends**; failure explanation to source is **mechanism**, because backtracking is one way a retained explanation can restore a usable position and make the changed later branch decision operative.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) <-> source -- source to controller evaluation is **extends**; controller evaluation to source is **mechanism**, because a usable backtracking path is one mechanism through which false leads can yield recovery rather than hidden commitment.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- rejected because addressability makes targeted revision and rollback possible but is not a prerequisite for all backtracking; the source also covers plans, opaque state, and other restorable search positions.
- [A repeatable operative path keeps a redesign class open to revision](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) -- rejected as a direct edge because it concerns continuity after an accepted operative revision and is already reachable through the source's authored program-theory link.
- [A theory's prototype standing is its revision cost: external binding plus lost investment](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) -- rejected because it models revision cost for theories only and overlaps the broader entrenchment candidate without grounding the source's plan, artifact, and search-position scope.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- rejected as a direct edge because it already grounds the authored lightweight-control note; another link would duplicate the prior-problem path rather than develop backtracking.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected because its rollback operation governs reject-capable evaluation or continued retention, while the source concerns a branch choice whose authority has not yet licensed adoption; it is also already reachable through lightweight control.
- [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) -- rejected because its rollback withdraws improperly authorized future force after detection; that is recovery from an operative authority failure, not preservation of a provisional search branch.
- [Ingest: On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) -- rejected as a direct edge because its stack restores policy distributions after retained self-modifications stop qualifying. That is strong evidence for reversible promotion but risks conflating post-adoption rollback with lightweight search control.
- [Ingest: Symbolic Learning Enables Self-Evolving Agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- rejected because its same-oracle rollback rejects a proposed harness update after re-evaluation; it supports an acceptance boundary more directly than provisional branch backtracking.
- [Ingest: Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) -- rejected because the observed runs distinguish local iteration from ineffective project-level backtracking but do not isolate backtracking causally or implement the operative return path asserted by the source.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- candidate for `Update architecture` beside proposal selection: the source states the return-path mechanism that keeps a lightweight search choice from acquiring the practical consequences of acceptance merely through continued work.
- [Computational model](../../../../tags/computational-model-README.md) -- candidate for `Scheduling & Orchestration`: the source makes checkpointed state, evidence-triggered re-entry, and branch redirection part of the scheduler's state-transition problem.

## Synthesis Opportunities

- **Reliable backtracking requires a split restoration boundary:** the source's usable-state condition, [Exo's preserved event log](../../../../agentic-systems/reviews/exo.md), [ScienceFlow's retained evidence and cumulative resource accounting](../../../../sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md), and [Apodex's non-atomic control/filesystem checkpoint](../../../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) together imply that mutually dependent control and executable state must resume at one logical point while failed-attempt evidence and spent resources remain monotonic outside rollback. No existing note captures the full claim.

## Maintenance Observations

None

## Flags

None
