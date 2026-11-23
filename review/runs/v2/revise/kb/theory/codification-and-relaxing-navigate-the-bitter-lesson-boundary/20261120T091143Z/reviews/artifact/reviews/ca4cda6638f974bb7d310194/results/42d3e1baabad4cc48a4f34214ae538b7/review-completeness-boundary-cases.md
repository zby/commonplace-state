---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the spec fully captures the subproblem, so implementing it need not lose generality
    within that declared scope
  reason: 'Boundary case: Canny edge detection. Its specification fully captures the
    subproblem "detect edges", so by the arithmetic bullet''s stated criterion it
    is an arithmetic-regime decomposition; by the vision bullet''s criterion (the
    spec is a theory of a larger capability) it is a vision-feature decomposition.
    The two bullets classify decompositions, but the criterion that separates them
    is relative to which larger capability is in scope. Heuristic 1 supplies that
    relativity ("relative to that numerical contract"), so the case maps, but only
    after reading ahead; coverage is possible but strained.'
  level: info
- scope: passage
  quotes:
  - In the arithmetic regime, the bet is safe
  reason: 'Boundary case: a component whose extracted regularity is genuinely part
    of the spec (bet won) but which is still relaxed because a general replacement
    extends past its scope or becomes cheaper to integrate than to maintain. The bet
    framing treats relaxing as what happens to a losing bet; this won-bet-but-relaxed
    case is not named. It is partly covered by the remark that economic gain depends
    on implementation and maintenance costs and by heuristic 1 ("current leverage,
    not permanence"), so coverage is strained rather than absent.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/ca4cda6638f974bb7d310194/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: 42d3e1baabad4cc48a4f34214ae538b7
completed-at: '2026-11-20T09:15:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/42d3e1baabad4cc48a4f34214ae538b7/outputs/review-completeness-boundary-cases.md
raw-output-sha256: bc15d68031948d2282552707128a9596367f58601f4fbe4926fb6b8a68329e9f
format: 2
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
