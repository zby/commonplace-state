---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it

**Source:** [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the source's three tag heads: `learning-theory-README.md`, `deploy-time-learning-README.md`, and `foundations-README.md`. None of the three tag heads declares `complete: true`; `learning-theory-README.md` declares only `covered_by`, so no by-tag scan was skipped.
- Read the destination heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. The notes heads concentrated the search around production method, open-ended evaluation, whole-system learning, and self-improvement pathways. The other heads supplied no equally direct candidate cluster.

**Title and description listing scans:**

- Generated the complete notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'`; it exposed the open-ended search, whole-system learning, computational-allocation, repeatable-path, codify/relax, and bounded-evidence candidates retained below.
- Generated complete title surfaces with the same command for `kb/types`, `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, `kb/sources`, and `kb/instructions`.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` for every authorised local destination.
- Ran the required by-tag description scans for `learning-theory`, `deploy-time-learning`, and `foundations` using `rg -l '^tags:.*\bTAG\b' kb/notes --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These scans kept the bounded Commonplace episode, whole-system learning boundary, and human-allocation endpoint; they rejected broad topical overlap with ordinary memory and context-engineering notes.

**Body search:**

- `rg -n -i 'hand-crafted|handcrafted|Bitter Lesson|bitter lesson' kb/notes --glob '*.md'` -- found the existing Bitter Lesson cluster plus codify/relax, whole-system learning, scaffold absorption, and earned-reach interpretations. Kept codify/relax and whole-system learning; the other obvious hits were redundant or answered a neighbouring carrier question.
- `rg -l -i 'bootstrap|outgrow|domain-extensible' kb/notes --glob '*.md'` -- surfaced the bounded 2026-08-30 episode and the already-authored inbound links from the defense-portfolio, residue-class, and theory-mediation notes.
- `rg -l -i 'global theory fit|global fit|selection environment' kb/notes --glob '*.md'` -- confirmed that the source already links the closest global-fit note and identified the episode as the strongest additional evidence target.
- `rg -l -i 'selection machinery|search and evaluation|search.*selection' kb/notes --glob '*.md'` -- kept the prior-search and repeatable-path candidates; rejected general proposal-loop duplicates already linked from the source.
- `rg -l -i 'human (judgment|share|intervention)|fixed decomposition|predefined' kb/notes --glob '*.md'` -- kept the computational-allocation endpoint and confirmed that the existing fixed-decomposition link already carries the update-space premise.
- For each non-notes destination ran `rg -n -i 'Bitter Lesson|bitter lesson|bootstrap|outgrow|domain-extens|global (theory )?fit|theory-guided|selection machinery|human judgment|human intervention|hand-crafted' kb/<destination> --glob '*.md'`. The reference search retained the ablation-baseline proposal. Types and instructions had no trigger-matching target. Agent-memory and agentic-system hits were implementation cases rather than evidence of a domain-extensible bootstrap. The source search found the Bitter Lesson ingest, but direct lineage would duplicate the source's existing grounded premise link.
- External prospecting was skipped. No user-supplied external target was in scope, and the known Bitter Lesson material already has a tracked local ingest.

**Link following:**

- Followed all six authored note links from the source and inspected their `Relevant Notes` neighborhoods. The production-method and fixed-decomposition neighborhoods led to whole-system learning and codify/relax; the proposal-loop neighborhood led to prior search allocation; the system-use neighborhood confirmed that the source already carries the closest global-fit premise.
- Followed inbound links to the source. The defense-portfolio, residue-class, and theory-mediation notes already author useful return paths, so they are not proposed again.
- Inspected the full claims, caveats, and footers of every retained candidate. All retained targets have frontmatter, and every listed path was verified to exist.

**Per-destination disposition:**

- `notes` (including `notes/definitions`): six new candidates passed the articulation and label tests. No missing definition justified a `defined-in` edge.
- `reference` (including `reference/definitions`): one Commonplace-specific experimental proposal passed as a sparing `see-also`; current-state descriptions and trace reports were weaker than the bounded evidence note.
- `types`: no plausible trigger; the lexical `outgrowing` hit in the tag-README type concerns index size, not learning outgrowing a hand-crafted bootstrap.
- `agent-memory-systems`: no candidate established the source's strategic compatibility condition or domain-extensibility criterion.
- `agentic-systems`: Exo and Compound Engineering illustrate editable/frozen surfaces, but neither establishes that this bootstrap strategy outgrows its starting structure.
- `sources`: the tracked Bitter Lesson ingest is already mediated by the source's grounded production-method premise; adding it directly would duplicate lineage without supporting the source's new first-strategy claims.
- `instructions`: no procedure adds ordering, defaults, or stopping conditions to this strategic claim strongly enough to warrant `operationalized-from`.

## Connections Found

- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) -- **evidenced-by**: the bounded episode directly corroborates the source's claim that current Commonplace already combines computational theory search with decisive human global-fit selection, while preserving the missing-ablation and non-autonomy limits.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- **grounds**: explains why the absence of a complete global-fit oracle still leaves a necessary computational allocation problem before adoption-quality evidence exists.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **grounds**: supplies the system boundary under which prompts, theory, code, evaluators, and their division of responsibility all face learning pressure rather than leaving the hand-crafted harness exempt.
- [A repeatable operative path keeps a redesign class open to revision](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) -- **extends**: turns the source's requirement that starting machinery remain challengeable into a six-part test for whether one redesign class can actually change and remain open to another change.
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../../../../notes/computationally-directed-self-improvement-is-a-reallocation.md) -- **extends**: develops the source's question about a falling human share into a per-function allocation profile and a cut-set endpoint rather than an intervention count.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **mechanism**: supplies the reversible codify/relax operation by which a useful hand-crafted component can be retained provisionally, tested under scale, and later migrated or reopened rather than protected by origin.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) -- **see-also**: gives the current Commonplace instance a concrete comparison design for the source's open question about curated-theory, episode-only, review-disabled, and stronger-bare-model baselines.

## Bidirectional Candidates

- [The 2026-08-30 Commonplace revision used retained theory to guide computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) <-> source -- source to episode is **evidenced-by**; episode to source is **exemplifies**, because the return path identifies the conditional bootstrap strategy the bounded human-inclusive episode instantiates without claiming that it already outgrew the bootstrap.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) <-> source -- source to whole-system boundary is **grounds**; whole-system boundary to source is **extends**, because the return path gives readers a provisional strategy and failure burden after establishing that non-model components belong inside the learning surface.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- rejected as redundant for this source: its earned-reach criterion is already reachable through the authored production-method premise, while the source's distinctive burden concerns handing production and selection to learning.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- rejected because its cross-form inventory is broad context already represented by the source's production-method and fixed-decomposition links; it does not sharpen the conditional bootstrap test.
- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- rejected because it answers whether an external function may recur at a moving frontier, whereas the source deliberately makes no carrier-survival claim and asks whether production can cease to be hand-crafted.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected because its rewritable executor and protected substrate illustrate one update-space boundary but do not show a theory-guided bootstrap becoming domain-extensible.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected because its mixed search and frozen prompt corpus illustrate both sides of the source's failure test without establishing the source's proposed strategy or providing a clean discriminating comparison.
- [Ingest: The Bitter Lesson](../../../../sources/wikipedia-bitter-lesson.ingest.md) -- rejected as a direct edge because the source already links the production-method note that owns and bounds this premise; another lineage edge would duplicate grounding rather than support the first-strategy extension.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- rejected because its objective and transfer-evidence gaps are broader current-system context; the episode note and ablation proposal give more precise evidence and experimental reader paths for this source.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- candidate for a curated entry under learning fundamentals or the framework boundary: the source states when a hand-authored deployment-time artifact path remains compatible with learning and what evidence would show that it failed to outgrow its starting structure.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- **Split candidate:** the artifact connects to more than five notes across at least three topic areas and makes three independently citable assertions: the narrow Bitter Lesson compatibility condition, the initial selection strategy under incomplete global evaluation, and the domain-extensibility/failure criterion. A future writer should test whether the latter two can be cited without importing the whole compatibility argument; if so, split them rather than expanding this note's footer further.
