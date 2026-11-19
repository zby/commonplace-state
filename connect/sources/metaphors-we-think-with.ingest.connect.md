---
description: "Discovery report for possible KB connections from metaphors-we-think-with.ingest.md"
type: types/connect-report.md
source: kb/sources/metaphors-we-think-with.ingest.md
source_has_frontmatter: true
date: "2026-02-27"
depth: standard
---

# Connection Report: Ingest: Metaphors We Think With: The Role of Metaphor in Reasoning

**Source:** [Metaphors We Think With: The Role of Metaphor in Reasoning](../../../../../sources/metaphors-we-think-with.ingest.md)

## Discovery Trace

**Collection:** sources (outbound section in `kb/sources/COLLECTION.md`)

**Authorised destinations:** theory, agent-memory-systems, sources, agentic-systems, external
**Excluded destinations:** kb/work/, kb/instructions/
**Authorised labels:** derived-from (external), is-evidence-for (theory, agent-memory-systems), abstracted-from (theory), rests-on (theory), compares-with (theory, sources, agent-memory-systems, agentic-systems), defined-in (theory/definitions), see-also (theory, reference, sources, agent-memory-systems, agentic-systems, external)

**Description listing scan (theory):**
- Scoped `rg '^description:' kb/theory/ --glob '*.md'` — 100+ notes. Flagged candidates by description match: `knowledge-storage-does-not-imply-contextual-activation` (storage vs activation distinction), `human-writing-structures-transfer-to-llms-because-failure-modes` (failure-mode overlap), `frontloading-is-partial-evaluation-not-divide-and-conquer` (framing as structural precision), `prompt-ablation-converts-human-insight-to-deployable-framing` (framing methodology), `human-llm-differences-are-load-bearing-for-knowledge-system-design` (dual-audience design).

**Title listing scan (theory):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` — full title surface scanned. Confirmed the five candidates above exist and match the ingest's claim surface. No additional title-level matches found beyond what description listing surfaced.

**Body search (theory):**
- `rg -n "framing\|metaphor\|covert\|knowledge.*activation" kb/theory/ --glob '*.md'` — returned hits in `knowledge-storage-does-not-imply-contextual-activation.md` (Tulving/Pearlstone and Gick/Holyoak citations, activation gap mechanism), `human-writing-structures-transfer-to-llms-because-failure-modes.md` (content effects, framing sensitivity), `frontloading-is-partial-evaluation-not-divide-and-conquer.md` (structural precision vs metaphor), `prompt-ablation-converts-human-insight-to-deployable-framing.md` (framing methodology), `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` (failure-mode overlap reference).
- `rg -n "figurative\|wording.*reason" kb/theory/ --glob '*.md'` — no direct matches; no theory note on figurative wording exists yet (the planned note mentioned in the ingest's occasion does not exist).

**Source-to-source scan:**
- `rg -n "framing\|metaphor\|reasoning" kb/sources/ --glob '*.ingest.md'` — identified two directly related sources:
  - `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` — LLM content effects on reasoning (complementary evidence, same failure-mode overlap axis)
  - `when-do-natural-language-metaphors-influence-reasoning.ingest.md` — direct critique/replication failure of the Thibodeau & Boroditsky claim (methodological counterpoint)

**Agent-memory-systems scan:**
- `rg -n "framing\|metaphor\|covert\|reasoning.*effect" kb/agent-memory-systems/ --glob '*.md'` — limited relevance. Body search returned only passing mentions of "framing" in review context (e.g., "README framing", "universal memory layer framing"). No artefact carries a claim about metaphor or framing effects on reasoning that would benefit from this source's evidence.

**Agentic-systems scan:**
- `rg -n "framing\|metaphor" kb/agentic-systems/ --glob '*.md'` — no relevant matches. Agentic-system reviews do not address metaphor framing or covert influence on reasoning.

**Link following:**
- From `knowledge-storage-does-not-imply-contextual-activation.md` — follows link to `gick-holyoak-analogical-problem-solving.ingest.md` (already named as reverse-edge candidate). The note cites Gick & Holyoak for the recognition/activation gap but does not cite Thibodeau & Boroditsky; the metaphor paper's covert-effect evidence would strengthen the note's "expert-witness pattern" example.
- From `human-writing-structures-transfer-to-llms-because-failure-modes.md` — already links to `language-models-like-humans-show-content-effects-on-reasoning.ingest.md`. The metaphor paper is a human-side complement to that LLM-side evidence; the note's failure-mode-overlap argument would benefit from the single-word-manipulation evidence.
- From `when-do-natural-language-metaphors-influence-reasoning.ingest.md` — this source explicitly critiques the Thibodeau & Boroditsky (2013) claim. It should link to `metaphors-we-think-with.ingest.md` as the original study it replicates/follows up on; that link is currently absent.

## Connections Found

- [knowledge-storage-does-not-imply-contextual-activation](../../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The paper provides empirical evidence for the note's central distinction between storage, read-back, and contextual activation. The covert-effect finding (participants cite statistics, not metaphor, as influential) is a clean demonstration of the "expert-witness pattern": knowledge is present but not self-triggering. The single-word manipulation shifting reasoning by 18-22% without participant awareness is a strong data point for the note's claim that "the model knows X" is often the wrong operational question. The note already cites Gick & Holyoak for this gap; Thibodeau & Boroditsky provides a second, independent human-studies antecedent with a different mechanism (frame-consistent knowledge structures vs analogical retrieval).

- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **is-evidence-for**: The paper provides human-side empirical evidence for the failure-mode-overlap argument. The finding that minimal linguistic framing (single word) produces large, covert shifts in reasoning supports the note's claim that LLMs share human-like reasoning vulnerabilities. Experiment 3's dissociation (lexical prime vs. embedded metaphor) is directly relevant to the note's mechanism-depth argument: mere word activation is insufficient; the framing must participate in an elaborated knowledge structure. This is the human-side complement to `language-models-like-humans-show-content-effects-on-reasoning.ingest.md`, which provides the LLM-side evidence.

- [frontloading-is-partial-evaluation-not-divide-and-conquer](../../../../../theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md) — **compares-with**: The metaphor paper argues metaphors are not "mere rhetorical flourishes" but have "profound influences on how we conceptualize and act"—directly relevant to the frontloading note's argument that PE framing is "structurally precise, not metaphorical." The relationship is complementary and tension-bearing: the metaphor paper shows metaphors *do* have real cognitive effects (so framing is never nothing), while the frontloading note clarifies that in a shared-token medium, some framings are precise substitutions rather than loose metaphors. A future ingest could note this tension: when does a framing's effect come from structural precision versus metaphorical knowledge-activation? The two sources should be read together.

- [prompt-ablation-converts-human-insight-to-deployable-framing](../../../../../theory/prompt-ablation-converts-human-insight-to-deployable-framing.md) — **see-also**: The metaphor paper is foundational empirical evidence for why framing matters. The prompt ablation methodology tests different framings to find which cognitive moves agents can reliably execute; the metaphor paper demonstrates that minimal framing changes (single word) produce significant behavioral shifts in humans. Relevant as background evidence for why ablation studies are worth running and as a model of controlled framing experiments. The paper's effect-size benchmark (18-22% shift > 8-9% partisan difference) is a useful quantitative anchor for framing-selection methodology.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **see-also**: The covert-influence finding and the political-affiliation interaction inform the naive-anthropomorphism warning. The paper demonstrates that humans are subject to covert framing effects they do not recognize—relevant to the note's argument that assuming LLM behavior mirrors human behavior without testing is risky. The source's extractable value item 6 explicitly flags the mismatch: the paper studies human reasoning, not LLM behavior, and any KB claim transferring these findings to LLM behavior would be extrapolation.

- [language-models-like-humans-show-content-effects-on-reasoning.ingest.md](../../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) — **compares-with**: Both sources investigate how linguistic framing/content affects reasoning outcomes—one in humans (metaphor framing), one in LLMs (content effects on syllogisms, NLI, Wason). Together they illustrate the failure-mode-overlap axis: humans show covert metaphor framing effects; LLMs show content-bias effects on logical reasoning. The two sources are natural companions for any note on figurative wording and reasoning, and the existing `human-writing-structures-transfer-to-llms-because-failure-modes.md` note already links the LLM-side source. Adding the human-side source would complete the comparative picture.

- [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) — **compares-with**: Direct methodological counterpoint. Steen et al. (2014) is a four-experiment critique finding no metaphor framing effect with proper controls (non-metaphorical baseline, removal of supporting metaphors, pre-exposure measurement). The original Thibodeau & Boroditsky claim appears to be an exposure effect. These two sources must be read together: one reports a positive effect, the other reports that the effect disappears under improved experimental design. Any KB claim about metaphor framing's influence on reasoning that cites only the positive study would be selectively evidence-based. The `when-do-natural-language-metaphors` ingest already links to `human-writing-structures-transfer-to-llms-because-failure-modes.md` and `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`; it should also link to this source as the original study it follows up on.

## Bidirectional Candidates

- [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) <-> [metaphors-we-think-with.ingest.md](../../../../../sources/metaphors-we-think-with.ingest.md) — **compares-with**: This is the strongest bidirectional candidate. Steen et al. explicitly follow up on and critique the Thibodeau & Boroditsky line of research. The `when-do-natural-language-metaphors` ingest's Connections Found section does not currently link to `metaphors-we-think-with.ingest.md`, but it should: the critique is meaningless without the original claim it tests. Both sources share the same occasion ("What human-reader evidence can inform the planned Commonplace note about figurative wording and reasoning?") and the same domains (metaphor, framing, reasoning). The tension between them (positive effect vs. null result with controls) is itself the most valuable insight for any KB reader.

## Reverse-edge Candidates

- [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) → [metaphors-we-think-with.ingest.md](../../../../../sources/metaphors-we-think-with.ingest.md) — **compares-with**: Under `kb/sources/COLLECTION.md` rules, this source should author a link to the original Thibodeau & Boroditsky study it replicates and critiques. The current ingest does not do so. This is the clearest reverse-edge candidate: the source's own summary says it is a "direct methodological critique and follow-up replication attempt" of Thibodeau & Boroditsky, but the Connections Found section links to `human-writing-structures-transfer-to-llms-because-failure-modes.md`, `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`, `first-principles-reasoning-selects-for-explanatory-reach-over.md`, and `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` — none of which are the original study.

- [knowledge-storage-does-not-imply-contextual-activation.md](../../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → [metaphors-we-think-with.ingest.md](../../../../../sources/metaphors-we-think-with.ingest.md) — **is-evidence-for**: Under `kb/theory/COLLECTION.md` rules, this note could strengthen its "expert-witness pattern" evidence by citing the covert-effect finding. The note already cites two human-studies antecedents (Tulving & Pearlstone, Gick & Holyoak); Thibodeau & Boroditsky provides a third with a different mechanism (frame-consistent knowledge structures) and a cleaner demonstration of the unrecognized-influence pattern. This is a candidate for the note's author to evaluate, not a connect write.

## Off-authorisation Candidates

None. All articulated candidates found an authorised label in the source's outbound set.

## Raw Text Candidates

None. The source is a frontmatter-bearing ingest report; the prospecting surface is the ingest itself, not a raw text companion.

## Rejected Candidates

- `agent-memory-systems/*` — body search returned only passing mentions of "framing" in review context (README framing, universal memory layer framing). No artefact carries a claim about metaphor or covert influence on reasoning that would gain concrete value from this source. Rejecting: topical proximity without articulation-test pass.

- `agentic-systems/*` — no relevant matches. Rejecting: no overlap with the source's claim surface.

- `reference/*` — no relevant matches. Rejecting: the reference collection is about the shipped Commonplace system, not about metaphor framing or reasoning effects. The source's evidence does not bear on system-operation claims.

- `kb/theory/context-contamination-operates-below-an-agents-compliance-reasoning.md` — body search returned a hit on "covert" but the note is about stance drift in writer agents, not about metaphor framing effects on human reasoning. The source's evidence does not bear on that claim. Rejecting: keyword match without articulation-test pass.

## Index Membership

- **metaphor-and-framing** (proposed) — This source, together with `when-do-natural-language-metaphors-influence-reasoning.ingest.md` and `language-models-like-humans-show-content-effects-on-reasoning.ingest.md`, forms a coherent cluster on metaphor framing and content effects on reasoning. No such index currently exists. A future writer could create one if the cluster grows.

## Synthesis Opportunities

- **Metaphor framing effects on reasoning: positive evidence vs. null result with controls** — `metaphors-we-think-with.ingest.md` (positive: single-word manipulation shifts reasoning 18-22%) and `when-do-natural-language-metaphors-influence-reasoning.ingest.md` (null: effect disappears with proper controls) together imply a higher-order claim not yet captured: *the empirical status of metaphor framing effects on human reasoning is contested; the positive finding does not survive improved experimental design, and the question reframes to boundary conditions.* This synthesis does not yet exist as a note. It would be a natural parent for both sources and for any future note on figurative wording and reasoning.

- **Covert influence across human and LLM reasoning** — `metaphors-we-think-with.ingest.md` (human covert metaphor framing), `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` (LLM content effects), and `human-writing-structures-transfer-to-llms-because-failure-modes.md` (failure-mode overlap theory) together imply that covert framing/content effects are a cross-domain phenomenon with different surface manifestations in humans and LLMs. No synthesis note captures this cross-domain pattern. The `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` note is the closest existing anchor.

## Maintenance Observations

- **Missing reciprocal link**: `when-do-natural-language-metaphors-influence-reasoning.ingest.md` explicitly positions itself as a follow-up to Thibodeau & Boroditsky but does not link to `metaphors-we-think-with.ingest.md`. This is a traversal gap in the sources cluster.

- **Planned note absent**: The ingest's occasion mentions a "planned Commonplace note about figurative wording and reasoning." No such note exists in `kb/theory/` as of this connect run. The source's extractable value items 1 and 2 (single-word manipulation result, covert-activation gap) are flagged for promotion into that note, but the note has not been written. Until it exists, the source's primary outbound surface remains the existing theory links.

- ** Quote gap**: Both `metaphors-we-think-with.ingest.md` and `when-do-natural-language-metaphors-influence-reasoning.ingest.md` have empty `## Quotes` sections. For sources whose empirical claims are the primary value, retained verbatim quotes would strengthen future grounding checks. This is a capture-quality observation, not a connection candidate.

## Flags

- **Split candidate**: The source connects to theory notes across three distinct topic areas (knowledge activation, human-writing transfer/failure modes, frontloading, prompt ablation, human-LLM differences) and makes independent assertions about each. The extractable value items span empirical evidence (items 1, 2, 5), mechanistic detail (items 3, 4), and scope limitation (item 6). A future writer promoting this source into a note should decide whether to write one integrated note or split across topics.

- **Tension flag**: The relationship between `metaphors-we-think-with.ingest.md` (positive effect) and `when-do-natural-language-metaphors-influence-reasoning.ingest.md` (null result with controls) is a live scientific tension, not a resolved contradiction. Any KB claim that cites one without the other is selectively evidence-based. The tension should be preserved, not resolved, in any note that uses either source.
