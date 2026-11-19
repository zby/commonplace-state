---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/gentle-coding.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Gentle Coding Framework

**Source:** [Gentle Coding Framework](../../../../sources/.snapshots/gentle-coding.md)

The snapshot is immutable. Candidate outbound edges below are for its authored surface, the matching [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md), not for the snapshot itself. The Proof-of-Concept and RESEARCH documents now have separate snapshots and ingests, so this pass treats them as companion source units rather than evidence folded into the main README.

## Discovery Trace

**Setup, source analysis, and authorised destinations:**

- Read the connect skill, [connect-report type](../../../../types/connect-report.md), complete snapshot, and `kb/sources/COLLECTION.md` before discovery. The source has frontmatter but no `tags`, so no tag-README or by-tag `rg` pass applied.
- The source collection authorises prospecting in `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`; it excludes `work` and `instructions`. Labels were restricted per destination to the current source contract. In particular, source-to-note candidates may use `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, or sparse `see-also`; source-to-source candidates may use `compares-with` or sparse `see-also`.
- Read `kb/notes/COLLECTION.md` for reverse-edge authorisation. A durable note-side evidence edge must land on the tracked ingest, never on the ignored snapshot.
- Decomposed the README into three proposed prompt-contract elements: a low-stakes collaborative style (Gentle Mindset), an explicit success criterion (Defined Winning Condition), and an acceptable observable non-success branch (Safety-Token). Separately, it reports a community benchmark table and gives anthropomorphic training-pressure explanations. This decomposition prevents the PoC's experiment and RESEARCH's bibliography from being attributed to the README.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` across every authorised local destination. Fresh counts were: `notes` 360, `reference` 141, `sources` 302, `agent-memory-systems` 173, and `agentic-systems` 12.
- The title scan surfaced instruction-specification, recovery, prompt-variation, psychology-transfer, and response-space clusters in notes and sources. Reference titles describe Commonplace selections and state, agent-memory titles describe retained-memory systems, and agentic-system titles describe whole harnesses; none offered a direct analogue for this prompt-only framework. Those three destinations were skipped after focused confirmation rather than sprayed with generic `see-also` edges.

**Description listing and body search -- notes:**

- Ran `rg '^description:' kb/notes/ --glob '*.md'`. Candidate descriptions included [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md), [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md), the experimental-contrast cluster, and the prompt-structure cluster.
- `rg -n -i 'safety[- ]?token|defined winning condition|winning condition|permission to fail|allowed fallback|acceptable (fallback|failure|exit|completion)|graceful exit|explicit (fallback|failure|non-success|abstention)|fail successfully|error winning condition' kb/notes/ --glob '*.md'` found no note that directly owns explicit non-success as part of a task's response space.
- `rg -n -i 'high[- ]stakes|low[- ]stakes|authoritarian|coercive|prompt (tone|framing|style)|emotional prompt|roleplay|expert role|mistakes are ok|performance anxiety|psychological safety' kb/notes/ --glob '*.md'` surfaced prompt ablation, emotional-prompt interpreter failure, writing styles, and psychology-transfer candidates. The psychology-transfer note passed because it supplies the exact test the README's trauma/anxiety rhetoric needs; prompt ablation and interpreter failure were rejected because the README does not preserve a fixed semantic task while varying only framing.
- `rg -n -i 'overthinking|over-reason|reasoning loop|freez(e|ing)|confabul|forced output|impossible task|impossible prompt|fail soft|failure branch|recovery strategy|structured recovery' kb/notes/ --glob '*.md'` surfaced structured recovery and soft-failure notes. Structured recovery passed as a design dependency for the Safety-Token; the soft-failure observation is better grounded by the separate PoC ingest.

**Description listing and body search -- sources:**

- Ran `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'prompt|framing|emotion|personality|stress|pressure|stakes|sycoph|fallback|abstain|no-op|failure|recovery|overthinking|latency|token|role'`. This surfaced Prompt Stability, Agent Behavioral Contracts, Simplification, RECV, and the two new Gentle-Coding companion ingests.
- `rg -n -i 'gentle[- ]coding|authoritarian|low[- ]stakes|high[- ]stakes|safety[- ]token|permission to fail|fallback (token|output)|emotional prompt|prompt (tone|framing)|personality prompt|no[- ]op|abstain|forced binary|response space' kb/sources/ --glob '*.md'` confirmed the shared comparison axes: matched emotional/style perturbations, typed recovery, and whether a non-success outcome is representable.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) passed as the controlled empirical counterpart to the README's self-reported framing effects. [Agent Behavioral Contracts](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) passed as the formal/runtime counterpart to a prompt-level fallback. Simplification and RECV were retained for the synthesis opportunity rather than as extra direct edges because the separate PoC ingest already makes those comparisons at the more specific impossible-task level.
- [Gentle-Coding Proof of Concept](../../../../sources/gentle-coding-proof-of-concept.ingest.md) and [Gentle-Coding Comparative Research Catalog](../../../../sources/gentle-coding-research.ingest.md) passed as sparse `see-also` companions: the former owns the origin experiment and the latter owns the bibliography. Neither should be silently reabsorbed into the main README ingest.

**Focused confirmation in the other destinations:**

- Ran focused description and body searches over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` for `prompt|failure|fallback|recovery|contract|reliab|instruction|output|emotion` and for `gentle[- ]coding|safety[- ]token|defined winning|low[- ]stakes|high[- ]stakes|prompt framing|permission to fail`. Reference hits concerned Commonplace's own instruction and review machinery; agent-memory hits concerned prompt injection or retained-memory recovery; the agentic-system scan produced no direct match. None passed the articulation test on a named shared axis.

**Link following and existing-state check:**

- Followed the explicit-done criterion from [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) into underspecification and frontloading. It clarified the useful reading of Defined Winning Condition: fix the goal, constraints, and meaning of done while leaving live method choices to the executor.
- Followed [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) to Agent Behavioral Contracts and the safety/recovery reliability cluster. This distinguished the README's natural-language exit branch from ABC's detected-violation, fallback-chain, and escalation machinery.
- Followed [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) through its simpler-mechanism test. Gentle Coding is a useful new worked case because its engineering proposal can be stated as task-contract variables without assuming model anxiety or trauma.
- Read the current main ingest and both new companion ingests in full. `rg -n -i 'gentle[- ]coding|safety[- ]token|OttoRenner' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` found no note-side link to the source; existing mentions are confined to the three Gentle-Coding ingests.
- External prospecting was skipped as required. The repository URL is already present in snapshot frontmatter; the README's linked PR and studies are source leads, not locally verified candidates.

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **rests-on**: Defined Winning Condition fixes the goal, constraints, and terminal criterion while leaving the route to the live executor, and Safety-Token additionally fixes what counts as an acceptable non-success result. This is the precise, non-psychological design rationale for those two concepts.
- [Enforcement without structured recovery is incomplete](../../../../notes/enforcement-without-structured-recovery-is-incomplete.md) -- **rests-on**: Safety-Token adds a predeclared fallback or escalation-shaped response after the primary task cannot be completed. The README implements this only as natural-language response policy, while the note explains why recovery must be designed rather than improvised.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -- **is-evidence-for**: the README bundles testable prompt-contract moves -- stakes, role framing, success criteria, and failure outputs -- with claims about anxiety, trauma-like behavior, and shareholder-driven engagement. It is a practitioner case for testing the engineering mechanism separately from the borrowed psychological explanation.
- [Ingest: Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) -- **compares-with**: both concern emotional and personality framing, but PromptSE attempts semantic/interface invariance, repeated sampling, and statistical analysis, while the README's table reports community results for a compound rewrite without preserving the protocol. The comparison bounds what the Gentle Coding results can identify.
- [Ingest: Agent Behavioral Contracts for Reliable Agents](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- **compares-with**: Gentle Coding makes failure recovery a prompt-level acceptable output; ABC makes violations, corrective actions, fallback chains, escalation, and recovery windows explicit runtime contract elements. The shared recovery axis shows what is gained and lost when the policy remains natural language.
- [Ingest: Gentle-Coding Proof of Concept](../../../../sources/gentle-coding-proof-of-concept.ingest.md) -- **see-also**: this separate source unit owns the small paired-prompt origin study that the README summarizes as project history; follow it for the actual task conditions and evidential limitations rather than folding its observations into the README ingest.
- [Ingest: Gentle-Coding Comparative Research Catalog](../../../../sources/gentle-coding-research.ingest.md) -- **see-also**: this separate source unit owns the project's annotated bibliography and its verification caveats; the main README may identify it as research infrastructure but should not treat its one-line literature summaries as evidence.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) -- **evidenced-by**: Gentle Coding is a non-memory worked case in which a potentially useful engineering intervention can be reduced to prompt-contract variables while the source explains it through human psychological vocabulary. The return path gives readers a fresh domain on which to apply the note's per-principle and simpler-mechanism tests.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- the README's benchmark table does not preserve the compared prompts, task cells, model identifiers, variance, or analysis. The separate Proof-of-Concept ingest carries the usable bundle-level contrast and already connects to this note.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- the README reports timeouts and loop reductions only as a summary table. The PoC source owns the concrete fabricated exits and manual termination, so evidence should be routed from that ingest rather than duplicated here.
- [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- Gentle Mindset plausibly adds social stakes and failure permission to functional writing-style choices, but its compound prompts do not distinguish style from task semantics or response policy. Prompt Stability is the cleaner local evidence for emotional/style sensitivity.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- its emotional-prompt example requires functionally equivalent specifications. Gentle Coding's conditions also alter asserted task facts, permission to fail, and valid outputs, so the README cannot establish interpreter failure under a fixed public meaning.
- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- its method holds input, tools, model, and target fixed while varying only framing. The README reports a compound rewrite and therefore is not an ablation case.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- Gentle Mindset, Defined Winning Condition, and Safety-Token jointly change framing, process discretion, and output policy; because the README does not vary them independently, it cannot bear on the independence claim directly.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- the README lists token and latency deltas but does not include the underlying records or enough protocol detail to verify them. Treat the table as a lead to capture the linked benchmark rather than as an evidence edge.

## Index Membership

None.

## Synthesis Opportunities

- **Explicit success and non-success branches jointly define the response space.** The README's Defined Winning Condition and Safety-Token name both terminal sides of a task contract; the [Proof of Concept](../../../../sources/gentle-coding-proof-of-concept.ingest.md) reports behavior when non-success answers are or are not allowed; [Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) proposes an explicit no-op control; and [RECV](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) shows a benchmark that removes abstention and forces a binary verdict. Together they imply the not-yet-owned claim that a response space determines whether warranted non-success is representable; tone is a separate experimental variable.

## Maintenance Observations

- The current [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) still declares itself a three-snapshot umbrella report in its title, description, classification, summary, connections, limitations, and recommended action. Separate tracked ingests now own [Proof-of-Concept](../../../../sources/gentle-coding-proof-of-concept.ingest.md) and [RESEARCH](../../../../sources/gentle-coding-research.ingest.md). A fresh main-ingest pass should analyse only `gentle-coding.md`, use the two reports as companion links, and avoid importing their experiment or bibliography as if those bytes belonged to the primary snapshot.
- The README's “Recent Findings” table links a 3,000+-call community experiment but does not preserve its prompts, run records, model identifiers, uncertainty intervals, or protocol. Capturing that linked primary record would be required before the table's numerical claims can support a durable evidence edge.

## Flags

- **Analysis split:** the README itself still makes more than one independent assertion across three areas. Keep Gentle Mindset (social framing), Defined Winning Condition (success criterion), Safety-Token (non-success response policy), and the community results analytically separate; do not let a reported bundle-level outcome assign causality to any one component.
- **Mechanism boundary:** retain the source's own model-dependent nulls -- neutral at N=100 for Sonnet 4.6, Opus 4.6, and GPT-5.5 -- and distinguish prompt-contract design from the unverified anxiety, trauma, RLHF-penalty, and shareholder-engagement explanations.
