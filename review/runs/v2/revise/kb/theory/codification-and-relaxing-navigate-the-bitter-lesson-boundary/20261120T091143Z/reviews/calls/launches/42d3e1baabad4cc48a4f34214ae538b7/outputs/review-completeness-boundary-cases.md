---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'the spec fully captures the subproblem, so implementing it need not lose generality within that declared scope'
    reason: 'Boundary case: Canny edge detection. Its specification fully captures the subproblem "detect edges", so by the arithmetic bullet''s stated criterion it is an arithmetic-regime decomposition; by the vision bullet''s criterion (the spec is a theory of a larger capability) it is a vision-feature decomposition. The two bullets classify decompositions, but the criterion that separates them is relative to which larger capability is in scope. Heuristic 1 supplies that relativity ("relative to that numerical contract"), so the case maps, but only after reading ahead; coverage is possible but strained.'
    level: info
  - scope: passage
    quotes:
      - 'In the arithmetic regime, the bet is safe'
    reason: 'Boundary case: a component whose extracted regularity is genuinely part of the spec (bet won) but which is still relaxed because a general replacement extends past its scope or becomes cheaper to integrate than to maintain. The bet framing treats relaxing as what happens to a losing bet; this won-bet-but-relaxed case is not named. It is partly covered by the remark that economic gain depends on implementation and maintenance costs and by heuristic 1 ("current leverage, not permanence"), so coverage is strained rather than absent.'
    level: info
outcome: pass
---

# Review

## Frameworks tested

The note builds three structures: the two-regime split of decompositions (arithmetic vs vision-feature) with an explicitly acknowledged blurry zone between them; the codify/relax trajectory, which it says runs in both directions and repeats at different stack levels; and the "every codification is a bet" frame with safe, risky and blurry outcomes.

## Boundary cases

- **Simplest instance** — an executable test checking a function's numeric return: maps cleanly to the arithmetic regime (the note's own heuristic 1 example).
- **Extreme instance** — edge detection codified, relaxed, then possibly re-codified as an accelerator: explicitly covered by the bidirectional trajectory.
- **Between items** — a component whose regime is unknown: covered by the declared blurry zone, which is the note's main premise.
- **Adjacent concept** — codification by adopting a model package: explicitly scoped out of the code-extraction case, and the note says a relaxed replacement can itself be codified by adoption.
- **Path-relative classification** (Canny) and **won bet that is still relaxed**: these map only with strain; recorded as INFO.

No case clearly falls outside the claimed coverage, because the note claims a two-pole picture with a blurry middle rather than an exhaustive partition. The taxonomy is short and proportionate to its role, so expanding it is not recommended; at most, making the path-relativity and the won-but-relaxed case explicit would remove the strain.
