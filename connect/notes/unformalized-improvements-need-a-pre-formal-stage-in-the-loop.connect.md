---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Formal-only gates have distinct admission and warrant limits

**Source:** [Formal-only gates have distinct admission and warrant limits](../../../notes/formal-only-gates-have-distinct-admission-and-warrant-limits.md)

## Discovery Trace

**Curated heads:**
- Read [Notes](../../../../notes/README.md), [Tags](../../../../tags/README.md), [Foundations](../../../../tags/foundations-README.md), [constraining](../../../../tags/constraining-README.md), and [Self-improving systems](../../../../tags/self-improving-systems-README.md). These concentrated the search in the constraining / proposal-selection / deploy-time-learning neighborhood. The strongest unlinked note candidates from the curated pass were [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md), [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md), and [The bitter lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md).

**Notes title and description listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — full title sweep confirmed dense nearby clusters around formalization, constraining, representational form, and bitter-lesson notes.
- `rg '^description:' kb/notes/ --glob '*.md'` — full description sweep surfaced the same neighborhood and confirmed that [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md), [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) were plausible but broader than the kept note-level candidates.
- `rg -n 'description:.*(formal|proof|codif|representational|translation|prototype|surrogate|criticism|world fit|premise|underspecified)' kb/notes --glob '*.md'` — kept [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md), [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md); rejected [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) and [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) as second-order rather than source-specific.

**Notes body search and link following:**
- `rg -n '(formal-only|formalization|proof|surrogate|translation|prototype|codif|representational form|world fit|premise|underspecified|criticism)' kb/notes --glob '*.md'` — confirmed the kept note set and surfaced broader context notes.
- Followed [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) to its `spec mining` / `changing requirements` neighborhood; kept the note itself because it names the phase decision this source implies, but not those downstream notes because the connection became less direct.
- Followed [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) to [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) and [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md); kept the boundary note and rejected the broader second-hop context as weaker than the direct cross-form-governance link.
- `rg -n '\[[^]]+\]\(([^)]+)\)' kb/notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md` — checked existing outbound links and rejected already-authored targets as new candidates: [Representational form](../../../../notes/definitions/representational-form.md), [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md), [Codification](../../../../notes/definitions/codification.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md), [False-positive generation is filtered before retention](../../../../notes/false-positive-generation-is-filtered-before-retention.md), [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md), [Eigenius](../../../../agentic-systems/reviews/eigenius.md), [Ingest: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), and [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md).

**Other authorised destinations:**
- Read [Agentic Systems](../../../../agentic-systems/README.md) and [Sources](../../../../sources/README.md).
- `rg '^description:' kb/agentic-systems/ kb/sources/ --glob '*.md'`
- `rg -n '(proof|Lean|formal|verification|correspondence|explanation quality|counterfactual|predictive accuracy|translation)' kb/agentic-systems/ kb/sources/ --glob '*.md'`
  - [Eigenius](../../../../agentic-systems/reviews/eigenius.md) and [Ingest: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) were the only strong matches. Both are already linked inline from the source, so they are not new outbound candidates. After reading [kb/agentic-systems/COLLECTION.md](../../../../agentic-systems/COLLECTION.md) and [kb/sources/COLLECTION.md](../../../../sources/COLLECTION.md), both were retained only as reverse-edge candidates.
- `rg -n 'description:.*(formal|proof|codif|representational|translation|prototype|surrogate|criticism|world fit|premise|underspecified)' kb/reference kb/instructions kb/types kb/agent-memory-systems --glob '*.md'`
- `rg -n '(formal|proof|codif|representational form|translation|prototype|surrogate|world fit|premise|underspecified|criticism)' kb/reference kb/instructions kb/types kb/agent-memory-systems --glob '*.md'`
  - `kb/reference/proposals/bidirectional-codification-comparative-test.md` was the nearest reference hit, but the relation stayed looser than the kept note-to-note candidates.
  - `kb/instructions/` hits were review gates and procedures rather than a procedure this source operationalizes.
  - `kb/types/` and `kb/agent-memory-systems/` produced no candidate with a stronger reader need than the kept notes or the already-linked external cases.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- **mechanism**: the source's prototype-stage argument depends on natural-language candidates admitting multiple valid projections before constraining chooses one formal surrogate; this note supplies that projection model directly.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- **extends**: the source distinguishes cases that still need a revisable pre-formal stage from cases ready for a determinate surrogate; this note turns that distinction into an artifact-timing policy across spec-first, live-spec, and mined-spec phases.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- **extends**: the source says a formal-only gate should not force early commitment on unsettled alternatives; this note supplies the concrete codification discipline that waits for repeated stability before freezing one projection into code.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) -- **extends**: the source says translation can restore reach without settling surrogate fidelity or world fit; this note sharpens that into the governance requirement for moving responsibility from interpreted prose into formal enforcement.
- [The bitter lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) -- **exemplifies**: the source is the specific answer to that note's separate cheap-formalization objection, so the portfolio gives readers the larger argumentative role this note plays beyond its local formal-gate claim.

## Bidirectional Candidates

- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) <-> source -- **extends**: the target explains when ambiguity should stay live or be mined later; a return link to the source would add the stronger reason that early formal surrogates still leave correspondence and world-fit questions open.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) <-> source -- **extends**: the target gives the operational rule for delaying codification; a return link to the source would supply the objection-level reason that formal-only gates otherwise exclude unsettled but revisable candidates.

## Reverse-edge Candidates

- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) → source -- **rests-on**: Eigenius's Lean-checking section already distinguishes proof validity from faithful encoding; this source provides the more exact admission-versus-warrant framing for why a checked formal surrogate need not settle the natural-language correspondence.
- [Ingest: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) → source -- **is-evidence-for**: the ingest's predictive-accuracy versus explanation-quality split is concrete evidence that internal success on one surrogate artifact does not by itself establish explanatory fit, matching the source note's surrogate-fidelity and world-fit limit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- already linked inline and already doing the source's formal-proof boundary work; not a new outbound candidate.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- already linked inline as the fixed-axiom limiting case.
- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- genuine overlap, but the kept notes supply the nearer mechanism and timing links; this note would be a second-order aggregation hop.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- plausible broader frame, but the connection was less source-specific than the kept constraining and cross-form-governance notes.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- relevant broader backdrop, but the portfolio note gives the more exact role this source plays inside that argument cluster.
- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) -- already linked inline from the source; retained only as a reverse-edge candidate.
- [Ingest: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- already linked inline from the source; retained only as a reverse-edge candidate.

## Index Membership

- [constraining](../../../../tags/constraining-README.md) -- the curated head currently covers codification timing and relaxing, but not this note's argument that formal-only gates impose an extra admission boundary before proof or evidence even begins.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the update-architecture section would gain a note that separates representational admission limits from post-admission oracle warrant inside proposal-selection loops.

## Synthesis Opportunities

- [Formal-only gates have distinct admission and warrant limits](../../../notes/formal-only-gates-have-distinct-admission-and-warrant-limits.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), and [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) together suggest a missing synthesis note: semantic work has three separate decisions -- when ambiguity collapses, when responsibility moves into formal enforcement, and what evidence warrants the mapping. The current notes cover those decisions separately but not as one design surface.

## Maintenance Observations

- [The bitter lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) still links to this source under its former title text, "Reaching unformalized improvements needs a pre-formal stage somewhere in the loop." The path is correct, but the stale claim text weakens title-as-claim discoverability after the retitle.

## Flags

- Split candidate: the note is currently doing two nearby but separable jobs -- the core admission-versus-warrant argument for formal-only gates, and the broader cheap-formalization objection role in the bitter-lesson cluster. The current artifact still holds together, but further growth on either side may justify splitting the objection-handling wrapper from the core formal-gate theory.
