---
description: "Candidate connections from the harness compositional generalization preprint to Commonplace's orchestration, context assembly, and strategy-retention work."
type: types/connect-report.md
source: "kb/sources/.snapshots/language-model-harnesses-compositional-generalizers.md"
source_has_frontmatter: true
date: "2026-11-20"
depth: standard
---

# Connection Report: Language Model Harnesses Can Be Compositional Generalizers

**Source:** Language Model Harnesses Can Be Compositional Generalizers, local snapshot at `kb/sources/.snapshots/language-model-harnesses-compositional-generalizers.md`. No tracked ingest pairs with this snapshot.

The preprint tests whether a harness can make an unfamiliar whole task solvable through familiar individual calls. The Recursive Language Model (RLM) keeps the corpus and intermediate results outside the root model's prompt. The root writes code that selects what fresh model calls see and combines what they return. In the tested tasks, transfer across length or domain depended on both a reusable root strategy and reliable local work. Pi's OOLONG failure shows why similar root traces alone are not enough (§3.3, Appendix D.4–D.5). The paper also tests training on synthetic tasks that preserve the target decomposition (§4.2) and training the model to hand each task in a gated chain to a fresh harness instance (§4.3). These are results for the tested tasks, models, and configurations, not evidence that arbitrary KB work decomposes this way.

## Discovery Trace

- **Scope and heads.** Read the snapshot in pages through Appendix D.5 and read the collection landings at `kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/README.md`. Also read `kb/tags/{computational-model,context-engineering}-README.md`: the former surfaced the decomposition heuristics; both surfaced the context-operation interface note. The agentic-systems landing surfaced Fractal and Claude Code dynamic workflows. The historical memory landing suggested Scroll and Virtual Context as interface analogues. The snapshot has no `tags:` field, so no by-tag `rg` pass was needed. No prospecting in `kb/work/` or `kb/instructions/`.
- **Titles.** For each of the six destinations above, ran `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/$d/ --glob '*.md' --glob '!*.brief.md'` with a display filter on composition, recursion, scheduling, trajectory, and named harnesses. Generated 441 theory, 258 reference, 175 agent-memory-systems, 156 agentic-systems, 35 tag, and 610 source titles before filtering. Resolved promising titles with `rg -l -F -x`, including the RLM orchestration and persistence notes, Tendril, and the LongCoT case study. The similarly titled ingest turned out to be the earlier practitioner post; there is no tracked ingest for the exact preprint target.
- **Descriptions.** In each destination ran `rg '^description:' kb/$d/ --glob '*.md'` filtered with `rg -i 'compositional generaliz|bounded.context (call|schedul)|trajectory.as.a.prompt|context offload|programmatic (sub|tool)|recursive language model|surrogate (harness|train)|projections its policy|context degrad|harness.*(weight|post.train)|prime agent|fractal|source.adoption'`. This confirmed Fractal and the earlier ingest, and identified Prime Agent and the source-adoption policy for comparison. A narrower theory description pass (`rg -n '^description:' kb/theory/*{operation-interface,ephemeral-orchestrators,scheduling,design-space}*.md`) confirmed the distinct roles of the interface, heuristics, orchestration, and design-space notes.
- **Body search.** In each destination ran `rg -il 'locally in.distribution|compositional generalization|trajectory.as.a.prompt|surrogate harness training' kb/$d/ --glob '*.md'` and `rg -il 'programmatic (sub.calls?|tool calling|sub.agent)|context offload|model.authored orchestrator|context.operation interface' kb/$d/ --glob '*.md'`. The hits reinforce the RLM mechanism and interface distinction. Scroll and Virtual Context share offloaded state, but their links from the interface note already lead to the relevant comparison and neither supplies the paper's strategy-transfer test. The tags yielded navigation, not another distinct evidence target. `rg -l '2611\.harness-cg|language-model-harnesses-compositional-generalizers\.ingest' kb --glob '*.md'` found no existing preprint references. These searches produced no ranked scores.
- **Link following and reverse pass.** Followed the earlier post ingest to the RLM orchestration note, the restriction/persistence comparison, the soft degradation note, and Fractal. The RLM note explicitly anticipates weight-based strategy retention. The persistence comparison leads to Tendril, whose executable registry provides a concrete contrast; it also cautions against inferring REPL disposal from a within-run trace. Followed the LongCoT ingest to the orchestration design-space note: its distinction between where a strategy runs and where it is learned is directly useful. Followed the Fractal review to Claude Code dynamic workflows and the strategy/run-state persistence note. The latter is a reverse-only candidate because a reader needs the paper to qualify its account of the costs of not saving generated code. Checked theory's outbound and source-grounding rules for these reverse paths. Reviewed the reference landing and the trajectory-aware evaluation and write-context assembly proposals; neither tests or implements the mechanism this preprint evaluates.
- **External.** No external prospecting. The canonical preprint URL is already in the snapshot and is the ordinary `derived-from` provenance for a future ingest, not an additional discovery candidate.

### Candidate origins

- kb/theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md — titles, descriptions, body-search, link-following
- kb/theory/context-operation-interface-bounds-context-policy.md — curated-head, titles, descriptions, body-search, link-following
- kb/theory/decomposition-heuristics-for-bounded-context-scheduling.md — curated-head, titles, descriptions, link-following
- kb/theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md — body-search, descriptions, link-following
- kb/sources/language-model-harnesses-are-compositional-generalizers.ingest.md — titles, descriptions, body-search
- kb/sources/mini-exercise-mismanaged-geniuses-longcot-rlm.ingest.md — titles, link-following
- kb/agent-memory-systems/reviews/tendril.md — titles, link-following
- kb/agentic-systems/reviews/fractal.md — curated-head, titles, descriptions, link-following
- kb/agentic-systems/reviews/claude-code-dynamic-workflows.md — curated-head, titles, link-following
- kb/theory/orchestration-strategies-and-run-state-have-opposite-persistence.md — link-following

## Connections Found

These are candidates for a future ingest of the exact preprint, not for the snapshot or the earlier post's ingest.

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — **is-evidence-for**: Appendix D.4's OOLONG trace pair shows the root generating the same batching-and-counting strategy for 787 and 6,374 records. The larger task requires more sub-calls, not a larger root prompt containing every record. This bears on the mechanism, not on whether generated code is discarded after return.
- [A context-operation interface bounds the projections its policy can realize](../../../../theory/context-operation-interface-bounds-context-policy.md) — **is-evidence-for**: §§3–4 show both changes in behavior after training within one harness and contrasts among harnesses with different callable operations. Read the former as better use of available operations, not expanded interface reach; read the latter at configuration grain, since the CodeAct variant changes output truncation as well as removing programmatic sub-calls.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) — **is-evidence-for**: GraphWalks illustrates exact processing outside the prompt; OOLONG illustrates local semantic labeling followed by symbolic aggregation. Pi's partial-label runs show what fails when one call returns labels for only part of its assignment. This is not evidence for open-ended KB synthesis.
- [Agent orchestration occupies a multi-dimensional design space](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — **is-evidence-for**: §4.2 adds a concrete acquisition path: synthetic, mostly root-level traces train a model to generate symbolic strategies at run time without changing the harness code. This separates learning the strategy from executing it.
- [Earlier practitioner post on compositional generalization](../../../../sources/language-model-harnesses-are-compositional-generalizers.ingest.md) — **compares-with**: compare evidence coverage: the post reports short-to-long and structural transfer; the preprint adds surrogate training, gated recursion, and local sub-task accuracy checks. Keep the reported ranges attached to their respective observations; shared authorship and overlapping experiments are not independent replication.
- [Mismanaged Geniuses LongCoT case study](../../../../sources/mini-exercise-mismanaged-geniuses-longcot-rlm.ingest.md) — **compares-with**: compare acquisition interventions inside an RLM: trace-derived prompt tips for brute-force and unchecked child answers versus synthetic-example training for decomposition and handoff. The LongCoT before/after result bundles several prompt changes and is not a head-to-head test.
- [Tendril](../../../../agent-memory-systems/reviews/tendril.md) — **compares-with**: compare what a later run can reuse: the preprint trains a tendency to regenerate a decomposition, while Tendril re-executes named workspace code. The latter has an inspectable artifact, not evidence of the same transfer effect.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — **compares-with**: both let model-authored Python select material and invoke sub-calls; the inspected Fractal runtime wraps the whole turn in that pattern and retains session summaries and traces. This gives a concrete implementation contrast, not a Fractal benchmark result.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) — **compares-with**: the RLM code can operate directly on the offloaded corpus before dispatch; the workflow script cannot read it directly and must receive data or delegate enumeration. Compare which parts of a corpus workflow each orchestration interface can do without putting text in a model call.

## Bidirectional Candidates

These return links depend on a tracked exact-preprint ingest; use retained quotes sufficient for the claim or mark the ingest citation `(snapshot required)`.

- [RLM orchestration note](../../../../theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) → future preprint ingest — **evidenced-by**: the paper gives the note's proposed weight-learning route a measured instance. Cite §4.2 as a qualification of the loss implied by not retaining generated code, not as evidence about the REPL's post-return lifecycle.
- [Orchestration design-space note](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) → future preprint ingest — **evidenced-by**: add surrogate training as a distinct acquisition case alongside trace-derived tips and searched workflows. Preserve the boundary: the recursion hint alone reduced full-chain success for RLM-27B, while the additional trained package improved it in the selected chain task; that package also changed the prompt and turn allocation.

## Reverse-edge Candidates

- [Orchestration strategies and run-state have opposite persistence economics](../../../../theory/orchestration-strategies-and-run-state-have-opposite-persistence.md) → future preprint ingest — **evidenced-by**: qualify the note's re-derivation cost claim. Related tasks can reuse a tendency to generate the same strategy without retrieving the previous executable. The paper does not compare that path with reuse of a tested library fragment or estimate when the latter pays. Use the theory contract's tracked-ingest grounding rule, not a snapshot link.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Source-adoption policy](../../../../reference/source-adoption-policy.md) — it governs borrowing in general; the paper supplies no evidence about that policy or any Commonplace adoption.
- [Trajectory-aware evaluation](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — trajectory similarity is a diagnostic for strategy reuse, not the proposal's test of whether a judge catches workflow violations missed by an output-only judge.
- [Soft degradation before the hard cap](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — relevant background, but the main harness contrast also varies execution, training, and in some cases window extension. Keep the more specific interface and decomposition links; do not use the paper to identify a soft-bound effect in isolation.
- [Prime Agent archive review](../../../../agentic-systems/reviews-archive/prime-agent.md) — related runtime, but not the tested RLM. Tendril and Fractal already carry the executable-retention and session-trace contrasts without treating Prime Agent's live refinement as equivalent to offline weight training.

## Index Membership

None. The snapshot does not participate in tag membership. The [computational model head](../../../../tags/computational-model-README.md) and [context engineering head](../../../../tags/context-engineering-README.md) were useful navigation, not proposed entries for the snapshot. The latter concerns how calls are assembled, not model training itself.

## Synthesis Opportunities

The [decomposition heuristics](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) and [interface reach note](../../../../theory/context-operation-interface-bounds-context-policy.md) imply three separate checks for a KB workflow expected to transfer: can the interface supply an appropriate input to each call, does the orchestrator select a suitable split on the new task, and do the local results retain what the merge needs? The paper's high-similarity Pi failure shows why the second check cannot substitute for the third. Test the three separately before attributing a workflow gain to scoping or to the learned strategy.

## Maintenance Observations

- The RLM orchestration and strategy/run-state notes assert disposal after each query, while the [restriction/persistence comparison](../../../../theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md) leaves that lifecycle unclassified from its cited material. Resolve with implementation-specific evidence. The preprint's within-run traces and weight-training results answer different questions and do not settle disposal.

## Flags

- No exact-preprint ingest exists. The similarly named July post has a different URL and checksum. Do not use it to ground the preprint's surrogate-training or recursion results.
- If the findings become durable theory, treat strategy transfer, surrogate training, and trained recursive handoff separately. The results vary different interventions and have different limits. In particular, Table 6's full solve rate rises from 55.2% to 77.5% for the trained RLM-27B chain package on selected tasks; it does not establish a general advantage from adding recursion alone.
