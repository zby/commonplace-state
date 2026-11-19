---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/sutskevers-list/chapters/04-deep-learning-accelerates.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Deep learning accelerates

**Source:** [Deep learning accelerates](../../../sources/sutskevers-list/chapters/04-deep-learning-accelerates.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg -n -i '^description:.*(feature|representation|bitter lesson|decomposition|learned|fixed|scale|requirement|architecture|data)' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. Flagged fixed-decomposition, exact-requirement, Bitter Lesson, scaling, and representation notes.

**Topic indexes:**
- Read the foundations, learning-theory, evaluation, and constraining heads. The strongest role is a transition case: fixed linguistic subcomponents are relaxed into end-to-end learning while sequence architecture and evaluation remain constrained.
- Read the agent-memory and agentic-system heads; RNN hidden state is model state, not durable agent memory under those collection contracts.

**Body search:**
- Ran `rg -n -i '(recurrent|sequence|bottleneck|dropout|end-to-end|speech|human.level|baseline|exposition)' kb/notes --glob '*.md'`. Most literal RNN hits were incidental; the durable matches concerned update-space boundaries and benchmark warrant.

**Link following:**
- Followed the fixed-decomposition note into exact requirements and Bitter Lesson boundaries.
- Revisited [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md); kept it only as a secondary comparison because the chapter argues that explanatory blogs made technical ideas actionable and canonical.
- Considered agent-memory notes because LSTM uses “memory”; rejected them because the collection's retained-artifact and cross-session semantics do not match recurrent hidden state.

## Connections Found

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: Deep Speech 2 removes fixed phonetic dictionaries and much of the modular speech pipeline, placing acoustic-to-text representation learning inside the trainable system; selective recurrent dropout likewise changes which pathways may vary without destroying temporal memory.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for**: the chapter's human-transcription comparison is locally measurable, yet its clean/read-speech subsets do not warrant a general “surpasses humans” requirement—humans remain better on noise and heavy accents.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- **is-evidence-for**: end-to-end learning replaces hand-built linguistic intermediates but succeeds through substantial retained structure: LSTM gates, convolution, CTC, decoding, language models, optimization, and distributed engineering.
- [Index curation adds orientation that generation cannot produce](../../../../notes/index-completeness-does-not-determine-editorial-orientation.md) -- **compares-with**: Karpathy's and Olah's explanatory essays add orientation and executable intuition around RNNs that paper lists and formal schematics did not provide.

## Bidirectional Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) <-> source -- **is-evidence-for**: speech recognition provides a second domain where learned representations replace a fixed upstream pipeline.

## Reverse-edge Candidates

- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -> source -- **evidenced-by**: Deep Speech 2 is a compact case of hand-built intermediates being relaxed without eliminating architecture or engineering structure.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- rejected: RNN/LSTM “memory” is transient model state, not a retained behavior-shaping artifact with read-back policy.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- rejected: neuron visualizations offer inspection but not selective, causally connected revision of a represented organization.

## Index Membership

- [Learning theory](../../../../tags/learning-theory-README.md) -- end-to-end learning and selective regularization as update-space choices.
- [Evaluation](../../../../tags/evaluation-README.md) -- bounded human-level claims and baseline selection.

## Synthesis Opportunities

- Pedagogical reach can be an engineering multiplier: an explanation changes who can reproduce and vary a system even when it adds no mathematical novelty. The curation note is adjacent, but a durable claim would need more than this chapter's popularity evidence.

## Maintenance Observations

None

## Flags

- The chapter's experiments vary recurrent connections, layer depth, normalization, data scale, and decoding, but the WER benchmarks and language-specific decoding assumptions remain outside the tested update space.

