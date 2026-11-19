---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A source that has been quoted verbatim is not one of them."
    reason: "DEFEATED — Premise (universal, no stated mode): once a source has been quoted verbatim, the reviewer no longer has to open it, so the grounding check's unit is the unquoted source. — Counterexample: a note quotes source S for one detail and attributes further details to S without quoting them. The validator passes the quotes that exist; the reviewer must still open S to check the unquoted attributions. The linked paired assay records this case: the compounding note's FAIL was 'missing retained support for two HyperAgents details', from a source the note otherwise cited. The cost unit is therefore the unquoted claim-to-source attribution, not the source. A partly quoted source still counts. — LOCAL: the commitment survives if the unit is restated as 'each attribution not carried by a validated quote'. The Mechanism section and the description need that restatement. — instance"
  - scope: passage
    quotes:
      - "Both are absences of a retained passage,"
    reason: "DOUBTFUL — Premise (universal): an absent retained passage is 'a validator's result rather than a reviewer's finding'. — Reason: the cited validator (ADR 046) checks only quotations that are present and marked verbatim, by substring match. It cannot see that a claim has no quote; noticing that a quote is missing still requires a reviewer judgment about which claims need one. The conditional that follows ('Had the details been quoted, either the quote would match or the note would have failed') holds. It does not turn the absence itself into a mechanical result. A rule requiring a quote for every source attribution would be needed, and the note does not state that rule; the Scope section disclaims deciding validator rules. — LOCAL: narrow to 'once quoted, the remaining check is mechanical', or name the required-quote rule as an assumption. — instance"
  - scope: passage
    quotes:
      - "An artifact-side bound does not have that failure mode, because a conforming"
    reason: "DOUBTFUL — Premise (universal): an artifact-side bound has no silent-failure mode, because a validator holds it and a conforming note fits the check by construction. — Reason: the silent failure moves rather than disappears. The validator can count only the citations the note makes and the quotes it carries. A note that quotes a convenient passage while its claim depends on surrounding qualification, or that leaves a source unlinked, conforms and receives a pass. From outside, that pass is indistinguishable from a sound one. The note concedes the representativeness gap later ('Occurrence is not representativeness'), but this premise is stated before that concession, without it. Also, no such validator exists yet (Scope: 'Does not decide N, a validator rule that would enforce it'), so 'by construction' describes a proposed mechanism. — LOCAL: restate as 'the failure moves from the reviewer's stopping point to the author's choice of passage, where a reader can see it on the page'. That weaker contrast still supports artifact-side placement. — instance"
  - scope: passage
    quotes:
      - "and under\nsuch a bound the four notes would have had to split or quote before review"
    reason: "DOUBTFUL — Premise (universal): all four cap-only findings in the paired assay arose because support lay beyond the cap. An artifact-side bound would have forced each note to split or quote, so the evidence reads as being about note size. — Reason: by the linked report, two of the four findings are not source-placement problems. The treat-continual-learning FAIL was 'broader mechanism attributed to a link that disclaims it', a link to another note. This note's own unit excludes such links from the count, so the bound would not force that note to restructure. The topology WARN was 'two target-side transfers not marked as hypotheses', a framing defect that quoting does not address. The note acknowledges the first case only in Open Questions. — LOCAL: limit the rereading to the two source-retention findings, which the note already singles out. — instance"
  - scope: passage
    quotes:
      - "with no observed loss, and the three notes offering the most"
    reason: "DOUBTFUL — Premise (stated as observation, used to rule out capacity as the basis for N): uncapped reviewers read up to 22 artifacts and 322 KB with no loss, and the three largest-offer notes all passed. — Reason: the assay had no ground truth for missed findings in the uncapped arm. A PASS on the largest notes is consistent both with no defect and with a reviewer that saturated and missed one, and nothing in the assay distinguishes the two. The linked report states that it 'does not identify a general attention price' and that size is confounded with evidence need. 'No observed loss' is therefore absence of measurement, not a measured absence. — LOCAL: the conventional-N argument rests mainly on auditability, which stands without this premise; weaken it to 'no degradation was detected, though the assay could not detect a miss in a PASS'. — instance"
  - scope: passage
    quotes:
      - "Links to other notes are also not sources in this sense, because a"
    reason: "DOUBTFUL — Premise (universal): a linked note discharges its own grounding, so it does not count toward the grounding step. — Reason: the discharge assumes that the linked note has a current, passing grounding review and that the citing note represents it faithfully. A linked note may be unreviewed or stale. Misrepresentation is a real failure mode: the assay's treat-continual-learning FAIL attributed a mechanism to a link that disclaims it. The note raises the second case in Open Questions, but the unit's exclusion is stated without conditions. — LOCAL: condition the exclusion on the linked note's review being current, and accept that a representation check remains. — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated premise (universal): a validator can compute the unquoted-source count from the artifact. It would have to tell source links from note links, recognize snapshot-required uses, and decide whether a source's every use is carried by a quote. — Reason: the first two are syntactic and plausible. The third requires knowing which sentences attribute content to a source, and the attribution boundary is a judgment of the kind the grounding reviewer makes. If the validator can count only links that carry no quote at all, the partly quoted source escapes the count (see the DEFEATED finding above). — LOCAL: the bound can be enforced on a coarser proxy, such as distinct sources with no validated quote, with the residual named as reviewer work. — instance"
  - scope: passage
    quotes:
      - "These are different quantities set by different mechanisms, and a note can"
    reason: "HOLDS — Premise: the co-loading bound and the checking bound are distinct quantities that can come apart. — Hunt: the note itself identifies the coupling, quoting spending against co-loading, and treats it as a coupling through one remedy rather than an identity. The eight single-claim, many-source notes are a checkable instance of divergence in one direction. The converse is offered only 'in principle', which is the modality it claims. No defeater was found."
  - scope: passage
    quotes:
      - "a step is atomic relative to a particular check, which is an"
    reason: "HOLDS — Premise: step size has content only relative to a named check. — Hunt: tried to find a check-independent atomicity, such as one claim per note. The note separates that as the co-loading bound, which measures something else. The example of one note being one step for quote-support but several for cross-passage inference shows the relativity concretely. No defeater was found."
  - scope: passage
    quotes:
      - "N is a convention, chosen so that a second checker — including a person — can"
    reason: "HOLDS — Premise: a small step's value is auditability by a second checker, and auditability is worth paying for because LLM verdicts are unstable on unchanged input. — Hunt: the linked assay records 1 of 5 capped repeats disagreeing on unchanged input, which supports the instability premise as a bounded local observation. 'In practice it is trusted rather than audited' is stated as a tendency, so a single counterexample of a large verdict that was audited does not dent it. The note limits the audit to the support judgment and concedes the context check. No defeater was found at the stated modality."
  - scope: passage
    quotes:
      - "so the transfer to agent-reviewed notes is an\nanalogy about checker-relative sizing"
    reason: "HOLDS — Premise: Descartes and Lamport supply a precedent for checker-relative step sizing. — Hunt: the note explicitly limits the transfer to an analogy and disclaims any carried-over N. The quoted passages, especially Lamport's 'depends on the sophistication of the reader', state reader-relative detail directly. No defeater was found at the claimed strength."
outcome: report
---

# Premise decomposition: A note is an atomic step relative to the check that reads it

**Register:** claim
**Central commitment (one sentence):** Notes are bounded twice, independently: once by co-loading and once by checking. The checking bound is relative to a named check, and for Commonplace's grounding check its unit is the unquoted source, which makes the bound placeable on the artifact rather than as a review-side reading budget.

## Premises and counterexamples

The commitment has three parts, and each consumes different premises.

1. **Two bounds, independent:** that the two quantities differ, and that size is meaningful only relative to a check. These premises hold. The note itself already prices the coupling through quoting.
2. **The unit is the unquoted source.** This part depends on three premises:
   - quoting a source removes it from the reviewer's work;
   - links to notes discharge their own grounding;
   - an absent passage is mechanically detectable.

   The pressure falls here. The paired assay the note relies on contains a partly quoted source whose unquoted details still required opening the source. That case defeats the source-level unit and points to a finer one: the unquoted attribution. The other two premises are dented by the same assay record and by the scope of the ADR 046 validator, which checks only quotes that are present.
3. **Artifact-side placement is better:** that a validator-held bound has no silent-failure mode, that the assay's four misses are about note size, and that N cannot be a capacity threshold. Each of these is stated more broadly than its support:
   - the silent-failure mode moves to the author's choice of passage;
   - two of the four misses are not about source placement;
   - "no observed loss" was not measurable in that design.

None of the failures propagates to the central commitment. Every one can be repaired by restating the unit more finely or by narrowing a reading of the evidence, so all are LOCAL. The auditability argument for a conventional N stands on its own and does not need the capacity premise.

## For the human

Look first at the DEFEATED unit premise. "A source that has been quoted verbatim is not one of them" fails on a partly quoted source, as in the compounding note's HyperAgents FAIL. Restating the unit as the unquoted attribution changes the Mechanism section, the description, and what any enforcing validator would have to count.
