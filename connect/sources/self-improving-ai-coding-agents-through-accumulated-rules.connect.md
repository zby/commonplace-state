---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/self-improving-ai-coding-agents-through-accumulated-rules.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Self-Improving AI Coding Agents Through Accumulated Behavioral Rules

**Source:** [Self-Improving AI Coding Agents Through Accumulated Behavioral Rules](../../../sources/self-improving-ai-coding-agents-through-accumulated-rules.md)

## Discovery Trace

**Collection rules and curated heads:**

- Read `kb/sources/COLLECTION.md`; snapshots are immutable, their ingest reports carry the authored outbound surface, and reverse edges normally come from notes using `evidenced-by` or `abstracted-from`.
- Read the notes tag hub plus the `deploy-time-learning`, `self-improving-systems`, `constraining`, and `agent-memory` curated heads. These routed the search toward durable behavior-changing artifacts, promotion oracles, activation, and lifecycle rather than generic coding-agent material.
- Read the `reference`, `agent-memory-systems`, and `agentic-systems` collection heads. The strongest reviewed-system match was Synapptic; no agentic-system analysis passed the articulation test.

**Complete title surfaces:**

- Generated fresh `rg -N --no-heading -m1 '^# '` listings for `kb/notes/` (326 headings), `kb/reference/` (125), `kb/agent-memory-systems/` (171), `kb/agentic-systems/` (8), and `kb/sources/` (411). Filtered title candidates around instructions, feedback, review, memory, rules, constraints, codification, learning, validation, and accumulation.

**Description listing scans:**

- `rg -n '^description:' kb/notes --glob '*.md' | rg -i 'deploy-time|instruction|feedback|correction|rule|persistent|artifact|self-improv|review'` kept [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md), [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md), [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md), and [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md).
- Equivalent scans over `kb/agent-memory-systems/` kept [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) and rejected Reflexion as already covered by the paper's own related-work comparison and as weaker on cross-session retention.
- Equivalent scans over `kb/sources/*.ingest.md` kept [Figma's agent security review account](../../../../sources/figma-agent-security-review-thread-2081739292859421118.ingest.md) as the closest source-level sibling: both turn review-derived precedents into future agent policy, but Figma reports an explicit evaluation corpus and precision-improvement process.

**Body searches:**

- `rg -n -i 'accepted (edit|comment)|review (feedback|comment).*rule|generaliz.*rule|rule.*generaliz' ...` surfaced the direct instance-versus-rule oracle tension in [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md).
- `rg -n -i 'before (the )?(mistake|action)|always.loaded|behavior-changing memory|behaviour-changing|cross.session.*(rule|instruction|memory)' ...` kept [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) and [AGENTS.md should be organized as a control plane](../../../../notes/agents-md-should-be-organized-as-a-control-plane.md); both speak to the paper's always-loaded rule file, but the latter qualifies its unbounded-growth posture.
- `rg -n -i 'monotonic.*(growth|accumul)|unbounded growth|rule conflict|instruction.*accumul|rollback.*accumul' ...` showed that the source's monotonic-growth principle conflicts with existing KB emphasis on promotion, rollback, retirement, and context-budget discipline.
- `rg -n -i 'guard|ablation|review|accepted|rule|with/without|feedback|promotion' kb/agent-memory-systems/reviews/synapptic.md` kept Synapptic because it tests individual behavior guards and can exclude redundant or harmful ones.

**Link following:**

- Followed the deploy-time-learning cluster into behavior change, constraining, readable artifacts, and context loading. The paper is a concrete deployment case, but it varies neither artifact form nor loading policy.
- Followed the accepted-edit note into the proposal for gate learning from accepted edits and the abstraction-boundary notes. These reinforced that comment acceptance verifies the local correction, not the generalized rule.
- Followed the activation and effects notes into Synapptic's guard-ablation review. This supplied the most useful alternative promotion/evaluation design.

## Connections Found

- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **is-evidence-for**: the paper reports a cross-session, version-controlled natural-language system-definition artifact changing coding-agent behavior without weight updates.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- **is-evidence-for**: accumulated rules, checklists, and validators are a worked instance of deployment-time narrowing intended to suppress known error classes.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- **compares-with**: the source treats every accepted generalizable review comment as immediately promotable policy, whereas the note argues that instance acceptance does not verify the extracted rule and calls for independent promotion and rollback.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) -- **is-evidence-for**: the shared instruction file is loaded before later coding actions, and the reported zero-recurrence observation is preliminary evidence for pre-action activation under one deployment.
- [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) -- **compares-with**: both distill interaction failures into cross-session assistant policy, but Synapptic adds per-guard WITH/WITHOUT evaluation and exclusion of redundant or harmful guards while this source relies on accepted comments, later observation, and manual conflict resolution.
- [Figma's agent security review account](../../../../sources/figma-agent-security-review-thread-2081739292859421118.ingest.md) -- **compares-with**: both convert review-derived precedents into reusable agent policy, while the Figma account foregrounds precision testing and an evaluation corpus rather than monotonic rule accumulation.

## Bidirectional Candidates

- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) <-> source -- **compares-with / evidenced-by**: the ingest should state the disagreement, and the note could cite this deployment as a concrete high-stakes example of immediate rule promotion from accepted feedback.
- [AGENTS.md should be organized as a control plane](../../../../notes/agents-md-should-be-organized-as-a-control-plane.md) <-> source -- **compares-with / evidenced-by**: the paper reports a ~6,250-token always-loaded rule set and anticipates unbounded-growth pressure, supplying a useful case against which the note's short-router design can be evaluated.

## Reverse-edge Candidates

- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) → source -- **evidenced-by**: add the paper as an observational production case of durable readable behavior change across sessions.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) → source -- **evidenced-by**: the accumulated rule/checklist/validator stack is a concrete constraining loop.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) → source -- **evidenced-by**: always-loaded rules reportedly suppressed nine tracked error classes within the observation window, while the study limitations should travel with the citation.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source -- **evidenced-by**: the source attempts downstream behavioral measurement rather than merely counting written rules, but lacks a controlled baseline or causal memory ablation.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) -- rejected as a primary connection because the paper already supplies this comparison and Reflexion's within-session feedback memory does not sharpen the local promotion-oracle or cross-session questions.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- rejected as too broad for the settled connection set: its benchmark-gated whole-harness evolution is useful background, but Synapptic isolates the rule/guard promotion difference more directly.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as a direct edge because the paper's rule addition is better diagnosed by the narrower accepted-edit note; the source does not cleanly expose a reject-capable rule-level candidate gate.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- retained as an analysis lens rather than a durable connection: it bounds what the reported experiment can establish but is not a source-specific navigation target.

## Index Membership

None.

## Synthesis Opportunities

The source, [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md), and [Synapptic](../../../../agent-memory-systems/reviews/synapptic.md) jointly imply a sharper lifecycle claim: review acceptance is a strong capture signal for candidate behavioral rules, while promotion requires rule-level effectiveness testing and retirement/rollback. The existing accepted-edit note already states most of this claim, so update it with the paper and Synapptic comparison rather than creating a duplicate synthesis note.

## Maintenance Observations

None.

## Flags

- **Empirical decomposition:** signals and histories are accepted human review comments, automated-review findings, production errors, self-discovered issues, prior rules, checklists, and task logs. Available updates are append/refine rule text, add checklist or validation items, and manually resolve conflicts. The effective mapping from event to rule is supplied by engineer judgment. Fixed outside the observed update space are the always-loaded Markdown representation, source taxonomy, typed-language microservice setting, human-review culture, rule abstraction heuristic, lack of semantic retrieval, and lack of retirement policy. Improvement within this configuration does not validate those fixed choices or monotonic accumulation as a general design.
- **Causal limit:** the 0/74 recurrence result, review-category shift, and transfer counts come from one four-week deployment without a no-rule or static-prompt baseline. They support feasibility and local association, not causal attribution to the rule mechanism or evidence that adjacent fixed choices were necessary.
- **Promotion split candidate:** if promoted beyond source analysis, separate (1) the observational deployment evidence for cross-session readable-artifact learning from (2) the normative rule-promotion and always-loaded-growth design, which the evidence does not independently validate.
