---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Commonplace currently spreads note valuation across five partial lenses rather
    than one rule
  reason: 'DOUBTFUL — Premise (unmodalized, so read as a description of current practice):
    the five lenses are how Commonplace currently values notes. — Several lenses are
    theory or brainstorm, not operating selection. The linked quality-scores note
    says "At our current scale, none of this needs implementation". The quality-signals
    note calls itself an "Exploratory question set, not an established scoring model".
    Counterfactual system use is framed as an initial selection environment, not a
    running check. The answer therefore lists available theory and calls it the current
    valuation practice. The repair is to separate operating lenses (answerability
    at admission, review gates) from proposed ones, which keeps the query. — LOCAL
    — instance'
- scope: passage
  quotes:
  - Inbound links and counterfactual system use only become observable after a note
    has been retained and used. Autonomous production needs a way to filter, quarantine,
    or trial new candidates before those downstream signals exist.
  reason: 'DOUBTFUL — Premise: no available signal can select candidates at admission,
    before downstream signals exist. — The note''s own first three lenses apply before
    retention. Answerability, the validity and learning-value gates, and the warranted-reader-update
    test with its comparison against a cheaper alternative such as adding a link all
    judge an unretained candidate. The gap must be that these admission lenses discriminate
    weakly or are not run as selection, not that no pre-retention signal exists. As
    written, the bullet contradicts the Current answer. Stating the weakness keeps
    the open question. — LOCAL — instance'
- scope: passage
  quotes:
  - We have no established way to represent query-centered root notes or propagate
    value from them down through answering notes and their subroutines.
  reason: 'DOUBTFUL — Premise: Commonplace has no way to represent query-centered
    root notes. — This note is a counterexample. Its description calls it a "Standing
    query", and it is a query-centered root with Stakes, Current answer and Unsettled
    sections. Representation exists at least as a prototype. The unsolved part is
    value propagation and the standing of a root as a demand signal. Narrowing the
    bullet to propagation keeps its point. — LOCAL — instance'
- scope: passage
  quotes:
  - Structural validation, source grounding, and critique gates check validity more
    strongly than anything checks learning value or reader update.
  reason: 'DOUBTFUL — Premise (unmodalized comparative): no check exercises learning
    value as strongly as validity checks exercise validity. — The supplied review-result
    contract lists a role report, with reasons such as DUPLICATED and NOT SUPPLIED,
    that checks dependents and duplication. Those are learning-value dimensions: redundancy
    and whether a note serves a need. Critique also attacks a note''s contribution,
    not only its coherence. The premise may still hold as a tendency, because report
    methods give no verdict and do not gate acceptance. But "anything" overstates
    it, and the repair is to say that value checks do not gate acceptance. — LOCAL
    — instance'
- scope: passage
  quotes:
  - Every retained artifact adds maintenance, navigation, and exposure cost
  reason: 'DOUBTFUL — Premise (universal): every retained artifact adds cost, so volume
    drives the clutter risk. — The linked maintenance-capacity note says gross generation
    volume is "only a proxy". It says load comes from defect incidence, expected harm,
    exposure time and detection latency, not from volume itself. A well-formed, unexposed,
    quarantined or unindexed note adds near-zero navigation or exposure cost. Valid
    but low-value clutter counts as harmful inflow only when it degrades retrieval
    or link trust. The stakes survive if the clutter path is stated, such as retrieval
    dilution or link-credibility erosion. — LOCAL — instance'
- scope: passage
  quotes:
  - it would narrow or retire once Commonplace adopts and validates an explicit selection
    mechanism
  reason: 'DOUBTFUL — Unstated premise behind the retirement condition: an explicit,
    validatable selection mechanism exists and would beat ad-hoc judgment. — The note''s
    own last Unsettled bullet doubts this: "we do not yet know ... when a coarse triage
    check outperforms a composite score". The quality-signals note''s Goodhart caveat
    adds that any composite stays a soft oracle. If calibrated reviewer judgment turns
    out to be the best practice, the retirement condition is never met, although the
    question would be answered. The condition should also allow retirement when ad-hoc
    judgment is shown adequate or its limits are characterized. — LOCAL — instance'
- scope: passage
  quotes:
  - Under the conjecture that [weakly discriminated qualities tend to be underselected](../theory/weakly-discriminated-qualities-tend-to-be-underselected.md),
    an autonomous authoring loop can enrich accepted notes more strongly for validity
    than for usefulness, and if production favors fluent local additions, clutter
    can accumulate.
  reason: 'HOLDS — Premise (conditional, conjectural): unequal discrimination yields
    unequal enrichment, and accumulation needs an added directional mechanism. — This
    matches the linked note''s statistical-conjecture mode. That note says absolute
    degradation needs an adverse directional mechanism, and "production favors fluent
    local additions" supplies one as a stated condition. The hunt found no overreach.'
- scope: passage
  quotes:
  - Those goals decide what a collection admits in principle, but they do not exhaust
    how to rank, keep, or reject candidate notes.
  reason: 'HOLDS — Premise: collection scope and quality bars set admission but not
    ranking or retention among admissible notes. — The answerability definition excludes
    mere usefulness from admission, so admission criteria are silent on relative value.
    Two admissible notes can be equally answerable and differ in reach or redundancy.
    No counterexample was found.'
- scope: passage
  quotes:
  - a top-level note that answers a live question can look orphaned if no other claim
    cites it
  reason: 'HOLDS — Premise: inbound-link signals undercount notes whose demand comes
    from inquiry rather than from other notes. — The quality-scores note''s own open
    question about new notes scoring low with no inbound links, and its exploration-slice
    fix, confirm that link-count ranking starves notes without citing neighbours.
    No counterexample was found.'
outcome: report
description: Retained report review of kb/notes/how-do-we-value-notes.md against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/e0e6ffdc4814456daf5eb115c92c73b1/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/2c944e6c30750722f4f62810/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: e0e6ffdc4814456daf5eb115c92c73b1
completed-at: '2026-11-25T05:24:50Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/e0e6ffdc4814456daf5eb115c92c73b1/outputs/review.md
raw-output-sha256: 6d10bbe9a7599afc75583ded12ff9de2ba58b8a5ce7e6f8135ccac461411b96a
format: 2
---

# Premise decomposition: How do we value notes?

**Register:** claim
**Central commitment (one sentence):** Commonplace values notes only through several partial lenses with no tested selection practice, and this gap matters because autonomous production can accumulate valid but low-value notes faster than curation can keep up.

## Premises and counterexamples

The note is a standing query, so its commitment has a descriptive half and a stakes half. The descriptive half says what Commonplace does now and what is unsettled. The stakes half says why the gap matters under autonomous production.

The descriptive half consumes four premises:

- the five lenses are current practice;
- admission criteria do not settle ranking;
- downstream signals are unavailable at admission;
- query roots cannot be represented.

The stakes half consumes three:

- each retained artifact adds cost;
- validity is selected more strongly than value;
- a validated explicit mechanism is the right retirement target, which is an unstated premise.

No premise failure is global. Each one is repaired by narrowing a sentence or marking it as proposed rather than operating, and the open question survives every repair. The failures share one pattern: the note treats KB theory about valuation as if it were operating practice. In two places it then contradicts itself. The cold-start bullet ignores the admission-time lenses the note just listed. The representation bullet is undercut by the note's own existence as a standing-query root. Premises stated with conjectural or conditional modality, such as underselection, survive.

## For the human

Look first at the "Current answer" framing. Several lenses are proposals or brainstorms, not operating selection. Separating operating lenses from proposed ones also resolves the cold-start contradiction.
