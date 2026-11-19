---
description: "A successor can improve a declared production dimension while disabling the machinery that would produce another revision; such a successor fails a non-regression requirement only when the revision capability is included in the checked scope"
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: []
---

# An improvement can close the path to further improvement

> Supplement to the preserved-capability consequence of [the better-factory comparison](./a-better-factory-claim-compares-operative-states.md).

A system can improve at its current work while losing the ability to improve itself again. These outcomes are compatible when the change improves production but disables a mechanism needed to select or install later revisions. When current production does not exercise the revision mechanism, checking the current gain does not check that the mechanism survives.

## A change can improve production while disabling the revision mechanism

Consider a hypothetical agent whose workflow tests proposed instruction changes and installs the successful ones. It installs a faster configuration that removes the revision workflow and permits only ordinary task execution. The agent now completes the declared task set faster, but no longer has a route for testing and installing another instruction change.

The speed gain can be real. The lost revision capability can also be real. There is no contradiction: the comparison checked task performance, while the change removed a different capability.

The files might remain editable by a maintainer. That does not show that the agent's revision workflow survived. The relevant question is whether evidence can still lead to a proposed change, an adoption decision, installation and later use. A [repeatable operative path](./a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) keeps those functions available after the transition for the same kind of revision. That note supplies the detailed test; this note explains why a successful improvement comparison can miss its failure.

## When closing the revision path fails non-regression

A non-regression requirement protects only the capabilities included in its checked scope. If that scope includes the ability to carry another revision through to use, a successor that destroys the only applicable revision path fails the requirement even if its production performance improves.

A successor that closes the path therefore fails non-regression only under an additional condition: the revision capability must be included in what is checked. Merely declaring non-regression on ordinary production tasks does not include it.

The required function need not stay in its original component. A successor can replace its revision workflow and preserve the capability, provided the replacement can carry another revision through to use. Conversely, keeping the old files does not preserve the capability if the successor no longer permits or consumes their changes.

## Remaining able to improve is not improving again

Preserving the path leaves another improvement possible; it does not establish that another improvement will occur. The system may propose no useful change, or its evaluator may repeatedly select harmful ones.

Nor does preservation establish that the retained change helps produce later improvements. That contribution is [tested in later improvement episodes](./compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), rather than inferred from the comparison that accepted the earlier change.

## Scope

- A fixed deployment can deliberately give up self-revision. The point is not that every system must preserve it, but that a production gain alone does not establish its preservation.
- The loss is relative to the declared system boundary and kind of revision. A maintainer may restore a path that the agent itself no longer has.
- Closing one path does not establish loss of the capability if another applicable path remains.
