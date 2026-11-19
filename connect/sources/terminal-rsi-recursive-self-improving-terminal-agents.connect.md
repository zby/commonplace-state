---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/terminal-rsi-recursive-self-improving-terminal-agents.md"
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine

**Source:** [Terminal-RSI snapshot](../../../../sources/.snapshots/terminal-rsi-recursive-self-improving-terminal-agents.md)

The source is an immutable snapshot. Every candidate below is for the matching ingest, `kb/sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md`, which did not exist when this report was written. Under the sources contract, the durable `derived-from` edge goes to the external URL `https://arxiv.org/abs/2610.22192`, not to the snapshot.

**Source reading used for judging:** Terminal-RSI is a weight-training pipeline for a 27B terminal agent with five retained stages: Base → RSR-1 → RPR-1 → RSR-2 → RPR-2.
- **RSR (Recursive Self-Rewrite)** keeps only trajectories that pass the protected verifier. It turns each one into a runbook. A reviewer screens the runbook for leakage, and the policy must reproduce the result in a fresh execution. The runbooks are then removed, and only actor supervision is kept.
- **RPR (Recursive Policy-Refine)** is PPO with a critic inherited from the previous stage.
- **Reward evolution:** FDR (Family Dense Reward) is replaced by SPR (Success-Prioritized Reward). The authors report that under FDR, failures received 50.09% of reward mass, and 48 failures passed every scenario check while failing the terminal gate.
- **Limitations the authors state:**
  - no causal controls;
  - checkpoint selection still needs protected validation;
  - "Tests certify enforced requirements only." In the Rust–C case, fuzz tests certify output equivalence while the solution delegates evaluation to Python.
  - "summarization changes the conditioning history", unlike chunking.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links. It authorizes these destinations: notes, reference, agent-memory-systems, agentic-systems, sources, tags, and external for `derived-from`/`see-also`. It excludes `kb/work/` and `kb/instructions/`. Authorized labels by destination:
- notes: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` (notes/definitions only), `see-also`
- sources: `compares-with`, `see-also`
- agentic-systems: `compares-with`, `see-also`

**Tag heads read:** `self-improving-systems` (complete: true), `trace-learning`, `continual-learning`, `evaluation`, and `deploy-time-learning`, from `kb/tags/`. Sources are not a participating tag collection (`kb/tags/COLLECTION.md` participating: notes, reference, instructions, agent-memory-systems, agentic-systems), so no tag-tail rg was needed. I used the head link lists for routing only. I filtered them with `grep -iE 'verif|weight|train|trace|trajector|reward|goodhart|oracle|checker|rl|fine-tun|distill|runbook|summar'`. That surfaced the proximate-target, oracle-domain, compounding, accumulation, retained-artifact, and weight-form candidates.

**Titles listing:** `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | grep -iE 'oracle|verif|reward|train|weight|trajector|trace|self-impro|partial|complet|benchmark|check|test'`. About 80 titles came back. From these I flagged `checked-outcome-licenses-episode-retention-not-abstraction`, `exact-implementation-does-not-validate-a-requirement`, `computationally-directed-self-improvement-is-a-reallocation`, `the-self-improving-system-definition-classifies-its-boundary-cases`, `diagnostic-richness-constrains-outer-loop-learning-quality`, `weakly-discriminated-qualities-tend-to-be-underselected`, `compounding-is-tested-in-later-improvement-not-by-the-accepting-metric`, and `an-accepted-edit-verifies-the-change-not-the-rule`.

**Body search (notes, agentic-systems, reference):**
- `rg -l -i -e 'partial credit|partial progress'`: only the summary-fallback note and a mem0 archive result. Not relevant.
- `rg -l -i -e 'reward hack|Goodhart|proxy (metric|target)'`: verifiability-gradient, boundary-of-automation, quality-signals, and aide2. These are general proxy discussions, weaker than the specific notes below.
- `rg -l -i -e 'verifier coverage|checker coverage|test coverage|certif'`: no note centers on verifier coverage. The coverage point lands on `exact-implementation-does-not-validate-a-requirement`, found through the title scan.
- `rg -l -i -e 'weight(s)?[- ]level|fine-tun|in the weights|model weights'`: constraining-during-deployment, treat-continual-learning-as-representational-form-coevolution, the self-improving-system definition, and reflective-coverage. Kept: the coevolution note.
- `rg -l -i -e 'summari[sz](ation|e) (changes|loses|removes|drops)'`: no hits. A follow-up search for `compaction|summari[sz]` descriptions found only the scheduler-compaction and semantic-sub-goal notes, which are off-axis.
- `rg -l -i -e 'STaR|ReST|generate.filter.train|rejection sampling'`: case-insensitive noise ("ReST" also matches "rest"). No note discusses generate-filter-train.
- `rg -l -i -e 'runbook'`: memory-requirements and workshop-layer notes. These use "runbook" in the human-procedure sense, not as a source of supervision. Rejected.
- `rg -l -i -e 'leakage'`: context-contamination, history-checkable, known-target-benchmarks, and several analysis archives. None of these concerns leakage review of generated supervision.

**Sources destination:**
- `rg -il 'recursive self-rewrite|terminal-bench|RSR|runbook' kb/sources/*.ingest.md` returned 14 hits. Kept: long-horizon-terminal-bench and agent-optimizers-compound-terminal-bench. Considered: toward-measuring-RSI, knowledge-centric-self-improvement, pilot, and automated-benchmark-auditing.
- `rg -l -i 'generate.{0,5}filter|self-generated training|self-training|training data|...|reinforcement learning' kb/sources/*.ingest.md`: kept skillrl-evolving-agents-recursive-skill-augmented-rl. Considered recursive-self-improvement-since-1987 and self-training-llms-through-knowledge-detection.
- `rg -il 'cross-harness|complementary.harness|self-rewrite|T1 terminal|TB-GAE|critic'`: no ingest for the RSR precursor paper (Li et al. [23]) or for T1 [46]. The hits match the generic word "critic".

**Agentic-systems / agent-memory-systems:**
- `rg -l -i 'terminal-bench|reinforcement learning|PPO|GRPO' kb/agentic-systems/reviews kb/agent-memory-systems/reviews`: the hits come from the case-insensitive substring "ppo" (as in "support") and from incidental mentions. No review covers an RL training pipeline for terminal agents.
- The `openrsi` review is in `reviews-archive/`, which is historical. It is not kept.

**Link following:**
- The LHTB ingest already links to `diagnostic-richness` and `oracle-strength-spectrum`. It raises one question and leaves it open: whether partial-credit scores fed to a later learner improve learning. Terminal-RSI is a direct case: it feeds partial credit into PPO reward. This confirmed the LHTB comparison.
- `checked-outcome` → `abstract-an-experience-only-when-you-can-state-the-boundary` and `an-accepted-edit-verifies-the-change-not-the-rule`. RSR's re-execution step fits the checked-outcome note better than either neighbor.
- `computationally-directed-self-improvement-is-a-reallocation` → `the-self-improving-system-definition-classifies-its-boundary-cases` has a row for "model fine-tuned by an external training pipeline". Terminal-RSI is an instance of that row.

## Connections Found

- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **compares-with**: shared axis is what evidence licenses moving from one verified episode to reusable supervision. RSR does not reuse a verified trajectory directly. It rewrites the trajectory into a runbook, gates the runbook for leakage, and counts it only after a fresh public execution passes the verifier again. This is a training-pipeline instance of the note's demand for evidence beyond the single checked outcome, and it uses repeated outcome tests rather than process evidence.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for**: the Rust–C case is concrete local conformance without the intended capability. Exact-output fuzz tests pass, yet evaluation is delegated to Python, so "fuzz-test success establishes tested output equivalence, not a native Rust–C AST execution path". The 48 failures that pass every scenario check but miss the terminal gate show locally satisfied checks failing to compose. Both are case evidence, not a controlled test.
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../../../../notes/computationally-directed-self-improvement-is-a-reallocation.md) -- **is-evidence-for**: the system is titled "recursive self-improving", but by the source's own account humans still make several decision-bearing choices:
  - redesigning the reward from FDR to SPR after seeing later training steps ("The eight later steps were already available when the reward was designed");
  - setting stage-specific learning rates;
  - choosing retained stages over discarded branches.

  Generation and filtering are computational. Humans remain a cut set for evaluation and retention.
- [The self-improving-system definition classifies its boundary cases without ad hoc exceptions](../../../../notes/the-self-improving-system-definition-classifies-its-boundary-cases.md) -- **is-evidence-for**: Terminal-RSI is a live instance of the note's "model fine-tuned by an external training pipeline" case. Whether "self-improving" applies depends on declaring the training pipeline and its human reward designers inside the boundary. The paper's title makes that declaration implicitly.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: shared axis is which form retains the learning. Terminal-RSI uses natural-language runbooks as transient scaffolding that produces parametric supervision, then removes them (the paper notes that P "removes private runbooks"). That makes it a weight-only end of the example list, beside SkillRL's co-retained skill bank.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **is-evidence-for**: the paper says "each retained stage consolidates discovered behaviors". The only support is benchmark scores, the same metric that accepted each stage. The authors concede that compute-matched and inherited-versus-reset controls "remain necessary", and SWR100 is "unchanged after RPR-1". The case shows the gap the note describes. Weaker than the candidates above.
- [Ingest: Long-Horizon-Terminal-Bench](../../../../sources/long-horizon-terminal-bench.ingest.md) -- **compares-with**: shared axis is partial credit versus strict completion. LHTB uses graded partial credit as evaluation evidence and leaves open whether feeding it to a learner helps. Terminal-RSI trains on partial credit through FDR and reports that it can keep rewarding incomplete behavior, which it fixes by making credit subordinate to strict success through SPR. Terminal-RSI also reports LHTB results (0/46 → 5/46).
- [Ingest: SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- **compares-with**: shared axis is what a trajectory-distillation-plus-RL loop retains. SkillRL keeps a readable skill bank that co-evolves with GRPO weights. Terminal-RSI distills trajectories into runbooks only to generate supervision, then retains only weights and the critic.
- [Ingest: Agent optimizers compound on Terminal-Bench](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: shared axis is multi-stage gain claims on Terminal-Bench without fresh-start causal controls. Both report staged improvement on the same benchmark family, and both lack the control that would separate compounding from accumulation.
- `https://arxiv.org/abs/2610.22192` -- **derived-from** (external): the ingest's origin edge.

## Bidirectional Candidates

- [Ingest: Long-Horizon-Terminal-Bench](../../../../sources/long-horizon-terminal-bench.ingest.md) <-> source -- **compares-with**: LHTB's open question is whether partial-credit scores improve a later learner. Terminal-RSI is the follow-up case, so a return `compares-with` from the LHTB ingest would route readers of that open question to it.

## Reverse-edge Candidates

These depend on the ingest existing at `kb/sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md`.

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) → ingest -- **evidenced-by** (notes→sources authorised; the phrase must say "illustrates/bounds", not corroboration, per the notes "Origin is not corroboration" rule): the Rust–C delegation case is a compact modern example of a hard oracle certifying conformance while the intended capability is absent. It would complement the vision-features history. If the claim is used, it needs grounding via `cp-skill-ground`.
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../../../../notes/computationally-directed-self-improvement-is-a-reallocation.md) → ingest -- **evidenced-by** (illustrates, not corroborates): a self-titled RSI training system whose reward redesign and stage retention stay human-supplied. This is useful if the note gains a worked example.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- the "passes every scenario check, misses the terminal gate" pattern resembles the note's composition-failure tell. However, FDR's partial credit sits in the verdict/reward position, and the note explicitly separates that position from a proximate target, which sits in the goal position. A link would blur that distinction. The exact-implementation note carries the case.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- this note concerns evidence the *proposer* inspects to form hypotheses. Terminal-RSI's dense reward is a gradient/selection signal, which is the oracle side of that note's split. The LHTB ingest already makes the diagnostic-richness link for subtask scores.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- the FDR problem is reward allocation that favors incomplete behavior. It is not unequal discrimination across qualities, and strict success is binary and well discriminated.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- relevant in general. The specific coverage-gap point is better carried by the exact-implementation note, and the LHTB ingest already links the spectrum for the same checks.
- [An insufficient summary precedes the source rather than replacing it](../../../../notes/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- the paper's distinction between chunking and summarization is a one-sentence aside about credit-assignment invariance. It does not test summary sufficiency.
- [Ingest: Toward measuring recursive self-improvement](../../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.ingest.md) -- the RSI framing is shared, but Shōbench measures whole-state agent adaptation, not weight training. Its axis is already covered by the compounding note candidate.
- [Ingest: Recursive self-improvement since 1987](../../../../sources/recursive-self-improvement-since-1987.ingest.md) -- reward-based retention is historically adjacent, but no specific shared axis gives a reader anything beyond the SkillRL comparison.
- `kb/agentic-systems/reviews-archive/openrsi.md` -- archived. It shows training interfaces, but archive reviews are historical, and the specific axis is not one Terminal-RSI informs.
- Runbook-mentioning notes (`designing-agent-memory-systems`, `generate-instructions-at-build-time`, and others) -- they use "runbook" for human-facing procedures. That is a keyword-only match.

## Index Membership

None. Sources are not a participating tag collection. When the ingest is written, its routing happens through outbound links, not tag membership.

## Synthesis Opportunities

Terminal-RSI with LHTB and the checked-outcome note: the same deterministic checks serve three roles. They support strict acceptance (the terminal gate). They support graded evaluation (LHTB partial credit). They act as a training reward (FDR/SPR). Terminal-RSI's 50.09% failure reward mass suggests that the role determines whether partial credit helps or misdirects: it is harmless or useful as evaluation detail and harmful as an unsubordinated reward. This is one case, and the paper offers no controlled test. Record it as a candidate observation, not a note.

## Maintenance Observations

- The precursor RSR paper (Li et al., ref [23], "complementary-harness discoveries through runbook planning, leakage review, and fresh public execution") and T1 (ref [46]) have no ingests. If the RSR mechanism matters to the checked-outcome comparison, the precursor is the primary source for it.
- The agentic-systems body search for `PPO` is dominated by case-insensitive substring noise. Future connect runs should use `-w` or case-sensitive `\bPPO\b`.

## Flags

- The ingest did not exist at report time. All outbound candidates target that future file.
- The source makes several independent assertions (credit assignment, critic handoff, reward evolution, verifier coverage), but it is a source, not a note, so a split does not apply. The ingest should pick the two or three KB-relevant lines (verified rewriting with re-execution, partial credit as reward, verifier coverage, human-held decisions) rather than summarize the RL machinery.
