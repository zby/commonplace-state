---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/instructions/review-gates/prose/source-residue.md
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
note-sha256: d3d9adf1ba7b1c70b97b2bd22e2ef692e8175350cbb2e11508b20ce1f301f766
criterion: kb/instructions/review-gates/prose/source-residue.md
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T185423Z
launch: 462f0f1a1a4a405aaa1951ab52d412ee
completed-at: '2026-11-16T18:55:34Z'
findings:
- scope: passage
  quotes:
  - this research setting
  reason: 'The title and opening state a general conditional claim ("when no complete
    fixed oracle decides that fit"). The Scope bullet instead ties the oracle''s absence
    to "this research setting," which the note never names. The phrase looks left
    over from a narrower originating context. Either name the setting as an illustrative
    case or restate the bullet generally, for example: "The absence of a complete
    fixed oracle is an observed current condition, not a proof that no general evaluator
    can exist."'
  level: warn
- scope: passage
  quotes:
  - branch allocation
  reason: '"Branch allocation" comes from a specific search-process vocabulary (allocating
    effort across candidate branches). The note neither introduces nor generalizes
    it. In a general list of consequential work, it may leave readers unsure what
    is meant. A general term such as "allocation of search effort" would avoid this.'
  level: info
contract: verdict
target-sha256: d7f8b2e30991dde2e42cd781c27113ba0addbb537564efb19d764c8273204321
target-capture: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/0d3e91faa81fd92f64a7fcea/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T185423Z/artifact/reviews/0d3e91faa81fd92f64a7fcea/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261116T185423Z/calls/launches/462f0f1a1a4a405aaa1951ab52d412ee/outputs/review-source-residue.md
raw-output-sha256: 03a2d3468c223800c80699f6e2dc3c340d9778b9b367896746596feb6eb2f0da
---

# Review

The note's claimed generality is any working theory whose fit lacks a complete fixed oracle. Most of its vocabulary matches that generality: proposal, diagnosis, recovery, modification and transfer. Its concrete examples (architecture claims, decompositions, theories of failure) are marked as illustrations ("A claim about architecture may..."). The residue comes from two unframed traces of a narrower context. One is the unnamed "this research setting" in Scope, which narrows a premise without saying to what. The other is "branch allocation," a term from a particular search process. The first matters more because it changes how far the oracle-absence premise reaches.
