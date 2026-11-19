---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/weakly-discriminated-qualities-tend-to-be-underselected.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Weakly discriminated qualities tend to be underselected

**Source:** [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md)

## Discovery Trace

**Setup and authorisation:**

- Verified the source at SHA-256 `f344a799111458dd4984ef7733ee768aa54b9ebcd6a137fab1eb10329a265c36`, then read it in full after reading the connect-report type contract.
- Read `kb/notes/COLLECTION.md` before prospecting. Its label table authorizes local destinations `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `work` is excluded. The reserved `external` destination is authorized only for already-known targets.
- Read the destination heads `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`.
- Read the source's four matching tag heads: `learning-theory-README.md`, `llm-reliability-README.md`, `evaluation-README.md`, and `self-improving-systems-README.md`. None declares `complete: true`; `learning-theory-README.md` declares only `covered_by`, so no by-tag scan was skipped.
- External prospecting was skipped because the user supplied no external target and no already-known external target was present in loaded context.

**Complete title and description surfaces:**

- Generated each complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes 354, reference 135, agent-memory-systems 173, agentic-systems 12, sources 504, instructions 44.
- Enumerated each destination with `rg '^description:' kb/<destination>/ --glob '*.md'`: notes 351 lines, reference 133, agent-memory-systems 171, agentic-systems 10, sources 440, instructions 97.
- Ran the by-tag description pipeline for every source tag in every authorized destination: `rg -l "^tags:.*\\b${tag}\\b" kb/<destination> --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. Match counts by destination for `learning-theory` / `llm-reliability` / `evaluation` / `self-improving-systems` were notes 116/31/17/40, reference 1/0/2/3, agent-memory-systems 1/0/0/0, agentic-systems 0/0/0/4, sources 2/0/0/0, and instructions 0/0/0/0.
- These were lexical repository searches, so no semantic-search score applies.

**Notes:**

- Body queries included `rg -n -i -m 6 'underselect|selection (pressure|asymmetry)|unequal (discrimination|enrichment)|weakly discriminat' kb/notes --glob '*.md'`, `rg -n -i -m 6 'proposal[- ]selection|candidate (set|distribution)|reject-capable|acceptance rule' kb/notes --glob '*.md'`, `rg -n -i -m 6 'generation failure|activation failure|selection failure|operative oracle|oracle (strength|asymmetry|discrimination)' kb/notes --glob '*.md'`, and `rg -n -i -m 6 'maintainability|delayed quality|future change|compounding|accumulat' kb/notes --glob '*.md'`.
- Focused follow-up queries included `rg -n -i -m 8 'oracle asymmetr|operative oracle|underselect|selection failure|generation failure|activation failure|weakly (verified|discrimin)|maintainability oracle' kb/notes/ --glob '*.md'`, `rg -n -i -m 8 'candidate.{0,30}selection|proposal.selection|accept.{0,30}retent|selection.{0,30}retent|accepted.{0,60}(later|starting|context|training)|false-positive acceptance' kb/notes/ --glob '*.md'`, and `rg -n -i -m 8 'pairwise|decorrelat|calibrat.{0,30}(outcome|later|effect)|proxy agreement|delayed outcome|later change|change cost|quality signals' kb/notes/ --glob '*.md'`.
- Kept the loop-anatomy and oracle-strength foundations, the false-positive terminal-filter mechanism, the activation diagnostic contrast, two applied composite-oracle designs, oracle accumulation, and the proximate-target extension. Rejected warranted-autonomy as a useful but one-hop consequence, diagnostic richness as the proposal-evidence rather than selection side, and the promotion/activation note as already inbound and covered by the more direct activation edge.
- Followed the proposal-selection note into false-positive acceptance, oracle strength, behavioral authority, and cumulativity; followed contextual activation into elicitation and the existing Bug That Shipped evidence; followed the maintainability-oracle note into HGM, diagnostic richness, pairwise calibration, KB quality signals, and SlopCodeBench; followed oracle accumulation into warranted autonomy and spec mining. These one-hop passes established distinct roles rather than a keyword cluster.

**Reference:**

- Body queries included the four general patterns above against `kb/reference/` plus `rg -n -i -m 8 'quality check.{0,40}(placement|cost|false positive)|semantic gate.{0,40}calibrat|selection.{0,30}(evaluation|retention)' kb/reference/ --glob '*.md'`.
- Kept the semantic-gate calibration proposal because its documented zero-firing known-positive case gives a bounded Commonplace instance of an oracle that produces plausible output without discriminating the target defect. Rejected ADR 005: it routes checks by cost and false-positive tolerance but does not establish unequal discrimination or selection enrichment. The full-improvement closure record was also rejected because it establishes reassessment and a stopping rule, not a per-quality selection result.
- Followed the calibration proposal into error correction, evaluation phase-gating, accepted-edit limits, gate learning, and trajectory-aware evaluation. Those neighbors refine calibration mechanics but do not need separate source edges.

**Agent-memory systems:**

- Body queries included the four general patterns above against `kb/agent-memory-systems/` plus `rg -n -i -m 8 'evaluation-gated|benchmark-frontier|parent selection|trace-judged|judge.{0,30}(write|promotion)|score-gated|benchmark performance' kb/agent-memory-systems/ --glob '*.md'`.
- No direct survivor. Agentic Harness Engineering demonstrates benchmark-gated artifact learning but does not measure the weakly selected qualities it explicitly excludes, so HGM is the cleaner empirical selection-target case. SkillWeaver exposes strong shape checks beside weak behavioral checks but likewise supplies no differential enrichment result. The Exo subsystem review is an older, narrower duplicate of the current whole-system analysis kept below.
- Followed Agentic Harness Engineering into diagnostic richness and later benchmark evaluation, SkillWeaver into oracle strength and task-time behavior, and the Exo review into the whole-system analysis; the latter supplied the strongest non-duplicate path.

**Agentic systems:**

- Body queries included the four general patterns above against `kb/agentic-systems/` plus `rg -n -i -m 8 'selection validity|versioned more strongly|mandatory semantic evaluation|later-episode outcome feedback|smoke gate|shape oracles|usefulness oracles' kb/agentic-systems/ --glob '*.md'`.
- Kept Exo: its reject-capable gate strongly checks build, test, manifest, schema, and loadability properties while explicitly failing to discriminate judgment quality and tool usefulness. This is a direct system-level instance of oracle asymmetry, though not a measured prevalence test of the source's statistical conjecture.
- Rejected Autogenesis as a redundant versioning-strong/selection-weak case after Exo, and Compound Engineering because the target already carries software-factory evidence and its omitted semantic lesson gate supplies no differential outcome comparison.
- Followed Exo into its memory-subsystem review, proposal-selection anatomy, warranted autonomy, and self-improving-system placement; these links confirmed that the source would add a distinct selection-pressure explanation rather than repeat Exo's existing autonomy analysis.

**Sources:**

- Body queries included the four general patterns above against `kb/sources/` plus `rg -n -i -m 8 'weak parent-selection signal|generation-evaluation gap|incumbent survival|acceptance criteria|later change cost|delayed accumulated-defect' kb/sources/ --glob '*.md'`.
- Kept HGM because it measures a selection-target mismatch between immediate benchmark performance and lineage productivity, bounding the source's requirement that an oracle be directionally aligned. Kept Autoreason because its gains concentrate where usable alternatives exist but comparative selection remains weak, while preserving the caveat that it does not hold one per-quality candidate distribution fixed.
- Rejected NLAH because its module ablations change process structure and likely activation/generation as well as evaluation; its evaluator-alignment result is benchmark-bound and partly post-hoc. Rejected SlopCodeBench as a direct source edge because it creates a delayed maintainability signal but does not close a proposal-selection loop; it remains reachable from the maintainability-oracle note that already states this boundary.
- Followed HGM into DGM and Meta-Harness, separating selection-target alignment from diagnostic richness. Followed Autoreason into pairwise judging, error correction, and synthesis-versus-selection. Those neighborhoods support the synthesis opportunity below without creating redundant direct edges.

**Instructions and reverse direction:**

- Body queries included the four general patterns above against `kb/instructions/` plus `rg -n -i -m 8 'blind judge packets|borda count|incumbent.*first-class|incumbent win streak|conservative tie' kb/instructions/ --glob '*.md'`.
- Read the complete `cp-skill-revise-autoreason` instruction and `kb/instructions/COLLECTION.md`. Kept it as a rare `operationalized-from` candidate: the procedure fixes candidate roles, blind fresh judges, Borda aggregation, incumbent-favoring ties, hard prechecks, and a stopping condition. Its independent return edge fits the instruction collection's meta-reader-only `rests-on` rule.
- Rejected `run-full-improvement-pass-on-note.md` as too broad: it composes many review surfaces but is already grounded through error-correction and closure records, whereas AutoReason directly exposes candidate generation, comparison, and survival.
- Backlink query `rg -n 'weakly-discriminated-qualities-tend-to-be-underselected' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` found existing inbound links from `warranted-reader-update-is-the-objective-of-substantive-writing.md`, `promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md`, `a-proximate-target-is-checked-for-achievement-not-for-warrant.md`, and `brainstorming-maintainability-oracles-for-agentic-development.md`. These already-authored edges were not re-reported as reverse-edge candidates.

**Path verification:**

- Verified with `test -f` all 13 kept connection paths, 5 bidirectional targets, 11 named rejected paths, and 3 index paths immediately before writing this report; every path existed.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **grounds**: defines the reject-capable selection architecture and operative-retention condition within which unequal discrimination can produce underselection and later accumulation.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **grounds**: supplies the hard/soft/interactive/delayed oracle vocabulary and defines the discriminative strength whose unequal effect on accepted candidates the source develops.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- **mechanism**: explains why errors admitted by the terminal acceptance filter become behavior-shaping retained state while rejected generated errors do not.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **contrasts**: separates activation failure, where available quality knowledge never shapes proposal or review, from selection failure, where usable candidates appear but the operative oracle does not favor them.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) -- **extends**: turns the motivating maintainability case into an explicit quality target, evidence surfaces, candidate-set experiment, calibration ladder, and narrow-authority policy.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- **extends**: develops the source's KB example as a composite-oracle design space while exposing correlation, Goodhart, link-noise, and agent-use failure modes.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- **extends**: shows how a retained failure check changes the selection pressure facing later candidates, while bounding that gain by coverage, monitoring, and proxy rot.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **extends**: applies the source's selection asymmetry one level up, where a strongly checked target can outcompete the delayed objective it was chosen to serve.
- [Proposal: Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) -- **evidenced-by**: documents a bounded case in which a semantic gate produced articulate verdicts while missing known positives, corroborating weak discrimination without claiming downstream enrichment.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **evidenced-by**: its reject-capable self-modification gate strongly discriminates build, test, manifest, schema, and loadability properties while explicitly leaving judgment quality and tool usefulness weakly checked.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- **evidenced-by**: immediate benchmark performance mis-ranks lineage productivity, demonstrating that even precise selection can miss the quality and horizon actually wanted when the oracle is not directionally aligned.
- [Ingest: Autoreason: Self-Refinement That Knows When to Stop](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- **evidenced-by**: blind comparative judging and incumbent survival help most where useful alternatives can be generated but selection remains a material bottleneck.
- [cp-skill-revise-autoreason](../../../../instructions/cp-skill-revise-autoreason/SKILL.md) -- **operationalized-from**: fixes a candidate set, blind fresh judges, Borda aggregation, conservative ties, hard prechecks, and an incumbent-survival stop rule for a concrete revision loop.

## Bidirectional Candidates

- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) <-> source -- **extends (candidate→source)**: the source develops terminal-filter error into a statistical prediction about which qualities gain less when the filter discriminates dimensions unequally.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source -- **contrasts (candidate→source)**: the return path gives readers a clean diagnostic fork between knowledge that never activates and active candidate quality that loses at acceptance.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) <-> source -- **grounds (candidate→source)**: underselection supplies the selection-pressure reason a KB needs discriminating signals rather than a larger basket of uncalibrated proxies.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) <-> source -- **grounds (candidate→source)**: the source states the unequal-selection problem whose recurrence the accumulated-check mechanism addresses.
- [cp-skill-revise-autoreason](../../../../instructions/cp-skill-revise-autoreason/SKILL.md) <-> source -- **rests-on (instruction→source)**: the procedure's separate blind selection layer and incumbent fallback depend on distinguishing production of plausible revisions from reliable selection of an improvement.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- a genuine consequence of weak discrimination, but already one hop away through the kept maintainability-oracle and oracle-accumulation notes.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- distinguishes proposal evidence from selection evidence; retained for the synthesis opportunity rather than forced into a direct edge about selection asymmetry.
- [Promotion selects for unreliable activation, and the regress ends only at an external terminator](../../../../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) -- already links to the source and is reached from the kept activation contrast; a reciprocal source edge would duplicate that path.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- measures benchmark-gated harness improvement but does not measure the weak qualities it says the benchmark excludes; HGM more cleanly isolates the selection-target mismatch.
- [SkillWeaver](../../../../agent-memory-systems/reviews/SkillWeaver.md) -- exposes strong shape checks and weak future-task verification, but supplies no accepted-population enrichment comparison.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- another strong-retention/weak-selection-validity case, rejected as redundant after the more explicit current Exo analysis.
- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- module ablations alter process structure and likely activation or generation as well as evaluation; the benchmark-alignment interpretation does not isolate selection.
- [Ingest: Why Software Factories Fail: Benchmarking the new frontier](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) -- creates delayed maintainability evidence but does not close a proposal-selection loop; it remains available through the kept maintainability-oracle note.
- [005-quality-check placement](../../../../reference/adr/005-quality-check-placement.md) -- routes checks by determinism, cost, and false-positive tolerance but does not establish differential discrimination or enrichment.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) -- a broad review composition whose direct reader need is closure over transformed bytes, not the source's per-quality selection mechanism.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- a specific conclusion-agreement evaluator pathology, but the source's existing automation-boundary link and kept oracle-strength edge already carry its relevant discrimination lesson.

## Index Membership

- [LLM reliability](../../../../tags/llm-reliability-README.md) -- candidate Oracle Theory entry: the source supplies the missing selection-pressure consequence of unequal oracle discrimination beside oracle strength, activation, automation boundaries, and error correction.
- [Evaluation](../../../../tags/evaluation-README.md) -- candidate Notes entry: the source is an explicitly refutable statistical conjecture with fixed-candidate and stronger-oracle test predictions.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- candidate Update Architecture entry: the source explains how evaluation inside proposal-selection pathways biases which qualities operative retention accumulates.

## Synthesis Opportunities

The source, [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), and [Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) imply three independent outer-loop evaluation surfaces: **oracle discrimination** determines which candidate wins, **selection-target alignment** determines whether the score represents the quality and horizon actually wanted, and **diagnostic richness** determines what the next proposer can infer from the result. [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) already instantiates the triad in one code-maintenance domain; a future synthesis would need to justify the domain-general form rather than merely restate that application.

## Maintenance Observations

- The prose scan list in `kb/notes/COLLECTION.md` names `notes`, `reference`, `agent-memory-systems`, `sources`, and `instructions` but omits `agentic-systems`, while the authoritative label table explicitly authorizes `evidenced-by`, `derived-from`, `abstracted-from`, and `see-also` to `agentic-systems`. This run followed the table and found Exo there; the prose/table mismatch is a collection-contract maintenance signal.

## Flags

None
