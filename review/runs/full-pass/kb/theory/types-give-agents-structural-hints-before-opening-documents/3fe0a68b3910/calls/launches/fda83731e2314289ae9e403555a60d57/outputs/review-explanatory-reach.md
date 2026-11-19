### Summary

The central claim is that types give agents structural hints before they open documents. The note offers a mechanism. Agents start each session with no memory and have finite context, so the decision to load must be made from metadata. A type that asserts a structural property (not subject matter) tells the agent which operations the document affords, and the description discriminates among instances. The verifiability paragraph gives the mechanism some hard-to-vary content. Replace the structural type with a subject-matter label ("design note") and the conclusion fails, which the note itself shows. The claim is falsifiable: subject-matter types giving equally good routing, or types adding nothing beyond descriptions, would count against it. The mechanism for the type's own contribution, as distinct from the description's, is thinner.

### Findings

- INFO: Varying a premise the note uses: remove the type and keep the description. The note's own reasoning says the description does the instance-level filtering and calls it "the most important field". The note does not explain what routing decision the type changes once a discriminating description and title are present. The illustrations (`spec` → implement, `structured-claim` → extract argument) show the type selecting an operation. They do not show a case where the description alone would have led to the wrong load decision. So the type's half of the mechanism is plausible but not yet constrained enough to be hard to vary.
- INFO: The opening dichotomy ("load everything or guess") treats the type as necessary for informed routing. The final paragraph then makes the type's role partly indirect: the type system makes descriptions exist. That indirect route is a real mechanism, but it explains enforced descriptions rather than "structural hints". The note does not separate which of these two mechanisms the title claim rests on.
- INFO: No ad-hoc accommodation found. The note adds no escape-hatch qualifiers.

## Result: PASS
