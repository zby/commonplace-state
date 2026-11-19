---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/interpolation-extrapolation-hyperpolation.md"
source_has_frontmatter: true
date: "2026-05-19"
depth: standard
---

# Connection Report: Interpolation, Extrapolation, Hyperpolation

**Source:** [Interpolation, Extrapolation, Hyperpolation](../../../sources/interpolation-extrapolation-hyperpolation.md)

## Discovery Trace

**Index scan:**
- Read [sources collection rules](../../../../sources/COLLECTION.md) -- authorised destinations: notes, reference, agent-memory-systems, sources; snapshots are immutable, so candidate authoring surface is the matching ingest report and reverse edges from library notes.
- Read [notes index](../../../notes/dir-index.md) -- flagged [automated synthesis](../../../../notes/automated-synthesis-is-missing-good-oracles.md) because the source's generative-hyperpolation discussion distinguishes reachable novelty from evaluated value; flagged [discovery](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) because the paper formalises "seeing a slice as part of a higher-dimensional whole"; flagged [oracle strength](../../../../notes/oracle-strength-spectrum.md) and [automation boundary](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) because the paper makes creativity depend on finding high-quality off-manifold points, not merely generating them.
- Read [reference index](../../../reference/dir-index.md) -- no concrete shipped-system component is directly informed by this paper; rejected broad `see-also` links into reference as too weak.
- Read [agent-memory-systems index](../../../agent-memory-systems/dir-index.md) -- no reviewed memory system is directly compared by this paper; rejected agent-memory links as off-target.
- Read [sources index](../../../sources/dir-index.md) -- flagged [Geometry of Knowledge ingest](../../../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md), [GIANTS ingest](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md), [Creative Thinking ingest](../../../../sources/creative-thinking-by-claude-shannon.ingest.md), [SuperARC ingest](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md), and [Pathway/Sudoku ingest](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) as source-level siblings around creativity, novelty, off-distribution generalisation, and verification.

**Topic indexes:**
- No dedicated creativity, novelty, or out-of-distribution topic index was found in the scanned indexes. The closest topical surfaces were the learning-theory notes surfaced by body search and existing ingest reports.

**Body search:**
- `rg -n "hyperpolation|interpolation|extrapolation|data manifold|manifold|off[- ]?manifold|out[- ]of[- ]distribution|OOD|creativity|creative|abduction|generalisation|generalization" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -- found no previous `hyperpolation` use, but surfaced the novelty/oracle cluster and many weak generalisation hits. Kept candidates whose mechanism involved off-distribution generation, discovery, or verification; rejected routine "generalization" mentions in benchmark limitations.
- `rg -n "novel|novelty|diversity|creative|creativity|idea selection|genuine reasoning|algorithmic abstraction|scientific insight|insight" kb/notes kb/sources --glob "*.md"` -- kept Geometry of Knowledge, GIANTS, Creative Thinking, automated synthesis, and discovery; rejected ordinary "insight" mentions in source summaries that did not discuss novelty generation.
- `rg -n "latent|embedding|manifold|geometry|semantic space|subspace|dimension|dimensional" kb/notes kb/sources --glob "*.md"` -- kept Geometry of Knowledge as the closest source sibling; rejected general "dimension" uses in evaluation and memory notes.
- `rg -n "oracle|verification|quality function|evaluate|evaluation|taste|problem selection" kb/notes kb/sources --glob "*.md"` -- kept oracle-strength and automation-boundary notes because the paper's generative-AI section depends on a quality-function framing; kept GIANTS as a source sibling because it manufactures a soft oracle for discovery-like synthesis.

**Link following:**
- From [automated synthesis](../../../../notes/automated-synthesis-is-missing-good-oracles.md), followed links to [Geometry of Knowledge](../../../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md), [oracle strength](../../../../notes/oracle-strength-spectrum.md), and [synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md). Geometry is the closest sibling; synthesis-is-not-error-correction is adjacent but about aggregation failure rather than off-manifold creativity, so it is weaker.
- From [discovery](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md), followed [first-principles reasoning](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md). Kept both: the source gives a mathematical vocabulary for moving from particulars to a higher-dimensional explanation, and for distinguishing adaptive fit from reach.
- From [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md), followed [automation boundary](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) and [automated synthesis](../../../../notes/automated-synthesis-is-missing-good-oracles.md). Kept GIANTS as a sibling because it operationalizes one narrow discovery/hyperpolation-like task by backcasting a known target.
- From [SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) and [Pathway/Sudoku](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md), kept only source-level sibling signal: they concern architectural generalisation outside training-distribution shortcuts, but their problem class is hard-oracle constraint/compression, not open-ended creativity.

## Connections Found

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- **evidence**: Ord's generative-hyperpolation framing says models must not only reach points outside the training manifold but find high-quality ones; this is the same generate-cheap, verify-expensive bottleneck the note names for KB synthesis.
- [Discovery is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -- **evidence**: the paper's core examples, such as seeing a curve as a slice of a ripple surface or a hyperbola as a cone section, formalise discovery as recognizing a known particular as a lower-dimensional instance of a newly posited general structure.
- [First-principles reasoning selects for explanatory reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **evidence**: hyperpolation distinguishes generalisation that leaves the observed subspace from interpolation/extrapolation along it, giving the reach/adaptive-fit distinction a geometric vocabulary.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the paper's distinction between predicting off-subspace truth and generating high-quality off-subspace artifacts makes oracle strength central; hyperpolation is useful only when there is some way to evaluate the off-manifold point.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the paper explains why current AI can generate plausible continuations yet struggles with "fundamental creativity"; the structural bottleneck is not sampling novelty alone, but validating quality outside the data manifold.

## Bidirectional Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) <-> source -- **evidence**: the note should consider this source as a conceptual frame for "off-manifold synthesis" alongside Geometry of Knowledge's empirical latent-conditioning case.
- [Discovery is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) <-> source -- **evidence**: the note's "generative model" depth could cite hyperpolation as a formal example where naming a higher-dimensional structure makes new instances predictable.

## Reverse-edge Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -> source -- **evidence**: add this source as a conceptual basis for distinguishing reachable novelty from useful novelty in generative AI and KB synthesis.
- [Discovery is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -> source -- **evidence**: add this source as a formal vocabulary for discovery by higher-dimensional re-description.
- [First-principles reasoning selects for explanatory reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -> source -- **evidence**: cite hyperpolation as a geometric way to discuss reach beyond the observed/training subspace.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -> source -- **evidence**: cite the paper's quality-function discussion as a weak-oracle case for creative generation outside known examples.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) -- rejected as a primary connection: it shares the verification bottleneck, but its mechanism is output aggregation versus voting, not off-subspace generalisation or creative discovery.
- [Pathway/Sudoku Bench ingest](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- rejected as a strong source comparison: it uses creativity language and transformer-limit claims, but its evidence is a hard-oracle constraint-satisfaction benchmark, not hyperpolation or open-ended novelty.
- [SuperARC ingest](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) -- rejected as a strong source comparison: both sources discuss training-distribution limits, but SuperARC tests algorithmic compression under exact verification, while Ord's paper is about higher-dimensional generalisation and creativity.
- [Creative Thinking ingest](../../../../sources/creative-thinking-by-claude-shannon.ingest.md) -- rejected as a primary source comparison: both concern creativity and generalisation, but Shannon provides heuristic operators while Ord provides a geometric taxonomy of generalisation.
- [Reference directory](../../../reference/dir-index.md) -- rejected: no shipped-system description needs this source directly.
- [Agent memory systems directory](../../../agent-memory-systems/dir-index.md) -- rejected: no reviewed external memory system is directly explained by this source.

## Index Membership

- [Sources directory](../../../sources/dir-index.md) -- future index refresh should add the snapshot and ingest report under the title "Interpolation, Extrapolation, Hyperpolation: Generalising into new dimensions".
- A future creativity / novelty / synthesis topic index, if created, should include this source as a conceptual paper on off-manifold generalisation.

## Synthesis Opportunities

Hyperpolation could name a missing bridge between the KB's discovery/reach notes and its oracle-boundary notes: generating a candidate outside the current subspace is only half the problem; useful creative automation also needs a way to evaluate the candidate in the new dimension. A synthesis note could connect [discovery](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md), [automated synthesis](../../../../notes/automated-synthesis-is-missing-good-oracles.md), [oracle strength](../../../../notes/oracle-strength-spectrum.md), [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md), and [Geometry of Knowledge](../../../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md).

## Maintenance Observations

None

## Flags

- Split candidate: the paper has at least two independently useful threads for the KB -- a formal vocabulary for higher-dimensional generalisation, and a creativity/AI limitation argument about off-manifold quality evaluation. The ingest report should keep both visible but recommend one narrow next action.
