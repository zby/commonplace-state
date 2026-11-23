---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "It also requires the compatible set to be nonempty."
    reason: "Basis: supplied-commission.md, Must keep, places nonemptiness on the source side: \"Greco, Mousseau and Słowiński's necessary weak preference over a nonempty compatible family\", with strictness alone as \"our stricter convention\". supplied-source-1.md (Summary) also says the authors show \"how to locate conflicting judgments when no function fits\", so an empty compatible set already signals conflicting inputs to revise in the source method. The candidate lists nonemptiness under \"two choices beyond the source\". That misplaces the line between borrowed method and chosen definition, which the commission's Current direction asks the note to draw. Required change: Present strict preference as the one choice beyond the source. Attribute the nonempty-family requirement, and the treatment of an empty set as conflicting judgments, to the source method. Alternatively, say only that the note makes explicit a condition the source handles by locating conflicts."
    level: warn
  - scope: passage
    quotes:
      - "and each added judgment orders more pairs"
    reason: "Basis: supplied-source-1.md, Quotes, qualifies the effect: \"Every new pairwise comparison of reference alternatives, for which the dominance relation does not hold, is enriching the necessary relation\". A judgment already implied by the current compatible set removes no function and orders no new pair. Saying that each added judgment orders more pairs overstates the cited source. Required change: Weaken the clause to say that a new judgment can order more pairs, or that consistent judgments can only add necessary comparisons."
    level: warn
  - scope: passage
    quotes:
      - "Local checks showed one workload running faster without source edits"
    reason: "Basis: in the candidate's Python section, the checks are offered as observations, but the candidate removed their record (the start's table of commands, builds and timings). The authorized sources do not carry them, and the old note is not independent support. The candidate therefore asserts evidence that a reader cannot inspect. Required change: State these as the release differences the judgment weighs, for example \"3.11 can run existing code faster, adds `asyncio.TaskGroup` and `tomllib`, and removes `inspect.getargspec`\", without claiming unreported local checks. Alternatively, keep one bounded figure with its conditions."
    level: warn
  - scope: passage
    quotes:
      - "extends: this note proposes one working definition meeting the requirements that note sets out"
    reason: "Basis: supplied-source-2.md sets requirements under \"What a usable definition of improvement needs\". They include separating working as designed or uptake from better work, and keeping three distinct judgments: reasoned forecast, expected-value calculation and observed outcome. The candidate addresses neither, and the commission asks only for \"one operational answer to the companion's question\". The context phrase claims more than the note delivers. Required change: Change the phrase to say that the note proposes one working definition answering the companion's question, or name only the requirements it meets: indexing to the alternative, fixing the definition for a test, and clear wins without forced closure."
    level: warn
  - scope: passage
    quotes:
      - "contrasts: why selection needs only a comparison among candidates at hand; this note supplies one such comparison"
    reason: "Basis: in supplied-collection-contract.md, `contrasts` is for \"the neighbouring-shape distinction\". The context phrase instead describes supply: this note provides a comparison the other note requires. The other note's footer calls this note its `mechanism` (supplied-source-3.md). Label and phrase disagree. Required change: Use a label that matches the stated relation, such as `extends`. Otherwise, rewrite the phrase to name an actual contrast between the two shapes."
    level: warn
  - scope: document
    quotes: []
    reason: "Basis: supplied-inbound.md, `kb/sources/making-reflective-equilibrium-precise.ingest.md`, cites the note for a weighted-average property: \"every weighted average of those settings selects that same set\". The start supplied it as \"So does any weighted average of them, so nobody has to say how the measures would be combined.\" The candidate drops that sentence. The candidate report's final paragraph says that the remaining inbound uses are still supported and names only the Greco, Mustajoki and Angilella ingests for the break-even case. It neither identifies this lost use nor lists the ingest as supported. Required change: Add the making-reflective-equilibrium ingest to the report's affected citations, recording that the weighted-average claim it parallels is no longer in the note. The note itself needs no change for this."
    level: warn
  - scope: document
    quotes: []
    reason: "The candidate meets the commission's must-keep items. It opens with the 90/10 break-even case under explicit frequency and additivity assumptions and works below, at and across nine. It keeps the `What a claim of improvement asserts` anchor. It fixes alternative, work, parties and horizon, and requires compatibility to be argued independently of the verdict. It fixes the definition per test and separates missing evidence from trade-off disagreement. It treats an open comparison as a permissible decision. The Python and Commonplace-objective sections are short and keep their anchors. It contains no LLM claim, survey or research agenda, and does not present the source as validating a purpose. All three Greco quotations match the ingest's Quotes section verbatim. Apart from the omission recorded above, the report's affected-citation entries match the inbound passages."
    level: info
outcome: warn
---

# Review

## Judgment

The candidate makes the commissioned contribution and can be published. It is short and self-contained, and it does what the commission's Current direction asks. It leads with the break-even question and uses that question to show that the same task counts yield different verdicts as the admissible ratio set changes. It then separates the borrowed relation, the chosen definition and the example's assumptions. The verdict list is exhaustive: improvement, weakly better or worse, tie, loss and open. The open case keeps the commission's distinction between missing evidence and contested trade-offs. The reserved decisions are respected: the title, path and anchors are unchanged, and the candidate introduces no cross-file commitments.

The warnings concern accuracy, not structure:

- **Source line.** The note says nonemptiness goes beyond the source. The commission and the ingest put that condition, or its handling as a conflict to locate, on the source side.
- **Overstatement.** The clause "each added judgment orders more pairs" claims more than the abstract's qualified wording supports.
- **Python evidence.** The Python section still cites "local checks" whose record the rewrite removed. Restating these as release differences costs nothing.
- **Footer relations.** One footer phrase says the note meets all of the companion's requirements, though the note addresses only some. Another link's label (`contrasts`) does not match its phrase.

## Affected citations

The writer's report identifies the displaced uses accurately: the routing-line example (Baudrit), the claim that known requirements need not be weighed afresh (SEP), the closing sentence about weighing (Fishkin), and the surviving instruction-revision and reversal-rule uses. It misses one lost use: the making-reflective-equilibrium ingest's parallel to the dropped claim that weighted averages of compatible measures preserve the verdict. Under the criterion, this lost use needs to be reported, but the note does not need to restore the claim. The deployment article's "routing-line example above" refers to the article's own text, as the report says.
