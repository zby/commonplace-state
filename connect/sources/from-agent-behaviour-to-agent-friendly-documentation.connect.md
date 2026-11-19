---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/from-agent-behaviour-to-agent-friendly-documentation.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: From Agent Behaviour to Agent-Friendly Documentation

**Source:** [From Agent Behaviour to Agent-Friendly Documentation](../../../../sources/.snapshots/from-agent-behaviour-to-agent-friendly-documentation.md)

The snapshot is immutable. These candidates belong on its future authored companion, `kb/sources/from-agent-behaviour-to-agent-friendly-documentation.ingest.md`, or on the target side where a reverse edge is independently useful.

## Discovery Trace

**Collection contract and authored surface:**

- Read `kb/sources/COLLECTION.md`; it authorizes prospecting in notes, reference, agent-memory systems, agentic systems, and sources, excludes work and instructions, and places snapshot-authored candidates on the matching ingest report.
- Read `kb/cache/types/connect-report.md` and the complete 1,807-line snapshot. The snapshot has frontmatter but no tags, so no matching tag-README or by-tag `rg` pass applied.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the context-engineering, document-system, agent-memory, evaluation, failure-modes, observability, and links curated heads. They routed prospecting toward human/agent audience differences, contextual activation, active-work state, verification, and the read-or-skip model of agent navigation.
- Read the reference, agent-memory-systems, agentic-systems, and sources collection heads. Reference supplied no direct candidate beyond local implementation context; Claude Workstream Kit was the strongest agent-memory comparison; no agentic-system analysis passed as strongly as the source and memory comparisons retained below.

**Complete title surfaces:**

- Generated fresh `rg -N --no-heading -m1 '^# '` listings for `kb/notes/` (360 headings), `kb/reference/` (140), `kb/agent-memory-systems/` (173), `kb/agentic-systems/` (12), and `kb/sources/` (296). Candidate titles clustered around agent instructions, dual audiences, activation, active work, actionability, verifiability, context files, navigation decisions, and instruction-following evaluation.

**Description listing scans:**

- `rg -n '^description:' kb/notes --glob '*.md' | rg -i 'instruction|documentation|context file|agent-facing|working (note|memory)|actionab|verifi|system-definition|control plane|consumption|loading|retriev|read|navigat'` kept the human/LLM, activation, active-work, actionability, verifiability, and navigation-decision candidates below.
- `rg -n '^description:' kb/reference --glob '*.md' | rg -i 'instruction|documentation|context|agent|control|routing|validation|review'` surfaced Control-plane goals and the review/evaluation machinery, but these describe Commonplace rather than sharpening the source's claims.
- `rg -n '^description:' kb/agent-memory-systems kb/agentic-systems --glob '*.md' | rg -i 'instruction|context|working|trace|document|coding agent|memory|verification|agent-facing'` kept Claude Workstream Kit and rejected broader harness matches.
- `rg -n '^description:' kb/sources --glob '*.md' | rg -i 'AGENTS\.md|CLAUDE\.md|documentation|context file|instruction.follow|coding agent|working note|agent.behavio|verifi'` kept the three source comparisons below.

**Body searches:**

- `rg -n -i 'agent instruction|AGENTS\.md|CLAUDE\.md|context files?' ...` surfaced the context-file inventory, the control-plane theory, Harness-IF, and source-level studies of agent-facing Markdown.
- `rg -n -i 'working notes?|active work state|thoughts/|verification logs|agent_working_note' ...` kept Active work state and Claude Workstream Kit because they distinguish a lifecycle-governed work surface from the paper's aggregate working-note category.
- `rg -n -i 'actionab|verifiab|read.{0,20}(act|edit|implement)|consult.{0,30}(test|build|validat)' ...` kept Actionable methodology and The verifiability gradient, while exposing that the paper's operational meanings should not be imported as Commonplace's technical vocabulary without qualification.
- `rg -n -i 'follow-reference|further read|read doc|navigation decision|information scent|locally retrievable' kb/notes kb/sources --glob '*.md'` kept Agents navigate by deciding what to read next and rejected the broader Linking theory: the trace corpus observes repeated reads and zero explicit Follow-reference events, but not pointer cues, follow/skip judgments, or decision cost.
- `rg -n -i 'no measurement of agent behavior|shape(s|d)? (agent )?behavior|instruction.{0,30}(behavior|compliance)|context file.{0,30}(effect|behavio)' kb/sources --glob '*.ingest.md'` kept Context Engineering for AI Agents in OSS, Harness-IF, and Emerging Markdown Formats as complementary presence, compliance, and taxonomy studies.
- `rg -n -i 'active work state|working note|session-start|AGENTS\.md|CLAUDE\.md' kb/agent-memory-systems --glob '*.md'` kept Claude Workstream Kit and showed that most other hits concern generic session-start memory rather than the paper's work-in-flight documents.

**Link following:**

- Followed Human-LLM differences into Design for the first-time human and the earlier OSS context-file ingest. The new paper supplies behavior-side evidence but does not support treating all human/agent differences as one mechanism.
- Followed Knowledge storage does not imply contextual activation into its storage-to-context and context-to-action split. The paper's consultation traces bear on the second transition, while its instrument cannot observe automatically loaded context files.
- Followed Active work state into the workshop-layer note and Claude Workstream Kit. This exposed the paper's broad `agent_working_note` category as a useful prevalence signal but not yet a lifecycle or memory architecture.
- Followed Actionable methodology and The verifiability gradient into their definitions and scope. The source tests neither Commonplace's operator-relative actionability relation nor the gradient across symbolic forms; it instead observes weak or absent behavioral sequences around repository-local prose.
- Followed Agents navigate by deciding what to read next into Linking theory and its Pirolli ingest. The source gives agent-side evidence that documentation reads occur in runs, but its zero Follow-reference count and purpose-free event coding cannot establish whether proximal cues improved a follow-or-skip decision.
- Followed Context Engineering for AI Agents in OSS, Harness-IF, and Emerging Markdown Formats through their existing limitations. Together with this source they form a measurement ladder from file presence and taxonomy, through consultation, to rule-level compliance; none alone establishes downstream task benefit.

## Connections Found

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- **is-evidence-for**: the paper finds that coding agents' observed documentation activity is dominated by agent instructions and agent working notes rather than the human-centered API and troubleshooting genres emphasized by prior documentation research.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: explicit documentation consultation most often leads to further reading or reasoning, its association with code editing changes under adjustment, and no explicit documentation-based validation sequence appears, supplying bounded ordinary-workflow evidence for a context-to-action gap.
- [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -- **compares-with**: documentation reads often lead to another read, which is consistent with repeated selection among information sources, but the study records zero explicit Follow-reference events and does not observe pointer cues or latent follow-or-skip judgments; it therefore supplies an agent-trace boundary, not a validation of the note's decision-cost model.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- **compares-with**: the paper's `agent_working_note` category establishes the prominence of plans, thoughts, brainstorms, and verification logs, while the note separates live state by pointers, gates, closure, and extraction rather than by filename or prose durability.
- [Actionable methodology](../../../../notes/definitions/actionable-methodology.md) -- **compares-with**: the paper treats “actionability” as an assumed document quality operationalized through read-to-action behavior, whereas Commonplace reserves the technical term for an operator-relative methodology–operations–target relation; the ingest should keep those meanings visibly separate.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- **compares-with**: the paper finds no observed prose-as-oracle sequence and proposes executable documentation as an intervention hypothesis, while the note predicts tighter loops as artifacts move from loose prose toward schemas, tests, and deterministic code; the observational zero does not test that cross-form gradient.
- [Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) -- **compares-with**: the earlier study measures which context files projects contain and how a small active subset evolves but not agent behavior, whereas this paper measures explicit consultation and production while remaining unable to see automatic startup exposure or causal instruction effects.
- [Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) -- **compares-with**: Harness-IF scores atomic rule compliance and controls for prior-aligned behavior, while this paper observes naturally occurring document interactions; together they separate encountering documentation from following an instruction.
- [Emerging Markdown Formats That Shape Coding Agent Behavior](../../../../sources/emerging-markdown-formats-that-shape-coding-agent-behavior.ingest.md) -- **compares-with**: the practitioner essay proposes roles for standing rules, skills, plans, domain context, and local memory, while this paper supplies behavioral prevalence and exposes the large working-note category without validating the essay's normative routing advice.
- [Claude Workstream Kit](../../../../agent-memory-systems/reviews/claude-workstream-kit.md) -- **compares-with**: the code-grounded kit gives one working-note family explicit session-start read-back, active pointers, evidence gates, and closure, providing a concrete lifecycle comparison for the paper's broad category while still lacking a faithfulness test of downstream behavioral uptake.

## Bidirectional Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) <-> source -- **is-evidence-for / evidenced-by**: the ingest can use the note to frame why the distribution matters, and the note can cite the paper as bounded behavior-side evidence that coding-agent documentation use differs from the human-centered literature it inherits.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) <-> source -- **is-evidence-for / evidenced-by**: the note supplies the storage/context/action distinction, while the source adds an observational coding-work corpus in which explicit reads do not show a consistent immediate implementation-and-verification path.
- [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) <-> source -- **compares-with / evidenced-by**: the note supplies a general follow-or-skip model, while the source shows recurrent explicit document reads and also exposes that its trace schema cannot identify cue-guided link traversal.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) <-> source -- **compares-with / evidenced-by**: the note can cite the paper for the scale and prominence of agent working artifacts while stating that the paper's unvalidated path classifier and aggregate category do not establish the lifecycle distinction.

## Reverse-edge Candidates

- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -> source -- **evidenced-by**: add the paper as empirical evidence about coding-agent documentation consumption and production, scoped to explicit repository-local file interactions.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -> source -- **evidenced-by**: add the consultation-to-action and absent-validation results as ordinary-workflow evidence, retaining the paper's first-order/three-event horizons and inability to observe model-internal use.
- [Agents navigate by deciding what to read next](../../../../notes/agents-navigate-by-deciding-what-to-read-next.md) -> source -- **evidenced-by**: use the recurrent-read result as bounded agent-side evidence for repeated source selection, while stating that zero explicit Follow-reference events means the study does not measure link-cue quality or individual follow/skip decisions.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -> source -- **evidenced-by**: cite the paper for the observed prevalence of plans, thoughts, brainstorms, and verification logs, while treating the exact 25.1% share as provisional because the category rests on unvalidated LLM path classification.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [AGENTS.md should be organized as a control plane](../../../../notes/agents-md-should-be-organized-as-a-control-plane.md) -- rejected as a direct evidential edge: the paper shows that instruction files are a prominent interaction surface, but it does not compare short routers with embedded procedures or test the note's layering and placement rules.
- [Linking theory](../../../../notes/linking-theory.md) -- rejected as a direct edge: the paper's trace taxonomy can motivate a future measurement design, but it does not observe cue diagnosticity, target utility, or context cost and therefore cannot test navigation-uncertainty reduction per token.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- rejected as a primary connection because the paper explicitly cannot observe context files automatically injected at session start; its explicit-read counts are lower bounds on exposure.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- rejected because the paper measures documentation interaction rather than a memory intervention's causal effect; Knowledge storage does not imply contextual activation is the narrower fit.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) -- rejected in favor of Claude Workstream Kit, which exposes the active-work artifacts and lifecycle in inspected code rather than a bundled practitioner recommendation.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected as too broad: it contains agent-facing instructions, plans, and retained solutions, but the source-level studies and Claude Workstream Kit isolate the paper's measurement and working-note questions more directly.

## Index Membership

None.

## Synthesis Opportunities

The source, [Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md), and [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) jointly support a staged evaluation model for agent-facing documentation: artifact presence and evolution, automatic or explicit exposure, behavioral uptake or rule compliance, and downstream task effect are distinct measurements. [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) already supplies the central distinction, so extend that note with the three-study ladder rather than creating a duplicate synthesis note.

## Maintenance Observations

None.

## Flags

- **Split candidate:** the source makes independent claims about document-type prevalence, consultation triggers and transitions, working-note production, code/document ordering, validation, and recovery. The ingest should keep empirical findings, measurement limits, and design implications distinct rather than collapse them into one “agent-friendly documentation” thesis.
- **Observation boundary:** SWE-chat exposes explicit repository-local file interactions but not automatic startup injection, browser documentation, model-weight knowledge, docstrings, or model-internal reasoning. The AIDev analysis exposes file changes but no tool-use trajectories. The two datasets are complementary populations, not cross-validation.
- **Classifier boundary:** the `agent_working_note` category was discovered through LLM classification of ambiguous paths and has not received human validation. Its qualitative prominence is more defensible than the exact 25.1% share.
- **Vocabulary boundary:** the paper's “actionability” and “verifiability” are document-design desiderata tied to observed behavior. Commonplace's technical actionable-methodology relation and its artifact verifiability gradient are different claims; the ingest should use ordinary wording or link and contrast the technical terms explicitly.
