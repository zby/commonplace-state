---
description: "Post-acceptance connection discovery for batch-invariant inference: qualifying sampling-only claims and locating independently useful inbound citations."
type: types/connect-report.md
source: kb/sources/defeating-nondeterminism-in-llm-inference.ingest.md
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: Defeating Nondeterminism in LLM Inference

**Source:** [Ingest: Defeating Nondeterminism in LLM Inference](../../../../sources/defeating-nondeterminism-in-llm-inference.ingest.md)

Discovery-only output of `cp-skill-connect`, produced by `gpt-6-astra` for post-acceptance ingest connection discovery. No proposed edge has been authored. The accepted ingest, current repository documents, source and theory collection contracts, and ingest/note/connect-report types supplied the judgment boundary. No external search, snapshot inspection, implementation execution, or agents were used.

## Discovery Trace

**Setup and scope:** Read the source in full and confirmed its collection contract before discovery. Sources permits theory, reference, historical agent-memory systems, agentic systems, tags, other sources, and already-known external targets. Instructions and work were excluded. Read the reports collection contract for the sole output. The source has no tags, so there was no source-tag listing or complete-head shortcut.

**Indexes and complete title surfaces:** Read `README.md` in each of `kb/theory/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/tags/`, and `kb/sources/`. Generated the complete fresh title surface for each with `rg -N --no-heading -m1 '^# ' kb/$d/ --glob '*.md'`; recovered the truncated combined output in successive reads. Titles selected the execution-indeterminism cluster, the debugging note, commitment versus derivation, Evans, and Qwenputer. The historical memory landing explicitly marks its corpus frozen; the current systems landing concerns harnesses rather than inference kernels.

**Description and body searches, applied separately to all six destinations:**

- `rg '^description:' kb/$d --glob '*.md' | rg -i 'determinis|repeatab|reproduc|sampling|numerical|variance|reliab'`
- `rg -n -i 'temperature.zero|batch.invarian|floating.point|sampler.trainer' kb/$d --glob '*.md'`
- `rg -l -i 'repeatability|run.to.run|numerical|greedy decoding|deterministic inference' kb/$d --glob '*.md'`

These were literal lexical searches, not scored semantic retrieval. Per-destination evaluations:

- **Theory:** Descriptions foregrounded execution indeterminism and the underspecification cluster. The first body query found unconditional temperature-zero language in execution indeterminism, the agentic-instructions framing, and commitment versus derivation. Full reads retained the first as an already-authored outbound relation with an independently warranted return citation; retained the latter two as inbound-only qualification candidates. The adjacent query and one-hop following selected debugging for a concrete fixed-conditions clarification. Read the three-way diagnosis synthesis and interpreter-failure note; did not fan out source citations across every sibling. The source tests numerical repeatability, not semantic conformance.
- **Reference:** Description hits concerned deterministic validation, packaging, and review execution. The focused body query returned no hits. The adjacent query surfaced evaluation and evidence-management proposals, but none named a numerical-repeatability requirement that this source would settle. No reference edge retained: generic reproducibility advice is insufficient for a shipped-system connection.
- **Agent-memory-systems:** Description hits included Echel, Sparks, AI Research OS Workshop, and DocMason's deterministic plumbing. The focused numerical query returned no hits; adjacent hits were review-framework design and Swamp. None supplied a shared inference-kernel mechanism or a tested memory implication. No edge retained; did not treat deterministic file processing as deterministic LLM inference.
- **Agentic-systems:** Focused hits were archived results recording temperature-zero API requests (Reflexion, Instinctual Memory, fragility-grid) and floating-point embeddings (Mem0). Instinctual Memory's matching passage already says those settings do not prove determinism. These are source-bound implementation descriptions, not claims that this numerical intervention was used or tested there. Other adjacent hits concerned general runtime/research repeatability. No edge retained, and no inference result was imported into a historical system characterization.
- **Tags:** Read the LLM reliability head after the description hit and followed its taxonomy links. Its focus fits the source's contribution, but the sources contract supplies no formal source-to-tags label, and the tags contract excludes sources from participating membership. No index membership or routine tag-head edge proposed. The head already routes through the directly affected execution note.
- **Sources:** Evans was retained after a full read as a comparison between two mechanisms reported to improve consistency: freezing categories versus stabilizing numerical reduction order. Qwenputer was fully read after its deterministic-CPU title surfaced; rejected because compiled execution of assigned instructions is not repeatability of ordinary learned generation. Reliability surveys and agent-memory variance reports were screened at description resolution, not retained as generic reliability companions. The ingest type favors compact theory-facing placement rather than a source-comparison map, so the Evans comparison is optional, not a recommendation to expand the ingest into a catalogue.
- **External:** The original Thinking Machines URL is already the source identity. No new provenance edge is needed. External prospecting was skipped; no browsing was performed.

**One-hop following:** From execution indeterminism, followed agentic-instructions framing, interpreter failure, three-way diagnosis, and the reliability head. From three-way diagnosis, followed debugging. Also read the source's existing theory-builder definition and fixed-decomposition note. Their outbound uses remain useful classification/context links; neither needs to cite this source back merely because it is applied here. The RL experiment does not test the definition or demonstrate a decomposition omission.

**Direction check:** Read `kb/theory/COLLECTION.md` fully before accepting inbound candidates. Every theory-to-source proposal below uses authorized `evidenced-by` as qualifying or bounding evidence, not corroboration. The proposed sentence must live in the linking note's body. Each inbound link solves a local reader problem independent of the ingest's outgoing links.

## Connections Found

- [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) — **is-evidence-for**: the reported fixed-model, fixed-prompt, greedy-decoding intervention identifies batch-dependent reduction order as removable variation beyond stochastic token selection. It materially qualifies the note's temperature-zero guarantee and sampling-only remedy. **Already present in the ingest:** retain its qualifying role rather than add a duplicate footer or claim universal determinism.
- [Evans: AI Components for a Deterministic System](../../../../sources/eric-evans-ai-components-deterministic-system.ingest.md) — **compares-with**: compare what each consistency intervention holds fixed. Evans freezes a classification scheme; Thinking Machines fixes numerical reductions while leaving the model and prompt unchanged. This prevents readers from treating semantic narrowing and numerical repeatability as interchangeable repairs. Both ingests explicitly limit consistency as evidence of correctness. Optional concise comparison only; no return edge is recommended without a source-side editorial need.

## Bidirectional Candidates

- [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) → [source (snapshot required)](../../../../sources/defeating-nondeterminism-in-llm-inference.ingest.md) — **evidenced-by**: the note's reader needs evidence for why temperature zero alone is not a repeatability guarantee and why changing the numerical implementation can remove variation without replacing the LLM. Author the citation beside a revised body explanation of stochastic sampling versus batch-dependent computation. This is an independent corrective use, not a mirrored backlink. The reported trial bounds the unconditional claim; it does not establish determinism for every deployment or correctness of the repeated answer.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → [source (snapshot required)](../../../../sources/defeating-nondeterminism-in-llm-inference.ingest.md) — **evidenced-by**: qualify the body's claim that at temperature zero “you just get the same one every time.” Readers deciding what temperature changes need the missing serving condition, while the note's distinction between repeatability and resolving specification ambiguity remains intact. Cite the bounded kernel intervention, not a purported test of natural-language semantics.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) → [source (snapshot required)](../../../../sources/defeating-nondeterminism-in-llm-inference.ingest.md) — **evidenced-by**: bound the deterministic-producer example's unconditional temperature-zero sentence. Readers assessing recomputation must distinguish fixing the decoder setting from fixing the numerical computation. The central argument survives: even an actually repeatable producer can add content the source does not determine. The citation is for that example's repeatability condition, not evidence for the whole ground-truth thesis.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) → [source (snapshot required)](../../../../sources/defeating-nondeterminism-in-llm-inference.ingest.md) — **evidenced-by**: extend check 3's fixed-conditions explanation with a concrete failure to hold computation fixed despite unchanged model, prompt, and sampling settings. A debugger gains a new inspection target—batch-dependent reductions—before attributing variation to decoding randomness or rewriting the prompt. This is a bounded transfer from inference serving, not a tested debugging-workflow improvement.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Qwenputer](../../../../sources/qwenputer.ingest.md) — deterministic execution of a compiled CPU inside a checkpoint concerns assigned instruction semantics and exact state operations. It does not investigate numerical batch invariance of ordinary LLM generation; sharing the word “deterministic” is not enough.
- [Theory builder](../../../../theory/definitions/theory-builder.md) — the ingest already applies the definition. An inbound citation would merely catalogue another weight-update learner without testing or changing the definition's boundary.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — already used as a limitation in the ingest. Numerical alignment does not identify a missing distinction, action, or mapping outside an effective update space; no independent evidential return edge follows.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — repeatability trials do not test instruction conformance, so this is not direct evidence for its central claim.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) — affected conceptually, but it already routes to the execution-indeterminism note and distinguishes runtime nondeterminism in its empirical discussion. Prefer qualifying the mechanism owner instead of adding the same source at every taxonomy level.

## Index Membership

None.

## Synthesis Opportunities

None. The existing three-way diagnosis already separates variation from specification adequacy and interpreter conformance. Refining the mechanism of variation does not require a competing synthesis note.

## Maintenance Observations

None.

## Flags

- **Grounding prerequisite:** the source currently retains no verbatim quotes. Proposed evidential inbound citations explicitly use `(snapshot required)`. Before durable adoption, either retain the minimum supporting passages through the authorized grounding workflow or keep that marker and verify the exact name-paired snapshot. This discovery pass did neither and does not certify source claims independently.
- **Scope of qualification:** one reported prompt/model trial and an implementation-specific intervention do not establish cross-hardware, cross-version, or whole-agent determinism. Avoid replacing “all deployed systems vary” with the opposite universal.
- **No changes authorized here:** candidates require later authoring and validation under each linking artifact's contract. No library document, index, source, or quote pool was changed.
