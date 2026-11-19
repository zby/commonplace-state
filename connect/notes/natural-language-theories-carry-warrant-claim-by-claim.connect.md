---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/natural-language-theories-carry-warrant-claim-by-claim.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Theory warrant should be tracked at the finest granularity evidence licenses

**Source:** [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md)

## Discovery Trace

**Source, contract, and curated heads:**

- Verified the source bytes before discovery: SHA-256 `e3cab06807826dcd9d6dd7b567eff54899e01579214e7c31dfc7450b6c008fd0`. Read the source fully. Its central rule allocates warrant to the finest truth-apt unit and scope identified by the evidence, keeps joint support joint until attribution is available, and separates evidential attribution from dependency propagation.
- Read `kb/notes/COLLECTION.md`. It authorises local prospecting into `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; excludes `work`; and authorises `external` only for already-known targets. Read `kb/instructions/COLLECTION.md` for the first-class inverse instruction pass; it authorises instruction → note `rests-on` edges for meta-readers.
- Read `kb/notes/README.md`, `foundations-README.md`, `learning-theory-README.md`, and `discovery-README.md`, plus the `README.md` curated head for every other authorised local destination. `discovery-README.md` declares `complete: true`, so the discovery by-tag `rg` was skipped and recorded as such. That head already lists the source. `learning-theory-README.md` routes complete coverage through children including discovery; `foundations-README.md` does not list the source.

**Complete title and description surfaces:**

- Generated every authorised local title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes 350, reference 132, instructions 44, types 10, sources 487, agent-memory-systems 172, and agentic-systems 12.
- Enumerated every authorised local description surface with `rg '^description:' kb/<destination>/ --glob '*.md'`: notes 347, reference 130, instructions 97, types 13, sources 423, agent-memory-systems 170, and agentic-systems 10.
- For the source tags, ran `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the equivalent query for `learning-theory`. The `discovery` query was skipped because its curated head is complete.

**Notes prospecting and candidate evaluation:**

- Ran `rg -n -i 'joint warrant|joint support|bundle.{0,30}component|component.{0,30}bundle' kb/notes/ --glob '*.md'`, `rg -n -i 'epistemic (status|warrant)|warrant.{0,40}(claim|scope|evidence)|claim.{0,40}warrant' kb/notes/ --glob '*.md'`, `rg -n -i 'discriminating evidence|identif(y|ies|ication).{0,50}(contrast|contribution|component)' kb/notes/ --glob '*.md'`, and `rg -n -i 'formalization|formalisation|proof.{0,40}(scope|domain|translation)|translation.{0,40}(proof|claim)' kb/notes/ --glob '*.md'`.
- Kept [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): its treatment-grain argument supplies the causal-identification ground for keeping bundle evidence at bundle grain. It already links back to the source, so that inbound edge is existing graph state rather than a reverse-edge candidate.
- Kept [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md): it develops the source's short formalization boundary into explicit causal, proof, translation, and model-domain obligations. Its closing natural-language contrast independently benefits from a return edge to the source.
- Kept [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md): it supplies the operational mechanism by which represented support and dependencies permit a failed premise to trigger targeted rather than document-wide repair. Its own rationale claim independently needs the source's evidence-attribution rule.
- Rejected [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md): it is a broader payoff conjecture and remains reachable through the selective-revision and formal-systems neighborhoods; a direct edge from this bookkeeping rule would not add a distinct reader need.
- Rejected [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md): it shares warrant vocabulary, but its objective is contribution selection rather than allocation of theory warrant; it already reaches the relevant subdocument issue through mixed epistemic status.

**Link following and inbound scan:**

- Followed one hop from the source and the three kept note candidates with `rg -o '\]\([^)]*\.md[^)]*\)' <candidate-files>`. This traversed the existing reach-assessment, derivation/inheritance, mixed-status, representational-form, experimental-control, causal/proof, oracle-domain, theory-mediated-learning, reflection, scope-boundary, and reasoning-evaluation neighborhoods. The pass strengthened the three kept connections but surfaced no additional load-bearing outbound edge.
- Scanned authored inbound links with `rg -n '\[[^]]+\]\([^)]*natural-language-theories-carry-warrant-claim-by-claim\.md\)' kb/notes kb/reference kb/instructions kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'`. Besides the experiment's existing link, the `unwarranted-scope` and `epistemic-status-blur` gates already carry `rests-on` edges. [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) applies the source's rule repeatedly but does not yet name it in its meta-reader footer, so it passed the inverse instruction articulation test.

**Reference, instructions, and types:**

- Ran `rg -n -i 'claim.{0,40}(scope|warrant)|warrant.{0,40}(claim|scope)|epistemic status|document.level|unwarranted scope' kb/reference/ --glob '*.md'` and `rg -n -i 'bundle.{0,30}component|discriminating evidence|formal domain|translation.{0,40}claim' kb/reference/ --glob '*.md'`. [ADR-023](../../../../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) was rejected because quote resolution improves structural grounding but does not allocate semantic warrant among theory claims.
- Ran `rg -n -i 'warrant.{0,50}(claim|scope)|claim.{0,50}(warrant|scope)|epistemic status|document.level|unwarranted scope|bundle.{0,30}component' kb/instructions/ --glob '*.md'`. The two semantic gates were recognized as existing inbound edges; the full-improvement instruction was kept only in the reverse, meta-reader `rests-on` direction. No note → instruction `operationalized-from` candidate added ordering, defaults, or stopping conditions specific enough to pass authorisation.
- Ran `rg -n -i 'warrant|epistemic|claim|scope|evidence' kb/types/ --glob '*.md'`. The review-gate type's uncalibrated warrant boundary is adjacent system policy, not evidence or a mechanism for the source claim, so no type candidate passed.

**Sources and external-system collections:**

- Ran `rg -n -i 'joint (warrant|support)|bundle.{0,40}component|component.{0,40}bundle|theory.{0,40}(claim|proposition|component)' kb/sources/ --glob '*.ingest.md'`, `rg -n -i 'evidence.{0,50}(scope|claim)|warrant.{0,50}(scope|claim)|claim.{0,50}(warrant|scope)|epistemic status' kb/sources/ --glob '*.ingest.md'`, and `rg -n -i 'discriminating evidence|risky prediction|falsif|rival.{0,40}(theory|hypothesis)' kb/sources/ --glob '*.ingest.md'`. [The Anatomy of a Design Theory](../../../../sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md) was rejected: it identifies theory components but does not establish how evidence warrants them individually or jointly.
- Ran `rg -n -i 'epistemic status|claim.{0,50}(warrant|scope)|warrant.{0,50}(claim|scope)|bundle.{0,30}component|joint (support|warrant)' kb/agent-memory-systems/ --glob '*.md'`. [Dense-Mem](../../../../agent-memory-systems/reviews/dense-mem.md) was rejected: its verifier classifies whether stored fragments entail an individual claim and explicitly stops short of external truth; it neither tests bundle-to-component attribution nor the source's general warrant rule.
- Ran `rg -n -i 'epistemic status|claim.{0,50}(warrant|scope)|warrant.{0,50}(claim|scope)|bundle.{0,30}component|joint (support|warrant)|proof.{0,30}(claim|scope)' kb/agentic-systems/ --glob '*.md'`; no analysis passed the articulation test.
- Open-web prospecting was skipped. `external` is authorised only for already-known targets, and no external target was supplied or already loaded. `kb/work/` was not searched because the notes contract excludes it.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **grounds**: independent variation fixes the finest causal attribution an experiment licenses, explaining why evidence for a jointly changed bundle cannot be distributed to its components.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — **extends**: develops the source's formalization boundary by showing exactly how causal assumptions, proof obligations, translation fidelity, and model domain bound formal warrant.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — **mechanism**: shows how faithful records of support, assumptions, and dependencies turn claim-granular warrant loss into targeted revision rather than undirected document replacement.

## Bidirectional Candidates

- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → source — **extends**: the source develops that note's unresolved natural-language side by specifying the truth-apt unit, interpretation, and scope to which natural-language warrant attaches.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) → source — **grounds**: selective revision needs the source's separation of evidential attribution from dependency propagation to say which premise lost support before a rationale determines what else should change.

## Reverse-edge Candidates

- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) → source — **rests-on**: the instruction repeatedly requires contribution warrant to preserve differences among observations, deductions, mechanisms, and conjectures, and the source states the claim-level non-distribution rule that makes that requirement coherent for meta-readers.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — broader payoff conjecture already reachable through more specific kept candidates; no distinct direct reader need.
- [Warranted reader update is the objective of substantive writing](../../../../notes/warranted-reader-update-is-the-objective-of-substantive-writing.md) — shares warrant vocabulary but addresses contribution selection, not attribution of support within a theory.
- [ADR-023: Quote-anchored citations for code-grounded reviews](../../../../reference/adr/023-quote-anchored-citations-for-code-grounded-reviews.md) — structural quote resolution narrows a citation check but does not establish semantic support or its distribution across claims.
- [The Anatomy of a Design Theory](../../../../sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md) — identifies theory components and scope without establishing claim-level or joint warrant.
- [Dense-Mem](../../../../agent-memory-systems/reviews/dense-mem.md) — claim/evidence entailment is a system-specific verification boundary and does not test the source's bundle-attribution or scope-transfer rule.

## Index Membership

- [Foundations](../../../../tags/foundations-README.md) — the source adds the foundational distinction between criticizable theory structure and evidence-granular warrant; it is tagged `foundations` but absent from this curated head. Discovery already lists it, and learning-theory routes through the complete discovery child.

## Synthesis Opportunities

None

## Maintenance Observations

- The final H1, “Theory warrant should be tracked at the finest granularity evidence licenses,” no longer matches the filename or the visible source labels in [discovery](../../../../tags/discovery-README.md), [the experimental-contrast note](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), [unwarranted-scope](../../../../instructions/review-gates/semantic/unwarranted-scope.md), and [epistemic-status-blur](../../../../instructions/review-gates/semantic/epistemic-status-blur.md), which still state variants of “natural-language theories carry warrant claim by claim and scope by scope.” A later retitle-alignment operation should rename through the repository relocation command and reconcile visible link text and summaries; connect does not perform that mutation.

## Flags

None
