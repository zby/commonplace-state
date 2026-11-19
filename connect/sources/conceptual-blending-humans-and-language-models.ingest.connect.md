---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/conceptual-blending-humans-and-language-models.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: Conceptual blending in humans and language models

**Source:** [Ingest: Conceptual blending in humans and language models](../../../../sources/conceptual-blending-humans-and-language-models.ingest.md)

The ingest already carries nine labelled footer edges (theory and sources). This report proposes additions only; existing edges were re-checked and all targets exist.

## Discovery Trace

**Linking rules:** `kb/sources/COLLECTION.md` "Outbound links" section. Destinations prospected: theory, reference, agentic-systems, tags, sources. `kb/agent-memory-systems/` is frozen/historical and was not prospected. `kb/work/` and `kb/instructions/` are excluded. External prospecting skipped (only the already-present `derived-from` URL).

**Description / title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` filtered with `rg -i 'goal|relev|interfer|distract|constraint|plausib|ground|analog|figur|metaphor|human|novel|combin|select|precision|error|test|embod'` -- flagged: figurative-wording (source-domain projection), synthesis-is-not-error-correction (merge without test), borrowed-patterns-transfer-only-over-shared-mechanism, a-goal-holding-interpreter-fails-soft, short-composable-notes-maximize-combinatorial-discovery, human-writing-structures-transfer-to-llms.
- `rg '^description:'` read on each flagged candidate and on the sibling workshop ingests (E15-E18).

**Topic indexes:**
- `kb/tags/` listing scanned; `goal-prioritization`, `failure-modes`, `llm-reliability`, `learning-theory` heads checked by description. None has an inclusion condition this ingest substantively meets (goal-prioritization is about which goals get effort, not goal-driven concept construction). Source carries no `tags:`, so no tag-scoped rg was run.

**Body search** (all over `kb/theory kb/reference kb/agentic-systems kb/sources kb/tags`):
- rg -i "blend" -- hits in the four sibling workshop ingests, scientisttwo (feature "blending" in an ML method, irrelevant), vocabulary-collisions note (incidental), sutskevers-list. Only sibling ingests kept for evaluation.
- rg -i "conceptual integration|Fauconnier" -- only the source.
- rg -i "predictive processing|predictive-processing|free energy" -- only the source.
- rg -i "precision-weight|precision weighting" -- only the source.
- rg -i "superposition" -- only the source.
- rg -i "image schema|affordance" -- generic "affordance" usages in theory/agentic-systems; none about affordance layers or image schemas. Rejected as keyword-only.
- rg -i "embodied|grounding problem|symbol grounding" -- pattee ingest, llm-learning-phases (already linked), factory notes; nothing on embodied grounding of concepts.
- rg -i "conflicting constraints|conflicting instructions|compromise" -- learning-inside-a-fixed-decomposition (already inline), autogenesis review, misc. No note on compromise outputs.
- rg -i "motivated reasoning|goal-congruent|confirmation bias" -- reasoning-production-is-not-reasoning-evaluation, persona-assigned motivated-reasoning ingest (sibling).
- rg -i "Sato|conceptual combination|novel combination" -- alien-space-of-science, automated-synthesis-is-missing-good-oracles; no Sato ingest exists.
- rg -i "analog(y|ies)" -- human-analogies (already linked), borrowed-patterns, figurative-wording, three-space-agent-memory-echoes-tulving.
- rg -n -i 'generic' in the MDS ingest; rg -n -i 'goal|congruen' in the persona ingest -- confirmed substantive overlap (below).
- rg -i "affordance layer|goal-conditioned|concept construction" over agentic-systems and reference -- no hits.

**Link following:**
- MDS ingest footer -> out-of-spec-output, reverse-compression, soft-degradation; checked reverse-compression and relaxed-goal descriptions for a generic-output signature.
- figurative-wording -> borrowed-patterns (its stated parent); confirmed borrowed-patterns is the general rule behind human-analogies.

## Connections Found

- [From Single to Multi: How LLMs Hallucinate in MDS (ingest)](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md) -- **compares-with**: output under a task constraint the input cannot satisfy. Asked for insights shared across documents when none (or no subtopic) exists, models emit unshared, generic and off-instruction bullets rather than abstaining, and the authors note bullets that merge two reference ideas. That is the nearest measured case in the KB of the condition Lynn's "generic compromise" conjecture is about, and it gives the source's Extractable Value item 4 (compromise vs. relaxed-goal signatures) a real dataset to check against. Caveat for the writer: MDS's constraint is unsatisfiable by input absence, not by conflict between constraints, so it bounds rather than tests Lynn's claim.
- [Figurative wording can suggest relations that the target claim does not justify](../../../../theory/figurative-wording-imports-source-domain-entailments-unless-mapped.md) -- **compares-with**: selective projection from a source domain. Lynn says a goal selects which source features enter a blend; the note says a figure carries source-domain relations into the target unless the mapping is stated and justified. Same axis (which source relations project), opposite emphasis (productive selection vs. unwanted import), and the note supplies the KB's existing human framing evidence (Thibodeau/Boroditsky, Steen et al.).
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- **compares-with**: combining multiple sources without a discarding test. The source's Extractable Value item 3 reads an unsupported relation as a goal-selected blend no error signal has checked; the note's claim that merging propagates errors while only selection-against-a-check corrects them is the KB's existing statement of that split, at the multi-agent scale.
- [Theory builder](../../../../theory/definitions/theory-builder.md) -- **defined-in**: the Learning Claims section assesses Lynn's loop against this definition's criteria (consumption, iteration, criticism, localized content) inline but the footer lacks the edge. Footer entry recommended so the reader who does not know the term reaches it.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: where the decomposition being learned over is fixed. Already linked inline in "What it adds or questions" (source concepts and image-schema vocabulary fixed, only precision updated) but missing from the footer; adding it keeps the footer complete.

## Bidirectional Candidates

- [Figurative wording can suggest relations that the target claim does not justify](../../../../theory/figurative-wording-imports-source-domain-entailments-unless-mapped.md) <-> source -- the note's "LLM transfer is a conjecture" section has no account of how an LLM chooses which source relations to project; a theory-side mention could cite this ingest as a (conceptual, untested) proposal for that selection. Theory-side outbound to sources is governed by `kb/theory/COLLECTION.md`, not checked here.

## Reverse-edge Candidates

- [From Single to Multi: How LLMs Hallucinate in MDS (ingest)](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md) -> source -- **compares-with** (sources->sources is authorised): its generic/merged-bullet findings would gain a named rival interpretation (Lynn's superposition compromise) next to its untested count-mismatch hypotheses.
- [Persona-assigned LLMs exhibit motivated reasoning (ingest)](../../../../sources/persona-assigned-llms-motivated-reasoning.ingest.md) -> source -- **compares-with**: goal- or identity-congruent selection that no disconfirming check corrects. The persona result is an LLM instance of the failure the conceptual-blending ingest says Lynn omits for humans (goal-congruent projection that stabilises without disconfirmation). Either direction works; inbound from the persona ingest is where the measured evidence sits.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- relevant to the affordance-layer inference, but the already-linked human-analogies note is the narrower, directly applicable test; a second edge adds little.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) -- "generic compromise" output resembles content-thin output, but reverse compression concerns expansion of a compact seed, not constraint conflict. Keyword-level overlap.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) -- motivated-reasoning hit is incidental to review-system design; no shared axis with goal-selected blending.
- [Generalization bias in LLM summarization (ingest)](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) -- "generic" there means generic (quantifier-dropping) claims, a different sense from Lynn's generic compromise. Vocabulary collision, not a connection.
- [LLM validity/plausibility conflation (ingest)](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) -- content effects on syllogism validity; no bearing on feature selection in blending beyond the shared workshop.
- [Short composable notes maximize combinatorial discovery](../../../../theory/short-composable-notes-maximize-combinatorial-discovery.md) -- "combinatorial discovery" is co-loading notes, not conceptual blending; tempting surface match that would mislead.
- [A goal-holding interpreter fails soft](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- about re-routing around blocked steps, not goal-driven selection of content.
- scientisttwo ingest "blending" hit -- an ML method's feature-blend interface; unrelated.
- Generic "affordance" hits in theory/agentic-systems -- ordinary-English usage; none concern affordance layers or image schemas.
- reference and agentic-systems -- no candidates; the source makes no claim about the shipped system or an external agent system.

## Index Membership

None. No tag head's inclusion condition is substantively met; the source enters as a conceptual comparison partner for a workshop.

## Synthesis Opportunities

The source (generic compromise), [LLM generation can hide a relaxed goal](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) (silently dropped conjunct) and the [MDS ingest](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md) (generic/unshared bullets instead of abstention) together suggest a candidate claim: an LLM facing an unsatisfiable task specification has several distinguishable output signatures (drop one constraint, thin all constraints, substitute generic content, abstain), and which one occurs is an open empirical question. Not authored here; the epistemic-relevance workshop is the natural place to weigh it.

## Maintenance Observations

- No ingest for Sato (2025), arXiv 2505.10948, which the source names as the empirical LLM-blending work; the KB has no direct LLM-blending evidence.
- The ingest's inline links to theory-builder and learning-inside-a-fixed-decomposition are absent from its footer.

## Flags

- Tension: the ingest's "Connections Found" prose says Lynn's interference claim should not be grouped with irrelevant-context studies; the MDS compares-with edge above must keep that boundary (MDS is input absence, not irrelevant content or conflicting constraints).
- The four sibling workshop ingests (E15-E18) and this one are all uncommitted; cross-links among them should be authored together to avoid one-sided edges.
