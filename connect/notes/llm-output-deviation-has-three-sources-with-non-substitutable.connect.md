---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/llm-output-deviation-has-three-sources-with-non-substitutable.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: LLM output deviation requires three-way diagnosis because remedies target different relations

**Source:** [LLM output deviation requires three-way diagnosis because remedies target different relations](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md)

## Discovery Trace

**Setup and authorization**

- Read [kb/cache/types/connect-report.md](../../../../types/connect-report.md), the full source note, [kb/types/note.md](../../../../types/note.md), and [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md).
- Authorized local destinations inferred from the notes outbound table: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, `kb/instructions/`, and `kb/types/`. `kb/work/` is explicitly excluded. `external` is authorized in principle but was skipped because no additional external target was supplied or already loaded beyond links already authored in the note.
- Read curated heads before prospecting: [Notes](../../../../notes/README.md), [LLM reliability](../../../../tags/llm-reliability-README.md), [Computational model](../../../../tags/computational-model-README.md), [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), [Sources](../../../../sources/README.md), [Instructions](../../../../instructions/README.md), and [Types](../../../../types/README.md).

**Notes (`kb/notes/`)**

- Curated heads showed the source already sits in the core `llm-reliability` and `computational-model` clusters; neither tag README declares `complete: true`, so by-tag scans were still required.
- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg 'underspec|interpreter|sampling|indetermin|oracle|verification|prompt|diagnos|specification|automation|contamination|separation|framing|stability'`
- Description scans:
  - `rg '^description:' kb/notes/ --glob '*.md' | rg 'underspec|interpreter|sampling|indetermin|oracle|verification|prompt|diagnos|specification|automation|contamination|separation|framing|stability'`
  - `rg -l '^tags:.*\bllm-reliability\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`
  - `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`
- Body searches:
  - `rg -n "prompt variation|framing|paraphrase|equivalent variants|brittleness|Prompt Stability" kb/notes/ --glob '*.md'`
  - `rg -n "underspecification|narrowing|writing styles|prescriptive|prohibitive|conditional" kb/notes/ --glob '*.md'`
  - `rg -n "OpenProse|scoping before it recovers|error correction|intermediate regime|LLM-mediated" kb/notes/ --glob '*.md'`
  - `rg -n "synthesis|voting|best-of-N|first-to-ahead-by-k|aggregation" kb/notes/ --glob '*.md'`
- Opened and evaluated: [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md), [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md), [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md), [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md), [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md), [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md), [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md), [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), and [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../notes/underspecification-and-indeterminism-complicate-programming-for.md).
- Link following:
  - Followed [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) to [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md); kept the systematic-prompt-variation note and rejected prompt ablation because it searches for a winning framing rather than diagnosing which relation failed in a bad run.
  - Followed the source’s already-authored path through [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) to [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md); rejected a direct source edge because the intermediate-regime note is a second-step refinement already reached through the stronger existing scheduler link.
- Kept from notes: [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md), and [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md).

**Reference (`kb/reference/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md' | rg 'verification|oracle|prompt|specification|diagnos|review|connect|sampling|reliability|automation'`
- Description scan:
  - `rg '^description:' kb/reference/ --glob '*.md' | rg 'verification|oracle|prompt|specification|diagnos|review|connect|sampling|reliability|automation'`
- README plus filtered title/description scans surfaced navigation, review, and link-vocabulary documents, but none offered a note-level `evidenced-by`, `derived-from`, `abstracted-from`, or `see-also` edge with more traversal value than the existing theory-note links. No body search was needed at standard depth once the destination failed the articulation test at title/description level.

**Agent Memory Systems (`kb/agent-memory-systems/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md' | rg 'verification|prompt|reliability|memory|retriev|context|agent|trace|learning|review'`
- Description scan:
  - `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg 'verification|prompt|reliability|memory|retriev|context|agent|trace|learning|review'`
- The strongest hits were memory/runtime reviews whose verification or retrieval machinery depends on the source note’s taxonomy rather than sharpening it. No candidate offered a direct reader gain for this source note, so the destination stopped at curated-head plus title/description pass.

**Agentic Systems (`kb/agentic-systems/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md' | rg 'verification|prompt|scheduler|reliability|orchestr|agent|memory|protocol|error|recovery'`
- Description scan:
  - `rg '^description:' kb/agentic-systems/ --glob '*.md' | rg 'verification|prompt|scheduler|reliability|orchestr|agent|memory|protocol|error|recovery'`
- Body search:
  - `rg -n "typed|verification|soft oracle|scheduler|recovery|prompt|error correction" kb/agentic-systems/ --glob '*.md'`
- Evaluated [Eigenius](../../../../agentic-systems/reviews/eigenius.md), [Swamp](../../../../agentic-systems/reviews/swamp.md), and the surrounding scheduler/control-plane hits from the body search. They are useful worked cases for typed execution and architectural separation, but the direct traversal still runs more cleanly through already-linked theory notes such as scheduler separation and error-correction. No kept candidate.

**Sources (`kb/sources/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' | rg 'prompt|stability|analyst|oracle|verification|sampling|specification|multiverse|judge|error|automation'`
- Description scan:
  - `rg '^description:' kb/sources/ --glob '*.md' | rg 'prompt|stability|analyst|oracle|verification|sampling|specification|multiverse|judge|error|automation'`
- Body search:
  - `rg -n "prompt stability|multiverse|verification|sampling|underspecification|interpreter failure|out-of-spec" kb/sources/ --glob '*.md'`
- Opened and evaluated: [Ingest: Agent Behavioral Contracts for Reliable Agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) and [Ingest: Solving a Million-Step LLM Task with Zero Errors](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md).
- Existing authored source edges remained the strongest source-side path:
  - [Ingest: Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md)
  - [Ingest: Many AI analysts, one dataset](../../../../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md)
  Both already link back to the source note.
- Rejected the newly opened source candidates because they sharpen subordinate mechanisms already handled by local notes: ABC is better reached through underspecification and error-correction theory; MAKER is better reached through the linked error-correction and scheduler notes.

**Instructions (`kb/instructions/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md' | rg 'review|validate|connect|ingest|debug|prompt|specification|verification'`
- Description scan:
  - `rg '^description:' kb/instructions/ --glob '*.md' | rg 'review|validate|connect|ingest|debug|prompt|specification|verification'`
- Under the notes collection posture, instructions are exceptional destinations. The scans surfaced review, ingest, and connect procedures, but no procedure clearly operationalized this note’s three-way diagnosis with additional ordering/defaults/stopping conditions. No candidate survived.

**Types (`kb/types/`)**

- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md' | rg 'note|instruction|review|definition|type|text|tag'`
- Description scan:
  - `rg '^description:' kb/types/ --glob '*.md' | rg 'note|instruction|review|definition|type|text|tag'`
- The notes label table authorizes `evidenced-by` to `types`, so this destination was still prospected even though the notes prose scan line does not mention it. No type contract functioned as an observation, case, or source that directly corroborates the source claim; no kept candidate.

## Connections Found

- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- **extends**: the source uses meaning-preserving prompt variation as one empirical way to separate framing sensitivity from repeated-sample variation; this note develops that diagnostic move and separates it from prompt variation used for verification or explanatory-reach testing.

- [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- **mechanism**: the source says prompt narrowing directly repairs the `V`-versus-`I` mismatch; this note details one concrete mechanism for that repair by treating instruction style as a family of constraint strategies that narrow the interpretation space in different ways.

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **extends**: the source’s non-substitutable remedies imply that improvement must reach different system surfaces — prompt/context, validator/correction layer, and runtime/sampling policy — and this note turns that implication into the stronger learning-boundary claim.

## Bidirectional Candidates

- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) <-> source -- **grounds**: the return path is useful because the prompt-variation note names diagnosis via fixed-semantics prompt changes but does not currently point to the broader three-relation taxonomy that explains what such a diagnostic result is separating.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) -- rejected: real architectural nuance, but already one hop behind the source’s existing [scheduler separation](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) link, so a direct edge would duplicate a tighter traversal path.

- [Synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) -- rejected: relevant to the source’s one sentence on `best-of-N`, but too narrow a multi-agent aggregation subcase to outrank the already-linked general error-correction path.

- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- rejected after link following: it searches for a framing that elicits a known target, whereas the source note is diagnosing which relation failed in a bad run.

- [LLM↔code boundaries are natural checkpoints](../../../../notes/llm-code-boundaries-are-natural-checkpoints.md) -- rejected: useful debugging note, but it tracks the older two-phenomena boundary rather than the source’s three-way diagnosis and would blur the new distinction.

- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../notes/underspecification-and-indeterminism-complicate-programming-for.md) -- rejected: explicitly provisional two-source decomposition that omits interpreter failure, so it risks routing the reader into the superseded frame.

- [Ingest: Agent Behavioral Contracts for Reliable Agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- rejected: good evidence for formal spec narrowing and runtime enforcement, but the reader reaches it more cleanly through the source’s existing underspecification and error-correction notes.

- [Ingest: Solving a Million-Step LLM Task with Zero Errors](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) -- rejected: strong empirical case for oracle-backed voting, but the source already links the local notes that translate MAKER into this KB’s error-correction and architectural vocabulary.

- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) -- rejected: compelling typed-execution substrate, but it exemplifies repair-surface separation more than it sharpens the source note’s diagnosis of where a deviation came from.

## Index Membership

None — the source is already present in [LLM reliability](../../../../tags/llm-reliability-README.md) and [Computational model](../../../../tags/computational-model-README.md), and no additional curated landing was justified.

## Synthesis Opportunities

- The source note, [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md), [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md), and [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) together imply a higher-order note that splits “prompt changes” into different causal roles: shrinking `V`, holding semantics fixed to diagnose brittleness, decorrelating judges, and searching for a deployable framing. That distinction is distributed across the current notes but not named as one map.

## Maintenance Observations

- [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md) has a routing mismatch: its prose scan list omits `kb/agentic-systems/` and `kb/types/`, but the outbound label table authorizes those destinations. This run treated the label table as authoritative and prospected both anyway, but the contract remains internally inconsistent.

## Flags

- None
