---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/same-model-different-harness-different-coding-agent-results.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Same Model, Different Harness: Different Coding-Agent Results

**Source:** [Same Model, Different Harness: Different Coding-Agent Results](../../../../sources/.snapshots/same-model-different-harness-different-coding-agent-results.md)

## Discovery Trace

**Collection, type, and source checks:**

- Read `kb/reports/types/connect-report.md`, `kb/sources/COLLECTION.md`, and the 2,010-line snapshot in full. The snapshot has readable YAML frontmatter. The source collection authorizes local prospecting into `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; it excludes `work` and `instructions`.
- The snapshot is immutable and the matching `kb/sources/same-model-different-harness-different-coding-agent-results.ingest.md` does not exist. Every retained outbound candidate below is therefore for that future ingest's authored surface, not for an edit to this snapshot.
- The independent source-side assertions evaluated were: model-plus-harness as the tested solver; separation of the retained run record from the model-visible working view; the tight-window and wide-window paired results; the closed-loop detector and command-safeguard package; cross-model reuse of one frozen treatment; fail-to-pass fraction as partial-repair evidence; and the package-level, single-trajectory attribution limits.

**Curated heads and topic indexes:**

- Read `kb/notes/README.md` and `kb/notes/tags-README.md`, then followed the promising neighborhoods through `kb/notes/context-engineering-README.md`, `kb/notes/computational-model-README.md`, `kb/notes/evaluation-README.md`, and `kb/notes/agent-memory-README.md`. These routed the source toward the model-plus-runtime evaluation boundary, transcript-versus-working-view policy, retained-evidence separation, context cost, and treatment-grain limits. The source has no `tags` field, so there was no source-tag by-tag sweep.
- Read `kb/reference/README.md` and evaluated the trajectory-evaluation proposal. Read `kb/agent-memory-systems/README.md` and followed its context-virtualization neighborhood into Scroll and Virtual Context. Read `kb/agentic-systems/README.md` and followed its model-harness and evaluation framing into AI Agent Book. Read `kb/sources/README.md` and followed the nearest local harness/context comparisons.

**Complete title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised local destination. The current counts were 414 titles/412 descriptions in `notes`, 159/158 in `reference`, 175/173 in `agent-memory-systems`, 14/12 in `agentic-systems`, and 362/362 in `sources`. These were lexical scans, so no relevance scores were available.

**Notes pass:**

- Ran `rg -n -i 'model.{0,40}harness|harness.{0,40}model|deployed system|tested solver|unit of (learning|evaluation)' kb/notes/ --glob '*.md'`. This retained the deployed-system unit claim and the runtime-decomposition note; broader model-quality hits were rejected when they lacked a paired-harness mechanism.
- Ran `rg -n -i 'chat history|session history|full (run |conversation |execution )?(history|record)|working view|working set|chronological transcript|transcript.*context|history.*default.*context' kb/notes/ --glob '*.md'`. This retained the session-history, chat-history, and preserve-evidence claims; the active-work-state hit was rejected because Yuj does not construct task-state artifacts.
- Ran `rg -n -i 'context pressure|context efficiency|context window|hard cap|prompt tokens|soft degradation|context.*(truncate|shorten|compress)|selective (loading|state projection)' kb/notes/ --glob '*.md'`. This retained the bounded context-efficiency and context-operation-interface candidates. The soft-degradation note was rejected because the paper explicitly studies a harness package, while the tight control often ends at the hard cap.
- Ran `rg -n -i 'paired (comparison|experiment|test)|bundle.*(effect|attribution)|component (study|effect|ablation)|run-to-run variation|one trajectory|partial (repair|progress)|complete (solution|resolution)|trajectory-aware' kb/notes/ kb/reference/ --glob '*.md'`. This retained the treatment-grain note and rejected the trajectory-aware proposal as an unrun evaluator comparison.
- Ran `rg -n -i 'repeated (failure|command)|stalled work|stall pattern|loop detector|detector response|intervention|retry|failure explanation|change (approach|a later (choice|branch))' kb/notes/ --glob '*.md'`. The failure-explanation note passed topical recall but was rejected because the package experiment does not isolate detector messages from working-view shortening or command safeguards.
- Read all mechanism-bearing sections of the eight retained note candidates and followed their one-hop links. The neighborhood confirmed that storage-versus-loading, transcript simplicity, context-operation reach, runtime decomposition, and treatment-grain are distinct reader needs rather than duplicate labels for one claim.

**Reference pass:**

- The paired-experiment search above and the complete reference surfaces flagged [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md). Reading it showed that it proposes a blinded output-only versus trajectory-aware judge comparison, whereas this paper uses output endpoints and operational trace statistics without running that evaluator contrast. No reference candidate survived the articulation test.

**Agent-memory pass:**

- Ran `rg -n -i 'context (virtualization|manager|management)|working (view|set)|compaction|eviction|paging|full (trace|history|record)|chronological|token budget|prompt.*(truncate|shorten|compress)' kb/agent-memory-systems/ --glob '*.md'`. Read Scroll and Virtual Context through their mechanism, comparison, and read-back sections. Both retain raw interaction evidence outside a bounded active view, but they add addressable recovery, summaries, retrieval, or paging that this experiment deliberately does not compare.

**Agentic-systems pass:**

- Ran `rg -n -i 'model.{0,40}harness|harness.{0,40}model|context (assembly|management|window|policy)|working view|conversation history|transcript|evaluation.*harness|tested solver' kb/agentic-systems/ --glob '*.md'`. AI Agent Book survived because it explicitly treats the model-plus-harness system as the evaluation object and asks for paired comparisons, complete trajectories, verifiers, protocols, and statistics; the paper supplies a narrower empirical coding-agent instance.

**Sources pass:**

- Ran `rg -n -i 'same model|model.{0,40}harness|harness.{0,40}model|context pressure|working view|full (chronological )?(transcript|conversation)|paired (comparison|experiment)|context.*(compaction|compression|truncation)' kb/sources/ --glob '*.md'`. Read the retained ACM, Harness Updating, Co-Harness, Effective Harnesses, and Mismanaged Geniuses comparisons through their claims, mechanisms, results, and limitations.
- Followed comparison links among those ingests, the context-operation-interface note, Scroll, Virtual Context, and the deployed-system note. This separated five useful axes: fixed versus learned context control, harness configuration benefit versus harness-edit production, fixed-model versus co-evolved weights, within-run context continuation versus cross-session work continuation, and controlled evidence versus a broad harness-bottleneck hypothesis.
- Ran `rg -n -i 'context regime|window pressure|harness quality|model.?harness.?context|harness.*context.*interaction|solver condition|tested solver' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'` to check the synthesis candidate. Hits discussed harness quality or the model-harness boundary, but none stated the context-regime interaction retained below.
- External prospecting was skipped as required. The arXiv URL already present in snapshot metadata is source identity, not a discovered external connection; no other external target was supplied.

**Candidate verification:**

- Verified every retained and rejected local path with `test -f`. No `Connections Found` target is raw text.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the paired study holds model weights, tasks, context capacity, tool interface, serving setup, evaluator, and run protocol fixed while changing one harness configuration package, directly showing that unchanged weights can produce different user-visible results when surrounding runtime policy changes.
- [Session history should not be the default next context](../../../../notes/session-history-should-not-be-the-default-next-context.md) -- **is-evidence-for**: Yuj retains the full in-memory conversation and trace files while rebuilding a smaller model-visible view under pressure, and that storage-versus-loading separation is part of a package that improves tight-window outcomes; the experiment does not isolate the view policy from the other treatment components.
- [The chat-history model trades context efficiency for implementation simplicity](../../../../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) -- **is-evidence-for**: the control is exactly a full chronological transcript that stops when the window fills, while the treatment changes the working view; tight-window gains and fewer prompt tokens per turn on wide Verified make the claimed bounded-context tradeoff observable.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **rests-on**: the paper correctly limits its causal result to one treatment package, declines to assign gains to shortening, detector responses, or safeguards separately, and calls for component ablation and repeated runs.
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../notes/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **is-evidence-for**: Yuj's context rebuilding, closed-loop intervention policy, full retained record, and tool execution occupy separable causal roles even though one harness implements them, which lets a reader see why the observed package effect is not one undifferentiated “model” effect.
- [A context-operation interface bounds the projections its policy can realize](../../../../notes/context-operation-interface-bounds-context-policy.md) -- **compares-with**: the paper evaluates one host-owned mechanical view policy against full-history loading while explicitly leaving model summaries, semantic state, retrieval, and other operation sets outside scope; the note explains why success in that pair cannot establish interface adequacy against those unrun alternatives.
- [Preserve Evidence Without Making History The Next Context](../../../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) -- **is-evidence-for**: the treatment keeps the complete run record and full trace files available while withholding older bulk from ordinary model input, providing a within-run coding-agent instance of the capture-versus-activation requirement rather than evidence about cross-session memory.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **is-evidence-for**: the tight-window comparisons show feasibility gains when the control hits its context boundary, while the wide-window results report both smaller outcome gaps and fewer prompt tokens per turn on Verified; this supports separate feasibility and token-cost faces within the tested coding regimes, not the note's broad priority claim by itself.
- [Scroll](../../../../agent-memory-systems/reviews/scroll.md) -- **compares-with**: both keep a recoverable interaction record and preserve recent tool results while reducing older model-visible bulk under pressure, but Scroll adds tiered address maps, validated continuation summaries, structured recall, and programmable access that Yuj's deliberately mechanical treatment omits.
- [Virtual Context](../../../../agent-memory-systems/reviews/virtual-context.md) -- **compares-with**: both let a host-owned layer mutate the live request while retaining raw trace evidence, but Virtual Context uses generated summaries and facts, retrieval ranking, paging, and restore handles; the comparison names major alternatives that the paired Yuj experiment does not test.
- [AI Agent Book](../../../../agentic-systems/reviews/ai-agent-book.md) -- **compares-with**: the book's doctrine treats the model-plus-harness system as the evaluation object and calls for task definitions, protocols, verifiers, trajectories, paired comparisons, and statistics; this paper supplies a narrowly controlled coding-agent case while retaining its single-trajectory and package-attribution ceilings.
- [Ingest: ACM: Agentic Context Management for Long Horizon Tasks](../../../../sources/acm-agentic-context-management-for-long-horizon-tasks.ingest.md) -- **compares-with**: ACM lets a learned controller invoke summarization, raw-prefix archiving, and later retrieval, whereas Yuj uses a fixed host trigger and deterministic age-tier shortening without semantic state or recall; comparing them prevents either result from being generalized to context management as one treatment.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: Harness Updating separates production, loading, procedural match, and downstream benefit for persistent harness changes, while this paper directly measures downstream task effects from a fixed configuration change without studying update production or causal uptake of any one component.
- [Ingest: Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: Co-Harness alternates mixed-form harness repair with weight updates and leaves their coupling under-isolated, while this paper fixes weights and changes only one harness package; together they mark sharply different intervention and attribution boundaries.
- [Ingest: Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) -- **compares-with**: the practitioner report argues that compaction alone does not provide cross-session work continuity without explicit progress state, requirements, commits, and verification; Yuj shows within-run working-view management can help under pressure but does not test that longer persistence problem.
- [Ingest: The “Mismanaged Geniuses” Hypothesis](../../../../sources/the-mismanaged-geniuses-hypothesis-2042588627260018751.ingest.md) -- **compares-with**: the hypothesis treats human-engineered scaffolds as a capability and measurement bottleneck but offers broad conceptual and example-level support; the paired paper supplies controlled evidence for the weaker claim that harness configuration mediates observed capability, not for the stronger claim that decomposition policy is the main frontier bottleneck.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. Durable source links must target tracked ingests, never `.snapshots/`, and the matching ingest does not yet exist. The strongest future return-link cases can be reconsidered after that authored target is created.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Soft degradation often binds before the hard cap when required evidence fits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- rejected because the paper explicitly says it studies the harness rather than context pressure itself, and the tight control commonly terminates at the hard context boundary; it does not isolate degradation before the cap while required evidence still fits.
- [Failure explanation changes later branch decisions](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- repeated-failure detector messages can redirect later work, but the experiment bundles those messages with view shortening and command safeguards, so it cannot establish the note's explanation-specific mechanism.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- Yuj preserves and mechanically shortens a chronological interaction record; it does not construct the explicit goals, next actions, blockers, evidence, and completion gates that make active work state a different artifact.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- the paper retains complete traces and reports operational statistics, but it does not compare output-only and trajectory-aware judges or evaluate process compliance, so the proposal would add topical adjacency without a tested shared contrast.

## Index Membership

None. The future ingest belongs in the sources collection but is not a member of the note, reference, agent-memory-system, or agentic-system indexes; any later Yuj whole-system analysis would be a separate artifact with its own index decision.

## Synthesis Opportunities

- This source plus [the deployed-system unit claim](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [the contrast-identification rule](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md), and [the context-operation-interface claim](../../../../notes/context-operation-interface-bounds-context-policy.md) imply a higher-order claim not yet captured: **a measured harness effect is conditional on the resource regime, not an intrinsic harness ranking**. Tight-window gains, wide-window convergence on two benchmarks, and a residual FeatureBench gap show why evaluation should report the interaction among model, harness configuration, context capacity, time endpoint, and task distribution rather than export one package delta as generic harness quality.

## Maintenance Observations

None

## Flags

- **Split candidate:** the source connects to more than five notes across whole-system evaluation, runtime decomposition, context engineering, agent memory, and experimental inference, and it makes independent solver-boundary, working-view, closed-loop-intervention, metric, and empirical claims. A future ingest should keep those analytical strands separate even though one ingest remains the correct source unit.
- **Unresolved compression tension:** the session-history note recommends goal-oriented rather than uniform compression, while this treatment uses deterministic age-tier shortening and reports gains. The package design prevents attributing those gains to mechanical shortening alone, so the result qualifies the design prior without resolving it.
- **Attribution ceiling:** each arm has one greedy trajectory per task and the intervention is a package. A future ingest should preserve both the absence of run-to-run variance estimates and the absence of component effects, especially when discussing the detector responses or cross-model reuse.
