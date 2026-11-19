---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/hyra-2-next-step-for-auto-research.ingest.md"
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: Ingest: Hyra 2.0: The Next Step for Auto Research

**Source:** [Ingest: Hyra 2.0: The Next Step for Auto Research](../../../../sources/hyra-2-next-step-for-auto-research.ingest.md)

The ingest already carries 16 labelled footer links (theory, sources, agentic-systems, external). This report proposes only additions and reverse edges beyond that set.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` outbound section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `rests-on`/`abstracted-from` (theory), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped: no external target beyond the already-linked source URL.

**Topic indexes:**
- Source tags `self-improving-systems`, `continual-learning`, `agent-memory`: all three heads declare `complete: true`, so by-tag rg was skipped. Sources are outside the participating collections, so tag heads give no source-membership action.

**Description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` filtered by `tool|skill|review|evidence|promot|verif|amorti|reproduc|retrospect|memory|hierarch|orchestr|research|anchor|reuse|distil|compound|self-improv|authority|claim` -- flagged: improvements-can-accumulate-without-compounding, usefulness-autonomy-warrant-and-power-are-separate-dimensions, computationally-directed-self-improvement-is-a-reallocation, retaining-episode-evidence-keeps-a-distilled-rule-open-to, agent-memory-requirements/make-authority-explicit, factory-construction-does-not-establish-knowledge-acquisition, accumulation-counts-dependence-through-the-retained-result, topology-isolation-and-verification..., memory-backed-personalization-can-look-like-model-improvement.
- `rg -N '^description:'` over the flagged theory files, over `kb/agentic-systems/reviews/*.md`, and over `kb/agent-memory-systems/reviews/autocontext.md` -- read to judge fit (evaluations below).

**Body search:**
- `rg -il 'autoresearch|auto-research|auto research|AI scientist|ai-scientist' kb/theory kb/sources kb/agentic-systems kb/agent-memory-systems kb/reference` -- 33 files; source ingests on research harnesses evaluated: primescientist, how-agents-fail-on-autoresearch, ai-scientists-results-without-scientific-reasoning, position-ai-agents-in-scientific-teams, harness-engineering-for-self-improvement, when-code-is-free, alien-space-of-science, weco-autoresearch-vs-classical-hpo, accelerating-scientific-research-gemini-real-world.
- `rg -l 'agora-git-as-shared-memory|hypothesis-evolution-protocol-auditable' kb` -- finds where sibling auto-research memory sources are cited (one theory note, plus an excluded work file).
- `rg -n 'sources/' <compounding, trace-extracted, long-run-learning, usefulness-autonomy, computationally-directed notes>` -- checked whether target notes carry source-case lists that Hyra could join (compounding note has an evidenced-by case list; computationally-directed cites Poetiq).
- `rg -n -i 'anchor|blind' kb/reference/review-architecture.md kb/reference/README-REVIEW-SYSTEM.md` -- "anchored" there means snapshot-anchored, not evidence-before-conclusion ordering; no reference target.
- `rg -n -i 'Observation|Verified|Convention|grade' kb/theory/trace-extracted-memory-...` -- confirms the rung model (record → verify → abstract) already linked.
- `rg -n -i 'hyra' kb` -- only the ingest itself; no inbound links yet.

**Link following:**
- compounding-is-tested note → its source cases (HyperAgents, Agent Optimizers, Harness Updating, Poetiq, Frontis Horizon) → flagged Poetiq and last-ai-built-by-humans as sibling vendor RSI claims.
- usefulness-autonomy note → warranted-autonomy / human-effort-relocation neighbours; confirmed the note asks progress claims to name which dimension moved.

## Connections Found

- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) -- **is-evidence-for**: Hyra reports per-tool usefulness (seven tool benchmarks) and then claims system power through a recursive self-improvement loop; the post is a clean case of a progress claim that moves one dimension and asserts another.
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../../../../theory/computationally-directed-self-improvement-is-a-reallocation.md) -- **is-evidence-for**: Hyra's RSI loop still routes Convention promotion, shared-knowledge sync and Hy model training through humans and the Hunyuan team; the note's question "which decision-bearing functions do humans still supply" is exactly what the ingest's undeclared-boundary point needs.
- [Improvements can accumulate without compounding](../../../../theory/improvements-can-accumulate-without-compounding.md) -- **compares-with**: on the accumulation/compounding axis, Hyra's tool and Books retention shows accumulation by design, while its amortisation argument asserts compounding; this note supplies the distinction more precisely than the compounding-test note alone.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- **is-evidence-for**: Books entries must carry their evidence (code versions, logs, traces) and are revised as evidence changes, a deployed instance of keeping the episode-to-rule relation available.
- [Ingest: How Do Agents Fail on AutoResearch?](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) -- **compares-with**: on review-to-revision failure, AutoResearchEval measures agents that notice but do not repair problems; Hyra states as policy that review findings "must be faithfully retained" and that Workers attach evidence, without measuring repair.
- [Ingest: A Poetiq Perspective on Recursive Self-Improvement](../../../../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) -- **compares-with**: both are vendor RSI accounts whose compounding and closure claims rest on per-benchmark results; reading them side by side shows the shared evidential gap.
- [Ingest: Accelerating Scientific Research with Gemini in the Real-World](../../../../sources/accelerating-scientific-research-gemini-real-world.ingest.md) -- **compares-with**: second frontier-lab research harness combining generation with execution checks; contrasts on what each retains between projects (Hyra: graded Books and skills; Co-Scientist: per-run evolutionary search).

## Bidirectional Candidates

- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) <-> source -- **is-evidence-for**: the theory note has no external source case; Hyra would give it a current frontier-lab example of a usefulness-to-power slide.

## Reverse-edge Candidates

- [Compounding is tested in later improvement, not by the accepting metric](../../../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source -- **evidenced-by** (theory side's own vocabulary, as used in its existing case list): the ingest's own Recommended Next Action; the note already keeps a bounded source-case list (HyperAgents, Agent Optimizers, Poetiq) that Hyra fits as a per-tool-accepting-metrics-only case.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → source -- evidence link under theory rules: Books' Observation / Verified / Convention grades are a deployed staged-authority scheme matching the note's rungs; currently the note cites no external deployed instance.
- [Git provenance requires contribution and dependency semantics](../../../../theory/git-provenance-requires-contribution-and-dependency-semantics.md) → source -- weak; this note already cites Agora for shared research memory, and Hyra's evidence-bearing completion reports (code versions, traces) are a non-Git provenance contrast. Author only if the note discusses external provenance records.
- [Ingest: Agora](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) and [Ingest: Hypothesis Evolution Protocol](../../../../sources/hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md) → source -- **compares-with**: the Hyra ingest links both; return links would make the three-instance staged-authority cluster (Extractable Value 2) traversable from either end.

## Off-authorisation Candidates

- [Review architecture](../../../../reference/review-architecture.md) -- Hyra's evidence-before-conclusion Review Worker ordering is a concrete variant for Commonplace's own review gates (Extractable Value 3), but only `see-also` is authorised to reference and the relation is a comparison on a named axis. Suggest rejecting for now; if the experiment is pursued, record it as a proposal rather than extending `compares-with` to reference.

## Raw Text Candidates

None

## Rejected Candidates

- [Make authority explicit](../../../../theory/agent-memory-requirements/make-authority-explicit.md) -- fits Books grades plus human approval, but redundant with the already-linked trace-extracted-memory and governing-writes notes.
- [Factory construction is not evidence of production-knowledge acquisition](../../../../theory/factory-construction-does-not-establish-knowledge-acquisition.md) -- about recursive software-factory constructors receiving their family definitions; the factory-learning link already covers Hyra's "class of tasks" framing.
- [Accumulation counts dependence through the retained result](../../../../theory/accumulation-counts-dependence-through-the-retained-result.md) -- definitional refinement; Hyra gives no dependence trace for it to bear on. The accumulation-without-compounding note is the useful entry point.
- [Topology, isolation, and verification form a causal chain](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) -- Hyra's hierarchy is described without isolation or failure data; keyword overlap only.
- [Ingest: AI scientists produce results without reasoning scientifically](../../../../sources/ai-scientists-results-without-scientific-reasoning.ingest.md) -- relevant axis (task success vs. visible hypothesis revision), but Hyra reports no reasoning traces to compare; would confuse more than help.
- [Ingest: Harness engineering for self-improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md) -- synthesis of harness-edit benchmarks; Hyra releases no harness and no edit loop over it.
- [Ingest: The Last AI Built by Humans](../../../../sources/last-ai-built-by-humans-recursive-self-improvement.ingest.md) -- plausible compares-with on RSI claims, but Poetiq is the closer vendor-account match; adding both would spray.
- PrimeScientist, Weco, alien-space-of-science, when-code-is-free, position-paper ingests -- research-automation topic overlap only; none shares a named axis with Hyra's tool-building, memory grading, or review design.
- [Autocontext review](../../../../agent-memory-systems/reviews/autocontext.md), [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md), [Exo](../../../../agentic-systems/reviews/exo.md) -- self-improving harnesses with inspectable code; Hyra gives only prose, so a comparison would be one-sided. Compound Engineering is already linked for the mechanism/claim split.
- Commonplace review reference docs -- "anchored" there means snapshot-anchored; no evidence-ordering mechanism to compare.

## Index Membership

None (sources are outside tag participating collections; `kb/sources/` has no curated topic index for auto-research).

## Synthesis Opportunities

Hyra (Books grades, policy), Agora (reproduction over an immutable graph) and HEP (tool-enforced evidence linkage) are three auto-research systems that grade shared research memory by reproduction or confirmation, matching the trace-extracted-memory rung model. Together they could support an evidence note on staged authority in auto-research memory, as the ingest's Extractable Value 2 already suggests. All three are design descriptions; none measures downstream effect.

## Maintenance Observations

- The ingest has no inbound links anywhere in the KB; its own Recommended Next Action (compounding note) is the obvious first inbound edge.
- `usefulness-autonomy-warrant-and-power-are-separate-dimensions` has no external source case in its footer, so vendor progress claims (Hyra, Poetiq) are not yet routed to it.

## Flags

- The ingest is already heavily connected (16 footer links). Adding all seven proposed outbound edges would push it toward a spray; the strongest additions are the usefulness/autonomy and computationally-directed notes, which address the ingest's central weakness (RSI claim, undeclared boundary) more directly than several existing links.
