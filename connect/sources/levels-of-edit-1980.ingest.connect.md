---
description: "Accepted-ingest connection discovery for JPL's edit levels, separating existing outbound comparisons from independently justified inbound candidates."
type: types/connect-report.md
source: "kb/sources/levels-of-edit-1980.ingest.md"
source_has_frontmatter: true
date: "2026-11-13"
depth: standard
---

# Connection Report: The Levels of Edit, Second Edition

**Source:** [Ingest: The Levels of Edit, Second Edition](../../../../sources/levels-of-edit-1980.ingest.md)

## Discovery Trace

### Boundary, contracts, and incumbent edges

Read the connect skill, connect-report type, source ingest in full, sources and reports collection contracts, and ingest-report type before discovery. For inbound assessment, also read the theory and reference collection contracts, note type, design-proposal type, and tags collection contract. This report is the only write. No workers, external search, source modification, index modification, or commits were used.

The ingest distinguishes three axes: commissioned service scope, sequencing by what later changes can discard, and sequencing by remaining feasible options. It also separates detection from repair authority and commissioned scope from effort estimates. Its evidence is practitioner description, not a comparison of revision orders or proof that a particular service taxonomy is optimal.

The source contract authorizes prospecting theory, reference, the historical agent-memory-systems collection, agentic-systems, tags, and other sources. Theory permits `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`, and `defined-in` only for definitions. Reference permits only `see-also`. Sources and both systems collections permit `compares-with` and `see-also`, with `is-evidence-for` additionally available for agent-memory-systems. External permits `derived-from` and sparse `see-also`. Tags are a navigation surface, not a destination with an authorized formal label in the sources table. Workshop and instruction destinations are excluded; links from candidates into those collections were not pursued as connection targets.

**Already authored outbound edges, not new candidates:**

- The ingest already compares its commissioned bundles with [the low-degree-of-freedom heuristic](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md). This is an authorized sources → theory `compares-with` use, not evidence for or against the heuristic.
- It already points to [the improvement-procedure proposal](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md), including in its recommended next action. Under sources → reference, this is an adjacent `see-also` connection; a formal `compares-with` label would not be authorized for this pair.
- It already compares JPL's responsibilities with [the author–executor boundary](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md). This is an authorized `compares-with` use, not corroboration of the decision-allocation rule.
- The original NASA PDF is already linked in the Summary and identified in metadata. External `derived-from` is authorized, but adding the same source again would be redundant. No open-web prospecting was performed.

Ran `rg -n 'levels-of-edit-1980|19800011701|Levels of Edit' kb --glob '*.md' --glob '!levels-of-edit-1980.ingest.md' --glob '!*.connect.md'`. Hits outside the ingest were workshop research references; those were not followed or proposed. A final exact check, `rg -n -F 'levels-of-edit-1980.ingest.md' kb/theory/ kb/reference/ kb/sources/ kb/tags/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`, found no authored inbound links. Thus the reverse edges below are missing-edge candidates, not a restatement of existing backlinks.

### Discovery surfaces and queries

**Curated heads:** Read `README.md` for all six authorized local destinations. The theory landing routes through tags rather than enumerating claims. The reference landing identifies the review system. The two systems landings establish their system-analysis focus; the sources landing explains ingest identity. The tags landing exposed review-system, document-system, goal-prioritization, and prose-readability as promising neighborhoods. After the title, description, and body scans, read those four heads fully. The ingest has no `tags:` field, so there were no matching source-tag scans. Review-system and prose-readability declare `complete: true`; no by-tag `rg` was run for either. Their completeness covers participating library collections, not sources.

**Fresh complete title surfaces:** For each of `theory`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `tags`, ran `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'`. Scanned the complete returned title surfaces. The known three targets remained prominent; new shortlists included the three-simplification-passes evidence note, acceptance/repair-session separation, criteria/process invalidation, dynamic variable ordering in CSPs, and set-based rework. Systems titles did not suggest an editorial-service comparison.

**Description scans:** For each of the same six destinations, ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'edit|revis|repair|scope|order|commission|delegat|authority|writing|effort|checklist'`. The theory shortlist distinguished semantic-preserving rewrite evidence from unrelated authority and memory work. Reference exposed ADR 080 and the authority-grades proposal. Sources exposed CSP ordering, set-based rework, and several writing critiques. Systems hits concerned memory repair or runtime authority, not commissioned edit services. Brief hits were treated as hits on their companion document; no brief is a candidate target. The truncated description output was recovered from the tool's full-output file.

**Theory body search:** Ran `rg -n -i 'edit levels|editorial|invalidation|substantive.{0,30}(edit|repair)|detection.{0,40}(repair|authority)|repair.{0,40}(scope|authority)' kb/theory/ --glob '*.md'`. Kept the three-simplification-passes comparison; examined acceptance/repair-session separation and criteria/process invalidation but rejected direct connections to their distinct mechanisms. Broad editorial-index hits were keyword overlap, not useful links.

**Reference body search:** Ran `rg -n -i 'edit levels|higher-order concerns|lower-order concerns|commissioned|outside.{0,30}(scope|authority)|claim.{0,20}hand.back' kb/reference/ --glob '*.md'`. The default composition is the closest local reader need: its rationale concerns discarded work, not service bundles. ADR 080 supplies a useful authority-boundary comparison but not a reason to amend its historical account with JPL. The authority-grades proposal was evaluated after following the default-composition proposal's link.

**Other sources body search:** Ran `rg -n -i 'edit levels|substantive edit|commissioned|least.flexible|remaining values|reducing rework' kb/sources/ --glob '*.md'`. Read the CSP and set-based rework ingests fully. Kept the CSP comparison to separate actual variable-order selection from scope bundles. Rejected set-based rework as an additional link because its active learning and convergence mechanism is not present in JPL's level scheme.

**Systems body searches:** Ran `rg -n -i 'edit levels|substantive edit|editorial scope|repair authority|commissioned edit' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` (no matches), then `rg -n -i 'copyedit|copy.edit|language edit|substantive.{0,20}edit|publication management' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`. The latter returned an archived Ecdysis report about an external harness editor and admission controls. Rejected at snippet level: executable harness mutation is not editorial service commissioning, and the apparent match does not name a useful shared comparison. With no plausible system-specific mechanism, stopped after heads, titles, descriptions, and these focused searches; no systems candidates were kept.

**Tags body search:** Ran `rg -n -i 'edit|revision|order|commission|repair' kb/tags/ --glob '*.md'`. Read the four heads named above. Goal-prioritization already has manually curated source entries and explicitly excludes sources from generated membership; it is the best optional navigation placement. The review-system and prose-readability heads supplied theory/reference neighborhoods, not automatic membership for this ingest.

**Cross-collection adjacent-concept pass:** Ran `rg -n -i 'manuscript condition|extraordinary (functions|services)|detect.{0,50}repair|scope.{0,40}effort|commission.{0,40}(scope|work)|fewest.{0,25}(options|values)' kb/theory/ kb/reference/ kb/sources/ --glob '*.md' --glob '!*.brief.md'`. The source itself carries the clearest scope/effort distinction. Other hits concerned maintenance capacity, conversation repair, or exact constraint search. No additional evidence-bearing candidate survived this pass. There are no semantic similarity scores: discovery was repo-local text traversal.

### Link following and independent inbound assessment

Read the three already linked artifacts in full. From the low-degree-of-freedom note followed its links to the CSP ingest, bounded-context decomposition heuristics, and the author–executor note. From the author–executor note followed productive deferral; from there followed set-based rework. From the improvement-procedure proposal followed authority grades and ADR 080. Read these candidate artifacts fully; did not follow excluded workshop/instruction destinations as targets. The three-simplification-passes evidence note links a neighboring two-rewrites experiment; its independent experiment is not needed to justify the scope-versus-coverage comparison, so no extra edge to that neighbor was kept.

For each of the three existing outbound targets, assessed the reverse reader need afresh. The proposal benefits from a warning against using JPL levels to justify its order. The sequencing note benefits from separating option counts from a seemingly similar editorial hierarchy. The author–executor note benefits from a concrete commissioned-service comparison in which permitted detection exceeds permitted repair. These are independent adjacent-context uses, not reciprocal obligations. None warrants `derived-from` or `abstracted-from`: the local artifacts do not claim to originate in JPL. None warrants corroborating `evidenced-by`: JPL does not test the local mechanisms. Theory and reference each authorize sources-bound `see-also` for the retained purposes.

### Candidate origins

- kb/theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md — titles, descriptions, body-search, curated-head
- kb/sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md — titles, descriptions, body-search, link-following
- kb/reference/proposals/one-improvement-procedure-over-atomic-instructions.md — known, titles, body-search, curated-head, link-following
- kb/theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md — known, titles, descriptions, link-following, body-search
- kb/theory/fix-what-the-executor-cant-determine-not-what-it-will.md — known, titles, link-following

## Connections Found

These are additional outbound candidates only. The three incumbent local outbound links are accounted for in Discovery Trace, not proposed again.

- [Three simplification passes exposed different clarity–precision tradeoffs](../../../../theory/evidence/three-simplification-passes-exposed-different-tradeoffs.md) — **compares-with**: JPL's commissioned edit types connect to this experiment because both distinguish the scope of an editing operation from a single stronger/weaker ranking. The experiment shows a local pass detecting and deferring a conceptual ambiguity while broader recasting has different benefits and risks. This gives a Commonplace consumer a concrete comparison for detection coverage versus repair scope. JPL does not explain or validate the experiment's ranking, and the experiment does not test JPL's bundles. Authorized by sources → theory.
- [Dynamic Variable Ordering In CSPs](../../../../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) — **compares-with**: JPL connects to this ingest because its included-service levels are not a next-decision selection rule, whereas minimum remaining values selects the next variable from current feasible sets. Following the link lets a reader distinguish scope commissioning from an empirically studied execution-order mechanism, including fail-first and its exact-search limits. It is not evidence that one editorial order outperforms another. Authorized by sources → sources.

## Bidirectional Candidates

None. Independently useful inbound candidates to the already linked artifacts are listed below rather than duplicated here. No return link from the two additional outbound targets is recommended: the rewrite experiment's evidence boundary does not need a historical taxonomy, and the CSP ingest is adequately about exact search without an editorial detour.

## Reverse-edge Candidates

All three edges below are absent in the searched library surfaces. Each is a candidate for a future target-side edit, not an edge authored by this pass.

1. [One improvement procedure over atomic instructions](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) → [this ingest](../../../../sources/levels-of-edit-1980.ingest.md) — **see-also**. At the default-composition discussion, the proposal connects to JPL because a service-scope hierarchy is a tempting but invalid justification for execution order. A reader evaluating the proposed higher-order-first rule gains a concrete contrast: JPL specifies included work; the proposal argues that upstream decisions can discard downstream wording work. This is adjacent comparison context under reference → sources, which authorizes `see-also`. Do not use reference → reference `compares-with` across this different destination pair, claim historical influence, or claim that JPL tests the proposed order. The design remains unadopted.
2. [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) → [this ingest](../../../../sources/levels-of-edit-1980.ingest.md) — **see-also**. Near the agent-workflow application or scope discussion, this note connects to JPL because an edit's broad substantive scope does not determine how many viable choices it has, nor make its numbered service tier a sequencing prescription. Readers transferring the heuristic to revision gain a specific non-example of option-count ordering. Authorized by theory → sources as sparse adjacent context. Not `evidenced-by`: the source neither tests nor refutes optionality preservation or fail-first. The reader need is transfer-boundary clarification, independently of the ingest's existing comparison in the other direction.
3. [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) → [this ingest](../../../../sources/levels-of-edit-1980.ingest.md) — **see-also**. At the actor/time/evidence distinction or authority boundary, this note connects to JPL because institutional minima and commissioned responsibilities fix permitted work while a language-level check can expose a substantive problem that requires work beyond that commission. A consumer gets a concrete editorial example of why recognizing a defect does not authorize its repair or determine when it should be addressed. Authorized by theory → sources. Keep this an illustration and comparison: JPL does not test allocation by authorized evidence, competent execution, or productive deferral. Do not present the institutional bundles as optimal agent delegation policy.

## Off-authorisation Candidates

None. The reference comparison has an honest authorized adjacent-context label; there is no need to request a new label merely to formalize it as `compares-with`. Tag navigation is evaluated as Index Membership, not an invented sources → tags formal relation.

## Raw Text Candidates

None.

## Rejected Candidates

- [Acceptance authority does not require a separate repair session](../../../../theory/acceptance-authority-does-not-require-a-separate-repair-session.md) — separates exact checking, acceptance, and session placement. JPL illustrates bounded repair authority, but does not distinguish worker-local checks from orchestrator acceptance or test context continuity. The author–executor candidate carries the useful comparison without this detour. No inbound edge recommended.
- [ADR 080: full passes hand claim changes back as a pending revise](../../../../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) — the detection/repair ceiling is a real adjacent distinction, but the ADR records a historical decision justified by local episodes. JPL adds no deciding evidence to that account. Prefer the live proposal's comparison; do not retrofit source lineage into the ADR.
- [Authority grades and learning from operator decisions](../../../../reference/proposals/authority-grades-and-learning-from-operator-decisions.md) — institutional permissions are adjacent to item grades, but JPL supplies no evidence for moving an automated grade, learned discrimination, or publication approval. The main procedure proposal is the more direct landing; an extra outbound or inbound link would mostly duplicate it.
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — invalidation here means changing the dependencies of a cached verdict or production artifact, not discarding prose during revision. Shared vocabulary does not supply a shared mechanism.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — JPL does not test bounded-context splitting, verifiability cost, or scheduler representations. Its option-order comparison is already served more precisely by the low-degree-of-freedom note.
- [Productive deferral](../../../../theory/productive-deferral-requires-option-evidence-and-convergence.md) and [set-based systems-engineering rework](../../../../sources/kennedy-sobek-kennedy-set-based-rework.ingest.md) — both require evidence-producing work and convergence while options remain live. JPL's service bundles do not specify those controls; shared concern with planning or wasted effort is insufficient.
- [Prose-readability head](../../../../tags/prose-readability-README.md) — not a recommended source entry: the ingest's main contribution is commissioned scope, not a demonstrated move that makes prose easier to follow. [Review-system head](../../../../tags/review-system-README.md) is also not a recommended entry: JPL is not an LLM review pipeline, and the live proposal supplies the closer route. No source-tag assignment is proposed.

## Index Membership

- [Goal prioritization](../../../../tags/goal-prioritization-README.md) — optional manually curated source entry under its objectives/requirements discussion: JPL makes included work, institutional minima, author options, and extraordinary services explicit, separating a concern that can be noticed from work commissioned for this case. This satisfies the head's substantive effort/scope-allocation question. Sources are outside participating collections, so this would be a hand-authored navigation entry, not generated membership or a consequence of assigning a tag. Do not describe the source as evidence for a preferred revision order. No index was edited.

## Synthesis Opportunities

The [default-composition proposal](../../../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md), [low-degree-of-freedom note](../../../../theory/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md), and JPL ingest together suggest a bounded clarification: included work, repair authority, invalidation-based order, and feasible-option order are separate decisions. The existing ingest already states most of this distinction, so prefer a focused proposal clarification over creating a new note merely to restate it. A genuinely new theory claim would need a worked case in which the two sequencing mechanisms recommend different orders and an explanation of when to choose between them; neither JPL nor the current source comparison tests that choice.

## Maintenance Observations

None.

## Flags

- The ingest's Quotes section is empty. The connection judgments above use its accepted analysis, not an independent re-reading of the private snapshot or PDF. Before authoring durable source-dependent descriptions of JPL's task boundaries, retain sufficient exact support through the grounding workflow or explicitly require the pinned snapshot where the full observation is needed. This report neither adds quotes nor silently upgrades the ingest into independently verified evidence.
- No load-bearing corroboration, source lineage, or claim of an optimal editing hierarchy is recommended. Existing outward comparisons do not establish reciprocal reader needs; each inbound candidate above has its own purpose and authorization.
- The proposal and ingest were evaluated as present in the working tree on 2026-11-13, including the proposal's uncommitted state and the accepted ingest's untracked state. Future authoring should recheck their then-current text. This run did not change either artifact or any unrelated work.
- No split flag: the source is one coherent editorial commissioning account. The retained new and reverse candidates do not span three independent topic areas warranting a split.
