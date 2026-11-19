---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/jdegoes-recursive-agent-architecture-2081854216264392934.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Your Old Agent Architecture Is Dead… Meet Its Replacement

**Source:** [Your Old Agent Architecture Is Dead… Meet Its Replacement](../../../sources/jdegoes-recursive-agent-architecture-2081854216264392934.md)

## Discovery Trace

**Description listing scan:**
- Read the self-improving-systems and computational-model routing surfaces, then scanned titles and descriptions across `kb/notes/`, `kb/reference/`, `kb/agentic-systems/`, and `kb/agent-memory-systems/`.
- Retained the deploy-time-learning, prose/symbolic-boundary, verifiability-gradient, code/inference-checkpoint, select/call, and scheduler-separation candidates because the source makes claims on those exact axes.
- Retained [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) as the concrete local comparison target the source itself discusses.

**Topic indexes:**
- Read [self-improving-systems](../../../../tags/self-improving-systems-README.md), [deploy-time-learning](../../../../tags/deploy-time-learning-README.md), and [computational-model](../../../../tags/computational-model-README.md) routing heads where present.
- The self-improving-systems head routed the source's claim about code/prose movement and actor allocation; the computational-model surface routed the recursive orchestration and code/inference boundary claims.

**Body search:**
- `rg -n -i "prompt.*code|code.*prompt|co.?evol|co.?recurs|recursive|code.*writes.*code|prompt.*compile|natural-language.*symbolic|symbolic.*natural-language"` over notes and reference.
- `rg -n -i "LLM.*code|code.*LLM|scheduler|tool loop|dynamic workflow|verifiability|constraining|relaxing|middleware|compiled"` over notes, reference, and agentic-systems.
- Candidate evaluation separated agreement on code-owned bookkeeping and recursive orchestration from disagreement about whether natural-language guidance is merely decoration and whether the movement across the boundary is one-way.

**Link following:**
- Followed [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) to [The verifiability gradient](../../../../notes/verifiability-gradient.md), then followed the boundary and scheduler notes. The chain exposed a settled tension: both accounts favor codifying reliable bookkeeping, but Commonplace explicitly preserves loosening and judgment-bearing natural-language as a valid end state.
- Followed [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) as the local implementation comparison; its model-authored JavaScript orchestration matches the source's recursive code/inference example, while its saved-command path remains more limited than the source's proposed universal architecture.

## Connections Found

- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **compares-with**: both describe behavior moving between natural-language prompts and deterministic code during deployment; the source hardens the movement into a mostly one-way compilation thesis, while the note treats code and prompts as co-evolving and preserves natural-language for irreducible judgment.
- [Improving an agentic system crosses the natural-language/symbolic boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) -- **compares-with**: the source supplies an external argument for crossing from prose rules to middleware and for reverse pressure when enforcement is insufficient; its claim that prose is decoration is stronger than this note's bidirectional boundary account.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- **compares-with**: the source's prompt→typed plan→test→code hardening path is a concrete placement on the gradient, but it underplays the note's loosening direction when a check loses its warrant.
- [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) -- **is-evidence-for**: the source's recursive code–inference alternation is a practitioner formulation of symbolic orchestration with bounded LLM calls, including nesting and explicit state between calls.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: both use model-authored code to orchestrate sub-agents and move bookkeeping out of the conversation; the source generalizes the shipped, depth-capped feature into a universal recursive architecture.

## Bidirectional Candidates

None. The ingest report is the source's authored surface; the durable comparison belongs there unless a later note revision chooses to add an evidence edge.

## Reverse-edge Candidates

- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) → source -- **evidenced-by**: the source is a concrete external argument for prompt/code movement during deployment, including a clearly stated hardening direction and a competing claim about the natural-language endpoint.
- [Improving an agentic system crosses the natural-language/symbolic boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) → source -- **evidenced-by**: the source supplies a strong counterpoint on the reliability pressure to compile prose into middleware and on the residual role it leaves to inference.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) → source -- **evidenced-by**: the source's typed plans, test tenants, middleware, and contained runtime instantiate multiple grades of the gradient while asserting a stricter hardening policy.
- [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) → source -- **evidenced-by**: the source independently describes nested code containing inference and inference emitting code as the general shape of capable systems.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [LLM context is a homoiconic medium](../../../notes/llm-context-is-a-homoiconic-medium.md) was rejected as a primary connection: the source discusses prompt injection and prose/code boundaries, but its central claim is execution architecture rather than shared representation of code and data.
- [Inspectability of readable artifacts](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) was rejected as secondary: the source's plans and middleware are inspectable, but the stronger comparison is already carried by the verifiability-gradient and boundary notes.
- Product-specific claims about Golem and external Cloudflare/Anthropic evidence were not separately prospected; connect does not browse the open web and the source's own claims remain source-level evidence.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the article contributes a contested practitioner formulation of code/prose co-recursion, hardening, and human-free execution capacity.
- [Computational model](../../../../tags/computational-model-README.md) -- the article contributes a concrete recursive code–inference architecture and a strong scheduler/guardrail separation thesis.

## Synthesis Opportunities

This source plus [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) and [The verifiability gradient](../../../../notes/verifiability-gradient.md) expose a useful comparison question: is code–prompt coevolution best understood as a reversible placement process along a verifiability gradient, or as a one-way compiler pipeline whose natural-language residue is only a temporary failure to formalize? The source is a counterpoint that sharpens the boundary rather than settling it.

## Maintenance Observations

None.

## Flags

- The article makes several independent assertions—recursive orchestration, plan-as-program execution, compiled guardrails, typed machinery, and durable runtime requirements. If it later informs a note, split those claims rather than citing the article as one undifferentiated architecture.
- The source uses “reliable” and “guarantee” rhetorically across code and middleware; implementation and runtime inspection would be needed before treating those as demonstrated properties.
