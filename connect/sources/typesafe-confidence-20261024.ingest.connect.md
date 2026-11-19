---
description: "Post-ingest discovery for TypeSafe confidence: qualitative score semantics, calibration boundaries and recovery policy; missing mathematics excludes formula and equivalence claims."
type: types/connect-report.md
source: kb/sources/typesafe-confidence-20261024.ingest.md
source_has_frontmatter: true
date: "2026-10-24"
depth: standard
---

# Connection Report: TypeSafe confidence documentation

**Source:** [TypeSafe confidence documentation](../../../../sources/typesafe-confidence-20261024.ingest.md)

Exact source path: `kb/sources/typesafe-confidence-20261024.ingest.md`.
This is accepted-ingest post-ingest discovery. Every edge below is a candidate for a future writer, not an authored library link. The source remains unchanged. Its three existing prose connections are identified below rather than presented as new discoveries.

## Discovery Trace

### Setup and recall surface

Read the connect skill, connect-report type and schema, source ingest, sources collection contract, reports collection contract and theory collection contract completely. Sources authorizes prospecting theory, reference, historical agent-memory systems, agentic systems, tags and other sources. Work and instructions are excluded. Read each of those six destination collections' root README. Read the LLM reliability and evaluation tag heads via topical routing; neither declares complete membership. The source has domains but no tags, so no matching-source-tag search or complete-tag skip applies.

Generated fresh complete title listings with `rg -N --no-heading -m1 '^# ' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md'`. The combined output truncated; repeated as two complete displayed title surfaces, one for theory and one for the other five destinations, using `cut -d: -f2-` to retain titles. Candidate paths were recovered through scoped description and body searches. No semantic scores are available.

Description scan: `rg '^description:' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md' | rg -i 'confidence|calibrat|discriminat|abstain|uncertainty|threshold|typed.decision|Jev|Basal|TypeSafe'`.

### Theory

- Root README and the two tag heads routed to generation confidence, reliability dimensions, the augmentation/automation boundary and structured recovery. Read those four notes fully.
- Body query: `rg -n -i 'confidence|calibrat|discriminat|fallback|escalat' kb/theory/{generation-confidence-does-not-by-itself-certify-soundness,reliability-dimensions-map-to-oracle-hardening-stages,enforcement-without-structured-recovery-is-incomplete,the-augmentation-automation-boundary-is-discrimination-not-accuracy}.md`.
- Followed the generation-confidence note's link to reliability dimensions, then the reliability head's recovery link. Kept the existing generation-confidence comparison and a new recovery comparison. Kept reliability dimensions as an inbound companion opportunity, not evidence that TypeSafe has a calibrated oracle. Rejected using the source to establish or refute empirical discrimination stagnation.
- The title surface also surfaced capture fidelity. Read `kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md` fully; used its distinction to constrain this report, not to recommend another generic provenance link.

### Reference

- Root README and filtered descriptions exposed the proposal on calibrating semantic gates.
- Query: `rg -n -i 'calibrat|discriminat|abstain|uncertainty|risk.based' kb/reference/ --glob '*.md'` (inspected the first 60 hits).
- Rejected the proposal as an outbound companion: it designs known-case regression and independently sampled gate calibration; TypeSafe supplies neither such evidence nor a concrete implementation of that proposal. No direct shipped-system relationship was found.

### Historical agent-memory systems

- Root README identifies a frozen historical corpus, not a current adoption surface.
- Query: `rg -n -i 'confidence|calibrat|uncertainty' kb/agent-memory-systems/reviews/{synto,quicky-wiki,Self-Training-LLM}.md`.
- Evaluated description/body hits: Synto uses confidence for draft publication, Quicky Wiki maintains heuristic claim confidence, and Self-Training-LLM filters training data using uncertainty. Rejected all three as unnecessary outbound comparisons: their scores have different producers and consumers; keyword overlap does not establish TypeSafe integration or equivalent score semantics. No reverse edge is justified merely because a historical review mentions confidence.

### Agentic systems

- Root README and full title surface checked current accounts and archived reviews.
- Broad query: `rg -n -i 'TypeSafe|\bJev\b|\bBasal\b|selective.accept|risk.based|confidence.threshold' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/ --glob '*.md'` surfaced the mem review and archival reports. Large comparison-table hits were not treated as independent support.
- Focused query: `rg -n -i 'JEV|confidence|calibrat' kb/agentic-systems/reviews-archive/instinctual-memory.md`. Read that review fully. Kept the existing comparison solely on component placement: requested retrieval ranking versus typed-answer uncertainty routing. Do not infer provider internals from an alias or attach new documentation as if it belonged to the review's historical source boundary.

### Other sources

- Root README, complete titles and filtered descriptions identified Basal and Competing Biases. Read both ingests fully.
- Query: `rg -n -i 'confidence|calibrat|threshold' kb/sources/{basal-2-0-max-20261024,competing-biases-llm-confidence}.ingest.md`.
- Followed the source's existing Basal link and Basal's generation-confidence link. Kept Basal as the strongest comparison and a useful return-link candidate. Competing Biases is a legitimate but lower-priority methodological neighbor: its synthetic-advice intervention is not a test of this provider statistic; omitted from recommended edges to avoid a confidence-topic spray.

### Tags and external

- Query: `rg -n -i 'confidence|calibrat|discriminat' kb/tags/ --glob '*.md'`; read the evaluation and LLM reliability heads fully. They already route readers to the relevant theory. No new head entry is needed for this narrow product document.
- Tags is an authorized scan surface but has no matching source-to-tags label row. No sufficiently valuable tag-target edge survived articulation, so there is no off-authorization candidate.
- External prospecting skipped. The already supplied `https://docs.typesafe.ai/confidence` is the ingest's original source, compatible with `derived-from`; durable identity is already recorded in frontmatter. No additional external edge is recommended and no network call was made.

All retained and rejected candidate paths were checked to exist locally. Discovery used the ingest's analysis and retained quotes, not a reconstructed mathematical source.

## Connections Found

- [Basal model-card ingest](../../../../sources/basal-2-0-max-20261024.ingest.md) — **compares-with**: TypeSafe describes a deterministic distribution summary and local threshold testing; Basal reports fitted calibration and selective error/coverage. The comparison helps an evaluator separate defining a score from validating an acceptance policy. Existing source-side connection; preserve its qualitative scope. No common formula, weights, calibration, interface interchangeability or model-quality ranking follows.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) — **compares-with**: both require establishing the relationship between a probability-derived signal and correctness separately, but next-token generation probability and typed-answer distribution summaries are different readouts. Existing source-side connection; retain as comparison, not empirical corroboration.
- [mem: sourced facts and host context](../../../../agentic-systems/reviews-archive/instinctual-memory.md) — **compares-with**: requested Jev relevance ranking in mem and uncertainty-based proceed/defer routing perform different causal jobs. Existing source-side connection; useful for avoiding a false Jev/Basal/TypeSafe equivalence in the investigation. The pinned review establishes neither current provider semantics nor comparative model quality.
- [Enforcement without structured recovery is incomplete](../../../../theory/enforcement-without-structured-recovery-is-incomplete.md) — **compares-with**: TypeSafe's qualitative confirmation, information-gathering, fallback and human-routing advice gives a concrete application-policy comparison to the note's separation of detection from recovery. A future KB trial must specify what happens after a threshold failure, not just the threshold. This is advice about response design, not evidence of executed recovery or bounded harm.

## Bidirectional Candidates

- [Basal model-card ingest](../../../../sources/basal-2-0-max-20261024.ingest.md) → source — **compares-with**, authorized by sources/COLLECTION.md: a return comparison would help Basal readers distinguish its fitted calibration and accepted-case measurements from a provider's default distribution statistic. The source already points to Basal; Basal currently does not point back. Keep the comparison qualitative because TypeSafe's formulas and example distributions were lost.
- [Generation confidence does not by itself certify soundness](../../../../theory/generation-confidence-does-not-by-itself-certify-soundness.md) → source — **see-also**, authorized for theory→sources: an optional body-level companion could show a documented typed-answer uncertainty interface beside the note's next-token case, while retaining the need for task-specific validation. This is not `evidenced-by` corroboration: the product documentation did not test the note, and its statistic is not the same object.

## Reverse-edge Candidates

- [Reliability dimensions map to oracle-hardening stages](../../../../theory/reliability-dimensions-map-to-oracle-hardening-stages.md) → source — **see-also**, authorized for theory→sources: an optional companion at the predictability discussion would distinguish an exposed distribution summary and risk-dependent response advice from measured calibration, discrimination and tested failure containment. The concrete reader benefit is recognizing which validation operations are still absent despite the presence of a field called confidence. The documentation supplies no empirical result for any of those dimensions; do not describe it as corroborating the note's empirical scaling claims.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [The augmentation-automation boundary is discrimination not accuracy](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) — no empirical discrimination test exists here, so neither corroboration of stagnation nor a counterexample to it is supported. Its basic caution is already served more precisely by the generation-confidence comparison.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — local threshold advice does not instantiate this proposal's known-case regression or field-calibration design. A generic testing adjacency would not improve this narrow ingest.
- [Synto](../../../../agent-memory-systems/reviews/synto.md), [Quicky Wiki](../../../../agent-memory-systems/reviews/quicky-wiki.md), and [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) — confidence is used for draft admission, graph maintenance and training-data filtering respectively. Different score production and downstream jobs make a broad cross-link unhelpful without a more specific design question.
- [Competing Biases](../../../../sources/competing-biases-llm-confidence.ingest.md) — useful context-sensitive confidence experiments, but no test of TypeSafe's statistic. Do not transfer the paper's behavioral results to this interface or use its equations to fill the missing TypeSafe mathematics.

## Index Membership

None. The sources landing is a collection guide, not a source roster. The selective tag heads already expose the relevant theory; no new entry is warranted.

## Synthesis Opportunities

None. Separating retrieval relevance, distribution summaries and validated selective acceptance is useful investigation framing already stated by the ingest, not yet an independently supported new theoretical claim.

## Maintenance Observations

The partial-source capture loses rendered mathematics and example distributions. A separately authorized new observation preserving those expressions is needed before formula comparison, numerical checking or compatible implementation. Preserve the existing bytes and checksum; neither the Basal card nor background knowledge repairs this evidence gap. No recapture is performed here.

## Flags

- **Binding source limit:** `capture_scope: partial-source` restricts every candidate to documented qualitative semantics, recommended response patterns and explicit validation gaps. No exact Choice/Score formula, numerical example, cross-type probability equivalence or threshold guarantee is inferred.
- **Evidence grade:** official-statement documentation supports intended interface behavior and provider advice, not observed calibration, error discrimination, workflow benefit or high-assurance acceptance. Do not upgrade candidates to `is-evidence-for` on those claims.
- **Historical boundary:** do not append contemporary provider semantics to the pinned mem review as if they were inspected at its reviewed revision. No reciprocal edit to that historical review is recommended.
- **No mutation authority:** deployment, model selection, math reconstruction and authoring any proposed library link remain outside this invocation. Only this cache report is written.
