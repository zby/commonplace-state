---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md"
source_has_frontmatter: true
date: "2026-07-30"
depth: standard
---

# Connection Report: Promotion, activation, and external triggers

**Source:** [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md)

## Discovery Trace

**Authorisation and curated heads:**
- Read `kb/notes/COLLECTION.md`; prospected the authorised local destinations `notes` (including `notes/definitions`), `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`. `kb/work/` was excluded. External targets are authorised for already-known context only; none was supplied, so external prospecting was skipped without web search.
- Read [Notes](../../../../notes/README.md), [Agent memory](../../../../tags/agent-memory-README.md), [Context engineering](../../../../tags/context-engineering-README.md), and [Failure modes](../../../../tags/failure-modes-README.md). None of the three tag heads declares `complete: true`, so no by-tag search was skipped.
- Read [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), [Sources](../../../../sources/README.md), and [Instructions](../../../../instructions/README.md). `kb/types/README.md` does not exist, so the type destination used its complete title/description surfaces and `kb/types/COLLECTION.md` for reverse-edge authorization.

**Title and description listing scans:**
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for every authorised local destination: notes 324 titles, types 9, reference 124, agent-memory-systems 171, agentic-systems 8, sources 405, instructions 36.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` once for every authorised local destination: notes 321 descriptions, types 13, reference 122, agent-memory-systems 169, agentic-systems 6, sources 345, instructions 85. Follow-up filter `rg -i 'activat|trigger|cue|unprompt|promotion|retention|remember|always.load|behavior|consumer|channel|retriev|memory|delivery|inert'` flagged the candidates evaluated below; no search scores were available.
- Ran the by-tag description recipe `rg -l '^tags:.*\bTAG\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` for `agent-memory`, `context-engineering`, and `failure-modes`. It surfaced the already-linked activation/cost/evaluation cluster plus [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md), [Open-domain memory retention needs a declared output spec](../../../../notes/open-domain-memory-retention-needs-a-declared-output-spec.md), and the routing candidates retained or rejected below.

**Body search:**
- Notes: `rg -l -i 'remember to remember|activation regress|external trigger|external terminator' kb/notes/ --glob '*.md'`; `rg -l -i 'produce-on-request|unprompted application|activation gap|open-versus-probed' kb/notes/ --glob '*.md'`; `rg -l -i 'always-loaded|unconditional loading|loaded unconditionally|event-fired|description scan|firing conditions|delivery path' kb/notes/ --glob '*.md'`; and `rg -l -i 'promotion.*(retention|memory)|retention.*promotion|what to retain|what to store' kb/notes/ --glob '*.md'`. Kept the routing-wire, skill-routing, and authority-vocabulary candidates; rejected narrower hygiene, admission-criterion, and loading-cost matches.
- Definitions/types: `rg -n -i 'activation|trigger|delivery|retention|memory|consumer|channel|behavior' kb/notes/definitions/ --glob '*.md'` and `rg -n -i 'activation|trigger|memory|retention|promot|behavior' kb/types/ --glob '*.md'`. Kept [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) because it names the consumer/channel/force path the source describes implicitly, and [Instruction](../../../../types/instruction.md) because its Operativity contract independently requires a firing path.
- Reference: `rg -n -i 'trigger|activation|activate|always-loaded|always loaded|read-back|delivery path|consumer.*channel|inert' kb/reference/ --glob '*.md'` and `rg -l -i 'retention|promotion|memory.*cost|effect.*behavior|behavior.*effect' kb/reference/ --glob '*.md'`. [Agent memory coverage](../../../../reference/agent-memory-coverage.md) accurately records the current Commonplace gap but adds no mechanism beyond the source and its already-linked requirements; ADR 025 is already linked from the source.
- Agent-memory systems: `rg -n -i 'behavioral faithfulness|activation (test|effect|quality)|tests? whether.*(memory|inject|context).*behavior|on-situation|event.*hook|hook-driven' kb/agent-memory-systems/ --glob '*.md'`. The individual reviews repeat or instantiate the aggregate result already linked through [the comparative review](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md), so no additional review edge was retained.
- Agentic systems: `rg -n -i 'activation|trigger|cue|memory|always-loaded|always loaded|context|hook|retention|promotion' kb/agentic-systems/ --glob '*.md'`. Kept [Swamp](../../../../agentic-systems/reviews/swamp.md), whose schedule and webhook start retained workflows without an agent recalling another artifact; GBrain's scheduled cycle was rejected as redundant evidence.
- Sources: `rg -l -i 'activation gap|unprompted application|produce-on-request|remember to remember|external trigger|external terminator' kb/sources/ --glob '*.md'`; `rg -l -i 'always[- ]loaded|always load|event[- ]trigger|event.*hook|scheduled trigger|trigger.*artifact|delivery path' kb/sources/ --glob '*.md'`; `rg -l -i 'what to retain|what to store|promotion criterion|memory.*promotion|promotion.*memory|retention criterion' kb/sources/ --glob '*.md'`; and `rg -l -i 'behavioral faithfulness|changes behavior|changed behavior|behavioral effect' kb/sources/ --glob '*.md'`. Kept the causal faithfulness study, behavior-trained router study, and trained skill-application boundary case; rejected practitioner restatements without controlled evidence.
- Instructions: `rg -n -i 'activation|activate|trigger|fires|firing|always-loaded|always loaded|promotion|promote|retention|inert|consumer|channel|misses' kb/instructions/ --glob '*.md'`. [Evaluate a log entry for note creation](../../../../instructions/evaluate-log-entry-for-note-creation.md) and [Write an Instruction](../../../../instructions/write-instruction.md) passed the reverse-edge articulation test under the instruction collection's exceptional `rests-on` posture; neither is a clean outbound `operationalized-from` target because neither fully implements the source's four-step activation-package test.

**Link following:**
- Followed one hop from [Skill discovery re-fires in every sub-agent context](../../../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md) through its links to [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md), [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md), and the observed `write-agent-memory-system-review` mitigation. This produced the paired evidence candidates: explicit invocation is reliable, while autonomous description matching is external to the artifact chain but probabilistic.
- Followed [Instruction](../../../../types/instruction.md) to [Operative change](../../../../notes/definitions/operative-change.md) and [Retrieval failure is reflection failure](../../../notes/retrieval-failure-is-reflection-failure.md). The latter was kept because it treats discovery as the causal wire, not merely a convenience; the former is already substantially represented by the source's retained-artifact and effect links.
- Followed [Agent memory coverage](../../../../reference/agent-memory-coverage.md) into the Commonplace gap plan and control-plane references; these document the local gap but do not add evidence beyond the retained type-contract candidate.
- Followed [Swamp](../../../../agentic-systems/reviews/swamp.md) to its memory-subsystem review and scheduler/LLM separation note; neither added a more direct external-terminator case than its scheduled/webhook workflow start.
- Followed the retained source ingests into the already-linked activation/effect requirements and neighboring system reviews. Those neighborhoods confirmed that the selected ingests add distinct evidence (causal uptake, router firing, and trained application) rather than another generic memory-system example.

## Connections Found

- [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) -- **defined-in**: names the consumer, channel, and force path implicit in the source's content-and-delivery package, and explicitly models those paths as composable chains.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) -- **contrasts**: supplies the cold-session case in which project-specific routing must be engineered, while the source adds the boundary that a pretrained disposition can root a path without becoming an author-controlled route.
- [Retrieval failure is reflection failure](../../../notes/retrieval-failure-is-reflection-failure.md) -- **grounds**: establishes discovery as the causal wire from retained representation to later behavior, supplying the premise from which the source follows that the wire itself needs a non-recall-dependent firing condition.
- [Skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **evidenced-by**: contrasts near-certain explicit command invocation with much weaker autonomous routing, directly corroborating the source's distinction between availability and reliable unprompted application.
- [Skill discovery re-fires in every sub-agent context](../../../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md) -- **evidenced-by**: provides an observed case where harness-level description matching terminates the recall chain yet still misfires probabilistically, bounding externality as necessary but insufficient.
- [Instruction](../../../../types/instruction.md) -- **evidenced-by**: the global type contract independently requires every instruction to name what loads it and when it fires, and declares an unconsumed instruction inert despite its persistence and truth.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- **evidenced-by**: its code-grounded schedule and webhook triggers start retained symbolic workflows without an agent first recalling another retained artifact, supplying a mechanical external-terminator case.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **evidenced-by**: causal interventions show condensed experience can be present and injected yet exert little behavioral influence, supporting activation-based promotion and package-level effect testing over presence.
- [Memento-Skills: Let Agents Design Agents](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- **evidenced-by**: measured route-hit and task-success deltas show that an external behavior-trained selector can improve firing while remaining probabilistic and domain-bounded.
- [SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) -- **evidenced-by**: cold-start training teaches a model to retrieve and apply readable skills, supplying a concrete boundary case for the source's claim that a trained disposition can terminate the regress without becoming an author-controlled mechanical path.

## Bidirectional Candidates

- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) <-> source -- **contrasts**: readers of the categorical "routing architectural, not learned" framing need the source's distinction between session-acquired navigation intuition and a trained disposition that can still fire from a live task cue.
- [Skill discovery re-fires in every sub-agent context](../../../../notes/skill-discovery-re-fires-in-every-sub-agent-context.md) <-> source -- **exemplifies** (return edge): the observed autonomous-matching failure is a specific instance of a causally external but unreliable activation trigger, so its readers gain the source's general regress/termination account.

## Reverse-edge Candidates

- [Instruction](../../../../types/instruction.md) → source -- **rests-on**: the type contract's firing-path and inert-instruction rules depend on the source's general claim that retained guidance is unfinished until its activation chain terminates outside retained recall.
- [Evaluate a log entry for note creation](../../../../instructions/evaluate-log-entry-for-note-creation.md) → source -- **rests-on**: its promotion decision currently tests novelty, mechanism, compression, traversal, and prediction; meta-readers need the source's separate delivery gate when revising that procedure.
- [Write an Instruction](../../../../instructions/write-instruction.md) → source -- **rests-on**: its promotion-to-skill steps add runtime discovery and a control-plane route because durable procedure content needs a firing path, not merely a reusable body.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Open-domain memory retention needs a declared output spec](../../../../notes/open-domain-memory-retention-needs-a-declared-output-spec.md) -- rejected because it supplies a domain-level inclusion criterion, while the source asks whether an already-worthy conclusion has activation value and a delivery path; the overlap at "what to retain" does not improve traversal enough.
- [Memory design adds operational axes to artifact analysis](../../../../notes/memory-design-adds-operational-axes-to-artifact-analysis.md) -- rejected because its activation-policy row is a useful router but the source already links the detailed activation, authority, lifecycle-cost, and effects notes the router points toward.
- [Instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- rejected because it restates the cost of always-loaded termination; the source already carries the general cost gate and the concrete ADR-025 capacity case.
- [Periodic KB hygiene should be externally triggered, not embedded in routing](../../../../notes/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) -- rejected as a narrow application of external triggering; the code-grounded Swamp case supplies clearer evidence that a retained workflow can fire without recall.
- [Agent statelessness means the context engine should inject context automatically](../../../../notes/agent-statelessness-means-the-context-engine-should-inject-context.md) -- rejected because it explicitly leaves the trigger mechanism open; the source diagnoses that omission rather than receiving a premise or implementation from it.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- rejected because it faithfully inventories Commonplace's missing on-situation cues and activation tests but does not add a mechanism or observation beyond the source and the retained instruction type contract.
- [The Second Brain Trap](../../../../sources/the-second-brain-trap-2041486539067154753.ingest.md) -- rejected because its trigger-rich-graph recommendation is unmeasured practitioner testimony and is subsumed by the causal faithfulness and behavior-trained-router evidence retained above.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) -- rejected because its scheduled dream cycle is a second external-event example without a reader benefit distinct from Swamp's schedule/webhook case.

## Index Membership

- [Failure modes](../../../../tags/failure-modes-README.md) -- the source names the "remember to remember" regress as a characteristic way relevant retained knowledge can exist without changing behavior and belongs beside the storage/activation and elicitation failures already curated there.
- [Agent memory](../../../../tags/agent-memory-README.md) -- the source sharpens the requirements map by adding an activation-gap promotion criterion and a trigger-termination obligation, making it a strong selective entry under activation or boundaries/failure modes.
- [Context engineering](../../../../tags/context-engineering-README.md) -- the source turns "load the right knowledge at the right time" into a concrete routing test: every intended unprompted delivery path needs a firing event independent of already having surfaced the routed conclusion.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Split candidate: the source independently argues (1) activation gap as a promotion criterion, (2) termination of the activation regress outside retained-artifact recall, and (3) the engineered-trigger versus trained-disposition distinction; the retained candidates span promotion policy, routing architecture, and trigger reliability, so a future author should test whether those claims remain composable as one citation unit.
- Wording tension: [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) can be read to exclude the trained-disposition terminator the source now admits. A future connection edit should preserve the narrower distinction between project-specific routing that cannot accumulate across cold sessions and general routing behavior already installed in model weights.
