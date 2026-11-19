---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/lightweight-search-control-does-not-license-adoption.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Lightweight search control allocates further search without licensing adoption

**Source:** [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md)

## Discovery Trace

**Source and authorisation:**

- Read the source note, `kb/notes/COLLECTION.md`, and `kb/reports/types/connect-report.md` in full. The source defines lightweight search control by its limited authority: it may allocate investigation, probing, continuation, suspension, or abandonment, but cannot by itself make a change operative. Cost, formality, and confidence do not determine that authority.
- The notes contract authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `work`. The reserved `external` destination was skipped because no external candidate was supplied or already loaded.
- Read each authorised destination's main `README.md` and the source's three tag heads: `kb/notes/foundations-README.md`, `kb/notes/computational-model-README.md`, and `kb/notes/self-improving-systems-README.md`. None declares `complete: true`, so all three by-tag description sweeps were run.
- Searched for existing backlinks with `rg -n 'lightweight-search-control-does-not-license-adoption|Lightweight search control allocates further search' kb/ --glob '*.md'`. Durable inbound edges already exist from natural-language project state, intent control, backtracking, search-controller evaluation, and failure-explanation notes; workshop hits were excluded.

**Fresh title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each of the seven authorised local destinations. The notes surface exposed the backtracking, controller-evaluation, candidacy-evidence, false-positive, autonomy, productive-deferral, and delayed-program-theory clusters. Other destinations exposed Commonplace candidate channels, Reflexion, Autogenesis, HippoRAG, staged canary acceptance, adaptive pathways, and discovery-only instructions.
- Ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding `computational-model` and `self-improving-systems` sweeps. These retained the authority-boundary and search-controller candidates and exposed `candidacy-evidence-licenses-escalation-not-acceptance.md` as the closest cross-domain formulation.
- Ran filtered destination description listings with `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'search|candidate|branch|probe|evaluat|adopt|accept|select|gate|triage|explor'` over `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`. The types title surface contained no semantic candidate beyond the operative-change definition in notes, so types body prospecting was skipped.

**Notes body search:**

- `rg -n -i 'lightweight search control|search judgment|license(s|d|ing)? adoption|licensing adoption' kb/notes/ --glob '*.md'` -- confirmed the direct cluster and identified all five existing inbound edges, which were not re-proposed as target-side candidates.
- `rg -n -i 'search control|search controller|branch (choice|decision|allocation)|allocate.*search|search.*allocat' kb/notes/ --glob '*.md'` -- kept backtracking, controller evaluation, delayed program theory, and the failure-explanation application; the last was rejected as a new outbound edge because the stronger mechanism and evaluation notes already provide the source-side read path.
- `rg -n -i 'provisional.*(judgment|branch|search|evaluation)|stronger evaluation|subject to.*evaluation|worth investigating' kb/notes/ --glob '*.md'` -- kept candidacy evidence and productive deferral because they respectively distinguish escalation evidence from verdict evidence and make continued search converge on a later decision.
- `rg -n -i '(adopt|accept|retain).{0,60}(candidate|change)|operative change|non-adoption|reject-capable' kb/notes/ --glob '*.md'` -- kept the operative-change definition, false-positive asymmetry, and warranted-autonomy consequence; rejected later-stage adoption-versus-entrenchment as a synthesis input rather than a direct search-control edge.
- `rg -n -i '(cost|confidence|formality).{0,50}(authority|acceptance|adoption)|authority.{0,50}(cost|confidence|formality)' kb/notes/ --glob '*.md'` -- found no competing definition of lightweight authority; adjacent cost and entrenchment notes address different decisions.

**Other-destination body search:**

- Ran `rg -n -i 'lightweight search control|search controller|search allocation|worth investigating|stronger evaluation|non-adoption|reject-capable|exploration controller|candidate.{0,50}(accept|adopt|reject)|accept.{0,50}candidate' kb/<destination>/ --glob '*.md'` over `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Read `where-change-candidates-come-from-in-commonplace.md` in full. It passed because Commonplace's connect reports, freshness signals, checks, and agent initiative produce search inputs that still require an explicit later maintenance or triage act before becoming operative.
- Read Reflexion through its complete claim-bearing, comparison, write-side, and read-back sections. It passed as a bounded case in which failure-derived reflections change the next same-instance attempt while remaining advisory and unpromoted to cross-task authority.
- Read Autogenesis through its resource/evolution split, current implementation, mutation safety, evaluation, and authority sections. It passed as a qualified case: the paper separates Reflect–Select–Improve from Evaluate–Commit, while the inspected current runtime shows how weak gates can preserve mechanical staging without sufficient semantic warrant.
- Read the canonical `cp-skill-connect` instruction in full. It passed as an operationalization because it fixes discovery order, authorised prospecting, articulation and label tests, the report-only output, and the explicit prohibition on mutating or adopting candidates.
- Evaluated HippoRAG, the AI Agents in Depth analysis, and Dynamic Adaptive Policy Pathways. Their superficially similar authority distinctions concern, respectively, a Commonplace borrowing recommendation rather than an observed promotion path, canary eligibility versus deployment, and monitoring information versus action triggers; none was retained as evidence for search allocation versus adoption.

**Link following:**

- Read the complete backtracking, search-controller, failure-explanation, intent-control, natural-language project-state, candidacy-evidence, false-positive, warranted-autonomy, productive-deferral, current-task-entrenchment, and program-theory notes. Kept candidates occupy distinct mechanism, evaluation, application, and governance roles rather than repeating the source's definition.
- Followed the source's two authored links into open-ended search allocation and the proposal-selection loop. Candidates that merely restated those functions were rejected; false-positive generation survived because it explains the consequence asymmetry, and warranted autonomy survived because it bounds delegation of the downstream gate.
- Followed existing inbound neighborhoods rather than proposing already-authored return edges. Source-side links were retained only where following them from the definition adds a new reader need; backtracking and controller evaluation pass that test, while intent and one implementation conjecture do not.
- Verified all 22 retained, rejected, synthesis, and index paths with `test -f` before writing this report.

## Connections Found

- [Operative change](../../../../notes/definitions/operative-change.md) -- **defined-in**: supplies the horizon- and consumption-path-relative threshold that the source's search judgment is explicitly unauthorized to cross.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **mechanism**: explains how restoring an earlier usable state prevents a branch trial from acquiring de facto adoption consequences merely because later work has begun to depend on it.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **extends**: supplies the matched, distributional evaluation design appropriate to a controller whose own judgments do not claim acceptance authority.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- **extends**: applies limited-authority branch control to open-ended program modification, where provisional theory-guided choices must remain correctable by delayed consequences.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- **extends**: restates the same authority boundary for staged evidence, showing why pursuit-worthiness may justify assessment cost without distributing warrant to the eventual verdict.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- **mechanism**: explains why search can safely operate under weaker authority than evaluation: bad generated candidates meet a downstream filter, while bad acceptances pass the last filter and acquire behavioral force.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **extends**: develops the actor-allocation consequence—automating branch search and automating adoption are not equivalent transfers because only the latter requires an oracle strong enough to warrant what becomes operative.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- **extends**: adds the conditions under which probing, suspension, and maintaining alternatives remain controlled search rather than hidden commitment or indefinite delay.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- **evidenced-by**: documents connect reports, freshness signals, mechanical checks, and agent initiative as candidate-producing channels whose outputs still await an explicit maintenance or triage decision.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) -- **evidenced-by**: inspected same-instance loops turn failure traces into advisory reflections that alter the next attempt, but do not promote those reflections into reusable cross-task authority.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **evidenced-by**: its paper architecture separates Reflect–Select–Improve from Evaluate–Commit, while the code-grounded review qualifies the result by showing that mechanical staging can coexist with semantically weak commit gates.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) -- **operationalized-from**: fixes a complete discovery procedure whose only output is a candidate report and whose mutation prohibition prevents discovered edges from acquiring adoption authority inside the same operation.

## Bidirectional Candidates

- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) <-> source -- **grounds** from the program-theory note: the source names the limited authority of the provisional search judgments that guide modification before delayed evidence arrives.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) <-> source -- **extends** from the candidacy-evidence note: the source generalizes its evidence-specific routing/verdict separation to investigation, probing, continuation, suspension, and abandonment judgments.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) <-> source -- **grounds** from the false-positive note: the source supplies the authority distinction that explains why search errors normally cost evaluation effort while acceptance errors acquire force.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) <-> source -- **grounds** from the deferral note: the source distinguishes authorization for another bounded probe from authorization to adopt the deferred choice.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) <-> source -- **rests-on** from the reference description: its distinction between ephemeral connect findings and the later act that authors links depends on the source's search-versus-adoption boundary.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) <-> source -- **is-evidence-for** from the review: code-inspected failure reflections have reliable same-instance routing force but no cross-task promotion path, materially bearing on the limited-authority category.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) <-> source -- **is-evidence-for** from the system analysis: the observed generator/evaluator/commit separation and weak-gate qualification jointly bear on why candidate production and operative adoption need distinct authority.
- [Connect — Discovery Only](../../../../instructions/cp-skill-connect/SKILL.md) <-> source -- **rests-on** from the instruction: for meta-readers, the report-only write boundary and prohibition on applying discovered links depend on this theoretical separation between search and adoption.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- rejected as a new outbound edge because it is a narrow instance already linked inbound to the source; backtracking and controller evaluation supply the more useful source-side mechanism and evaluation routes.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- rejected because it already links inbound and explains whether intent causally changes a branch ordering, not the separate authority that ordering possesses.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- rejected because it already links inbound and offers one conjectured implementation of search control; the source's general definition does not need to privilege that substrate.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- rejected as a direct edge because it separates reversible adoption from a later, costlier commitment rather than search allocation from adoption; the possible three-stage authority relation is recorded below as synthesis, not assumed.
- [Measuring autonomy well enough to see it improve is an open problem](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) -- rejected because its search/evaluation stakes paragraph already derives the distinction through the retained false-positive and warranted-autonomy candidates; a direct link would duplicate that route.
- [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md) -- rejected because its signpost/trigger distinction separates monitored information from a rule that activates a prepared action, not a search-routing judgment from a later adoption judgment.
- [HippoRAG](../../../../agent-memory-systems/reviews/HippoRAG.md) -- rejected because “use generated triples as candidate routing state, not accepted claims” is a Commonplace borrowing recommendation in the review; HippoRAG's inspected system does not itself expose the staged claim-promotion path needed as evidence here.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) -- rejected because canary eligibility versus deployment is a valuable later-stage operational-authority distinction, but it does not identify the candidate-producing judgment as lightweight search control.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- the selective head could place this note under “Scheduling & Orchestration” as the authority contract for a search controller: it selects branches and probes without owning the downstream acceptance transition.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the selective head could place this note immediately after the proposal-selection subtype under “Update architecture,” separating search authority from the evaluation and operative-retention functions already named there.

## Synthesis Opportunities

- [Lightweight search control](../../../../notes/lightweight-search-control-does-not-license-adoption.md), [candidacy evidence](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md), and [current-task fit versus entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) together suggest a three-stage authority ladder: nominate or allocate further work, adopt reversibly for a bounded current use, then entrench through dependencies. Evidence calibrated for one transition does not automatically license the next. No retained note currently states and tests that combined ladder.

## Maintenance Observations

None

## Flags

None
