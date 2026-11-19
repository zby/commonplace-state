---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a cache must never be the only copy"
    reason: "The note presents itself as the general form of a software-caching maxim without stating the shared mechanism. That maxim mainly concerns durability (the source must survive), while this note's rule concerns consistency (a retained copy must be verified against a surviving source). The relation is plausible, because both keep the source authoritative and the copy disposable, but the bridge is left implicit. It is a framing remark, not evidence the argument depends on."
    level: info
outcome: pass
---

# Review

The note cites no external studies or empirical results. Its evidence is internal to agent-operated KB and software-artifact maintenance: the shipped `complete`-mark validator, ADR 025, ADR 027, a logged skill edit and linked theory notes. These share the note's argument domain.

The memory-systems source (keep-compiled-views-aligned) is the closest domain shift. The note bridges it by stating the shared mechanism: a derived surface without provenance, regeneration rules and staleness detection becomes an independent authority. The closing appeal to "a cache must never be the only copy" imports a caching maxim without naming the shared mechanism. Because it serves as framing rather than support, it is recorded as INFO, and the gate passes.
