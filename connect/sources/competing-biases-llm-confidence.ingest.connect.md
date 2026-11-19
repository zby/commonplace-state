---
description: "Answer ownership and opposing advice change calibrated confidence in bounded LLM tasks, informing validation of confidence and review context."
type: kb/reports/types/connect-report.md
source: kb/sources/competing-biases-llm-confidence.ingest.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: Competing biases in LLM confidence

**Source:** [Paper ingest](../../../../sources/competing-biases-llm-confidence.ingest.md)

## Discovery Trace

Read the completed ingest fully after checksum, metadata and exact Quotes checks. Reassessed its selected confidence-validation contribution and experimental proposal. All three pre-ingest comparisons remain bounded and useful; the confidence note independently benefits from an empirical example of changed context, while the contamination note gains no direct evidence of refusal-resistant drift. No reciprocal link is warranted merely by the outbound link.

Read the complete 2,748-line captured article including Methods, code-availability statement and references. Reused same-batch source and destination contracts, curated heads and complete claim-title surfaces for notes, reference, sources, agent-memory-systems and agentic-systems. Ran `rg -n -i '^description:.*(confidence|self.evalu|self.critic|independen.*review|agreement|anchoring|blind)' kb/notes --glob '*.md'` and `rg -n -i '(blind|independent.*critic|fresh.*review|self.*bias|self.preference)' kb/notes --glob '*.md'`. Read generation-confidence and context-contamination notes fully; followed the former to reliability-dimensions and read it fully. These distinguish confidence from soundness, contextual influence from refusal, and calibration from discrimination. `rg -l -i 'competing biases|choice.supportive|confidence.*dynamics' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` returned no matches. No further edge selected in those destinations: the paper concerns confidence updating in bounded queries, not a demonstrated memory architecture or shipped Commonplace procedure. External prospecting skipped; excluded collections not traversed.

## Connections Found

- [Generation confidence](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) — **is-evidence-for**: answer-token probabilities calibrated on one population change when the model sees its own answer or receives fictitious advice. This gives a bounded empirical case for validating a confidence signal under its actual consumption context; it does not establish a universal inverse relation with truth.
- [Context contamination](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — **compares-with**: showing a prior answer as the model's own changes later commitment, whereas attributing it to another model removes the measured choice-supportive effect in a control. This compares attribution-sensitive influence with the note's own-voice stance experiment; it does not replicate refusal-resistant writing drift.
- [Reliability dimensions](../../../../notes/reliability-dimensions-map-to-oracle-hardening-stages.md) — **compares-with**: initial probability calibration, discrimination and subsequent normative updating are different measurements. A fitted calibration temperature does not by itself validate confidence after altered conversational evidence.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Generation confidence](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) → this tracked ingest — **evidenced-by**: adds a specific context-sensitive calibration example for the note's requirement that confidence use inherit task-validation limits. Preserve the answer-token measurement, initial-option target and synthetic-advisor assumptions.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- A generic prescription to hide all prior work from reviewers: the experiments do not compare long-form review quality or required evidence loss.
- Direct evidence of contamination surviving explicit refusal: that manipulation is absent here.
- Confidence equals correctness or an internal belief readout: token probabilities and the chosen normative benchmark do not establish either interpretation.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

The main article is captured; separately linked supplementary information is not part of this observation. Models include Gemma 3 12B/27B, GPT-4o, o1-preview, DeepSeek V3 and Llama 3.1 70B; o1 lacks confidence measurements. Most queries use temperature 1 and short completions; DeepSeek uses 0.7. Main latitude trials use binary choices, while SimpleQA and GSM-MC use four choices with constructed distractors. Task difficulty differs across models, so a cross-model ranking would be confounded. The same questions recur across conditions; stateless model calls do not make all observations independent items.

Advice comes from no actual second model: its answer and stated accuracy are experimentally assigned. The Bayesian observer assumes the stated accuracy supplies the required conditional likelihood, and uses calibrated initial confidence as prior. Calibration uses 40,000 held-out latitude questions and a fixed Gemma temperature 3.3, with residual ECE .09; the paper's claim that this rules out calibration artifacts is stronger than demonstrating perfect calibration under every changed condition. The main confidence variable is probability of the initially selected option even after a changed final answer, not confidence in the final choice. OUCS is a deviation from an ideal-observer prediction, not ordinary accuracy calibration. The extracted OUCS equation and prose/sign interpretation merit care; do not silently resolve a source inconsistency through invented precision.

Showing the model its own initial answer generally reduces changes of mind and boosts confidence even with neutral advice. Incorrect-answer and fictitious-city controls address simple copying and a pure in-context versus weights account. Attribution to another model removes the measured choice-supportive effect in that control; multiturn validation reproduces it. These support a behavioral ownership effect, not a mechanistically established human-like drive. Opposing advice produces larger-than-ideal updates, with model-specific variation; same-advice effects are smaller and not uniformly absent. Corrected shown-opposite ratios subtract a population-average visibility effect, an additive adjustment rather than a direct mechanism isolation. The two biases can coexist.

Bayesian regression fitted to SimpleQA transfers to GSM-MC for reported variables; two task families do not prove generality to open-ended reasoning or autonomous revision. RLHF and self-consistency explanations remain hypotheses. Code availability explicitly releases figure and Bayesian-regression code; complete experiment inference depends on proprietary Google infrastructure. Code analysis is a separate workflow, not evidence inspected for this paper ingest.
