---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "An artifact-side bound does not have that failure mode, because a conforming artifact fits by construction"
    reason: "Overclaims. The bound counts unquoted sources, a proxy for the grounding check's cost. Some of that cost stays off the page: representativeness of a quoted passage, the faithful representation of linked notes (which the unit excludes), inferential moves such as marking a transfer as a hypothesis, and noticing a source-attributed detail that has no quote. When a reviewer has to open sources or linked notes for these reasons, its limit binds again, and a pass from a reviewer that stopped looks the same as a pass from one that read everything. The note admits parts of this elsewhere ('Occurrence is not representativeness', the auditability paragraph, the first open question) but leaves this sentence unqualified. Scoping it, for example 'does not have that failure mode for the finding step the validator performs', would bring it into line with those admissions."
  - scope: passage
    quotes:
      - "and an absence of that kind is a validator's result rather than a reviewer's finding"
    reason: "As stated, this is false for the validator the note describes. The ADR 046 validator substring-matches quotations that exist. It cannot detect that a detail attributed to a source has no retained quote. Finding that absence is exactly what the uncapped reviewer did. The following counterfactual ('Had the details been quoted...') holds only if something forces the author to quote, and that is the unbuilt validator rule the Scope section declines to decide. Either name the missing rule (e.g. every source-attributed claim must carry a quote or a snapshot-required mark) as a premise, or restate the absence as a reviewer finding the bound would make cheaper."
  - scope: passage
    quotes:
      - "Read as a fact about notes, it says the reviewer honoured its cap and the notes had put their support beyond it"
    reason: "The rereading mixes units. The experiment's 'opened' counts were distinct linked artifacts, and those include linked notes. The note's unit is the unquoted source and explicitly excludes linked notes. Of the four findings, one ('broader mechanism attributed to a link that disclaims it') concerns a linked note's representation, which the source-count bound would never have forced to split or quote. Another ('two target-side transfers not marked as hypotheses') is an inference-labelling problem, not missing support. The note recruits only two of the four as support. It should state that the other two fall outside the proposed unit. Otherwise the experiment looks like stronger evidence for the artifact-side placement than it is."
  - scope: passage
    quotes:
      - "the bound is held by a validator that fails the note, not by a reviewer that stops reading"
    reason: "This contrast depends on a validator rule that the Scope section says the note does not decide ('Does not decide N, a validator rule that would enforce it'). The failure-mode comparison is therefore between a deployed review-side budget and a hypothetical artifact-side one. Say so, so that a reader does not take the comparison as one between two working mechanisms."
outcome: report
attack-outcome: partially lands
---

# Critique: A note is an atomic step relative to the check that reads it

**Note:** kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
**Central commitment:** A note's step size is relative to the check that reads it. For Commonplace's grounding check the unit is the unquoted source. Bounding that count on the artifact avoids the silent-failure mode of a review-side reading budget, because a conforming note fits the check by construction.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is the maintainer who holds the current review-side placement (ADR 079's sixteen-artifact budget), argued from measurement. Their case runs as follows.

The relativity claim and the two-bounds distinction are sound and not in dispute. The dispute is over the claim that matters operationally: that an artifact-side bound "does not have that failure mode". That claim does not survive. The bound counts unquoted sources. That count measures only the *finding* step the verbatim validator mechanizes. It does not measure the grounding check's actual cost. The remaining cost still needs off-page reading, and conformance does not shrink it:

1. **Representativeness.** A short verbatim passage can pass the substring validator while a qualifying sentence sits just outside it. The note says so itself: "a reader who suspects a passage was lifted out of a qualifying context has to open the source after all."
2. **Linked-note representation.** The unit excludes links to other notes on the grounds that each linked note discharges its own grounding. But the citing note still owes a faithful *representation*, and checking that means opening the linked note. In the paired experiment, one of the four uncapped-only findings was exactly this: "broader mechanism attributed to a link that disclaims it". No source-count bound would have touched it.
3. **Inference labelling.** Another of the four findings ("two target-side transfers not marked as hypotheses") was neither missing support nor a quote problem. It was a judgment about how the note frames its own inference.
4. **Absence detection.** The note says an absent retained passage "is a validator's result rather than a reviewer's finding." The validator it cites matches quotations that exist. It cannot report a quotation that should exist and doesn't. Noticing that absence was the uncapped reviewer's work.

So on a conforming note the reviewer's limit *can* still bind: whenever any of these four reasons sends the reviewer off the page. When it binds, the failure is just as silent as before. The artifact-side bound reduces how often the reviewer must leave the page. It does not remove the failure mode. Meanwhile the review-side budget, with consumption telemetry and sufficiency/budget disclosure, has a measured record: in the 68-note recertification, 37 of the 38 partial reads reported sufficiency, and the one budget stop named its unchecked routes. The opponent concludes that the note's own evidence supports both mechanisms as complements: the artifact bound cuts finding cost, and the review budget covers the residue. It does not support the artifact bound as a replacement free of the review budget's failure mode.

## How the note engages it

**Partially engaged.**

- *Representativeness* is answered directly in "Mechanism" ("Occurrence is not representativeness…") and in "What kind of number a step size is" ("the audit the bound buys is of the step the validator did not do, not of the one it cannot"). This part of the attack is already conceded and priced.
- *Linked-note representation* is raised as the first Open Question, which cites the very finding. The note therefore knows the residue exists. But the experiment section still reads the four findings as evidence that "the notes had put their support beyond" the cap. It never says that one of the four lies outside the proposed unit.
- *Inference labelling* is not engaged. The note recruits two of the four findings and is silent about the other two.
- *Absence detection* is not engaged. The note asserts the opposite of what its cited validator can do, and supports it with a counterfactual ("Had the details been quoted…") that presupposes an enforcement rule the Scope section explicitly leaves undecided.
- The *failure-mode* sentence in "Placing the bound on the artifact rather than the review" is stated without qualification ("on a conforming note it never binds"). This conflicts with the note's later concessions.

The attack does not reach the note's core: step size relative to the check, the two bounds coming apart, quoting jointly-supporting passages rather than splitting, and N as an auditability convention. These stand, and the note's precedents and scope bounds support them. The attack lands on the placement comparison and on how the note reads its own evidence.

## Constructive findings

- Qualify the failure-mode claim to what the validator actually removes. For example: the artifact-side bound removes the silent failure *for the finding step*. The reviewer's limit can still bind on representativeness, on linked-note representation and on inference framing, and those still need disclosure. This makes the placement section consistent with "Occurrence is not representativeness" and the first Open Question.
- Correct the "validator's result" sentence. Either name the missing enforcement rule as a premise (every source-attributed detail carries a verbatim quote or a `(snapshot required)` mark, checked mechanically), or describe the absence as a reviewer finding that the bound makes cheaper to reach.
- In the experiment paragraph, account for all four findings. Two are absences of retained support (in scope). One is a linked-note representation failure (outside the unit by construction). One is inference labelling (outside the unit). The evidence then supports what the note can actually claim: the artifact bound would have caught half the cap-hidden findings before review, and the rest still need a reviewer who reads.
- Mark the artifact-side side of the comparison as proposed rather than deployed, since its validator rule is not yet decided.

## Secondary objections (optional)

- The experiment counted "distinct linked artifacts", including linked notes and ingests. The note's unit is the unquoted source. The "six, eleven, fourteen and sixteen artifacts" figures are therefore not counts in the note's own unit. A reader could take them as showing those notes exceeded a source bound that was never measured.
- The corpus section counts notes in `kb/notes/` as of 2026-08-27, while the note itself lives in `kb/theory/`. If the collection has since moved, the location should be marked as historical so the count stays reproducible.
