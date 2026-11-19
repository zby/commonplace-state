---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/symbols-neural-networks-mathematical-intelligence.ingest.md"
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: Ingest: Symbols, neural networks, and mathematical intelligence

**Source:** [Ingest: Symbols, neural networks, and mathematical intelligence](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md)

The ingest is fresh and already carries 11 note links and 4 source links, all verified to exist. This report lists only candidates **beyond** those existing edges, plus reverse edges.

## Discovery Trace

**Linking rules:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: notes, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (notes, agent-memory-systems), `abstracted-from`/`rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). No label authorises a `kb/tags/` destination. External prospecting skipped (no externally supplied target).

**Existing-link check:** every `../notes/...` link in the ingest resolves.

**Title listing scan (notes):**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i "bitter|symbol|codif|relax|scaffold|verif|formal|intuition|math|proof|neural|parametric|weights|internaliz|tool|absorb|oracle|lean|conjecture|distill|learn"` -- flagged: bitter-lesson-selects-against-unearned-reach-not-against-structure, a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it, the-bitter-lesson-defense-portfolio-has-one-load-bearing-member, evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs, goedel-machines-are-a-proof-governed-case-of-self-modification, formal-systems-assess-explanatory-reach-through-causal-and-proof, operational-signals-that-a-component-is-a-relaxing-candidate, unified-calling-conventions-enable-bidirectional-refactoring, oracle-strength-spectrum, parametric-reproduction-cannot-replace-an-authoritative-record, llm-learning-phases-fall-between-human-learning-modes, spec-mining-as-codification, error-correction-works-above-chance-oracles-with-decorrelated-checks. Descriptions read for all; bodies read for the unearned-reach and bootstrap notes.

**Body search (all permitted destinations):**
- `rg -il "\bLean\b|AlphaProof|AlphaGeometry|IMO\b|olympiad|theorem prov|Fodor|Pylyshyn|connectionis|PDP\b|Lampinen" notes sources agentic-systems agent-memory-systems reference tags` -- 50 files. Evaluated: prove2me ingest and agentic review, eigenius review, lamport proof ingest, llms-cant-jump and hot-take-llm-can-jump ingests, symbolic-learning-enables-self-evolving-agents, falsifybench, human-writing-structures-transfer-to-llms-because-failure-modes, error-correction note, formal-systems note, unformalized-improvements note. Most other hits are keyword noise (`lean` as a verb, Sutskever-list chapters).
- `rg -n -i "lean\b|lampinen|wason|olympiad|IMO\b"` over the formal-systems, human-writing, error-correction, and unformalized-improvements notes -- the Lampinen hits are all the 2024 content-effects paper, which the ingest already links through its own ingest.

**Tag heads:** `kb/tags/COLLECTION.md` line 30 excludes `sources` from tag participation; constraining-README read to confirm the codification/relaxing cluster lives there. No tag edge is possible from this source.

**Link following:** from the unearned-reach note to its refutation condition ("a case that isolates explicitness itself as the disadvantage refutes the note for that case"); from the bootstrap note to its scaffold/bootstrap distinction; from llms-cant-jump to its links to formal-systems and the verification-boundary note; from the scaling-absorbs note's "Observed at both ends" section (two practitioner cases, 2 source links, so ADR 082 has room).

## Connections Found

- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **compares-with**: shared axis is whether explicit structure itself is what loses to scale. Lampinen asserts exactly that (removing Lean "improved performance"); the note says such a case refutes it only if it isolates explicitness as the disadvantage, and the ingest's own Limitations show the IMO comparison does not. The link lets a reader see why this essay is not a counterexample to the note. Stronger and more specific than the existing production-methods link for this point.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **compares-with**: shared axis is scaffold vs bootstrap. The 2024 Lean medium was a scaffold discarded by a different, retrained system, which matches the ingest's point that "the system that did the relaxing is not the one solving problems". The note's distinction names that pattern precisely.
- [Lamport: How to Write a 21st Century Proof](../../../../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) -- **compares-with**: shared axis is prose vs structured proof form. Lamport argues prose hides logical structure and structured steps make checking possible; Lampinen argues prose is where proof-finding works. Together they support the ingest's Extractable Value 3 (form for finding vs form for checking).
- [Prove2Me: collaborative math formalization](../../../../sources/prove2me-collaborative-math-formalization.ingest.md) -- **compares-with**: shared axis is the role of Lean in LLM mathematics. Prove2Me keeps Lean as the coordination and acceptance artifact, with human audits of meaning; Lampinen treats Lean as a reasoning medium that was shed. This is the "verification outside the generation loop persists" side of Extractable Value 3, and a counterweight to the essay's "verification is irrelevant" framing.
- [LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) -- **compares-with**: shared axis is what LLM mathematical successes show about invention. The Jacobian and unit-distance counterexamples are search within stated conjectures, i.e. Zahavy's deduction/search side, not premise invention. The link keeps the essay from being cited as evidence of abductive capacity.

## Bidirectional Candidates

- [Lamport: How to Write a 21st Century Proof](../../../../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) <-> source -- **compares-with**: a reader of Lamport's ingest gains the counter-position that informal prose is the productive medium for finding proofs.

## Reverse-edge Candidates

Under `kb/notes/COLLECTION.md`, notes link to source ingests with `evidenced-by` (corroborates, qualifies, or bounds; a case that risked nothing must be phrased as qualifying or bounding, not corroborating).

- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) → source -- **evidenced-by** (illustrative, bounded): the IMO 2024→2025 case as a third bullet in "Observed at both ends", carrying the model/training/compute/medium confound. Matches the ingest's Recommended Next Action; the note currently cites 2 sources, so the ADR 082 bound has room.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) → source -- **evidenced-by** (illustrative): a formal-domain relaxing instance beside the vision and hardware examples; the note cites 0 tracked sources.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) → source -- **evidenced-by** (bounds): a well-known claimed "explicitness loses" case that fails the note's own isolation condition; useful as a worked non-refutation. The note cites 3 sources.

## Off-authorisation Candidates

- None. (`kb/tags/` is listed as a scan destination in `kb/sources/COLLECTION.md` but no label authorises it; moot here because sources do not participate in tags.)

## Raw Text Candidates

None

## Rejected Candidates

- [Prove2Me agentic-system review](../../../../agentic-systems/reviews-archive/prove2me.md) -- same point as the Prove2Me ingest; the source-to-source edge is the cleaner one.
- [Eigenius review](../../../../agentic-systems/reviews/eigenius.md) -- Lean proof-term checking is incidental to the essay's question.
- [Hot Take: LLM can 'jump'](../../../../sources/hot-take-llm-can-jump.ingest.md) -- mentions Lean only as a strong oracle for formalized targets; reached via llms-cant-jump if needed.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) and [error correction works with above-chance oracles](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- their Lampinen material is the content-effects paper, already reached through the linked content-effects ingest.
- [Missing rationale does not exclude a theory builder; weight-only retention excludes one across runs](../../../../notes/evidence/missing-rationale-does-not-exclude-a-builder-weights-do-across-runs.md) -- the ingest already applies the theory-builder conditions directly; the note's Apodex case adds nothing specific to this essay.
- [The Bitter Lesson defense portfolio has one load-bearing member](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) -- about defending Commonplace's strategy, not about the essay's case.
- [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) -- signals apply within a deployed system; the IMO relaxing was done by lab retraining, which the signals do not address.
- [Symbolic learning enables self-evolving agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- "connectionist" is analogy vocabulary there; keyword match only.
- Oracle-strength spectrum, Gödel machines, formal-systems/explanatory-reach, LLM learning phases, unified calling conventions, spec mining, parametric reproduction -- topical overlap without a reason an agent would follow the link from this essay.

## Index Membership

- None. Sources are excluded from tag participation (`kb/tags/COLLECTION.md`).

## Synthesis Opportunities

The Lampinen essay (prose for finding), [Lamport](../../../../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) (structure for checking), [Prove2Me](../../../../sources/prove2me-collaborative-math-formalization.ingest.md) (Lean as persistent acceptance artifact), and [FunSearch](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md) (fixed symbolic evaluator around a model) jointly suggest the conjecture already flagged in the ingest's Extractable Value 3: formal structure inside the generation loop is absorbable at fixed difficulty, while formal verification of the finished result persists. Still too thin for a note (no case isolates the variable), but four sources now bear on it.

## Maintenance Observations

None

## Flags

- The unearned-reach note and this essay touch at the note's stated refuter. A future reader citing Lampinen against structured artifacts should be routed through that note's isolation condition.
