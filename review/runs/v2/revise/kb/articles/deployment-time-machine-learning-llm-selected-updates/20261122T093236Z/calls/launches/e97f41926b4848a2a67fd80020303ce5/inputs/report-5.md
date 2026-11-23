---
type: types/review-result.md
format: 2
description: Retained report review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
note-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 86d5c3082fa3fb82afab97a45faf7c7ae3265ce3a43ae7791051657759ca54bd
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/role
launch: 1a25dc8d46a74658adc58447149e5b5b
completed-at: '2026-11-22T09:41:59Z'
findings:
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/articles/README.md — the index entry needs three things from
    the note: the question whether a deployed agent can use an LLM to select revisions
    to its own instructions without a single score; the distinction between the decision
    to try an edit and evidence that the edit improved later work; and the statement
    that no end-to-end automated run is reported. The opening paragraph poses the
    question, the routing-line walkthrough and the section on whether a change improved
    the system draw the decision/evidence distinction ("Letting a change stand while
    its verdict is open is a decision, not a demonstrated gain"), and the evidence
    paragraph reports no completed end-to-end automated run. The three are spread
    across the note, so no single span carries them.'
- scope: passage
  quotes:
  - derive the preference model from the declared purpose of the work, make the robust
    comparison
  - for work where no fixed criterion is adequate
  reason: 'SUPPLIED — kb/articles/testing-autonomous-selection-based-learning.md —
    its framing paragraph needs the note''s central claim: a fixed-weight language
    model could serve as the judge where no fixed test is adequate, using a robust
    comparison in place of a single value function. The note''s bet paragraph in the
    proof/formula/judgment section states exactly this. The dependent says ''could
    serve'' and the note calls it a bet, so the two agree on its untested status.
    The dependent''s ''edits to a readable, addressable store'' matches the note''s
    chosen case.'
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/articles/testing-autonomous-selection-based-learning.md —
    its link list describes the note as ''the lead article stating the paradigm, the
    weight-training contrast, and the Bitter Lesson argument''. The note has a section
    for each: the two-claim opening plus the selection-versus-gradient section, the
    comparison table, and ''Compatible with the Bitter Lesson''.'
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/index.md — the ''Central thesis'' entry needs the note to
    argue that selection-based learning needs a comparison but not a single score,
    and that a fixed-weight LLM can supply that comparison in a way compatible with
    the Bitter Lesson. It also needs the note to rest on the selection-based learning
    definition and the necessary-preference note. The note states the first claim
    in its opening (''needs a comparison, not a single score'') and the second as
    its ''empirical bet''. The Bitter Lesson section gives the compatibility argument,
    and both grounding notes are linked and listed in source_notes. One difference
    in framing: the index says the note ''argues that'' an LLM can supply the comparison.
    The note presents that claim as an untested bet. It makes Bitter Lesson fit conditional
    on automated learning outgrowing the hand-written bootstrap, and it leaves open
    whether added compute pays off.'
- scope: passage
  quotes:
  - that a fixed-weight language model can do that work autonomously
  reason: SUPPLIED — kb/tags/improvement-loop-README.md — the tag head needs the note
    to argue Commonplace's bet that a fixed-weight language model can do the selecting
    unaided, and to mark the bet as untested. The note states the bet here and in
    'the software alone can, given a stated purpose'. Its evidence paragraph reports
    no completed end-to-end automated run, which supplies 'untested so far'.
contract: report
target-sha256: de65ef3cbd7be2cb00fa46f642e6503d8dfefba806d94d3bfe93e40172e0ee07
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/role/calls/launches/1a25dc8d46a74658adc58447149e5b5b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/role/artifact/reviews/4545d124deff92579e4a8284/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/role/calls/launches/1a25dc8d46a74658adc58447149e5b5b/outputs/review.md
raw-output-sha256: 8e7b57dd6e994896af73729889e0fb14b655e174aea4fd7ad7ff69160e220d80
---

# Role in the KB: Deployment-Time Machine Learning: LLM-Selected Updates Without a Single Score

## Role
The note is the KB's lead statement of its central thesis. Selection-based learning needs a comparison, not a single score. The bet is that a fixed-weight LLM can build the preference model and make the robust comparison, autonomously and where no fixed criterion is adequate. The front-door indexes (`kb/index.md`, `kb/articles/README.md`), the improvement-loop tag head and the companion testing article all cite it as the place where this thesis and its untested status are argued. No dependent argues from the note's internal steps; they cite its headline claims and its evidence status.
Relied on: the title; the "comparison, not a single score" claim; the fixed-weight-LLM bet (preference model, robust comparison, no fixed criterion adequate); the "no completed end-to-end automated run" status; the distinction between deciding to try an edit and showing that it improved later work; the existence of a weight-training contrast and a Bitter Lesson argument; draft status. Unused: the Gödel machine, PRODIGY and EURISKO precedents; the stochastic-dominance and Greco et al. exposition of preference models and its analogy limit; the routing-line walkthrough as such; the consistency/cycle test; the two-part empirical check (operative dependence, robust improvement); the five hazards; the Sutton interview and the harness-ceiling study; the cost ledger and the inspectability caveats.

## Dependents
- `kb/articles/README.md` — index summary: the question, the decision/evidence distinction, and the absence of an end-to-end run.
- `kb/articles/testing-autonomous-selection-based-learning.md` — framing premise (the LLM as judge using a robust comparison where no fixed test is adequate) and a link-list description (paradigm, weight-training contrast, Bitter Lesson argument).
- `kb/index.md` — the "Central thesis" entry: the comparison-not-score claim, the LLM-can-supply-it claim, Bitter Lesson compatibility, its grounding notes, and draft status.
- `kb/tags/improvement-loop-README.md` — citation for Commonplace's bet that a fixed-weight LLM can select unaided, and for its untested status.

## Duplication
None beyond pointer summaries. Each dependent paraphrases the note's thesis in one or two sentences as a pointer and defers to the note for the argument. In the visible passages no dependent restates the argument itself. The testing article's body probably overlaps the note's two-part empirical check and its "open comparison" discussion, but only the two linking passages were supplied. Any such overlap is unseen.

## Untaken recommendations
None. No linking passage recommends a change to the note.

## Reach
- **The fixed-weight-LLM bet** (it builds the preference model from a stated purpose, makes the robust comparison and decides open cases, where no fixed criterion is adequate) reaches all four dependents: `kb/index.md`, `kb/articles/README.md`, `kb/tags/improvement-loop-README.md`, `kb/articles/testing-autonomous-selection-based-learning.md`.
- **"Needs a comparison, not a single score"** and the title's "Without a Single Score" reach `kb/index.md` and `kb/articles/README.md`. The title is also quoted as link text in `kb/articles/testing-autonomous-selection-based-learning.md`.
- **The evidence status** ("no completed end-to-end automated run") reaches `kb/articles/README.md` and `kb/tags/improvement-loop-README.md` ("untested so far").
- **The decision-to-try versus evidence-of-improvement distinction** reaches `kb/articles/README.md`.
- **The weight-training contrast and the Bitter Lesson argument** reach `kb/articles/testing-autonomous-selection-based-learning.md` (link list) and `kb/index.md` (Bitter Lesson compatibility). A change to the Bitter Lesson section's conditions would also affect how accurate the index's unconditional wording is.
- **The note's grounding** in the selection-based learning definition and the necessary-preference note reaches `kb/index.md`.
- **Draft status** reaches `kb/index.md` ("(draft)").
- The historical precedents, the decision-analysis exposition, the consistency test, the empirical-check structure, the hazards list and the cited 2026 studies reach no dependent.
