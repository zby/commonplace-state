# Assessment: A knowledge base should support fluid resolution-switching

**Proposed purpose (operator named none):** Agents and maintainers designing
KB navigation (indexes, link context, descriptions, search) should be able to
use resolution-switching as a criterion that rejects specific design choices
that retrieval accuracy and addressability grain would accept.

**Decision: stop. Plan the rewrite, not passes.** The highest-value change
against this purpose is to the claim, not the text. The upward half of the
central "should" is unsupported as stated. The passes do not change claims,
and most of the text they would polish (the caveats, the Boundaries section,
the link-context paragraph) is text a rewrite would replace.

## Ranked changes

1. **Support or scope the upward-route claim** — cost: claim change; rewrite.
   No pass can make it. "A detailed artifact should leave a discoverable route
   back to wider organizing context" has only one ground: readers alternate
   between views. The composition-friction report marks it UNSUPPORTED. The
   premise-decomposition report marks it DOUBTFUL: the Boundaries section
   accepts search as a route back, so every searchable KB passes the "back"
   half unless the fourth question carries the test, and the note never says
   it does. The note also never settles whether the artifact or the system
   owes the route. A rewrite must state the entry condition under which a
   route back is needed (for example, arrival by search rather than descent
   from an index). It must also say which question tests the route back.
2. **Give the "should" content a retrieval-centric designer could dispute**
   — cost: claim change; rewrite. The explanatory-reach finding (depth 2),
   the claim-strength finding on the title (depth 2) and the critique
   (attack partially lands) converge. Once task-relativity, "avoidable" cost
   and optional return are stated, the prescription weighs cheap switching
   against nothing. It also names no design that the criterion rejects and
   existing measures accept. The critique and premise reports supply the
   missing parts: the bounded-context reason for switching, the cost of
   writing and maintaining indexes and link phrases (stale indexes raise
   switch cost), and one separating case. If no separating case exists, the
   critique says the honest claim is weaker: a named bundle of existing
   properties, evaluated at transitions. Choosing between these is a claim
   decision.
3. **Narrow the link-context mechanism** — cost: claim change in one
   paragraph, which dependents use. The premise report shows that authored
   link phrases preserve the author's argument relation, not the reader's
   task relation. The friction report adds that the phrase sits at the source
   and does not help the reverse direction. Concept attribution (depth 5) and
   grounding alignment (depth 2) both find that "the navigational value of
   [encoding link strength…]" overstates what the target supplies. The
   target's payoff is traversal priority. Narrowing "task-relative
   relationship" changes a claim that `kb/sources/i-like-em-thick.ingest.md`
   relies on.
4. **Reconcile Q2 with the grain boundary** — cost: one question reworded,
   but the reword changes what the criterion tests. The critique shows that
   Q2 restates addressability grain while Boundaries says the criterion is
   distinct from grain. Rewording Q2 to ask whether a route exists from the
   current broad view into the unit changes what the criterion checks.
5. **Consolidate the four caveats and state both conditions in the opening**
   — cost: one structural pass (readability-and-flow). This comes from the
   compression synthesis and the marginal-value-redundancy WARN (depth 4).
   It is worth doing only after items 1–2. The second Boundaries paragraph
   it would delete is the passage that admits search as a route back, which
   is where item 1's rewrite works.
6. **Identify Commonplace in the mechanisms section** — cost: one clause
   (accessibility/unidentified-references, depth 3). Cheap. Fold it into the
   rewrite.
7. **Title** — cost: title change (opening-and-title, or claim-strength via
   fix-strategy-taxonomy). The title should follow whatever claim item 2
   settles. Retitling now would retitle a claim still in question.

## Sentence a hostile reviewer attacks first

"A detailed artifact should leave a discoverable route back to wider
organizing context." The note gives it no ground beyond observing that
readers alternate. Its own Boundaries section then lets search count as the
route, which makes the requirement close to vacuous for any searchable KB.

## What reads well

The four mechanism paragraphs each name a distinct surface and link it to
grounded support. The view-relative definition of resolution ("scope and
detail exposed by a view, not an intrinsic abstraction rank") is a clean
cut that the premise review found no counterexample to.

## Candidate overclaims: support or divergence

- "This is the navigational value of [encoding link strength in position and
  prose]" — **support**; may be narrowed to "the target supplies relationship
  words as role cues".
- "its role is to preserve the task-relative relationship across the
  transition" — **support**; may be narrowed to the author's argument
  relation. Narrowing it reaches `kb/sources/i-like-em-thick.ingest.md`.
- "Those properties can enable or defeat a switch, but none alone establishes
  bidirectional navigability." — **support**; the rewrite decides whether it
  becomes a separating case or a bundle claim.
- "A detailed artifact should leave a discoverable route back to wider
  organizing context." — disputed; goes to the rewrite (item 1), not to a pass.
- **Divergence (must keep):**
  - "Resolution here means the scope and detail exposed by a view, not an
    intrinsic abstraction rank assigned to an artifact." All six dependents
    rely on the term and this sense.
  - "Resolution-switching is not the same as addressability grain." The
    premise review found the distinction holds: a fine-grained, accurate,
    high-recall system can still lack an upward route.
  - "a system may retrieve the right detailed artifact yet make its wider
    context hard to recover" — the existential separation from retrieval
    accuracy, which the premise review found holds.
  - "Resolution-switching helps a reader assemble those views; it does not
    perform the recognition or guarantee a discovery." This bounds the
    stronger reading in `kb/sources/creative-thinking-by-claude-shannon.ingest.md`.

## Stale qualifications (claim questions for the operator)

- The opening says the *artifact* "should leave a discoverable route back".
  The second Boundaries paragraph says backlinks, an index or search may
  supply that route instead. These two places assign the obligation to
  different owners.
- Q2 ("reach the needed detail without loading unrelated material") is
  qualified as distinct from grain by Boundaries, but it restates grain's
  selective-read floor.
- The "Commonplace mechanisms" heading assumes the reader knows what
  Commonplace is.

## Dependents affected by the rewrite

From the role report (run directory
`kb/reports/state/review/runs/v2/revise/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching/43adb6715b85/role`).
No dependent uses the evaluative criterion, the four questions, the
Boundaries section or the open questions, so items 1, 2 and 4 reach no
dependent. These dependents are reached:

- Item 3 (link context) reaches `kb/sources/i-like-em-thick.ingest.md`.
- Any change to the term or its view-relative sense reaches
  `kb/theory/areas-exist-because-useful-operations-require-reading-notes-together.md`
  (which reads it as "levels"), `kb/sources/gwern-design-of-this-website.ingest.md`,
  `kb/sources/i-like-em-thick.ingest.md` and
  `kb/sources/creative-thinking-by-claude-shannon.ingest.md`. The Shannon
  ingest already uses the term in another sense (restatement from other
  viewpoints) and claims a stronger role than the note allows.
- The title/description/body mechanism reaches
  `kb/theory/short-composable-notes-maximize-combinatorial-discovery.md`.
- The progressive-disclosure gradient reaches
  `kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md`.

The rewrite should keep the term, its definition and these two mechanisms.

## Findings not acted on in this run

The run stops, so no finding gets a pass. Each is routed to the rewrite:

- `…/semantic/explanatory-reach.md` (depth 2) — a claim change (item 2);
  passes cannot add the trade-off or the failure condition.
- `…/frontmatter/claim-strength.md` (depth 2) — the title should follow the
  claim the rewrite settles (items 2, 7).
- `…/semantic/grounding-alignment.md` (depth 2) and
  `…/sentence/concept-attribution.md` (depth 5) — they fall in the
  link-context paragraph, which item 3 rewrites. A local attribution fix now
  would be replaced.
- `…/accessibility/unidentified-references.md` (depth 3) — valid and cheap.
  Fold it into the rewrite rather than spend a pass on a section the rewrite
  will touch.
- `…/kb/instructions/compression-bundle/marginal-value-redundancy.md`
  (depth 4) — its WARN targets include the Boundaries paragraph that item 1
  rewrites. Its INFO item is the link-context sentence of item 3.

## Stop

A claim is unsupported: "A detailed artifact should leave a discoverable
route back to wider organizing context." (composition-friction UNSUPPORTED;
premise-decomposition DOUBTFUL). The critique
(`kb/reports/state/review/results/kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md/kb/instructions/critique-note.md`)
proposes, conditionally, a different and weaker claim: a named bundle of
existing properties evaluated at transitions. Route:
`commonplace-review run rewrite kb/theory/a-knowledge-base-should-support-fluid-resolution-switching.md --commission FILE`,
with the commission prepared with `cp-skill-write-multistage`.
