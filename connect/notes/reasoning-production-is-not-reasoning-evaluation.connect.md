---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/reasoning-production-is-not-reasoning-evaluation.md"
source_has_frontmatter: true
date: "2026-06-17"
depth: standard
---

# Connection Report: Reasoning production is not reasoning evaluation

**Source:** [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/notes/COLLECTION.md`; authorised destinations for notes include `notes`, `reference`, `agent-memory-systems`, `sources`, and rare `instructions` links. `work` is excluded.
- Ran `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md' | rg -i 'review|critique|semantic|oracle|verification|evaluation|judge|reasoning|process|validity|entailment|gate'`. Kept nearby notes on oracle discrimination, process/output separation, semantic review, critique calibration, and operational review gates.
- Duplicate guard: `rg -n "Reasoning production is not reasoning evaluation|production is not reasoning evaluation|answer reconstruction|answer validity" kb/notes --glob '*.md'` found no pre-existing note with this title or exact abstraction.

**Topic indexes:**
- The note belongs in the `evaluation` and `llm-interpretation-errors` areas. The write did not edit tag README files.

**Body search:**
- `rg -n "premise|entail|grounding|reasoning path|semantic review|critique pass|review gate|conclusion|oracle|judge|valid reasoning|answer agreement|process validity" kb/notes kb/reference kb/instructions --glob '*.md'` surfaced `semantic-review-catches-content-errors-that-structural-validation.md`, `quality-signals-for-kb-evaluation.md`, `composition-friction-gate.md`, `semantic/grounding-alignment.md`, and review-system proposals.
- `rg -n "review gate|semantic/grounding-alignment|composition friction|accepted edit|human judge|critique" kb/instructions kb/reference kb/notes --glob '*.md'` surfaced operational surfaces. The strongest are `composition-friction-gate.md` and `semantic/grounding-alignment.md`; broader review architecture docs were rejected as implementation background.

**Link following:**
- Followed from the VAIR ingest to `oracle-strength-spectrum`, `error-correction-works-above-chance-oracles-with-decorrelated-checks`, `the-augmentation-automation-boundary-is-discrimination-not-accuracy`, and `process-structure-and-output-structure-are-independent-levers`. The new note already links the most load-bearing subset.
- Followed from `quality-signals-for-kb-evaluation` to its critique-calibration section. Kept as an existing link because conclusion-agreement substitution is a specific critique calibration risk.
- Followed operational hits into `composition-friction-gate`, `semantic/grounding-alignment`, and `critique-note`. Kept the first two as rare instruction links because they are concrete review surfaces; rejected `critique-note` because it is a general report procedure and does not force premise-to-conclusion tracing.

## Connections Found

- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **grounds**: the note's "independent verifier" warning depends on the oracle having discriminative power and decorrelated failure modes.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **grounds**: the note is a specific verification-boundary case for prose/reasoning review.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **extends**: valid-conclusion-invalid-reasoning cases are a concrete failure taxonomy item that should precede automated judge optimization.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) -- **see-also**: the note supplies a candidate mined gate shape: catch conclusion-agreement substitution by requiring explicit premise-to-conclusion tracing.

## Bidirectional Candidates

- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) <-> source -- **extends**: the new note narrows one content-error class: a conclusion may be true while the artifact's support does not establish it.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) <-> source -- **extends**: the new note identifies a critique-signal failure mode for the existing calibration section.

## Reverse-edge Candidates

- [Composition friction gate](../../../../instructions/composition-friction-gate.md) -> source -- **rationale**: the instruction should eventually cite this note as theory for refusing green-check self-grades and checking inferential joints.
- [Grounding alignment gate](../../../../instructions/review-gates/semantic/grounding-alignment.md) -> source -- **rationale**: the gate should eventually cite this note if hardened to explicitly test conclusion-agreement substitution.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) -> source -- **rationale**: if a future accepted edit adds a premise-to-conclusion trace requirement, this note is the theory behind that candidate gate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Review architecture](../../../../reference/review-architecture.md) -- rejected: implementation architecture is not the right target for this theoretical warning unless code changes are proposed.
- [Critique a note](../../../../instructions/critique-note.md) -- rejected as a direct link: it asks for a strong opposing case but does not specifically force route inspection or premise-to-conclusion tracing.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- rejected: mentions semantic review as a shipped trust surface, but this note is about a narrower evaluator failure mode.
- [Text testing framework](../../../../notes/text-testing-framework.md) -- rejected: useful background, but the note already links the more specific semantic-review and quality-signals notes.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- the note affects review-gate and critique-signal design.
- [LLM interpretation errors](../../../notes/llm-interpretation-errors-README.md) -- the note abstracts answer-confirmation bias into a review-system failure mode.

## Synthesis Opportunities

- A future operational note or proposal could define a "valid conclusion, invalid support" regression fixture for review gates, using this note plus `composition-friction-gate` and `semantic/grounding-alignment`.

## Maintenance Observations

None

## Flags

- The note is seedling and source-grounded. It should not yet trigger review-gate edits without a small local regression example or accepted-edit evidence.
