purpose: "An agent or maintainer who designs or approves self-revising KB and agent workflows should notice that a check of a production gain does not show that the revision path survives, and know what a non-regression check must cover before it counts against losing that path."
must-keep:
  - "A system can improve at its current work while losing the ability to improve itself again."
  - "A non-regression requirement protects only the capabilities included in its checked scope."
  - "Merely declaring non-regression on ordinary production tasks does not include it."
  - "Keeping the old files does not preserve the capability if the successor no longer permits or consumes their changes."
  - "Preserving the path leaves another improvement possible; it does not establish that another improvement will occur."
  - "A fixed deployment can deliberately give up self-revision; a production gain alone does not establish its preservation."
passes:
  - pass: narrow-overclaims
    scope: "The description's 'non-regression prevents this'; the heading 'When non-regression protects the revision path' and the sentence 'Preserving the path is therefore a consequence of non-regression only under an additional condition' (narrow to the supported claim that a path-closing successor fails a correctly scoped requirement); 'the ability to revise the system's improvement machinery' (narrow to the first-order ability to carry another revision through to use, the capability the example loses); the opening sentence 'Checking the current gain does not check that the revision mechanism survives' (add the condition that production does not exercise the revision mechanism); the heading 'A gain can consume the mechanism that produced it' (drop the causal coupling, e.g. 'disable')."
  - pass: readability-and-flow
    scope: "Cut or fold the 'no contradiction' recap paragraph, any residue of the narrowed 'therefore' sentence, and the Scope bullet on another applicable path. State the files-versus-capability boundary once, keeping its three meanings (surviving files do not show surviving capability; a replacement can preserve it; loss is relative to the declared system boundary) and the handoff to the repeatable-operative-path note. Let the opening carry the checked-scope condition in conditional form. In the opening, replace 'select or install later revisions' with the full path through to use. Name the referent of 'its failure'."
stop: null
