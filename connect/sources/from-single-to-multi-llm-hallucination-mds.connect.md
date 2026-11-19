---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/from-single-to-multi-llm-hallucination-mds.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization

**Source:** [From Single to Multi: How LLMs Hallucinate in Multi-Document Summarization](../../../../sources/.snapshots/from-single-to-multi-llm-hallucination-mds.md)

The source is an immutable snapshot. No tracked ingest exists yet (`kb/sources/from-single-to-multi-llm-hallucination-mds.ingest.md` is absent). Every outbound candidate below is for that future ingest's `## Connections Found`. Reverse-edge candidates must target the ingest, never the snapshot.

Source content read for this report: abstract, introduction, sections 2-6 (problem setup, SummHay-derived benchmarks, two-way LLM-judge metric, results on document count, the shared-insight setting, abstention on non-existent subtopics, input recency and output-position effects, error taxonomy, post-hoc mitigation). Appendices were scanned by heading only.

Main claims used for prospecting:
- Over 5 LLMs, the hallucination rate (macro-FDR) averages at least 20% (news) and 52% (conversation), up to 75%. It changes only about ±5% from 2 to 10 documents (Gemini Flash under 10%), while recall falls as document count rises.
- An instruction to keep only insights shared across documents shortens summaries but raises hallucination (news +10.47%, conv +4.20%).
- Given a non-existent subtopic and told to answer "No insights found", models abstain 20.65%-71.08% of the time. Abstention falls as document count rises. GPT-3.5 and GPT-4o still summarize 79.35% and 44% of the time.
- Hallucinated insights lean slightly toward later input documents (3 of 5 models). Accuracy falls with bullet position, apart from generic openers and "takeaway" closers.
- In 700+ human-annotated insights, most errors are *pedantic* (correct but uninformative) or *instruction inconsistency* (off-topic, redundant, not shared). *Context inconsistency* (overgeneralization, oversimplification) is 9%-37%; *fabrication* is 0%-9%.
- Post-hoc filters (top-k, redundancy, paraphrase and unrelated-subtopic removal) move F1 by about ±3%. They trade up to 7 points of hallucination for up to 6 points of recall. The authors suggest hierarchical per-document summarization.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference (`see-also` only), sources, agent-memory-systems, agentic-systems, tags, external. Excluded: `kb/work/` and `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `abstracted-from`/`rests-on` (theory), `defined-in` (theory/definitions), `see-also` (sparingly), `derived-from` (external). External prospecting was skipped. The only known external target is the source URL itself (`https://aclanthology.org/2025.findings-naacl.293/`), which the ingest gets as `derived-from` by construction.

**Curated heads read:**
- `kb/tags/README.md` listing, `kb/tags/llm-reliability-README.md` (taxonomy: underspecification / interpreter failure / indeterminism), `kb/tags/context-engineering-README.md` (core claims, degradation), `kb/tags/evaluation-README.md` (oracles and judges). `kb/tags/failure-modes-README.md` description only (it includes over-generalization). The snapshot has no `tags:`, so no tag-driven rg pass was needed.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`, filtered with `grep -iE 'context|summar|distill|degrad|attention|position|halluc|confiden|abstain|verif|oracle|deviation|underspecif|compress|lossy|interference|synthes|instruction|faithful|ground'`. About 85 titles came back. Flagged: soft-degradation, out-of-spec interpreter failure, decomposition heuristics, reverse compression, generation confidence, synthesis-is-not-error-correction, automated-synthesis-missing-oracles, context contamination, llm-context-composed-without-scoping, two-context-boundaries, holistic rewrite, claim-routed reading.

**Description listing:**
- `rg -m1 '^description:'` on the 15 flagged theory/source files, then on `peters-chin-yee-llm-generalization-bias.ingest.md`, `gsm-dc-...ingest.md`, `longmemeval-...ingest.md`, `out-of-spec-...md`, `abstract-an-experience-...md`, `decomposition-heuristics-...md`, `two-context-boundaries-...md`, `information-value-is-observer-relative.md`, `claim-routed-reading-...md`, `evolving-understanding-...md`.

**Body search** (`rg -il "<q>" kb/theory kb/reference kb/sources kb/agentic-systems kb/agent-memory-systems kb/tags --glob '*.md'`, snapshots excluded):
- `hallucinat`: about 40 files, mostly agent-memory reviews and unrelated ingests. Kept: `out-of-spec-output-...` (line 16 uses "Summarise this document → LLM includes facts not in the document" as its hallucination example) and `paulsen-...mecw.ingest.md`.
- `fabricat`: memory reviews and AAS archives. Nothing on summarization.
- `abstain|abstention`: mostly the factory/decomposition sense of "abstain". Kept: `longmemeval-...ingest.md` (abstention is one of its five abilities).
- `lost in the middle|recency bias|position bias|positional`: kept `soft-degradation-...` (cites Liu et al. primacy/recency) and `position-bias.ingest.md`. The rest use "position" in an unrelated sense.
- `summariz`: many memory reviews that describe summarization features. No claim-level match.
- `multi-document`: `paulsen-...mecw.ingest.md`, `agent-memory-systems/reviews/o-o.md` (incidental).
- `LLM-as-a-judge|LLM-as-judge|llm judge`: evaluation-tag notes and `calibrating-semantic-gates-against-labelled-fixtures.md` (reference proposal).
- `generic|pedantic`: no claim-level match beyond `reverse-compression-...`, which the title listing had already found.
- `sycophan`: `gentle-coding-research.ingest.md` only (incidental).
- `corroborat`, `refus`, `overgenerali`, `instruction.follow`, `distractor`, `generalization bias`, `top-k|truncat`, `hierarchical summar|map-reduce|summarize each` (theory, sources, tags). Kept: `peters-chin-yee-llm-generalization-bias.ingest.md` (overgeneralization in summaries), `gsm-dc-...ingest.md` (distractor volume), `llm-webagents-...ingest.md`, `decomposition-heuristics-...` (lines 30, 43, 55, 57 on summarization and selection vs joint reasoning).

**Link following:**
- `soft-degradation-...` body and footer: its volume and interference sections cite GSM-DC, web agents, ConvexBench, J-space and Paulsen. Those are the same five tracked sources this paper would sit beside. They also confirm that `context-contamination-...` and `llm-context-is-composed-without-scoping` are the neighbouring mechanism notes.
- `peters-chin-yee-...ingest.md` Connections: links `abstract-an-experience-only-when-you-can-state-the-boundary.md` as the over-generalization mechanism. That made the abstract-an-experience note a candidate here. It was rejected (see below).
- `paulsen-...ingest.md` Connections: links context-efficiency, bounded-context-orchestration, decomposition-heuristics, information-value, two-context-boundaries. These were checked as candidates here. Only decomposition-heuristics has a specific articulation for this source.
- `out-of-spec-...` line 16 checked in context: the worked failure catalogue uses summarization hallucination as an archetypal interpreter failure.

**Per-destination breadth:**
- theory: full standard pass (above).
- sources: full standard pass (above).
- tags: heads read. Tag fit is recorded under Index Membership.
- reference: only `see-also` is authorised. One candidate (the judge-calibration proposal) was evaluated and rejected.
- agent-memory-systems / agentic-systems: `summariz|hallucinat|fabricat` hits are system descriptions of summarization features or incidental mentions. No reviewed system makes a claim about multi-document summary faithfulness that this benchmark tests, so no candidate passed the articulation test. Destination skipped after the hit scan.

## Connections Found

- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **is-evidence-for**: 2-10 document inputs fit well inside the provider windows. Even so, recall falls and abstention on absent subtopics falls as documents are added, while output stays fluent. This is the invisible soft bound in a summarization task shape. It also bounds the note: the hallucination *fraction* barely moves with volume, so the degradation shows up as lost coverage and lost abstention, not as rising fabrication.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- **is-evidence-for**: the note's archetypal hallucination ("summarise this document → facts not in the document") gets a measured breakdown here. In MDS most out-of-spec insights violate explicit prompt conditions (subtopic, conciseness, shared-only) or are uninformative. Outright fabrication is 0%-9%. Instruction violations under a sufficient spec are the interpreter-failure case, and the weak post-hoc filters show the detection-and-correction repair surface at work.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) -- **is-evidence-for**: the "subtopic+trustworthy" setting asks one call to do selection (which insights are on-topic) and joint reasoning (which recur across documents) together. That call hallucinates more than the single-condition setting. The authors' proposed fix is per-document summarization before merging. This is the note's "separate selection from joint reasoning" and hierarchical-merge fallback, offered from outside the KB. It is not tested in the paper, so it is weak support.
- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) -- **is-evidence-for**: the human-coded "pedantic" class (correct insights that paraphrase the topic, opening remarks, takeaway closers) is the most frequent error type for several models. It is a coded external instance of output that adds length but no extractable information, comparable to the SuperARC instance the note already uses.
- [Generalization Bias in LLM Summarization of Scientific Research](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) -- **compares-with** (axis: scope distortion in LLM summaries): this paper's "context inconsistency" class includes overgeneralization ("individual opinions turned into broader claims"), the move Peters and Chin-Yee code and measure in single-document science summaries. Comparing them shows how far scope broadening goes from single-document science abstracts to multi-document news and dialogue. Here it is a minority error (9%-37%), dominated by instruction violations.
- [Paulsen: maximum effective context window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- **compares-with** (axis: how error rates scale with input volume): Paulsen reports hallucinations approaching 100% beyond the effective window. This paper finds a near-flat hallucination fraction from 2 to 10 documents while recall drops. The two measure different quantities (error share of output vs task accuracy) at different scales. A reader citing either for "more context, more hallucination" needs the contrast.
- [GSM-DC: irrelevant context degrades reasoning](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) -- **compares-with** (axis: controlled growth of non-target input): GSM-DC varies synthetic distractor count and finds power-law error growth. This paper varies naturally co-occurring documents, where most content is off-subtopic, and finds recall loss but flat output error share. They are two controlled volume manipulations with different dose-response shapes.
- [LongMemEval](../../../../sources/longmemeval-benchmarking-chat-assistants-long-term-memory.ingest.md) -- **compares-with** (axis: abstention when the asked-for information is absent): LongMemEval treats abstention on unsupported premises as a separate memory ability. This paper measures the same ability for summarization over a non-existent subtopic and shows it decays with document count. Together they suggest abstention is a separately failing capability across task shapes.

## Bidirectional Candidates

- [Paulsen: maximum effective context window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) <-> source -- **compares-with**: the Paulsen ingest's analysis treats hallucination growth beyond MECW as the headline. A return link would warn its readers that a multi-document study at small N finds the hallucination *share* stable while coverage falls.
- [Generalization Bias in LLM Summarization of Scientific Research](../../../../sources/peters-chin-yee-llm-generalization-bias.ingest.md) <-> source -- **compares-with**: the Peters/Chin-Yee ingest serves the epistemic-relevance workshop as the anchor case for scope broadening under compression. This paper supplies the relative frequency of overgeneralization against other summary errors, which bounds how central that failure is in multi-document settings.

## Reverse-edge Candidates

Theory may author `evidenced-by` edges to `kb/sources/` ingests (`kb/theory/COLLECTION.md` labels table). Both targets below are the not-yet-written ingest `kb/sources/from-single-to-multi-llm-hallucination-mds.ingest.md`.

- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) → future ingest -- **evidenced-by** (qualifies/bounds, not corroboration): it adds a summarization task shape to the volume and interference sections, and the flat-FDR result bounds what "degradation" looks like. The note already cites 5 unquoted tracked sources (ConvexBench, GSM-DC, web agents, Paulsen, J-space), the ADR 082 limit. Adding this one requires a verbatim quote retained via `cp-skill-ground`, or replacing a source.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) → future ingest -- **evidenced-by** (qualifies): the note's summarization-hallucination example could cite the measured taxonomy. The citation would qualify the default reading of "hallucination" as fabrication, since most measured MDS errors are instruction violations.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- the Peters/Chin-Yee ingest links it for dropped condition clauses. Here overgeneralization is only a sub-case of one error class with no separate counts, so the link is too thin to carry `is-evidence-for`. Peters/Chin-Yee is the better route.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) -- the abstention failures look related, but the paper measures no confidence or probability signal. Keyword-level match only.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- about merging multi-agent outputs. MDS merges documents, not independent agent answers, so the mechanism does not transfer.
- [Automated synthesis is missing good oracles](../../../../theory/automated-synthesis-is-missing-good-oracles.md) -- about judging novel cross-note insight. The paper's judge checks coverage against reference insights, a closed oracle, so the axis differs.
- [Two context boundaries govern collection operations](../../../../theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md) and [context efficiency is the central design concern](../../../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- linked from the Paulsen ingest, but at 2-10 short documents this paper gives no calibration of either boundary. Too generic to help.
- [Position-bias ingest](../../../../sources/position-bias.ingest.md) -- also about position effects, but on judge order in pairwise comparison. This paper's recency finding is "slight" and concerns provenance of generated errors. No shared measured axis strong enough for `compares-with`.
- [LLM webagents long-context benchmark](../../../../sources/llm-webagents-long-context-reasoning-benchmark.ingest.md) -- a valid volume comparison, but GSM-DC already carries the controlled-volume contrast with a sharper dose-response. Adding both would be redundant.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) -- the paper's 100-pair check of a gpt-4o-mini judge and its finding that the 3-to-2 label mapping shifts conversation-domain results by about 30% are relevant judge-calibration evidence. But reference allows only `see-also`, and the paper adds nothing to the proposal's design. Rejected rather than sprayed.
- `kb/agent-memory-systems/` and `kb/agentic-systems/` summarization hits (e.g. llm-wiki variants, `o-o.md`) -- feature descriptions, not claims the benchmark tests.

## Index Membership

- [LLM reliability tag](../../../../tags/llm-reliability-README.md) -- a future ingest may carry `tags: [llm-reliability]`. The paper substantively diagnoses why output deviates (instruction-violation vs fabrication vs uninformative output) and tests post-hoc correction. Sources do not join generated tag listings (`kb/sources/COLLECTION.md`), so this is search scope only.
- [Context engineering tag](../../../../tags/context-engineering-README.md) -- weaker fit. Degradation with document count is in scope, but the paper is a benchmark, not a context-management design. Optional.

## Synthesis Opportunities

Across this paper, Paulsen, GSM-DC and LongMemEval, "degradation with input volume" splits into at least three separately measured quantities: lost coverage (recall), rising error share in output, and lost abstention. These need not move together: this paper shows recall and abstention falling while error share stays flat. A note could argue that context-degradation claims must name which quantity degrades. The soft-degradation note currently treats "task performance drops" as one quantity. Do not create this during connect.

## Maintenance Observations

- `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` is at the five-unquoted-source limit (ADR 082). New corroborating or bounding sources on context degradation, including this one, cannot be linked there without quote retention. This recurring constraint may justify splitting the note by dimension (volume / interference / complexity).
- No tracked ingest exists for this snapshot. All authored edges wait on `cp-skill-ingest`.

## Flags

- Tension to keep visible, not resolve: the paper's flat hallucination share against document count differs from Paulsen's "hallucinations approaching 100% beyond the effective window". The scales and metrics differ (2-10 documents of about 750 words each vs effective-window limits; output error fraction vs task accuracy). An ingest should state that difference rather than present either as the general rule.
- Metric caveat that affects every `is-evidence-for` edge: the reported rates use an optimistic label mapping (PARTIAL counted as correct) and a gpt-4o-mini judge. The conversation-domain numbers shift by about 30% under the mapping choice, so conversation-domain magnitudes are weak support.
