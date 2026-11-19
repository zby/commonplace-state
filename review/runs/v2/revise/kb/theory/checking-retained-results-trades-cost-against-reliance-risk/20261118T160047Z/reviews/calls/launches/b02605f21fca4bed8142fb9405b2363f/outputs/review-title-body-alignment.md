---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A mechanical check derives a retained result from, or compares it against, identified available inputs. Relying on one requires:"
    reason: "The body also lists the conditions a mechanical check needs before it can be relied on: a rule applied without judgment, a locatable copy and source, a source available at check time, and a sufficiently trustworthy checker. It separately establishes that the absence of a known change does not establish freshness. Both sections bear on how cheap and how reliable a check is, so they stay within the title's trade-off. They do extend its scope slightly, from the trade-off itself to the preconditions for mechanical checking. This needs no title change."
    level: info
outcome: pass
---

# Review

## Summary

The body supports the H1 claim. It sets out the saving a retained result provides and says checking spends part of it. It then names the reliance risk: staleness through separate update paths, and suppression of the search that would find omissions. It concludes that how often to check depends on check cost relative to reliance risk. Two worked cases apply the trade-off. The completeness mark has a cheap, defined check on a claim that authorizes stopping, so it favours enforcement. The connect report has expensive rediscovery with broad dependencies, so reuse can be reasonable.

The later sections, on freshness and on what a mechanical check requires, elaborate the cost and reliability side of the same trade-off. There is no claim drift. The scope extension is minor and is recorded as an info finding.
