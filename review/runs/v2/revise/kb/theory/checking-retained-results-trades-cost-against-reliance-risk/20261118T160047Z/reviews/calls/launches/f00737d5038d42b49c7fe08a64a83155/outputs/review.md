---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["An inexpensive, defined check on a claim that authorizes stopping makes enforcement attractive."]
    reason: "UNSUPPORTED — the note never shows that the membership check is inexpensive. It gives the rule's shape (one-hop reach over named inputs) and its timing (at validation, not per read), but no cost comparison against the saving or against the connect report's rerun. The mark's side of the trade-off rests on 'inexpensive' while the cost half of the claimed trade-off is not concretized for this example. The tag-readme type supports 'defined' and 'enforced'; nothing linked supports 'inexpensive'."
  - scope: passage
    quotes: ["Accepting some risk between checks can be right, provided it is an explicit choice rather than a hidden consequence of trusting the copy."]
    reason: "THIN — the 'provided' condition is added without a reason. The preceding paragraphs establish that check frequency trades cost against risk; they do not establish why an explicit choice changes whether the accepted risk is right, or what makes a choice explicit. The same risk taken implicitly or explicitly has the same reliance cost unless explicitness changes consumer behaviour, which the note does not argue."
  - scope: passage
    quotes: ["Reusing an earlier report can be reasonable when rerunning costs more than the risk accepted for the task."]
    reason: "THIN — the contrast that makes the two examples 'land differently' rests on the report's candidate-only contract lowering reliance risk, but the same paragraph concedes consumers may treat the report as the full set, and Scope says the contract is 'not evidence of how consumers behave'. Once that concession is made, the reason reuse is more acceptable than for the mark reduces to rerun cost and broad dependencies; the note does not consider a cheap staleness proxy (for example, any change in the searched scope since the pass) as the analogue of the mark's check, so 'rerunning costs more than the risk' compares cost against an unquantified, possibly unbounded risk."
  - scope: passage
    quotes: ["The mark's contract supplies the first three; nothing in it establishes the fourth."]
    reason: "THIN — condition 3, 'a source available at check time', is a runtime fact, not something a contract can supply. The note itself says the validator reads the participating collections 'when they are supplied', and the tag-readme type warns that validating one collection does not clear a head. The contract names the inputs (condition 2); whether they are present at check time is not established by it."
  - scope: passage
    quotes: ["The absence of a known change is evidence of freshness only if every relevant change reaches the checker."]
    reason: "THIN — 'only if every' overstates the inference. Partial change propagation still makes absence of a known change weak evidence of freshness; what complete propagation adds is strength, not the evidential status itself. The conclusion that 'assurance dates from the last check' holds, but the biconditional-sounding premise is stronger than needed and not argued."
  - scope: passage
    quotes: ["How often to check a retained result therefore depends on the cost of checking relative to the risk of relying on stale or wrong content."]
    reason: "HOLDS — the 'therefore' follows from the two preceding paragraphs: checking spends part of the saving, and reliance carries a conditional staleness and suppression risk. The step implicitly assumes a check reduces reliance risk, which is close enough to definitional to carry the conclusion at the qualitative level the Scope section declares."
outcome: report
---

# Friction check: Checking retained results trades cost against reliance risk

**Central claim (one sentence):** How often to check a retained derived result should be set by weighing the cost of checking against the risk of relying on a stale or wrong copy, with any accepted risk chosen explicitly.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent thing: a qualitative trade-off between check cost and reliance risk. Saving work by retaining, spending part of that saving on checks, and accepting bounded risk between checks can coexist; the note does not ask for a result that is both free to keep and guaranteed current. The two worked examples are positioned at different points on the trade-off rather than as conflicting requirements, and the Scope section disclaims calibration, so no hidden pair of incompatible properties appears.

## Thinnest joints

The weakest joints sit in the worked examples, not in the general trade-off. The general argument (saving, spending, risk, therefore frequency depends on both) holds at the qualitative level the note claims. The examples are where the trade-off has to be concretized, and there the cost side is asserted rather than shown: the mark's check is called inexpensive without comparison, and the connect report's reuse is justified against a risk the note admits it cannot bound once consumers ignore the candidate-only contract. The "explicit choice" proviso ranks next because it adds a normative condition the argument never earns. The condition-3 attribution and the freshness "only if" are local overstatements that do not carry the central claim. The headline "therefore" is listed last as the strongest joint.

## For the human

Look first at the mark section's "inexpensive" and the connect report's reuse condition: the note's claim that the two examples "land differently" needs the cost side of each concretized, not only their contracts.
