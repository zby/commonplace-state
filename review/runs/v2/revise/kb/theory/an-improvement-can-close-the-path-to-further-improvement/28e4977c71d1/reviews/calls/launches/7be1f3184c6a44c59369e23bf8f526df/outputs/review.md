---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The speed gain can be real. The lost revision capability can also be real. There is no contradiction: the comparison checked task performance, while the change removed a different capability."
    reason: "This paragraph repeats the opening paragraph's point that the two outcomes are compatible because checking the current gain does not check the revision mechanism. The example has already made the case concrete, so the recap adds no new contrast. Cut it, or reduce it to one clause attached to the example's last sentence."
    level: warn
  - scope: passage
    quotes:
      - "Preserving the path is therefore a consequence of non-regression only under an additional condition: the revision capability must be included in what is checked."
    reason: "This sentence restates the preceding paragraph: non-regression protects only what is in its checked scope, and it protects the revision path when that scope includes it. The following sentence is the useful part, because it says that production-only non-regression leaves the path out. Fold that sentence into the previous paragraph and drop the restatement."
    level: warn
  - scope: passage
    quotes:
      - "Closing one path does not establish loss of the capability if another applicable path remains."
    reason: "The body already makes this point twice: a successor fails only if it 'destroys the only applicable revision path', and 'The required function need not stay in its original component.' The scope bullet adds no new boundary case and can be cut."
    level: warn
  - scope: passage
    quotes:
      - "A maintainer may restore a path that the agent itself no longer has."
    reason: "This partly repeats the earlier maintainer-editable-files paragraph. Its framing in terms of the declared system boundary may still help prevent misapplication. I am unsure whether that is enough to justify keeping it as a separate bullet."
    level: info
outcome: warn
---

# Review

## Summary

The note is short and its main parts do real work. The hypothetical agent makes the failure concrete. The non-regression section states the condition under which the failure is prevented. The section on remaining able to improve separates preservation from actual later improvement. The first Scope bullet, about fixed deployments that deliberately give up self-revision, adds a boundary the body does not otherwise state.

The redundancy is local. Three chunks restate a point that an adjacent or earlier passage has already made. The first is the "no contradiction" paragraph after the example. The second is the "therefore ... only under an additional condition" sentence, which repeats the scope rule it follows. The third is the Scope bullet about another applicable path, which the body already covers. Cutting or folding these would shorten the note without removing anything the reader needs.

The sentence "That note supplies the detailed test; this note explains why a successful improvement comparison can miss its failure" was considered and is not flagged. It tells the reader where the detailed test lives, which the earlier link alone does not.
