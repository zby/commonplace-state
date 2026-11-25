---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A bounded empirical illustration of a base-model floor appears in"
    reason: "The note uses the Harness Evolution ingest as evidence that the three weakest tested models produced no held-out gains under a loop that improved stronger models. The link text does not carry `(snapshot required)`, so only the ingest's `## Quotes` section counts as source support, and that section states that no source quotes have been retained. The retained extracts therefore contain no source material from which to judge this evidential use."
    level: fail
  - scope: passage
    quotes:
      - "harness code can take over much of the loop's machinery"
    reason: "The scheduler–LLM separation note argues, as a conjecture about total cost of reliable execution, that code can maintain workflow state and enforce defined transitions (bookkeeping). The note invokes it for a wider list: context assembly including routing and loading the relevant artifacts, replaying cases, running ablations and bisects, and executing rollbacks. Deciding which artifacts are relevant is not bookkeeping in the target's sense, and the note does not articulate why the target's asymmetry transfers to these functions. The support is plausible but the scope extension is not stated clearly enough to verify."
    level: warn
  - scope: passage
    quotes:
      - "In open-ended work where new failure modes, commitments, and remedies keep arriving"
    reason: "The relocation note says a meaning-dependent judgment can be placed upstream or on another processor but not removed. The note concludes the judgments remain on the frozen base LLM. The open-ended condition partly supplies the transfer (the target says a judgment falls due at use time when its inputs do not yet exist), but the target also permits offloading to other processors, including people, which the note handles only in the bootstrap paragraph. Plausible, not airtight."
    level: info
outcome: fail
---

# Review

## Summary

The only external empirical support in the note is the Harness Evolution ingest. Its `## Quotes` section has no retained quotations, and the link is not marked as requiring the snapshot. Under this gate's rules, the note's specific empirical claims about that paper cannot be checked against source material. That gives a FAIL regardless of whether the ingest's analysis paraphrase agrees with the note.

The linked library notes were checked for whether they are represented accurately. The operative-change, single/double-loop, on-balance-judgment and diagnostic-richness links are used at the scope their targets claim; the footer labels them as extensions or definitions, not as proof of the split. The scheduler–LLM separation link is stretched. Its target concerns bookkeeping and defined state transitions and frames the benefit as a cost conjecture. The note uses it to cover a broader set of harness functions, including artifact routing. The relocation link mostly supports the note, though moving from "cannot be eliminated" to "stays on the base LLM" depends on the open-ended-work condition.
