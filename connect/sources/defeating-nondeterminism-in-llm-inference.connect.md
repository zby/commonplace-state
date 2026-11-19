---
description: "Pre-ingest discovery for batch-invariant LLM inference: numerical reproducibility, sampling attribution, and temperature-zero claims needing qualification"
type: types/connect-report.md
source: kb/sources/.snapshots/defeating-nondeterminism-in-llm-inference.md
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: Defeating Nondeterminism in LLM Inference

**Source:** [Defeating Nondeterminism in LLM Inference](../../../../sources/.snapshots/defeating-nondeterminism-in-llm-inference.md)

Purpose: pre-ingest discovery. Produced with `cp-skill-connect` by `gpt-6-astra`. All edges below are candidates, not authored library state. The snapshot is immutable; proposed outbound edges belong to a future matching ingest. No ingest was drafted.

The complete retained article was inspected through an in-memory Python `HTMLParser` text rendering, including code, figure captions, experiments, footnotes and citation. No snapshot bytes were changed. The article distinguishes deterministic kernels on fixed inputs from per-request invariance under changing batch sizes and sequence partitioning. Its proposed repair fixes reduction order across RMSNorm, matrix multiplication and attention. It reports 80 distinct temperature-zero completions in 1,000 trials before intervention and identical completions in 1,000 trials with batch-invariant kernels. It also reports performance costs and sampler–trainer numerical alignment in an RL experiment. These are practitioner-reported results, not independently reproduced here.

## Discovery Trace

**Scope and authorization:** Read `kb/sources/COLLECTION.md`, `kb/reports/COLLECTION.md`, and `kb/types/connect-report.md` before discovery. Prospected theory, reference, agent-memory-systems, agentic-systems, tags and sources. Excluded work and instructions. Read the theory contract for reverse-edge authorization and the agentic-systems contract when evaluating the archived fragility-grid account. External authorization was used only for the source URL already supplied in capture metadata; no external searches or agents were used.

**Curated indexes:** Read each of the six destination `README.md` files and followed the tags index to `kb/tags/llm-reliability-README.md`. This head routed to the execution-indeterminism note, three-way diagnosis and debugging checks. The source has no tags, so no source-tag membership query or completeness shortcut applied.

**Complete title surface:** Generated `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each of the six destinations. Recovered the truncated output in chunks. Theory titles identified the direct sampling claim and debugging cluster; sources identified Evans and Prompt Stability; system titles supplied no batch-invariant inference implementation account.

**Description and body queries:** For every destination, ran:

- `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'determinis|reproducib|variance|sampling|reliability|numerical'`
- `rg -n -i 'batch.invarian|floating.point|temperature.?0|temperature zero|greedy decod' kb/<destination>/ --glob '*.md'`
- `rg -l -i 'run.to.run|reproducib|numerical|batch.size' kb/<destination>/ --glob '*.md'`

Per-destination evaluations:

- **Theory:** Read the execution-indeterminism, underspecified-instructions, commitment-versus-derivation, debugging and three-way-diagnosis notes in full. Kept the execution claim as a direct evidential qualification; kept debugging as the practical diagnostic destination. The other temperature-zero assertions need reverse citations or revision, not a broad outbound link spray. The three-way diagnosis remains useful; numerical variation changes its causal attribution, not its intent/specification/output distinctions.
- **Reference:** Description hits concerned structural validation, context assembly and review machinery. The focused numerical query returned no hits. The adjacent query found provenance and reproducibility discussions, but no concrete dependence on batch-invariant model inference. Rejected generic deterministic-validation adjacency.
- **Agent-memory-systems:** Description hits such as DocMason and Sparks concerned deterministic retrieval or plumbing. The focused numerical query returned no hits. Reproducibility matches did not supply a shared numerical inference mechanism. No candidate retained; a GPU-kernel article does not establish a memory-system claim.
- **Agentic-systems:** The focused query found the archived fragility-grid account's explicit warning that greedy decoding and seeds do not establish reproduction. Read that account fully. Its comparison is useful but secondary: the article supplies one additional numerical mechanism, not evidence that this particular system experienced it. Archived raw reports containing temperature-zero settings alone were not promoted to candidates.
- **Tags:** The title and description surfaces routed to LLM reliability. Read its inclusion condition and taxonomy fully. It is substantively relevant, but the sources contract lists tags as a search destination without authorizing any source-to-tags relationship label. No tag edge invented.
- **Sources:** Read Evans and Prompt Stability in full. Retained Evans as a comparison between semantic stabilization and numerical reproducibility. Retained Prompt Stability as a comparison of what variation experiments identify. General reliability, RL and invariance title hits were not retained merely because they share those words.

**Link following:** Followed the execution-indeterminism note to its underspecified-instructions and three-way-diagnosis companions, then to debugging. Followed its named Prompt Stability source to the tracked ingest. That ingest's claims of clean separation conflict with the more qualified account in the three-way-diagnosis note. The Evans ingest also links the underspecified-instructions note, providing a second route into the same cluster. These links make the numerical-versus-semantic distinction useful to a KB operator rather than merely a GPU engineering topic.

No search scores were available; candidate judgments are qualitative.

## Connections Found

- [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **is-evidence-for**: the article materially qualifies this claim by demonstrating reported output variation with greedy sampling and explaining a batch-dependent reduction mechanism. It supports the note's batching caveat, but challenges its attribution to sampling alone and its unconditional temperature-zero repetition language. This is qualifying evidence, not blanket corroboration.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — **is-evidence-for**: the fixed-prompt experiment supplies a concrete reason to include serving conditions in repeated-run diagnosis. A fixed prompt, model and sampler do not hold batch-dependent numerical execution fixed. This bounds what an operator may attribute to sampling; it does not test the note's whole diagnostic procedure.
- [AI Components for a Deterministic System](../../../../sources/eric-evans-ai-components-deterministic-system.ingest.md) — **compares-with**: both seek repeatable LLM-backed behavior, but Evans freezes a category scheme while this article stabilizes numerical reductions. Following the comparison prevents treating semantic consistency and bitwise inference reproducibility as the same intervention or as correctness guarantees.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — **compares-with**: compare attribution of output variation. Prompt Stability varies framing and repeats samples at temperature 0.2; this article isolates a serving-level mechanism visible even at temperature zero. The comparison shows why fixed decoding settings alone do not isolate sampler noise. It does not establish that numerical variation caused any particular Prompt Stability result.
- [Original article](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) — **derived-from**: the future ingest's source account would be worked out from this original article, already identified by the snapshot metadata.

## Bidirectional Candidates

None. Useful theory-to-source directions are specified below rather than duplicated here.

## Reverse-edge Candidates

These are future theory-to-source **evidenced-by** edges authorized by the theory contract. They must target a tracked ingest after one exists, never the local snapshot. The intended companion basename is `defeating-nondeterminism-in-llm-inference.ingest.md`; it is not asserted to exist or linked as an existing artifact.

- [Execution indeterminism](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) → future ingest — **evidenced-by**: qualify the assertion that temperature zero yields the same interpretation every time and replace the unspecified batching caveat with a specific mechanism. The article's finite trial does not justify a universal determinism claim across hardware, software versions or all serving arrangements.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → future ingest — **evidenced-by**: bound the temperature-zero assertions in “Two Distinct Phenomena” and “Narrowing the Interpretation Space.” Deterministic sampling is not sufficient for repeatable inference; this correction leaves the semantic-underspecification argument intact.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) → future ingest — **evidenced-by**: qualify the sentence “An LLM at temperature zero returns the same output every time.” The commitment argument can instead use a conditional deterministic-producer example. Numerical repeatability is neither necessary nor sufficient for source entailment.

## Off-authorisation Candidates

- [LLM reliability](../../../../tags/llm-reliability-README.md) — the article gives readers a concrete mechanism beneath this head's execution-indeterminism branch. Sources may prospect tags, but the sources label table authorizes no source-to-tags edge. Reject the formal edge for this run; if direct source-to-head navigation is wanted later, extend the sources contract explicitly rather than inventing a label.

## Raw Text Candidates

None.

## Rejected Candidates

- [fragility-grid collection and resume subsystem](../../../../agentic-systems/reviews-archive/fragility-grid.md) — an intelligible comparison on reproducibility controls, but not retained as an outbound edge: the account is historical, already qualifies its seeds and greedy decoding, and the article supplies no observation of batch sensitivity in that exact system. The general debugging connection serves the reader without implying a new system finding.
- [Deterministic validation should be a script](../../../../theory/deterministic-validation-should-be-a-script.md) — keyword overlap only. Structural checking in Python and invariant GPU reduction orders solve different problems; this article does not test the validator-design claim.

## Index Membership

None. No immutable snapshot should be added to durable navigation. A future ingest could carry the existing `llm-reliability` topic tag because the article diagnoses and repairs output variation; this is not an assignment made by this report. Sources are outside the participating collections used for tag-head member completeness.

## Synthesis Opportunities

None. The existing three-way-diagnosis and debugging notes can accommodate the numerical mechanism without a new synthesis note.

## Maintenance Observations

- The [Prompt Stability ingest](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) calls its experiment a clean separation of underspecification and indeterminism, while [three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) explains that its aggregate does not isolate within-prompt sampling dispersion and that meaning-preserving variants do not test underspecification. The ingest also says the execution-indeterminism note has no sources section, but that note now has one. These are existing interpretation and stale-state discrepancies, not findings about the new article. No repair performed.

## Flags

- **Pre-ingest dependency:** reverse source citations cannot be authored until a tracked ingest with appropriate grounding exists. This does not block discovery-report completion.
- **Claim tension:** deterministic kernels for fixed complete inputs can coexist with nondeterministic per-request results when external load changes batching. Do not flatten this into either “GPUs are inherently random” or “temperature zero guarantees determinism.”
- **Scope:** the article's reported kernels, completion trial, performance measurements and RL alignment do not establish reproducibility across all hardware/software versions or semantic correctness. Parallelism-related reductions are explicitly outside its detailed treatment; fixed-size attention splitting also required internal changes not included in the described code release.
- **No split flag:** retained connections fall within one output-reliability cluster, not three topic areas. The RL result alone does not warrant new KB links here.
