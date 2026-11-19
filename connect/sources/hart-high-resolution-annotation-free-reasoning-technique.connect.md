---
description: "Discovery report for possible KB connections from the HART paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/hart-high-resolution-annotation-free-reasoning-technique.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: HART visual evidence selection

**Source:** [HART paper snapshot](../../../sources/hart-high-resolution-annotation-free-reasoning-technique.md)

## Discovery Trace

**Description listing scan:**
- Ran `rg -n -i '^description:.*(oracle|verif|context|routing|retriev|select|diagnostic|evidence|ground|reward|reasoning|feedback|proxy|causal)' kb/notes --glob '*.md'`. Kept the outcome/process, learned-selection, oracle-domain, and fixed-experiment candidates; rejected generic context-window and structural-validation matches.
- Ran the same scoped description query over `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, and `kb/sources`. The reference results described shipped Commonplace machinery rather than this paper; the system collections described complete deployed systems, whereas HART is a model post-training method. The source scan surfaced VAIR and CEDAR-GRPO as discriminating comparisons.

**Topic indexes:**
- Read `kb/notes/README.md` and `kb/notes/tags-README.md`; the relevant routing heads were context engineering, learning theory, and LLM reliability. The snapshot has no `tags` field, so no tag-completeness shortcut applied.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. No direct reference, agent-memory-system, or agentic-system membership was warranted; `kb/sources/` is the correct descriptive home.

**Full title scans:**
- Ran `rg -N --no-heading -m1 '^# '` over each authorised local destination: `kb/notes`, `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, and `kb/sources`. The complete surfaces confirmed that the closest durable claims concern oracle discrimination, outcome-versus-process evidence, feedback-trained selection, and fixed experimental decompositions.

**Body search:**
- `rg -n -i 'answer correctness|final-answer|final answer|correct answer' kb/notes --glob '*.md'` kept [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) and [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md).
- `rg -n -i 'oracle domain|reward misspecification|proxy|discriminat|diagnostic' kb/notes --glob '*.md'` kept [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) and the fixed-experiment lenses; generic proxy mentions were rejected.
- `rg -n -i 'context (routing|selection)|evidence (routing|selection)|select.*evidence|retriev.*relevant|relevant.*context' kb/notes --glob '*.md'` kept [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) as an explicitly analogical transfer target. [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) was rejected because HART learns an inferred selector rather than specifying a rule-ready routing signal.
- `rg -n -i 'answer correctness|final-answer|final answer|reward misspecification|grounding|process-aware|reasoning evaluation|oracle domain' kb/sources --glob '*.ingest.md'` kept the VAIR and CEDAR-GRPO reports.
- Equivalent routing/oracle searches in `kb/agent-memory-systems` and `kb/agentic-systems` found broad thematic overlap but no useful artifact-level edge from this scientific paper.

**Link following:**
- Followed the outcome/process cluster from the VAIR ingest to the checked-outcome and reasoning-evaluation notes. HART supplies a complementary intervention: it restricts the answerer's accessible evidence to make outcome success more informative about evidence sufficiency, while VAIR shows that unrestricted answer agreement can remain non-discriminating about process validity.
- Followed the learned-memory-policy note to oracle-domain and automation-boundary claims. The visual-to-KB routing transfer remains an inference, not a result reported by HART.
- Followed the experiment notes to the fixed-decomposition lens. HART varies its feedback loop, optimizer stages, and `k`, but retains bounding boxes, crops, prompts, model families, answer oracle, and benchmark decomposition.
- External prospecting was skipped: `external` is authorised only for already-known targets, and no additional external target was supplied for this connection pass.

## Connections Found

- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — **is-evidence-for**: HART's withhold-the-full-image intervention is a concrete test of whether selected evidence is sufficient for an outcome, while its surviving correct-answer/incorrect-grounding cases also show why outcome success does not fully identify the producing route.
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) — **compares-with**: HART is a visual worked case of learning a selection policy from downstream outcomes after redesigning the execution context to make those outcomes more discriminating; transfer to textual KB routing is our inference.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) — **rests-on**: HART's self-verification claim is warranted only for grounding cases where cropped-evidence answer correctness discriminates sufficiently; the paper's residual mismatch and benchmark-specific oracle keep that domain bounded.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) and [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **rests-on**: the reported gains support learning within the fixed ROI/crop/answer pipeline and the actual AP-GRPO/SFT contrasts, not the universal adequacy of that decomposition.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) — **compares-with**: VAIR exposes answer correctness as non-discriminating for reasoning validity; HART instead restricts causal access to increase how diagnostic answer correctness is of selected-evidence sufficiency.
- [CEDAR-GRPO ingest](../../../../sources/cedar-grpo-process-aware-rl-abductive-reasoning.ingest.md) — **compares-with**: CEDAR adds explicit process-reward signals, whereas HART changes the execution intervention so a final-answer signal carries more information about an intermediate selection.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) → HART snapshot — **evidenced-by**: a future revision could cite HART as a bounded cross-domain example of hardening a downstream outcome signal by isolating the selected evidence, while marking the KB-routing transfer as an experiment proposal rather than an established result.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) → HART snapshot — **evidenced-by**: HART provides an intervention-based sufficiency check and simultaneously reports residual outcome/process mismatch, which helps delimit what such a check establishes.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Rule-based context selection needs a pre-existing signal](../../../../notes/rule-based-context-selection-needs-a-pre-existing-signal.md) — rejected because HART predicts regions from image/question content; it does not study codified routing from a pre-existing rule-ready signal.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — rejected because HART changes reward diagnosticity by restricting accessible evidence; it does not give a later proposer richer failure evidence.
- `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` candidates — rejected because the paper neither describes the shipped Commonplace system nor constitutes a deployed agent-memory or agentic system.

## Index Membership

None.

## Synthesis Opportunities

- HART, VAIR, and the memory-policy oracle note jointly suggest a higher-order hypothesis: an outcome oracle can sometimes be hardened by experimentally isolating the candidate evidence or operation whose contribution is under evaluation, not only by replacing the judge. HART establishes this locally for visual-region sufficiency; applying it to KB context routing still requires a dedicated experiment and stronger negative controls.

## Maintenance Observations

None.

## Flags

- HART's Proposition 1 moves from higher mutual information to language of stronger "causal dependency." Mutual information alone is not causal evidence; the withholding intervention gives a causal-access argument, but question-only shortcuts, crop leakage, and residual correct-answer/incorrect-grounding cases remain live alternatives.
- The KB context-routing analogy is explicitly an inference. The paper evaluates image regions, bounding boxes, and high-resolution visual benchmarks, not text retrieval, linked notes, or agent-operated KB decisions.
