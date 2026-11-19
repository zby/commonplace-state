---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "For dependent knowledge in general the KB runs"
    reason: "The title and opening state a general rule about any derived copy of recomputable truth, but the scope section defines the rule's boundary through this KB's own machinery (\"the KB runs managed staleness\", Level A/B of the KB's text testing pyramid). The section is readable as this KB's implementation of a general split between judgment-priced and mechanically priced verification, and the next paragraph states that general criterion (\"mechanical derivation makes verification Level A — deterministic, near-zero cost, binary\"). Framing the KB machinery explicitly as an illustration of that general split would remove the overcommitment."
    level: info
outcome: pass
---

# Review

Claimed generality: the title and description apply to any artifact carrying a copy of mechanically recomputable information. The opening lists heterogeneous examples (a tag-README mark, a memory system's compiled cue, an inlined contract list, a duplicated file), and they are explicitly framed as examples.

Commonplace-specific vocabulary in the body is mostly marked as illustration. The "Instances across four surfaces" section is labeled as instances, and the ADR and log references sit inside an explicit example of omission. The memory-systems material is cited as one instance, not as the frame. The one place where KB-local framing does structural work is the scope section, where the boundary is described as what "the KB runs" and as KB pyramid levels. The general criterion (deterministic, cheap, binary verification) is stated alongside, so the claim does not depend on the residue. It is recorded as INFO, and the gate passes.
