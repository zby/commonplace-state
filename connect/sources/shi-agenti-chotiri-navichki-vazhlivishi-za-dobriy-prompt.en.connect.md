---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.md"
source_has_frontmatter: true
date: "2026-06-22"
depth: standard
---

# Connection Report: AI Agents: Four Skills More Important Than a Good Prompt

**Source:** [AI Agents: Four Skills More Important Than a Good Prompt](../../../sources/shi-agenti-chotiri-navichki-vazhlivishi-za-dobriy-prompt.en.md)

## Discovery Trace

**Collection contract reads:**
- Read `kb/sources/COLLECTION.md`: snapshots are immutable; ingest reports carry the active outbound surface; allowed ingest/source-review labels include `evidence`, `derived-from`, `rationale`, `compares-with`, `defined-in`, and sparse `see-also`.
- Read `kb/notes/COLLECTION.md` for reverse-edge candidates: notes may link to sources with `evidence`, `derived-from`, or sparse `see-also`.
- Read `kb/cache/types/connect-report.md` for report structure.

**Description listing scan:**
- `rg -n "^description:.*(prompt|AI Fluency|fluency|delegat|discern|diligence|description|verification|responsib|operator|context engineering|intent engineering|skill|instruction|agency|agent)" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- surfaced strong note candidates around context efficiency, instruction specificity, methodology enforcement, underspecification, verification, skills, and prompt evaluation; surfaced source comparisons for Fintool, professional developer control, Raschka's coding-agent components, and harness engineering.
- `rg -n "^description:" kb/notes --glob '*.md' | rg "context|instruction|skill|prompt|agent|operator|verification|quality|behavior|responsibility|delegation|workflow|harness|intent"` -- confirmed that relevant theoretical homes are in `kb/notes/`, not `kb/reference/` or system-review collections.

**Topic indexes:**
- Read [notes README](../../../../notes/README.md): source belongs to transferable theory if promoted, not reference docs.
- Read [reference README](../../../../reference/README.md): no shipped-system documentation target; article discusses general AI/operator practice.
- Read [agent-memory systems README](../../../../agent-memory-systems/README.md) and [agentic systems README](../../../../agentic-systems/README.md): no external system or harness is being reviewed, so no direct destination there.
- Read [sources README](../../../../sources/README.md): sibling-source comparison is appropriate.

**Body search:**
- `rg -n "AI Fluency|Delegation|Description|Discernment|Diligence|description-discernment|prompt engineering|intent engineering|operator responsibility|deployment diligence|context engineering" ...` -- exact AI Fluency terms appear only in the new translated source; adjacent KB vocabulary is context engineering, constraining, instruction loading, verification/oracles, and skills.
- `rg -n "agent.*operator|operator.*agent|human.*agent|verification|verify|responsibility|accountability|prompt|instruction|skill|context engineering|intent" kb/notes --glob '*.md'` -- identified close body hits in [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md), [writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md), and prompt-evaluation notes.

**Candidates loaded and evaluated:**
- Loaded [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- kept: the source independently frames prompt quality as subordinate to context and task/environment setup.
- Loaded [instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- kept: the source explicitly distributes Description across prompt, project instructions, skills, and AGENTS/CLAUDE files.
- Loaded [methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- kept: the source's practice section says repeated work should move into projects, skills, external tools, and updated instructions.
- Loaded [agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- kept: product/process/performance Description is a practitioner-facing decomposition of narrowing valid interpretations.
- Loaded [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- kept: automation/augmentation/agency are differentiated partly by verification, monitoring, and responsibility burden.
- Loaded [skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -- kept as weaker evidence: the source describes skills as long-term Description for repeated work, not the full methodology-to-skill derivation mechanism.
- Loaded [skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- kept as weaker evidence: the source's skill discussion aligns with skills as more than single-prompt text, but does not discuss execution policy.
- Loaded [writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- kept as synthesis input: source offers a complementary product/process/performance taxonomy rather than the same five writing styles.
- Loaded [prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) and [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- rejected as direct connections: the source argues for iterative description and checking, not controlled prompt experiments.
- Loaded sibling ingests for [Fintool lessons](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md), [professional developers do not vibe](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md), [Raschka coding-agent components](../../../../sources/components-of-a-coding-agent-raschka.ingest.md), and [harness engineering](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- kept as compares-with targets.

**Link following:**
- Followed existing links from the loaded notes to context engineering, constraining, oracle-strength, and skills notes. These confirmed clusters but did not add stronger direct targets than the candidates above.

## Connections Found

- [agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- **evidence**: the source's Description taxonomy (product, process, performance) is a practitioner-facing way to narrow the interpretation space beyond "write a better prompt."
- [instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- **evidence**: the source explicitly says durable description for repeated work is distributed across prompts, project instructions, system/project files, and skills rather than living in one prompt.
- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the source's Automation/Augmentation/Agency split ties increasing autonomy to stronger monitoring, audit, and accountability requirements.
- [methodology enforcement is constraining](../../../../notes/methodology-enforcement-is-constraining.md) -- **evidence**: the source's practice loop moves from choosing a repeated task to project instructions, skills, safe tools, and instruction updates after cycles, matching progressive movement from prompt guidance toward more durable control surfaces.
- [context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- **evidence**: the source reinforces that agent quality is not just prompt text; context engineering controls what the agent knows while working.
- [skills derive from methodology through distillation](../../../../notes/skills-derive-from-methodology.md) -- **see-also**: the source treats a skill as "description in long-term form" for repeated work; it is adjacent evidence for skills as operationalized procedure, but it does not specifically cover methodology-to-skill distillation.
- [skills are instructions plus routing and execution policy](../../../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) -- **see-also**: the source distinguishes prompt text from skills and project instructions, but it does not reach the note's execution-policy distinction.
- [professional-software-developers-dont-vibe-they-control.ingest.md](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) -- **compares-with**: both sources reject passive "vibe" use in favor of expert/operator control, explicit task framing, and verification; the paper supplies empirical evidence while this article supplies the AI Fluency vocabulary.
- [lessons-from-building-ai-agents-for-financial-services.ingest.md](../../../../sources/lessons-from-building-ai-agents-for-financial-services.ingest.md) -- **compares-with**: both sources argue the work has moved beyond prompt engineering into context, skills, and domain-specific quality controls.
- [harness-engineering-leveraging-codex-agent-first-world.ingest.md](../../../../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) -- **compares-with**: Lopopolo's harness-engineering account is the production-engineering version of the same shift from prompt wording to constraints, context, verification, and durable scaffolding.
- [components-of-a-coding-agent-raschka.ingest.md](../../../../sources/components-of-a-coding-agent-raschka.ingest.md) -- **compares-with**: Raschka decomposes agent quality into harness/context components, while this source decomposes operator competence into Delegation, Description, Discernment, and Diligence.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) → source -- **evidence**: the note could cite this source as practitioner-facing corroboration that prompt engineering is really about narrowing interpretation space through task/product/process/behavior description.
- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidence**: the source's Agency section makes verification and audit load increase with autonomy, an accessible operator-level instance of the automation/verification boundary.
- [instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) → source -- **evidence**: the source names the same distribution of behavior descriptions across prompt, project instructions, skills, and AGENTS/CLAUDE files.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- rejected as direct: the source's description-discernment loop is ordinary iterative refinement, not controlled prompt-framing ablation against a known target.
- [systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- rejected as direct: the source recommends checking and iterating, but does not discuss prompt variants as decorrelated verification or brittleness diagnosis.
- [writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- rejected as a simple evidence edge: the source's product/process/performance taxonomy is complementary to the five context-file writing styles, not evidence for that taxonomy.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- rejected: the source mentions subagents and agency as prior-series context, but does not analyze Claude Code's dynamic-workflows API or orchestration surface.

## Index Membership

None

## Synthesis Opportunities

- **Operator fluency as the human-side complement to context engineering.** Existing KB notes cover system-side mechanisms: context loading, instruction tiers, constraining, verification, and skills. This source adds a compact operator-skill overlay: Delegation selects the right task and modality; Description narrows the interpretation space; Discernment supplies product/process/performance checking; Diligence assigns responsibility and transparency. A future note could map these four skills onto the KB's existing mechanism vocabulary without adopting AI Fluency as a checklist.
- **Delegation crosses the operator/orchestration boundary.** The source's Delegation is an operator skill, but Commonplace also uses delegation as an orchestration strategy: a scheduler or parent agent can decide which derivation to perform before a bounded child call, which work to assign to siblings, and which residual task to hand down. This synthesis should connect the source to [frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md), [symbolic scheduling over bounded LLM calls](../../../../notes/bounded-context-orchestration-model.md), and [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../../../notes/feasibility-is-the-heaviest-forks-net-load.md) without treating the article itself as evidence for the technical orchestration claim.
- **Intent engineering needs a local definition before use.** The source ends by contrasting context engineering ("what the agent knows") with intent engineering ("the right desires"). No existing note owns that term. Treat it as a candidate vocabulary gap, not as an established connection.

## Maintenance Observations

- The original Ukrainian snapshot and the English translation are both present. Downstream ingest should target the English translation for corpus consistency while preserving the Ukrainian original as provenance.

## Flags

- The source is a conceptual/practitioner explainer based on the Anthropic AI Fluency framework, not primary empirical evidence. Use it mainly for vocabulary, operator framing, and accessible corroboration rather than as a load-bearing source for broad claims.
