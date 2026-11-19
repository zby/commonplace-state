---
description: "Pre-ingest discovery for Goedecke's AI-system design essay: semantic versus mechanical work, dormant expertise, and competing explanations of agent design failures."
type: types/connect-report.md
source: kb/sources/.snapshots/llms-are-terrible-at-designing-ai-systems.md
source_has_frontmatter: true
date: "2026-11-08"
depth: standard
---

# Connection Report: LLMs are terrible at designing AI systems

**Source:** [LLMs are terrible at designing AI systems](../../../../sources/.snapshots/llms-are-terrible-at-designing-ai-systems.md)

**Purpose and boundary:** Pre-ingest connection discovery only. The snapshot has frontmatter and was read fully. Its SHA-256 is `f52b7368087e53707eeaa25230689b3d9efc0d8a34c4196bb67933f3cd9c1da1`. No matching ingest exists at discovery time. Outbound suggestions below belong in a future name-paired ingest, not the immutable snapshot. Reverse suggestions are likewise deferred until that tracked ingest exists; no durable artifact should link to this local snapshot.

The essay reports agents choosing symbolic solvers or regexes for semantic tasks, including memory contradiction detection. It distinguishes three possible explanations: training-code history, reinforcement-learning environments without model API access, and broader software-design weakness. Its particularly useful observation is that a model reportedly explained the design's impossibility when challenged, despite having pursued it earlier. These are practitioner anecdotes and causal conjectures, not controlled comparisons or prevalence measurements.

## Discovery Trace

### Setup and search coverage

- Read the connect skill, global connect-report type and schema, source collection contract, report collection contract, and target in full before judging candidates. Read the theory collection contract before evaluating reverse edges.
- The sources contract authorises prospecting theory, reference, historical agent-memory-systems, agentic-systems, tags, and other sources. It excludes work and instructions. All six authorised local destinations were prospected. No external search, MCP service, or agent was used.
- Read each destination's `README.md`. Generated fresh complete first-heading surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of those six destinations. Recovered the truncated beginning of the theory and sources listings from the tool's retained output. Ordinary `rg` respects ignored snapshots; the supplied snapshot was explicitly read separately. Brief hits were treated as hits on their parent documents, never as link targets.
- Scanned descriptions using, for each destination, `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'symbolic|contradict|codif|regex|decision model|bounded judgment|software design|design judgment|complexity|semantic review'`. This was a focused description scan, not a full-body read of all matches. No numeric similarity scores were produced.

### Theory

**Breadth:** Broad enough to compare semantic/mechanical allocation and knowledge use; restricted to implications for KB design and operation, not general software-design commentary.

- The description scan selected the decision heuristics, relaxing signals, symbolic-operation comparison, and semantic-review note. Titles additionally surfaced bounded-judgment models and the scheduling note's contradiction-search case.
- Ran `rg -n -i 'regex|contradiction detection|semantic judgment|wrong tool|design error' kb/theory/ --glob '*.md'`. The scheduling note explicitly partitions corpus contradiction work into symbolic candidate handling and model judgments; this is a stronger connection than a generic shared interest in memory.
- Followed the decision-heuristics note's links to the scheduler-separation and deterministic-validation notes; read both fully. They bound the essay's recommendation: exact bookkeeping and structural checks still belong in code. The scheduler note points back to the symbolic-operation distinction already surfaced in descriptions; that broader target was not needed as another edge.
- Read the activation note fully after the failure-modes head pointed to it. Kept the prompted-explanation versus spontaneous-design contrast as an anecdotal instance, not proof that the relevant knowledge was present in the earlier live context.
- Read the decision heuristics, relaxing signals, semantic scheduling, bounded-judgment models, semantic-review note, and codification definition fully. Kept the first four direct relationships below; rejected relaxing signals and semantic review as additional edges because they would add less than the selected allocation and scheduling paths.
- Reverse pass: under theory's own `evidenced-by` permission to sources, selected the activation and allocation notes as potential consumers of a future ingest. These uses would qualify or illustrate their claims, not corroborate them by testing.

### Reference

**Breadth:** Target the shipped division between mechanical coordination and semantic review, rather than unrelated architecture or ADR history.

- The README and title scan identified review architecture and the validation contract. Ran `rg -n -i 'semantic.*(check|review)|deterministic.*(check|valid)' kb/reference/review-architecture.md kb/reference/validation-contract.md`, then `rg -n -i 'judgment|semantic|contradict' kb/reference/review-architecture.md`.
- Read review architecture fully. Its deterministic job protocol around external judgment gives a concrete Commonplace companion to the essay's tool-allocation problem. Kept one sparse `see-also` candidate. No claim that the essay validates the shipped subsystem, and no reverse implementation-dependency edge proposed.

### Agent-memory-systems

**Breadth:** Search for implemented contradiction handling, not all memory products.

- Read the historical survey landing and scanned its full title and focused description surfaces. Ran `rg -n -i 'contradiction|contradict' kb/agent-memory-systems/reviews/{graphiti,mem0,hindsight}.md`.
- Graphiti's LLM edge-resolution path supplied the clearest implementation comparison. Read its review fully. Kept the contrast between learned semantic judgment and formal state mutation, with its warning about silent invalidation.
- Mem0's search hits describe default ADD-only inference and skill/manual contradiction handling; not retained as another connection because Graphiti provides the more direct runtime mechanism. A further bounded search, `rg -n -i 'contradict|symbolic|LLM' kb/agent-memory-systems/reviews/hindsight.md | head -12`, exposed extraction and consolidation but no equally direct contradiction-specific landing in that slice; did not infer absence from this bounded search.

### Agentic-systems

**Breadth:** Test whether present system accounts expose an operational distinction between similarity and contradiction.

- Read the landing and scanned all first headings and the focused descriptions. Ran `rg -n -i 'contradict|regex' kb/agentic-systems/reviews/ kb/agentic-systems/reviews-archive/gbrain-garrytan.md`.
- Read archived GBrain fully. It records near-duplicate handling while the contradiction classifier has no non-test caller. Kept this as a comparison about wiring semantic checks, not an allegation that GBrain was built through the failure process in the essay. Academic Research Skills' conflicting recovery instructions were a keyword hit about a different problem and were not pursued.

### Tags

**Breadth:** Routing aids only. The source has no `tags:` field, so no source-tag-driven scan was required.

- Read the tags landing; scanned titles/descriptions. Ran `rg -n -i 'symbolic|codif|failure|judgment' kb/tags/{constraining,failure-modes,llm-reliability}-README.md`.
- Read constraining and failure-modes heads fully. Followed constraining's decision-heuristics/relaxing links and failure-modes' activation link. The failure-modes head declares `complete: true`; no by-tag `rg` was run for it. No by-tag search was otherwise needed.
- No direct tag edge kept: the sources contract lists tags as a prospecting destination but authorises no label to tags, and these heads served discovery rather than an indispensable direct reader need. No off-authorisation extension is requested. Source tags, if later assigned to the ingest, do not create membership in participating-collection tag listings.

### Sources

**Breadth:** Compare alternative explanations of agent design errors, with priority to practitioner reports whose evidence limits are inspectable.

- Read the sources landing and complete first-heading surface; the focused description scan identified the two practitioner accounts retained below.
- Ran `rg -n -i 'Goedecke|regex|RLVR|design.*(mistake|error)|contradiction detection' kb/sources/ --glob '*.md' | head -100`; treated this as a bounded body-search supplement, not an exhaustive body search. Followed the selected Goedecke ingest's existing comparison link to the Answer.AI ingest and read both fully.
- Ran `rg -n -i 'RLVR|training|grader' kb/sources/{sean-goedecke-what-requirements-dont-you-have,why-llms-cant-make-your-code-simpler}.ingest.md`. Kept both because their explanations distinguish missing acceptance context, reward-shaped overbuilding, and generic design weakness rather than collapsing them into one diagnosis.
- From Graphiti's neighborhood, ran `rg -n -i 'symbolic|contradiction|decision model' kb/sources/graphiti-temporal-knowledge-graph.ingest.md`. That ingest itself names the code-grounded Graphiti review as its primary technical companion. Kept the review instead of duplicating the source-side route.

### External

- No open-web prospecting. The original article URL is already supplied in snapshot metadata and is eligible for the future ingest's `derived-from` edge. Other URLs in the essay were not independently evaluated and are not recommended as new connections.

## Connections Found

All local targets below exist and have frontmatter. Each label is authorised for sources → that destination. These are candidates for a future ingest, not authored links.

- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) — **compares-with**: The essay's solver-versus-model choice connects to this note because the note separates specification, checking, interpretation, and total cost. It gives the ingest reader a way to evaluate the proposed replacement without turning an anecdote into a universal preference for model calls.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The reported agent could explain the flaw when challenged but did not reject it during design. This is an anecdotal instance of probe-retrievable expertise failing to guide unprompted work; it does not establish the cause or prevalence of that gap.
- [Semantic sub-goals that exceed one context window become scheduling problems](../../../../theory/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — **compares-with**: Both address corpus contradiction search. The note adds the missing scale boundary to the essay's batch/pairwise recommendation: candidate enumeration, pruning, and aggregation can stay mechanical while surviving pairs receive semantic judgments.
- [Language models for bounded judgments form an emerging category](../../../../theory/language-models-for-bounded-judgments-form-an-emerging-category.md) — **see-also**: The essay explicitly proposes a decision model. This note explains what judgment-specialized components change and which execution, calibration, coverage, and escalation properties need local evaluation. It does not establish that contradiction detection is solved by choosing that model category.
- [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md) — **compares-with**: The review supplies a concrete hybrid implementation for the essay's memory case: an LLM identifies contradicted facts and code records temporal invalidation. Its retained-history and hidden-authority caveats separate detecting conflict from being authorised to resolve it. Evidence is the review's pinned historical code boundary, not a new audit here.
- [GBrain](../../../../agentic-systems/reviews-archive/gbrain-garrytan.md) — **compares-with**: The archived review distinguishes near-duplicate similarity from contradiction judgment and records an unwired classifier. It helps readers check whether a semantic operation is actually called, rather than assuming that similar-looking curation machinery supplies it. It does not explain why that design arose.
- [Review system architecture](../../../../reference/review-architecture.md) — **see-also**: Commonplace's implemented responsibility split illustrates the useful boundary: code selects, snapshots, validates transport, and persists results; external reviewers supply judgment. This is a shipped companion, not evidence that the source's anecdotes apply to Commonplace.
- [What requirements don't you have?](../../../../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — **compares-with**: The same author previously attributed agent-added coordination to grader-shaped over-satisfaction and missing business context. Comparing the two essays helps a KB operator distinguish invented requirements from poor tool choice; their shared authorship is not independent confirmation of an RLVR cause.
- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — **compares-with**: This account makes absent change expectations and product trade-offs an alternative explanation of design disagreement. It gives the future ingest a reason to ask what context the agent received before calling a complex proposal a capability failure.
- [Original article](https://www.seangoedecke.com/llms-are-terrible-at-designing-ai-systems/) — **derived-from**: The future ingest analyses this already-captured external source. This is provenance, not a new research connection; no network verification was performed.

## Bidirectional Candidates

None. Useful return paths from theory are listed separately below rather than mechanically mirroring every outbound suggestion.

## Reverse-edge Candidates

These potential source-side authors exist. Their eventual destination must be the tracked ingest once created; no link to a nonexistent ingest or durable link to the snapshot is proposed.

- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → future ingest — **evidenced-by** under theory → sources: A compact practitioner illustration for the expert-witness pattern, where explicit questioning elicits a concern that failed to govern earlier work. Qualifies the claim; no test, exposure trace, or causal mechanism is established.
- [Codify-versus-LLM decision heuristics](../../../../theory/codify-versus-llm-decision-heuristics.md) → future ingest — **evidenced-by** under theory → sources: A failure report relevant to choosing an inadequate formalization before checking it against semantic examples. Illustrates the allocation risk; does not corroborate a cost or reliability advantage for the model alternative.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Operational signals that a component is a relaxing candidate](../../../../theory/operational-signals-that-a-component-is-a-relaxing-candidate.md) — The essay reports a dead end but supplies no paraphrase, integration, or distribution-shift tests. The decision-heuristics connection captures the allocation problem without implying those diagnostic signals were observed.
- [Semantic review catches content errors that structural validation cannot](../../../../theory/semantic-review-catches-content-errors-that-structural-validation.md) — Relevant to contradiction checking, but mostly duplicates the selected semantic/mechanical allocation paths. The essay does not test this note's claims about combining semantic checks.
- [Deterministic validation should be a script](../../../../theory/deterministic-validation-should-be-a-script.md) — Read as a boundary check, not a contradiction: structural validation has a specified predicate, unlike interpreting arbitrary memory claims. Its historical opening is not evidence about the current validator.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — Useful boundary context, but the selected corpus-scheduling note names the exact contradiction-search problem. No separate edge needed, and the essay does not test the scheduler note's reliability-cost conjecture.

## Index Membership

None. The source remains a local input awaiting ingest. No snapshot should be added to a durable index, and the sources collection is outside tag participation. Possible future ingest tags require a separate authoring decision, not index edits from this report.

## Synthesis Opportunities

None. The current allocation and activation notes already capture the main higher-order mechanisms. The essay's three training/design explanations remain competing conjectures, not grounds for another synthesis claim.

## Maintenance Observations

- The archived GBrain account contains a broken relative link to `kb/notes/definitions/conjectural-learning.md`; existence was checked and the target is absent. Leave correction to an authorised maintenance task. The selected comparison uses the account's explicit curation findings, not that missing definition.

## Flags

- **Split candidate for downstream analysis:** More than five local connections span tool allocation, knowledge activation, and design-context diagnosis, and the essay makes independent claims about each. Preserve the snapshot intact. A future ingest should separate these claims and their evidence limits; any eventual theory extraction should not import the entire essay as one premise.
- **Unresolved tension:** Failure of a proposed universal natural-language-to-logic pipeline does not show that every bounded formalization is impossible. Conversely, replacing it with an LLM does not provide guaranteed contradiction detection. The essay's categorical impossibility language and its claim that the task is relatively trivial need separate scrutiny.
- **Causal uncertainty:** No inspected training environment, API-access comparison, model cohort, or controlled design task distinguishes pretraining history, RLVR incentives, missing context, and design capability. Do not report any as the established cause.
- **Pre-ingest limit:** No durable source companion or retained quote pool exists yet. The report supplies discovery context only; no artifact, index, log, or snapshot was edited and no edge was authored.
