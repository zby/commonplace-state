---
description: "Post-ingest connection discovery for Procedural Graphs, with independently assessed return links and evidence-use limits"
type: kb/reports/types/connect-report.md
source: "kb/sources/procedural-graphs-self-evolving-execution.ingest.md"
source_has_frontmatter: true
date: "2026-09-21"
depth: standard
---

# Connection Report: Ingest of Procedural Graphs

**Source:** [Ingest: Procedural Graphs](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md)

Separate post-ingest discovery pass under `kb/instructions/cp-skill-connect/SKILL.md`. The accepted ingest is the target. All entries below are proposals for future authoring; this pass changes only this report.

## Discovery Trace

**Setup and contracts:** Read the accepted ingest fully. Reused the already-loaded connect-report type, sources and reports collection contracts, destination READMEs, and context-engineering and self-improving-systems curated heads from the preceding snapshot pass. The target has frontmatter and domains but no tags. No tag-completeness shortcut was used. Sources authorize prospecting notes, reference, agent-memory-systems, agentic-systems, and other sources; instructions and workshops remain excluded. The known original arXiv URL needs no external prospecting.

**Fresh listing scans:** Regenerated complete title and description surfaces using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'`. Counts were notes 438/435, reference 162/161, agent-memory-systems 175/173, agentic-systems 21/18, and sources 440/440. Filtered the title surface with `consumption path|pre-existing signal|testing selected|proposal.selection|Workflow Memory|Autogenesis|GEPA|fixed decomposition|refinement.*source bundle|Procedural Graphs`. This confirmed the earlier candidate cluster and the newly tracked ingest. Scores are unavailable for these lexical searches.

**Focused body search:** Ran `rg -n -i 'localiz|incumbent|rejection|consumption'` over the three linked mechanism notes, the proposal-selection note, the automated-refinement proposal, AWM review, Autogenesis review, and GEPA ingest, with `--max-count 2`. Candidate judgments came from full target reads, including fresh rereads of all four notes nominated for inbound links, rather than from these snippets alone.

**Notes:** Freshly read the action-model, rule-ready-signal, retained-instruction, and proposal-selection notes. The ingest's first three connections survive the articulation test. Independently tested whether each note's own readers would benefit from the source case: the first gains a same-graph consumption contrast; the second gains a concrete identifier/fallback/inference decomposition; the third gains an evaluated frozen-model procedure-selection case. The proposal-selection note gains a finite-score gate case distinct from its direct-update and proof-gate contrasts. All four proposed inbound edges are checked under the loaded notes collection's `evidenced-by` authorization to sources, not under the ingest's outbound labels. The fixed-decomposition note remains useful outbound context, but the source does not exhibit an unreachable correction, so no reciprocal edge is proposed for that note.

**Reference:** The README and complete fresh title/description scans retain the automated-refinement proposal as the closest candidate. Its incumbent is a set of notes judged for prose quality; PG's incumbent is a procedural graph judged on task outcomes. The general proposal-selection note supplies the more useful connection. No reference edge retained.

**Agent-memory-systems:** The README, fresh listings, and previously read AWM review support a comparison between coarse domain-scoped workflow-file injection and per-step generated local guidance. This comparison is proposed outbound only; this pass does not assume that the historical code-grounded AWM review should acquire a newer paper comparison.

**Agentic-systems:** The README, fresh listings, and loaded Autogenesis review support comparison of revision scope and acceptance criteria: general extension lifecycle with a smoke gate versus graph-specific held-out task validation. No return link inferred from that shared mechanism.

**Sources:** Fresh listings identify GEPA, AWM, Autogenesis, and the accepted target. The loaded GEPA ingest provides the closest comparison of retained prompts versus graph edits and Pareto versus incumbent-based selection. AWM and Autogenesis ingests would duplicate the more concrete review comparisons; no extra links retained.

**Link following:** The retained-instruction note's authored `grounds` link led to the proposal-selection note, reread in full. The GEPA ingest's accepted-edit link and the fixed-decomposition note's diagnostic-richness link remain useful interpretive neighbors, but neither adds enough to this accepted ingest to justify another outbound recommendation. The notes collection permits inbound `evidenced-by` links only with a claim-level source use; matching topic or an existing outbound link supplies no such use by itself.

## Connections Found

The first three are already represented inline in the accepted ingest; they are retained as evaluated connections, not requests to duplicate footer links.

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: Table 3 varies consumption of the same graph, supporting a bounded claim that the runtime access path affects outcomes.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — **is-evidence-for**: last-procedure matching supplies the identifier signal, full-graph fallback supplies a superset, and model interpretation handles situational relevance.
- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) — **is-evidence-for**: validation selects a procedural checkpoint that later episodes reuse without changing model weights.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: already used in Learning Claims to distinguish editable graph topology/attributes from fixed tools, localization, guidance, and evaluation. PG identifies that boundary without showing that the fixed layer contains a mistake.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — **compares-with**: contrasts domain-scoped workflow-file injection with per-step localization and generated advice. Keep original AWM code evidence separate from the paper's adapted baseline.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) — **compares-with**: compares the scope of editable artifacts and strength of adoption checks; the reviewed branch's crash-oriented smoke gate and PG's held-out score gate assess different properties.
- [GEPA](../../../../sources/gepa-reflective-prompt-evolution.ingest.md) — **compares-with**: trace-driven prompt revision with Pareto parent selection contrasts with graph edits and one non-decreasing-score incumbent.

## Bidirectional Candidates

These are independently justified note → ingest return links for three existing ingest → note connections. Each return label is `evidenced-by`, authorized by `kb/notes/COLLECTION.md` for notes → sources. None follows automatically from reciprocity.

- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) → [ingest](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md) — **evidenced-by**: add a bounded empirical example to the note's distinction between retained representation and operative access. The same graph yields different results under full versus local generated guidance. Preserve the missing localized raw-injection arm and total-token overhead; do not claim graph structure alone caused the gain. This is the strongest return candidate and matches the ingest's recommended next action.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) → [ingest](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md) — **evidenced-by**: corroborate the note's staged selector mechanism with an implemented architecture as reported in the paper: exact action identifier, neighborhood extraction, full-graph fallback, and model interpretation. This is an illustrative mechanism case, not empirical proof that the identifier captures all relevant state.
- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) → [ingest](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md) — **evidenced-by**: give the note's presently compact argument a concrete instance of model-generated candidates selected by validation and retained for reuse. The construction study supports a selected procedural configuration, without verifying the refiner's explanation or general transfer.

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → [ingest](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md) — **evidenced-by**: the note's reader needs an explicit empirical gate case where rejecting a candidate is distinct from generating its successor. PG copies the incumbent, proposes edits, can reject before or after task validation, preserves the incumbent on rejection, and reuses accepted graphs in later solver calls. This complements its direct-update and proof-gate contrasts with a fallible measured-score gate. Independently authorized under notes → sources; the accepted ingest currently has no outbound link to this note. The proposed use should state that non-decreasing observed validation scores do not guarantee non-decreasing expected performance.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), as a return link — identifying fixed machinery does not demonstrate a required correction outside its effective update space. The ingest's outbound comparison is useful without a reciprocal evidential claim.
- [Failure explanations as search control](../../../../notes/failure-explanation-changes-later-branch-decisions.md), as an inbound evidential link — rejection records have a specified input path, but the source does not independently establish that a retained explanation changed a later proposal or improved search.
- [Retained system-definition artifacts and deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), as an inbound evidential link — the reported updates occur between training batches; the graph is fixed during test and within episodes. That does not establish adaptation during deployment.
- [Automated note refinement as a search over a fixed source bundle](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) — the shared incumbent pattern is better handled through the general proposal-selection note than by a weak system-proposal link.

## Index Membership

None. No selective index membership is necessary for this source record beyond its authored connections.

## Synthesis Opportunities

None. The accepted ingest supports concrete additions to existing notes; the present pass does not identify a distinct higher-order claim requiring a new artifact.

## Maintenance Observations

None newly established by this post-ingest pass.

## Flags

- **Grounding before inbound authoring:** the ingest's Quotes section is empty. A future evidence use must retain sufficient source quotes through the grounding workflow or explicitly mark its ingest link `(snapshot required)` and rely on the pinned snapshot. Do not create an unmarked evidential dependence whose support exists only in the ignored capture.
- **Authored use rather than footer-only backlink:** the notes collection requires source evidence to carry a claim in the body. Any accepted return edge should add or support a bounded sentence or paragraph, not merely append a reciprocal footer.
- **No universal graph claim:** Table 3 tests compound consumption treatments and lacks localized raw injection. The result supports its measured configurations rather than proving graphs generally outperform text memories.
- **Multiple topics:** the accepted ingest connects procedural representation, context selection, and learning governance. Keep those uses separate when revising theory notes; its source identity does not require splitting.
