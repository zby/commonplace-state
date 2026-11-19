---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/notes/storing-llm-outputs-is-constraining.md
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Selecting an LLM output fixes a result, not its interpretation

**Source:** [Selecting an LLM output fixes a result, not its interpretation](../../../../notes/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md)

## Discovery Trace

**Source reading and linking rules:**
- Read the final source, `kb/notes/COLLECTION.md`, and `kb/cache/types/connect-report.md` in full. The source now separates persistence, selection, and behavioral authority, and derives distinct generator- and artifact-testing targets without claiming that stored text becomes unambiguous.
- The notes collection authorises `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `kb/work/`. No open-web prospecting was performed.

**Curated heads and tag routing:**
- Read `kb/notes/tags-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/constraining-README.md`. The learning-theory head routes through validated child tags; the constraining head still carries the source's pre-reframe title and summary.
- Read `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md` before evaluating destination surfaces.

**Complete title and description scans:**
- Generated the complete title surface for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`, then filtered candidates with `select|selection|choos|retain|retention|persist|stor|artifact|authorit|commit|output|test|verif|generator|interpret|indetermin|underspec|activat|learn`.
- Ran whole-destination `rg '^description:'` scans over `types`, `reference`, `agentic-systems`, and `instructions`; ran focused description scans over `notes`, `agent-memory-systems`, and `sources` using the same selection, persistence, authority, testing, and ambiguity vocabulary.

**Focused body searches:**
- Notes: `rg -n -i "selection.*result|select(ed|ing).*output|persistence.*(choose|select)|storage does not|persistence alone|stored bytes|consumption path|behavioral authority|operative retention|generator testing|artifact testing|testing target|ambiguity.*stored|fixed bytes|commitment.*result" kb/notes/ --glob '*.md'` surfaced the activation, governance, authority, selection-loop, and testing clusters.
- Types: `rg -n -i "selected output|retained|artifact|authority|consumption|output|testing target|persistence" kb/types/ --glob '*.md'` found contracts that classify artifacts but no type-level development of this claim.
- Reference: `rg -n -i "selected output|stored output|retained artifact|behavioral authority|consumption path|artifact testing|generator.testing|persistence.*selection|fixed bytes" kb/reference/ --glob '*.md'` found shipped review/storage machinery but no system description the theoretical claim needs.
- Agent-memory systems and agentic systems: `rg -n -i "selected output|retained artifact|behavioral authority|consumption path|artifact testing|persistence alone|operative retention|promotion.*candidate" kb/<destination>/ --glob '*.md'` surfaced system-specific promotion loops; none improved on the already-linked theory notes.
- Sources: the same query over `kb/sources/` surfaced retained-adaptation sources and prior ingests. The final note no longer makes the append-only or frozen-taxonomy claims that made the Koylanai and Evans captures candidates in the initial run.
- Instructions: the same query over `kb/instructions/` surfaced review and selection procedures. The source already links the one retained-instruction application, and the collection contract makes other instruction edges exceptional.

**Link following and candidate evaluation:**
- Followed [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) through its read-back and activation distinctions. Kept it because it supplies the broader storage-to-use boundary behind the source's narrower operative-reuse condition.
- Followed [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) through behavioral authority and proposal-selection. Kept it as the broader governance consequence of the source's final learning boundary.
- Followed the authority neighborhood through [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) and the selection neighborhood through [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md). Rejected both as useful but downstream concerns not needed to understand this note's claim.
- Ran `rg -n "storing-llm-outputs-is-constraining"` across all seven destinations. Existing inbound links confirm that this source has no duplicate owner, but many still state the former claim that storage resolves interpretation.
- Verified every retained candidate path exists before writing this report.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **grounds**: supplies the broader distinction between persistence, read-back, and behavioral effect that makes operative reuse necessary rather than an optional implementation detail.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **extends**: generalizes the final boundary from selected LLM outputs to governed behavior-changing writes across representational forms, including the evidence-responsive condition under which retention counts as learning.

## Bidirectional Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source -- **extends**: the source gives a concrete post-storage sequence—selection, persistence, and authority—and a testing consequence for one generated artifact.

## Reverse-edge Candidates

None. Existing inbound links are maintenance targets because their visible wording predates the reframe, not missing-edge candidates.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Behavioral authority](../../../../notes/definitions/behavioral-authority.md), [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md), [Automated tests for text](../../../../notes/automated-tests-for-text.md), and [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- already linked in the final source at the places where each does argumentative work.
- [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) -- develops authorization bypass after authority is assigned; useful downstream, but not needed for the source's selection-versus-storage distinction.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- develops the cost of a bad selection verdict; adjacent to candidate filtering but outside the source's two-target testing claim.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- distinguishes outcome from process evidence for episodes, not generator from selected-artifact testing.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) and [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- system and survey instances whose relevant promotion structure is stated more directly by the linked proposal-selection theory note.
- [Where It Lives Is Not What It Is](../../../../sources/where-it-lives-architectural-vocabulary-retained-adaptation.ingest.md) -- corroborates authority and storage as separate axes, but those premises are already available through local theory notes and the final source no longer depends on an external case.

## Index Membership

None. The source is already routed through the `constraining` tag and through `learning-theory`'s validated child coverage.

## Synthesis Opportunities

None. The final source now owns the specific conjunction that the closest notes leave separate: selecting one generated result fixes artifact identity, operative reuse gives it force, and this creates an artifact test distinct from generator testing.

## Maintenance Observations

- `kb/notes/constraining-README.md`, `kb/notes/definitions/constraining.md`, and numerous inbound citers still call the source “Storing LLM outputs is constraining” or say keeping an output resolves it to one interpretation. Those summaries conflict with the final source and must be reconciled when the required post-pass rename updates visible link text and premise uses.
- The canonical filename also retains the former title. Renaming it during this pass would violate the full-pass reframe boundary; use `commonplace-relocate-note` in the required follow-up operation.

## Flags

- Near-duplicate check: no merge owner found. Existing notes separately own persistence-versus-activation, behavioral authority, commitment, selection loops, and text testing; this source owns their LLM-output-specific testing consequence.
- No split signal remains. The final note has one claim and one derived testing consequence; the initial append-only, prompt-strategy, and verbatim-risk branches are gone.
