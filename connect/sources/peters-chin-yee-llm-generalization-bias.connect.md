---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: Generalization Bias in LLM Summarization of Scientific Research

**Source:** [Ingest: Generalization Bias in LLM Summarization of Scientific Research](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md)

The ingest already carries six authored outbound links in its `Connections Found` section (five theory notes plus one source). All six paths exist. This report evaluates them, adds two new candidates, and lists the reverse edges that matter most: no artifact outside `kb/work/` links to this ingest yet.

## Discovery Trace

**Linking rules read:** `kb/sources/COLLECTION.md` § Outbound links. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. `external` is authorised for `derived-from` and `see-also` only; no external target was supplied, so external prospecting was skipped. Labels by destination: theory takes `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also` (and `defined-in` for theory/definitions); sources takes `compares-with`, `see-also`; agent-memory-systems takes `is-evidence-for`, `compares-with`, `see-also`; agentic-systems takes `compares-with`, `see-also`; reference takes `see-also` only. For reverse edges, `kb/theory/COLLECTION.md` § Labels was read (theory -> sources uses `evidenced-by`; corroboration requires a test the claim could have failed; the unquoted-source limit is 5).

**Topic indexes:**
- `kb/tags/llm-reliability-README.md` (the source's only tag) -- this confirmed the existing three-way-diagnosis, out-of-spec and execution-indeterminism targets. The head is not `complete: true`. Its "Sources" section lists one external paper (Ma et al.).

**Title / description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "summar|distill|compress|generali|scope|faithful|fidelity|warrant|licens|paraphras|plausib|prompt|negat|temperature|sycophan|confident|abstract|lossy|claim"` -- flagged: generality-bought-to-avoid-counterexamples (kept), artifacts-must-preserve-named-choice-scope (rejected), claim-modality-is-the-inference-form-of-the-refuter (rejected), theory-warrant-tracked-at-the-finest-granularity (rejected), checked-outcome-licenses-episode-retention-not-abstraction (rejected), reverse-compression (rejected), plus the existing targets.
- `rg -N --no-heading -m1 '^description:' kb/sources --glob '*.ingest.md' | rg -i "summar|faithful|sycophan|overconfid|plausib|generali|hallucin|distort|scope|abstract|compress"` -- flagged: meta-harness (kept), competing-biases-llm-confidence (rejected), hacker-news-ai-dr-ai-didnt-read (rejected).

**Body search:**
- `rg -n -i "quantif|tense|generic claim|action-guiding|recommendation" kb/theory` -- no note treats quantifier, tense or descriptive-versus-action-guiding as scope operators; the hits are incidental uses.
- `rg -l -i "summar(y|ies|ization)" kb/sources --glob '*.ingest.md' | xargs rg -l -i "faithful|distort|overstat|lossy|scope|generali"` -- about 40 files, mostly incidental mentions. Only meta-harness measures summary loss against the source.
- `rg -l -i "sycophan|RLHF.*(confiden|overconfid)|overconfiden" kb/sources kb/theory` -- competing-biases-llm-confidence and generation-confidence; both rejected (see below).
- `rg -n -i "summar[a-z]* (drift|distort|overgenerali|broaden|lose|loses|lossy)|lossy summar|summary drift" kb/agentic-systems kb/agent-memory-systems kb/theory kb/reference` -- the MemPalace review ("Verbatim always ... avoids summary drift") and two retained analysis results about lossy summarizers (incidental).
- `rg -n "peters|generalization-bias|E16" kb --glob '*.md'` (excluding `kb/work`) -- no inbound links to this ingest exist.

**Link following:**
- I read the footer of generality-bought-to-avoid-counterexamples. It links abstract-an-experience-only-when-you-can-state-the-boundary (already linked by the ingest), narrowing-bought-to-survive-review and generation-confidence. This confirms the boundary-test cluster the ingest already joins.
- I read the body of an-insufficient-summary-precedes-the-source. Its sufficiency condition is a four-part tuple `(summary, source path, question, required reliability)`, which supports the ingest's existing reading.
- In competing-biases-llm-confidence, the outbound links are generation-confidence and reliability-dimensions. These are confidence calibration, not summary scope.

## Connections Found

The six existing authored links all pass the articulation test and use authorised labels. They are listed so a future editor can keep or relabel them deliberately:

- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **is-evidence-for** (existing): the paper measures the dropped condition clause under LLM compression. As the ingest says, it qualifies rather than corroborates, because summarizing another author's text is a different setting from forming a lesson.
- [A citation cannot assert more fidelity than its capture preserved](../../../../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) -- **is-evidence-for** (existing): LLM paraphrase of a scoped claim is skewed in a predictable direction, not just unverified. That argues for retaining scope qualifiers verbatim.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- **is-evidence-for** (existing): for population, time or recommendation-strength questions, LLM summaries often fail the sufficiency condition.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) -- **is-evidence-for** (existing): two remedies from different classes act on one deviation in opposite directions (accuracy prompt OR 1.90; temperature 0 cuts the odds by 76%).
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) and [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- **compares-with** (the existing links are inline and unlabelled; `compares-with` fits better than `is-evidence-for`): the shared axis is whether sampling control can reach interpreter failure. The classification of scope broadening is unsettled, so the inline "in tension with" phrasing should not harden into an evidence label.
- [How Language Models Conflate Logical Validity with Plausibility](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) -- **compares-with** (existing): plausibility or broad applicability displaces fidelity to what the input licenses. That paper shows it mechanistically for syllogisms; this one shows it behaviourally for claim scope.

New candidates:

- [Generality bought to avoid counterexamples is paid for in precision](../../../../theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- **compares-with**: the shared axis is raising universality while dropping the precision that excluded cases. The paper's quantified-to-generic move is a measured instance of widening scope in LLM-produced text. The note's forbids-test ("name a case the new wording rules out") is a ready per-operator checker for the paper's three operators. The motive differs: the note covers *defensive* abstraction against a known counterexample, while the paper's broadening is unmotivated summary drift. So use `compares-with`, not `is-evidence-for`.
- [Meta-Harness: end-to-end optimization of model harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: the shared axis is what an LLM summary loses relative to its source for a downstream consumer. Meta-Harness shows summaries fail to recover diagnostic signal from raw traces (a capability loss). This paper shows summaries change claim scope in one direction (a fidelity distortion). Together they give two different reasons to keep the source in the reading path.

## Bidirectional Candidates

- [Generality bought to avoid counterexamples is paid for in precision](../../../../theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) <-> source -- the theory side could cite the paper as `evidenced-by` (qualifies) for the claim that hedged, broad prose is high-probability output. The paper counts hedged broadened claims ("suggests", "may") as generalized, which matches the note's point that hedging does not restore precision. This is useful only once the ingest retains a quote, because of the theory unquoted-source limit.

## Reverse-edge Candidates

No artifact outside the workshop links to this ingest. Theory notes are the useful direction, since the paper bounds their claims. Under `kb/theory/COLLECTION.md`, each edge would be `evidenced-by` with a context phrase saying it *qualifies or bounds* the claim. These are not corroboration: the study was not built as a test of these notes.

- [A citation cannot assert more fidelity than its capture preserved](../../../../theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md) -> source -- **evidenced-by**: qualifies the note. LLM paraphrase is directionally biased toward broader scope, so scope qualifiers deserve priority in quote retention. This is the strongest reverse edge.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -> source -- **evidenced-by**: bounds the note with a measured case where LLM summaries fail sufficiency for scope-sensitive questions, while expert summaries (NEJM Journal Watch) did not.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) -> source -- **evidenced-by**: qualifies the note with an empirical case where a prompt-narrowing remedy worsened the targeted deviation and sampling control only reduced it. The caveats are one prompt wording and a temperature condition confounded with access mode.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) -> source -- **evidenced-by**: bounds the note. Condition-clause dropping is measurable in LLM compression of others' claims. The weakest of the four, because the setting differs from lesson formation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An artifact must preserve the scope of each named system choice](../../../../theory/artifacts-must-preserve-named-choice-scope.md) -- it shares the phrase "scope preservation under repackaging". But it concerns reference rules and roles for named system choices, and it explicitly says quantifier syntax is not what matters. The paper's population, time and modality scope is a different object, so a link would mislead.
- [Claim modality is the inference form of the refuter](../../../../theory/claim-modality-is-the-inference-form-of-the-refuter.md) -- "modality" here means the claim mode (deductive, inductive, abductive), not descriptive versus action-guiding force. Keyword match only.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../theory/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- the paper's standard is fidelity to the original, not warrant. The ingest says this explicitly, so linking to a warrant-allocation note would import the conflation the ingest warns against.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../theory/checked-outcome-licenses-episode-retention-not-abstraction.md) -- its scope-boundary requirement concerns abstracting one's own episodes. abstract-an-experience already covers that cluster.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) -- the only bridge is the paper's untested RLHF "confident, broadly applicable answers" conjecture. That is too thin to carry a label.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) -- it concerns volume inflation, not scope change. The paper's summaries are shorter, not longer.
- [Competing biases underlie overconfidence and underconfidence in LLMs](../../../../sources/competing-biases-llm-confidence.ingest.md) -- it concerns confidence updating under advice, with no shared axis on summary scope.
- [Hacker News: AI didn't read](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) -- it covers reader burden from unedited AI text, which is too general a match.
- [MemPalace review](../../../../agent-memory-systems/reviews/mempalace.md) -- its "Verbatim always ... avoids summary drift" is an unargued remark in the curiosity pass. The paper would support it, but the collection is historical and frozen, and `kb/agent-memory-systems/COLLECTION.md` restricts links into sources to lightweight back-links to the source a review was abstracted from.

## Index Membership

- [LLM reliability tag head](../../../../tags/llm-reliability-README.md) -- the source is already tagged `llm-reliability`. Under `kb/sources/COLLECTION.md`, source tags do not create head membership. The head's "Sources" section is curated and currently lists one external paper. A maintainer could add this paper there as empirical evidence that prompt-narrowing and sampling-control remedies act differently on one deviation. That is an editorial choice, not a membership requirement.

## Synthesis Opportunities

The citation-fidelity note, the insufficient-summary note, the Meta-Harness ingest and this paper together suggest a higher-order claim. **LLM-made summaries fail as substitutes for their sources in two separable ways:** they lose signal (Meta-Harness), and they distort scope in one direction (this paper). Each needs a different guard. Loss is guarded by keeping the source in the reading path. Distortion is guarded by verbatim retention of scope-bearing features, checked feature by feature. This depends on more than one study of scope distortion (as the ingest's Extractable Value item 3 notes). It may belong to the epistemic-relevance workshop rather than to a theory note now.

## Maintenance Observations

- The ingest's `## Quotes` section is empty. Every proposed reverse edge from `kb/theory/` counts against that collection's unquoted-source limit (5) until quotes are retained through `cp-skill-ground`. The quotes most likely needed are the OR 1.90 accuracy-prompt result, the temperature-0 result, the three-operator coding definitions and the NEJM comparison.
- The existing inline links to out-of-spec-output and execution-indeterminism are phrased as tension, not support. That is correct given the unsettled classification, and a future footer should not label them `is-evidence-for`.

## Flags

- Tension (not resolved here): the temperature-0 result sits between two notes. Execution-indeterminism and out-of-spec-output say sampling control is irrelevant to interpreter failure. Three-way-diagnosis allows sampling control to suppress a bad tail. Which note the paper bears on depends on whether scope broadening is interpreter failure or underspecification. The ingest already flags this.
- No split candidate: the ingest has one central contribution (scope-broadening under summarization) despite touching five theory notes.
