---
type: types/review-result.md
format: 2
description: Retained report review of kb/notes/how-do-we-value-notes.md against kb/instructions/critique-note.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 479811efa1a44ac5aae146fc4ad4658d
completed-at: '2026-11-25T05:24:46Z'
findings:
- scope: passage
  quotes:
  - 'Commonplace currently spreads note valuation across five partial lenses rather
    than one rule:'
  reason: The Current answer says what Commonplace does now, but only the answerability
    lens is an operative admission rule. Most of the other lenses come from theory
    notes that do not describe shipped practice. The linked quality-scores note says
    "At our current scale, none of this needs implementation". The linked quality-signals
    note calls itself an "Exploratory question set, not an established scoring model."
    Readers will infer that Commonplace already ranks notes by these signals. The
    note should say, for each lens, whether it is an operative check, an available
    signal that nothing consumes, or a proposal.
- scope: passage
  quotes:
  - combine structural maturity (type), review verdicts, recency, and link-strength-weighted
    inbound links
  reason: '"Combine" implies that an existing composite runs. The source notes only
    propose a composite. They leave its weighting open and leave its implementation
    deferred until connect starts struggling. Review verdicts are the only signal
    here that is actually produced. Even so, nothing uses them for ranking or retention.'
- scope: document
  quotes: []
  reason: 'The Current answer leaves out the operative value test the note itself
    names in Stakes: the root quality bar in AGENTS.md. Under that bar, a design insight
    earns a note when it changes how someone builds or operates a KB. Anything that
    fails it stays in the log. That test is the current learning-value gate at admission,
    and it is applied by authorial or reviewer judgment. Calling it a baseline scope
    rule rather than a valuation lens makes the current practice look more like a
    set of signals and less like judgment than it is.'
- scope: passage
  quotes:
  - 'looks for counterfactual effect: whether withholding or replacing a note actually
    changes search, diagnosis, decisions, or recovery.'
  reason: The linked note applies counterfactual use to claims in a working theory,
    and it warns that system use can confirm the system's own misconceptions. Under
    autonomous production, notes that autonomous runs wrote can become indispensable
    to later autonomous runs. That is the self-sealing case the source warns about.
    The lens should carry that caveat, or the closed-loop concern already raised in
    Unsettled should be extended to it.
contract: report
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/479811efa1a44ac5aae146fc4ad4658d/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/35aa89697e44143f56c16231/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/479811efa1a44ac5aae146fc4ad4658d/outputs/review.md
raw-output-sha256: b998c54c237fa4c9f3f964663d0b936fa27cf3cfcbe7e18b2f23002a85a3562a
attack-outcome: partially lands
---

# Critique: How do we value notes?

**Note:** kb/notes/how-do-we-value-notes.md
**Central commitment:** Commonplace currently values notes through five partial lenses: answerability, separating validity from value, reader update and comparative work gain, counterfactual use, and structural/curation proxies. None of them is a tested selection mechanism, so the query stays open until an explicit mechanism is adopted and validated.
**Critique mode:** description
**Attack outcome:** partially lands

## Strongest case against it

This objection comes from an operator auditing which checks actually decide note survival. It uses the KB's own idea of the operative oracle from [weakly discriminated qualities tend to be underselected](../theory/weakly-discriminated-qualities-tend-to-be-underselected.md): "The operative oracle need not match the rubric a system says it values."

The Current answer describes Commonplace's practice ("Commonplace currently spreads note valuation…"). Check each lens against what actually changes which notes survive:

- **Answerability** is operative. Collection contracts apply it at admission.
- **Validity separate from value** is a theory claim about what a loop *should* have. No shipped learning-value gate exists. The note admits this in Unsettled.
- **Reader update / comparative work gain** is a writing objective and a theory of improvement. No step checks a candidate note against the "link an existing record instead" alternative.
- **Counterfactual use** is a theory of selecting for fit. Nothing withholds or perturbs notes to observe the effect.
- **Structural and curation proxies** are proposals. [Notes need quality scores](../theory/notes-need-quality-scores-to-scale-curation.md) says "At our current scale, none of this needs implementation." [Quality signals](../theory/quality-signals-for-kb-evaluation.md) calls itself an "Exploratory question set, not an established scoring model."

So the accurate current answer is narrower than five lenses. It has three parts:

1. Answerability and validity checks (structure, grounding, critique) act as operative gates.
2. The AGENTS.md quality bar ("changes how someone builds or operates a KB"), applied by judgment, is the only learning-value test.
3. Four theory notes describe lenses that Commonplace could adopt.

Presenting proposals as current lenses commits the error that the note's own Unsettled section diagnoses: a quality looks valued in the rubric while exerting no selection pressure. A reader deciding whether autonomous production is safe would take the wrong lesson. They would conclude that note value is already partly covered by several mechanisms, when it rests on one judgment-applied bar plus validity gates.

## How the note engages it

The note partially engages the objection. Several passages concede the substance:

- Stakes calls the lenses insufficient and says the query stays open while "candidate selection relies on ad-hoc judgment rather than a tested valuation practice".
- The heading word "partial" hedges the list.
- The Unsettled bullet "Asymmetric selection pressure under autonomous production" states that validity gates check "more strongly than anything checks learning value or reader update".
- The "Cold-start selection at admission" bullet says that downstream signals do not exist at admission.

Read together, these show that the author knows the value lenses are not operative.

The Current answer itself never draws that line. Its verbs present the lenses as running practice: "asks", "grounds that test", "looks for", "combine". It also leaves the root quality bar out of the lens list, even though that bar is the one value test that actually runs. The concession lives in other sections, while the section a reader consults for "what do we do now" overstates it.

The attack does not fully land. The note never claims that a tested mechanism exists, and the query's openness depends on exactly the gap the attack identifies. The question itself and the Unsettled agenda survive; the error is confined to how the Current answer is labelled.

## Constructive findings

- Split the Current answer into the parts that actually run and the parts that are theory. The parts that run are answerability at admission, the validity gates, and the AGENTS.md quality bar, all applied by judgment. The theory parts are the comparative-work-gain test, counterfactual use, and the composite score. Label each as an operative check, an available but unused signal (review verdicts), or a proposal.
- Add the AGENTS.md quality bar ("changes how someone builds or operates a KB"; pattern recording without explanation stays in the log) as the current learning-value gate at admission. Note that judgment applies it, without any discriminating oracle. This lets the asymmetric-pressure bullet point at a concrete weak oracle.
- Change "combine" in the proxies lens to "propose combining". Also note that weighting is open and implementation is deferred until connect struggles, as both sources say.
- Attach the self-confirmation caveat from the system-use note to the counterfactual-use lens. Autonomously written notes that become indispensable to later autonomous runs are the case where that caveat matters most.

## Secondary objections (optional)

- **The urgency premise is unevidenced.** Stakes says the question "becomes urgent as autonomous production increases note volume," but it cites no volume growth or clutter incident. The quality-scores note puts the need for ranking off until connect visibly degrades. A YAGNI-minded maintainer would say this query should cite an observed signal of growing clutter, or state the threshold at which it becomes urgent. This is partly answered because the link to maintenance capacity supplies the mechanism, though not the observation.
- **Per-note valuation may be the wrong unit.** The comparative-work-gain lens already treats value as relative to an alternative action, such as adding a note versus adding a link. Value is then a property of a change against a portfolio, not of a note. On that view, the retirement condition ("adopts and validates an explicit selection mechanism") may never be met in note-scoring form. The query could say whether it expects a per-note score or a per-change comparison. The "Combining dimensions" bullet touches this but does not choose between the two.
