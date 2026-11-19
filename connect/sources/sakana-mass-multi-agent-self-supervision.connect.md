---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/sakana-mass-multi-agent-self-supervision.md"
source_has_frontmatter: true
date: "2026-10-24"
depth: standard
---

# Connection Report: Multi-Agent Self-Supervision (MASS)

**Source:** [Multi-Agent Self-Supervision (MASS)](../../../../sources/.snapshots/sakana-mass-multi-agent-self-supervision.md)

The target is an immutable snapshot. Its authored connection surface is the
name-paired ingest `kb/sources/sakana-mass-multi-agent-self-supervision.ingest.md`,
which does not exist at report time. Every candidate below is for that ingest
(or, for reverse edges, for the named artifact). Durable links must point at the
ingest, never at the snapshot.

Source claims used for judging: (1) homogeneous RSI, where one model is
executor, workflow optimizer and pairwise evaluator on non-verifiable research
tasks; (2) an inner loop searches written workflows (role, instruction,
contract, hop) against a self-judged champion, and an outer loop LoRA-tunes on
the top-ranked of 18 champion runs with the workflow text stripped from the
prompt; (3) two rounds on Qwen3.6-27B raise external-judge win rates (69.9% vs
base on held-out synthetic tasks) and score per output token 1.2-1.6x on four
research benchmarks, but 0.94-0.96x on SWE-bench Verified and Terminal-Bench;
(4) optimizer and evaluator improve without being trained (evaluator agreement
with external judges 73% to 93%); (5) evolved workflows concentrate task
information in contracts and hops; (6) multi-agent trajectories give more win
rate per supervised token than single-agent ones; (7) upgrading the evaluator
alone helps a little, upgrading the optimizer too helps a lot; (8) shared blind
spots in a homogeneous loop can be accepted and trained into the next model.
Evidence is author-run, with GPT-5.5 and Claude Opus 4.8 as withheld external
judges.

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` "Outbound links".
Destinations: theory, reference, agent-memory-systems, agentic-systems, tags,
other sources; `kb/work/` and `kb/instructions/` excluded. Labels:
`is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory),
`rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems,
agentic-systems), `defined-in` (theory/definitions), `see-also` (broad, use
sparingly), `derived-from` (external). External prospecting skipped: the only
external target in hand is the source URL itself (`derived-from`, trivially
authored by the ingest). The arXiv record `2610.12176` and the author blog post
named in the snapshot are known but were not evaluated beyond noting them.

**Tag heads:**
- `kb/tags/self-improving-systems-README.md` (`complete: true`) -- by-tag rg skipped; yielded the casebook, objective notes, and child-area routing.
- `kb/tags/improvement-loop-README.md` (`complete: true`) -- by-tag rg skipped; yielded the proposal-selection loop, false-positive acceptance, open-ended search, and oracle notes.
- Tags do not list `sources` as a participating collection (`kb/tags/COLLECTION.md` `participating:`), so no tag membership applies to the ingest.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (425 titles), filtered with `rg -i 'self-improv|evaluat|judge|oracle|optimi|blind|correlat|multi-agent|subagent|orchestrat|distill|verif|self-supervis|workflow|contract|handoff|trajector|learning loop|gradient|text space|homogen'` -- about 50 hits; descriptions read for 25.
- `rg -N --no-heading -m1 '^# ' kb/agentic-systems/` and `kb/agent-memory-systems/` filtered with `rg -i 'self|evol|optimi|workflow|multi-agent|...'` -- flagged OpenRSI, AIDE2, Meta^n, Claude Code dynamic workflows, Self-Training-LLM, Incremental Self-Improvement, AgentFly, trace-learning comparison.

**Body search:**
- `rg -l -i 'same model|correlated (error|blind)|shared blind|self-judg|self-evaluat|LLM-as-judge|llm judge' kb/theory kb/agentic-systems kb/agent-memory-systems kb/reference` -- 40+ files; strongest hit `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`.
- `rg -l -i 'sakana|MASS\b|recursive self-improvement|ADAS|AFlow|workflow optimi|automated design of agentic' kb` (excluding `kb/work`) -- surfaced the RSI source cluster (ADAS, Terminal-RSI, Poetiq, AIDE2, SIFT, DGM, harness-engineering survey, Shobench, Schmidhuber retrospective); `sakana` matches SIFT and DGM only, so no existing MASS ingest or citation.
- `rg -l -i 'decorrelat' kb/theory` -- 33 files; kept the decorrelation note and the shared-prior reviewer note.
- `rg -n -i 'text.space|textual gradient|prompt optimi|DSPy|GEPA|TextGrad' kb/theory` -- led to `treat-continual-learning-as-representational-form-coevolution.md`, whose "Loops today" list includes Co-Harness.
- `rg -l -i 'multi-agent' kb/sources/*.ingest.md | xargs -r rg -N --no-heading -m1 '^description:'` -- flagged Mismanaged Geniuses, Towards a Science of Scaling Agent Systems, xinmingtu hierarchical MAS.
- `rg -l -i 'self-preference|self-evaluation|llm.as.a.judge|judge' kb/sources/*.ingest.md | xargs -r rg ... '^description:'` -- flagged Autoreason, Terminal-RSI, pairwise-judging source.
- Targeted checks: `rg -n -i 'acqui|trained|weights|learned'` in the orchestration design-space note (has a distributed-parametric decomposition-policy row); `rg -n -i 'compound|next model|blind'` in the false-positive note (line 51: "the blind spot that let the change in is the blind spot that lets it stay"); `rg -n -i 'contract|return artifact|guarantee'` in the coordination-guarantees note; `rg -n -i 'verif|27B|Qwen'` in Terminal-RSI; `rg -n -i 'verified traj|round'` in Co-Harness.

**Link following:**
- From the representational-form coevolution note to [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md): a two-round alternation of harness repair and SFT on generated trajectories, the closest structural twin in the KB.
- From the Mismanaged Geniuses ingest to the orchestration design-space note: the decomposition-policy acquisition axis that MASS instantiates in weights.
- From the Autoreason ingest to the error-correction and pairwise-comparison cluster.

**Reference:** no reference artifact describes a shipped Commonplace mechanism that MASS bears on; `see-also` into reference not proposed.

## Connections Found

- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **is-evidence-for**: MASS is a deliberately correlated case, the same model as executor and evaluator. Its own discussion names the predicted failure: a shared blind spot that the loop accepts and trains in. The 73% to 93% agreement with external judges is a measured soft-oracle trajectory, not a decorrelation result.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../theory/false-positive-generation-is-filtered-before-retention.md) -- **is-evidence-for**: MASS's safety section describes acceptance-side error in weight form. A flawed workspace accepted by the self-evaluator becomes training data for the next model, which then also judges. This matches the note's "same oracle that made the original mistake" case.
- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: MASS adds a cross-form loop. Natural-language workflow search runs with frozen weights, and LoRA distillation then removes the workflow text from the prompt. Learned organization moves from a readable artifact into weights, the reverse of the note's readable-artifact bet.
- [Agent orchestration occupies a multi-dimensional design space](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **is-evidence-for**: the note's distributed-parametric decomposition-policy row rests mainly on the Mismanaged Geniuses proposal. MASS reports an acquisition path: workflows found by search are trained into the orchestrator with the plan stripped, and gains hold without a supplied workflow.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **is-evidence-for**: evolved MASS workflows move task-specific information into contracts and hops, such as the leakage `validation_report` that gates later agents. The optimizer selects for what each handoff must establish rather than for role wording. The evidence is a mutual-information analysis of author-chosen components.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **is-evidence-for** (qualifying): in Figure 7 a stronger external evaluator alone helped a little, while a stronger optimizer as well helped a lot. In this loop the binding constraint was candidate generation, not oracle quality. The result is bounded: one base model, 12 tasks, and a homogeneous loop that still reached winning workflows on 11 of 12.
- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../theory/open-ended-improvement-allocates-search-before-evaluation.md) -- **is-evidence-for**: the optimizer-bottleneck result, together with the reported noisy workflow search ("reaching a good workflow and improving on it stably are different problems"), shows search capacity limiting improvement when evaluation is held fixed.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **compares-with** on the function-allocation axis: MASS has all three functions. They are the optimizer, the champion-replacing pairwise evaluator, and LoRA retention. One model fills all of them, and retention changes the model that runs search and evaluation in the next round.
- [Self-improving system](../../../../theory/definitions/self-improving-system.md) -- **defined-in**: the ingest will use "recursive self-improvement". Readers need the KB's frame-relative definition (boundary, horizon, objective) to see that MASS's objective is self-judged and its outside measure is withheld external judges.
- [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with** on the harness-then-weights alternation axis: both run two rounds of harness search followed by SFT on trajectories from the improved harness. Co-Harness admits verified trajectories on checkable math and keeps the harness. MASS admits self-ranked trajectories on non-verifiable tasks and strips the workflow from the training prompt.
- [Terminal-RSI](../../../../sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md) -- **compares-with** on the trajectory-admission oracle axis: both use a 27B Qwen base and rounds of trajectory distillation. Terminal-RSI keeps only protected-verifier passes; MASS keeps self-judged Bradley-Terry winners. MASS's 0.96x score per token on Terminal-Bench marks where the two diverge.
- [Automated Design of Agentic Systems](../../../../sources/automated-design-of-agentic-systems.ingest.md) -- **compares-with** on the outer-loop-machinery axis: both search agent or workflow designs. ADAS keeps a fixed meta-agent and an archive. MASS retrains the model that serves as meta-agent, so search machinery changes between rounds; this is the "fixed outer-loop machinery" gap the ADAS ingest names.
- [Autoreason](../../../../sources/autoreason-self-refinement-that-knows-when-to-stop.ingest.md) -- **compares-with** on the incumbent-retention axis: both keep an incumbent (MASS's champion) that a candidate must beat under pairwise judgment. Autoreason uses fresh blind judges and Borda aggregation, and MASS uses the same model, so they differ in exactly the judge-hygiene variables Autoreason ablates.
- [The Mismanaged Geniuses Hypothesis](../../../../sources/the-mismanaged-geniuses-hypothesis-2042588627260018751.ingest.md) -- **compares-with** on the decomposition-policy-training axis: MGH proposes training models to choose decompositions inside a scaffold. MASS reports one way to do it, by searching workflows and then distilling orchestrator and subagent conversations.

## Bidirectional Candidates

- [Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) <-> source -- **compares-with**: a reader of Co-Harness who asks whether verified trajectories are necessary gets MASS's non-verifiable counterpart. Sources-to-sources `compares-with` is authorised.
- [Terminal-RSI](../../../../sources/terminal-rsi-recursive-self-improving-terminal-agents.ingest.md) <-> source -- **compares-with**: the same verifier-versus-self-judge contrast is useful from the Terminal-RSI side.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) <-> source -- the return edge is a qualifying counter-case to "the bottleneck is typically oracle construction, not generation". The note would author it under its own collection's rules once the ingest exists.

## Reverse-edge Candidates

- [Treat continual learning as representational-form coevolution](../../../../theory/treat-continual-learning-as-representational-form-coevolution.md) -> source ingest -- its "Loops today" list could add MASS beside Co-Harness. It is a natural-language-plus-weights loop that deletes the readable form after distillation. The note already says Co-Harness "does not isolate coevolution". MASS's Table 2 workflow-transfer result (the base model executing round-1 workflows wins 64%) is a partial isolation of the harness contribution.
- [Real self-improving systems occupy combinations no single rung captures](../../../../theory/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -> source ingest -- MASS is a placement candidate: a homogeneous loop whose retention target, the weights, is also the evaluator and the optimizer.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -> source ingest -- MASS could serve as the note's worked example of a same-model checker inside a training loop, where correlation compounds across rounds rather than only plateauing within a vote.
- [Agent orchestration occupies a multi-dimensional design space](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -> source ingest -- the distributed-parametric decomposition-policy row currently cites a proposal. MASS supplies a reported instance.

## Off-authorisation Candidates

- [OpenRSI](../../../../agentic-systems/reviews-archive/openrsi.md) -- connects through a search-to-training loop: OpenRSI's selected steps are meant to become training messages, but its release "does not close" that conversion. MASS reports that conversion closed. `compares-with` into agentic-systems is authorised, but the target is in `reviews-archive/`, so it is likely stale. Reject unless the archive is meant to be a link destination; otherwise prefer a live review.

## Raw Text Candidates

None

## Rejected Candidates

- [Process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) -- contracts and hops look like output and process structure, but the note is about templates constraining one model's reasoning steps, not inter-agent handoffs. The mapping would mislead.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- the MASS orchestrator integrates subagent results, but the source does not test synthesis against voting.
- [Decorrelated reviewers still share the field's prior](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- topically adjacent (shared blind spots), but MASS's concern is same-model correlation, which the decorrelation note already covers. Adding this would duplicate the edge.
- [Weakly discriminated qualities tend to be underselected](../../../../theory/weakly-discriminated-qualities-tend-to-be-underselected.md) -- MASS reports no per-quality discrimination data; the link would be speculative.
- [The deployed system, not the model, is the unit of learning](../../../../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- MASS learns the workflow and then moves it into the model, which is a tension. The coevolution edge already carries this point more precisely.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- that source is about test-time multi-agent gains; MASS's distinct claim is about training-data value per token. The overlap is a keyword match.
- [Poetiq](../../../../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) and [SIFT](../../../../sources/sift-self-improvement-fast-tree-search.ingest.md) -- the same RSI area and lab (SIFT), but harness-only search with no weight update; no named shared axis beyond Co-Harness and ADAS.
- [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) -- self-generated data trained into weights, but its filter is NLI and uncertainty on factual QA, not self-judged team work. The axis is too generic.

## Index Membership

- [Sources README](../../../../sources/README.md) -- if it groups RSI or self-improvement sources, the ingest belongs beside Co-Harness and Terminal-RSI as a non-verifiable, homogeneous weight-update case. The README was not read for structure in this pass.

## Synthesis Opportunities

MASS, Co-Harness and Terminal-RSI form a natural three-way contrast. All three
alternate trajectory generation with weight training on roughly similar bases.
They vary the trajectory-admission oracle: self-judged, harness-validated, or
protected verifier. A theory note could claim that the admission oracle sets
how far such loops transfer, using MASS's research-benchmark gains against its
SWE-bench and Terminal-Bench regressions as the first data point. This is
evidence for a conjecture, not an established claim.

## Maintenance Observations

- The theory corpus has a firm "verification is the bottleneck" thread (the automation-boundary synthesis, the oracle-strength spectrum). It has no note on when the generator or optimizer is the binding constraint. MASS is the first source here with an ablation that separates the two. This gap could be tracked in the log until a second source agrees.

## Flags

- Tension: MASS's optimizer-bottleneck finding qualifies [the boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md). It is left unresolved; scope (one model, 12 tasks, research-style work) limits how far it bears.
- The authored surface (`kb/sources/sakana-mass-multi-agent-self-supervision.ingest.md`) does not exist yet; all candidates wait on it.
- Caveat for the ingest author: the snapshot is a blog write-up of arXiv 2610.12176. Several numbers ("more details in paper", Figures 3-8) are shown only as figures, so claims resting on them may need the paper.
