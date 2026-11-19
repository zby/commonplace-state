---
description: "On-policy distillation shows cross-domain gains and regressions despite domain routing, motivating broader validation of parametric updates."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/dual-nature-generalization-on-policy-distillation.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: Generalization in On-Policy Distillation

**Source:** [Paper snapshot](../../../../sources/.snapshots/dual-nature-generalization-on-policy-distillation.md)

## Discovery Trace

Read all 3,800 lines of the v2 paper, including lineage definitions, evaluation settings, full tables and supplementary curves. Reused batch contracts, curated heads and complete title surfaces for all five authorized destinations. `rg -n -i '^description:.*(parametric|weights|transfer|regression|side.effect)' kb/notes --glob '*.md'` identified governing behavior-changing writes, representational form and related cross-form notes. Read the first two fully and followed the governing-writes link to the complete representational-form coevolution note; retained only the narrower governance and definition edges. Experimental contrast was fully read earlier in this batch. `rg -l -i 'on.policy distill|same.origin|MOPD' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources` found OpenClaw-RL, ACM, Machine Studying and Language Models Need Sleep ingests. Their title/description scope (and prior full Machine Studying reading) concerns different feedback/retention mechanisms; no same-origin multi-teacher comparison warrants an extra source edge. No candidate in reference or either system collection. No external prospecting or excluded destinations.

## Connections Found

- [Govern behavior-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — **is-evidence-for**: a teacher supervising one prompt domain changes other-domain behavior, including regressions, so validating only its assigned domain can miss consequences of a retained weight update. This supplies a concrete parametric example for regression validation; the paper does not test deployed continual learning or Commonplace governance.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: teacher-mixture and role-swapping experiments show that prompt domain does not confine influence, but origin is compared among existing model lineages with different capacities and post-training. Top-token overlap and performance transfer do not isolate whole-policy alignment as their causal mechanism.
- [Representational form](../../../../notes/definitions/representational-form.md) — **defined-in**: the retained changes here are distributed-parametric updates, evaluated behaviorally across tasks. Domain labels route supervision; they do not create separately editable domain-specific knowledge records or guaranteed boundaries on the resulting behavior.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Govern behavior-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → eventual tracked ingest — **evidenced-by**: the non-target-domain losses and reversed teacher-role experiment provide a bounded example for validating regressions beyond the update's nominal domain. Keep the post-training setting distinct from deployment-time adaptation.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- General routing or authorization notes: this is training-supervision routing and shared parameter updates, not runtime tool access or evidence authority.
- Cross-form coevolution as an additional edge: no co-optimized readable-artifact loop is studied, so the narrower parametric-update distinction suffices.
- Off-domain regression proves malicious or unsafe behavior: the experiments measure capability, with safety transfer discussed as a possibility rather than tested.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

The study uses policy-gradient on-policy distillation with sampled-token reverse-KL supervision on student-generated trajectories, not supervised imitation of complete correct teacher solutions. Four teacher rollouts classify 25k math questions into easy, hard and random subsets. Zero observed successes is not proof that the teacher can never solve a question. Similar endpoint gains across these subsets and matched 8k absolute-difficulty pools support useful token supervision without complete solved answers; they do not isolate the content of a transferred reasoning process.

Student-side dynamic sampling improves the two reported averages by .6 and .4 percentage points when it discards fully solved problems, retaining pass rate below one. The takeaway parenthesis incorrectly says pass-rate zero for already-solved problems; follow the table and surrounding procedure, not that typo. No repeated training-seed intervals establish those small differences as statistically reliable.

Same-origin means a shared concrete initialization/post-training lineage, not merely one vendor or architecture family. Several teachers and students have different sizes and recipes; lineage is a useful observed grouping rather than a randomized cause. Qwen3-32B to Qwen3-8B-SFT is cross-origin yet improves language and reasoning-horizon math, with weak code transfer. Same-origin Light-R1-14B transfer can exceed its teacher on composed math. Thus neither a universal same-origin requirement nor a strict teacher-performance ceiling follows.

Same-origin math supervision can transfer code/science behavior, including pulling science performance downward toward a weaker-science math teacher. Multi-teacher runs use two complementary teachers with fixed domain routing and adjusted prompt proportions; reversing assignments still transfers off-domain capabilities. But the main Setting 1 uses Dev-1.5B already given ten science/IF distillation steps, while Setting 2 uses the base distilled student, so the cross-setting comparison also changes initial state. Within-setting mixtures and supplementary base-student results are more precise contrasts. Teacher proportion and prompt-domain proportion move together; the evidence rejects strict influence confinement but does not isolate every teacher-versus-data mechanism.

Top-16 next-token overlap rises more in same-origin pairs during training. This local distributional diagnostic supports compatibility as a hypothesis, not identification of alignment over every possible context or all capabilities. Mixture effects are not strictly monotone on every benchmark; changing teacher share and sequential science-then-math training expose interference in the tested shared student. No larger expert pools, adaptive routers, multimodal or interactive-agent settings are tested.

Training uses at most 200 steps of 128 prompts, four rollouts each, learning rate 1e-5 and 40k–96k sequence caps by model group. Evaluation uses stochastic decoding and Avg@K, not best-of-K: K ranges 1–16 by benchmark. LiveCodeBench training and evaluation date ranges are disjoint. Curves use centered five-point smoothing with future checkpoints, so displayed trajectories cannot establish precise online reversal times. Tables are unsmoothed. No code inspected or experiments executed for this ingest.
