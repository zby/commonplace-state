---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/evidence/commonplace-revision-used-theory-guided-computational-search.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Commonplace theory-guided revision evidence

**Source:** [The 2026-08-30 Commonplace revision used retained theory to guide computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md)

## Discovery Trace

**Curated heads:**

- Treated `kb/notes/evidence/` as part of the `notes` source collection and read `kb/notes/README.md`, `kb/notes/tags-README.md`, `foundations-README.md`, and `self-improving-systems-README.md`. Neither matching tag head declares `complete: true`, so both required by-tag description scans were run. The self-improving-systems head exposed actor allocation, accumulation, reflective structure, and evidence placements as distinct candidate roles.
- Read the destination heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The reference head led to the canonical Commonplace frame. No external-system, source, type, or procedure head supplied a direct candidate.

**Title and description listing scans:**

- Generated a complete fresh title surface for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`, where `<destination>` was each of `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Generated the complete description surface for the same destinations with `rg '^description:' kb/<destination> --glob '*.md'`. The notes surface exposed the first-strategy, search-specialization, actor-allocation, accumulation, Commonplace-case, and evidence-quality candidates evaluated below.
- Ran by-tag description scans for `foundations` and `self-improving-systems` with `rg -l '^tags:.*\bTAG\b' kb/notes --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These retained the closure, cumulative-dependence, Commonplace classification, and Bitter Lesson bootstrap cluster while exposing broader compounding and autonomy claims that the episode does not establish.

**Body search:**

- `rg -n -i 'retained (project )?(theory|knowledge).*search|theory[- ]guided.*search|project state.*search|knowledge.*constrain.*revision' kb/notes --glob '*.md'` -- retained natural-language project state as the closest mechanism claim and the bootstrap and defense-portfolio notes as the closest strategic consequences.
- `rg -n -i 'human[- ]inclusive|operator.*(selection|judg|correction)|computational.*(search|selection)|global[- ]fit|credit assignment' kb/notes --glob '*.md'` -- retained methodological/computational closure and the broader Commonplace classification; rejected autonomy relocation because this one episode supplies no before/after allocation comparison.
- `rg -n -i 'later (work|episode|commit).*retained|retained (state|result).*later|recurrence|accumulat.*without compounding|informational dependence' kb/notes --glob '*.md'` -- retained the retained-result cumulativity test and rejected compounding claims that require a measured productivity contribution.
- `rg -n -i 'Git.*(reason|causal|transcript|evidence)|commit.*(reason|causal|transcript|evidence)|decision surface|production history|missing.*transcript' kb/notes --glob '*.md'` -- retained the production-time history limit and the checked-episode abstraction ceiling. The more specific decision-surface mining note was rejected because the source is not attempting to infer a rationale vocabulary from endpoint state.
- `rg -n -i 'first strategy|bootstrap.*Bitter Lesson|Bitter Lesson.*bootstrap|pre-computational|computation.*already' kb/notes --glob '*.md'` -- retained the hand-crafted-bootstrap condition and the defense-portfolio synthesis as the arguments the episode's successive operator corrections produced.
- `rg -n -i 'Commonplace.*(reflective|revision|episode|trace)|tag-readme.*trace|human-agent.*system|human-inclusive.*Commonplace' kb/notes --glob '*.md'` -- retained the broader Commonplace reflective-system case and the tag-README trace for synthesis rather than as a direct edge.
- `rg -n -i 'evidence case|causal trace|episode|human-inclusive|operative change|retained result' kb/types --glob '*.md'` supplied no type-level connection beyond the already loaded note contract.
- `rg -n -i 'commit.*(reason|evidence|lineage)|Git.*(reason|evidence|lineage)|human-inclusive|operator.*selection|revision.*episode|theory.*revision' kb/reference --glob '*.md'` -- retained `commonplace-declared-frame.md` because it is the canonical record that bounds Commonplace allocation claims. `commonplace-as-an-instrument.md`, design-rationale management, and the candidate-source survey remained adjacent but did not add a distinct source-to-target reader path.
- `rg -n -i 'theory[- ]guided|human.*selection|operator.*selection|retained.*theory|causal.*memory|faithfulness.*(tested|audit)' kb/agent-memory-systems --glob '*.md'` and the corresponding searches over `kb/agentic-systems` and `kb/sources` found external systems and studies with superficially similar learning or selection language, but none observes this local Commonplace episode or improves its evidence boundary.
- `rg -n -i 'record.*(human|computational).*contribution|episode schema|causal trace|decision record|operator.*selection|credit assignment|theory.*revision' kb/instructions --glob '*.md'` found no instruction that adds ordering, defaults, or stopping conditions specific enough for `operationalized-from`.
- External prospecting was skipped because no external target was supplied or already loaded. The target is grounded in local episode and Git evidence rather than an external source.

**Link following:**

- Followed all four authored source links. Theory-mediated self-improvement supplies the functional ladder; system use supplies the global-fit selection account; the mediation trace supplies the claimed-use versus causal-effect boundary; and proposal-selection supplies search, reject-capable evaluation, and retention. None is repeated as a candidate.
- Followed the bootstrap and defense-portfolio neighborhoods one hop. They preserve the exact distinction the operator corrections introduced: computation is already present, the bootstrap is a provisional first strategy, and missing global-fit selection machinery is a current bottleneck rather than an exemption from the Bitter Lesson.
- Followed the natural-language-state, open-ended-search, and code-complement neighborhoods one hop. Git inspection confirmed that commits `643908b9` and `fe7e893e`, which the source names as later consumers, introduced these pre-decisive search and model-mediated/symbolic-operation claims. The report keeps the three hub-level connections rather than every sibling created in those commits.
- Followed methodological closure, fixed-boundary reallocation, and autonomy relocation one hop. The episode directly profiles search/synthesis as computational and decisive global-fit selection as human, but it does not compare two states of allocation or measure intervention density, so only the closure profile passed.
- Followed cumulativity, accumulation/compounding, and later-episode measurement one hop. The named descendant commits establish a retained-result path at the repository level, while the source expressly lacks the counterfactual and productivity measurements required for compounding.
- Followed the broader Commonplace reflective-system case and its tag-README causal trace. The former provides the useful system-level placement; the latter has materially stronger commit-and-validator causal instrumentation and is used below for synthesis rather than a plain companion edge.
- Followed the production-history, decision-surface, and checked-episode neighborhoods. The source's contemporaneous episode record carries partial process evidence, while Git confirms changed artifacts and later descendants but cannot recover the omitted prompt, tool calls, or all causal inputs.
- Searched inbound links with `rg -n --fixed-strings 'commonplace-revision-used-theory-guided-computational-search.md' kb --glob '*.md'`. `system-use-selects-theory-fit-without-a-fixed-oracle.md` already authors the only inbound note edge. Two articles also link the record, but articles are not an authorised outbound destination for notes. Remaining hits were in the excluded workshop layer.
- Inspected `git log --follow` for the source and the stats of commits `2b406eea`, `4af042ca`, `d26bf3d7`, `643908b9`, and `fe7e893e`. This confirmed the source's relocation into `kb/notes/evidence/`, its doctrine-compliance revision, and the named descendant note clusters without treating commit adjacency alone as a semantic connection.
- Read the complete claims, scopes, caveats, and relevant-link surfaces of every retained candidate. All retained and rejected targets below have frontmatter, and all 21 candidate and index paths were verified to exist.

**Per-destination disposition:**

- `notes` (including `notes/evidence` and `notes/definitions`): ten outbound candidates passed the articulation and label tests. Seven warrant useful return paths. No term required a new `defined-in` edge.
- `types`: no type contract bears specifically on the episode's search, allocation, recurrence, or causal-evidence claims.
- `reference` (including `reference/definitions`): the canonical Commonplace frame passed as the record bounding the human-inclusive attribution. Other Commonplace descriptions were either already reached through the broader reflective-system case or only adjacent.
- `agent-memory-systems`: no reviewed external memory system supplies evidence about this local episode.
- `agentic-systems`: no external harness analysis supplies a distinct reader path for the Commonplace case.
- `sources`: no tracked external ingest corroborates the episode-specific Git and operator-feedback account more directly than the retained local evidence.
- `instructions`: no procedure met the narrow `operationalized-from` trigger.

## Connections Found

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **exemplifies**: the episode is one bounded instance of computation participating from the start while human judgment remains at global-fit selection, exactly the first-strategy configuration whose scalability the general note leaves open.
- [The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) -- **extends**: it turns the episode's successive rejection of defense-portfolio and handcraft-now framings into the resulting four-level position—narrow compatibility, working conjecture, provisional first strategy, and open comparison.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- **exemplifies**: the retrieved Commonplace theory, intent, branch history, and constraints are a bounded observational case of project state specializing model search, while the absent withholding or replacement control preserves the conjecture's stated evidence limit.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- **exemplifies**: the model searched among formulations, distinctions, experiments, and repository changes before the operator supplied decisive global-fit selection, instantiating pre-decisive allocation without claiming the allocation was optimal.
- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md) -- **extends**: this is the later descendant claim named by the episode record; it develops the source's model-mediated repository search into a two-operation architecture where installed code and tools execute symbolic consequences independently of prompt reinterpretation.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- **exemplifies**: the episode's function-level record separates computational proposal and synthesis from human decisive selection, showing why production volume cannot substitute for an actor-allocation profile.
- [Accumulation counts dependence through the retained result, not through the evidence it caused](../../../../notes/accumulation-counts-dependence-through-the-retained-result.md) -- **exemplifies**: the named later commits read and transformed the revised repository state rather than independently replacing it, giving a bounded retained-result dependence claim without a matched substitution test.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- **exemplifies**: this is a second human-inclusive Commonplace pathway in which retained self-representation is interpreted, revised, installed, and used later, but with weaker causal instrumentation than the tag-README case.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) -- **exemplifies**: the omitted complete prompt and tool-call transcript cannot be reconstructed from the resulting commits; Git carries artifact state and descendants, while only the contemporaneous episode record preserves the available production account.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **exemplifies**: Git warrants the bounded claims that artifacts changed and later work used them, but the incomplete process record and absent intervention prevent those outcomes from identifying every causal input or licensing a general theory-guided-search effect.
- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) -- **evidenced-by**: the canonical boundary record qualifies the episode's human-inclusive allocation claim by placing harness-loaded agents inside Commonplace while keeping provider weights and inference infrastructure outside unless an explicit departure is declared.

## Bidirectional Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) <-> source -- source to bootstrap is **exemplifies**; bootstrap to source is **evidenced-by**, because the episode records one present-day configuration with computational search, human global-fit selection, retained revision, and no demonstrated scalability advantage.
- [The Bitter Lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) <-> source -- source to the portfolio is **extends**; the portfolio to source is **evidenced-by**, because the episode preserves the actual sequence of operator corrections that narrowed the position from a broad defense to a first strategy and open comparison.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) <-> source -- source to project-state specialization is **exemplifies**; project-state specialization to source is **evidenced-by**, because the episode supplies a project-specific observational case and explicitly records the missing ablation that prevents a causal estimate.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) <-> source -- source to closure is **exemplifies**; closure to source is **evidenced-by**, because the episode names search, synthesis, global-fit judgment, acceptance, and retention separately enough to demonstrate a mixed actor-allocation profile.
- [Accumulation counts dependence through the retained result, not through the evidence it caused](../../../../notes/accumulation-counts-dependence-through-the-retained-result.md) <-> source -- source to cumulativity is **exemplifies**; cumulativity to source is **evidenced-by**, because the three named commits preserve a repository-level earlier-result-to-later-revision path while leaving the controlled substitution unrun.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) <-> source -- source to the broader classification is **exemplifies**; the classification to source is **evidenced-by**, because the episode adds a theory-revision pathway beside the canonical tag-README pathway while retaining a human cut set and uneven evidence.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) <-> source -- source to the history limit is **exemplifies**; the history note to source is **evidenced-by**, because the episode shows precisely which production facts Git preserved and which unrecorded LLM-process facts became unrecoverable.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) -- rejected because the episode shows later use of retained state but does not establish that the earlier revision was a benefit that made later improvement cheaper, broader, more reliable, or more productive; the narrower cumulativity note fits the observed evidence.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- rejected because no displaced productivity measure, frozen-state comparison, or reinvestment trace was retained.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- rejected because one mixed-allocation episode locates human judgment at global fit but does not show that increasing autonomy moved the frontier or changed improvement per human judgment.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) -- rejected because the source is not mining a rationale vocabulary from endpoint state; the broader production-history note captures the actual missing-transcript limit without importing that mechanism.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- rejected because the source does not infer a general rule from acceptance alone. Its concern is incomplete causal attribution and later compliance defects, a different evidence boundary.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) -- rejected because the episode records no intended-path failure or successful fallback; successful repository writes being semantically imperfect is not the path-deviation mechanism that note claims.
- [The tag-readme change as an observed causal-connection trace](../../../../notes/evidence/tag-readme-trace-observed-causal-connection.md) -- rejected as a direct edge because it is a different Commonplace episode rather than a premise, mechanism, or general class. The broader Commonplace classification supplies the traversal path, and the two traces are compared only in the synthesis opportunity below.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- rejected because its shipped-system survey is adjacent to this instance of agent search, but the target's existing proposal-selection link and the broader Commonplace classification already supply the useful paths; a source-to-reference `see-also` would add little.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- rejected because the episode does not close that reference's missing outside-transfer, full-lineage, or faithfulness tests. Treating any internal use episode as evidence for the instrument claim would overread both artifacts.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- rejected as one of several descendants in commit `643908b9`: commit lineage alone is not a semantic edge, and the open-ended-search plus project-state notes carry the source-relevant relation without linking every sibling.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- add under **Placements** as a second Commonplace episode: it profiles theory-guided computational search, human global-fit selection, retained revision, and later use while making the missing causal intervention explicit.

## Synthesis Opportunities

- The source, [the tag-README causal trace](../../../../notes/evidence/tag-readme-trace-observed-causal-connection.md), and [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) together imply an observability gradient across Commonplace improvement paths: symbolic transitions with tests and explicit consumers can support commit-level causal reconstruction, while semantic LLM-mediated revision can leave Git-level retention and later dependence visible but causal prompt inputs underidentified unless captured at production time. No current note compares the two Commonplace cases on that evidence axis.

## Maintenance Observations

- The source declares `GPT-5.6 Pro` inside its episode boundary, while [the canonical Commonplace frame](../../../../reference/commonplace-declared-frame.md) places harness-loaded agents inside but provider weights and inference infrastructure outside. The source should eventually clarify whether `GPT-5.6 Pro` names the inside agent process only or whether it deliberately departs from the canonical frame; the present wording leaves actor allocation and reflective coverage ambiguous.

## Flags

- **Split candidate:** the artifact independently carries claims about theory-specialized search, human/computational allocation, cross-episode cumulativity, and the evidential ceiling of Git plus an incomplete episode record. Because it is a bounded evidence artifact, preserving one case narrative may still be preferable; review whether to extract those theory-facing conclusions into separate notes or mark the case explicitly as a multi-claim synthesis rather than silently treating the title claim as atomic.
