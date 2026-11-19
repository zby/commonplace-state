---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A detailed artifact should leave a discoverable route back to wider organizing context."
    reason: "DOUBTFUL — (universal, normative) the upward direction of the criterion discriminates between KB designs — the note later counts search as an adequate outward route (\"Backlinks, an index, or search may supply the outward route\"), and in any searchable KB every artifact then trivially has a discoverable route back, so the 'back' half of 'both directions' is satisfied by every searchable design unless the fourth question (preserving why the views belong together) carries the test; the note never says that it does — LOCAL — instance"
  - scope: passage
    quotes:
      - "A contextual phrase says why the target matters in the current argument."
    reason: "DOUBTFUL — (universal) authored link context preserves the task-relative relationship across a switch — the phrase records why the target mattered to the author's argument at writing time; a reader following the same link for a different task (e.g. an agent tracing evidence for a claim the linking note only mentions in passing) receives the author's bearings, not its own, so the link preserves an argument-relative relation and only coincidentally a task-relative one; the note's claim that link context preserves 'the task-relative relationship' needs the condition that reader task and authoring argument align — LOCAL — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — (unstated, universal) making switches inexpensive is worth its authoring and maintenance cost wherever a reader switches views — the 'should' prices only the reader's transition cost; indexes, contextual link phrases and descriptions must be written and kept current, and stale indexes or drifted descriptions give misleading broad views that raise rather than lower switch cost; a KB small enough to load whole also gains little from switch routes; the criterion needs a scope condition on scale or maintenance capacity, or an explicit trade-off with upkeep cost — LOCAL — instance"
  - scope: passage
    quotes:
      - "A reader using a knowledge base alternates between broad views that expose possible routes and narrower views that supply detail."
    reason: "HOLDS — (generic description of KB reading) readers alternate between broad and narrow views — the obvious counterexample, a single-fact lookup that goes straight from search to one artifact and stops, is conceded and fenced by the note's 'task-relevant switches' and its Boundaries statement that not every task returns to a broad view; under that qualification no defeater was found"
  - scope: passage
    quotes:
      - "a system may retrieve the right detailed artifact yet make its wider context hard to recover"
    reason: "HOLDS — (existential) switch cost is a property separable from retrieval accuracy — re-derivable instance: chunk-level retrieval that returns the correct passage stripped of its parent document and section context; the converse (good overview that never reaches detail) is equally checkable; the premise needs only existence and has it"
  - scope: passage
    quotes:
      - "The gradient is useful only when each pointer supports a sound next-read decision"
    reason: "HOLDS — (conditional) Commonplace's pointer tiers (title, description, link phrase, body) form a usable cost gradient — the natural defeater, titles or descriptions that misrepresent their bodies, is already priced in by this stated condition and the linked pointer-tradeoff note; the mechanism claims are conditional on pointer accuracy and survive under that condition"
  - scope: passage
    quotes:
      - "Resolution here means the scope and detail exposed by a view, not an intrinsic abstraction rank assigned to an artifact."
    reason: "HOLDS — (definitional cut) resolution belongs to views, not artifacts — the Mechanisms section does sort by artifact kind (index vs note), which looks like an intrinsic rank, but each case is presented as a view an artifact exposes, and the same note can be a broad view (its title list of links) or a detailed one (its body); no case was found that the view-relative cut mis-sorts"
  - scope: passage
    quotes:
      - "Resolution-switching is not the same as addressability grain."
    reason: "HOLDS — (definitional distinction) resolution-switching is distinct from grain, pointer accuracy and recall — coarse grain can prevent a narrower view from existing, which shows dependence rather than identity, and the note explicitly says these properties 'can enable or defeat a switch' without establishing it; the distinction is not idle because a fine-grained, accurate, high-recall system can still lack an upward route"
outcome: report
---

# Premise decomposition: A knowledge base should support fluid resolution-switching

**Register:** claim
**Central commitment (one sentence):** A knowledge base should make task-relevant transitions between broader and narrower views inexpensive in both directions while preserving why the views belong together, and this qualitative criterion is distinct from and complementary to retrieval accuracy.

## Premises and counterexamples

The commitment is a normative design criterion with two parts: a definitional cut (what resolution-switching is and what it is not) and a "should" that is bidirectional. It consumes three kinds of premise. First, descriptive premises about reading: readers do alternate between scopes, and switch cost is separable from retrieval accuracy. Both hold, partly because the note already fences the obvious exceptions with "task-relevant" and its Boundaries section. Second, mechanism premises: that titles, descriptions, indexes, link phrases and progressive disclosure supply the views and preserve the relationships between them. The pointer-gradient premise survives because it is stated conditionally. The link-context premise is dented: authored phrases carry the author's argument, not the reader's task. Third, premises the "should" consumes without stating them. The downward and upward directions must both discriminate between designs, and providing the routes must be worth its cost. The upward direction is weakened by the note's own concession that search counts as a route back, which makes that half nearly vacuous unless the "preserves why" question carries it. The cost premise is never stated, and maintenance drift is a concrete way switch routes become misleading.

No premise failure propagates to the commitment as a whole. The criterion is modest and explicitly qualitative, so each dent can be repaired by a qualification in the Boundaries section rather than by retracting the claim.

## For the human

Look first at the upward-route premise: once search counts as a route back, decide whether the "back" half of "both directions" is tested by the fourth question (preserved relationship) and say so, or the bidirectional criterion stops distinguishing designs.
