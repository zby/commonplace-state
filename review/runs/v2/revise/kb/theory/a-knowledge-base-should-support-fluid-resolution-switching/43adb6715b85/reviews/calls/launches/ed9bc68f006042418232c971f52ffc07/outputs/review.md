---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["A detailed artifact should leave a discoverable route back to wider organizing context."]
    reason: "UNSUPPORTED — The only stated ground is that readers alternate between broad and narrow views. That establishes the movement, not that the upward return must be a KB obligation. A reader who descended from an index or overview may still hold that broad view in context. So the upward route matters mainly when the reader arrived at the detail without a broad view, for example through search, and the note never states this condition. The later Boundaries section also weakens the claim: it lets backlinks, an index or search supply the outward route, so the requirement that the artifact itself 'leave' a route is never pinned down. The index paragraph's 'Returning to the index restores the topic-level view' has the same gap, because it assumes the reader knows which index to return to."
  - scope: passage
    quotes: ["It lets a reader move to a different scope without reducing the connection to an untyped jump."]
    reason: "THIN — The heading claims that link context 'preserves bearings during a switch'. The phrase sits at the source, though, so it explains why the reader should go down. It does nothing for the reader at the target unless the source passage is still loaded. The note does not establish that the phrase survives the transition, or that it helps the reverse direction the note's criterion requires. The sentence 'its role is to preserve the task-relative relationship across the transition' restates the conclusion rather than giving a mechanism."
  - scope: passage
    quotes: ["Titles, descriptions, contextual link phrases, generated summaries, and full bodies can form a cost gradient."]
    reason: "THIN — The gradient described consists of increasingly costly views of one target. It lowers the cost of deciding whether to narrow, not of moving between scopes. The note defines resolution as 'scope and detail', yet the inference that this gradient 'supplies intermediate views' for resolution-switching only addresses the detail axis and the downward direction. It leaves unestablished whether any tier helps a reader widen scope."
  - scope: passage
    quotes: ["a system may retrieve the right detailed artifact yet make its wider context hard to recover, or offer an elegant overview that never reaches the required detail."]
    reason: "THIN — This is offered as the ground for 'It complements retrieval accuracy'. The first case separates fluidity from accuracy: the right artifact is retrieved, but its context is lost. The second case, an overview that never reaches the needed detail, is arguably a retrieval recall failure, not a separate property. So only half the stated contrast shows that the criterion measures something retrieval metrics miss."
  - scope: passage
    quotes: ["a reader can inspect a chain of assertions before choosing which bodies to load."]
    reason: "HOLDS — If titles carry assertions, then reading titles alone does expose a chain of claims at lower cost than bodies, and the linked note is cited for exactly this. The joint is scoped to title-as-claim artifacts, and the note does not claim more. The only implicit limit is that artifacts with topical titles do not offer this view."
outcome: report
---

# Friction check: A knowledge base should support fluid resolution-switching

**Central claim (one sentence):** A knowledge base should let a reader move between broader and narrower views, in whichever direction the task needs, at low transition cost and without losing why the views belong together.

## Filter
**Filter:** SURVIVES

The properties held at once are low transition cost in both directions, no loading of unrelated material, preserved relationship between views, and task-relativity, including permission for routes other than outbound links. These can coexist. Richer link context and intermediate views add some reading cost, but they do so to avoid larger avoidable costs, and the note asks only for avoidable cost to be removed. The hedge "task-relevant" reconciles "in both directions" with "Nor does every task need to return to a broad view". So the claim concretizes to one consistent criterion, though it is weak: it is qualitative and offers no scoring rule, as the note says.

## Thinnest joints

The weakest joint is the opening normative step to the upward direction, because the note gives no reason for it beyond observing that readers alternate. It also leaves unresolved whether the artifact or the system supplies the route back. The two mechanism paragraphs come next. Each one supports the downward, narrowing move well, and each is then credited with the bidirectional, scope-crossing property the criterion defines. This is where the note's fluent prose covers a gap. The contrast with retrieval accuracy is half supported. The title-as-claim inference is the strongest joint and holds within its stated scope. The discovery and grain-boundary paragraphs are hedged enough that they make no load-bearing inference worth surfacing.

## For the human
Look first at the upward direction. Say under what entry conditions, such as arrival by search versus descent from an index, a route back is needed, and whether the artifact or the system owes it. The link-context and progressive-disclosure mechanisms currently mostly support downward movement.
