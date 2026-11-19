# Friction check: Stale indexes reduce discovery when they suppress fallback search

**Note:** kb/notes/stale-indexes-reduce-discovery-when-they-suppress-fallback-search.md
**Central claim (one sentence):** An incomplete index that appears exhaustive lowers discovery recall relative to no index when its presence makes the same consumer stop instead of running a more complete search of current content.

## Filter
**Verdict:** SURVIVES
The claim requires an incomplete but plausible index, a more complete fallback search, and a consumer who runs that search only when the index is absent. Those properties describe one consistent control-flow comparison; the claim does not require every stale index to reduce recall or claim lower total utility.

## Signal — thinnest joints
1. **“The important question is therefore not which lifecycle event deserves another reminder, but whether every relevant source change reaches the index through a reliable synchronization path.”** — THIN — Manual synchronization supports checking whether the whole update path is reliable, but it does not establish the “not ... but” exclusion: an event-specific trigger or reminder can be part of that path.
2. **“A failed check must invalidate the claim and force repair or fallback rather than leave consumers trusting the view.”** — THIN — A mismatch supports invalidating the completeness claim, but it does not make repair or fallback the only warranted responses. Reclassifying the view as partial and making the recall trade-off explicit is another response allowed by the note's next defense and conclusion.
3. **“When membership is mechanically queryable, generate the complete listing from that source instead of maintaining a second membership list by hand. This removes the coupled edit: regeneration recovers the current set.”** — THIN — Generation removes the manual membership edit and regeneration can recover the current set, but this does not connect a source change to timely regeneration; a retained generated view can still be stale between refreshes.
4. **“Together, these defenses align stopping behavior with warranted coverage.”** — THIN — The defenses can establish or communicate coverage, but stopping behavior aligns only if refreshes run and consumers receive and honor invalidation, partiality, or continuation signals. The note prescribes those responses without supplying the common operational link that makes the synthesis follow.
5. **“The same mechanism applies to any artifact a consumer treats as exhaustive, including specs, documentation, plans, and curated lists. Once an outdated artifact changes the consumer's stopping behavior, it can suppress a check against more current information.”** — HOLDS — The generalization retains the mechanism's causal conditions: the artifact must be outdated, treated as sufficient, and alter stopping behavior. Under those conditions its type does not matter to the control-flow effect.

## For the human
Look first at the missing link between a source change and the refresh or consumption behavior that makes the proposed defenses preserve fallback discovery.
