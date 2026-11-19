---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 6a33452f49e5477b8099d126092706ac
completed-at: '2026-11-16T22:21:23Z'
findings:
- scope: passage
  quotes:
  - the two-copy layout is designed in
  - source-of-truth for the byte-identical
  reason: The body and footer present ADR 027 as the design source for a two-copy,
    byte-identical AGENTS.md.template layout. ADR 027 does not mention AGENTS.md.template
    or byte-identical copies. It replaces scaffold symlinks with Hatch force-include
    mappings plus source-checkout fallback, and says editable checkouts read canonical
    files directly, 'preserving the no-duplicated-scaffold invariant'; the only real
    files it keeps under src/commonplace/_data/templates/ are COLLECTION.md templates.
    A reader following the link finds a decision against duplication, not a design
    for it.
  level: warn
- scope: passage
  quotes:
  - LLM recompute cost inverts the store-vs-recompute default
  reason: The footer link text says LLM recompute cost inverts the default. The target
    is now titled 'LLM recompute cost shifts the store-vs-recompute balance' and says
    expensive model-side derivation 'does not by itself justify persistence', comparing
    three paths. A reader who does not follow the link takes away a stronger claim
    than the target makes.
  level: warn
- scope: passage
  quotes:
  - holistic rework rather than patching
  reason: The link text presents holistic rework as the general fix for stale dependent
    artifacts. The target is a conditional claim about whole-picture narratives replacing
    fragment reconciliation when that reconciliation is infeasible within effective
    context; it treats rework of a dependent narrative but not patching versus rework
    for dependent artifacts in general. Related but narrower than the link text implies.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/c2e8b4875271072526ae218a/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/c2e8b4875271072526ae218a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-misleading-link-text.md
raw-output-sha256: 04a5a81c189c088499aa21b8344152b93b258e1ee8c9742518f0402e29db3374
---

# Review

Checked every link, counting repeated targets once: the tag-readme spec, indexes-lower-recall, the lineage note (titled 'Source changes should surface downstream review targets...'), make-like staleness detection, evolving-understanding, the text testing framework, frontloading, fix-what-the-executor-can't-determine, the lineage definition, keep-compiled-views-aligned, ADR 025, ADR 027, the boundary of automation, LLM recompute cost, history-has-one-chance, the enforced tag-README note, and local materialization. All resolved. Most link texts match their targets' heads; the enforced tag-README footer text differs slightly from the current title but carries the same concept.

The ADR 027 links misattribute a two-copy design to a decision that states a no-duplication invariant. The LLM recompute footer text overstates its target's now-hedged claim.
