---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "checked routing catalogues"
    reason: "\"Routing\" is the one KB-flavoured term that recurs throughout the body (routing surfaces, routing cost, unknown-name routing, routing and migration debt, route obsolete prose, routing catalogues). It is never formally defined, so there is no definition point for it to drift from. Most later uses keep enough local context (lookup cost, migration debt, retirement review) to be read alone. This late use leans hardest on the reader remembering what a route is in a KB. Consider a short plain gloss such as \"catalogues that point agents to the right file\"."
    level: info
outcome: pass
---

# Review

The note introduces several KB-internal phrases: zero-structure expansion, selection bloat, value gate, reachability oracle, fixed-difficulty scaffolding and encoding distortion. Each appears once or twice, usually in the bullet that grounds it. None is reused more than twice after it is introduced, so this gate's failure mode does not occur.

The only term that recurs is "routing". Its uses are spread across sections but mostly come with local cues that keep them readable. The single INFO finding marks the use where a plain-language gloss would help most. It does not block the note.
