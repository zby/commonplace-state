---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: An insufficient summary precedes the source rather than replacing it

**Source:** [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md)

## Discovery Trace

All discovery was repository-local. No semantic scores were available. Existing authored links from the source were used as traversal neighborhoods and were not re-proposed under `Connections Found`.

### `kb/notes/`

**Curated heads:**

- Read [`README.md`](../../../../notes/README.md), [`context-engineering-README.md`](../../../../tags/context-engineering-README.md), and [`document-system-README.md`](../../../../tags/document-system-README.md). Neither tag README declares `complete: true`, so neither by-tag scan was skipped. The source is tagged for both indexes but appears in neither curated head.

**Title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` over the complete 359-heading title surface.
- Ran the 356-line whole-collection `rg '^description:' kb/notes/ --glob '*.md'` surface, then the narrower `rg -l '^tags:.*\bcontext-engineering\b' kb/notes/ --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''` (48 tagged files) and the corresponding query for `document-system` (26 tagged files). The tag scans surfaced the source beside the addressability, cache-ledger, task-relative trust, routing-signal, and multi-consumer notes.

**Body searches:**

- `rg -n -i 'summary.{0,120}(source|raw|trace|fallback)|(?:source|raw|trace|fallback).{0,120}summary' kb/notes/ --glob '*.md'` — found the existing addressability and materialization neighborhood, trace-summary boundary cases, and the missing multi-consumer connection.
- `rg -n -i 'sufficien.{0,100}(stop|reliab|answer|source)|(?:stop|reliab|answer|source).{0,100}sufficien|full substitution|partial substitution|pure addition' kb/notes/ --glob '*.md'` — found no duplicate of the four-part stopping claim; it strengthened the rule-ready-signal and multi-consumer candidates.
- `rg -n -i 'compression ratio|fallback work|source anyway|source path|reconstructions avoided|materiali[sz].{0,100}(substitut|remove)|substitut.{0,100}(work|cost)' kb/notes/ --glob '*.md'` — confirmed that opposed-recompute supplies the outer ledger while the source supplies the condition inside “reconstructions avoided.”
- `rg -n -i 'orientation.{0,120}(accuracy|question|summary|source)|accuracy.{0,120}(orientation|question|summary|source)|coverage.{0,80}(signal|reliab)|reliab.{0,80}(signal|coverage)' kb/notes/ --glob '*.md'` — found no competing orientation/accuracy treatment and exposed the pre-existing-signal prerequisite behind the source's open routing question.
- `rg -n -i 'expected.{0,100}(fallback|summary|read|reconstruction)|traffic distribution|closure rate|cost currency|reorientation|stopping question|license.{0,80}(action|stop)|authoritative fallback' kb/notes/ --glob '*.md'` — found no separate estimator for the source's distribution-level ledger; the cache-ledger and two-layer-fallback hits were already evaluated above.

**Candidate evaluations:**

- Treated [`rule-based-context-selection-needs-a-pre-existing-signal.md`](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) as an existing authored neighbor rather than a new outbound candidate: the final source now uses it inline for the operational prerequisite behind direct fallback routing.
- Kept [`serve-multiple-consumers.md`](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md): its evidence-sufficiency signals and trace-replay fallback directly develop the source's open question about detecting likely insufficiency before overusing a thin result.
- Kept [`linked-note-durable-payload-is-what-consumption-path-cannot-supply.md`](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md): it applies reliability relative to a consumption path to the concrete authoring decision about what may safely be factored behind a link.
- Rejected [`an-experiment-identifies-only-the-contrast-it-actually-runs.md`](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): its Meta-Harness case concerns a trace-replacing summary with no raw fallback, so it sharpens the source's excluded boundary but does not test the summary-then-fallback ledger.
- Rejected [`access-burden-and-transformation-burden-are-distinct-query-dimensions.md`](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md): it can classify some removed fallback work but does not decide whether the candidate answer licenses stopping, and the source already names the relevant work categories locally.
- Rejected [`agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md): its task-relative loadability and trust tests are a useful umbrella, but the kept routing-signal and multi-consumer notes answer the source's specific open questions more directly.
- Rejected [`semantic-work-can-be-relocated-but-not-eliminated.md`](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md): it accounts for total semantic work across production and consumption, whereas the source measures work removed from one use path after the summary already exists.
- Rejected [`stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md`](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md): it explains a dangerous false stop caused by apparent completeness, but that case lies outside the source's reliability-compliant ledger and is already reachable through the checked-copy neighborhood.
- Rejected [`theory-and-methodology-form-a-two-layer-execution-system.md`](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md): its fast-path/live-theory architecture makes fallback expected for uncovered cases, but it does not compare a consumed summary with a direct authoritative route or price work removed from that route.

**Link following:**

- Followed all existing source links to pointer design, rule-based selection, addressability, opposed recompute, LLM recompute, frontloading, recoverability, and context efficiency. Addressability and LLM recompute already carry useful return links to the source; pointer design, rule-based selection, opposed recompute, and frontloading do not, yielding the four return-link candidates below.
- Followed opposed recompute to `Serve Multiple Consumers`, then followed that note to Cludebot's experimental coverage/strength/diversity/agreement gate. This established a concrete signal family without elevating the Cludebot review itself to evidence for the source's stopping ledger.
- Followed the linked-note payload note through its recognition-anchor and behavioral-test neighborhood. It develops a distinct authoring application rather than duplicating the summary-cost claim.

### `kb/types/`

- Read [`README.md`](../../../../types/README.md), ran `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'` (10 headings), and ran `rg '^description:' kb/types/ --glob '*.md'` (13 description lines, including template examples).
- Ran `rg -n -i 'summary|sufficien|substitut|reliab|fallback|compression ratio|source path' kb/types/ --glob '*.md'`. The note type says descriptions are retrieval filters rather than summaries, while the tag-README type governs deterministic cache marks. Neither type observes, tests, or operationalizes the source's reliability-relative stopping claim, so no candidate passed the articulation test.

### `kb/reference/`

- Read [`README.md`](../../../../reference/README.md), ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (140 headings), and ran `rg '^description:' kb/reference/ --glob '*.md'` (139 description lines).
- Ran `rg -n -i 'summary.{0,120}(source|raw|fallback)|(?:source|raw|fallback).{0,120}summary|sufficien.{0,100}(answer|reliab|stop)|source anyway|orientation.{0,100}accuracy|compression ratio|fallback work' kb/reference/ --glob '*.md'`. The binding [`COLLECTION.md`](../../../../reference/COLLECTION.md) economy test restates the source-anyway test, orientation/accuracy distinction, and matched-grain caution; under its own outbound rules it can author a reverse `rests-on` edge.

### `kb/agent-memory-systems/`

- Read [`README.md`](../../../../agent-memory-systems/README.md), ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (173 headings), and ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` (171 description lines).
- Ran `rg -n -i 'summar(y|ies|ization)|progressive disclosure|full content|fallback|source of truth|authoritative' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i 'summary.*(source|full|fallback|trust|reliab)|source.*summary|description.*(full|body|load)|overview.*(detail|source)' kb/agent-memory-systems/ --glob '*.md'`.
- Rejected [`OpenViking`](../../../../agent-memory-systems/reviews/openviking.md): its L0/L1/L2 architecture can route from abstracts through overviews to full content, but the review supplies neither a question-level stopping test nor a matched comparison of read cost and removed fallback work.

### `kb/agentic-systems/`

- Read [`README.md`](../../../../agentic-systems/README.md), ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (12 headings), and ran `rg '^description:' kb/agentic-systems/ --glob '*.md'` (10 description lines).
- Ran `rg -n -i 'summar(y|ies|ization)|progressive disclosure|full content|fallback|source of truth|authoritative' kb/agentic-systems/ --glob '*.md'` and `rg -n -i 'summary.*(source|full|fallback|trust|reliab)|source.*summary|description.*(full|body|load)|overview.*(detail|source)' kb/agentic-systems/ --glob '*.md'`. [`Fractal`](../../../../agentic-systems/reviews/fractal.md) retains an always-visible session summary beside inspectable full history, but its analysis provides no task-relative stopping test or path-cost comparison; no candidate passed.

### `kb/sources/`

- Read [`README.md`](../../../../sources/README.md), ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` (289 headings), and ran `rg '^description:' kb/sources/ --glob '*.md'` (289 description lines).
- Ran `rg -n -i 'summar(y|ies|ization)|progressive disclosure|full content|fallback|source of truth|authoritative' kb/sources/ --glob '*.md'`, then focused on source reopening, raw-evidence fallback, hierarchical summaries, and faithfulness with `rg -n -i 'reopen.{0,100}(source|file)|source.{0,100}verif|progressive.{0,120}(source|raw|original)|(?:source|raw|original).{0,120}progressive|hierarch.{0,100}(summary|evidence|source)' kb/sources/ --glob '*.md'`.
- Kept [`Harness Handbook`](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md): the handbook treatment uses L1-L3 views to narrow edit-site search, requires every proposed site to be reopened in live source before planning, and reduced planner-token use in its bounded evaluation. This is a direct partial-substitution case rather than mere architectural resemblance.
- Kept [`Decentralized Multi-Agent Systems with Shared Context`](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md): its gist-to-summary-to-raw hierarchy retains authoritative drill-down, while removing the intermediate summary layer separately reduced GPT-5.4 LongBench accuracy. The fixed-pipeline limit keeps this as bounded evidence, not a general prevalence claim.
- Rejected [`Meta-Harness`](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md): its fixed summary arm had no raw-trace access, so the experiment measures lost diagnostic information under replacement rather than an additive summary-then-source path.

**Link following:**

- Followed Harness Handbook to pointer design, checked-copy enforcement, and compiled-view alignment. Its distinctive addition here is the measured combination of mandatory live-source verification and reduced planner-token use.
- Followed DeLM to the coordination-guarantee and fixed-decomposition notes. Its summary ablation and recoverable raw-evidence hierarchy support only the tested pipeline, which matches the source note's bounded per-use framing.

### `kb/instructions/`

- Read [`README.md`](../../../../instructions/README.md), ran `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` (47 headings), and ran `rg '^description:' kb/instructions/ --glob '*.md'` (99 lines, including review-gate and template descriptions).
- Ran `rg -n -i 'summary.{0,120}(source|raw|trace|only)|(?:source|raw|trace).{0,120}summary|fresh agent loaded with only|sufficien.{0,80}(evidence|answer|reliab)|source anyway' kb/instructions/ --glob '*.md'`.
- Kept [`example-onboard-second-brain.md`](../../../../instructions/example-onboard-second-brain.md): Phase 3 fixes a consumed context summary, a fresh consumer, and an orientation question, then tests whether that route can stop at the summary; this adds a concrete sufficiency gate without claiming to estimate the fallback-work ledger.
- Rejected snapshot and paper-ingest instructions that require full-source capture: those rules protect capture fidelity and evidence authority rather than test whether a consumed summary removes fallback work.

### Reserved `external`

- The notes contract authorizes `external`, but no external target was supplied or already present in loaded context. Open-web prospecting was therefore skipped.

## Connections Found

- [Serve Multiple Consumers, Not One Retrieval Interface](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) — **extends**: develops the open routing question into evidence-sufficiency signals that may warn before overuse and trace/source surfaces that remain available when a summary is under suspicion.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — **extends**: applies reliability-relative path sufficiency to the authoring decision about whether shared exposition can be factored behind a link or must remain inline as recognition, rationale, provenance, or warrant.
- [Ingest: Harness Handbook](../../../../sources/harness-handbook-making-evolving-agent-harnesses-readable.ingest.md) — **evidenced-by**: a bounded handbook treatment with L1-L3 pointers reduced planner tokens and improved localization while exact edit planning still required reopening current source, demonstrating useful partial substitution rather than task closure.
- [Ingest: Decentralized Multi-Agent Systems with Shared Context](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) — **evidenced-by**: its summary hierarchy retains raw-evidence fallback, while removing the intermediate layer lowers accuracy inside the tested pipeline; this bounds the claim that failure of full substitution need not make a summary useless, although the experiment does not measure the read-cost ledger.
- [Example: Onboard a Second Brain on Commonplace](../../../../instructions/example-onboard-second-brain.md) — **operationalized-from**: Phase 3 fixes a summary, fresh consumer, orientation question, and cold-context boundary, then requires that route to stop with a coherent summary-only answer before the onboarding phase closes.

## Bidirectional Candidates

- [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) ↔ source — return **grounds** edge: the source already points to its outer cache ledger; the return path would expose the stopping condition that determines whether one of that ledger's “reconstructions avoided” was actually avoided at matched reliability.
- [Pointer design tradeoffs in progressive disclosure](../../../../notes/pointer-design-tradeoffs-in-progressive-disclosure.md) ↔ source — return **contrasts** edge: the source already credits pointers as partial substitution; pointer readers gain the complementary distinction that preceding a source is success for narrowing but not evidence that the pointer closed the task.
- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) ↔ source — return **extends** edge: the source already uses the selector prerequisite; the return path adds its economic consequence—without an advance signal, summary-routed attempts pay summary cost before learning whether authoritative fallback remains necessary.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) ↔ source — return **grounds** edge: the source already applies frontloading; the return path supplies the reliability-relative test for whether an inserted result replaced derivation or merely added itself ahead of it.

## Reverse-edge Candidates

- [`kb/reference/COLLECTION.md`](../../../../reference/COLLECTION.md) → source — **rests-on**: its binding economy test uses the source-anyway criterion, orientation/accuracy split, and matched-grain caution; a meta-reader link would expose the theory behind that contract rule.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — its fixed summary-without-traces case has no authoritative fallback available to that arm, so it bounds an excluded replacement regime rather than testing the source's additive summary-then-fallback ledger.
- [Access burden and transformation burden are distinct query dimensions](../../../../notes/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — can decompose some saved work but cannot say whether the summary licenses stopping, and adds no distinct traversal need beyond the source's own work ledger.
- [Agent memory needs discoverable, loadable, composable, trusted knowledge under bounded context](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) — a broad use-time umbrella; the kept routing-signal and multi-consumer notes answer the source's concrete design questions more directly.
- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — concerns total semantic work across production and consumption, while the source's ledger is intentionally scoped to fallback work removed from one use path.
- [Stale indexes reduce discovery when they suppress fallback search](../../../../notes/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — explains an unsafe false stop, which the source explicitly excludes from the reliability-compliant ledger and already reaches through its checked-copy neighborhood.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — shares a fast-path/fallback shape but does not compare summary consumption with the direct fallback path or supply the source's reliability-relative cost ledger.
- [OpenViking](../../../../agent-memory-systems/reviews/openviking.md) — L0/L1/L2 architecture without evidence that a tier closes a stated question or reduces the matched fallback path.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — exposes an always-visible session summary and separately inspectable full history, but the analysis supplies neither a stopping test nor evidence about fallback work removed.
- [Ingest: Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — the summary arm could not reach raw traces, so its measured loss belongs to the source note's unsupported-answer boundary rather than its additive-read ledger.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) — the source belongs beside addressability and opposed recompute as the reliability-relative stopping condition for context-saving summary layers.
- [Document system](../../../../tags/document-system-README.md) — the source belongs in the documentation-cache cluster because it changes how summaries and reference layers should be evaluated independently of whole-artifact compression.

## Synthesis Opportunities

- The source, [rule-based context selection](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md), and [Serve Multiple Consumers](../../../../notes/agent-memory-requirements/serve-multiple-consumers.md) imply a reliability-aware summary router: when a rule-ready coverage or trust signal predicts that the summary cannot close the question, route directly to the authoritative path; when no such signal exists, expose the summary as a bounded pointer with an explicit weak-evidence state and preserved drill-down. The source asks for the advance signal, while the other notes constrain its implementation; no note yet states or tests the composed policy.

## Maintenance Observations

None

## Flags

None
