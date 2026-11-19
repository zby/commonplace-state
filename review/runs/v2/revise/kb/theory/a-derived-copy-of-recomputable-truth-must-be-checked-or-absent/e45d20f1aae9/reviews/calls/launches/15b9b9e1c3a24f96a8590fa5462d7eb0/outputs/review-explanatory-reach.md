---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "that is why hand-maintained-and-trusted is *forbidden* rather than merely risky"
    reason: "The asymmetry alone (bounded versus unbounded downside) compares worst cases, not expected costs, so by itself it supports 'risky' as much as 'forbidden'. The prohibition becomes hard to vary only when combined with the later premise that a Level A check costs nearly nothing, so trusting an unchecked copy saves nothing. The note supplies both premises, but attributes the forbidding force to the asymmetry section. The mechanism is present but slightly mislocated."
    level: info
outcome: pass
---

# Review

The central claim has a constrained mechanism. Two premises carry it: (1) a false trusted copy suppresses the recomputation that would expose it, while an absent copy costs only a bounded recomputation; (2) where derivation is mechanical, verification drops to a deterministic, near-free check.

**Variation test.** Vary premise 2: if checking were judgment-priced (Level B), the conclusion changes, and the note itself says so. In that regime hand-maintained dependent artifacts are "unavoidable", and managed staleness governs. Vary premise 1: if a stale copy carried a signal, or did not suppress recomputation, the prohibition loses its ground. The conclusion therefore depends on the premises; it is not adaptive pattern-recording.

**Falsifiability.** The claim would be undercut by a domain where a mechanically recomputable copy cannot be cheaply checked, or where an unchecked trusted copy's expected cost is lower than both checking and omission. Preconditions 1–4 name where enforcement fails and route those cases out explicitly.

**Ad-hoc accommodation.** Precondition 4's clause, which treats a judgment-based derivation rule as "the forbidden state, just relocated", tightens the claim rather than shielding it. Precondition 3's exclusion of execution-produced values follows from the definition of recomputability, not from a counterexample patch.

Only one thin spot remains, recorded as INFO.
