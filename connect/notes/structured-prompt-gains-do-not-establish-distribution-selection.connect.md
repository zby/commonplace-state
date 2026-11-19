---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/structured-prompt-gains-do-not-establish-distribution-selection.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Structured-prompt gains do not establish training-distribution selection

**Source:** [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md)

## Discovery Trace

**Authorisation and breadth:**

- Read `kb/notes/COLLECTION.md`. It authorises outbound prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; excludes `work`; and authorises already-known `external` targets without making the open web a prospecting surface. No external target was supplied, so external prospecting was skipped.
- The rewritten source makes a causal-identification claim about structured-prompt experiments. That justified a broad notes-and-sources pass, narrower checks for shipped type/reference surfaces and external-system cases, and a first-class reverse-edge pass over instructions because the notes contract says the usual notes/instructions direction is inverse.

**Curated heads and tag routing:**

- Read `kb/notes/README.md` and the matching [Type system](../../../../tags/type-system-README.md) tag head. The tag head does not declare `complete: true`, so ran `rg -l '^tags:.*\btype-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. This recovered the source's already-authored failure-mode, reviewability, process/output, Toulmin, and type-role neighborhood; none is a new outbound candidate.
- Read `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No matching `type-system-README.md` exists outside notes. Ran the same by-tag description query over the other authorised destinations; only `kb/reference/validation-contract.md` and `kb/reference/proposals/generalized-validation-invalidation-and-imperative-extension.md` matched, and both concern deterministic type validation rather than causal attribution for prompt effects.
- Read [Evaluation](../../../../tags/evaluation-README.md), [Learning theory](../../../../tags/learning-theory-README.md), and [Document system](../../../../tags/document-system-README.md) after the full scans exposed them as possible routing surfaces. Evaluation is the only additional head whose reader need matches the rewritten note.

**Full title and description surfaces:**

- Generated every authorised local destination's complete title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` and `rg '^description:' kb/types/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/instructions/ --glob '*.md'`, then used `rg -n -i '^description:.*(causal|mechanism|experiment|contrast|ablation|prompt|structure|reasoning|training|distribution|identif|rival|confound|accuracy|format|compliance|task decomposition|token budget)' ... --glob '*.md'` to tighten candidate evaluation. Notes surfaced the contrast-identification, prompt-variation, claim-granular-warrant, mechanism-transfer, and outcome/process clusters. Sources surfaced RECV, Natural-Language Agent Harnesses, prompt-stability, rationale-faithfulness, strategy-discourse, and reasoning-cost cases. Types, reference, agent-memory systems, and agentic systems supplied no target with a distinct reader need.

**Body searches:**

- Ran `rg -n -i 'training[- ]distribution|distribution[- ]selection|structured[- ]prompt|heading-only|process-only|format(ting)? compliance|task decomposition|extra (generated )?tokens|token budget|causal identification|experimental contrast|treatment grain|rule out (the )?rival' kb/notes/ --glob '*.md'`. Kept [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): its treatment-grain rule directly explains why a bundle-level prompt gain cannot identify distribution selection. The query also exposed stale pre-rewrite assertions in the source's inbound neighborhood.
- Ran corresponding `training-distribution|distribution-selection|structured-prompt|format-compliance|task-decomposition|causal-identification|experimental-contrast|prompt-ablation` searches separately over `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. Type and reference hits described structural surfaces; agent-memory hits described prompt injection or planning; agentic-system searches returned no hits. None passed the articulation test.
- Ran the same focused query over `kb/sources/`. Kept [RECV](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md), whose prompt arms bundle persona, examples, step-by-step wording, explanation requirements, and output shape, and [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md), whose module ablations supply evaluator alignment as a live alternative account of where explicit structure helps. Rejected prompt-stability, rationale-faithfulness, strategy-discourse, and reasoning-cost hits because they do not isolate the source's disputed mechanism or add a comparably direct rival.
- Ran `rg -n -i 'structure-activates-higher-quality-training-distributions|training[- ]distribution|distribution[- ]selection|structured[- ]prompt|heading-only|process-only|format(ting)? compliance|task decomposition|causal identification|experimental contrast|prompt ablation' kb/instructions/ --glob '*.md'`. [Analyse an External System's Epistemic Architecture](../../../../instructions/analyse-external-system-epistemic-architecture.md) frontloads the general contrast-grain rule but does not depend on this narrower prompt-mechanism application, so no exceptional `rests-on` reverse edge is warranted.

**Existing-link and backlink scan:**

- Ran `rg -n 'structure-activates-higher-quality-training-distributions' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'`. The source's seven current outbound links all resolve. RECV, Agentic Code Reasoning, and the content-effects ingest already link inbound; the epiplexity and Natural-Language Agent Harnesses ingests do not.
- Existing inbound links from the type-system cluster, `information-value-is-observer-relative`, `llm-learning-phases-fall-between-human-learning-modes`, `error-correction-works-above-chance-oracles-with-decorrelated-checks`, and several ingests were not repeated as reverse-edge candidates. Their outdated context phrases are recorded under Maintenance Observations instead.

**Link following:**

- Followed all current source links. The epiplexity note and ingest preserve the analogy/transfer caveat; the failure-mode and reviewability notes supply independent design rationales; the process/output note names two rival levers; and the Agentic Code Reasoning and content-effects ingests preserve the measured gains and limits. These links already cover the source's immediate evidential neighborhood.
- Followed [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) into prompt variation, fixed-decomposition, and claim-granular-warrant notes. The first-hop neighborhood confirms that the contrast-identification note is the narrowest missing general premise; the broader warrant notes remain reachable without another direct edge.
- Followed RECV into the contrast-identification and prompt-variation notes. Its bundled prompt arms and reversing cell effects make it a direct worked case rather than a keyword match. Followed Natural-Language Agent Harnesses into the process/output and specification-separation neighborhood; its distinct contribution is an empirical alternative mechanism, not another generic structure example.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **grounds**: its treatment-grain rule supplies the general causal premise for the source's central conclusion: when format, process, and compute move together, an observed prompt gain cannot identify distribution selection as the component cause.
- [Ingest: Assessing LLM Reasoning in Evidence-Based Claim Verification](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) -- **evidenced-by**: its prompt arms bundle persona, demonstrations, step-by-step wording, rationale requirements, and output shape, while effects reverse across benchmark cells; this is a concrete case where performance differences cannot identify one structural mechanism.
- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- **evidenced-by**: its module ablations report that explicit structure helps selectively when it aligns intermediate behavior with evaluator acceptance criteria, furnishing a bounded empirical rival to training-distribution selection rather than treating structure count as the cause.

## Bidirectional Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -> source -- **extends**: the source develops the general contrast-grain rule into a concrete structured-prompt application and specifies the heading-only, process-only, combined, and unstructured arms needed to test the disputed mechanism.
- [Ingest: From Entropy to Epiplexity](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) -> source -- **is-evidence-for**: the ingest's explicit warning that dataset-learning measurements may not transfer to one-shot prompt consumption should expose this concrete application of that boundary to readers arriving from the source analysis.

## Reverse-edge Candidates

- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -> source -- **is-evidence-for**: the ingest's selective, evaluator-alignment-sensitive ablation result materially bears on the source's claim that a structure-related gain does not by itself identify training-distribution selection.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Epiplexity by example: what entropy and complexity miss](../../../../notes/epiplexity-by-example-what-entropy-and-complexity-miss.md) -- already linked from the source and correctly bounded there as an arrangement-sensitive analogy rather than causal identification.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- already linked from the source as the distinction that exposes two rivals; no duplicate candidate is needed.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- adjacent methodological distinction, but the more exact contrast-identification note is the load-bearing premise and already reaches this note in one hop.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- supports the broad non-distribution rule for evidence, but is less specific than the contrast-identification candidate and remains reachable through it.
- [Ingest: Language Models Don't Always Say What They Think](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) -- shows that a rationale may be unfaithful, but the source disputes causal attribution for an accuracy gain rather than rationale faithfulness.
- [Ingest: Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- demonstrates framing sensitivity without identifying its mechanism, but adds no matched structured-prompt contrast beyond the source's current cases.
- [Ingest: Researchers Asked LLMs for Strategic Advice](../../../../sources/researchers-asked-llms-strategic-advice-trendslop.ingest.md) -- its discourse-prior interpretation is second-hand and itself does not distinguish training-data attribution from option order, tuning, or assistant-persona effects.
- [Ingest: Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) -- separates some recurring reasoning cost from action-loop cost, but tests injected distilled skills rather than matched formatting and process controls for structured prompts.
- [Analyse an External System's Epistemic Architecture](../../../../instructions/analyse-external-system-epistemic-architecture.md) -- applies the general causal-contrast rule, but its procedure does not depend on this narrower structured-prompt application; the instructions collection's exceptional-link posture therefore rules out a speculative `rests-on` edge.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) -- the rewritten note now contributes a concrete prompt-study identification rule and a matched-control design alongside the index's prompt-ablation and systematic-variation methods.

## Synthesis Opportunities

None. The higher-order claim that structured-prompt studies must separate format, process, information, and compute is already stated directly in the source rather than merely implied across candidates.

## Maintenance Observations

- Resolved during the required reframe follow-up: the source moved to `structured-prompt-gains-do-not-establish-distribution-selection.md`, the old path now redirects, and the authored inbound neighborhood was reconciled to the causal-identification claim.

## Flags

None
