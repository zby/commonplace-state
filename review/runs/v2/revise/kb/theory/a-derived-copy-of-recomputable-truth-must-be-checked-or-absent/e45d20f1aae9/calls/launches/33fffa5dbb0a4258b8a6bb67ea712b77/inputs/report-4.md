---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/synthesis
launch: dbaa88674d8b44549af6fd29074759cc
completed-at: '2026-11-16T22:23:59Z'
findings:
- scope: passage
  quotes:
  - Enforcement is the third class that lets both stand
  reason: 'The section''s role is hidden. The note carries a second claim that it
    never states as a claim: a checked copy beats omission (''Omission is the fallback,
    not the optimum''). This section is the only place that justifies that ranking.
    It is framed instead as an extension of another note''s arbitrary/situational
    taxonomy, so a reader sees a side excursion rather than the support for the ranking.
    A revision could reframe the section around why a checked copy is worth keeping
    rather than deleting, and reduce the third-class framing to one sentence or to
    the existing footer annotation.'
- scope: passage
  quotes:
  - Any use-shaped artifact depends on its sources
  - Machine-followable suffices; human visibility is not required once the validator
    carries the interrupt.
  reason: The regime-boundary argument is heavier than its job. The dense managed-staleness
    paragraph opens with a general taxonomy of derived and abstracted artifacts and
    their repair modes. Its job is to set up the contrast in which Level A checking
    turns enforce-or-omit into the rule. The point that lineage need only be machine-followable
    is then made twice, once in the regime section and again in precondition 2. A
    revision could cut the background down to the contrast the flip needs (judgment-priced
    review versus a free deterministic check) and state the machine-followable-lineage
    consequence in one place.
- scope: passage
  quotes:
  - It is the general form of "a cache must never be the only copy"
  reason: 'The closing generalization leaves the rule''s scope ambiguous, and the
    compression checks disagree about it: one says delete the sentence because the
    cache maxim is about losing the source, one says move it to the opening as the
    most memorable framing, and one says trim its trailing clause. Readers cannot
    tell whether the note endorses the analogy. A revision could either drop the sentence
    and end on the instances, or state the analogy beside the opening rule with its
    limit (here the source always exists; the question is trust, not loss).'
contract: report
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/synthesis/artifact/reviews/20856af8544a1fd177e62d74/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/synthesis/artifact/reviews/20856af8544a1fd177e62d74/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/synthesis/calls/launches/dbaa88674d8b44549af6fd29074759cc/outputs/review.md
raw-output-sha256: d979383e982ad4cb858614611045d56532ea4dcefd6248c1ce68b994909743b9
---

# Simplification synthesis: A derived copy of recomputable truth must be checked or absent

The core claim is prominent: the title, description and first paragraph all state the two-state rule. The four checks found mostly local redundancy. Local fixes are left to those findings: the asymmetry recap, the "not asserted at all" restatement, the packaging parenthetical in the `AGENTS.md.template` instance, and the amortization repeat in the tag-README instance. Three opportunities need authorial judgment beyond those cuts.

## Opportunities

### 1. Make the checked-over-absent ranking the explicit job of "What enforcement buys"

- Location: `## What enforcement buys`, from "Frontloading spares execution context" through "discovered mid-task"; read with the Consequences line "Omission is the fallback, not the optimum."
- Combines: branch-bloat (info finding on the third-class taxonomy extension); cross-cutting with the Consequences section.
- Preserve or decide: Decide whether the ranking (a checked copy dominates omission when recomputation sits on the hot path) is part of the note's claim or only a consequence. The title and opening assert only that both states are valid. If the ranking is part of the claim, the opening may need to say so. Also decide whether the third-class contribution to the fix-what-the-executor note should stay here, since the footer declares an `extends` edge for it, or move into that note. One possible resolution: open the section with "Of the two valid states, checked is better wherever recomputation is costly," then give the frontloading tension as the reason.

### 2. Compress the regime-boundary apparatus to the contrast it sets up

- Location: `## Where the rule applies: the deterministic end of derived knowledge` (both paragraphs), and precondition 2 in `## What "checked" requires — and its limits`.
- Combines: detail-overhang (info finding on the managed-staleness background); marginal-value-redundancy (warn on the repeated machine-followable lineage point); branch-bloat (body remark that the interrupt-placement point appears twice).
- Preserve or decide: Preserve the claim that hand-maintained dependent artifacts are unavoidable, not forbidden, when verification is judgment. This is what stops the rule from overreaching. Preserve the Level A/B gradient as the boundary and the three linked mechanisms (lineage, timestamps, holistic rework), at least as links. Decide where the machine-followable-lineage point lives: in the regime section as a consequence of the flip, or in precondition 2 as a requirement. Do not state it in both.

### 3. Settle the status of the cache-maxim generalization

- Location: the closing sentence of `## Instances across four surfaces`: "It is the general form of "a cache must never be the only copy" — applied not only to caches but to every derived copy of recomputable truth."
- Combines: branch-bloat (warn: delete, the analogy is wrong), core-claim-obscured (info: move it to the opening), marginal-value-redundancy (warn: trim the trailing clause).
- Preserve or decide: The checks point in incompatible directions, so this is a meaning choice, not a compression edit. The author must decide whether the note claims a real generalization of the cache maxim. The maxim guards against losing the source, while this note assumes the source survives and governs trust in the copy. If the analogy is kept, it needs that limit stated and probably belongs beside the opening rule. If it is not kept, the sentence goes and the instance list ends the section.
