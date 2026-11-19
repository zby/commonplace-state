---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/a-better-factory-claim-compares-operative-states.md"
source_has_frontmatter: true
date: "2026-09-02"
depth: standard
---

# Connection Report: A better-factory claim compares operative states

**Source:** [A better-factory claim compares operative states under an antecedent assessment relation](../../../../notes/a-better-factory-claim-compares-operative-states.md)

## Discovery Trace

**Setup and authorization:**

- Read the connect skill, this report type, the report schema, the target note, and `kb/notes/COLLECTION.md`.
- Source collection determined from the path as `notes`. `kb/notes/COLLECTION.md` exists and authorizes prospecting from notes to `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, `instructions`, and the reserved `external` destination.
- The source collection excludes `kb/work/`, so no workshop prospecting was performed. `external` was skipped because the skill treats it as authorization for already-known targets, not an open-web prospecting surface.
- Authorized source-side labels used for kept outbound candidates: `mechanism`, `extends`, `grounds`, `evidenced-by`, and `see-also`, filtered by destination.

**Curated heads and title/description surfaces:**

- Read `kb/notes/README.md`, `kb/notes/foundations-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/self-improving-systems-README.md`. None of the three tag heads declared `complete: true`, so by-tag description sweeps were not skipped.
- Read `kb/reference/README.md`, `kb/types/README.md`, `kb/instructions/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md` as destination heads.
- Generated title surfaces with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, plus the same query for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`.
- Ran description listings with `rg '^description:' kb/notes/ --glob '*.md'`, plus the same query for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The broad notes listing was large; the decisive candidates came from tag-restricted sweeps and focused body search.
- Ran tag-restricted notes description sweeps: `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`, and equivalent queries for `learning-theory` and `self-improving-systems`.

**Body search:**

- Ran `rg -n "operative successor|antecedent assessment|evaluator location|learner boundary|non-regression|candidate admission|measurement over snapshots|factory development|improvement objective|operative states|prior scope" kb/notes/ --glob '*.md'`. This surfaced the source itself, its existing premise links, and adjacent claims about proposal-selection loops, proximate targets, weak oracle discrimination, open-ended search, autonomy, and factory development.
- Ran the same query over `kb/reference/`, `kb/instructions/`, and `kb/sources/`. Reference yielded the tag-readme self-improvement trace; instructions yielded no candidates; sources yielded software-factory and harness-evolution ingests.
- Ran `rg -n "harness benefit|harness-updating|non-regression|held-out|accepted candidate|proposal validation|improve themselves|self-improvement loop|operative retention|proposal-selection|operative successor|candidate admission|evaluator" kb/agent-memory-systems/ --glob '*.md'`, with equivalent searches over `kb/agentic-systems/`, `kb/sources/`, and `kb/types/`. This separated memory/harness systems with real accepted-successor loops from generic retrieval or storage systems.

**Candidates opened and evaluated:**

- Opened notes: [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md), [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md), [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md), and [Evidence bearing on an improvement objective](../../../../notes/definitions/evidence-bearing-on-an-improvement-objective.md).
- Opened reference candidates: [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md), [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md), [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md), and [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md).
- Opened source candidates: [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md), [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md), [Harness Engineering for Self-Improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md), and [Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md).
- Opened system candidates: [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md), [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md), [Exo](../../../../agentic-systems/reviews/exo.md), [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md), [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md), [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md), [GBrain](../../../../agent-memory-systems/reviews/gbrain.md), and [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md).
- Verified kept candidate paths with `test -f` before writing. All paths included below exist.

**Link following:**

- Followed the source's existing footer links through factory learning, declared objectives, operative revision paths, compounding, experiment contrasts, deployed-system boundaries, and objective revision. Those links already cover the source's immediate premises, so most are not repeated as new candidates.
- Followed the self-improving-systems head into proposal-selection, reflective structure, improvement dynamics, governance, and actor allocation. This made candidate admission, evaluator location, and learner boundary the main connection axes.
- Followed the proposal-selection loop into open-ended search, lightweight search control, false-positive acceptance, and operative retention. Kept the broader and more load-bearing links; rejected narrower search-controller links where they would duplicate the open-ended-search bridge.
- Followed Commonplace reference cases into the declared frame, tag-readme trace, change-candidate survey, and ablation proposal. Kept the trace and ablation proposal as reverse/reference candidates because they use this note's comparison discipline more than they ground it.
- Followed harness and agentic-system reviews into their acceptance gates, retained successor artifacts, rollback boundaries, and oracle limitations. Kept the cases that materially illustrate accepted-successor or reverse-edge use; rejected close overlaps whose evidence was weaker or redundant.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **mechanism**: the source's candidate-admission route requires a generated candidate, a reject-capable evaluator, and an accepted change becoming operative; this note supplies that loop anatomy.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- **extends**: the source states the comparison needed once a successor route exists; this note develops the prior search-allocation problem that decides which candidates or tests ever reach that comparison.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **extends**: the source makes a better-factory comparison falsifiable by declaring dimensions and thresholds; this note adds the adjacent gap where achieving the target does not warrant the target-to-objective link.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **mechanism**: the source's non-regression and improvement relation depends on what the evaluator can discriminate; this note explains how weakly discriminated qualities can lose selection pressure even while nominally included.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **grounds**: the source separates evaluator location from learner boundary, and this note explains why moving evaluation into the system supports warranted autonomy only inside the evaluator's oracle domain.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- **evidenced-by**: the trace is a Commonplace worked case where passing validation establishes a local result, while whether the retained change made the KB better remains a separate improvement claim.
- [Ingest: Self-Harness: Harnesses That Improve Themselves](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **evidenced-by**: the ingest records a split-gated harness loop where a candidate is accepted only under improvement-plus-non-regression conditions, directly instantiating antecedent, scope-indexed candidate admission.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **evidenced-by**: the ingest separates producing persistent harness updates from a task-solving agent benefiting from them, supporting the source's distinction between retained change and a warranted better-factory claim.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) -- **evidenced-by**: Auto Harness turns train traces into candidate `agent.py` edits, admits them through regression and score gates, and makes accepted code the next evaluated agent version.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **evidenced-by**: the system review separates product change, project-knowledge retention, installed plugin state, candidate rejection, and compounding claims in a way that materially exercises the source's declarations.

## Bidirectional Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) <-> source -- **extends**: a return link would help readers move from loop anatomy to the stricter requirement that an improvement claim declare which operative predecessor and successor states are compared.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) <-> source -- **extends**: a return link would connect the target/objective warrant gap to the source's state-comparison form for factory improvement claims.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) <-> source -- **extends**: a return link would let readers move from selection-pressure asymmetry to the source's requirement that the assessment relation be declared before it judges a successor.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) <-> source -- **extends**: a return link would specialize oracle-domain warrant to evaluator location, where an automated evaluator inside the factory changes actor allocation without automatically improving warrant.

## Reverse-edge Candidates

- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -> source -- **rests-on**: the proposal's ablation arms need the source's predecessor/successor, objective, horizon, and evaluator-location structure to state what a comparison would establish.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -> source -- **rests-on**: the reference note's claim that validation passing is a result rather than proof that the KB is better depends on the source's distinction between accepted result and warranted improvement.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -> source -- **rests-on**: the analysis distinguishes generated probes, accepted edits, retained component versions, and legitimate self-improvement boundaries; the source supplies the missing comparison standard for when those accepted successors count as better.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -> source -- **rests-on**: the analysis says Autogenesis has strong versioned mutation and rollback but weak selection validity; the source explains why retained successor state is not by itself a better-system claim.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) -> source -- **rests-on**: the review's warning against borrowing scalar-score gates where the oracle is weak depends on the source's evaluator-location and objective-threshold constraints.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -> source -- **rests-on**: the review treats benchmark frontier promotion as a harness-level acceptance gate; the source would clarify the additional state-comparison claim needed before treating a retained frontier candidate as a better factory.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Factory-learning mechanisms should be compared on the same causal job](../../../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) -- genuine overlap on causal jobs and operative retention, but rejected because the source already links the factory-learning premise and experiment-contrast limit that cover the necessary path.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- rejected because it specializes the pre-evaluation search-control problem, while the open-ended-improvement note gives the broader bridge to this source.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- rejected because it concerns search-control authority before adoption, not the source's predecessor/successor comparison relation.
- [Evidence bearing on an improvement objective](../../../../notes/definitions/evidence-bearing-on-an-improvement-objective.md) -- rejected as a new source link because the source already reaches it through self-improvement and objective links; adding it directly would not change reader work.
- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) -- rejected as outbound because it states Commonplace's local boundary, while the source is a transferable comparison form; the ablation and tag-readme trace candidates are more concrete uses.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- rejected because it catalogs candidate-forming mechanisms, whereas the source concerns how to compare operative states after a candidate route exists.
- [Note](../../../../types/note.md) -- rejected because the type contract governs notes generally and adds no specific reader need for the source's better-factory claim.
- [Instruction](../../../../types/instruction.md) -- rejected because the source found no procedure whose execution depends on this specific comparison form.
- [Run the compression bundle on one note](../../../../instructions/run-compression-bundle-on-note.md) -- rejected because note-revision workflow evaluation does not operationalize the source's factory-level predecessor/successor comparison.
- [Composition friction gate](../../../../instructions/composition-friction-gate.md) -- rejected because it tests note composition, not factory-improvement state comparison.
- [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) -- rejected as a direct evidence edge because it grounds the software-factory and factory-development vocabulary already reached through definitions; it does not itself supply the better-factory comparison.
- [Harness Engineering for Self-Improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md) -- rejected because it is a broad secondary map; `Self-Harness` and `Harness Updating Is Not Harness Benefit` provide sharper evidence for admission and update-versus-benefit distinctions.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- rejected as an outbound candidate because it is a close trace-to-change system review, but Auto Harness and Meta-Harness expose cleaner gate/frontier successor structure for this report.
- [GBrain](../../../../agent-memory-systems/reviews/gbrain.md) -- rejected because its SkillOpt and dream-cycle mechanisms are relevant to held-out mutation gates, but the review is too broad a memory-service analysis for a precise link from this source.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected as an outbound candidate because its review's strongest point is broad self-modifiability plus oracle limitations; that is better surfaced as a reverse-edge use of the source's comparison standard.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the source should be listed near proposal-selection and improvement-dynamics entries as the note that states the formal shape of a "this factory is better now" claim: declared objective, predecessor and operative successor states, succession route, evaluator location, boundary, and horizon.
- [Learning theory](../../../../tags/learning-theory-README.md) -- the source could be added to the factory-learning/self-improvement area because it separates retention, admission, measurement, and improvement warrant for deployed software-factory learning.
- [Foundations](../../../../tags/foundations-README.md) -- if this curated head keeps a self-improvement cluster, the source should be included as a foundational comparison discipline for improvement claims rather than as a general evaluation note.

## Synthesis Opportunities

- The source, [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md), [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md), and [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) imply a three-gap account of better-factory evaluation: objective-to-target warrant, criterion-to-quality discrimination, and evaluator-location/oracle-domain warrant.
- The source, [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md), and [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) imply a staged ladder for self-improvement claims: candidate search, admission into operative state, pairwise state comparison, and later contribution to further improvement.

## Maintenance Observations

None

## Flags

- The source is not a split candidate under the connect-report rule despite finding candidates across several collections. The candidates cluster around one assertion family: the structure of a better-factory comparison.
