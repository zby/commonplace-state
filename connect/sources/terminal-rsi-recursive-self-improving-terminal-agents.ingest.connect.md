---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md"
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Ingest: Terminal-RSI: Recursive Self-Improving Terminal Agents

**Source:** [Ingest: Terminal-RSI](../../../../sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md)

The ingest already carries ten authored outbound links (all verified to exist): checked-outcome episode retention, exact implementation, LHTB ingest, computationally directed self-improvement, self-improving boundary cases, compounding test, representational-form coevolution, SkillRL ingest, agent-optimizers ingest, learning inside a fixed decomposition. This report lists only *additional* candidates.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section. Destinations: notes, reference, agent-memory-systems, agentic-systems, tags, sources; excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (notes, agent-memory-systems), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `abstracted-from`/`rests-on` (notes), `defined-in` (notes/definitions), `see-also` (sparingly), `derived-from` (external, already present). External prospecting skipped (origin URL already authored).

**Description listing scan:**
- `rg -N --no-heading '^description:' sources --glob '*.ingest.md' | rg -i 'self-impro|reward|RL\b|reinforcement|verifier|terminal|STaR|bootstrap|rejection|critic|partial credit|RSI'` -- ~100 hits. Flagged: `whale-joint-harness-weight-optimization` (alternating weight/harness phases with schedule controls), `cedar-grpo-process-aware-rl-abductive-reasoning` (process rewards in GRPO), `huxley-godel-machine-...` (immediate benchmark score as weak selection signal), `language-models-need-sleep-...` (self-distillation into weights), `self-harness-harnesses-that-improve-themselves` (Terminal-Bench), `frontis-ma1-...`, `giants-...`, `on-the-fragility-of-self-improving-agents`.
- Description reads for notes: `oracle-strength-spectrum`, `warranted-autonomy-is-bounded-by-oracle-domain`, `the-boundary-of-automation-is-the-boundary-of-verification`, `error-correction-works-above-chance-oracles-with-decorrelated-checks`, `a-proposal-selection-loop-requires-search-evaluation-and-retention`, `trace-extracted-memory-earns-authority-per-operation-not-at-capture`, `an-insufficient-summary-precedes-the-source-rather-than-replacing`, `an-experiment-identifies-only-the-contrast-it-actually-runs`, `the-deployed-system-not-the-model-is-the-unit-of-learning`, `weakly-discriminated-qualities-tend-to-be-underselected`, `an-omitted-loop-function-and-a-frozen-one-need-different-repairs`, `oracle-accumulation-improves-the-selection-environment`.
- agentic-systems: `reviews-archive/lhtb.md`, `reviews-archive/openrsi.md`, `reviews-archive/modularrsi.md`, `reviews-archive/rsiagent.md` descriptions.

**Topic indexes:**
- `kb/tags/COLLECTION.md`: participating collections are notes, reference, instructions, agent-memory-systems, agentic-systems; sources do not participate, so tag heads (self-improving-systems `complete: true`, trace-learning, evaluation, continual-learning) are routing aids only, not membership targets.

**Body search:**
- `rg -l -i 'partial credit|reward hacking|specification gaming|verifier' notes/` -- 36 files; kept oracle cluster for evaluation.
- `rg -l -i 'STaR|ReST|rejection sampling|self-distill|trajectory rewrit|runbook' notes sources agentic-systems` -- mostly agentic-systems keyword noise; no note on rewrite-then-reverify retention beyond the already-linked checked-outcome note.
- `rg -l -i 'terminal-bench|terminal bench|PPO|GRPO|reward shaping|process reward|dense reward' sources notes agentic-systems/...` -- surfaced cedar-grpo, contextpilot, s3gym, self-harness.
- `rg -l -i 'partial (credit|progress|completion)|shaped reward|reward shaping|proxy metric|metric gaming|teaching to the test' notes` -- factory-learning-mechanisms, oracle-strength-spectrum, boundary-of-automation, insufficient-summary; the last uses "partial credit" in an unrelated (summary-substitution) sense.
- `rg -l -i 'selected on|selection on the test|benchmark feedback|held-out|checkpoint selection|...' notes` -- weakly-discriminated-qualities, omitted-vs-frozen loop function, compounding (already linked), oracle-accumulation.
- `rg -n -i 'partial|process reward|dense' sources/cedar-grpo-...` -- confirmed CEDAR reports held-out gains from composite process reward.
- `rg -n -i 'alternat|control|compute' sources/whale-...` -- confirmed WHALE runs stagewise-vs-alternating and single-axis controls.
- `rg -l 'terminal-rsi' kb/` -- no existing inbound links.

**Link following:**
- Read `weakly-discriminated-qualities-tend-to-be-underselected.md` body: its condition 3 explicitly includes accepted outputs entering the "training signal" of later iterations; Terminal-RSI's verifier-fixed reward is a qualifying loop.
- Read `an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md`: "frozen" = outside the effective update space; human-held reward redesign and checkpoint selection fit, but the already-linked fixed-decomposition and reallocation notes carry this more directly.
- WHALE ingest links to `the-deployed-system-not-the-model-is-the-unit-of-learning` and `an-experiment-identifies-only-the-contrast-it-actually-runs`, which led to those two candidates.
- HGM ingest body: "selection-target alignment is a separate axis from oracle strength" -- matches Terminal-RSI's benchmark-selected retained stages.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **is-evidence-for**: Terminal-RSI changes reward, learning rate, critic initialization and stage order together and compares RSR-then-PPO with a non-compute-matched direct-PPO control; the authors' own list of missing controls (compute-matched alternation, inherited-vs-reset critic, isolated TB-GAE) is a clean case of bundle-to-component attribution the run does not license.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **is-evidence-for**: the Rust–C case (fuzz gates pass while evaluation is delegated to Python) and the 48 all-scenario-pass failures show a training loop whose operative oracle does not discriminate the intended architecture, so reward cannot enrich it; case evidence only, not the note's predeclared enrichment comparison.
- [Whale: joint harness–weight optimization](../../../../sources/whale-joint-harness-weight-optimization.ingest.md) -- **compares-with**: on alternating update phases. Both alternate two update regimes in cycles; WHALE runs stagewise-vs-alternating, single-axis and cadence controls that Terminal-RSI lacks, and WHALE alternates across representational forms (weights vs harness) while Terminal-RSI alternates two weight-update regimes (SFT vs PPO) under a fixed harness.
- [CEDAR-GRPO: process-aware RL](../../../../sources/cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md) -- **compares-with**: on non-outcome reward components. CEDAR reports held-out gains from a composite process reward; Terminal-RSI's offline rescoring shows proportional partial credit giving failures ~50% of reward mass and fixes it by capping partial credit below strict success. Together they bound when shaped credit helps vs misdirects.
- [Huxley–Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- **compares-with**: on selection signal for retained stages. Terminal-RSI retains stages by benchmark score; HGM argues immediate benchmark score is a weak selection signal for long-run improvement. Useful to a reader weighing the "each retained stage consolidates" claim.

## Bidirectional Candidates

- [Long-Horizon-Terminal-Bench ingest](../../../../sources/long-horizon-terminal-bench.ingest.md) <-> source -- **compares-with**: the LHTB ingest left open whether feeding graded partial credit to a learner helps; Terminal-RSI's offline rescoring is the (offline-only) follow-up answer, so the return link closes that open question for LHTB readers.
- [Whale](../../../../sources/whale-joint-harness-weight-optimization.ingest.md) <-> source -- **compares-with**: WHALE readers gain an uncontrolled, larger-scale alternation case that shows what the missing schedule controls cost.

## Reverse-edge Candidates

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) → source -- under notes' rules: cite the Rust–C fuzz-gate case as a bounded illustration (matches the ingest's Recommended Next Action; ground quotes via `cp-skill-ground` first).
- [Computationally directed self-improvement is a fixed-boundary reallocation](../../../../notes/computationally-directed-self-improvement-is-a-reallocation.md) → source -- under notes' rules: a "recursive self-improving" titled system in which reward redesign, learning-rate choice and checkpoint retention remain human.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source -- under notes' rules: stages retained by the same benchmarks used to report gains, with SWR100 (training-disjoint) plateauing after RPR-1.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) → source -- under notes' rules: a weight-training instance of condition 3 (accepted outputs entering the training signal), complementing its software-factory example.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- topically adjacent, but the protected verifier is a hard oracle used as designed; the paper's lesson is coverage of the oracle, which the exact-implementation and weakly-discriminated notes carry more precisely.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- synthesis-level; adding this source adds no distinct mechanism.
- [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- Terminal-RSI's weights-only update with fixed harness fits, but the already-authored fixed-decomposition and representational-form links cover the same point.
- [An omitted loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- human-held reward redesign is "frozen" in this sense, but the reallocation and fixed-decomposition links already carry it; would duplicate.
- [Trace-extracted memory earns authority per operation](../../../../notes/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) -- RSR's rewrite-reverify gate resembles "authority earned per operation", but runbooks are discarded and only weights persist; the checked-outcome link is the better fit.
- [An insufficient summary precedes the source](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- "partial credit" here means summary substitution; the paper's chunk-vs-summarize aside is flagged `just-a-reference` in the ingest.
- [Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- same benchmark family but harness editing, not weights; agent-optimizers link already covers Terminal-Bench staged gains.
- [Language models need sleep](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) -- self-distillation into weights is a loose analogy to RSR; no shared named axis worth a link.
- [LHTB system review (archive)](../../../../agentic-systems/reviews-archive/lhtb.md) -- archived; the LHTB ingest is the live comparison surface.
- `openrsi`, `modularrsi`, `rsiagent` reviews -- harness/program-search RSI systems; "RSI" keyword match only.

## Index Membership

None -- `kb/sources/` is not a participating tag collection (`kb/tags/COLLECTION.md`), and sources have no curated README index entries to add.

## Synthesis Opportunities

Terminal-RSI (partial credit misdirects when unsubordinated), CEDAR-GRPO (process reward helps held-out), and LHTB (partial credit as evaluation detail) together imply a claim not yet stated in notes: non-outcome credit is safe as reward only when subordinated to the outcome gate, and its value as evaluation detail does not transfer to its value as a training signal. Could be folded into `weakly-discriminated-qualities-tend-to-be-underselected` or `oracle-strength-spectrum` rather than spawned as a new note.

## Maintenance Observations

None

## Flags

- Tension: CEDAR-GRPO's positive process-reward result vs Terminal-RSI's offline evidence that partial credit misallocates reward. Not contradictory (different reward constructions, CEDAR is online-trained, Terminal-RSI's evidence is offline rescoring), but a writer citing either should scope accordingly.
- No inbound links to the ingest exist yet (`rg -l 'terminal-rsi' kb/` empty).
