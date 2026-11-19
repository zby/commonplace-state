---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/jit-agent-scaling-harness-intelligence.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution

**Source:** [JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution](../../../../sources/.snapshots/jit-agent-scaling-harness-intelligence.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The strongest routes were the deploy-time-learning and self-improving-system theory clusters, existing harness-learning ingests, code-grounded harness-learning reviews, and the Claude Code dynamic-workflow analysis. The reference landing exposed only Commonplace-specific runtime material, so no reference candidate passed the articulation test.

**Full title listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over all five authorised local destinations: notes (414 titles), reference (159), agent-memory-systems (175), agentic-systems (14), and sources (359). Candidate titles were retained only when they distinguished task-conditioned generation, harness evolution, model–harness evaluation, diagnostic repair, or orchestration persistence.

**Description listing scans:**

- Ran `rg '^description:' kb/notes --glob '*.md' | rg -i 'harness|deployed system|fixed decomposition|orchestration|diagnostic|proposal-selection|memory management|self-improvement'`. Kept the deployed-system, proposal-selection, fixed-decomposition, persistence, and diagnostic-richness notes. Rejected memory-policy and orchestration-scaling matches where this paper did not isolate the claimed mechanism.
- Ran `rg '^description:' kb/sources --glob '*.md' | rg -i 'harness|self-improv|adaptation|runtime|orchestrat'`. Compared the paper against Meta-Harness, Harness Continual Learning, Continual Harness, HarnessCompass, Natural-Language Agent Harnesses, Self-Harness, AutoSaddler, and Claude dynamic workflows; retained the four comparisons that most sharply distinguish just-in-time synthesis from durable search or a narrower per-task orchestrator.
- Ran `rg '^description:' kb/agent-memory-systems --glob '*.md' | rg -i 'harness|planning|orchestrat|trace-learning|self-improv'`. Kept the code-grounded Meta-Harness and Agentic Harness Engineering reviews because they establish the implementation-side ahead-of-time comparison the paper foregrounds.
- Ran `rg '^description:' kb/agentic-systems --glob '*.md' | rg -i 'harness|runtime|orchestrat|self-improv'`. Kept Claude Code dynamic workflows as the closest shipped instance of model-authored task-specific orchestration.
- Ran `rg '^description:' kb/reference --glob '*.md' | rg -i 'harness|runtime|orchestrat|self-improv'`. All hits described Commonplace-specific implementation state or historical decisions and were rejected.

**Body search:**

- `rg -n -i 'JIT[- ]Agent|just-in-time harness|harness intelligence|Model-as-a-Harness|Evo-GDPO|HarnessFactory' kb --glob '*.md' --glob '!sources/.snapshots/**'` returned no prior use of this paper or its named mechanisms.
- `rg -n -i 'task[- ](specific|conditioned).*harness|harness (search|generation|evolution)|model.?harness|fixed decomposition|diagnostic (richness|evidence)|proposal.selection' kb/notes --glob '*.md'` confirmed the fixed-update-space, diagnostic-evidence, and proposal-selection neighborhoods.
- Scoped searches over sources, agent-memory systems, and agentic systems for `task-specific harness`, `harness search`, `harness evolution`, `dynamic workflow`, and `orchestrat` surfaced the retained comparisons below.

**Link following:**

- Followed the deployed-system note to the proposal-selection and fixed-decomposition notes and to its Meta-Harness evidence. This made the fixed-backbone controlled comparisons and the remaining fixed four-module protocol separate candidate connections rather than one undifferentiated “harness matters” edge.
- Followed diagnostic richness to Meta-Harness, AutoSaddler, and Agentic Harness Engineering. JIT-Agent uses structured compiler and runtime diagnostics for repair, but does not ablate diagnostic richness, so that connection remains `see-also` rather than evidence.
- Followed Claude Code dynamic workflows to the orchestration-strategy/run-state persistence note and its RLM comparison. JIT-Agent generates a broader executable four-module scaffold and trains the generator, making the shipped workflow surface a useful bounded comparison.
- External prospecting was skipped: the source collection authorises external links, but no external candidate beyond the supplied source was already in context.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — **is-evidence-for**: the paper defines capability over the model–harness pair and reports same-backbone gains when only the harness changes, including 18 improved matched backbone–benchmark pairs and controlled comparisons with fixed runtimes.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: static inference samples and selects harness candidates, while streaming inference evaluates reward, latency, and cost and retains only candidates that advance the harness-bank frontier for later tasks.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: JIT-Agent makes object-level harness structure learnable only inside a fixed memory/planning/action/capability protocol; the authors explicitly call that compact protocol a starting point rather than a validated decomposition.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — **is-evidence-for**: JIT-Agent separates transient task execution from reusable generated harnesses and a cross-task harness bank, with static mode discarding experience and streaming mode retaining only frontier-improving strategies and metrics.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **see-also**: Stage II turns compiler errors, interface mismatches, tool failures, and runtime exceptions into bounded repair supervision, but the paper does not isolate richer diagnostics as the cause of improved repair.
- [Meta-Harness: End-to-End Optimization of Model Harnesses](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) — **compares-with**: Meta-Harness repeatedly searches durable task/domain harness code from raw traces, whereas JIT-Agent amortizes search into a trained generator that produces a harness for the current instance from a protocol, capability registry, and small retrieved bank context.
- [Harness Continual Learning](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) — **compares-with**: both keep the executor weights fixed and update a four-part harness state, but HCL commits sequential component edits behind current-task and retention gates while JIT-Agent generates a fresh task-conditioned harness and optionally retains it in a frontier bank.
- [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) — **compares-with**: Continual Harness directly edits prompts, sub-agents, skills, and memory within a persistent episode and can also train weights; JIT-Agent instead trains a separate harness generator and keeps the executor fixed during reported harness evolution.
- [A harness for every task — dynamic workflows](../../../../sources/a-harness-for-every-task-dynamic-workflows.ingest.md) — **compares-with**: both generate task-specific orchestration on demand, but dynamic workflows produce an ephemeral sub-agent script from a general model while JIT-Agent is purpose-trained to emit a complete executable memory/planning/action/capability scaffold.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) — **compares-with**: the code-grounded review exposes the filesystem traces, generated Python candidates, and evaluation frontier behind the paper's ahead-of-time comparison class.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) — **compares-with**: AHE distills coding-agent traces into durable workspace edits across iterations, while JIT-Agent trains a reusable generator and treats the bank, rather than one evolving workspace, as the cross-task retention surface.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — **compares-with**: this shipped system is a narrower model-authored just-in-time orchestrator over bounded sub-agent calls; it keeps memory policy, action kernel, capability registry, and runtime restrictions outside the generated script.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — rejected because JIT-Agent changes memory together with planning, action, and capability orchestration; its experiments do not isolate a learned memory policy or the effect of its oracle.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../notes/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) — rejected because the qualitative harness examples include all three features but do not run the intervention needed to identify that causal chain.
- [Harness sub-agent model selection regression](../../../../reference/harness-sub-agent-model-selection-regression.md) — rejected as a Commonplace-specific execution-provenance incident whose only overlap is the word “harness.”
- [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) — useful representational-form overlap, but weaker for this ingest than the selected AOT/JIT and dynamic-workflow contrasts; both interventions also bundle structure with their runtime, so a direct empirical comparison would overstate what either source isolates.

## Index Membership

None

## Synthesis Opportunities

- JIT-Agent, Meta-Harness, Harness Continual Learning, and Claude Code dynamic workflows suggest a missing distinction between **when harness structure is chosen** and **what remains fixed while it is chosen**. A trained generator can move task-level selection from ahead of deployment to inference time without making its protocol, capability registry, training objective, evaluator, or retention rule just-in-time. That boundary could support a note only after checking whether it changes an actual Commonplace design choice rather than merely naming the paper's taxonomy.

## Maintenance Observations

None

## Flags

None
