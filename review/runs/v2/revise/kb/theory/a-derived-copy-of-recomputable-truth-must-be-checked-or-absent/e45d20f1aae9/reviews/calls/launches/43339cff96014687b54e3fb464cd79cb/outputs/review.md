---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'It is the general form of "a cache must never be the only copy" — applied not only to caches but to every derived copy of recomputable truth.'
    reason: "The closing generalization imports a different principle. 'A cache must never be the only copy' guards against losing the source when a cache is evicted; this note assumes the source always exists and governs whether a copy may be trusted. The note does not argue for the analogy, the argument does not need it, and it gives readers an easy target. Delete the sentence; the instance list already ends the section."
    level: warn
  - scope: passage
    quotes:
      - 'Enforcement is the third class that lets both stand'
    reason: "The 'What enforcement buys' section adds a third class to another note's arbitrary/situational taxonomy. It earns a place by explaining why a checked copy beats omission, which the Consequences section relies on ('Omission is the fallback, not the optimum'). But the taxonomy extension mostly develops the linked fix-what-the-executor note rather than the checked-or-absent rule. Consider cutting it to the value point and leaving the third-class framing to that note or a link annotation. Where it should go is unclear, so this is informational."
    level: info
outcome: warn
---

# Review

The main claim: a copy of information that can be mechanically recomputed from a source must either be machine-checked against that source or not exist. Hand-maintained copies that consumers trust are forbidden. Most side material supports this claim in its current place:

- **The asymmetry section** is the premise that justifies forbidding the copy rather than calling it risky.
- **The regime-boundary section** is the boundary condition. It explains why hand-maintained dependent artifacts are acceptable where checking needs judgment, and why the rule applies only where the check is cheap and deterministic (Level A).
- **The four preconditions** set out what "checked" means. Precondition 4 answers the obvious objection that the validator is itself unchecked.
- **The instances** are the evidence for generality. The instance list states the application state of each case, so it does real work rather than just listing examples.

One branch needs action. The closing sentence claims the rule is the general form of "a cache must never be the only copy." That maxim is about losing data, not about trusting a stale copy. It adds an analogy the argument does not use, and the analogy is weak. Removing it costs nothing.

One branch is borderline. The section on what enforcement buys places "recomputable-and-checked" as a third class in a taxonomy from another note. Its value point supports the note's ranking of checked over absent. The taxonomy extension belongs more to the linked note, and the footer link already records it. Trimming it is optional.

A smaller point in the regime section, not flagged separately: the remark that "the interrupt-placement problem dissolves" also belongs to the lineage note. Precondition 2 repeats it. If one of them is cut, the argument does not change.
