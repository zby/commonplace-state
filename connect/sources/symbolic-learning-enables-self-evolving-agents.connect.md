---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/symbolic-learning-enables-self-evolving-agents.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Symbolic Learning Enables Self-Evolving Agents

**Source:** [Symbolic Learning Enables Self-Evolving Agents](../../../sources/symbolic-learning-enables-self-evolving-agents.md)

## Discovery Trace

**Curated heads and full listings:**
- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`; no source tags were available for tag-README routing.
- Generated complete `#` title listings and `description:` listings for notes, reference, agent-memory-systems, agentic-systems, and sources. The notes surface foregrounded the deploy-time-learning, readable-artifact, representational-form, and self-improving-system clusters. Reference had no direct shipped-system analogue. Agent-memory results were mostly trace-learning systems with narrower retained-memory targets. Agentic systems supplied Exo as a much broader code-rewriting comparison. Sources supplied Co-Harness as the closest successor comparison.

**Body search:**
- `rg -i 'symbolic learning|language gradient|textual gradient|joint.*optimi|optimizable graph|prompt.*tool.*pipeline|self-evolv|self-improv|deploy-time learning|test-time learning' ...` -- kept the two representational-form coevolution notes; rejected keyword-only self-improvement mentions.
- `rg -i 'prompts, tools|prompts.*tools.*pipeline|pipeline.*prompts.*tools' ...` -- kept the readable-artifact target and Co-Harness comparison; the harness-taxonomy sources only enumerate components and do not address joint learning.
- `rg -i 'textual.*gradient|natural.language.*gradient|feedback.*artifact|trajectory.*update' kb/notes ...` -- evaluated the natural-language/symbolic-boundary and theory-mediated-self-improvement notes; retained the former only as a reverse-edge possibility because the paper mutates both forms but does not study governed boundary crossing.

**Link following:**
- Followed [representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) to [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), and [constraining during deployment](../../../../notes/constraining-during-deployment-is-continuous-learning.md). The source supplies a concrete joint optimizer for prompts, tool definitions/implementations, and pipeline structure, but its rollback uses the same prompted loss and its experiments do not establish durable cross-session operation.
- Followed [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) to Co-Harness. Co-Harness crosses from harness artifacts into model weights; this 2024 paper instead keeps weights fixed and optimizes the readable harness as one network, making the pair a useful chronological and architectural comparison.
- Followed the self-improvement cluster to Exo and theory-mediated self-improvement. Exo's protected substrate, build/test gates, and full code rewrite are too different for an outbound edge from this ingest; retained as a rejected candidate.

## Connections Found

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: the paper is an early concrete attempt to optimize natural-language prompts and symbolic tools/pipeline structure jointly while holding model weights fixed, directly instantiating one pair in the note's three-form frame.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: its trajectory, language-loss, backward credit-assignment, and rollback procedure shows that prompts, tools, and topology can be treated as one editable and evaluable artifact surface.
- [Co-Harness: Co-Evolving Harnesses and Model Weights for LLM Agents](../../../sources/co-harness-co-evolving-harness-and-model-weights.md) -- **compares-with**: both learn from execution trajectories and optimize prompts/tools/harness structure, but symbolic learning holds weights fixed and applies language-gradient updates across one symbolic network while Co-Harness alternates validated harness repair with weight fine-tuning.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -> source -- **evidenced-by**: the source supplies the note's missing early example of joint natural-language/symbolic optimization, with cross-node credit assignment rather than isolated prompt search.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -> source -- **evidenced-by**: the source operationalizes the proposed readable pair, though only as proof-of-concept benchmark training.
- [Improving an agentic system crosses the natural-language/symbolic boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) -> source -- **evidenced-by**: tool creation/deletion and pipeline mutation alongside prompt revision are a concrete cross-form improvement path, bounded by the paper's weak acceptance oracle.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- rejected as duplicative: the two retained coevolution/readable-loop notes state the more specific reader need, and the paper's experiments are offline rather than demonstrated deployment-time accumulation.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- rejected: the framework interprets trajectories and revises agent configuration, but the paper does not analyze theory retention, separable applicability conditions, or explanatory reach.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected: both concern self-modification, but Exo's protected substrate, rebuild/restart mechanism, and executable acceptance boundary make the comparison too broad to aid traversal from this focused optimizer paper.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected: trajectories feed optimization, but the paper does not present a retained memory subsystem or analyze read-back, promotion, and authority.

## Index Membership

None

## Synthesis Opportunities

- The source, [the readable-artifact loop](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), and Co-Harness together suggest a historical progression from isolated prompt optimization, through whole-readable-harness optimization, to alternating readable-harness/weight coevolution. The unresolved discriminator is not editability but validation radius: this paper's same-model language loss both proposes and judges updates, whereas later systems add held-out or executable gates.

## Maintenance Observations

None

## Flags

- The paper repeatedly calls prompts and tool descriptions “symbolic weights,” but under the KB's representational-form vocabulary prompts remain natural-language and only code, schemas, and graph operations are symbolic. Preserve that vocabulary mismatch when citing the source.
