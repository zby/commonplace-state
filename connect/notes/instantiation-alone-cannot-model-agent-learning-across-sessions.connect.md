---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Instantiation alone cannot model agent learning across sessions

**Source:** [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md)

## Discovery Trace

**Destination: notes**

- **Curated heads:** Read [Notes](../../../../notes/README.md), [Computational model](../../../../tags/computational-model-README.md), [deploy-time-learning](../../../../tags/deploy-time-learning-README.md), and [Learning theory](../../../../tags/learning-theory-README.md). None of the source tag READMEs declares `complete: true`, so I did not skip the tag-scoped sweep.
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — flagged [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md), and [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) as the strongest unlinked neighbors.
- **Description listing scan:** `rg '^description:' kb/notes/ --glob '*.md'` plus `rg -l '^tags:.*\b(computational-model|deploy-time-learning|learning-theory)\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` — kept the five candidates above because each fills a distinct gap the source currently leaves implicit: the whole-system learning boundary, the retained-artifact update path, the governance problem for behaviour-changing writes, the addressability requirement on writable retained state, and the specific reflective advantage of revising prior commitments. I rejected several nearby hits as already linked or weaker continuations, especially [LLM contexts interpret instructions and content through one medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md), which the source already cites directly.
- **Body search:** `rg -n 'instantiation|class|instance|cross-session|durable definition|update relation|behavior-determining organization|placement|frontloading|ephemeral computation|proposal-selection|reflection|reflective|addressability|deployment-time adaptation' kb/notes/ --glob '*.md'` — confirmed that:
  - [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) directly supports the source's opening move that a durable definition includes prompts, retrieval, tools, validators, and runtime policy rather than weights alone.
  - [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) states the broader update path the source models as the missing second relation beyond startup instantiation.
  - [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) supplies the general governance frame for the source's claims about writable placement, validation, authority, and retained update.
  - [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) explains why the source's writable update surfaces are readable artifacts rather than tacit retention forms.
  - [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) sharpens what the source's reflective-system aside buys: explicit revision and rescoping of earlier commitments, not merely generic substrate change.
- **Link following:** Followed the kept candidates and the source's existing links to [behavior-determining organization](../../../../notes/definitions/behavior-determining-organization.md), [reflective system](../../../../notes/definitions/reflective-system.md), [frontloading](../../../../notes/frontloading-spares-execution-context.md), [ephemeral computation](../../../../notes/ephemeral-computation-prevents-accumulation.md), [promotion](../../../../notes/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md), and [the proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). That pass reinforced that the missing value is not more placement-policy machinery — already linked — but the surrounding boundary, governance, and addressability frame.

**Destination: reference**

- **Curated head:** Read [Reference](../../../../reference/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/reference/ --glob '*.md'`
- **Body search:** `rg -n 'always-loaded|cross-session|promotion|activation|authority|behavior-determining|memory|control-plane' kb/reference/ --glob '*.md'`
- **Evaluation:** [Agent memory coverage](../../../../reference/agent-memory-coverage.md) and [Control-plane goals](../../../../reference/control-plane-goals.md) were the strongest descriptive prospects. I rejected both as outbound candidates from this source: they are useful Commonplace-specific witnesses, but the note already has a strong theoretical spine and the tighter reader need is the missing note-level theory and source evidence, not a shipped-system instance.

**Destination: agent-memory-systems**

- **Curated head:** Read [Agent Memory Systems](../../../../agent-memory-systems/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`
- **Body search:** `rg -n 'always-loaded|memory file|promotion|trace-learning|rollback|self-modif|activation|authority' kb/agent-memory-systems/ --glob '*.md'`
- **Evaluation:** promising hits included [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md), [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md), and [Exo](../../../../agent-memory-systems/reviews/exo.md). None survived the articulation test as first outbound edges from this note: each is narrower than the source's general class/instance-versus-update argument, and the kept note/source candidates already cover the needed mechanism at a better abstraction level.

**Destination: agentic-systems**

- **Curated head:** Read [Agentic Systems](../../../../agentic-systems/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/agentic-systems/ --glob '*.md'`
- **Body search:** `rg -n 'self-modif|versioned|rollback|governed|behavior-determining|promotion|reflective|executor' kb/agentic-systems/ --glob '*.md'`
- **Evaluation:** [Exo](../../../../agentic-systems/reviews/exo.md), [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md), and [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) were the strongest prospects. I rejected them as outbound edges from this source: Exo and Autogenesis are good case studies of governed self-modification, and dynamic workflows is a good startup-surface case, but the source's immediate missing traversal is still the note-level frame and the missing Self rival-paradigm citation, not a whole-system case study.

**Destination: instructions**

- **Curated head:** Read [Instructions](../../../../instructions/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/instructions/ --glob '*.md'`
- **Body search:** `rg -n 'cross-session|promotion|activation|authority|behavior-determining|always-loaded|memory file|session' kb/instructions/ --glob '*.md'`
- **Evaluation:** no instruction survived the articulation test. The notes collection contract says notes → instructions is usually inverse, and this pass did not reveal an `operationalized-from` or high-value `see-also` exception for this source.

**Destination: sources**

- **Curated head:** Read [Sources](../../../../sources/README.md).
- **Full titles listing:** `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`
- **Description listing scan:** `rg '^description:' kb/sources/ --glob '*.md'`
- **Body search:** `rg -n 'class-instance|prototype|self|metaobject|monkey patch|deopt|release handling|code loading|cross-session|retained adaptation' kb/sources/ --glob '*.md'`
- **Evaluation:** the source already links its strongest reflective-mutation pricing evidence — [Metaobject Protocols](../../../../sources/metaobject-protocols-why-we-want-them-and-what-else-they-can-do.ingest.md), [Monkey patch](../../../../sources/monkey-patch.ingest.md), [Fast properties in V8](../../../../sources/fast-properties-in-v8.ingest.md), [Erlang/OTP release handling](../../../../sources/erlang-release-handling.ingest.md), and [Erlang/OTP compilation and code loading](../../../../sources/erlang-compilation-and-code-loading.ingest.md). One additional hit survived: [SELF: The Power of Simplicity](../../../../sources/self-the-power-of-simplicity.ingest.md), whose own ingest explicitly identifies itself as the missing rival-paradigm attestation for this note's prototype-based contrast.

**External destination**

- Authorized by the notes collection contract, but no already-supplied external artifact needed evaluation because the relevant external evidence has already been ingested locally. Open-web prospecting was therefore skipped.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **grounds**: the source's durable-definition startup relation only works if prompts, retrieval, tools, validators, and runtime policy belong to the learning boundary rather than being treated as fixed scaffolding around the model.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **mechanism**: the source's missing second relation beyond instantiation is exactly the retained-artifact update path this note names and generalizes.
- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **grounds**: the source's claims about writable placement, validation, authority, and later-session effects are a concrete instance of that note's broader governance requirement.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **mechanism**: the source treats skill files, routing rules, validators, and memory stores as revisable update surfaces; this note explains why readable explicit artifacts, rather than tacit retention forms, are the currently governable substrate for that role.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) -- **extends**: the source distinguishes startup instantiation from reflective update; this note develops the payoff of that distinction into explicit rejection, rescoping, and revision of earlier commitments.
- [SELF: The Power of Simplicity](../../../../sources/self-the-power-of-simplicity.ingest.md) -- **evidenced-by**: the source invokes prototype-based OO as a rival paradigm to a fixed class plan; this ingest is the direct primary attestation for that rival and for the specific tradeoff between class plans and prototype cloning.

## Bidirectional Candidates

- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) <-> source -- **extends**: the source sharpens that framework with a specific startup-versus-update model and makes revisable content placement one concrete update surface.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) <-> source -- **extends**: the source contributes a worked consequence of that whole-system boundary by showing why a class/instance startup analogy fails unless later sessions can revise the durable definition they inherit.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [LLM contexts interpret instructions and content through one medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) -- rejected because it is already linked in the source body, so it is not a candidate new connection.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- rejected because it catalogs startup surfaces the source already enumerates; the stronger missing reader need is the surrounding learning/governance frame, not another catalog.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- rejected because it is a good practical continuation, but the more load-bearing missing step is the broader retained-artifact and whole-system frame that the kept notes provide.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) -- rejected because it is a useful Commonplace-specific witness, but this note's first missing outbound need is general theory plus the missing Self source, not a descriptive shipped-system map.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected because it is a strong governed-self-modification case study, but it is a narrower and more system-specific continuation than the kept note-level candidates.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) -- rejected because its trace-to-memory-file pipeline is an interesting placement case, but it is too specific to user-model compilation to serve as the clearest next hop for this source's general update-relation argument.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- this curated head covers context composition, frontloading, orchestration, and instruction semantics, but it omits this note's class/instance and reflective-update model for startup versus cross-session revision.
- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) -- the curated head covers retained artifacts, coevolution, and feedback quality, but it omits this note's specific account of cross-session learning as revision of the durable definition plus its placement policy.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
