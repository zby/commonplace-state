---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
findings:
- scope: passage
  quotes:
  - and holding model weights fixed does not put the comparison out of reach
  reason: The linked note argues that, in an LLM-based application, the deployed system
    rather than the model is the unit of learning and evaluation. The note transfers
    this to a software factory, a Greenfield-lineage production environment that need
    not be LLM-based, without stating the transfer. The transfer is plausible because
    the list of machinery (prompts, natural-language artifacts, evaluators) implies
    an LLM-operated factory. It is not load-bearing for the central claim.
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/8fbe2ef1152c92cfc534784a/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/8fbe2ef1152c92cfc534784a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-grounding-alignment.md
raw-output-sha256: 2b5561d7b8c15407ed17d9fe7e8950ac00b2ae6c984f3944b182eb0244d46faf
---

# Review

Each linked library artifact was checked for representation: its title and opening, plus the interior passage the note invokes where that was relevant.

- **Factory learning is experience-responsive retention that improves the factory.** The note's opening restates the target's definitions of experience-responsive retention and factory-level learning at the target's scope. The target makes improvement a separate condition on retention, which supports the note's point that retention carries no quality requirement.
- **Self-improvement is relative to a declared objective.** The target defines antecedence as independent specifiability and says it is "a condition on identifiability, not on retention". The note represents this accurately. It says it *adds* prior declaration to the linked requirement of independent specifiability, and it states what independent specifiability blocks (objectives fitted to the result). The note does not claim that the target requires temporal prior declaration.
- **A repeatable operative path keeps a redesign class open to revision.** The target says repeatability requires the causal functions to remain applicable after the transition, and that writability marks only the outer envelope. This matches "a revision path that remains applicable after the transition, not merely editable files."
- **An experiment identifies only the contrast it actually runs.** The note uses it to require a with/without comparison of the retained instruction. That is the target's claim, used at its scope.
- **The deployed system, not the model alone, is the unit of learning.** This supports the claim that non-model machinery can be the locus of improvement. The transfer from an LLM application to a software factory is unstated (INFO).
- **Operative change**, **software factory** and **factory development** definitions. They are used in their defined senses: installed with a behavioral-authority path rather than merely stored; a family-specific production environment; revision of reusable family-level machinery.
- **Revising an improvement objective…** This is an adjacent "extends" link and makes no support claim.

No linked artifact is cited as grounding a broader mechanism or wider scope than it states.
