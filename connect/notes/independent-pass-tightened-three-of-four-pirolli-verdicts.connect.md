---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: An independent pass tightened three of four Pirolli grounding verdicts

**Source:** [An independent pass tightened three of four Pirolli grounding verdicts](../../../../notes/evidence/independent-pass-tightened-three-of-four-pirolli-verdicts.md)

## Discovery Trace

All discovery was repository-local. No semantic scores were available. Existing authored links from the source were used as traversal neighborhoods and were not re-proposed under `Connections Found`.

### `kb/notes/`

**Curated heads:**

- Read [`README.md`](../../../../notes/README.md), [`evaluation-README.md`](../../../../tags/evaluation-README.md), and [`kb-maintenance-README.md`](../../../../tags/kb-maintenance-README.md). Neither tag README declares `complete: true`, so both by-tag scans were run. The source is tagged for both indexes but appears in neither curated head.

**Title and description scans:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` over the complete 367-heading title surface.
- Ran `rg '^description:' kb/notes/ --glob '*.md' | rg -i 'contamin|blind|independ|comparison|contrast|ablation|decorrelat|source|ground|verdict|evaluation|evidence|judge|attribut|isolation'`. This surfaced the causal-contrast, contamination, warrant-granularity, subrole-verification, prompt-variation, and bounded-evidence neighborhoods.
- Ran `rg -l '^tags:.*\bevaluation\b' kb/notes/ --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''` and the corresponding query for `kb-maintenance`. The paired five-link-cap evidence note was the strongest additional candidate from these tag surfaces.

**Body searches:**

- `rg -n -i 'bilateral isolation|source-blind|target-blind|context contamination|over-attribution|false narrowing|blind judge|independent pass|comparison procedure|same context' kb/notes/ --glob '*.md'` — found the direct contamination analogy, the causal-isolation conjecture, and the exact Pirolli case.
- `rg -n -i 'independent.*(judge|comparison)|blind.*judge|role decomposition|separate.*(source|target)|frozen.*(claim|representation)|over-attribution|false narrowing|comparison contamination' kb/notes/ --glob '*.md'` — added the summary-sufficiency failure route and confirmed that no other note states bilateral source/target reconstruction as an established mechanism.

**Candidate evaluations:**

- Kept [`an-experiment-identifies-only-the-contrast-it-actually-runs.md`](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): the source explicitly changed roles, prompts, and intermediate representation together, so its own causal limit is one local instance of the treatment-grain rule.
- Kept [`borrowed-patterns-transfer-only-over-shared-mechanism.md`](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md): the C1-C3 dispositions separate Pirolli's shared proximal-cue/distal-source structure from stronger local navigation and cost claims that the source does not establish.
- Kept [`theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md`](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md): the source's central result is that document-level thematic fit did not distribute uniformly across four claim-level verdicts.
- Kept [`an-insufficient-summary-precedes-the-source-rather-than-replacing.md`](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md): it supplies a concrete failure route for the source's unobserved false-narrowing risk when a frozen source reconstruction is insufficient for the comparison question but the comparator cannot reopen the source.
- Kept [`a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md`](../../../retained/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md): both are bounded grounding-method cases with changed verdicts, but the five-link assay varies evidence coverage under much tighter matching while this source varies a role/prompt/representation bundle.
- Rejected [`context-contamination-operates-below-an-agents-compliance-reasoning.md`](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md): it establishes stance drift after exposure in a different task, but this source does not identify contamination as the cause of its verdict change; a `mechanism` edge would over-attribute the case.
- Rejected [`process-structure-and-output-structure-are-independent-levers.md`](../../../../notes/process-structure-and-output-structure-are-independent-levers.md): it classifies only part of the changed bundle, while the kept experimental-contrast note states the exact attribution limit.
- Rejected [`checked-outcome-licenses-episode-retention-not-abstraction.md`](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md): it shares the one-case-to-rule boundary, but the source already preserves that boundary and is not abstracting a producing-process explanation from a successful task outcome.
- Rejected [`topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md): its claim concerns scaling, decomposition, and verifier decorrelation; this source neither tests that chain nor identifies isolation as causal.
- Rejected [`narrowing-bought-to-survive-review-is-paid-for-in-content.md`](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md): its failure is analytic narrowing by subject redefinition, not the source-reconstruction omission or literalism risk named here.

**Link following:**

- Followed the source's existing links through [`Agents navigate by deciding what to read next`](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md), [`linking theory`](../../../../notes/linking-theory.md), [`candidacy evidence licenses escalation to assessment, not acceptance`](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md), [`reasoning production is not reasoning evaluation`](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md), and the Pirolli ingest. Those edges are already authored and were not re-proposed.
- Followed the candidacy note to the warrant-granularity note. The source adds a direct claim-by-claim case, so that target survived re-filtering despite the existing one-hop route.
- Followed the inbound literature-grounding proposal to the borrowed-pattern transfer rule, the narrowing warning, ADR 081, and the operative assessment instruction. The shared-mechanism rule, ADR, and instruction survived; the narrowing note did not.
- Followed the five-link-cap evidence note through its matched-arm and repeat-baseline design. Its useful relationship is contrast rather than shared cause: coverage truncation and cross-side representation contamination are different threats to a grounding verdict.

### `kb/types/`

- Read [`README.md`](../../../../types/README.md), ran `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'` over 10 headings, and ran `rg '^description:' kb/types/ --glob '*.md'`.
- Ran `rg -n -i 'comparison|isolation|source|ground|verdict|evidence|claim grain|blind' kb/types/ --glob '*.md'`. The note type declares the source's `has-comparison` and `has-external-sources` traits, but no global type contract explains, tests, or operationalizes its comparison-method claim. No candidate passed the articulation test.

### `kb/reference/`

- Read [`README.md`](../../../../reference/README.md), ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` over 154 headings, and ran `rg '^description:' kb/reference/ --glob '*.md' | rg -i 'literature|ground|source|claim|comparison|isolation|review|evidence|disposition'`.
- Ran `rg -n -i 'bilateral isolation|source-blind|target-blind|claim-grained|literature assessment|literature-assessment|source reconstruction|comparison procedure' kb/reference/ kb/instructions/ --glob '*.md'`. Kept ADR 081 as a reverse-edge candidate because its conditional diagnostic decision depends on the source but currently names only an unlinked "bounded Pirolli rerun."
- The inbound [`operational-destinations-for-literature-grounding-findings.md`](../../../reference/proposals/operational-destinations-for-literature-grounding-findings.md) already links the source and was not re-proposed. Its current text conflicts with the adopted ADR and instruction; that is recorded under `Maintenance Observations` rather than converted into another connection.
- Rejected [`source-adoption-policy.md`](../../../../reference/source-adoption-policy.md): it gives broader Commonplace source-transfer policy, while the kept borrowed-pattern note states the exact shared-mechanism boundary exposed by the four Pirolli verdicts.

### `kb/agent-memory-systems/`

- Read [`README.md`](../../../../agent-memory-systems/README.md), ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` over 173 headings, and filtered the description surface with `rg '^description:' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md' | rg -i 'blind|independ|judge|isolat|compar|critic|review|verification|source|ground|evidence'`.
- Ran `rg -n -i 'blind judge|blind comparative|fresh judge|source-blind|target-blind|context isolation|independent judge|comparison contamination' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`. [`AI Research OS Workshop`](../../../../agent-memory-systems/reviews/ai-research-os-workshop.md) isolates downstream writers from raw evidence through source pages, but its review measures neither source-page faithfulness nor resulting comparison verdicts, so it was rejected.

### `kb/agentic-systems/`

- Read [`README.md`](../../../../agentic-systems/README.md) and ran the title, description, and body queries recorded above over its 12-heading surface. No whole-system analysis tests bilateral source/target representation, and no candidate passed the articulation test.

### `kb/sources/`

- Read [`README.md`](../../../../sources/README.md) and ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` over the complete 320-heading source surface.
- Filtered titles with `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' | rg -i 'search|information|forag|relevance|citation|evidence|science|reason|query|judg|source|scent|retriev|discov'` and descriptions with `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'search|information forag|relevance|query|source selection|citation|discovery|evidence|judg|confirmation|bias'`.
- Ran `rg -n -i 'blind comparative|fresh.{0,40}judge|source-blind|target-blind|prompt.{0,40}bundle|context.{0,40}bias|independent.{0,40}judge|comparison.{0,40}contamin' kb/sources/ --glob '*.md'`. This surfaced Autoreason, RECV, position bias, and context-bias sources.
- Ran `git log --since='2026-08-23' --name-only --pretty=format: -- kb/sources | sort -u | rg -i 'search|retriev|query|pirolli|teevan|tombros|maron|kuhns|robertson|sparck|salton|bates|belkin|broder|croft|relevance|information|forag|berry|marchionini|ingwersen|saracevic|kochen|cooper|swanson|vakkari|harter|spink|white|card|chi'` to identify the newly ingested classic-search subset.
- The exact [`Pirolli ingest`](../../../../sources/pirolli-proximal-information-scent-distal-content.ingest.md) is already linked from the source and remains its direct external evidence route.
- Rejected [`The Perfect Search Engine Is Not Enough`](../../../../sources/teevan-perfect-search-engine-orienteering.ingest.md) and [`Advantages of Query Biased Summaries in Information Retrieval`](../../../../sources/tombros-sanderson-query-biased-summaries.ingest.md): both strengthen the underlying navigation and pointer-design cluster, but neither bears on whether combined versus isolated source comparison changes support verdicts.
- Rejected [`Autoreason`](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md): fresh blind judges are part of its incumbent/revision/synthesis tournament, but the study neither reconstructs source and target independently nor isolates freshness from multiple judges, Borda aggregation, conservative ties, and incumbent survival.
- Rejected [`Assessing LLM Reasoning in Evidence-Based Claim Verification`](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md): its bundled prompt arms are another attribution-limit case, but the general experimental-contrast note is the more direct navigation target and RECV does not test source-comparison contamination.
- Rejected [`Position Bias Benchmark`](../../../../sources/position-bias.ingest.md) and its [`launch thread`](../../../../sources/does-an-llm-keep-the-same-judgment-when-you-swap-the-answer.ingest.md): order swapping shows comparison-format sensitivity, but order was not the changed factor in the Pirolli rerun and these sources do not test bilateral reconstruction.
- Rejected [`Language Models Don't Always Say What They Think`](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md): it supports a general hidden-context-influence mechanism, not the causal interpretation of this confounded source-grounding case.

### `kb/instructions/`

- Read [`README.md`](../../../../instructions/README.md), ran `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` over 49 headings, and ran the complete `rg '^description:' kb/instructions/ --glob '*.md'` surface.
- The reference/instruction body query above found [`assess-a-claim-bearing-artifact-against-external-literature.md`](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md). Kept it because it gives bilateral isolation explicit triggers, fresh source/target/comparison roles, frozen intermediate artifacts, a stop on missing information, and a two-sided over-attribution/false-narrowing check while refusing to make the control routine.
- Rejected [`cp-skill-revise-autoreason`](../../../../instructions/cp-skill-revise-autoreason/SKILL.md): it also uses fresh roles and a blind judge, but its target is candidate note revision and incumbent survival, not source-side claim reconstruction or literature disposition.

### Reserved `external`

- The notes contract authorizes already-known external targets, but the only supplied external source is represented by the tracked Pirolli ingest already linked from the source. Open-web prospecting was skipped as required.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **exemplifies**: the Pirolli rerun is a bundle-level contrast because fresh roles, prompts, and intermediate representation changed together; this is the general rule behind the source's refusal to attribute the tighter verdicts to isolation alone.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — **exemplifies**: C3 retains the shared proximal-cue/distal-source structure while withholding the target's surrounding-context, tractability, and avoided-load additions, and C1-C2 likewise stop surface resemblance from granting source warrant.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — **exemplifies**: the four separate verdicts show why thematic source fit and document-level overlap cannot distribute warrant across independently usable target claims and scopes.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **mechanism**: a frozen source reconstruction that cannot license the comparison at the required reliability can omit a distributed claim; forcing the comparator to stop at that representation is a concrete route to the false narrowing the source says remains unmeasured.
- [A five-link cap missed four grounding findings in twelve reviews](../../../retained/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) — **contrasts**: both cases show grounding verdicts changing with procedure, but the five-link assay varies evidence coverage under matched target snapshots and repeat controls while the Pirolli case varies role, context, prompt, and representation together.
- [Assess a claim-bearing artifact against external literature](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) — **operationalized-from**: the procedure turns the bounded result into a conditional diagnostic branch with exact triggers, three fresh roles, frozen representations, and checks for both over-attribution and false narrowing without treating bilateral isolation as a default.

## Bidirectional Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) ↔ source — return **evidenced-by** edge: the Pirolli rerun is a local Commonplace case where a changed bundle produced a different result and the artifact correctly withholds component-level causal attribution.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) ↔ source — return **evidenced-by** edge: the C1-C3 disposition table supplies a concrete source-adoption case in which shared mechanism licenses only part of a tempting cross-domain transfer.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) ↔ source — return **evidenced-by** edge: three tightened claim-level verdicts show the operational consequence of refusing to spread support from a source or document as a whole.
- [A five-link cap missed four grounding findings in twelve reviews](../../../retained/a-five-link-cap-missed-four-grounding-findings-in-twelve-reviews.md) ↔ source — return **contrasts** edge: the symmetric path would keep the two observed grounding-method risks distinct—evidence truncation versus cross-side representation—while exposing the more tightly matched assay design the Pirolli follow-up needs.
- [Assess a claim-bearing artifact against external literature](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) ↔ source — return **rests-on** edge: a meta-reader maintaining the conditional bilateral-isolation branch needs the exact bounded case and causal limit behind the instruction's explicit refusal to make it routine.

## Reverse-edge Candidates

- [ADR 081 — Literature disposition is explicit and claim-grained](../../../../reference/adr/081-literature-disposition-is-explicit-and-claim-grained.md) → source — **rests-on**: the accepted decision makes bilateral isolation a conditional diagnostic because this rerun tightened three verdicts but changed several procedural factors and did not test false narrowing; the ADR currently describes that evidence without linking its durable record.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — a plausible analogy, but retaining it as the source's mechanism would contradict the source's own bundled-treatment limit.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) — classifies only part of what changed and adds less navigational value than the kept causal-contrast rule.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — shares a one-case-to-rule warning but concerns outcome-checked episodes rather than source-support adjudication.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — uses isolation in a broader scaling hypothesis that this case cannot test.
- [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — its analytic-redefinition failure is not the source-summary omission risk here.
- [Autoreason](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) — fresh blind judging appears inside a materially different refinement tournament and does not establish bilateral reconstruction.
- [Assessing LLM Reasoning in Evidence-Based Claim Verification](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) — another bundled-comparison limit, already better reached through the general experimental-contrast note.
- [Position Bias Benchmark](../../../../sources/position-bias.ingest.md) — establishes order sensitivity, a factor not varied in the Pirolli rerun.
- [The Perfect Search Engine Is Not Enough](../../../../sources/teevan-perfect-search-engine-orienteering.ingest.md) — supports the underlying navigation topic, not the source-comparison method claim.
- [Advantages of Query Biased Summaries in Information Retrieval](../../../../sources/tombros-sanderson-query-biased-summaries.ingest.md) — supports query-specific pointer design, not the source-comparison method claim.
- [AI Research OS Workshop](../../../../agent-memory-systems/reviews/ai-research-os-workshop.md) — describes source-page isolation without measuring its faithfulness or effect on comparison verdicts.
- [cp-skill-revise-autoreason](../../../../instructions/cp-skill-revise-autoreason/SKILL.md) — shares fresh-role and blind-judge structure but operates on note revision rather than literature grounding.

## Index Membership

- [Evaluation](../../../../tags/evaluation-README.md) — the source is a bounded empirical result about comparison procedure, with an explicit candidate control and prospective-test obligation.
- [KB maintenance](../../../../tags/kb-maintenance-README.md) — the source records a source-grounding failure mode and the conditional maintenance control now used when comparison independence is challenged.

## Synthesis Opportunities

None

## Maintenance Observations

- [`Operational destinations for literature-grounding findings`](../../../reference/proposals/operational-destinations-for-literature-grounding-findings.md) still says the multistage path has only asymmetric protection, treats an operative bilateral-isolation branch as unresolved, and says the proposal closes when such a branch is named. [ADR 081](../../../../reference/adr/081-literature-disposition-is-explicit-and-claim-grained.md) and the [literature-assessment instruction](../../../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) now define that conditional branch. The proposal needs a lifecycle disposition: archive it if that satisfied its closure condition, or revise it to retain only the narrower open question of whether a matched prospective test should make isolation routine.

## Flags

- Unresolved proposal-state tension: do not add a new source-to-proposal navigation edge until the proposal is reconciled with ADR 081 and the operative instruction.
