---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/gentle-coding-proof-of-concept.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Gentle-Coding Proof of Concept

**Source:** [Gentle-Coding Proof of Concept](../../../../sources/.snapshots/gentle-coding-proof-of-concept.md)

The snapshot is immutable. Its current authored surface is the composite [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md), which explicitly analyses this PoC together with the repository README and research bibliography. Every outbound candidate below is therefore a possible future edit to that ingest (or to a future same-stem ingest), never to the snapshot itself.

## Discovery Trace

**Setup and source analysis:**

- Read the connect skill, [connect-report type](../../../../types/connect-report.md), complete snapshot, and `kb/sources/COLLECTION.md` before discovery. The source has frontmatter but no `tags`, so no matching tag-README or by-tag `rg` pass applied.
- The source collection authorizes prospecting in `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`; it excludes `work` and `instructions`. Candidate labels were restricted per destination to the collection's current set: notably `is-evidence-for`, `rests-on`, `abstracted-from`, `compares-with`, `defined-in`, and sparing `see-also` for notes, and `compares-with` or sparing `see-also` for sources.
- Source decomposition used for search and judgment: six free cloud-model interfaces; three deliberately impossible or contradictory tasks; paired authoritarian/gentle prompts; reported fabricated answers, loops, and latency differences; and a causal explanation invoking penalty avoidance and training pressure. Each pair changes task framing, status threat, output shape, permission to fail, and availability of an acceptable fallback together.

**Curated heads and complete title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` across every authorized local destination. Fresh counts were: `notes` 360, `reference` 141, `sources` 296, `agent-memory-systems` 173, and `agentic-systems` 12.
- The reference head and title surface contained no Commonplace-specific selection or state that this practitioner prompt study would clarify. The agent-memory and agentic-system heads and title surfaces likewise contained no system review sharing a specific comparison axis with this prompt experiment. Those three destinations were skipped after the trigger check rather than searched for generic topical overlap.

**Description listing and body search — notes:**

- `rg '^description:' kb/notes/ --glob '*.md'` flagged the experimental-contrast, structured-prompt, prompt-variation, psychology-transfer, underspecification, and reliability clusters.
- `rg -n -i 'fallback token|safety-token|permission to fail|acceptable (no[- ]?op|fallback)|abstain|warranted abstention|no-change outcome|forced (answer|output|verdict|choice)' kb/notes/ --glob '*.md'` found no existing note whose claim directly owns permitted failure outputs.
- `rg -n -i 'authoritarian|high[- ]stakes|pressure|penalt(y|ies)|emotion(al)? prompt|empathetic|prompt framing|prompt tone' kb/notes/ --glob '*.md'` surfaced [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md), [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md), and the prompt-sensitivity neighborhood. Prompt ablation was rejected because the PoC changes several variables at once.
- `rg -n -i 'multi-factor confound|prompt bundle|contrast it actually runs|systematic prompt variation|ablation' kb/notes/ --glob '*.md'` kept [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) as the precise causal-grain target.
- `rg -n -i 'structured[- ]prompt|training distribution|selection history|RLHF|prompt gains|prompt.*train|train.*prompt' kb/notes/ --glob '*.md'` kept [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md), because the PoC attributes the bundle's behavior to hard training penalties without a contrast that distinguishes that mechanism.
- `rg -n -i 'confabul|hallucin|reasoning loop|overthinking|freez(e|ing)|unresolvable|impossible prompt' kb/notes/ --glob '*.md'` plus link following from the no-op comparison source kept [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md). The PoC reports detected impasses producing repeated reasoning, fabricated exits, and manual termination rather than a loud fail-stop.

**Description listing and body search — sources:**

- `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'prompt|framing|emotion|personality|stress|pressure|sycoph|reasoning|underspec|impossible|fallback|confabul|hallucin|latency|safety-token|tone'` surfaced the existing Gentle-Coding analysis, Prompt Stability, Simplification, RECV, semantic leakage, and content-effects sources.
- `rg -n -i 'authoritarian|gentle framing|gentle prompt|emotion(al)? prompt|personality prompt|pressure|penalt(y|ies)|permission to fail|fallback token|safety-token|impossible task|unresolvable|response policy|forced binary|prompt bundle|multi-factor confound' kb/sources/ --glob '*.md'` retained [Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) and [Assessing LLM Reasoning in Evidence-Based Claim Verification](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md). Both make the permitted response space load-bearing: the former proposes an explicit no-op control, while the latter identifies forced binary verdicts as a confound.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) passed the articulation test but was not retained as a new candidate because the existing Gentle-Coding ingest already authors that comparison.

**Link following and authored-surface checks:**

- Read the existing Gentle-Coding ingest in full. It already links the PoC analysis to psychology-transfer, systematic prompt variation, writing styles, underspecification, context efficiency, and Prompt Stability. Those edges were evaluated as existing state, not re-proposed as new outbound candidates.
- Followed the experimental-contrast note to systematic prompt variation and claim-granular warrant. This made the bundle-grain note a more exact target than the broader prompt-variation note: Gentle-Coding changes the claimed task state and output policy, not only surface framing.
- Followed the structured-prompt note to process/output structure. The latter was rejected as a direct edge because the PoC never varies process and output constraints independently.
- Followed the Simplification and RECV source neighborhoods through underspecification, fixed decompositions, and response policy. Together with this PoC they imply the synthesis opportunity below.
- `rg -n -i 'gentle[- ]coding|safety[- ]token|Otto Renner' kb/notes/ --glob '*.md'` returned no note-side links, so the reverse candidates remain unauthored.
- External prospecting was skipped as required. The original GitHub page is already represented by snapshot frontmatter and the composite ingest's `source` field; no additional external target was supplied or already loaded as a prospective edge.

## Connections Found

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: the PoC's condition pairs jointly change task framing, status threat, output constraint, permission to fail, and fallback availability. Its reported differences are therefore a concrete practitioner case of a bundle-level contrast that cannot identify “empathy,” “pressure,” or the fallback token separately.
- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) — **is-evidence-for**: the PoC moves a structured prompt bundle and then attributes the result to penalty-shaped training dynamics. Because it does not distinguish training-distribution activation from response policy, task semantics, salience, extra reasoning requirements, or fallback availability, it is a worked negative case for the note's causal boundary.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) — **is-evidence-for**: on impossible tasks, the PoC reports continued re-derivation, arbitrary answers, and one manually terminated reasoning loop instead of immediate failure; its gentle conditions add an acceptable terminal state. The unlogged timings make this bounded practitioner evidence, not a measured cost estimate.
- [Ingest: Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) — **compares-with**: Briggs predicts that an open-ended coding request fabricates work when it lacks an acceptable no-change result; Gentle-Coding supplies an analogous impossible-task case and an explicit fallback completion. Simplification also proposes the cleaner control Gentle-Coding lacks: hold framing fixed and vary only the no-op branch.
- [Ingest: Assessing LLM Reasoning in Evidence-Based Claim Verification](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) — **compares-with**: RECV shows the evaluation-side version of the same response-space issue, where removing `unverified` and forcing SUPPORTS/REFUTES can turn warranted abstention into apparent reasoning error. Gentle-Coding instead reports better behavior when “Random,” “No word present,” or uncertainty becomes an allowed completion.

## Bidirectional Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) ↔ [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) — return **evidenced-by**: the PoC is a compact worked case in which fine-grained observations do not refine the jointly varied treatment bundle into a component-level cause.
- [Structured-prompt gains do not establish training-distribution selection](../../../../notes/structured-prompt-gains-do-not-establish-distribution-selection.md) ↔ [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) — return **evidenced-by**: the source explicitly makes the training-penalty attribution that its prompt comparison cannot discriminate from several inference-time rivals.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../notes/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) ↔ [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) — return **evidenced-by**: the reported loop and fabricated exits are a bounded external instance of detected blockage being absorbed into continued interpretation rather than surfaced as a hard failure.

## Reverse-edge Candidates

- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) — **evidenced-by**: the PoC is a non-memory worked case where a reusable engineering mechanism (task stakes plus permitted fallback) is bundled with an anthropomorphic anxiety/trauma explanation. It lets the note test whether the named human mechanism transfers or merely supplies vocabulary for a prompt-contract effect.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — already linked from the Gentle-Coding ingest. No return edge is proposed because the PoC does not hold task semantics fixed: its paired prompts change whether a solution is asserted to exist, along with tone and response policy. The experimental-contrast candidate above states the exact limitation.
- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — requires only framing to vary against a fixed known target. The PoC jointly changes several treatment components, so calling it an ablation would misdescribe the design.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) — both dimensions change across the PoC conditions, but neither is independently varied. The structured-prompt and experimental-contrast targets already tell the reader why that bundle cannot support component attribution.
- [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) and [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — both are already discussed in the composite ingest. As direct evidence, the PoC is weak because its conditions change task assertions and allowable outputs rather than preserve one semantic specification under stylistic variation; Prompt Stability is the cleaner local evidence.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the PoC labels latency only as “fast,” “takes long,” or manual stop and explicitly says time and token costs were not scientifically measured. That is insufficient for a fresh evidence edge about context efficiency.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — the Safety-Token is an explicit allowed response, not silent recovery from a failed path. The shared word “fallback” does not supply the note's mechanism.
- [Prompt Stability in Code LLMs](../../../../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) — a genuine controlled counterpart, but the current Gentle-Coding ingest already authors this comparison, so it is not a candidate future edge.

## Index Membership

None.

## Synthesis Opportunities

- **A response space determines whether warranted non-success is representable.** [Gentle-Coding](../../../../sources/gentle-coding.ingest.md) permits “Random,” “No word present,” or expressed uncertainty; [Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) predicts fabricated code changes when no no-op completion is available; and [RECV](../../../../sources/assessing-llm-reasoning-evidence-based-claim-verification.ingest.md) removes `unverified` and forces a binary verdict. Together they imply a higher-order claim not yet owned by a note: an explicit no-op, unknown, or insufficient-evidence branch changes the task's possible correct outcomes rather than merely making its tone gentler. Evidence remains bounded to two practitioner reports and one benchmark-design analysis.

## Maintenance Observations

- The composite [Gentle-Coding ingest](../../../../sources/gentle-coding.ingest.md) explicitly covers this snapshot, but its registered primary checksum (`5c9960…`) belongs to `gentle-coding.md`; this PoC's checksum is `1a8e61…`, its file-level source URL differs from the ingest's repository URL, and no `gentle-coding-proof-of-concept.ingest.md` exists. `commonplace-validate kb/sources` therefore currently reports the snapshot as unpaired: no same-stem ingest and no ingest matching its URL or checksum. A future ingest-maintenance pass should give this supporting snapshot machine-checkable ownership; connect does not alter the ingest.
- The composite ingest's `## Claims` section still says “No claims have been grounded yet.” Before a writer promotes the reverse `evidenced-by` candidates, an ingest pass should ground the exact PoC propositions and locators needed for those evidence uses rather than relying only on the local snapshot and summary prose.

## Flags

- **Causal-attribution tension:** the source calls prompt architecture the sole independent variable, but each authoritarian/gentle pair changes multiple causally relevant components. Retain only a bundle-level behavioral comparison unless a factorial or matched ablation isolates tone, stakes, output policy, and fallback availability.
- **Measurement boundary:** model versions, run logs, repeated-run variance, token counts, and measured timings are absent; the source itself says timing and token costs were not scientifically measured. Treat the reported 100% fabricated-number result and latency/loop observations as small practitioner data, not a population estimate or verified mechanism.
