---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/llm-validity-plausibility-conflation-content-effects.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: How Language Models Conflate Logical Validity with Plausibility

**Source:** [Ingest: How Language Models Conflate Logical Validity with Plausibility](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md)

This report replaces an earlier cache report written against the snapshot before the tracked ingest existed. The ingest now authors nine outbound edges in its `## Connections Found` prose: the Lampinen, Gonen, Lampinen-essay and Fodor-Pylyshyn ingests, and the theory notes on out-of-spec output, error correction, unscoped context, structured-prompt gains and reasoning production. Those are treated as already encoded and are not re-proposed. This report covers new outbound candidates and the reverse edges, which matter most here: no artifact outside `kb/reports/cache/` links to this ingest yet.

**Source claim, as read:** Within the last-token residual stream and difference-in-means directions, validity and plausibility are single linear directions that steer verdicts in late layers. They are aligned at cosine about 0.5-0.64, against controls near 0.1, and cross-steer in both directions. Alignment predicts content-effect size across 57 model-prompt pairs. A task-difference vector, with layer and scale selected per model, cuts the content effect. CoT lowers the content effect, but alignment and cross-steering persist.

## Discovery Trace

**Collection contract:** Read `## Outbound links` in `kb/sources/COLLECTION.md`. Authorised destinations are theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded as link targets. The labels are `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` and `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (sparingly) and `derived-from` (external). External prospecting was skipped: no external target was supplied, and the arXiv URL is already in `source`.

**Destination breadth:**
- theory, sources: full prospecting; the source's claim and Connections Found point here.
- reference: skipped after a body search; no reference doc treats model-internal bias, steering or content effects.
- agentic-systems: body search only; hits were retained AAS reports using "content effect" in an unrelated sense.
- agent-memory-systems: historical and frozen per `AGENTS.md`; skipped after the body search returned only `reviews/claude-obsidian.md` (keyword use of "probing").
- tags: read as an index surface (see Index Membership).

**Topic indexes:**
- `kb/tags/llm-reliability-README.md` (the source's tag): the Taxonomy and Error Correction Theory groups list out-of-spec, error-correction and systematic-prompt-variation. The first two are already linked. `systematic-prompt-variation-serves-verification-and-diagnosis-not.md` was evaluated and rejected (below).

**Title listing:**
- `rg -N --no-heading -m1 '^# ' theory --glob '*.md' | rg -i "bias|plausib|valid|interpret|correlat|chain-of-thought|CoT|reasoning|parametric|weights"`: flagged `reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md`, `llm-context-interprets-instructions-and-content-through-one-medium.md`, `parametric-reproduction-cannot-replace-an-authoritative-record.md`, `semantic-review-catches-content-errors-that-structural-validation.md` and the already-linked notes. All were evaluated and rejected below, except where kept.

**Description listing:**
- `grep -m1 '^description'` over the flagged theory notes and over source ingests found by body search: `gsm-dc-...`, `when-do-natural-language-metaphors-...`, `verbalizable-representations-global-workspace-llms`, `language-models-dont-always-say-what-they-think`, `towards-faithfully-interpretable-nlp-systems`, `concept-bottleneck-models`, `assessing-llm-reasoning-evidence-based-claim-verification`.

**Body search:**
- `rg -l -i "content effect|content-effect|syllogis|plausibilit|belief bias|steering vector|activation steering|linear representation|residual stream|probing"` over theory, reference, agentic-systems, agent-memory-systems, sources, tags: 55 files. Most "plausibility" and "probing" hits are ordinary usage.
- `rg -n -i "content effect|content-effect|syllogis|belief bias|steering vector|activation steering|cross-steer"` over the same set: concentrated on the Lampinen cluster (error-correction, human-writing-structures, structured-prompt-gains, context-contamination, llm-context-is-composed-without-scoping, out-of-spec), the GSM-DC and Gonen ingests, and `reflection-makes-retained-lessons-second-order.md` (mention only).
- `rg -l -i "interpretab|probe|parametric" theory`: 30 files. Kept none beyond the cluster; `knowledge-storage-does-not-imply-contextual-activation.md` was evaluated (rejected).
- `rg -l "llm-validity-plausibility-conflation" --glob '*.md' .` excluding the cache: no inbound links anywhere.

**Link following:**
- GSM-DC ingest, lines 109-123: its three-paradigm comparison (count / associative concepts / belief congruence) says the training-response divergence is "evidence against assuming one mechanism across the three paradigms". This paper supplies a mechanism for the Lampinen end only, so GSM-DC is the natural reverse-edge author.
- `context-contamination-...`: its "noticing can fail to neutralize" and "expressed refusal can coexist with residual steering" are the agent-level analogue of the paper's CoT finding, but the note's evidence is stance drift from injected material.
- Turpin ingest summary: CoT rationalizes bias-driven answers without naming the biasing feature. That is a separate CoT-versus-internal-signal axis from Lampinen's.
- J-space ingest quotes: "the information relevant to the automatic computation is present in the J-space but unused for the task". Compared on whether a represented concept causally routes into a decision.
- `out-of-spec-...` line 18: the "Content bias" catalogue bullet is still unsourced; the remedy paragraph (line 29) lists no model-internal remedy.

## Connections Found

All are recommendations for a future edit of the ingest's `## Connections Found`.

- [Language models don't always say what they think (Turpin et al.)](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) -- **compares-with**: Both papers test how chain-of-thought relates to an internal bias signal, with opposite surface results. In Turpin, CoT leaves a biased answer in place and omits the feature that caused it. In this paper, CoT removes most of the behavioural content effect while the measured validity-plausibility alignment and cross-steering persist. Together they warn against reading either the CoT text or the CoT gain as evidence about the underlying mechanism.
- [Verbalizable representations as an LLM global workspace (J-space)](../../../../sources/verbalizable-representations-global-workspace-llms.ingest.md) -- **compares-with**: Shared axis: whether a linearly readable concept causally routes into a task decision. J-space reports information present but unused in automatic computation and flexible reasoning that routes through the workspace. This paper reports a content concept that does route into an automatic validity verdict. The J-space split also offers a conjecture, untested by either paper, for why CoT could lower the effect without changing the alignment. Use as a comparison, not support, since the two methods (Jacobian lens versus difference-in-means) differ.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) -- **is-evidence-for** (qualifying): The note rests on Lampinen's content effects and argues that structures fix shared failure modes. This paper reconfirms the overlap on 2025-2026 models. It also shows that a structural intervention (CoT) can remove the behaviour while leaving the representational signature intact. So "the structure helps" is supported, but "the structure removes the failure mode" is not. The authors' training-data conjecture (valid arguments in text are usually sound) is an untested candidate for the note's imitation-versus-convergence question. This partly reverses the earlier cache report, which rejected the note as reconfirmation only; the CoT result is what makes it material.

## Bidirectional Candidates

- [Language models, like humans, show content effects on reasoning](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) <-> source -- **compares-with**: Already authored from this side. The return edge matters because the Lampinen ingest is where readers arrive for content effects. Its CoT reading ("push large models to rely more on logical strategies") should point to this paper's finding that alignment persists under CoT.
- [Language models don't always say what they think](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) <-> source -- **compares-with**: If the outbound edge above is authored, the Turpin ingest gains a representational counterpart on the same CoT-versus-internal-signal axis.

## Reverse-edge Candidates

No artifact links to this ingest yet. Theory notes would author these under `kb/theory/COLLECTION.md` as `evidenced-by`. That contract requires the context phrase to say whether evidence corroborates, qualifies or bounds; none of these is corroboration of a claim the note risked, so each should say qualifies or bounds.

- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) → ingest -- **evidenced-by** (bounds): Source for the unsourced "Content bias" bullet (line 18). Plausibility steering changes validity verdicts on fixed syllogisms, which a conforming interpreter would judge by structure. The remedy paragraph (line 29) could gain a scope sentence: a model-internal remedy layer exists but is unreachable through hosted APIs.
- [Error correction works above chance oracles with decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) → ingest -- **evidenced-by** (qualifies): The Lampinen paragraph (lines 61-63) treats content bias as uniformly shared across families. This paper finds the same pattern across three newer families but graded by model, with strength predicting effect size. The 2x2 valid/plausible design is a template for a decorrelating check that holds structure fixed and varies content; it should report per-cell accuracy, not only the difference metric.
- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) → ingest -- **evidenced-by** (bounds): The note groups Lampinen with GSM-DC and Gonen (line 62). This paper places the content-effect signal in the task's own content, which no scoping step can remove. It does not test the other members.
- [Structured-prompt gains do not establish training-distribution selection](../../../../theory/structured-prompt-gains-do-not-establish-distribution-selection.md) → ingest -- **evidenced-by** (bounds): Line 24 cites Lampinen's partial CoT reduction. This paper shows a CoT gain with no change in the measured representational signature, and the training-data account stays untested.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) → ingest -- **evidenced-by** (bounds, analogous): Validity verdicts pulled toward plausible conclusions have the same shape as accepting a plausible destination without checking the route. The task differs, so this does not test the review-gate claim.
- [GSM-DC ingest](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) → ingest -- **compares-with**: The three-paradigm paragraph (lines 109-123) is the KB's common-mechanism discussion. This paper is the only mechanism datum for the belief-congruence paradigm. It sits at the endogenous end of the axis GSM-DC already names, and its CoT result adds a fourth training/prompting response to the divergence list.
- [Language models, like humans, show content effects on reasoning](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) → ingest -- **compares-with**: See Bidirectional Candidates.
- Workshop E15 in `kb/work/epistemic-relevance-and-conceptual-blending/evidence-register.md` (line 151) is this ingest's occasion. The ingest's Recommended Next Action already directs that edge. It is outside this skill's link targets, so it is noted, not proposed.

## Off-authorisation Candidates

- `kb/instructions/` semantic-review or grounding gates -- A review gate that checks reasoning could use the plausibility-swapped 2x2 design (Extractable Value item 4) as a calibration probe. `kb/sources/COLLECTION.md` excludes `kb/instructions/` as a destination, so this is rejected for this source. The idea should reach instructions through the error-correction or reasoning-production theory notes.

## Raw Text Candidates

None.

## Rejected Candidates

- [Context contamination operates below an agent's compliance reasoning](../../../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- Close analogue ("noticing can fail to neutralize" versus CoT lowering behaviour while the signal persists), but the note is about stance drift from injected, exogenous material. Linking would blur the endogenous/exogenous distinction the ingest itself draws (Extractable Value item 6). It is reachable through llm-context-is-composed-without-scoping.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- The debiasing vector's "disentangling" reading is a bundle-to-component attribution, since the task-mean difference also encodes instruction and format differences. This is an instance of the note's failure, not evidence bearing on its claim, and the ingest's Limitations already state it. A future edit of the note could use it as a worked example; the earlier cache report also rejected it.
- [Systematic prompt variation serves verification and diagnosis](../../../../theory/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- The paper varies content under fixed structure, not framing under fixed semantics. The decorrelation lever is better carried by error-correction.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- "Probe" there means a retrieval question to the model, not a linear probe. Keyword match.
- [Reviewers share the field's prior](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- Shared-prior correlated error is adjacent, but the note concerns field consensus in review, not a model-internal bias on formal tasks.
- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) -- Mentions activation steering as a parametric pathway only. Keyword match.
- [Towards faithfully interpretable NLP systems](../../../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) -- Its "plausibility" means explanation persuasiveness, not conclusion truth. Vocabulary collision; linking would mislead.
- [When do natural-language metaphors influence reasoning](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) -- Human framing study, reached indirectly through Lampinen.
- [Assessing LLM reasoning (RECV)](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) -- Forced-binary verifier confounds are adjacent to this paper's binary-prompt limitation, but RECV studies claim verification, not validity-plausibility coupling.
- [Concept Bottleneck Models](../../../../sources/concept-bottleneck-models.ingest.md) -- Superseded capture, and about concept supervision, not steering.

## Index Membership

- [LLM reliability tag head](../../../../tags/llm-reliability-README.md) -- The ingest already carries `tags: [llm-reliability]`. Sources are outside the participating collections, so no head entry is needed. No other index applies; `kb/sources/README.md` is a landing page, not a per-source index.

## Synthesis Opportunities

- **Endogenous versus exogenous interference.** The ingest (Extractable Value item 6), the Gonen ingest's sibling paragraph and the GSM-DC three-paradigm paragraph each come close to the same distinction. Exogenous interference from injected or irrelevant context responds to scoping and exclusion. Endogenous interference from the judged task's own content needs content variation or model-internal intervention. The ingest marks this log-level; a note needs a mechanism statement and a test that varies source location under a fixed task.
- **CoT gains do not license mechanism claims in either direction.** Turpin (CoT text omits the cause), this paper (CoT removes behaviour while representation persists) and structured-prompt-gains (prompt gains do not establish distribution selection) together imply that a CoT result says nothing about mechanism on its own. structured-prompt-gains may already be the right home; check before writing a new note.

## Maintenance Observations

- `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md` line 18: the "Content bias" catalogue entry is still unsourced, while its neighbours are sourced. Flagged in the earlier cache report too; still open.
- The Lampinen ingest still uses labels outside the `kb/sources/COLLECTION.md` authorised set (`grounds`, `exemplifies`, `extends`, `evidenced-by`). Flagged in the earlier cache report too; still open.
- This ingest has no inbound links, although the workshop occasion and five theory notes cite its behavioural predecessor.

## Flags

- **Tension (carried in the ingest):** Lampinen reads CoT as partly restoring content-independent reasoning, while this paper finds the representational signature persists under CoT. Do not cite the two together for "CoT removes the content-bias mechanism".
- **Bound:** This is a mechanism for one paradigm only. Any reverse edge from GSM-DC or llm-context-is-composed-without-scoping must not present it as settling the cross-source common-mechanism question (see commit 67d941382).
- **Number check before reuse:** The ingest records internal inconsistencies (cosine range 0.48-0.64 versus 0.53-0.64; Qwen3-14B CoT figures). Reverse-edge context phrases should cite the range loosely or check the snapshot.
- No split candidate: one study, one connected claim cluster.
