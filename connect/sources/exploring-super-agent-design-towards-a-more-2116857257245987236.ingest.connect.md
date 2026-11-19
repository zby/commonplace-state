---
description: "Post-ingest connection discovery for DeepSeek Harness's Router/Worker proposal, separating scheduling-cost evidence, recall interfaces, and unresolved coordination and security guarantees."
type: types/connect-report.md
source: "kb/sources/exploring-super-agent-design-towards-a-more-2116857257245987236.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Exploring Super-agent Design: Towards a More Autonomous Agent System

**Source:** [Exploring Super-agent Design ingest](../../../../sources/exploring-super-agent-design-towards-a-more-2116857257245987236.ingest.md)

Discovery only. These are candidates for future authoring, not changes to library artifacts. The first three outbound candidates refine connections already present in the ingest; the remaining six are additional candidates. Evidence judgments below use the ingest, not a newly inspected implementation or snapshot.

## Discovery Trace

### Authorization and method

Read the complete source, sources collection contract, connect-report type, reports collection contract, and validation skill. The sources contract permits prospecting theory, reference, historical agent-memory systems, agentic systems, tags, and other sources; instructions and work are excluded. Sources may use `is-evidence-for` for theory and historical agent-memory systems; `compares-with` for theory, sources, and both system collections; `see-also` for the same destinations plus reference. Definition and lineage labels were not needed. No agents or external search services were used.

For each of the six local destinations, read its root `README.md` and generated the complete fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered the truncated listing through the tool's saved output. The source has no `tags:`; no source-tag membership search or completeness skip applied.

For every destination, ran the description listing `rg '^description:' kb/<destination>/ --glob '*.md'`, filtered with `rg -i 'schedul|rout(er|ing)|orchestrat|progressive|pointer|recall|subscription|persistent|watchdog|coordination|asynchron|brain.*hands|session history'`. Also ran both body passes per destination:

- `rg -n -i 'subscription|pass-through|watchdog|inline.{0,5}spill|chain of recall' kb/<destination>/ --glob '*.md'`
- `rg -l -i 'event.driven|router.{0,30}worker|atomic.{0,20}(claim|ownership)|brain.{0,20}hands' kb/<destination>/ --glob '*.md'`

No similarity scores were produced by these repository-local searches.

### Theory

The title and description scans surfaced scheduler–LLM separation, pointer tradeoffs, coordination guarantees, session-history selection, context-operation interfaces, privilege quarantine, and the orchestration design-space map. Read each in full. Kept the first five relevant outbound routes below, including the source's existing three connections. Read `kb/theory/COLLECTION.md` for the reverse-edge pass: `evidenced-by` into sources is authorized for observations that corroborate, qualify, or bound a claim. Retained three inbound candidates with explicitly bounded uses, not claims of broad corroboration.

The design-space map is useful framing but adds less than the three precise mechanism routes; rejected as an additional generic edge. The context-operation note is best used inbound: the new ingest supplies a bounded graph-recall example for its architecture comparison, rather than establishing that the proposed interface is adequate.

### Reference

The root README and full title scan led to replaceable workflow orchestrators. The description scan also returned navigation and archived code-scheduled-workflow proposals. Read the replaceable-orchestrators proposal fully. Rejected it: its contract-equivalence and interrupted-publication requirements are not evaluated by the target's synthetic scheduling tests. Body hits for subscription/pass-through were skill-stub and billing uses, not event-routing mechanisms. No reference edge retained.

### Historical agent-memory systems

The README routes current analysis elsewhere but preserves historical comparisons. Description scanning surfaced Scroll, Letta, Spacebot, and several recall services. Chose Scroll for full reading because its title/description promised tiered eviction maps and programmable recall, a direct comparison with Inline & Spill and Chain of Recall. Kept the comparison on recoverability, addressability, and exposure controls, not learning quality. The specific body pass found subscriptions in Semiont and TheKnowledge, but those hits did not establish a closer Router/Worker or recoverable-context comparison. Did not retain a keyword-only edge.

### Agentic systems

The README, titles, and descriptions identified beads_rust's transactional claims. Read its review fully and kept the contrast between a notification channel and actual local claim exclusion. The review explicitly limits the guarantee to the CLI/local database route; generic MCP updates and separate Git branches do not inherit it. Watchdog and subscription hits in archived reports and matrix rows concerned request liveness or unrelated data-delivery paths. No stronger source-specific edge was justified by those hits, so none was retained.

### Tags

Read the tags root and the computational-model and context-engineering heads. Both lack `complete: true`. Their curated links supplied the session-history, coordination, and context-operation candidates. No by-tag scan was required by source metadata, and the complete title/description passes already covered the authorized collections. Tags are a prospecting/index surface here: the sources contract authorizes scanning tags but supplies no ordinary sources-to-tags relationship label. No direct tag edge or index-membership addition is proposed. Source-scoped tags are optional and do not make this ingest a generated participating member.

### Other sources

Titles and descriptions surfaced Managed Agents, folding subagents, Slate, runtime-independent agents, and scheduler-theoretic execution. Read Managed Agents and folding subagents fully. Retained the first for the concrete compute/state/execution and credential-boundary comparison; retained the second because it supplies a scoped rival to mandatory Router/Worker decomposition. Slate and the scheduler position paper offered less incremental value than the theory routes and the two sharper source comparisons; they were not promoted from scan hits.

### Link following and checks

Followed the coordination note's link to the orchestration design-space map, then its link to session-history selection. Followed the historical-memory README and Scroll review to the context-operation note, whose architecture discussion distinguishes legal projections from achieved retrieval quality. Followed the folding-subagents ingest's existing link to the Managed Agents ingest. These neighborhoods produced the selective-history and concrete interface comparisons rather than a broad orchestration spray.

Ran `rg -n -i 'pointer|selective|retention|credential|asynchron'` over the loaded session-history, context-operation, Scroll, beads_rust, and Managed Agents artifacts to check the retained axes. Verified all twelve evaluated artifact paths with `Path.is_file()` before report inclusion.

External prospecting was skipped. The source URL is already known provenance; repeating its `derived-from` relationship offers no new discovery value. No external pages or ignored snapshots were opened.

## Connections Found

- [Scheduler–LLM separation](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — **is-evidence-for**: the source bears on the cost of repeated model-mediated routing because subscription pass-through reduces cache-read tokens from 31.8M to 23.2M within the fixed Router/Worker design. This is a synthetic inference-cost example, not a test of total reliability cost. Existing source connection; preserve this bound.
- [Pointer design tradeoffs](../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) — **compares-with**: Chain of Recall's summaries and related-object IDs give an agent concrete pointers for successive retrieval; the note supplies axes for assessing their specificity, availability, cost, and accuracy. Reachability is not measured retrieval quality. Existing source connection.
- [Coordination guarantees, not just channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: many-to-many Thread notifications let Workers notice overlapping work but do not specify atomic ownership or write consistency. The note identifies the missing guarantee a concurrent KB writer must demand. Existing source connection; treat this as an architectural gap, not an observed collision.
- [Session history should not be the default next context](../../../../theory/session-history-should-not-be-the-default-next-context.md) — **compares-with**: Inline & Spill and graph-based recall separate retaining task/session history from exposing selected content, giving a concrete alternative to transcript inheritance without claiming successful months-long memory.
- [Privilege quarantine](../../../../theory/orchestration-needs-privilege-quarantine-not-permission-scope.md) — **see-also**: the source leaves untrusted-event influence over credential-bearing endpoints unresolved; this companion names the direct read/act privilege boundary to inspect before adoption and the indirect poisoned-output risk that remains. Router non-execution alone is not evidence that quarantine is enforced.
- [Scroll](../../../../agent-memory-systems/reviews/scroll.md) — **compares-with**: both approaches retain history outside bounded active context and expose compact recall pointers. Scroll's reviewed implementation adds persistence-before-eviction, bounded recall, read-only history, and explicit retention limits; these make concrete comparison questions for Inline & Spill rather than presumed properties of the proposal.
- [beads_rust](../../../../agentic-systems/reviews/beads-rust.md) — **compares-with**: its CLI compare-and-set claim supplies the local ownership exclusion that Thread notification alone does not specify. The review's MCP and Git boundary caveats prevent mistaking one local atomic claim for distributed shared-write safety.
- [Scaling Managed Agents](../../../../sources/scaling-managed-agents-decoupling-brain-from-hands.ingest.md) — **compares-with**: both separate computation, retained session state, and execution environments; Managed Agents supplies a practitioner account of stable interfaces and credential isolation against which to inspect the proposal's personal-machine endpoint risk. Neither account establishes adversarial safety.
- [When to fold subagents into the main loop](../../../../sources/building-agents-fold-subagents-into-main-loop.ingest.md) — **compares-with**: this practitioner account favors removing unnecessary routers and specialist loops, whereas the target structurally prevents the Router from executing tasks. Their different workloads and bundled comparisons motivate testing responsiveness and context isolation separately, not declaring either topology generally superior.

## Bidirectional Candidates

None. Inbound theory uses are listed separately below; no mirror links are proposed merely for symmetry.

## Reverse-edge Candidates

All three are authorized by `kb/theory/COLLECTION.md` as theory-to-sources `evidenced-by`. A future writer should place the citation in claim-bearing prose, not only in a footer. The ingest currently retains no quotes; the source-use check must be made runnable through the appropriate grounding workflow before durable adoption.

- [Scheduler–LLM separation](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) → source — **evidenced-by**: add the within-architecture pass-through ablation as a bounded inference-cost example. It qualifies the broader cost conjecture: no end-to-end reliability, correction burden, or implementation-maintenance comparison was run. This is the highest-priority inbound candidate and matches the ingest's recommended next action.
- [Pointer design tradeoffs](../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) → source — **evidenced-by**: add Chain of Recall as a proposal-level example of successive summary-and-ID navigation. The case illustrates an interface and leaves pointer accuracy and navigation outcomes untested; it does not corroborate a performance ranking.
- [Context-operation interface bounds context policy](../../../../theory/context-operation-interface-bounds-context-policy.md) → source — **evidenced-by**: its architectural contrasts could include related-object traversal as a distinct addressable interface beside structured and programmable recall. The target bounds what is known: scheduling tests do not test recall-interface adequacy, achieved retrieval, or long-term memory quality.

## Off-authorisation Candidates

None. No substantive candidate required a label absent from its source-to-destination authorization. Tag heads were used for discovery, not forced into an unauthorized ordinary edge.

## Raw Text Candidates

None.

## Rejected Candidates

- [Replaceable workflow orchestrators](../../../../reference/proposals/replaceable-workflow-orchestrators.md) — shared orchestration terminology does not make the target evidence for portable workflow contracts, acceptance parity, or recovery semantics. The more specific scheduling theory route is sufficient.
- [Orchestration design-space map](../../../../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — useful during discovery, but a general taxonomy edge adds little after the scheduler, pointer, and coordination routes identify the precise comparison axes.

## Index Membership

None. Sources are outside generated tag participation, and no curated landing examined needs this one source as an editorial entry.

## Synthesis Opportunities

None. The loaded notes already separate scheduler placement, context selection, and coordination guarantees. The new proposal supplies cases and test questions, not a distinct higher-order claim requiring another note.

## Maintenance Observations

- The computational-model head's scheduler–LLM separation blurb still says symbolic operations are error-correctable through redundancy while LLM bookkeeping compounds errors silently. The current note instead argues direct enforcement of defined transitions, permits reliable model-mediated bookkeeping, and states a total-cost conjecture. A later index-maintenance pass should reconcile the blurb with that note. Neither was edited here.

## Flags

- Split candidate for downstream theory extraction: nine outbound candidates span scheduling, retrieval, coordination, runtime boundaries, and security, and the source makes multiple independent assertions. Preserve the ingest as one source-identity record; do not import its entire architecture into one theory claim.
- Unresolved topology tension: mandatory Router non-execution and fold-subagents advice concern different workload and context regimes. Neither bundled comparison isolates the structural choice well enough to settle the general design question.
- Evidence boundary: the target is an analysis of a translated design proposal with synthetic scheduling experiments, not an implementation inspection. No connections should upgrade it to coding-quality evidence, demonstrated long-term recall, concurrency safety, or secure autonomous operation.
