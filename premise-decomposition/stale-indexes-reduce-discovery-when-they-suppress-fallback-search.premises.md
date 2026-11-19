# Premise decomposition: Stale indexes reduce discovery when they suppress fallback search

**Note:** kb/notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md
**Register:** claim
**Central commitment (one sentence):** An incomplete index lowers discovery recall relative to no index when its apparent exhaustiveness makes the same consumer stop instead of running a more complete fallback over current content.

## Premises and counterexamples
1. **In every covered comparison, the fallback would actually surface at least one index-omitted item that counts toward the same discovery task's recall.** — DOUBTFUL — The body says the current-content operation “could” reveal additional items, but a full-text search can run and still miss a relevant renamed note because the consumer's query uses none of its terms; a more current search surface does not guarantee an additional discovery in that run. — GLOBAL — instance
2. **In every covered comparison, relevant discoveries available only through the index do not offset all relevant discoveries added by the fallback.** — DOUBTFUL — A curated stale index can surface an older relevant note through an editorial category that lexical search misses, while the no-index search surfaces one new relevant note omitted by the index; each route then finds one of two relevant notes, so suppressing the fallback does not lower recall unless “more complete” means greater realized task-relevant coverage. — GLOBAL — instance
3. **The index is the but-for cause of the fallback not running: this same consumer would run the fallback without the index and stops because the index appears exhaustive when it is present.** — HOLDS — Cases where the consumer would stop anyway, or would search despite the index, were hunted but fall outside the claim's explicit suppressed-fallback comparison.
4. **The stop persists through the recall endpoint, so no delayed continuation or equivalent operation restores the omitted discoveries along the route being measured.** — HOLDS — A consumer who later performs the search can erase the route-level loss, but then the index has not ended discovery in the way the note specifies.
5. **The index and no-index routes are evaluated for the same discovery task, relevant-item set, and endpoint.** — HOLDS — Changing the information need, the relevant set, or the measurement endpoint can reverse the comparison, but it no longer tests the note's same-consumer counterfactual.
6. **For a fixed relevant-item set, a route that discovers strictly fewer relevant items has lower recall even if it is faster or better for orientation.** — HOLDS — Speed, orientation, and total utility can favor the index, but they do not change recall; the note expressly places those measures outside the claim.

## For the human
Look first at premise 1: the conclusion needs the suppressed fallback to yield, not merely be capable of yielding, additional task-relevant discoveries.
