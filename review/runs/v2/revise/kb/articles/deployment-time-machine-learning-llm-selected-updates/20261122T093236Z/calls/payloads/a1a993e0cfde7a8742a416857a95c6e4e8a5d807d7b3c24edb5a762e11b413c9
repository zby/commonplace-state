---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/composition-friction-gate.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 1e87180034c04441b0fdfe66216fa57b
completed-at: '2026-11-22T09:37:33Z'
findings:
- scope: passage
  quotes:
  - If selection-based learning over readable stores is not new, why did earlier AI
    systems not turn it into a general machine learning paradigm?
  reason: 'UNSUPPORTED — The section poses this question and then answers it only
    implicitly: proof, fixed formula and human-corrected heuristics each failed as
    the judge, so a language-model judge is the missing piece. It never argues that
    the judge was the bottleneck. The note itself later names credit assignment without
    a chain rule as "the hard problem" and weak proposals as a hazard the bet does
    not address. Either could equally explain why earlier systems stayed niche. If
    the judge was not the binding constraint, the bet''s framing as the step that
    turns an old process into a paradigm loses its ground.'
- scope: passage
  quotes:
  - Third, no single scalar metric had to be invented to compare saved misfilings
    against diffuse context load.
  reason: UNSUPPORTED — The routing-line sequence is introduced with "Suppose". A
    constructed scenario can illustrate a claim but cannot "establish" it. The judge's
    choice of the trial is narrated, not derived. The text never shows that the trial
    wins under every compatible weighting of misfilings against context load. Without
    that, the example does not show that no scalar was used; a judge picking by an
    unstated weighting would produce the same narrative. The joint carries weight
    because later sections cite this example as their worked case.
- scope: passage
  quotes:
  - Keeping the routing line for good may be open, while trying it with a cheap way
    back can be better under every compatible measure.
  reason: THIN — The move that turns an open comparison into a robust one by changing
    the alternative is asserted, not shown. A trial still pays the context cost during
    the trial and adds a scheduled review. A compatible measure that weights diffuse
    context load heavily and routing errors lightly can therefore still prefer leaving
    the file alone. The trial is robustly better only if such measures are excluded,
    and the note does not say what excludes them. If they are not excluded, the example's
    selection is a decision on an open comparison, not a robust one. The hedge "can
    be" keeps the sentence true but leaves the worked example unsupported.
- scope: passage
  quotes:
  - Once a language model supplies the comparison inside an automated selection loop,
    the system sits on the computation side of the Bitter Lesson.
  reason: THIN — The production-method reading licenses this categorization only if
    the retained content is produced by search and learning rather than supplied by
    people. Here the preference model is derived from a human-declared purpose, and
    the starting instructions and gates are hand-written. The sentence makes the placement
    categorical. The bootstrap condition is attached only two paragraphs later, and
    the note concedes that whether additional compute pays "is open". The joint establishes
    that compute can be spent, not that the system's results scale with it, which
    is what being on the Bitter Lesson's winning side means.
- scope: passage
  quotes:
  - A model that approves a change and then approves its reversal on the same evidence
    is equivalent to no set of value functions
  reason: 'THIN — The equivalence holds for robust (necessary) preference: no nonempty
    set can make both a change and its reversal strictly better. The note, however,
    also lets the judge "decide the cases it leaves open" as bounded decisions. Approving
    a change, and later its reversal, on an open comparison is consistent with a set
    whose functions disagree. As stated, the test conflates approval with robust preference.
    A consistency check built on it would either flag legitimate open-case decisions
    or need a distinction the note does not draw.'
contract: report
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/1e87180034c04441b0fdfe66216fa57b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/a8f037747552408de44be43b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/1e87180034c04441b0fdfe66216fa57b/outputs/review.md
raw-output-sha256: a5bef5426300578066dc86b4838bc48199fc73abc0e08fc9275f7f5cfb44a305
---

# Friction check: Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

**Central claim (one sentence):** A deployed agent can learn by selecting edits to its readable instruction store through a robust comparison over a preference model instead of a single score, and the bet is that a fixed-weight LLM can autonomously build that preference model from a stated purpose, make the comparison, and revise its own criteria.

## Filter
**Filter:** SURVIVES

The properties the claim holds at once are: no single scalar, robust comparison (every compatible function agrees), an LLM that supplies reasons rather than computing over value functions, decisions on cases the comparison leaves open, and criterion revision under a fixed objective. These come close to colliding. With no stated preferences the note admits that robust comparison "leaves most real changes unordered". Open-ended objections can also widen the set, so much of the actual selection falls to decisions on open comparisons, not robust ones. The note avoids contradiction by keeping these decisions explicitly separate from improvement claims and making them reversible. It also does not claim that open-case decisions use no weighting, only that they are not reported as improvements. The claim therefore commits to one consistent thing. Its practical content, though, rests more on the open-case decision procedure than the title's "without a single score" suggests.

## Thinnest joints

The top joint is ranked first because it frames the whole bet: the article presents the judge as what turns an old process into a paradigm, but it never argues that the judge was the binding constraint, and its own limits section points elsewhere. The second and third joints are paired. The worked example is offered as establishing that no scalar was needed, but the robustness of the trial over leaving the file alone is the step that would make that true, and it is asserted, not traced. The Bitter Lesson placement is next: its categorical wording outruns the conditions the note attaches afterwards. The consistency test ranks lowest. Its logic is sound for strict robust preference and fails only through the conflation with open-case approval, which a short distinction would repair. The source-diagnosis passage about the harness-evolution study was considered but not surfaced. It is hedged enough ("though their single remedy run stayed within noise") that it does not bear the weight of a rebuttal.

## For the human
Look first at whether the routing-line trial is actually better than no change under every compatible measure. If it is not, the article's only worked case shows a decision on an open comparison, not the robust selection the title promises.
