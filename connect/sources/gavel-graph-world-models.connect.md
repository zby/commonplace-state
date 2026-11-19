---
description: "GAVEL connects model-derived repair to symbolic separation, residual semantic work and the boundary between a correct model rollout and physical feasibility."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/gavel-graph-world-models.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: GAVEL

**Source:** [GAVEL snapshot](../../../../sources/.snapshots/gavel-graph-world-models.md)

## Discovery Trace

Read the complete 1,028-line paper. Reused batch collection contracts, curated heads and complete title surfaces across all five destinations. No source tags. Notes description search for codification, repair, verification, formal models and specification identified symbolic separation, preferential codification and typed verification. Read all three fully; followed the exact-implementation and oracle-domain links already read in this batch. Retained the first two and the exact-implementation boundary; typed classification adds no distinct reader need here.

Focused body searches for GAVEL, graph world model, modeled preconditions, model-derived repair and symbolic planning covered reference, agent-memory-systems, agentic-systems and sources. Reference and agentic-systems yielded no precise target. AriGraph's table/review description identified a learned graph memory, but storage similarity does not establish a repair-mechanism comparison; no edge proposed. Sources returned Meta-AQUA's planning over learning operators and ToolGate's admissibility filter. These share broad symbolic constraints, but the directly relevant notes already express the useful relationship. No external search. Instructions and work excluded.

## Connections Found

- [Scheduler–LLM separation](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — **compares-with**: the symbolic action model repairs consequences it can derive and returns unresolved failures to the LLM. Repair without another LLM call outperforms feedback-only replanning for the smaller planner and approximately matches it for the larger one; combined repair and feedback performs best in the paper's tests. This is a bounded intervention on error handling, not a proof of the note's full theory.
- [Preferential codification](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — **compares-with**: routing model-derived corrections to symbolic repair leaves failures outside those repair rules for model interpretation. It illustrates a supplied selection mechanism, not autonomous discovery of the rules or a measurement showing every residual case is less predictable than every removed case.
- [Exact implementation and requirement warrant](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **compares-with**: rollout validates plans relative to supplied preconditions, effects, goals and restoration constraints. Those rules omit manipulation geometry and do not repair incorrect extraction of the instruction's objects. Passing modeled execution therefore does not establish physical feasibility or faithfulness to the user's intended goal.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Scheduler–LLM separation](../../../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) → eventual tracked ingest — **evidenced-by**: a paper-reported comparison of direct symbolic repair with feedback-only replanning, preserving the shared pipeline, modeled action space and smaller-versus-larger planner distinction.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Shared graph storage proves a connection to every graph-memory system: the intervention is model-derived repair and belief-aware scheduling.
- Belief updating demonstrates cross-task learning of the world model: location beliefs change during execution, but action semantics and the trained room prior remain fixed.
- Stronger models remove the need for checking: the tested hosted models retain large gaps between unassisted and checked planning, but the result remains confined to this benchmark.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

The benchmark uses a lightweight symbolic executor with geometric navigation, not manipulation-level collision/reachability checks. The paper reports agreement with OmniGibson on all 100 single-task instructions, not an independent physical-robot trial or full multi-task validation. Baselines reproduce relevant mechanisms within the same pipeline rather than running original systems unchanged. Five-seed means and standard deviations are reported. Multi-task instructions contain two to five independent tasks over disjoint object sets; ordering is enumerated exactly over an approximate pairwise cost model, not a globally optimal policy for arbitrary dependent tasks. The 5.4% travel reduction combines distributional beliefs and online reordering versus MAP fixed ordering; online reordering alone reduces 79.69 to 78.01 meters. Location updates are in-run state, not evidence of continuing adaptation of action rules or the semantic prior. Object extraction accounts for many residual failures. Implementation not inspected for this source-only connection pass.
