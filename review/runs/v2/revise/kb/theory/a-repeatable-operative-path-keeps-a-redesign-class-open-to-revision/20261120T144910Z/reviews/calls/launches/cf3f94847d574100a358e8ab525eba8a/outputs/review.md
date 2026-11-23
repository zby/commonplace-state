---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["This episode satisfies the first five checks for a revision of verification machinery, but it does not demonstrate a further revision of the installed mark/schema/validator organization."]
    reason: "THIN — The class narrows from verification machinery to the installed mark, schema, and validator. The linked trace also records a later correction to the documented search recipe after the validator exposed a missed note. The inference depends on whether that recipe is inside the original class and, if it is, which of the first five checks the correction fails to demonstrate."
  - scope: passage
    quotes: ["The next maintainer cannot recover how the problem was diagnosed, which condition admitted the change, or what would carry a challenge to the successor. General human capability supplied the missing transition; the retained system did not."]
    reason: "UNSUPPORTED — The absence of a retained rationale for one patch establishes a gap in the episode record. It does not establish that existing review rules, repository conventions, or observable failures cannot supply a route for another change in the same class."
  - scope: passage
    quotes: ["Without representation, the path cannot formulate the redesign as a change to the system."]
    reason: "THIN — The argument establishes that some representation must let the process target the component. It does not establish that identifying its consumer, channel, and force is causally necessary. An update rule can locate and revise a code module through a stable interface without an explicit description of who consumes it or how its output governs behavior."
  - scope: passage
    quotes: ["Those transitions show that the installed successor remains operative and editable. They support a continuity argument for the named redesign classes, but do not by themselves show that determination, admission, and installation remain available after every successor transition"]
    reason: "THIN — Replay and subsequent use establish installation and dependence. Editability establishes that the successor can be patched. For a named class and one particular successor, the note does not show how evidence can produce another candidate, how that candidate can be admitted, or how it would become operative. The gap arises before any claim about every successor transition."
  - scope: passage
    quotes: ["This episode satisfies the first five checks for a revision of verification machinery"]
    reason: "THIN — The linked trace supplies the drafted change, the accepted ADR, implementation and later use. The note does not identify the admission condition or the decision that applied it. The existence of a committed ADR locates the accepted result but does not by itself identify how the candidate could displace the incumbent."
outcome: report
---

# Friction check: A repeatable operative path keeps a redesign class open to revision

**Central claim (one sentence):** A named redesign class remains open to revision when evidence can lead to an admitted and installed change that later operation uses, and the same causal functions remain available for another change in that class.

## Filter

**Filter:** SURVIVES

The properties that must coexist are an operative change and a route to another such change in the same class after installation. For example, a failing check can motivate a validator revision, review can admit it, and CI can run the installed successor. If the successor still emits evidence reviewers can use to revise the validator and the same route can install that revision, both properties hold.

## Thinnest joints

The class boundary comes first because it can change whether the note's most detailed case contains a second relevant episode. Next comes the inference from an undocumented decision to the absence of a repeatable route, followed by the distinction between what the system must represent to act and what a reviewer must know to verify the path. The two evidence findings have narrower consequences because their sources already establish concrete transitions, with particular checks left open.

## For the human

Define the redesign class for the tag-README trace before deciding whether the later search-recipe correction exercises the path again.
