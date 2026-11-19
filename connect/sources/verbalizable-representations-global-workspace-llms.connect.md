---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/verbalizable-representations-global-workspace-llms.md"
source_has_frontmatter: true
date: "2026-08-03"
depth: standard
---

# Connection Report: Verbalizable Representations Form a Global Workspace in Language Models

**Source:** [Verbalizable Representations Form a Global Workspace in Language Models](../../../sources/verbalizable-representations-global-workspace-llms.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/sources/COLLECTION.md`: snapshots are immutable; the authored connection surface is the ingest report, and useful reverse edges usually come from notes pointing to source snapshots as `evidence` or `derived-from`.
- Read curated heads: `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Ran `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' | rg -i "represent|parametric|memory|context|artifact|learning|reason|interpret|constrain|external|hidden|observ|activation|trace|reflection"`. Strong candidates: `representational-form`, `treat-continual-learning-as-substrate-coevolution`, `process-structure-and-output-structure-are-independent-levers`, `knowledge-storage-does-not-imply-contextual-activation`, `activate-behavior-changing-memory`, `agent-context-is-constrained-by-soft-degradation-not-hard-token-limits`, `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`. Rejected broad candidates: `context-engineering` and `distillation` definitions were adjacent but too generic for a load-bearing link.

**Topic indexes:**
- `kb/notes/tags-README.md` routed to learning theory, artifact analysis, context engineering, observability, and LLM interpretation errors. The strongest indexed fit was artifact analysis because the source is mainly useful as a concrete distributed-parametric inspection/intervention case.
- Re-read `kb/notes/context-engineering-README.md`, `kb/notes/foundations-README.md`, `kb/notes/llm-interpretation-errors-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/observability-README.md` on 2026-07-29. These confirmed direct reverse-edge value for the soft-bound and contextual-activation claims; the broader context-engineering and observability indexes remain routing surfaces rather than evidence targets.
- `kb/notes/observability-README.md` was read through search; it framed hidden-state visibility but did not itself warrant a durable source link because tag READMEs should not absorb evidence that belongs on claim notes.

**Body search:**
- Re-ran the complete note-title scan with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, then the scoped description scan `rg '^description:' kb/notes/ --glob '*.md' | rg -i "context|complex|activation|workspace|external|reason|represent|parametric|probe|hidden|process|memory|knowledge|observer|load|capacity|scarc|interference|retention|address"`.
- Re-ran `rg -n -i "externaliz|internal workspace|working memory|scratchpad|chain.of.thought|intermediate (state|steps)|carry.*(intern|context)|compositional.*(depth|complex)|cognitive load" kb/notes --glob '*.md'`, `rg -n -i "activation|activate|context.to.action|read.back|available knowledge|latent knowledge|retriev|causal.*use|behavior.*chang|task framing|elicitation" kb/notes --glob '*.md'`, and `rg -n -i "distributed.parametric|parametric state|probe|hidden state|inspectab|blackbox|observab|representational form" kb/notes --glob '*.md'`.
- Ran `rg -n "workspace|global workspace|J-space|Jacobian|verbalizable|conscious|introspection|internal reasoning|reflection|alignment auditing|prompt injection|hidden" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"`. This produced many false positives on ordinary workspace files and agent harness workspaces; kept only model-internal representation and hidden-state hits.
- Ran `rg -n "representational form|parametric|model weights|distributed|internal state|externalization|retained artifact|context engineering|symbolic|probe|activation" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"`. Kept `representational-form`, `treat-continual-learning-as-substrate-coevolution`, `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`, and `agent-memory-requirements/use-trace-derived-extraction` as context; rejected the last as memory-policy-specific rather than a direct fit.
- Ran `rg -n "counterfactual reflection|process|output|implicit chain|auxiliary reasoning|reflection training|ethical" kb/notes kb/sources --glob "*.md" --glob "!verbalizable-representations-form-global-workspace-language-models.md"`. Kept `process-structure-and-output-structure-are-independent-levers` and `treat-continual-learning-as-substrate-coevolution`.
- Ran `rg -n "probe|parametric|weights|distributed-parametric|J-lens|Jacobian|blackbox|inspect" kb/notes kb/sources --glob "*.md" --glob "!verbalizable-representations-form-global-workspace-language-models.md"`. Kept `representational-form`, `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`, `generation-confidence-does-not-by-itself-certify-soundness`, and `an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md`; rejected the generation-confidence note as only a weak analogy because this source does not test soundness representations.
- Ran `rg -n "activation|activate|context-to-action|read-back|behavior-changing|visible memory|WITH/WITHOUT" kb/notes kb/sources --glob "*.md" --glob "!verbalizable-representations-form-global-workspace-language-models.md"`. Kept `knowledge-storage-does-not-imply-contextual-activation` and `activate-behavior-changing-memory`.
- Ran `rg -n "externaliz|externalis|internal workspace|working memory|scratchpad|chain-of-thought|intermediate steps|carry in" kb/notes kb/sources --glob "*.md" --glob "!verbalizable-representations-form-global-workspace-language-models.md"`. Kept `agent-context-is-constrained-by-soft-degradation-not-hard-token-limits` and `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model` for the source's chain-of-thought-as-externalized-workspace result.
- Ran `rg -n -i "limited capacity|capacity|competition|interference|distract|bottleneck|chain.of.thought|external|ablat|multi.step|flexible|working memory|workspace" kb/sources/verbalizable-representations-global-workspace-llms.md`. This sharpened the soft-bound candidate beyond externalization: unrelated list items drop from J-space as lists grow, category switches rapidly evict the prior category, concurrent multi-step arithmetic and concept maintenance interfere, and J-space ablation preserves fluent continuation while selectively disrupting abstract context-sensitive inference.

**Link following:**
- Followed `agent-context-is-constrained-by-soft-degradation-not-hard-token-limits` to `context-efficiency-is-the-central-design-concern-in-agent-systems`, `feasibility-is-the-heaviest-forks-net-load`, and `llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model`. Kept the soft-bound note as the direct target; rejected the others because the paper neither establishes context as the system's central resource nor tests orchestration or fork scheduling.
- Followed `knowledge-storage-does-not-imply-contextual-activation` to `elicitation-requires-maintained-question-generation-systems` and `activate-behavior-changing-memory`. Kept the general activation note; the source does not test maintained question-generation or an agent-memory read-back system.
- Followed `representational-form` to `treat-continual-learning-as-substrate-coevolution` and `readable-artifact-loop-is-the-tractable-unit-for-continual-learning`; kept the substrate-coevolution note because counterfactual reflection training is a direct prose/text-to-parametric behavior-shaping case. Rejected `readable-artifact-loop...` as mostly contrasting background.
- Followed `process-structure-and-output-structure-are-independent-levers` to `reasoning-production-is-not-reasoning-evaluation`; rejected the latter as VAIR-specific, though the two papers compare usefully as source-to-source probe/patching evidence.

## Connections Found

- [representational form](../../../../notes/definitions/representational-form.md) -- **evidence**: the J-space is a concrete distributed-parametric operative part that is inspected by probing and intervened on by steering, swaps, and ablations.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **evidence**: the language-identification experiments show concepts can be present in J-lens readouts yet causally used only for report/flexible computation, not automatic continuation or anomaly detection.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: counterfactual reflection training changes later behavior by training reflective continuations that are never emitted at evaluation, separating process-shaping from direct output-format training.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **evidence**: reflection text supervises a distributed-parametric update whose behavioral effect is mediated by model-internal workspace concepts, making prose/text and weights visibly coupled.
- [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **evidence**: the J-space is a candidate internal mechanism spanning the note's dimensions. Its limited capacity makes unrelated content drop out and new categories evict old ones; concurrent concept maintenance interferes with multi-step arithmetic; ablation preserves fluent ordinary prediction while selectively disrupting context-specific flexible inference; and explicit chain-of-thought reduces dependence on the ablated workspace by externalizing intermediate state. Together these results mechanically connect volume, relevance/interference, complexity, and invisible degradation, while stopping short of proving that every long-context failure routes through J-space.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- **compares-with**: both sources use representation probes and causal interventions to separate surface output from hidden model state, but this source studies workspace-like reasoning while VAIR studies answer-confirmation bias in evaluation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -> source -- **evidence**: J-space capacity, displacement, dual-task interference, selective ablation, and chain-of-thought robustness jointly supply a candidate internal-workspace mechanism for the note's soft degradation surface. The return edge should appear in the explanatory body, not only as a footer example, because it relates the note's otherwise empirical dimensions through one causal model.
- [representational form](../../../../notes/definitions/representational-form.md) -> source -- **evidence**: add as a concrete "probe distributed-parametric artifacts" example, with the limitation that J-lens covers only a token-indexed, single-token-friendly subspace.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -> source -- **evidence**: use the J-space selective-mediation result to strengthen the note's context-to-action distinction with model-internal causal evidence.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -> source -- **evidence**: reflection training is a training-time instance where shaping potential reflective process changes behavior without directly supervising the target output.
- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -> source -- **evidence**: add as a distributed-parametric/prose coupling example alongside prompt/code/readable-artifact loops.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- rejected as a direct backlink target: the paper gives a mechanism for one face of the soft bound, not evidence that context is the system's single central resource; traversal through the soft-bound note is cleaner.
- [Bounded-context orchestration model](../../../../notes/bounded-context-orchestration-model.md) -- rejected: external chain-of-thought relieves internal workspace demand, but the paper does not test symbolic scheduling, prompt selection, or the select/call model.
- [Elicitation requires maintained question-generation systems](../../../../notes/elicitation-requires-maintained-question-generation-systems.md) -- rejected: task questions modulate J-space loading, but the paper does not test maintained elicitation systems; the general activation note carries the evidence without overextending it.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -- weak: coherent categories occupy J-space more efficiently than unrelated lists, but this model-specific capacity result is not needed to support the note's general observer-relative value claim.
- [Activate Behavior-Changing Memory Before The Mistake](../../../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) -- rejected as a direct backlink target: counterfactual reflection training provides an activation analogue, but it is not retained memory or an agent-memory read-back path; the general contextual-activation note is the precise target.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- weak: J-space is partially probeable, but the paper studies transient activation representations and does not provide the diff, test, rollback, or governance operations the note contrasts with weight updates.
- [context engineering](../../../../notes/definitions/context-engineering.md) -- rejected: the paper changes and probes model-internal representations; the definition explicitly excludes fine-tuning, RL, embedding-model improvement, and architecture changes from context engineering.
- The distillation concept was rejected: counterfactual reflection training has a distillation-like shape, but the source's value is better captured as cross-form training/probing rather than KB distillation; no current definition artifact exists to receive the link.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- weak: the J-lens is a soft probe/oracle over internal state, but the paper does not directly address verifier design or oracle hardening for KB operations.
- [Generation confidence does not by itself certify soundness](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) -- weak: the source supports the general possibility that hidden state diverges from output, but does not test truth or soundness representations.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- rejected as a note target: the source is adjacent through hidden-state probing, but VAIR remains the cleaner evidence for evaluator route inspection.

## Index Membership

None

## Synthesis Opportunities

- The source, [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md), and [LLM-mediated schedulers are a degraded variant of the clean model](../../../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) together imply a candidate note: externalized reasoning trades internal workspace demand for context budget. The source supplies a mechanistic result: written chain-of-thought reduces dependence on the J-space under ablation.
- The source, [representational form](../../../../notes/definitions/representational-form.md), and [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) suggest a caveat to the KB's current readable/opaque contrast: some distributed-parametric state may be locally probeable and steerable, but probeability is weaker than artifact inspectability because it lacks stable discrete commitments, provenance, diff, review, and rollback.

## Maintenance Observations

- The authored soft-degradation note already links this ingest in its `Relevant Notes` footer, added by commit `dc67ccca`, but the edge's context phrase mentions only flexible-reasoning ablation and chain-of-thought relief. It omits the paper's capacity, displacement, and dual-task results, leaving the strongest candidate mechanism outside the note's explanatory body.

## Flags

- Split candidate: the source contains at least four separable promotion targets -- J-lens/J-space method, activation-vs-presence evidence, alignment auditing of hidden deliberation, and counterfactual reflection training. Promote one claim at a time rather than writing a broad "global workspace in LLMs" note.
