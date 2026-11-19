---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/llm-generation-relaxes-goals-where-human-writing-stalls.md"
source_has_frontmatter: true
date: "2026-06-15"
depth: standard
---

# Connection Report: LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on

**Source:** [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md)

## Discovery Trace

**Source and rules loaded:**
- Read `kb/cache/types/connect-report.md`, the full source note, and `kb/notes/COLLECTION.md`.
- Source claim: when LLM prose generation cannot satisfy a conjunctive goal, it emits a plausible relaxation without a stall signal; the dropped constraint moves verification burden to the reader. Scope is prose-as-discovery and oracle-poor work.
- `kb/notes/COLLECTION.md` authorizes notes, reference, agent-memory-systems, agentic-systems, sources, and rare instructions links; excludes `kb/work/`; notes->instructions is exceptional and normally inverse unless `see-also` is genuinely useful.

**Description listing scan:**
- Read `kb/notes/README.md` and `kb/notes/learning-theory-README.md`. `learning-theory-README.md` has `covered_by` but not `complete: true`, so ran the by-tag listing instead of skipping it.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` and `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`.
- Flagged: `automated-synthesis-is-missing-good-oracles.md` (same generate-cheap/evaluate-hard shape), `error-correction-works-above-chance-oracles-with-decorrelated-checks.md` (conditions for the separate checking operation the source asks about), `semantic-review-catches-content-errors-that-structural-validation.md` (operational content-error checks), `structured-prompt-gains-do-not-establish-distribution-selection.md` and `human-writing-structures-transfer-to-llms-because-failure-modes.md` (structure can improve generation but does not directly address the hidden dropped-conjunct mechanism).
- Rejected by description alone: broad context/scoping notes, type-system infrastructure, agent-memory reviews, and general verification notes where the path from the source to the target would only say "verification matters."
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/instructions/README.md`. No agent-memory or agentic-system candidate passed the articulation test; their oracle mentions were system-review evidence rather than a direct edge from this theoretical source.

**Topic indexes:**
- Read `kb/notes/llm-interpretation-errors-README.md`, `kb/notes/observability-README.md`, `kb/notes/type-system-README.md`, and `kb/notes/evaluation-README.md`.
- Kept `llm-interpretation-errors-README.md` as index membership because the source is about LLM confidence, interpretation failure, verification, and oracle-poor correction.
- Kept `observability-README.md` as weaker index membership because the source centers a hidden failure signal and the cost of recovering it.
- Rejected `type-system-README.md`: structured types may mitigate but the source is not primarily about document types.
- Rejected `evaluation-README.md`: prompt/evaluation methods are adjacent but too broad for membership from this note alone.

**Body search:**
- Ran `rg -n "witness|counterfeit witness|relaxation|human writer|writing stalls|because|therefore|typicality|camouflage|constraint" kb/notes/ --glob '*.md'`.
- This confirmed the already-authored neighborhood: `machine-searches-for-camouflage-human-writer-slips-into.md`, `llm-generation-confidence-tracks-typicality-not-soundness.md`, `reverse-compression-is-when-llm-output-expands-without-adding.md`, `the-boundary-of-automation-is-the-boundary-of-verification.md`, `vibe-noting.md`, and `definitions/constraining.md` are already linked from the source.
- Ran `rg -n "composition-friction|frictionless generation|stall|witness|relaxation|typicality|camouflage|constraint" kb/instructions/ --glob '*.md'`; kept `composition-friction-gate.md` because it directly operationalizes the source note's open question.
- Ran `rg -n "witness|relaxation|typicality|camouflage|constraint|verification|oracle" kb/reference/ --glob '*.md'`; found three proposals already citing the source through `rationale`, with `focused-single-aspect-review-passes-open-ended-catalogue.md` the strongest possible source-side `see-also`.
- Ran `rg -n "witness|relaxation|typicality|camouflage|constraint|verification|oracle" kb/agent-memory-systems/ --glob '*.md'` and the same over `kb/agentic-systems/`; hits were mostly extraction-oracle statements in external-system reviews, rejected as too distant for a note-authored edge.
- Ran `rg '^description:' kb/sources/ --glob '*.md'` and `rg -n "trendslop|discourse priors|task logic|fashionable|typicality" kb/notes kb/sources --glob '*.md'`; kept `researchers-asked-llms-strategic-advice-trendslop.ingest.md` as an adjacent empirical source for discourse-prior typicality, not as direct proof of the whole witness-stall mechanism.

**Link following:**
- Followed `composition-friction-gate.md` -> source. The instruction already carries the reverse `rationale` link, so only the source-side `see-also` candidate is needed.
- Followed reference proposal backlinks found by `rg`: `focused-single-aspect-review-passes-open-ended-catalogue.md`, `gate-learning-from-accepted-edits.md`, and `automated-note-refinement-as-search-over-source-bundle.md`. All already link to the source under reference rules; only the focused-pass proposal was kept as a source-side candidate because it generalizes the "separate focused pass reconstructs the stall" design.
- While reading `automated-note-refinement-as-search-over-source-bundle.md`, found a stale link to `../../notes/current-llm-inference-removes-composition-friction-filter-signal.md`, recorded under Maintenance Observations.

## Connections Found

- [composition-friction-gate.md](../../../../instructions/composition-friction-gate.md) -- **see-also**: Direct operational companion that reconstructs the source note's missing stall signal by forcing a fresh adversarial pass over concretization and inferential joints.
- [automated-synthesis-is-missing-good-oracles.md](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- **extends**: Develops the same generate-cheap/evaluate-expensive asymmetry for KB synthesis, where LLMs can produce plausible combinations but oracle-poor evaluation keeps humans in the loop.
- [error-correction-works-above-chance-oracles-with-decorrelated-checks.md](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **enables**: Supplies the conditions under which a separate adversarial or semantic check could recover the dropped constraint the source says generation confidence cannot expose.
- [semantic-review-catches-content-errors-that-structural-validation.md](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) -- **extends**: Turns the source note's reader-side burden into concrete single-note checks for structurally valid but semantically defective prose.
- [researchers-asked-llms-strategic-advice-trendslop.ingest.md](../../../../sources/researchers-asked-llms-strategic-advice-trendslop.ingest.md) -- **evidence**: Corroborates the typicality/discourse-prior subclaim by showing LLM strategy advice preserving fashionable management defaults despite prompt and context variation; not evidence for the whole witness-stall mechanism.
- [focused-single-aspect-review-passes-open-ended-catalogue.md](../../../reference/proposals/focused-single-aspect-review-passes-open-ended-catalogue.md) -- **see-also**: Describes a Commonplace review design that applies the source note's mechanism: focused passes get teeth by reconstructing the weak joint diffuse fluent reading would miss.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) -- Rejected as an outbound candidate: that note asks which mechanism produced an observed prompt gain, while this source's specific concern is hidden constraint relaxation and reader-side verification.
- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- Rejected: the note explains why human writing conventions can transfer to LLMs, but the source already supplies the relevant human/LLM contrast more directly.
- [oracle-strength-spectrum.md](../../../../notes/oracle-strength-spectrum.md) -- Rejected as a new candidate because the source already links to the stronger synthesis note [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), which imports oracle strength at the right abstraction level.
- [gate-learning-from-accepted-edits.md](../../../../reference/proposals/gate-learning-from-accepted-edits.md) -- Rejected for source-side linking: it already cites the source via `rationale`, but the design's central edge is accepted-edit oracle asymmetry rather than composition-stall reconstruction.
- [automated-note-refinement-as-search-over-source-bundle.md](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) -- Rejected for source-side linking: it already cites the source via `rationale`; its design problem is broader automated refinement identity, not the source note's strongest operational application.
- [language-models-like-humans-show-content-effects-on-reasoning.ingest.md](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- Rejected: useful evidence for content bias and structure, but not specific enough to dropped-conjunct relaxation.

## Index Membership

- [llm-interpretation-errors-README.md](../../../notes/llm-interpretation-errors-README.md) -- The source belongs in this area because it separates typicality from soundness, names a hidden interpretation/reasoning failure, and depends on separate verification to recover what confidence cannot.
- [observability-README.md](../../../../tags/observability-README.md) -- Weaker candidate: the source's main cost model is hidden failure signal recovery, which fits the observability area if the note is tagged or cross-listed beyond `learning-theory`.

## Synthesis Opportunities

- The source, [composition-friction-gate.md](../../../../instructions/composition-friction-gate.md), [focused-single-aspect-review-passes-open-ended-catalogue.md](../../../reference/proposals/focused-single-aspect-review-passes-open-ended-catalogue.md), and [semantic-review-catches-content-errors-that-structural-validation.md](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) imply a reusable claim: focused adversarial passes are weak-oracle reconstructions of composition friction, not just "more review." This may deserve a theory note if it becomes useful outside the current review proposals.

## Maintenance Observations

- `kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md` links to missing `../../notes/current-llm-inference-removes-composition-friction-filter-signal.md`; traversal suggests this should now point at `../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md` or another successor.
- `kb/notes/learning-theory-README.md` says every `learning-theory` note carries one of its child tags, but the source note currently has only `tags: [learning-theory]`. If validation agrees, add the appropriate child tag, likely `llm-interpretation-errors`, and consider `observability` if the hidden-signal framing is intended to be navigable there.

## Flags

- Source is `status: seedling`; avoid making it a load-bearing `grounds` or `mechanism` target until the witness/relaxation framing matures.
