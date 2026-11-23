---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The [proposal-lifecycle decision](../reference/adr/028-design-proposals-live-in-reference-proposals.md)
    was later used to design the [article layer](../reference/adr/057-articles-use-an-editorial-profile-and-excluded-drafts.md)
  reason: The linked decisions identify the two endpoints, but the note gives no specific rule carried
    from the earlier decision into the article design. The article ADR identifies a proposal and a worked
    case as inputs without identifying ADR 028 as an input. Supply the trace of reuse or state the observable
    similarity directly.
  level: warn
- scope: passage
  quotes:
  - while the [reports-layer decision](../reference/adr/007-reports-directory-for-generated-snapshots.md)
    introduced a role later consumed by several workflows
  reason: The linked decision describes how report producers, authors, reviewers, and the scaffold use
    the collection and its retention policy. The note leaves the reused role unnamed and gives no example
    of a later workflow consuming it. Name the role and identify a workflow that exercised it after the
    decision.
  level: warn
outcome: warn
---

# Review of orphan references

The evidence inventory gives a source and a comparison axis for the named experimental systems. The Agno walkthrough and tag-README trace also give enough local context to evaluate the bounded claims made from them.
