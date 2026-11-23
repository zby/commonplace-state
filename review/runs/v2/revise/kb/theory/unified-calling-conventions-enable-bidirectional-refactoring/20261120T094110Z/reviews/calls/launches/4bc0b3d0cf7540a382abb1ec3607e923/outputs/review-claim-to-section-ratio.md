---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Both are callables with defined interfaces. The unified calling convention is what makes the type-theoretic view practical rather than just analogical."
    reason: "The typed-callables section is the thinnest section: beyond the concrete detail that `.agent` files pair frontmatter with a prompt, it mostly restates the mechanism section's point that both component kinds present one interface. It still carries a distinct (if small) claim, so it does not push the section count past the claim count."
    level: info
outcome: pass
---

# Review

The note's distinct non-obvious claims are:

1. A unified calling convention, implemented by name-based dispatch, makes the neural/symbolic boundary movable without changing call sites (intro and "The mechanism").
2. Without it, each codification step is a breaking change that pushes toward big-bang rewrites; with it, constraining and relaxing become incremental, and the reverse move to a prompt can serve as a cheap experiment ("Why this matters for constraining").
3. An imperative scheduler, unlike a graph DSL, lets boundary refactorings use ordinary code refactorings ("The scheduler layer").
4. The unified convention turns the typed-callables view from analogy into practice ("The connection to typed callables").

The body has five substantive sections (intro plus four headed sections) and an Open Questions section, which is a separate support unit carrying boundary conditions (scale, debugging, host language). Claim 1 spans the intro and the mechanism section, but the intro states the problem and the mechanism section supplies the inference step (name-based dispatch and late binding), so neither merely restates the other. Sections do not outnumber claims plus necessary support units. The typed-callables section is thin, as the info finding notes, but it is not a restatement of framing.
