---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance."
    reason: "Body composability and the placement test. This section records what Commonplace selected as its improvement objective and why. It does not illustrate or test the general claim. Under the contract, a record of a Commonplace selection belongs in kb/reference/. Explicitly scoped local material may stay in a theory note only as origin, illustration or test. The section is scoped honestly ('a practical commitment about the work we value'). Even so, it forms a second cluster: a note that cites this one as a premise for the general claim would also import Commonplace's declared objective. Split the declaration into a reference artifact and link to it, or recast the section as an application of the general claim."
    level: warn
  - scope: passage
    quotes:
      - "Four checks on local CPython 3.10.16 and 3.11.11 builds illustrate what enters the judgment."
    reason: "The Python checks and the random.py diagnostic comparison report concrete measurements (median timings, version-specific behaviour), but the note links no retained record of them. They act as illustrations rather than corroboration, so the contract does not require an evidenced-by edge. A link to a retained report, if one exists, would let readers inspect the runs instead of relying on the summary."
    level: info
  - scope: document
    quotes: []
    reason: "The description frames the note as how-to guidance ('How to decide whether to keep a change ...'), and parts of the body give imperative steps ('First ask what improved ...'). The body still argues why on-balance judgments work and where they fail: the alternative, the affected parties, the time period, and reversal-sensitive investigation. That keeps the note within theory and stops it from being a procedure that belongs in kb/instructions/. If the decision steps grow into an ordered procedure, they should move there."
    level: info
outcome: warn
---

# Review

The note belongs in `kb/theory/`, and it mostly follows the collection's conventions. Once its named system choices are scoped, a substantive claim about the design space remains. That claim is that comparative, on-balance reasons can justify keeping a change without a global score. It also says when to investigate an unknown: when a plausible answer could reverse the choice. The Python and library cases come from domains outside KB design, which counts toward explanatory-reach. The note marks its boundaries in prose: a binding requirement overrides an on-balance judgment, a preference does not assign credit to a component, and the partial order does not do the weighing.

Outbound links follow the contract. Inline links use connectives such as "By contrast" and "Nor does … identify". The single footer edge (`grounds`) points to a theory note and carries a context phrase. The note does not present the tag-coverage trace as corroboration of its claim; it uses the trace only to show a local gain. No sources are cited, so the grounding bound is not engaged.

The unmet convention is body composability. The section "What Commonplace chooses to count" records Commonplace's own selection of an improvement objective, and that selection is part of the note's contribution. A selection like this belongs in `kb/reference/`. Keeping it here means that anyone citing the general claim also imports the local commitment. The rest of the Commonplace material is acceptable: the `AGENTS.md` line and the validator are explicitly scoped illustrations of the general rule.
