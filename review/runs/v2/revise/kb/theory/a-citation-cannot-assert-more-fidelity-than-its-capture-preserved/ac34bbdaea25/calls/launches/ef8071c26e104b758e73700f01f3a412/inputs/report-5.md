---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/role
launch: 953f8cb4a4f24e6fbbf75627b768a1b1
completed-at: '2026-11-16T22:15:10Z'
findings:
- scope: passage
  quotes:
  - A paraphrase-layer passage has no such rule — there is no mechanical comparison
    between a paraphrase and its source, only judgment.
  reason: 'PARTLY SUPPLIED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — needs the three grounding layers and the premise that the non-verbatim markers
    (`paraphrase layer` and `second-hand`) have no derivation rule and so stay unchecked
    by construction. The note supplies the three layers and argues the no-derivation-rule
    premise for the paraphrase layer. It does not argue it for the second-hand layer.
    The note defines that layer by the intermediary that must be named, not by the
    absence of exact text: a second-hand passage can be the intermediary''s verbatim
    words. The ADR''s ''never claimed exact text'' for `second-hand` therefore rests
    on the ADR, not on the note.'
- scope: passage
  quotes:
  - A paraphrase-layer passage has no such rule — there is no mechanical comparison
    between a paraphrase and its source, only judgment.
  reason: PARTLY SUPPLIED — kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md
    — cites the note as treating 'a paraphrase-layer passage as unverifiable' and
    uses that to argue for verbatim retention of scope-bearing qualifiers. The note
    supplies the paraphrase layer, the lack of a mechanical check and the consequence
    that load-bearing passages must be promoted into the verbatim layer at capture.
    But the note says paraphrase verification 'requires going back to the authoritative
    artifact'. That makes paraphrase not mechanically checkable, not unverifiable,
    so the ingest reads the claim in a stronger sense than the note states. The direction
    of paraphrase bias is the ingest's own addition and does not depend on the note.
- scope: passage
  quotes:
  - what grade of provenance evidence a passage carries, whether the source's own
    words or somebody's restatement
  reason: PARTLY SUPPLIED — kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md
    — uses the title as a principle that a citing note cannot assert a claim stronger
    in scope than the captured body supports. Its case is a snapshot description that
    overstates an abstract-level capture. The title's wording supports this use. The
    body, however, defines fidelity as the grade of provenance evidence (verbatim,
    paraphrase or second-hand). It separates fidelity from authority and does not
    discuss the strength or scope of the claim a capture supports. The overstating
    description fits the note's paraphrase layer, but the note does not state the
    inference 'paraphrase overstates, so the citer must restate at the source's strength'.
- scope: passage
  quotes:
  - no citation syntax, no locator type, no review gate can promote a passage to a
    grade its capture did not preserve
  reason: SUPPLIED — kb/tags/claims-and-grounding-README.md — only a citation, glossed
    'capture fixes the evidence a citation can claim; stronger notation cannot restore
    lost fidelity'. The note's opening paragraph and its section 'Why notation cannot
    repair it' state exactly this.
- scope: passage
  quotes:
  - recoverable only by returning to the authoritative artifact and capturing again
  reason: 'SUPPLIED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — needs, as a premise, the capture-time bound: a passage never captured word for
    word cannot take the quoting route without returning to the source. Together with
    the no-derivation-rule argument for paraphrase and the requirement to promote
    load-bearing passages at capture or quote-mine the authoritative artifact, the
    note states this premise.'
- scope: passage
  quotes:
  - 'A verbatim-layer quote has one: substring match. A paraphrase-layer passage has
    no such rule'
  reason: 'DUPLICATED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — this dependent applies ''a derived copy of recomputable truth must be checked
    or absent'' to citation: a quote is admissible because a validator re-derives
    it, and a paraphrase has no such derivation rule. The note''s ''Why notation cannot
    repair it'' paragraph makes the same application. The dependent''s version ties
    it to the shipped validator (ADR 046, ADR 073), so it is more concrete for its
    own grounding-check argument. The note''s version is fuller as an argument: it
    adds that marking a paraphrase `verbatim` creates a forbidden hand-maintained
    copy carrying a stronger trust signal.'
- scope: passage
  quotes:
  - A paraphrase-layer passage has no such rule — there is no mechanical comparison
    between a paraphrase and its source, only judgment.
  reason: 'DUPLICATED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — the ADR passage restates in one clause the note''s argument that no derivation
    rule exists for non-verbatim layers, and defers to the note for its reason (''which
    is precisely why''). The note states the argument better for this use because
    it derives it. The ADR adds what the note lacks: the marker names and the point
    that `verbatim` is the only mechanically falsifiable marker.'
contract: report
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/role/artifact/reviews/2d5de2ad1c67342d01437815/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/role/artifact/reviews/2d5de2ad1c67342d01437815/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/role/calls/launches/953f8cb4a4f24e6fbbf75627b768a1b1/outputs/review.md
raw-output-sha256: 735575ac95c6dd660116fb76d66aa799519c879dcdcd2eea1350b6444d9248ad
---

# Role in the KB: A citation cannot assert more fidelity than its capture preserved

## Role
The note supplies two things to other KB files. The first is a premise: a citation's provenance grade is fixed at capture, and only re-capture raises it, because a non-verbatim passage has no mechanical derivation rule. The second is the verbatim / paraphrase / second-hand layering behind ADR 046's grounding-layer markers. One theory note argues from it, and the shipped ADR justifies its unchecked markers with it. Two source ingests cite it as a principle, one of them in a stronger or broader sense than the body states, and one tag head lists it.
Relied on: the title claim (capture bounds citation fidelity), the paraphrase layer's lack of a derivation rule, re-capture as the only remedy, and the three-layer vocabulary (ADR 046). Unused: the fidelity/authority distinction, the forced-constraint argument for layering (context window, copyright, provider filters, the boundary-preserving-rival link), the link to "history has one chance to become checkable", the locator corollary, the Scope section on lossless short sources, the Open Questions and the ADR 046 evidence paragraph.

## Dependents
- `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` needs the three layers and the premise that the non-verbatim layers have no derivation rule.
- `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md` needs the claim that paraphrase-layer passages are weak evidence, read as "unverifiable".
- `kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md` needs the title as a principle limiting claim strength to what the capture holds.
- `kb/tags/claims-and-grounding-README.md` needs only a citation with a gloss.
- `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` needs the capture-time bound as a premise for which sources can take the quoting route.

## Duplication
- `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` restates the note's application of the derived-copy rule to citation. It is more concrete about the shipped validator; the note gives the fuller argument.
- `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` restates the no-derivation-rule clause in brief and defers to the note for the reasoning.

## Untaken recommendations
None. The supplied passages contain no revision or add-citation recommendation addressed to this note. The Peters ingest says it is evidence for the note and that it "argues for verbatim retention of scope-bearing qualifiers". This argument concerns capture practice, and the passage does not ask for a change to the note. The ROME ingest's "Any note citing this ingest should restate the claim…" is addressed to notes that cite ROME. Only the linking passages were supplied: any recommended-next-action section elsewhere in either ingest is unseen.

## Reach
- **Title claim** (capture bounds citation fidelity; notation cannot raise it). Dependents: all five files, namely ADR 046, the Peters and ROME ingests, the claims-and-grounding tag head (whose gloss repeats it) and "A note is an atomic step…". The ROME ingest relies on the broad reading of the title rather than the body's provenance-grade definition, so narrowing the title would leave it unsupported.
- **No derivation rule for the paraphrase layer** ("Why notation cannot repair it"). Dependents: ADR 046, "A note is an atomic step…" and the Peters ingest.
- **The three-layer vocabulary** (verbatim, paraphrase layer, second-hand). Dependent: ADR 046, whose marker names follow it. The Peters ingest uses "paraphrase-layer".
- **Re-capture as the only remedy, and promotion into the verbatim layer at capture.** Dependents: "A note is an atomic step…" and, implicitly, the Peters ingest's argument for verbatim retention.
- **Definition of fidelity as provenance grade, separate from authority.** No dependent argues from the distinction. Changing it reaches the ROME ingest only through how the title is read.
- **The rest reaches no dependent:** the forced-constraint argument, the locator corollary, the Scope section, the Open Questions and the evidence paragraph.
