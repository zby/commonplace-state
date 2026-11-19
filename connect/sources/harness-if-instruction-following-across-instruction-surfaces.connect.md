---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/harness-if-instruction-following-across-instruction-surfaces.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: Harness-IF

**Source:** [Harness-IF: Evaluating Instruction Following Across Instruction Surfaces in Coding Agents](../../../sources/harness-if-instruction-following-across-instruction-surfaces.md)

## Discovery Trace

**Description listing scan:**

- Generated the complete `# ` title surface with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. The strongest title-level candidates were the notes on systematic prompt variation, always-loaded context surfaces, whole-system behavior, and fixed decompositions; the trajectory-aware evaluation proposal; and the existing Harness Updating, prompt-stability, and context-file ingests.
- Ran path-and-description scans from matches to `rg -l -i 'instruction[- ]following|against[- ]prior|unprompted default|prompt depth|instruction surface' ...`, `rg -l -i 'system prompt|project file|skill description|tool description|AGENTS\.md|CLAUDE\.md' ...`, and `rg -l -i 'final task success|task[- ]level outcome|rule[- ]level|process[- ]level|execution evidence|prompt variation|counterbalanc' ...`. These confirmed the candidates above and surfaced weaker overlaps with behavioral contracts, context contamination, and instruction unit testing.

**Topic indexes:**

- Read the curated heads for notes, reference, agent-memory systems, agentic systems, and sources. No source tags were present, so no tag-README pass applied.
- The notes head places evaluation and learning theory in scope. The agent-memory and agentic-system heads contain no casebook entry for Harness-IF itself: it is a benchmark paper, not an inspectable memory system or whole harness implementation, so those destinations were not pursued beyond their full title scans.

**Body search:**

- `rg -l -i 'instruction following|instruction-following|compliance|prompt variation|final success|final task|outcome check|process.*verif|loading hierarchy|control surfaces|against-prior|unprompted default|default behavior' kb/notes kb/reference kb/sources --glob '*.md'` -- retained the prompt-variation, always-loaded-surface, whole-system, and fixed-decomposition notes; rejected generic reliability and underspecification matches.
- `rg -l -i 'system prompt|project file|skill description|tool description|AGENTS\.md|CLAUDE\.md' ...` -- retained the always-loaded-context note and the empirical context-file ingest; most agent-memory hits merely mentioned `AGENTS.md` as a storage or bootstrap mechanism.
- `rg -l -i 'final task success|task[- ]level outcome|rule[- ]level|process[- ]level|execution evidence|prompt variation|counterbalanc' ...` -- retained the trajectory-aware evaluation proposal and prompt-stability ingest. The outcome/process notes were informative context, but Harness-IF does not test abstraction from an episode, so they were not kept as direct edges.

**Link following:**

- Followed the prompt-variation note to prompt ablation and the prompt-stability ingest. Harness-IF is a diagnosis design rather than prompt optimization: E0 relocates a fixed rule across delivery surfaces and counterbalances conflicts, while the main panel only assigns admissible surfaces.
- Followed the whole-system note to the fixed-decomposition and output-deviation notes. Harness-IF supports the whole-system boundary through E0, while its main panel leaves surface assignment, task design, rule taxonomy, tools, model weights, and judge fixed.
- Followed the context-surface note to instruction-specificity and the OSS context-file study. Harness-IF adds behavior-side evidence to their descriptive inventories but does not identify which instructions belong on which surface.
- Followed the Harness Updating ingest to activation and adherence. It separately measures loading and faithful use, whereas Harness-IF starts from configured delivery and scores rule compliance; the sources are complementary rather than redundant.

## Connections Found

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- **is-evidence-for**: Harness-IF turns the note's project-file, skill-description, and tool-description distinctions into evaluated delivery surfaces, then adds system and user surfaces plus rule-level compliance and a conflict-precedence pilot.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- **is-evidence-for**: E0 holds rule semantics and task structure fixed while relocating mutually exclusive rules across surfaces, a controlled diagnostic variation whose result concerns interpreter precedence rather than the truth of the instructions.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the counterbalanced E0 result shows that changing harness delivery surface while holding the rule and task fixed can change which instruction prevails, so observed behavior belongs to the model-plus-harness configuration.
- [LLM output deviation has three sources with non-substitutable remedies](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) -- **is-evidence-for**: the zero-injection control shows that an apparent pass can reflect prior-aligned default behavior rather than response to the specification, qualifying what a compliance verdict over the interpreter's output distribution establishes.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting Harness-IF requires separating improvement within its fixed rule, task, tool, surface, and scoring design from evidence for those choices. Only E0 varies surface placement, and it does so for four synthetic conflicts; the main panel's per-surface rates are descriptive strata.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- **see-also**: Harness-IF is a concrete adjacent instrument that derives per-rule verdicts from traces, diffs, tests, output, and artifacts instead of collapsing execution into a final task score, though it does not perform the proposal's paired output-only versus trajectory-aware judge comparison.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- **compares-with**: Harness Updating separates artifact loading, faithful use, and downstream benefit; Harness-IF assumes configured delivery and focuses on whether each delivered rule is followed, with a withheld-rule baseline for prior alignment.
- [Ingest: Context Engineering for AI Agents in Open-Source Software](../../../../sources/context-engineering-ai-agents-oss.ingest.md) -- **compares-with**: the OSS study supplies naturalistic input-side evidence about what projects write in context files, while Harness-IF supplies controlled behavior-side evidence about whether operational rules survive across instruction surfaces.
- [Ingest: Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- **compares-with**: PromptSE varies emotional and stylistic framing within user prompts; Harness-IF varies delivery surface and, in E0, conflict direction. Both hold task meaning fixed but diagnose different interpreter sensitivities.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) → source -- **evidenced-by**: cite Harness-IF as behavior-side evidence that the catalogued surfaces are not interchangeable delivery containers.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) → source -- **evidenced-by**: add surface relocation as a diagnosis design alongside paraphrase and framing variation, bounded to the four-conflict E0 pilot.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: use E0 as controlled evidence that a harness-level delivery choice changes behavior without a model-weight change.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) → source -- **evidenced-by**: use Harness-IF's execution-evidence bundle and constraint-level verdict protocol as one adjacent benchmark design, while preserving the proposal's need for a paired judge comparison.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Instruction specificity should match loading frequency](../../../../notes/instruction-specificity-should-match-loading-frequency.md) -- rejected because Harness-IF measures adherence and precedence, not the normative placement question of which instruction specificity belongs at each loading frequency.
- [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) -- rejected because Harness-IF scores explicit operational-rule violations; it does not test residual semantic influence after an agent recognizes and refuses content.
- [Ingest: Agent Behavioral Contracts for Reliable Agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- rejected as too broad: ABC evaluates runtime monitoring and recovery for declared contracts, while Harness-IF measures instruction-following across natural-language surfaces without enforcing recovery.
- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- rejected as a weaker source-to-source edge than the retained trajectory-evaluation and context-file comparisons; its component ablations ask whether a harness improves task outcomes, not whether an atomic delivered rule is followed.
- [Unit testing LLM instructions requires mocking the tool boundary](../../../../notes/unit-testing-llm-instructions-requires-mocking-the-tool-boundary.md) -- rejected because Harness-IF is an integration benchmark over real execution evidence, not a mock-boundary unit-test design.

## Index Membership

None

## Synthesis Opportunities

- Harness-IF and [LLM output deviation has three sources with non-substitutable remedies](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) imply a missing evaluation claim: **an instruction-following score without a no-instruction baseline counts prior-aligned coincidence as obedience**. The zero-injection design gives the claim an operational test, while the fixed-decomposition lens limits it to behavior expressible under the chosen tasks, rules, tools, models, and judge.

## Maintenance Observations

None

## Flags

- The main panel's per-surface rates are confounded by rule family, prior class, wording, and surface admissibility; only E0 identifies a placement contrast, and only over four synthetic conflict pairs and nine older builds.
- The paper is experiment-bearing. Its effective update space lets a model condition actions on the assembled instruction stack, repository state, multi-turn history, and tool/test feedback; compose tool calls, file edits, commands, and final output; and map those signals to actions through a fixed model and harness. Rule taxonomy, task fixtures, admissible surface set, surface phrasings, tool interface, turn budget, model weights, item selection, prior-label procedure, and mostly LLM-judged scoring remain fixed outside the comparison.
