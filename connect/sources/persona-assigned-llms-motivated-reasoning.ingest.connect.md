---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/persona-assigned-llms-motivated-reasoning.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning

**Source:** [Ingest: Persona-Assigned Large Language Models Exhibit Human-Like Motivated Reasoning](../../../../sources/persona-assigned-llms-motivated-reasoning.ingest.md)

The ingest already carries nine inline outbound links (five theory notes, four
sources). All nine were verified to exist and are not re-proposed below. This
report adds new candidates and the reverse edges; no inbound link to this
ingest exists anywhere in `kb/` yet (`rg -l 'persona-assigned-llms-motivated-reasoning' kb`
returns only the ingest itself).

## Discovery Trace

**Linking rules:** `kb/sources/COLLECTION.md` § Outbound links. Destinations:
theory, reference, agent-memory-systems, agentic-systems, tags, other sources;
excluded: `kb/work/`, `kb/instructions/`. Labels for sources→theory:
`is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`,
`defined-in`, `see-also`; sources→sources: `compares-with`, `see-also`.
External prospecting skipped (no externally supplied target).

**Topic indexes:**
- `kb/tags/llm-reliability-README.md` (source's tag; not `complete: true`) — Error Correction Theory and Aggregation sections surfaced `error-correction-works-above-chance...` (already linked), `systematic-prompt-variation...` (already linked), `synthesis-is-not-error-correction` (evaluated, rejected below).

**Description listing scan:**
- `rg -m1 '^description:'` over flagged files in theory and sources — flagged `semantic-leakage-lms-gonen.ingest.md`, `llm-validity-plausibility-conflation-content-effects.ingest.md`, `prompt-stability-code-llms-emotion-personality-variations.ingest.md`, `revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md`, `llm-context-is-composed-without-scoping.md`, `process-structure-and-output-structure-are-independent-levers.md`, `gentle-coding-research.ingest.md`, `from-single-to-multi-llm-hallucination-mds.ingest.md`.

**Body search** (scope: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources`):
- rg -i "persona" — hits mostly agent-memory/agentic-system reviews using "persona" as user-profile storage (off-topic); `execution-indeterminism...` (mentions Ma et al. personality framing); `human-analogies-suggest-functions...` (personalization, off-topic).
- rg -i "motivated reasoning" — only the source.
- rg -i "sycophan" — `gentle-coding-research.ingest.md` only.
- rg -i "role-play|roleplay|role play" — one trace-learning file, off-topic.
- rg -i "debias" — the source and `llm-validity-plausibility-conflation-content-effects.ingest.md`.
- rg -i "chain.of.thought|CoT" — `process-structure-and-output-structure...`, `revision-guided-by-rationale...`, `human-writing-structures...` (linked), `structured-prompt-gains...`.
- rg -i "self-consistency|voting" — reliability cluster; `synthesis-is-not-error-correction` evaluated.
- rg -i "judge bias|LLM-as-judge|LLM judge" — reviews and oracle notes; none concern persona-differentiated judges.
- rg -i "identity-congruent|belief bias|belief-congruent" — `llm-context-is-composed-without-scoping.md` (Lampinen line), `semantic-leakage-lms-gonen.ingest.md`.
- rg -i "exhortation" — only the source.
- rg -n -i "persona|personality" in `prompt-stability-code-llms-emotion-personality-variations.ingest.md` — confirms Ma et al. treat personality-style variants as semantically equivalent perturbations.

**Link following:**
- `llm-context-is-composed-without-scoping.md` lines 36–38: treats GSM-DC, Gonen, Lampinen as "prompt content the task does not license steering output" and points to the context-contamination note — led to Gonen ingest.
- `revision-guided-by-rationale...`: cites Turpin for unfaithful CoT — the same neighbourhood the source's verbalization finding sits in.
- `prompt-stability...ingest.md` links `error-correction...` with "enables" for personality variants as decorrelation — directly in tension with this source.
- Checked inbound counts of unquoted ingests on reverse-edge targets (theory unquoted-source limit is five): context-contamination 2, error-correction 1, human-writing-structures 0, systematic-prompt-variation 0.

## Connections Found

- [Prompt stability in code LLMs (Ma et al.)](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- **compares-with**: on whether persona/personality prompt variants are semantics-preserving. Ma et al. build stability metrics on the assumption that personality-style variants preserve the task; this source shows identity personas shift answers directionally on stance-bearing evidence while leaving a neutral control unchanged. A reader using persona variants for stability or decorrelation needs both.
- [Semantic leakage in LMs (Gonen et al.)](../../../../sources/semantic-leakage-lms-gonen.ingest.md) -- **compares-with**: on a prompt feature irrelevant to the item steering output. Gonen injects unrelated concepts into completions; here the irrelevant feature is an attribute of the reasoner, and the effect is conditional on the item carrying a stance. The comparison separates association-driven leakage from congruence-driven shift.
- [LLM validity–plausibility conflation (content effects steering study)](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) -- **compares-with**: on mitigation level for a content-conditioned reasoning bias. Prompt-level debiasing (CoT, accuracy clause) fails here; there a representation-level task-difference vector reduces content effects. Together they suggest where the lever is, though the bias sources differ (persona vs item content).
- [Revision guided by rationale needs faithfulness, not just legibility](../../../../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) -- **is-evidence-for**: the mitigations cut explicit identity references from 46% to 8% and 0% without removing the identity-congruent error, so after intervention the visible rationale no longer names what moved the answer. This is a second behavioral case beside Turpin for legibility diverging from faithfulness, with the added twist that the intervention itself produced the divergence. Caveat travels: no rationale-guided repair was tested.

## Bidirectional Candidates

- [Prompt stability in code LLMs (Ma et al.)](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) <-> source -- **compares-with**: Ma's ingest recommends personality templates as a calibrated decorrelation method for `error-correction...`; a return link to this source would warn that persona variants can carry a shared, content-dependent lean.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md`, theory notes may link to tracked ingests with `evidenced-by` (corroborates, qualifies, or bounds). All four targets below are under the five-unquoted-source limit.

- [Context contamination operates below an agent's compliance reasoning](../../../../theory/context-contamination-operates-below-an-agents-compliance-reasoning.md) → source -- **evidenced-by** (bounds): the note leaves open whether an explicit neutrality reminder can inoculate against a present stance (line 43). Here an accuracy/skepticism clause removed visible identity talk but not the congruent error. The context phrase must carry the caveat that the persona is a sanctioned instruction, not a contaminant.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) → source -- **evidenced-by** (qualifies): a persona is a shared systematic bias of the kind line 48 describes; same-persona samples lean together, and CoT did not decorrelate it.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source -- **evidenced-by** (bounds): line 18 says structured prompting "pushes toward content-independent reasoning"; step-by-step gave no significant mitigation against persona-induced bias.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../theory/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) → source -- **evidenced-by** (qualifies): identity personas are not semantics-preserving variants on stance-bearing items, so they give biased decorrelation and cannot stand in for surface paraphrase in diagnosis.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) -- its contamination evidence is "prompt content the task does not license"; the persona is explicitly licensed by an instruction demanding identity fidelity, so this source does not instantiate the claim. The licensed-vs-unlicensed distinction is already carried via the context-contamination link.
- [Process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) -- "think step by step" is a minimal process cue, not a structured process template; the decorrelation open question it raises is better served through the existing error-correction link.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- about merge vs vote operations; the persona result concerns correlated bias that defeats voting, which the error-correction note owns.
- [Gentle-Coding research catalog](../../../../sources/gentle-coding-research.ingest.md) -- routes sycophancy/evaluator-bias questions without grounding claims; keyword-level overlap only.
- [From single to multi-LLM hallucination (MDS)](../../../../sources/from-single-to-multi-llm-hallucination-mds.ingest.md) -- sibling ingest from the same workshop batch, but its failure (passing off unshared insights, non-abstention) shares no axis with persona-conditioned evidence evaluation.
- [Structured-prompt gains do not establish distribution selection](../../../../theory/structured-prompt-gains-do-not-establish-distribution-selection.md) -- about attributing prompt gains to a mechanism; this source reports no gains, so it does not test the claim.
- Agent-memory-system reviews matching "persona" (e.g. `continuity.md`, `synapptic.md`) -- use "persona" for stored user profiles, not prompt-assigned identities.

## Index Membership

- [LLM reliability tag head](../../../../tags/llm-reliability-README.md) -- the source carries the tag; its Sources section currently lists only Ma et al. A future maintainer could add this as evidence that persona prompts are a correlated-error source under the Error Correction Theory heading.

## Synthesis Opportunities

The ingest's own Extractable Value 5 already names the candidate: this source plus [Peters and Chin-Yee](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) give two designs where an accuracy exhortation worsened a measured bias and CoT did nothing, while [the validity–plausibility steering study](../../../../sources/llm-validity-plausibility-conflation-content-effects.ingest.md) reduces a content effect at the representation level. Together they suggest "prompt-level exhortation is not a debiasing control; the effective lever sits below the prompt". Mechanism is unexplained in all three, so under the quality bar this belongs in `kb/log.md`, not a note yet.

## Maintenance Observations

- [Ma et al. ingest](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) links `error-correction...` with the label "enables" for personality templates as calibrated decorrelation. This source contradicts the unqualified version of that suggestion on stance-bearing content. ("enables" is also not in the sources→theory authorised label set; likely a legacy label.)

## Flags

- Tension: Ma et al. treat personality variants as semantics-preserving; this source shows identity personas are not on stance-bearing items. Not resolved here; scope differs (code tasks vs political evidence; style personas vs identity personas).
- The persona effect may be role compliance rather than distorted inference (the ingest's central confound). Every reverse edge's context phrase should carry it.
