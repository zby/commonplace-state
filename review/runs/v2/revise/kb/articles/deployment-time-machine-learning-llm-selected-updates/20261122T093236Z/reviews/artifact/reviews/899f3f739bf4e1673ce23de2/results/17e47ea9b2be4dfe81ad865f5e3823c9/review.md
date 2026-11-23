---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'The case argued here is the one where the changes are edits to the system''s
    own readable, addressable store. The process itself is not new: software teams
    do it when they maintain handbooks and linters, and symbolic learners such as
    PRODIGY ran a fixed-formula version of it in the 1980s. Like reinforcement learning,
    the term names a process with no built-in guarantee of improvement.'
  reason: 'The first numbered point packs scope restriction, a novelty disclaimer,
    a historical precedent and an RL analogy behind the comparison claim. These sentences
    sit between the reader and the bolded bet. They duplicate material that later
    sections develop fully: the readable-store scope in the gradient-training section,
    PRODIGY in the precedents section, and the no-guarantee point in the evaluation
    section. Cutting them or folding them into those sections would let the comparison
    claim lead directly into the bet.'
  level: info
- scope: passage
  quotes:
  - The loop itself is not new.
  reason: The novelty disclaimer repeats the earlier 'The process itself is not new'
    and sits between the bolded bet and its elaboration. It interrupts the sentence
    that should carry the article. One disclaimer is enough, and the opening needs
    none because the precedents section makes that argument.
  level: info
- scope: passage
  quotes:
  - This is double-loop selection-based learning with targeted correction, for work
    where no fixed criterion is adequate.
  reason: 'The fullest statement of the bet appears only after the three precedents.
    It adds deciding the cases the comparison leaves open, and it names the bet double-loop
    learning with targeted correction while the declared objective stays fixed. The
    opening statement covers parts of this (''revise the criteria it uses to judge
    future edits'') without those labels or the open-case decision. A possible revision
    target: bring the opening statement into line with this fuller form so the reader
    keeps one formulation rather than two.'
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/17e47ea9b2be4dfe81ad865f5e3823c9/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/899f3f739bf4e1673ce23de2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 17e47ea9b2be4dfe81ad865f5e3823c9
completed-at: '2026-11-22T09:36:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/17e47ea9b2be4dfe81ad865f5e3823c9/outputs/review.md
raw-output-sha256: c17f390973a4f32abe89e047af62ca5d9a51a96dfb16c4e6749304282e8ab8f3
format: 2
---

# Review

The article's strongest claim, stated only from its own commitments, is this: selection-based learning over a readable store needs a robust comparison, not a single score, and a fixed-weight LLM can build the preference model from a stated purpose, make that comparison and decide the cases it leaves open.

The core claim is easy to find. The opening question sets it up, the second and third paragraphs state both halves, and the bet is bolded. The later sections clearly serve it. The worked example makes the comparison concrete. The gradient-training contrast and precedents place the bet as the step after proof and fixed formula. The Bitter Lesson section answers the main objection. The final section says how to test the bet and what would refute it. Each section returns to the bet or to the routing-line example. The article therefore passes.

The opening's shape makes the claim less memorable than it should be. The first numbered point carries a definition, two technical terms, a scope restriction, a novelty disclaimer, a historical precedent and an RL analogy. A second novelty disclaimer then splits the bolded bet from its elaboration. A reader leaves the introduction with the hedges as vivid as the claim. The simplest repair is to cut the precedent, analogy and duplicate disclaimer from the opening, because later sections already carry them, and to keep the comparison claim and the bet adjacent.

The bet also appears in two forms. The precedents section gives the sharper one, which adds the open-case decision and the double-loop label. Aligning the opening with it is a revision target. It does not show that the claim is hidden.
