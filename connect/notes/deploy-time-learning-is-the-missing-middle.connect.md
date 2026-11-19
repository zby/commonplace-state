---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/deploy-time-learning-is-the-missing-middle.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Retained system-definition artifacts enable persistent deployment-time adaptation

**Source:** [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md)

## Discovery Trace

### Scope and source reading

- Read the report type, the complete source artifact, and the notes collection contract before discovery. The source claim is lifecycle-specific: deployment evidence selects and retains a behavior-shaping artifact change that can affect later executions without entering model weights. Its practical advantage is conditional on bounded impact and evaluation, not on readable artifacts being intrinsically faster or uniquely capable of deployment-time updates.
- The notes contract authorizes local prospecting in kb/notes/, kb/types/, kb/reference/, kb/agent-memory-systems/, kb/agentic-systems/, kb/sources/, and kb/instructions/; it excludes kb/work/. The reserved external destination is authorized for already-known targets only. No unlinked external target was supplied or remained in the final source, so external prospecting was skipped and no browsing was performed.
- sha256sum kb/notes/deploy-time-learning-is-the-missing-middle.md returned the supplied final hash, 598768afdf45496947dd2d717ee4056195874584ff965bfd7c7b310b25ca7986.
- Fresh full-title and description surfaces were generated with rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md' | wc -l and rg '^description:' kb/<destination>/ --glob '*.md' | wc -l. Counts were: notes 350/347, types 10/13, reference 132/130, agent-memory-systems 172/170, agentic-systems 12/10, sources 487/423, and instructions 44/97.

### kb/notes/

**Curated heads and scoped descriptions:**

- Read [Notes](../../../../notes/README.md), [Learning theory](../../../../tags/learning-theory-README.md), and [deploy-time-learning](../../../../tags/deploy-time-learning-README.md). learning-theory-README.md declares covered_by but not complete; deploy-time-learning-README.md also lacks complete, so neither tag allowed the by-tag searches to be skipped.
- rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r '' produced 115 descriptions; the corresponding deploy-time-learning query produced 30.
- rg '^description:' kb/notes/ --glob '*.md' | rg -i 'deploy|continual|adapt|retention|persistent|system-definition|model.weight|validation|rollback|proposal-selection|evidence-responsive|localized|impact closure' surfaced the localization, retained-instruction, oracle-accumulation, self-improving-system, reflection, and readable-artifact neighborhoods.

**Body search:**

- rg -n -i 'deployment[- ]time|deploy[- ]time|system-definition|model[- ]weight|model weights|artifact revision|operative retention|retained change|persistent adaptation|localized.*(artifact|retention)|impact closure|evidence-responsive|proposal-selection' kb/notes --glob '*.md' found the source's mechanisms and the stronger boundary notes.
- rg -l 'deploy-time-learning-is-the-missing-middle' kb/notes --glob '*.md' and the equivalent per-collection inbound searches identified existing return links and exposed pre-rethesis link contexts.
- rg -n -i '^.*\[[^]]+\]\([^)]*deploy-time-learning-is-the-missing-middle\.md[^)]*\).*$' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/instructions --glob '*.md' distinguished already-authored support from stale claims about the old title, three-timescale table, speed, and agile framing.

**Link following and evaluation:**

- Followed [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) to reflection, the readable-artifact loop, Parnas's decomposition criterion, retrieval failure, and the bitter-lesson boundary. Kept it because it states the exact three-part condition—matching units, explicit dependencies, and small impact closure—needed by the source's conditional localization claim.
- Followed [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) to proposal selection, committed ground truth, and recompute cost. Kept it because it isolates why evaluation plus retention adds reusable procedure even when candidate content was already generable from model weights.
- Followed [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) through the readable-artifact loop, spec mining, and the tag-README trace. Kept it as the concrete check/test branch of the source's general artifact path.
- Rejected [Self-improving system](../../../../notes/definitions/self-improving-system.md) as a direct connection: it requires a declared boundary, objective, operative path, and causal uptake, while the source establishes a deployment-time adaptation path and permits human proposal or approval without making a self-improvement attribution.
- Rejected [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) as a new edge because [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md), already linked by the source, carries the needed comparison and routes onward to reflection.
- Rejected [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md): later behavioral effect is required for operativity, but the source does not claim that an earlier gain causally improves a later improvement episode.
- Rejected [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md): it explains why heuristic artifacts exist, not the evidence-selection-retention path by which they adapt.
- Rejected [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) as a new outbound edge because it already links inbound to the source and the source already links context efficiency for the narrower bounded-context reader need.

### kb/types/

- Read [Types](../../../../types/README.md). No matching tag README exists.
- rg '^description:' kb/types/ --glob '*.md' | rg -i 'instruction|review|note|definition|system|behavior|artifact' and rg -n -i 'system-definition|retained|behavio(u)?r|learning|adapt|persistence|rollback' kb/types/ --glob '*.md' made [Instruction](../../../../types/instruction.md) the only plausible hit.
- Rejected the instruction type: its operativity rule says a retained instruction needs a consumer and channel, but a global type contract is not evidence for the deployment-time adaptation claim and adds no mechanism beyond the source's existing system-definition definition.

### kb/reference/

- Read [Reference](../../../../reference/README.md). No matching tag README exists.
- rg '^description:' kb/reference/ --glob '*.md' | rg -i 'self-improv|reflect|adapt|retention|artifact|validation|rollback|learning|behavior', rg -n -i 'deploy[- ]time|continual learning|continuous learning|self-improv|reflective' kb/reference/ --glob '*.md', and rg -n -i 'system-definition|artifact revision|versioned.*artifact|rollback|evaluation.*retention|operative retention' kb/reference/ --glob '*.md' concentrated the live evidence in the Commonplace reflective-system cluster.
- Followed [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) to the declared frame, the causal trace, and the proposal-selection reading. Kept the classification because it records an observed natural-language-and-symbolic artifact change that altered later validation and agent search behavior while provider weights remained outside the declared frame.
- Rejected [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) as an additional source edge because the classification already routes to the detailed trace and gives the more economical evidence surface.
- Rejected [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) as evidence because it is unadopted and its source description cites wording removed by the final rethesis.

### kb/agent-memory-systems/

- Read [Agent Memory Systems](../../../../agent-memory-systems/README.md). No matching tag README exists.
- rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'trace|skill|rule|workflow|self-improv|learning|frozen|weight|persistent|retention|rollback', rg -n -i 'deploy[- ]time|deployment[- ]time|continual learning|continuous learning|frozen model|frozen weights|model weights|token[- ]space' kb/agent-memory-systems/ --glob '*.md', and rg -n -i 'durable.*(skill|rule|prompt|artifact)|persistent.*(skill|rule|prompt|artifact)|trace-learning|evaluate.*retain|rollback' kb/agent-memory-systems/ --glob '*.md' surfaced the cross-system survey and several individual implementations.
- Followed [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) through its promotion-target comparison and into [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md), SkillWeaver, and EQUIPA. Kept the aggregate because it compares code-inspected promotion into readable artifacts and model weights while making evaluation, not extraction or retention alone, the recurring boundary.
- Rejected Agent Workflow Memory, SkillWeaver, and EQUIPA as separate source edges. AWM has weak artifact provenance and no item-level faithfulness test; SkillWeaver and EQUIPA already author inbound links; all three are represented more economically by the aggregate survey plus the stronger source-level experiments below.

### kb/agentic-systems/

- Read [Agentic Systems](../../../../agentic-systems/README.md). No matching tag README exists.
- rg '^description:' kb/agentic-systems/ --glob '*.md' | rg -i 'self-evolv|self-improv|skill|prompt|artifact|version|rollback|learning|adapt' and rg -n -i 'deploy[- ]time|deployment[- ]time|continual learning|continuous learning|self-improv|co-evol|frozen model|weights|prompt|skill|artifact' kb/agentic-systems/ --glob '*.md' surfaced GBrain, Autogenesis, Exo, and weaker versioned-runtime matches.
- Followed [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) into its code-grounded memory review. Kept it because SkillOpt implements the source's narrow causal shape: scored rollouts, reflected skill edits, a reject-capable median gate, retained Markdown instructions, and later host-agent consumption, with human review retained for bundled skills.
- Followed [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) into its paper ingest and proposal-selection/readable-artifact neighborhood. Kept it as the complementary broad-resource case: prompts, tools, memory, skills, and code share versioning, mutation, rollback, and evaluation hooks, while the report preserves the important caveat that current semantic selection is weaker than its commit machinery.
- Rejected [Exo](../../../../agentic-systems/reviews/exo.md): protected history and rebuild/rollback make self-revision recoverable, but its broader recursive harness boundary is less discriminating for the source's artifact-selection claim than GBrain's gated skill loop and Autogenesis's uniform resource lifecycle.

### kb/sources/

- Read [Sources](../../../../sources/README.md). No matching tag README exists.
- rg '^description:' kb/sources/ --glob '*.md' | rg -i 'skill|rule|workflow|harness|self-improv|learning|frozen|weight|persistent|retention|rollback|deploy-time', rg -n -i 'deploy[- ]time|deployment[- ]time|continual learning|continuous learning|frozen model|frozen weights|without (weight|fine-tun)|outside (of )?weights|token[- ]space' kb/sources/ --glob '*.ingest.md', and rg -n -i 'durable.*(skill|rule|prompt|artifact)|persistent.*(skill|rule|prompt|artifact)|versioned.*(skill|rule|prompt|artifact)|evaluate.*retain|rollback|cross[- ]task transfer|held[- ]out transfer' kb/sources/ --glob '*.ingest.md' surfaced direct experiments, production observations, and conceptual restatements.
- Followed [SkillOpt](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) through its readable-artifact, diagnostic-richness, and related-skill comparisons. Kept it because a frozen target model, bounded skill-text edits, a strict held-out reject gate, and deployment of only the retained winner instantiate the source's proposal/evaluation/retention path cleanly.
- Followed [Memento-Skills](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) through its routing, mutation, Voyager, SkillOpt, SkillRL, and faithfulness neighbors. Kept it because controlled read/write ablations show later behavior changing through a rewritten natural-language-plus-symbolic skill folder around a frozen LLM, with domain alignment and a trained router explicitly bounding the result.
- Kept [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) because its frozen-artifact transfer experiment isolates a retained external artifact across tasks and model families; its benchmark oracles and fixed adapter bound how far that evidence transfers to open-ended system-definition artifacts.
- Kept [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) because its agent/evolver cross-pairings separate producing a persistent harness edit, loading it, judged procedural match, and downstream benefit—the uptake distinctions the source's “affects later behavior” clause needs.
- Kept [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) as a naturalistic production case, with the context phrase preserving its uncontrolled design and instance-to-rule oracle gap.
- Rejected [Agent Workflow Memory ingest](../../../../sources/agent-workflow-memory.ingest.md) as an additional edge because its benchmarked workflow evidence is narrower and is already represented by the trace-learning survey; its rule-based near-match and weak item lifecycle make it a useful survey component rather than a distinct source for this note.
- Rejected [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md): its substrate-by-horizon matrix is an independent conceptual restatement, not empirical evidence, and the source now states the lifecycle/form orthogonality directly.
- Existing [OpenClaw-RL ingest](../../../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) was evaluated as already authored by the source rather than repeated as a candidate.

### kb/instructions/

- Read [Instructions](../../../../instructions/README.md) and the instruction collection contract because the notes contract says the usual useful direction is inverse, instruction → note via rests-on. No matching tag README exists.
- rg '^description:' kb/instructions/ --glob '*.md' | rg -i 'instruction|skill|improv|review|revise|retain|promot|system' and rg -n -i 'deploy[- ]time|deployment[- ]time|continual learning|persistent adaptation|system-definition|artifact revision|evaluate.*retain|improvement loop|rollback' kb/instructions/ --glob '*.md' made [Write an Instruction](../../../../instructions/write-instruction.md) and [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) the closest candidates.
- Rejected both reverse edges. Write an Instruction operationalizes stable-core abstraction but does not require deployment evidence or an evaluation-selected retained change. The full-improvement pass performs evaluation and retention over knowledge notes, but does not depend specifically on the source's system-definition-artifact lifecycle claim. No exceptional operationalized-from edge passed.

**Verification:** Every kept, bidirectional, rejected, and maintenance-observation path named below was checked with test -f; all exist.

## Connections Found

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) — **extends**: states the matching, explicit-dependency, and small-impact-closure conditions under which the source's claimed localization and rollback advantage actually holds.
- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) — **mechanism**: explains why evaluation plus retention creates reusable procedural value even when model weights could regenerate every candidate.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) — **extends**: develops the source's “tests” case into a deployment-time path where retained checks alter the selection environment for later proposals.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) — **evidenced-by**: records one observed, bounded natural-language-and-symbolic change that revised later validation and agent behavior while provider weights remained outside the frame.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — **evidenced-by**: compares many code-inspected trace-to-artifact and trace-to-weight paths, corroborating the source's timing/form separation while locating evaluation as the common promotion boundary.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) — **evidenced-by**: its SkillOpt path evaluates and retains Markdown skill edits that later host agents consume, with explicit mutation, gating, and human-review boundaries.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) — **evidenced-by**: its versioned resource lifecycle makes prompts, tools, memory, skills, and code mutable and rollbackable without weight updates, while its weak semantic gate bounds what “evaluated” warrants.
- [SkillOpt ingest](../../../../sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md) — **evidenced-by**: scored rollouts, bounded text edits, strict held-out selection, and deployment of the retained winner demonstrate readable external policy learning around frozen target models.
- [Memento-Skills ingest](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) — **evidenced-by**: controlled read/write ablations show durable mixed-form skill folders improving later behavior around a frozen LLM, with domain alignment and parametric routing as explicit boundaries.
- [Knowledge-Centric Self-Improvement ingest](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — **evidenced-by**: held-out cross-task and cross-model transfer isolates a frozen retained artifact as the carrier of later behavior change, while benchmark oracles and a fixed adapter bound the result.
- [Harness Updating Is Not Harness Benefit ingest](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) — **evidenced-by**: controlled cross-pairings separate persistent update production, loading, judged procedural match, and downstream benefit, sharpening the causal-uptake condition behind later behavioral effect.
- [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules ingest](../../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.ingest.md) — **evidenced-by**: accepted review feedback becomes versioned cross-session instruction rules in a production deployment, with the uncontrolled design and instance-to-rule oracle gap limiting the inference.

## Bidirectional Candidates

- [A retained instruction preserves what testing selected](../../../../notes/a-retained-instruction-preserves-what-testing-selected.md) → source — **exemplifies**: the retained tested instruction is one concrete instance of persistent deployment-time adaptation through a system-definition artifact.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) → source — **is-evidence-for**: the survey's code-inspected readable-artifact cases materially support the existence and boundaries of the deployment-time path the source names.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) → source — **is-evidence-for**: SkillOpt is a shipped, code-grounded instance of deployment evidence selecting and retaining a behavior-shaping instruction change.
- [Memento-Skills ingest](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) → source — **is-evidence-for**: the controlled frozen-LLM experiment directly bears on the source's claim that evaluated retained artifacts can carry persistent adaptation outside model-weight updates.

## Reverse-edge Candidates

None. The instruction-first inverse-direction pass found no procedure that depends specifically enough on this lifecycle claim to justify rests-on; other useful inbound directions are paired with outbound candidates above.

## Off-authorisation Candidates

None. Every retained candidate fits an authorized source→destination label; no plausible connection required inventing or broadening the notes collection vocabulary.

## Raw Text Candidates

None. Source snapshots were not used as authored targets; their frontmatter-bearing .ingest.md companions carry the candidate evidence edges.

## Rejected Candidates

- [Self-improving system](../../../../notes/definitions/self-improving-system.md) — importing this definition would silently add boundary, objective, self-change, and causal-uptake obligations the source does not claim for every deployment-time adaptation path.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) — the already-linked explicit-retention synthesis carries this reader need and routes onward.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — persistent later behavior is not yet causal contribution to a later improvement episode.
- [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) — explains artifact motivation rather than deployment-time selection and retention.
- [Instruction type](../../../../types/instruction.md) — its consumer/channel requirement is a contract, not corroborating evidence for the learning path.
- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) — redundant detail behind the kept Commonplace classification.
- [Agent Workflow Memory](../../../../agent-memory-systems/reviews/agent-workflow-memory.md) — the aggregate survey gives a better comparative route and the implementation lacks item-level faithfulness and mature lifecycle controls.
- [Exo](../../../../agentic-systems/reviews/exo.md) — its whole-harness self-rebuild surface is less specific to the source's artifact-selection mechanism than the two kept agentic cases.
- [Agent Workflow Memory ingest](../../../../sources/agent-workflow-memory.ingest.md) — narrower empirical support already represented by the aggregate survey and stronger skill-artifact experiments.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) — conceptual convergence rather than evidence, with no additional mechanism beyond the source's final lifecycle/form decomposition.
- [Write an Instruction](../../../../instructions/write-instruction.md) — repeated-operation abstraction does not require an evidence-responsive deployment loop.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) — updates knowledge artifacts and does not depend specifically on persistent system-definition adaptation.

## Index Membership

None. The source is already linked from the notes landing, learning-theory head, and deploy-time-learning head; those memberships need wording maintenance rather than a new index entry.

## Synthesis Opportunities

None. The strongest apparent synthesis—separating retained update production, causal uptake, and bounded validation—is already divided across the self-improving-system definition, the harness-benefit evidence, and the localized-retention note; a new note would duplicate that established decomposition.

## Maintenance Observations

- The final rethesis changed the H1 but left the old filename and many old-title link texts. More importantly, [Notes](../../../../notes/README.md), [Learning theory](../../../../tags/learning-theory-README.md), and [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) still describe the target as a “missing middle,” a three-timescale framework, or agile-style coevolution. The deploy-time head's summary now contradicts the final note's explicit statement that lifecycle phase is not an exclusive timescale category.
- Several inbound notes still import claims the final source removed: [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) calls this the faster-than-retraining “fast-loop requirement”; [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) attributes an agile-style argument to it; [The verifiability gradient](../../../../notes/verifiability-gradient.md), [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md), [Human–LLM differences are load-bearing for knowledge-system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md), [Three-space agent memory echoes Tulving's taxonomy but the analogy remains untested](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md), and [LLM learning phases fall between human learning modes](../../../../notes/llm-learning-phases-fall-between-human-learning-modes.md) still cite a removed three-timescale model.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) quotes the removed sentence “a system that can only tighten ratchets itself into brittleness.” It now points at a source that no longer supplies that claim.
- [OpenClaw-RL ingest](../../../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) still says it challenges the target's three-timescale model and recommends revising the framework to allow weight updates during deployment. The final target now makes exactly that repair, so the ingest's description, connection text, limitation framing, and recommended next action are stale.

## Flags

None. The final note remains one composable claim; no split candidate, unresolved candidate conflict, or no-connections finding arose.
