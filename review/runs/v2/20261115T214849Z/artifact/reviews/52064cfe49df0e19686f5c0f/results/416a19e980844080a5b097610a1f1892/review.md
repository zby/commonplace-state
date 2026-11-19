---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - In that regime the hand-maintained dependent artifact is not forbidden; it is
    unavoidable
  - And the interrupt-placement problem dissolves
  reason: 'The scoping section ''Where the rule applies'' is the densest part of the
    note and leans on related-note machinery (managed staleness, make-like timestamps,
    holistic rework, Level A/B checks, interrupt placement). It supports the claim,
    since it explains why enforce-or-omit holds only where checks are mechanical.
    But it is longer than the claim it scopes, and its second paragraph introduces
    terms (detector plus judge, interrupt placement) that the reader must decode before
    returning to the rule. A shorter version would protect the claim: one sentence
    saying that judgment-checked dependents stay under managed staleness, and one
    saying that a Level A check flips the regime. The rest could be cut or left to
    the linked notes.'
  level: info
- scope: passage
  quotes:
  - a compiled cue (a memory system's derived retrieval hint)
  reason: The opening sentence lists four example kinds, two with parenthetical glosses,
    before the paragraph states the rule ('Such a copy has exactly two valid states').
    The title and description already carry the claim, so the claim is still findable.
    Moving the two-states sentence first, or shortening the example list, would make
    the opening paragraph lead with the rule rather than with examples.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 8f6c7399d2a1a0ddbec3351010b3cc1896bd530cb07a00e111e441ba2f55f050
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/52064cfe49df0e19686f5c0f/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/52064cfe49df0e19686f5c0f/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T214849Z
launch: 416a19e980844080a5b097610a1f1892
completed-at: '2026-11-15T21:49:23Z'
raw-output: kb/reports/state/review/runs/v2/20261115T214849Z/calls/launches/416a19e980844080a5b097610a1f1892/outputs/review.md
raw-output-sha256: 164920ee77a381664833ea98ab2ae3c5d39d37388d4ee02adcdc78b2b301bf6a
format: 2
---

# Review

## Core claim

In one sentence: a copy of information that can be mechanically recomputed from a ground-truth source must either be checked by a validator against that source or not exist, because a hand-maintained copy that consumers trust can make them silently and unboundedly wrong.

## Assessment

The claim is easy to find. The title states it as a claim. The description repeats it. The first paragraph ends by stating it plainly: "Such a copy has exactly two valid states," and "There is no safe middle." The next section gives the asymmetry that justifies the word *forbidden*, which makes the claim easy to remember. The later sections each serve the rule. "What enforcement buys" gives the reason to prefer checking over omitting. The precondition list says when checking is possible. The consequences and the four instances apply the rule. None of them competes with it.

The two findings are INFO-level shape issues. Neither hides the claim:

- **The scoping section is heavy.** "Where the rule applies" carries the most apparatus in the note, and much of that apparatus comes from neighbouring notes. Compressing it to the regime flip would make the claim more memorable: judgment-checked dependents are managed for staleness, while mechanically checkable copies follow enforce-or-omit.
- **The opening leads with examples.** The first paragraph lists examples before it states the rule. The title and description offset this, but starting the paragraph with the two-states sentence would make the claim more prominent.

No WARN applies. The core claim does not need to be moved, restated or protected: it already appears early and plainly, and the later material is organized around it.
