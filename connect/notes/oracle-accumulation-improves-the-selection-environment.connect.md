---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/oracle-accumulation-improves-the-selection-environment.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: Oracle accumulation in its maintained domain

**Source:** [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md)

## Discovery Trace

**Authorisation and posture:**
- Read `kb/notes/COLLECTION.md` and filtered candidates by its source-to-destination rules. It authorises `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, `kb/instructions/`, and the reserved `external` destination; it excludes `kb/work/`. Notes permit theoretical labels such as `grounds`, `enables`, and `exemplifies`; descriptive systems and sources permit `evidenced-by`; reference permits `evidenced-by`, lineage labels, and sparse `see-also`; instructions permit `operationalized-from` and sparse `see-also`.
- Read `kb/agent-memory-systems/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/agentic-systems/COLLECTION.md`, `kb/sources/COLLECTION.md`, `kb/instructions/COLLECTION.md`, and `kb/types/COLLECTION.md` before judging return links. The notes contract says instruction edges are usually inverse, so instruction-to-note `rests-on` prospecting was treated as a first-class reverse pass.
- No external target was supplied or present as an independently loaded candidate, so external prospecting was skipped as required; no web search was performed.

**Curated heads and tag routing:**
- Read `kb/notes/README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/deploy-time-learning-README.md`. The learning-theory head declares `covered_by: [deploy-time-learning, ...]`, so its direct by-tag `rg` was skipped and the child routing was trusted. The deploy-time-learning head has no `complete: true`, so ran `rg -l '^tags:.*\bdeploy-time-learning\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; the source is tagged but absent from the curated head.
- Read destination heads `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. `kb/types/README.md` does not exist, so the small collection's title and body surfaces were used directly.

**Full title and description scans:**
- Generated a fresh complete title surface once per authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for notes, types, reference, agent-memory-systems, agentic-systems, sources, and instructions.
- Ran `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'oracle|selection|check|validat|enforc|failure|accumulat|evaluation|retention|autonomy|formaliz|lesson|policy'`. It elevated the proposal-selection loop, typed-target verification, accepted-edit generalisation boundary, error-correction/decorrelation, diagnostic-richness, and broader constraining notes.
- Ran the corresponding destination-scoped description filters over reference, agent-memory-systems, agentic-systems, sources, instructions, and types using combinations of `validat|oracle|failure|check|enforc|selection|regression|promot|learn|gate|eval`. The closest non-note candidates were the gate-learning proposal, Auto Harness, Autocontext, the Fintool ingest, and fixed gate/type contracts.

**Body search:**
- Ran `rg -n -i 'oracle accumulation|failure-derived|selection environment|selection.*retention|retention.*selection|regression coverage|validation (corpus|work)|maintained check|checks? accumulate|exhaustive (delivery|consumption)|amortiz' kb/notes/ --glob '*.md'`. This surfaced the proposal-selection anatomy, retained-criterion path, validator amortisation, and already-authored inbound uses in the bitter-lesson and reflective-machinery notes.
- Ran `rg -n -i 'failure.{0,40}(check|test|validator|gate)|check.{0,40}(accumulat|retain|correlat|domain)|regression|selection environment|oracle domain' kb/notes/ --glob '*.md'`. Kept typed-target verification, accepted-edit generalisation, and decorrelated-check error correction because each explains a distinct clause or caveat in the source; rejected broader same-cluster matches that merely repeat the source's existing oracle-strength and spec-mining links.
- Ran destination-scoped variants of `rg -n -i 'regression|promot.{0,30}(test|eval|suite|gate)|failure.{0,40}(check|test|gate)|oracle|validation obligation'` over reference, agent-memory-systems, agentic-systems, sources, instructions, and types. Auto Harness uniquely showed automatic promotion of newly fixed failures into a later regression suite. Autocontext generates validators but does not establish the same failure-derived regression obligation as directly. Agentic-system matches exposed fixed gates, not accumulating check corpora. Instruction and type matches described or consumed fixed checks rather than operationalising accumulation.
- Ran `rg -n '\]\([^)]*oracle-accumulation-improves-the-selection-environment\.md\)' kb/ --glob '*.md'`. Existing inbound links were found in the bitter-lesson note, the reflective-machinery note, the bidirectional-codification proposal, and the effective-harnesses ingest; those authored edges were not re-proposed.

**Link following and candidate evaluation:**
- Followed the source's existing links to retrieval failure, the tag-readme causal trace, warranted autonomy, the readable-artifact loop, oracle strength, spec mining, harness engineering, the consumption-channel authority warning, and relaxing signals. This confirmed that spec mining and the tag-readme episode are already covered; a second link to the self-improving-loop interpretation of the same episode would be redundant.
- Followed one hop from the proposal-selection loop through behavioral authority, oracle strength, the two-layer promotion system, accumulation, and reflection. Kept it as the missing base architecture: the source's retained checks strengthen the loop's evaluation function and become consequential only through operative retention.
- Followed typed-target verification through warranted autonomy, codification, artifact analysis, and Exo. Kept it because the source's new title and opening make “maintained domain” load-bearing, and the target explains how reusable checks acquire a statable domain that covers later instances.
- Followed accepted-edit generalisation through trace-extracted authority, spec mining, oracle strength, and the gate-learning proposal. Kept it because it supplies the exact instance-to-rule warrant boundary behind the source's regression-coverage-versus-domain-expansion distinction.
- Followed error correction through oracle strength, spec mining, reliability hardening, and isolation. Kept it because it explains why merely accumulating overlapping or correlated checks may fail to improve discrimination.
- Followed the gate-learning proposal through accepted edits, spec mining, methodology enforcement, review architecture, and quality signals. Kept a sparse `see-also` outbound edge and a `rests-on` return candidate: the unadopted design applies the source's mechanism by proposing a maintained gate registry with promotion, calibration, quarantine, and retirement.
- Followed Auto Harness through its trace-learning survey, system-definition/knowledge definitions, and regression-suite evidence. Kept it over Autocontext and self-reported source cases because the code-grounded review explicitly records fixed failures becoming durable task-id regression obligations that gate later candidates.
- Verified every retained candidate path with `test -f` before writing the report.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **grounds**: supplies the loop anatomy in which accumulated checks strengthen the evaluation function and only matter once retained with enough authority to affect later acceptance.
- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) — **grounds**: explains the source's load-bearing “maintained domain” qualifier—a reusable check covers later candidates only when its target class and membership are statable.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — **grounds**: supplies the instance-to-generalisation warrant boundary behind the source's distinction between immediate regression coverage and earned oracle-domain expansion.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **grounds**: develops the source's correlation caveat by showing why overlapping checks with shared errors do not amplify discrimination merely because more checks were retained.
- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) — **see-also**: applies the mechanism to a proposed maintained registry in which instance-derived gates gain authority through promotion, calibration, quarantine, and retirement rather than raw accumulation.
- [Auto Harness](../../../../agent-memory-systems/reviews/auto-harness.md) — **evidenced-by**: the code-grounded system promotes newly fixed train failures into a regression suite whose gate evaluates later agent candidates, while keeping natural-language lessons on a separate advisory wire.

## Bidirectional Candidates

- [Gate learning from accepted edits](../../../../reference/proposals/gate-learning-from-accepted-edits.md) <-> source — **rests-on**: the proposal depends on the claim that retained checks change later selection and therefore require corpus lifecycle controls; the source-side `see-also` gives theory readers the concrete design application.
- [Auto Harness](../../../../agent-memory-systems/reviews/auto-harness.md) <-> source — **is-evidence-for**: its automatic promotion of fixed failures into later regression obligations materially bears on the theory claim, while the source gives system readers the lesson/check and retrieval/enforcement distinctions needed to interpret that mechanism.

## Reverse-edge Candidates

None. The useful unauthored return edges are paired with outbound candidates above; the strongest other inbound relationships are already authored.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) — central mechanism, but the current source already links it explicitly under “Relation to oracle hardening.”
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) — the source is an instance of its broader claim, but the existing readable-artifact, oracle-strength, and spec-mining links already provide the useful classification and mechanism; another generalisation edge would add little traversal value.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — rich failure evidence helps manufacture better checks, but it governs proposal formation rather than the source's retained selection environment; the target itself treats these as orthogonal bottlenecks.
- [Autocontext](../../../../agent-memory-systems/reviews/autocontext.md) — generated validators re-enter later runs, but the review does not establish failure-to-regression-obligation promotion as directly as Auto Harness, and retaining both would duplicate the same external-system reader need.
- [Lessons from building AI agents for financial services](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) — reports a large test corpus and regression gate, but does not show that observed failures progressively became new maintained checks; the evidence is also self-reported.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) — already links inbound and explicitly says its ledger shows a fixed selection environment rather than measured growth.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) — maps the same episode the source already cites through the observed causal-trace document; a second reference link would duplicate evidence.
- [Exo](../../../../agentic-systems/reviews/exo.md) — contains fixed acceptance tests and useful oracle-domain boundaries, but not a retained failure-derived check corpus.
- [Review gate](../../../../types/review-gate.md) — defines one model-judged check and explicitly denies it reject-capable enforcement authority; it is a contract for a check, not evidence of accumulation.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — composes multiple existing checks for decorrelation, but neither manufactures nor retains new checks from failures, so it does not operationalise the source claim.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — add under “Feedback and signal quality” or a compact oracle-learning subgroup: the source explains how deployment failures become durable evaluation capacity and already carries the tag.
- [Learning theory](../../../../tags/learning-theory-README.md) — no direct entry recommended; its `covered_by` mark deliberately routes this note through the deploy-time-learning child head.

## Synthesis Opportunities

None. The source already supplies the higher-order bridge among failure-derived checks, exhaustive enforcement, domain-scoped warrant, and corpus costs; the surrounding notes separately own proposal diagnostics, oracle hardening, and relaxing.

## Maintenance Observations

- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) and [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) still use the former footer link text “Oracle accumulation improves the selection environment for every later candidate.” Their paths resolve, but the displayed title should be updated to the current scoped H1, “Oracle accumulation improves selection for later candidates in its maintained domain.”

## Flags

- None.
