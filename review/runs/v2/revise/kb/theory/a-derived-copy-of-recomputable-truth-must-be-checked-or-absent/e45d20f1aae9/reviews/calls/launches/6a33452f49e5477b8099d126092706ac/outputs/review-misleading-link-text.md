---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the two-copy layout is designed in"
      - "source-of-truth for the byte-identical"
    reason: "The body and footer present ADR 027 as the design source for a two-copy, byte-identical AGENTS.md.template layout. ADR 027 does not mention AGENTS.md.template or byte-identical copies. It replaces scaffold symlinks with Hatch force-include mappings plus source-checkout fallback, and says editable checkouts read canonical files directly, 'preserving the no-duplicated-scaffold invariant'; the only real files it keeps under src/commonplace/_data/templates/ are COLLECTION.md templates. A reader following the link finds a decision against duplication, not a design for it."
    level: warn
  - scope: passage
    quotes:
      - "LLM recompute cost inverts the store-vs-recompute default"
    reason: "The footer link text says LLM recompute cost inverts the default. The target is now titled 'LLM recompute cost shifts the store-vs-recompute balance' and says expensive model-side derivation 'does not by itself justify persistence', comparing three paths. A reader who does not follow the link takes away a stronger claim than the target makes."
    level: warn
  - scope: passage
    quotes:
      - "holistic rework rather than patching"
    reason: "The link text presents holistic rework as the general fix for stale dependent artifacts. The target is a conditional claim about whole-picture narratives replacing fragment reconciliation when that reconciliation is infeasible within effective context; it treats rework of a dependent narrative but not patching versus rework for dependent artifacts in general. Related but narrower than the link text implies."
    level: info
outcome: warn
---

# Review

Checked every link, counting repeated targets once: the tag-readme spec, indexes-lower-recall, the lineage note (titled 'Source changes should surface downstream review targets...'), make-like staleness detection, evolving-understanding, the text testing framework, frontloading, fix-what-the-executor-can't-determine, the lineage definition, keep-compiled-views-aligned, ADR 025, ADR 027, the boundary of automation, LLM recompute cost, history-has-one-chance, the enforced tag-README note, and local materialization. All resolved. Most link texts match their targets' heads; the enforced tag-README footer text differs slightly from the current title but carries the same concept.

The ADR 027 links misattribute a two-copy design to a decision that states a no-duplication invariant. The LLM recompute footer text overstates its target's now-hedged claim.
