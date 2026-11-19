---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
  against kb/instructions/critique-note.md
note: kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
note-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews
launch: f07d2c1b4e8a4526b78a944878b55276
completed-at: '2026-11-16T22:31:33Z'
findings:
- scope: passage
  quotes:
  - Can the reader reach the needed detail without loading unrelated material?
  - Resolution-switching is not the same as addressability grain.
  reason: 'The second diagnostic question asks for the condition that addressability
    grain already prices: whether an access path can retrieve the needed unit without
    loading the rest. The Boundaries section then says the criterion is distinct from
    grain. The note should either say what this question adds beyond grain, such as
    the existence of a route into the unit from the broader view, or attribute the
    question to grain and keep only the transition-specific part.'
- scope: passage
  quotes:
  - Those properties can enable or defeat a switch, but none alone establishes bidirectional
    navigability.
  reason: '"None alone" leaves the reductionist reply open: their conjunction, together
    with link context and backlinks or index membership, may establish it. To support
    the claim that the criterion complements existing measures, the note needs a case
    where pointer accuracy, grain, retrieval recall, upward-route availability and
    link context all hold but a task still pays avoidable transition cost. If the
    note cannot give one, it should present the criterion as a named bundle of those
    properties at the level of transitions, which is a weaker but defensible claim.'
- scope: passage
  quotes:
  - Fluidity is relative to the task and to the navigation operations actually available
    to the reader.
  - without paying avoidable transition cost or losing the
  reason: 'With task-relativity, avoidable cost and the optional return to a broad
    view all stated, the normative title risks a near-tautology: make the transitions
    the task needs no more expensive than necessary. The note should state one design
    choice that the criterion would reject and that a retrieval-accuracy or grain
    evaluation would accept. One candidate is a KB whose detail artifacts are reachable
    only through search, with no index or backlink, for a task that repeatedly re-orients.
    That choice would give the "should" observable content.'
- scope: passage
  quotes:
  - 'It complements retrieval accuracy: a system may'
  reason: The two contrast cases are framed against retrieval accuracy alone. The
    linked end-to-end evaluation note already rejects evaluation by retrieval alone
    and lists navigation or decision cost as a diagnostic. The note would be stronger
    if it compared the criterion with that wider diagnostic set and said which transition
    failure the set's questions miss.
contract: report
target-sha256: 43adb6715b85adfb0189cfa5485696ff5e43b0a397a031a8696e7f9ea697c9f2
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/e41c83e5e9f68716f8778cbb/inputs/target/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/artifact/reviews/e41c83e5e9f68716f8778cbb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/reviews/calls/launches/f07d2c1b4e8a4526b78a944878b55276/outputs/review.md
raw-output-sha256: bc6a863b2430e1beb4fe61a9c4b0209162141c9a7579bd2aa6632e513c0aef57
attack-outcome: partially lands
---

# Critique: A knowledge base should support fluid resolution-switching

**Note:** kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md
**Central commitment:** A knowledge base should make task-relevant movement among broad and detailed views inexpensive in both directions, and this "resolution-switching fluidity" is a qualitative evaluative criterion distinct from, and complementary to, retrieval accuracy, addressability grain and pointer accuracy.
**Critique mode:** claim (with a definitional component: the criterion's distinctness from existing properties is load-bearing)
**Attack outcome:** partially lands

## Strongest case against it

This objection comes from an evaluation reductionist: the information-retrieval and component-metric tradition, or within this KB the end-to-end evaluation note's own method of keeping separate diagnostics "without inventing a total score". A new criterion earns its place only if it predicts failures that existing component measures miss. "Resolution-switching fluidity" does not meet that test, for two reasons.

**First, each diagnostic question reduces to an existing property.**

- Q1 asks whether the reader can choose a narrower target without opening every body. The pointer-design and "agents navigate by deciding what to read next" notes already cover this as pointer specificity and accuracy at a follow-or-skip decision.
- Q2 asks whether the reader can reach the detail without loading unrelated material. This is the addressability grain note's matched selective-read floor, almost word for word: "retrieve through the access path in use without loading the rest of the artifact."
- Q3 asks whether the reader can recover a broader view by link, index or search. That is route availability: backlinks, index membership and search coverage.
- Q4 asks whether the transition preserves why the two views belong together. The link-strength note's contextual articulation covers this.

The note's own Commonplace mechanisms section confirms the mapping. Every mechanism it lists is borrowed from one of those linked notes. The "complements retrieval accuracy" contrast then knocks down a narrower opponent than the one that exists. The linked end-to-end note already rejects evaluation by retrieval alone and lists "navigation or decision cost" among its diagnostics.

**Second, once the criterion is hedged, its "should" loses observable content.** The note says:

- fluidity is relative to the task and to the operations available;
- only *avoidable* transition cost counts;
- not every task needs to return to a broad view;
- an outward route may come from search instead of an authored link;
- no scoring rule or threshold exists.

What remains is: make the transitions a task needs no more expensive than they must be. No designer rejects that. Under this reading, the title's normative claim either restates generic cost minimization or names a conjunction of properties the KB already has notes for. The author cannot dismiss this in one sentence, because the note's best defence, "none alone establishes bidirectional navigability", concedes the reductionist's point that a conjunction might.

## How the note engages it

**Partially engaged.**

- The Boundaries section separates the criterion from addressability grain, pointer accuracy and retrieval recall. Its grain contrast, in which grain prices the smallest retrievable unit while resolution-switching asks whether views at different scopes exist and connect, is a real distinction. A KB could have fine grain and no broad views at all. That is the strongest part of the defence, and it keeps the attack from landing fully.
- The evaluative criterion section gives two concrete failure cases: right detail with an unrecoverable wider context, and an overview that never reaches detail.
- The section explicitly limits the criterion to "a qualitative design criterion, not yet a metric". The open questions concede that it has no cost unit and no dead-end test.

What the note does not engage:

- **The conjunction.** It argues against each component property *alone*, not against their combination, so the reduction stays open.
- **Q2 and grain.** It never notices that its second diagnostic question restates grain, which undercuts the boundary it draws.
- **The wider baseline.** Both failure cases are framed against retrieval accuracy, not against the end-to-end diagnostic set the note links to.
- **Vacuity.** It does not show a design choice that the criterion would reject and that the existing measures would accept.

The surviving part of the attack is this: as written, the criterion is defensible as a named, transition-level view over existing properties. It is not yet shown to be an independent property with its own failure mode.

## Constructive findings

- Supply one separating case: a KB, or a Commonplace configuration, where pointer accuracy, grain, recall, upward-route availability and link context each pass, yet a task still pays avoidable transition cost. Possible sources are the absence of intermediate views between a topic index and note bodies, or a broad view whose groupings do not match the task's decomposition. If no such case exists, restate the commitment as a named bundle that evaluates these properties together at transitions. That is a weaker but honest claim.
- Rewrite Q2 so it asks what grain does not: whether a route exists from the current broad view into the needed unit. Alternatively, credit grain for Q2 and keep only the transition-specific remainder.
- Give the "should" observable content by naming one design the criterion rejects, for example detail artifacts reachable only by search, with no index or backlink, for a task that repeatedly re-orients. State why the existing diagnostics would not flag it.
- Compare the criterion with the end-to-end note's diagnostic set, not with retrieval accuracy alone, and say which transition failure that set misses.

## Secondary objections (optional)

- Treating "resolution" as task-relative view scope instead of artifact abstraction rank is reasonable. However, the term invites a reading of fixed levels, such as zoom levels or abstraction tiers. The disclaimer appears only once, in the opening paragraph. Later uses of "broad" and "detailed" quietly rely on a fairly stable ordering of index above note above body.
- The connection-to-discovery section is careful to say that switching does not perform recognition. It gives no mechanism by which fluid switching *raises* the chance of recognition, so its contribution to the note's case is mostly a disclaimer.
