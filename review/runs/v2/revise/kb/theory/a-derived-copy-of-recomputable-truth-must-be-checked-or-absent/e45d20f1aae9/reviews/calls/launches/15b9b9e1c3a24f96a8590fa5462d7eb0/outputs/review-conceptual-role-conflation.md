---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the general source-of-truth requirement, stated for memory systems in"
    reason: "Conflates a source account with an object of application. The bullet sits in a list of 'Four surfaces in the system' that 'instantiate the rule', but its content is a prior requirement stated in another note for memory systems in general, not an identified surface in this system. Reading A: Commonplace has compiled cues where the rule is stated but unenforced, so this is instance evidence. Reading B: the linked note is an antecedent account that this note generalizes (as the footer's 'extends: generalizes its compiled-view source-of-truth rules' suggests), so it is inherited theory, not an instance. The choice changes what the note claims to inherit versus contribute and whether the bullet counts toward 'The spread is what shows it generalizes'. The author must decide whether this is an instance surface or a prior account."
    level: warn
  - scope: passage
    quotes:
      - "It is the general form of"
    reason: "The unattributed maxim 'a cache must never be the only copy' is presented as the special case this note generalizes. The relation is unclear: the maxim concerns durability (a cache needs a backing store), while this note concerns consistency checking. It is unclear whether the note inherits the maxim's concept or only borrows its phrasing. The sentence is a closing remark rather than load-bearing, so this is INFO."
    level: info
outcome: warn
---

# Review

Most role assignments in the note are explicit. It applies the text-testing pyramid's Level A/B distinction to its own regime boundary. It names the tag-readme `complete` mark as a shipped object of application, with the contract in the type spec. It positions itself against the frontloading and determinability notes as adding a third class. Its relation to the managed-staleness notes ("specializes", "contrasts") is stated in context.

The one material blur is in the instances list. The list is framed as surfaces in the system in four states of application. Its second bullet instead points to another note's general requirement for memory systems. A reader cannot tell whether the bullet is evidence that the rule already has a stated-but-unenforced instance here, or a predecessor theory the note extends. The footer leans toward the latter. The list's claim that the spread shows generality leans toward the former.
