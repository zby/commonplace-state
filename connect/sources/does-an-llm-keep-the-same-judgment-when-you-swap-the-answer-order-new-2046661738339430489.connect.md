---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order-new-2046661738339430489.md"
source_has_frontmatter: true
date: "2026-04-23"
depth: standard
---

# Connection Report: Thread by @LechMazur

**Source:** [Thread by @LechMazur](../../../sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer-order-new-2046661738339430489.md)

## Discovery Trace

**Index scan:**
- Read [sources COLLECTION](../../../../sources/COLLECTION.md) to confirm the active outbound surface lives on the future `.ingest.md`, not the immutable snapshot, and that `notes`, `reference`, `agent-memory-systems`, and `sources` are the permitted prospecting destinations.
- Read [notes directory index](../../../notes/dir-index.md) and flagged the judge-reliability cluster: [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md), [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md), [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), [Interpretation errors are failures of the interpreter](../../../notes/interpretation-errors-are-failures-of-the-interpreter.md), [Reliability dimensions map to oracle-hardening stages](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md), [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md).
- Read [agent-memory-systems directory index](../../../agent-memory-systems/dir-index.md) and flagged [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) as the only obvious operational analogue because it already recommends order-swapping in pairwise comparisons.
- Read [reference directory index](../../../reference/dir-index.md); no reference note promised more than contextual adjacency, so `reference` was rejected at index level.

**Topic indexes:**
- None. The snapshot only carries `x-thread`, which does not map to a useful curated note-topic index.

**Body search:**
- `rg -n "position bias|order bias|order effect|swap the answer order|first-shown|judge model|preference label|grader|LLM-as-a-judge|llm as a judge|judge reliability|comparison prompts" kb/notes kb/reference kb/agent-memory-systems kb/sources --glob "*.md"` -> confirmed the strongest exact lexical overlap is the existing [position-bias ingest](../../../../sources/position-bias.ingest.md) plus the note cluster already identified; no reference note offered a stronger destination than `notes` or `sources`.
- `rg -n "position bias|order bias|order effect|swap order|first-shown" kb/notes kb/agent-memory-systems --glob "*.md"` -> kept [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) because it explicitly lists position bias as a failure mode to measure; kept [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) because it explicitly prescribes order-swapping; rejected the other incidental hits as too indirect.
- `rg -n "pairwise|position bias rate|tournament|Borda|judge" kb/notes --glob "*.md"` -> reinforced [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md), [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), and [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md); rejected [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) as a direct edge because the thread supplies only one concrete bias instance, not a fresh argument about decorrelation theory.
- `rg -n "position-bias mitigation|swap order|pairwise comparison" kb/agent-memory-systems --glob "*.md"` -> one precise hit in [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md), supporting a reverse-edge or off-authorisation note rather than a source-authored outbound edge.
- `rg -n "position-bias|judge reliability|llm-as-a-judge|pairwise" kb/sources --glob "*.ingest.md"` -> identified [position-bias ingest](../../../../sources/position-bias.ingest.md) as the strongest same-topic source already in the KB, plus [the Koylan pairwise ingest](../../../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy-for-scient-2035982137539559616.ingest.md) and [the Autoreason ingest](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) as neighbouring pairwise-judging material.

**Link following:**
- Read [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) and followed its outbound links to [Agent Skills for Context Engineering](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md), [quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md), and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md). This confirmed the thread belongs in the existing pairwise-judge / soft-oracle cluster, but mostly as additional evidence rather than as a new conceptual bridge.
- Read [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md) and [Operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md). These establish that order-swap behavior is already theorized in the KB as diagnostic prompt variation and brittleness-under-reordering.
- Read [position-bias ingest](../../../../sources/position-bias.ingest.md). This is the decisive comparison: the repo ingest already carries the full methodology, data substrate, and main numeric prior. The X thread adds a compact public-summary surface, the author's operational motivation ("annoyed me in regular-use ChatGPT comparison prompts"), and pointers to human order-effect literature, but it does not replace the repo snapshot as the main evidence artifact.

## Connections Found

- [position-bias.ingest.md](../../../../sources/position-bias.ingest.md) -- **compares-with**: this thread is the compact announcement surface for the same benchmark the repo ingest covers in depth; useful when the graph needs headline numbers and author motivation without loading the full repository snapshot.
- [brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md](../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden-soft-oracles.md) -- **evidence**: the thread provides exactly the failure mode the note says pairwise judges must be tested against, including explicit order-swap instability and a public "first-shown" rate.
- [systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md](../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not-explanatory-reach-testing.md) -- **evidence**: order-swapping the same pairwise comparison is a clean diagnostic prompt-variation case where task semantics stay fixed and invariance is the success criterion.
- [operational-signals-that-a-component-is-a-relaxing-candidate.md](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) -- **evidence**: judge flips under answer-order swap are a direct judge-layer instance of brittleness under reordering, the note's first operational signal for proxy-theory behavior.

## Bidirectional Candidates

- [position-bias.ingest.md](../../../../sources/position-bias.ingest.md) <-> source -- **compares-with**: the repo ingest could link back to this thread as the public announcement / motivation surface for the same benchmark family, especially if we want a quick citation surface for the headline result.

## Reverse-edge Candidates

- [agent-skills-for-context-engineering.md](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) -> source -- **evidence**: the review's "swap order and check whether the conclusion changes" recommendation has a compact public example here, even though the repo snapshot remains the stronger evidential target.

## Off-authorisation Candidates

- [agent-skills-for-context-engineering.md](../../../../agent-memory-systems/reviews/agent-skills-for-context-engineering.md) -- the articulation is strong ("this source empirically supports the review's order-swap mitigation rule"), but `kb/sources/` has no authorised outbound label stronger than `see-also` into `kb/agent-memory-systems/`. Downgrading this to `see-also` would hide the evidential relationship, so keep it as a reverse-edge or reject it.

## Raw Text Candidates

None

## Rejected Candidates

- [interpretation-errors-are-failures-of-the-interpreter.md](../../../notes/interpretation-errors-are-failures-of-the-interpreter.md) -- relevant at a high level, but the thread does not add enough beyond "LLM judges can fail under invariant-preserving reordering"; the stronger repo snapshot is the better evidence surface for that note.
- [reliability-dimensions-map-to-oracle-hardening-stages.md](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) -- plausible `evidence`, but the thread lacks the methodological detail needed to sharpen the note beyond what the repo ingest already provides.
- [the-augmentation-automation-boundary-is-discrimination-not-accuracy.md](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- same issue: the claim is relevant, but the X thread is a thin summary compared with the existing benchmark-repo ingest.
- [quality-signals-for-kb-evaluation.md](../../../../notes/quality-signals-for-kb-evaluation.md) -- pairwise judging is adjacent, but this source is about evaluator failure in model-comparison tasks, not about KB mutation-quality signals directly.
- [evaluation-automation-is-phase-gated-by-comprehension.md](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- the author's "I saw this in ordinary ChatGPT use and turned it into a benchmark" is suggestive, but the thread itself is not a rich enough field report to ground the note cleanly.
- [oracle-strength-spectrum.md](../../../../notes/oracle-strength-spectrum.md) -- too general; the thread helps only through the already-captured benchmark result, so the repo ingest remains the better edge.
- [reference/](../../../reference/dir-index.md) candidates -- no reference note offered a destination whose reader need beat the existing notes/source matches.

## Index Membership

None

## Synthesis Opportunities

- The Koylan pairwise-judging source, the benchmark-repo ingest, and this announcement thread together support a cleaner synthesis note: pairwise comparison is not a usable evaluation primitive unless order-swap contamination is explicitly measured or mitigated. Koylan supplies the evaluation primitive, the repo ingest supplies the strong numeric prior, and this thread supplies the operational motivation and public-summary surface.

## Flags

- Strong overlap with [position-bias ingest](../../../../sources/position-bias.ingest.md). Any downstream `.ingest.md` for this thread should focus on incremental value: concise citation surface, author motivation from real comparison workflows, and the human-order-effect references surfaced in replies.
