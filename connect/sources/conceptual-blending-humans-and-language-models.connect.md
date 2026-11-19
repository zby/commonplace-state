---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/conceptual-blending-humans-and-language-models.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Conceptual blending in humans and language models

**Source:** [Conceptual blending in humans and language models](../../../../sources/.snapshots/conceptual-blending-humans-and-language-models.md)

The source is an immutable snapshot (Lynn 2026, Frontiers in Psychology, conceptual analysis, no new experiment). Under `kb/sources/COLLECTION.md` the snapshot never authors links; every outbound candidate below is a recommendation for the not-yet-written `kb/sources/conceptual-blending-humans-and-language-models.ingest.md`. No ingest exists at the time of this run.

Source claim summary used for judging candidates: blending is goal-selected projection of source-concept features into a new concept; in humans the goal is an internal parent node in a predictive-processing hierarchy (precision-weighted selection, error-driven revision, embodied affordances); in LLMs purposiveness is a "proxy-goal" externalized in alignment, prompt framing, context and decoding. Three claimed differences: (1) LLMs hold linguistic traces of image-schematic structure without the perception-action grounding that makes it operative; (2) superposition makes conflicting constraints yield "generic compromises" rather than structured resolution; (3) ICL gives short-term adaptation but not lasting model change, and reflection needs prompted scaffolding. Proposed remedy: an intermediate affordance layer (goal -> affordance spec -> candidate -> causal test -> revision). All mechanism claims are conceptual; the VSA toy model is an in-principle illustration.

## Discovery Trace

**Contract reads:**
- `kb/sources/COLLECTION.md` outbound section: destinations theory, reference, agent-memory-systems, agentic-systems, tags, sources, external; `kb/work/` and `kb/instructions/` excluded. Labels per destination: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- `kb/types/connect-report.md` loaded before discovery.

**Pre-check for existing coverage:**
- `ls kb/sources | grep -iE 'blend|relevan|superpos|interfer|sato|prompt-induced'` -- only `gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md`; no existing ingest of this paper or of Sato 2025 (cited as ref 43).
- `rg -il 'blend' kb --glob '*.md' --glob '!kb/work/**'` -- hits are incidental uses ("blend" as ordinary verb in agentic-system analyses and memory reviews) plus the four new untracked source ingests; no artifact treats conceptual blending as a topic.
- `rg -il -e 'Fauconnier|conceptual (blend|integration)'` over permitted destinations -- no hits.
- Read `kb/work/epistemic-relevance-and-conceptual-blending/README.md` for context only (excluded destination). It is the active workshop on agents assigning unsupported relations between two useful ideas; its recent Q001 closure qualified the "one mechanism" claim across interference sources (commit 67d941382). Its outbound links pointed at theory notes `lightweight-search-control-does-not-license-adoption`, `knowledge-storage-does-not-imply-contextual-activation`, `capable-agents-need-methodology-selection`, `llm-context-is-composed-without-scoping`, and source ingests on semantic leakage, GSM-DC, content effects, persona reasoning, generalization bias, MDS hallucination.

**Title listing scan (theory):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles), filtered with `grep -iE 'context|interfer|goal|relevan|ground|embod|prompt|scaffold|superpos|concept|distractor|compromise|reflect|self-correct|model change|weights|in-context|world model|affordance|purpos|generic|creativ|analog|framing|attention|underspecif'`. Flagged: `llm-generation-relaxes-goals-where-human-writing-stalls`, `a-goal-holding-interpreter-fails-soft-...`, `human-analogies-suggest-functions-not-component-boundaries`, `knowledge-storage-does-not-imply-contextual-activation`, `context-contamination-operates-below-...`, `world-models-assess-explanatory-reach-through-action-conditioned`, `in-context-learning-presupposes-context-engineering`, `llm-learning-phases-fall-between-human-learning-modes`, `agentic-systems-interpret-underspecified-instructions`, `kb-goals-in-always-loaded-context-guide-inclusion-decisions`, `llm-context-is-composed-without-scoping`.

**Description listing scan (sources):**
- `rg -N --no-heading -m1 '^description:' kb/sources/*.ingest.md | grep -iE 'ground|embod|concept|creativ|prompt framing|in-context|superpos|instruction tuning|RLHF|alignment|world model|analog'` -- flagged `interpolation-extrapolation-hyperpolation`, `towards-causal-representation-learning`, `seed-programmed-autonomous-general-learning`, `smolensky-proper-treatment-connectionism`, `pattee-physics-of-symbols-2001`, `when-is-it-better-to-think-without-words`, `psychology-solves-ai-memory-identity-construction-...`, `language-models-like-humans-show-content-effects-on-reasoning`.
- Descriptions read for workshop-linked ingests: `semantic-leakage-lms-gonen`, `gsm-dc-...`, `persona-assigned-llms-motivated-reasoning`, `llm-validity-plausibility-conflation-content-effects`, `peters-chin-yee-llm-generalization-bias`, `from-single-to-multi-llm-hallucination-mds`.

**Topic indexes:**
- Tag head list `ls kb/tags/`; read heads of `llm-reliability-README.md` and `goal-prioritization-README.md`. Source carries no `tags:` (snapshot), so no by-tag `rg`; heads read only to judge future ingest tag fit.

**Body search:**
- `rg -il -e 'superposition'` (theory, reference, sources, agentic-systems, agent-memory-systems, tags) -- no hits.
- `rg -il -e 'conflicting constraints|competing constraints'` -- only `an-action-model-matters-only-through-its-consumption-path.md` (unrelated: action-model consumption).
- `rg -il -e 'generic compromise|averag(e|ing) (of|across) (goals|constraints)'` -- no hits.
- `rg -il -e 'relevance (selection|realization|judg)'` -- memory-system reviews and `activate-behavior-changing-memory.md`, `pointer-design-tradeoffs-in-progressive-disclosure.md`; all about retrieval relevance scoring, not goal-conditioned concept construction. Rejected.
- `rg -il -e 'embodi'` -- bitter-lesson and factory notes, `llm-learning-phases-fall-between-human-learning-modes.md`, `pattee-physics-of-symbols-2001.ingest.md`; only the learning-phases note engages a comparable human/LLM contrast.
- `rg -il -e 'proxy.goal'` -- no hits.
- `rg -il -e 'affordance'` -- `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` (uses "affordances" in the reader sense), several reviews; ordinary-English use. Only the human-llm-differences note kept for evaluation.
- `rg -il -e 'predictive processing|free.energy|active inference'` -- `memory-systems-table.md`, `Closure-SDK.md`; incidental.
- `rg -l -i 'affordance|embodied|grounding problem' kb/agentic-systems kb/agent-memory-systems` -- 10 review hits, all RAG/"grounding" in the retrieval-citation sense. Rejected as a group.

**Link following:**
- `llm-generation-relaxes-goals-where-human-writing-stalls.md` read fully: argmax-over-plausibility relaxation hypothesis; links to `generation-confidence-does-not-by-itself-certify-soundness.md` (exists).
- `human-analogies-suggest-functions-not-component-boundaries.md` read fully; followed to `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md`, whose principle 2 "Goal-relevant filtering (working self)" is the closest existing KB treatment of goal-gated selection.
- `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` opening read: concerns document conventions for dual audiences, not cognitive mechanism.
- `llm-context-is-composed-without-scoping.md` line 36: the qualified interference paragraph (GSM-DC, Gonen, Lampinen) post-Q001.
- `seed-programmed-autonomous-general-learning.ingest.md` body read: causal-relational models, analogy, revision; useful comparison partner.

**External:** the source's own URL is already in hand (`derived-from` authorised for external). No web prospecting performed.

## Connections Found

All are candidates for the future `kb/sources/conceptual-blending-humans-and-language-models.ingest.md`.

- [Lynn 2026, Frontiers in Psychology](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1849083/full) -- **derived-from**: the ingest analysis is worked out from this article (DOI 10.3389/fpsyg.2026.1849083).
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- **compares-with**: on the axis "what LLM output looks like when constraints cannot all be met". The note hypothesizes argmax-over-plausibility that silently drops one conjunct; Lynn proposes superposition interference that selects tokens "lexically consistent with all constraints while not satisfactorily addressing any" (a generic compromise). Two rival conjectural mechanisms for the same surface symptom, both human/LLM contrasts, neither measured. Not `is-evidence-for`: Lynn offers no data.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- **compares-with**: on the axis "inferring an engineered architecture from a human cognitive mechanism". Lynn moves from a human predictive-processing hierarchy to a recommended "intermediate affordance layer" for AI; the note supplies the test that separates the surviving function (goal-conditioned feature selection and error-driven revision) from the inherited component boundary. The ingest should apply that test rather than adopt the layer.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -- **compares-with**: on goal-gated selection. The note judged Conway's "working self" goal-relevant filtering mostly decorative for agents (reduces to relevance filtering, no involuntary intrusion). Lynn's claim is different in kind: goals select which *features* project into a constructed concept, and LLM interference is involuntary at the representational level. The comparison tests whether the decorative verdict extends to construction-time selection.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- **compares-with**: on the axis "available versus operative knowledge". Lynn says LLMs have "linguistic traces" of image-schematic and force-dynamic structure but lack what makes them "operative constraints"; the note separates loaded knowledge from knowledge that governs behavior. Same distinction, different proposed gate (embodied grounding versus context activation).
- [World models assess explanatory-reach through action-conditioned prediction](../../../../theory/world-models-assess-explanatory-reach-through-action-conditioned.md) -- **compares-with**: on the axis "closed action-test-revise loop". Lynn locates human conceptual flexibility in a loop where "action tests those affordances, and prediction error revises the model over time"; the note states when action-conditioned prediction tests a commitment. Lynn's affordance-layer proposal is a version of that loop applied to concept construction.
- [LLM learning phases fall between human learning modes](../../../../theory/llm-learning-phases-fall-between-human-learning-modes.md) -- **compares-with**: on the human/LLM learning-mode mapping. Lynn's third distinction ("short term adaptability but not lasting model change") assumes ICL maps onto short-term human adaptation and pretraining onto nothing goal-revising; the note argues the phases do not map 1:1, which bounds how far Lynn's contrast can be read as a clean dichotomy (Lynn himself says it is "not an all-or-none opposition").
- [Seed-programmed autonomous general learning ingest](../../../../sources/seed-programmed-autonomous-general-learning.ingest.md) -- **compares-with**: on the axis "architecture for goal-driven causal model construction and revision". Thórisson's seed grounds drives in observable variables and builds causal-relational models revised by analogy and reflection; Lynn proposes goal -> affordance specification -> candidate -> causal test -> revision. Both are architecture proposals from outside LLM training that make causal revision intrinsic; Thórisson has AERA implementation cases, Lynn only a toy VSA script.
- [Interpolation, extrapolation, hyperpolation ingest](../../../../sources/interpolation-extrapolation-hyperpolation.ingest.md) -- **compares-with**: on the axis "novelty relative to a training distribution". Lynn's "distributionally novel blends" are novel yet consistent with learned statistics; Ord's vocabulary distinguishes within-subspace from off-subspace novelty and could make Lynn's category precise.

## Bidirectional Candidates

- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) <-> source -- **compares-with**: the note's mechanism is explicitly conjectural and grounded only in Borretti's polemic. A rival mechanism (generic compromise under interference) belongs in its Scope or Open questions section once the ingest exists. The return link helps a reader of the note see that "relaxation" and "compromise" predict different surface signatures (one conjunct missing versus all conjuncts weakly addressed), which is a discriminating observation.

## Reverse-edge Candidates

- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) → future ingest -- under theory's own rules, an example citation: Lynn's affordance-layer recommendation is a fresh instance of the function-versus-boundary inference the note analyzes (currently illustrated only by the Tulving three-space case).
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → future ingest -- could cite Lynn as a source whose goal-gating principle concerns concept construction rather than memory retrieval, which the principle-2 verdict does not cover.

Reverse edges only after the ingest exists; the theory collection's `COLLECTION.md` governs the labels, which this run did not read.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) -- topical match on interference, but Lynn's superposition-interference account concerns conflicting *task* constraints, not unlicensed context content. Adding it to that note's interference list would repeat the Q001 error the workshop just closed (merging distinct paradigms under one mechanism without a comparison). Rejected as a link; see Flags.
- [GSM-DC ingest](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md), [semantic leakage ingest](../../../../sources/semantic-leakage-lms-gonen.ingest.md) -- empirical irrelevant-context studies; Lynn neither cites nor measures them, and the shared word "interference" does not name a shared axis Lynn addresses. Keyword-only.
- [Persona-assigned LLMs motivated reasoning ingest](../../../../sources/persona-assigned-llms-motivated-reasoning.ingest.md) -- goal-like framing steering output, but identity-congruent judgment is not concept construction. Weak.
- [Peters and Chin-Yee generalization bias ingest](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md), [MDS hallucination ingest](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md) -- "generic" outputs there are overgeneralized claims or off-instruction answers; superficially resembles Lynn's "generic compromises" but different phenomena. Could become relevant if the workshop's watch finds a common observation; not now.
- [Towards causal representation learning ingest](../../../../sources/towards-causal-representation-learning.ingest.md) -- Lynn's causal-versus-correlational contrast cites Wu et al. 2024, not Schölkopf; the comparison adds little beyond the seed-programmed candidate.
- [Smolensky ingest](../../../../sources/smolensky-proper-treatment-connectionism.ingest.md), [Pattee physics of symbols ingest](../../../../sources/pattee-physics-of-symbols-2001.ingest.md) -- representation-level vocabulary is adjacent to Lynn's superposition-versus-structure contrast, but no shared axis tight enough for `compares-with`.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- concerns document conventions for dual audiences; Lynn's differences are cognitive mechanisms with no document-design consequence. Not `is-evidence-for`.
- [KB goals in always-loaded context guide inclusion decisions](../../../../theory/kb-goals-in-always-loaded-context-guide-inclusion-decisions.md) -- tempting reading that "proxy-goals live in the context window" supports always-loaded goals, but the note's warrant is hop cost and decision frequency, not Lynn's mechanism. Would be a decorative link.
- [A goal-holding interpreter fails soft](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md), [In-context learning presupposes context engineering](../../../../theory/in-context-learning-presupposes-context-engineering.md), [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md), [Context contamination operates below compliance reasoning](../../../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- share vocabulary (goal, in-context, interpretation, interference) without a claim Lynn bears on.
- `kb/agentic-systems/` and `kb/agent-memory-systems/` hits for affordance/embodied/grounding -- retrieval-citation sense of "grounding"; no system reviewed implements goal-conditioned concept construction.
- `kb/reference/` -- no plausible trigger; Lynn does not bear on Commonplace's shipped system.

## Index Membership

- [LLM reliability tag head](../../../../tags/llm-reliability-README.md) -- possible ingest tag only if the ingest's analysis treats the generic-compromise mechanism as an output-deviation diagnosis; Lynn's conceptual framing alone may not meet "substantive connection to output deviation or correction". Sources are outside tag participation, so this is search-scoping only.
- [Goal prioritization tag head](../../../../tags/goal-prioritization-README.md) -- likely not: Lynn's goals select features for concept construction, not which concerns get effort.

## Synthesis Opportunities

None at this depth. A candidate exists but should not be drafted: "relaxation" (one conjunct dropped) and "generic compromise" (all conjuncts weakly addressed) are two conjectural LLM responses to unsatisfiable constraint sets that predict different observable signatures. That is a discriminating observation for the epistemic-relevance workshop's watch, not yet a theory claim.

## Maintenance Observations

- The epistemic-relevance-and-conceptual-blending workshop is named after this topic but no tracked artifact treats conceptual blending (Fauconnier and Turner) at all; this source is the first. Whoever writes the ingest should decide with the workshop owner whether it enters the workshop's evidence register; connect does not link into `kb/work/`.
- Lynn cites Sato 2025, "The way we prompt: conceptual blending, neural dynamics, and prompt-induced transitions in LLMs" (arXiv 2505.10948), which is the more direct LLM-blending source and is not ingested.

## Flags

- **Tension guard from Q001:** Lynn's superposition-interference claim is conceptual and cites only Elhage et al. 2022 (toy models of superposition). It must not be listed as a further member of a common interference mechanism in `llm-context-is-composed-without-scoping.md` or the Gonen ingest; the workshop just qualified that unsupported merge.
- **Evidence strength:** every mechanism claim (human predictive-processing blending, LLM proxy-goals, generic compromise) is a conceptual analysis without new data; the VSA script is an in-principle illustration. Hence `compares-with` throughout and no `is-evidence-for`.
- **The source's goal-selected projection is directly relevant to the workshop's watched failure** (two useful ideas fused because both serve one goal). Lynn treats goal-selected fusion as the *success* mode of blending. This is a tension the workshop's review point should weigh: the same mechanism may produce both productive blends and unsupported relations.
- Not a split candidate.
