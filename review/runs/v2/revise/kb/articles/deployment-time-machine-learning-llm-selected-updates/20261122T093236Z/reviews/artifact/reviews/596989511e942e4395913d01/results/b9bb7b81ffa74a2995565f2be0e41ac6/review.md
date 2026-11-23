---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The procedure need not assign every version a number. For the pair at hand, the
    judge can favor either version or leave the comparison open.
  - Some open comparisons close when the alternative is changed. Keeping the routing
    line for good may be open, while trying it with a cheap way back can be better
    under every compatible measure. What still remains is taken as a decision with
    its reasons, not reported as an improvement, and later evidence can reverse it.
  reason: 'Most of this paragraph recaps points already made. The introduction already
    says the judge need only compare the candidates at hand, including leaving the
    system unchanged. The robust-comparison paragraph just above already says an open
    comparison can still be acted on through reversibility, ''as in the routing-line
    example above''. The ''decision, not an improvement'' stance appears again in
    the success section (''Letting a change stand while its verdict is open is a decision,
    not a demonstrated gain''). Only two sentences add anything: the judge-specification
    sentence (''This says what the judge must do, not how its weights produce an answer'')
    and the warning that consistent answers can still neglect a required cost. Fold
    those two into the preceding ''The bet is not that the model writes down value
    functions...'' paragraph and delete the rest.'
  level: warn
- scope: passage
  quotes:
  - The loop itself is not new.
  reason: The previous paragraph has just said 'The process itself is not new' and
    given handbooks, linters and PRODIGY as precedents. This repeat sits inside the
    bold statement of the bet and adds nothing. Cut it.
  level: warn
- scope: passage
  quotes:
  - Its limits are which proofs can be found and whether the formalization is adequate.
  reason: 'This closing restatement repeats the same paragraph''s earlier price clause:
    the machine must ignore improvements it cannot prove, and a valid proof does not
    establish adequate axioms. The ''not rigid'' point before it is new: the machine
    can rewrite its own utility function. The recap after it is not. Cut it, or end
    the paragraph on the utility-rewrite sentence.'
  level: warn
- scope: passage
  quotes:
  - '*Unfaithful rationales.* Legible prose can diverge from what actually steers
    the model''s outputs, masking the real cause of gains or losses.'
  reason: This hazard repeats the faithfulness cost already argued and linked in the
    gradient-training section. It may earn its place because the failure condition
    in the closing paragraph names it, and the list collects the hazards. It could
    also shrink to a back-reference. Uncertain whether the repetition does necessary
    reader work.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b9bb7b81ffa74a2995565f2be0e41ac6/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/596989511e942e4395913d01/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: b9bb7b81ffa74a2995565f2be0e41ac6
completed-at: '2026-11-22T09:37:00Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/b9bb7b81ffa74a2995565f2be0e41ac6/outputs/review.md
raw-output-sha256: 0b456e182466b46579d14fb6bbbe94b1207ca85c2c0b7979e5c1e92d6251e56b
format: 2
---

# Review

The article is mostly economical for a lead piece that has to carry a worked example, a definition, a precedent sequence, a Bitter Lesson objection and an evidence section. Most of its restatements do a job. The three-point summary after the routing-line example turns the example into claims. The return to the "no built-in guarantee" point at the start of the success section turns it into the separate success test. The final failure condition turns the hazards into a falsifiable bet. None of these is flagged.

The redundancy is concentrated around the statement of the bet. The robust-comparison subsection says the same things in three paragraphs in a row: that the judge compares a pair and may leave it open, that reversibility lets the system act on an open comparison (with the routing line as the example), and that an action on an open comparison is a decision rather than a demonstrated improvement. The third paragraph adds only two sentences of new content. Those can be folded into the paragraph before it. Smaller repeats are a duplicated "not new" clause in the introduction and a recap sentence that closes the Gödel machine paragraph.

The hazard list's "unfaithful rationales" item repeats an earlier cost paragraph. It is marked INFO because the closing failure condition names that hazard, so the list entry may be needed as the anchor for that reference.
