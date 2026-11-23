---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: 3125329d200797e278a80b8df53efc9ed3ffadd480bb72147866bd06e20dfd11
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: fail
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews
launch: 59a27bb0c8874f0eb150c9b50d4e9333
completed-at: '2026-11-22T09:36:21Z'
findings:
- scope: passage
  quotes:
  - only while a fixed utility formula estimated positive time saved
  reason: 'The PRODIGY paragraph carries evidential weight through an unquoted link
    to kb/sources/minton-utility-of-ebl-aaai88.ingest.md (no snapshot-required marker).
    It makes specific claims about the source: a 1988 working learner, retention of
    search-control rules while a fixed utility formula estimated positive time saved,
    estimates updated from later use, and rules dropped when the estimate turned negative.
    The ingest''s Quotes section reads ''No source quotes have been retained yet'',
    so the retained extracts give no material on which to judge this use. Material
    support is absent.'
  level: fail
- scope: passage
  quotes:
  - own diagnosis attributed the stall to what the proposer was not shown
  - the whole harness gain came from editing a natural-language lessons
  reason: 'The Harness Evolution paragraph reports specific findings from kb/sources/harness-evolution-ceiling-weight-training.ingest.md
    through an unquoted link: the loop stalled and deferred hard failures to weight
    training, the authors attributed the stall to information withheld from the proposer,
    a scorer saw a failure mode in a quarter of runs, a single remedy run stayed within
    noise, and on one model line the whole gain came from a lessons file. The ingest''s
    Quotes section reads ''No source quotes have been retained yet'', so none of these
    claims can be judged against retained source material. Material support is absent.'
  level: fail
- scope: passage
  quotes:
  - A heuristic could gain credit by influencing how credit was awarded
  reason: 'The EURISKO ingest''s retained quotes support the H12'' episode: elimination
    of the bad heuristic, synthesis of heuristics that would have prevented its survival,
    a restriction against replacing AND by OR, and permanent retention of one of them.
    They contain nothing on Lenat correcting judgments of worth or on a heuristic
    gaining credit by influencing how credit was awarded. The note uses this second
    episode to establish the limit of EURISKO''s double-loop capability. That claim
    has no retained source support. The ''early-1980s'' dating is also unsupported
    by the quotes, though it is not load-bearing.'
  level: fail
- scope: passage
  quotes:
  - a plausible written rule need not be what actually drove the model's behavior
  reason: 'The linked note''s claim concerns rationale for revising an addressable
    theory: a recorded explanation of why a rule holds may be unfaithful to the theory''s
    actual basis and so misdirect repair. The article invokes it for a different relation:
    whether a written rule is what causally drove the model''s behavior. The target
    mentions that self-evolving agents'' behavior is often not causally grounded in
    the artifacts they claim to use, so a link exists. But the article does not state
    the step from ''rationale unfaithful to the theory''s basis'' to ''written rule
    not causally operative''. The transfer is plausible but not articulated.'
  level: warn
- scope: passage
  quotes:
  - he and Khurram Javed argue that forming new concepts requires continual weight
    updating
  reason: This attribution rests on an external podcast link rather than the tracked
    ingest the KB holds for this interview. The linked library note on the Bitter
    Lesson does represent the interview as treating continued weight updating as necessary
    for new concepts, so the attribution is consistent with KB material. However,
    the evidential link itself goes outside kb/sources/ and could not be read within
    this review's scope.
  level: info
contract: verdict
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/artifact/reviews/4f37402aafd7ffcfb09a650a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/reviews/calls/launches/59a27bb0c8874f0eb150c9b50d4e9333/outputs/review-grounding-alignment.md
raw-output-sha256: 98fe6783649efee788b29437e904acbc948e200b8590a00698cb0d364988856d
---

# Review

## Summary

Most library links are represented at the scope their targets claim. This applies to the deployed-system unit of learning, deployment-time lifecycle versus speed, affordable inspection, the Gödel machine's proof-gated admission and utility rewriting, necessary preference and its strictness relative to Greco et al., reversibility and the trial-versus-as-proposed distinction, proxy revision under a fixed objective, operative change, false-positive acceptance, the production-method reading of the Bitter Lesson and the bootstrap condition. The AlphaGo Zero and AlphaZero contrast matches the retained AlphaZero quote. The Greco et al. account of preference models, necessary and possible relations, the weak-dominance baseline and narrowing by stated comparisons matches the retained abstract.

The failure comes from the historical-precedent and empirical-rival paragraphs. Two ingests used as evidence, Minton and Harness Evolution, retain no quotes. The gate's rule is explicit: with no retained extracts, the use cannot be judged and the result is FAIL. The EURISKO paragraph also makes a second claim that its retained quotes do not cover. That claim, about credit hijacking and Lenat's correction, sets the limit of EURISKO's double-loop capability.

The faithfulness link is a modest transfer from rationale faithfulness to causal operativity of a written rule. The note should state that step.
