---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/pilot-live-self-improvement-long-horizon-agents.md"
source_has_frontmatter: true
date: "2026-09-04"
depth: standard
---

# Connection Report: PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents

**Source:** [PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents](../../../../sources/.snapshots/pilot-live-self-improvement-long-horizon-agents.md)

The snapshot is immutable. Every outbound candidate below is for the future name-matched ingest report, not for the snapshot itself.

## Discovery Trace

**Collection rules and scope:**

- Read `kb/sources/COLLECTION.md`. The authored ingest may prospect `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and other `sources`; `work` and `instructions` are excluded. The snapshot itself never authors a durable link. The name-matched ingest did not exist during discovery.
- The original arXiv URL and the project GitHub URL were already present in the snapshot. They were treated as known provenance/implementation targets, not open-web prospects. No open-web or external search was run.

**Curated heads and complete recall surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agent-memory-systems/lightweight/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes head routed the paper toward deploy-time learning and orchestration; the memory-system head routed it toward trace learning; the agentic-system head exposed the whole-harness comparison surface. The reference head yielded only broad Commonplace planning analogues.
- The source carries no `tags`, so no tag-README or by-tag description scan applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` separately over all five authorised local destinations: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- The title and description surfaces flagged the self-improving-system definition, deployment-time artifact learning, checked-outcome and intended-path limits, agent-to-agent conversation, orchestration dimensions, context efficiency, the trace-learning survey, Hermes Agent, Claude Code dynamic workflows, Continual Harness, the harness-update/benefit study, the Terminal-Bench compounding study, and the self-improving-agent fragility study. The reference surface produced no source-specific target whose traversal value justified the collection's sparse `see-also` label.

**Body search:**

- Notes: `rg -n -i 'live steer|mid-run|active (run|worker)|supervisor|worker remains|ongoing trajector|redirect.*(worker|run)' kb/notes/ --glob '*.md'`; `rg -n -i 'persistent harness|harness (update|evolution)|trace-extracted|successful runs|checked outcome|outer-loop learning|deployment-time adaptation|behavio(u)?r-changing write|factory learning' kb/notes/ --glob '*.md'`; and `rg -n -i 'supervisor.*context|context.*supervisor|separate context|isolated context|delegat.*(feedback|steer|active)|orchestration.*(state|persist|coordination)' kb/notes/ --glob '*.md'`.
- Agent-memory systems: `rg -n -i 'live steer|mid-run|active (run|worker)|supervisor|worker|ongoing trajector|persistent harness|trace learning|trace-learning|skill (library|distill)|self-evol|successful runs' kb/agent-memory-systems/ --glob '*.md'`.
- Agentic systems: `rg -n -i 'live steer|mid-run|active (run|worker)|supervisor|worker|ongoing trajector|persistent harness|self-evol|sub-agent|delegat' kb/agentic-systems/ --glob '*.md'`.
- Sources: `rg -n -i 'live steer|mid-run|active (run|worker)|supervisor|worker|persistent harness|trace.*skill|self-evol|successful runs|Terminal-Bench' kb/sources/ --glob '*.md'`.
- Reference: `rg -n -i 'live steer|live self-improvement|self-evol|supervisor.worker|two-way (live )?channel|mid-run (input|steer|correction)' kb/reference/ --glob '*.md'` and `rg -n -i 'trace.*(skill|memory)|successful.run|harness update|trajectory.*retention|agent-memory gap' kb/reference/ --glob '*.md'`. These found only Commonplace's current memory coverage/gap plan, not a direct peer or dependency suitable for a source-side `see-also` edge.
- Exact-name check: `rg -n -i '\bPILOT\b|live self-improvement|live self-evolution' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found no prior PILOT coverage; other uses of “pilot” were ordinary pilot-study references.

**Candidate evaluation:**

- Kept the self-improving-system definition because PILOT declares the frozen backbone plus mutable harness as its system boundary, while Commonplace's definition supplies the stricter obligations needed to distinguish retained updates from demonstrated operative self-change.
- Kept the deployment-time-adaptation note because PILOT reports exactly the fixed-weight path it predicts: live trajectory evidence becomes persistent natural-language skills and memory used by later workers and iterations.
- Kept the checked-outcome note because PILOT carries inter-iteration updates only from successful tasks, while end-task success does not identify which distilled rule or explanation produced the outcome.
- Kept the intended-path-health note because PILOT's manual steering analysis explicitly refuses to count “intervention followed by PASS”; it requires a concrete diagnosed error, followed correction, and eventual success along the corrected path.
- Kept the conversation/refinement note because PILOT's Question and Steer operations continue the worker with its accumulated partial work instead of restarting it from a rewritten prompt; this is a concrete live-conversation design with no isolated comparison against restart/refinement.
- Kept the orchestration-design-space note because PILOT combines an LLM supervisor, isolated worker contexts, a two-way live coordination channel, same-backbone role separation, task-local trajectory state, and cross-task harness persistence. Those properties occupy several independent axes rather than one delegation level.
- Kept the context-efficiency note narrowly: PILOT reports falling output tokens and rising successes per million output tokens as skills accumulate, but the bundled iterative comparison does not isolate skill reuse, supervisor separation, or task-order effects as the cause.
- Kept Continual Harness as the closest paper-level online-adaptation comparison: both edit skills/memory during a live long-horizon episode, but Continual Harness directly installs Refiner edits into the next step while PILOT separates self-improvement into a connected supervisor and retains successful-run updates across benchmark iterations.
- Kept Harness Updating Is Not Harness Benefit because PILOT reports aggregate later-task gains and token efficiency without measuring per-skill loading, adherence, or causal uptake; the comparator names and measures those intermediate stages.
- Kept the Terminal-Bench optimizer study because it separates static gain, transfer to new tasks, and re-optimization on an expanded task set, whereas PILOT repeatedly sweeps a fixed task set and reports best-observed improvement.
- Kept the fragility study because PILOT's persistent skill state makes task order and early-run variance potential causes of later outcomes, while its two repeats and fixed iteration design do not test shuffled-order sensitivity.
- Kept the trace-learning survey because PILOT adds a hybrid not yet catalogued: supervisor-mediated extraction from an active worker trajectory, immediate within-episode steering, persistent skill/memory writes, and later outcome-filtered cross-iteration carryover.
- Kept Hermes Agent because both systems use a separate same-family context to inspect foreground traces and write memory or skills without contaminating the foreground context; Hermes reviews after turns and lacks an outcome oracle, while PILOT can steer the still-running worker and filters cross-iteration retention by task success.
- Kept Claude Code dynamic workflows because its sub-agent calls return only final results and explicitly lack mid-run input, which is the precise orchestration seam PILOT's Notification, Question, Steer, and Abort channel changes.
- Rejected Diagnostic richness as a direct evidence edge: PILOT motivates a separate supervisor context and selective trajectory inspection, but does not ablate trace access, summaries, or diagnostic context.
- Rejected Orchestration strategies and run-state have opposite persistence economics: PILOT retains procedures and memories, but the paper does not show that the retained units are scheduler `select` strategies rather than task/domain skills.
- Rejected GBrain, Exo, Meta-Harness, and Reason Wide, Not Deep as regular edges. They share self-modification, trace-learning, or skill-distillation vocabulary, but the kept candidates provide more discriminating comparisons on live intervention, same-context separation, uptake measurement, and task-stream evaluation.

**Link following:**

- Followed the self-improving-system definition to operative change, behavior-determining organization, proposal selection, objective-relativity, and its boundary-case note. This confirmed that PILOT's harness boundary is plausible while later causal dependence on particular retained skills remains incompletely identified.
- Followed the deployment-time-adaptation note to governing behaviour-changing writes, the deployed-system learning boundary, proposal-selection retention, and context efficiency. This separated the existence of PILOT's non-weight update path from the quality and governance of each write.
- Followed the checked-outcome note to trace-extracted-memory authority, boundary-statability, diagnostic richness, and final-task-success. This made PILOT's manual corrected-path classification materially different from its success-only inter-iteration retention rule.
- Followed the orchestration-design-space and conversation/refinement notes to bounded-context orchestration, context isolation, coordination guarantees, and persistence horizons. The useful PILOT contribution is the live continuation channel between isolated contexts, not generic multi-agent delegation.
- Followed the trace-learning survey to Hermes Agent, Meta-Harness, Agentic Harness Engineering, and success-gated skill systems. Hermes remained the closest inspected comparison for isolated live-trace review; Meta-Harness and Agentic Harness Engineering remained staged outer-loop systems rather than mid-run steering peers.
- Followed the source neighborhood among Continual Harness, Harness Updating Is Not Harness Benefit, the Terminal-Bench compounding study, On the Fragility of Self-Improving Agents, and Reason Wide, Not Deep. This separated online edit latency, causal uptake, task-stream transfer/order sensitivity, and token amortization into distinct comparison axes.

## Connections Found

- [Self-improving system](../../../../notes/definitions/self-improving-system.md) -- **rests-on**: analysis of PILOT's “self-improvement” claim needs the boundary-sensitive distinction between evidence-responsive harness writes and later operations causally depending on those operative changes; aggregate iteration gains do not identify every link in that path.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **is-evidence-for**: PILOT reports a fixed-backbone system that turns live execution experience into persistent skills and memory, then exposes the evolved harness to later workers and benchmark iterations.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **is-evidence-for**: PILOT's successful-run filter warrants carrying case-level updates forward, but task success alone does not establish that each distilled procedure is the faithful producing explanation or state its transfer boundary.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) -- **is-evidence-for**: the paper's manual steering analysis requires a diagnosed error, a followed correction, and success on the corrected path, explicitly rejecting the weaker “intervention followed by PASS” inference.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- **is-evidence-for**: PILOT implements the conversational continuation pole through Question and Steer events, preserving an active worker's accumulated context and partial work instead of restarting from a revised prompt.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **is-evidence-for**: PILOT combines role-separated same-model agents, isolated contexts, a live two-way coordination form, task-local trajectory state, and cross-task skill/memory persistence, showing why these properties cannot be collapsed into one delegation level.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **is-evidence-for**: across PILOT iterations, reported output tokens per evaluated task fall by 42.9% and 47.4% while success per million output tokens rises, a bounded system-level result consistent with retained procedures reducing repeated exploration but not isolating that mechanism.
- [Ingest: Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- **compares-with**: both systems update skills and memory during a live long-horizon episode; Continual Harness directly installs Refiner edits into the acting agent's next step, while PILOT gives a separate supervisor live control of a worker and carries successful-run updates across iterations.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: PILOT measures aggregate later-task outcomes, skill-count growth, and token efficiency, while this study separately measures artifact loading, judged procedural adherence, and downstream benefit, exposing the causal-uptake stages PILOT leaves bundled.
- [Ingest: Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both use Terminal-Bench 2.0 to study persistent harness change over time; the optimizer study tests transfer to newly introduced tasks and re-optimization on the expanded set, whereas PILOT repeats a fixed task sweep and reports best-observed iteration gains.
- [Ingest: On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) -- **compares-with**: the fragility study varies repeated runs and task order to expose path dependence in textual memory, supplying a missing reliability control for PILOT's successful-run skill carryover across only two fixed-order benchmark repetitions.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **is-evidence-for**: PILOT adds supervisor-mediated learning from an active worker trace, coupling immediate steering with persistent skill/memory extraction and later outcome-filtered carryover rather than fitting only post-turn or completed-trajectory patterns.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) -- **compares-with**: both isolate same-family trace review from foreground execution and can write memory or skills; Hermes reviews a completed foreground turn without an outcome oracle, while PILOT remains connected to redirect the active worker and filters cross-iteration retention by task success.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: dynamic workflows expose returning sub-agent calls with no mid-run user input, while PILOT's live channel exposes notifications, blocking questions, queued steering, and abort so supervision can act before the delegated execution returns.

## Bidirectional Candidates

- [Ingest: Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) <-> future PILOT ingest -- **compares-with**: a return edge would distinguish direct same-agent next-step harness edits from supervisor-mediated steering plus cross-iteration retention.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) <-> future PILOT ingest -- **compares-with**: a return edge would give readers a same-model supervisor/worker case whose aggregate gains are positive but whose skill-loading and adherence stages remain unmeasured.
- [Ingest: Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) <-> future PILOT ingest -- **compares-with**: a return edge would contrast fixed-task iterative accumulation with explicit new-task transfer and re-optimization controls on the same benchmark family.
- [Ingest: On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) <-> future PILOT ingest -- **compares-with**: a return edge would place PILOT's two-run best-observed iteration results beside direct repeated-run and shuffled-order tests of textual-memory path dependence.
- [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) <-> future PILOT ingest -- **compares-with**: a return edge would compare two isolated same-model trace-review designs on intervention timing, outcome filtering, and when learned artifacts become visible.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) <-> future PILOT ingest -- **compares-with**: a return edge would point readers from a final-return-only sub-agent API to an explicit live supervisory control channel.

## Reverse-edge Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) → future PILOT ingest -- **evidenced-by**: PILOT is a reported fixed-weight, live-trajectory-to-persistent-skill instance with measured later-iteration outcome and token-efficiency changes.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) → future PILOT ingest -- **evidenced-by**: successful task outcomes decide which run-produced updates survive, but no per-skill process or causal-uptake test establishes each abstraction.
- [Final task success does not establish intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) → future PILOT ingest -- **evidenced-by**: PILOT's trace classification explicitly separates a correction that causally redirects the successful path from an intervention merely followed by success.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) → future PILOT ingest -- **evidenced-by**: the Question/Steer protocol is a current design instance of preserving late-stage worker work through conversational continuation.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) → future PILOT ingest -- **evidenced-by**: PILOT fills a live supervisor-mediated trace-to-skill subtype not named in the current recurring-stage comparison.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- rejected as direct evidence: the supervisor can inspect relevant trajectory portions from a cleaner context, but the paper does not compare trace access, summaries, or diagnostic-context treatments.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- rejected as a separate outbound edge: PILOT's within-episode direct writes and between-iteration success filter raise different governance questions, and the retained-artifact plus checked-outcome candidates state those two supported relations more precisely.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) -- rejected: PILOT retains procedures and memory, but the paper does not show that these artifacts are reusable scheduler `select` strategies rather than benchmark-task or domain skills.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) -- rejected: PILOT implements adjacent trace, activation, and evaluation mechanisms, but the target is a Commonplace-specific plan and the source collection offers only sparse `see-also` into reference; an unadopted analogy would not help source traversal.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) and [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected: their durable scheduler and protected self-modification boundaries are broader than PILOT's paper-reported supervisor/worker channel; Claude Code dynamic workflows supplies the sharper API comparison.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) and [Ingest: Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) -- rejected as regular edges: they sharpen staged trace-to-harness search and offline skill amortization, but Continual Harness, Hermes, and the uptake study better discriminate PILOT's live intervention and retention mechanism.

## Index Membership

- [Agentic Systems](../../../../agentic-systems/README.md) -- a future implementation-grounded PILOT analysis belongs in the whole-system index because live supervisory events, worker lifecycle, context separation, abort semantics, and persistent harness updates are coupled runtime mechanisms rather than only a memory subsystem.
- [Lightweight agent memory systems](../../../../agent-memory-systems/lightweight/README.md) -- if inspection of the source-linked project does not support a code-grounded review, PILOT's skill/memory subsystem merits doc-grounded lightweight coverage; if the implementation is inspectable, route it to `reviews/` instead.

## Synthesis Opportunities

- PILOT, [Continual Harness](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md), and [Hermes Agent](../../../../agent-memory-systems/reviews/hermes-agent.md) together imply that “live learning” needs at least three independent timing fields: **intervention latency** (can oversight redirect the current action path?), **extraction timing** (during a turn, after a turn, or after an episode?), and **activation horizon** (current worker, later worker in the episode, or later task/session). PILOT occupies more than one value at once, so a single online/offline label loses the operative differences.

## Maintenance Observations

- The current trace-learning survey has no named slot for supervisor-mediated extraction that both intervenes in the active trajectory and writes cross-task memory. If PILOT receives a tracked ingest or system review, the survey's ingestion-pattern comparison should decide whether this is a new subtype or a composition of existing live-capture and trajectory-run patterns.

## Flags

- The source is an immutable snapshot and its name-matched ingest did not exist during discovery. Apply accepted outbound and inbound candidates to `kb/sources/pilot-live-self-improvement-long-horizon-agents.ingest.md` after that authored surface is created; never author a durable link to the snapshot.
- Split candidate for the future analysis: the paper independently claims a live steering mechanism, a persistent skill/memory learning mechanism, and iterative outcome/token-efficiency gains. Keep those claim groups separately qualified even if one ingest retains them together.
- The source reports two runs per configuration and best-observed improvement across repeated fixed-task iterations. It does not report shuffled task-order controls, per-skill causal uptake, or independent reproduction; keep those limits attached to any evidence edge.
