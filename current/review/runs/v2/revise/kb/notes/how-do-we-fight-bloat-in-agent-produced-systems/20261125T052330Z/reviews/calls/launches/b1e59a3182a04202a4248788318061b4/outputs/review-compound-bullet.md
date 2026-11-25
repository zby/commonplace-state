---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "An unconfirmed conjecture in `kb/log.md` is that thoroughness pressure paired with superficial length pressure produces both failures at once"
    reason: "The brevity-pressure bullet, about 150 words long, first makes a sourced claim: length pressure makes wording denser without cutting content. It then adds a separate, unconfirmed conjecture from the log: thoroughness pressure combined with length pressure produces bloat and encoding distortion together. The conjecture is a second claim with a different evidential status. It could stand as its own bullet, but here it sits after two long quotations, where a reader scanning the list is likely to miss it."
    level: warn
  - scope: passage
    quotes:
      - "At the code–prose boundary,"
    reason: "The first Current answer bullet pairs the executor-determinability principle with a separate code–prose finding: direct access to live source made exact-fact documentation copies unnecessary. Both fit the lead-in, which names the executor and live source, so the bullet reads as one rule with two applications rather than as two unrelated points. Splitting it would make the evidence-backed second half easier to scan, but the bullet still works as written."
    level: info
outcome: warn
---

# Review

## Summary

Most long bullets develop one point with supporting detail. Examples are the reverse-compression bullet, which backs its claim with rewrite evidence, the cheap-adoption bullet and the agent-additive-bias bullet. The bias bullet's two questions, why the bias exists and how to counter it, are tied together by its own reasoning: different causes call for different countermeasures.

The brevity-pressure bullet in Unsettled is the clear case of a compound bullet. Its sourced finding and its unconfirmed log conjecture are independent claims with different evidential status. The conjecture comes after long verbatim quotations, so a reader scanning the list is likely to miss it. The first Current answer bullet is a milder case, because its lead-in already covers both halves.
