---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Markers that never claimed exact wording, such as a paraphrase marker, give the
    check nothing to match.
  reason: 'PARTLY SUPPLIED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — needs the explanation of why `paraphrase layer` and `second-hand` markers stay
    unchecked by construction, which it attributes to the note''s title claim. The
    note supplies the paraphrase half: a marker that never claimed exact wording gives
    a wording check nothing to match. It does not supply the second-hand half in the
    ADR''s sense: the note says exactness and second-hand provenance are independent,
    so a second-hand quote can still be exact and checked against an intermediary''s
    extract. The body also never derives either point from a capture-fidelity bound,
    which is the link the ADR''s ''precisely why'' draws.'
- scope: passage
  quotes:
  - Marking a span as an exact quotation asserts that these words occur in a named
    source. Unchecked, that assertion rests on the author's word. A quote check makes
    it falsifiable by testing one relation
  reason: DUPLICATED — kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md
    — the ADR passage states that the `verbatim` marker is the only grounding marker
    that can be mechanically falsified and that the other markers never claimed exact
    text; the note's opening paragraph restates the same point in general terms. For
    the ADR's own use, the ADR's wording is better because it names Commonplace's
    three markers; the note's version is the general one other dependents could cite
    without the marker vocabulary.
- scope: passage
  quotes:
  - 'Semantic hops compound instead: checking a paraphrase against a paraphrase adds
    a judgment at each hop, and rewording at either hop can change the proposition.'
  reason: 'PARTLY SUPPLIED — kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md
    — the ingest says the note ''treats a paraphrase-layer passage as unverifiable''
    and builds on that premise. The note says something narrower: a paraphrase gives
    the wording check nothing to match and needs a costlier, noisier judgment of support,
    and paraphrase-of-paraphrase chains add a judgment at each hop. ''Not mechanically
    checkable'' is supplied; ''unverifiable'' is a stronger sense than the note uses.'
- scope: document
  quotes: []
  reason: 'UNTAKEN — kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md
    — the ingest presents itself as evidence for the note: LLM paraphrase of scoped
    claims is biased toward broader scope, which argues for verbatim retention of
    scope-bearing qualifiers. The passage frames this as evidence rather than an explicit
    action, but the note neither cites the ingest nor states the directional bias
    of paraphrase or the case for retaining scope-bearing qualifiers verbatim.'
- scope: passage
  quotes:
  - 'The binding stops at the capture: no mechanism here checks that the capture faithfully
    represents the original or that the named author wrote it.'
  reason: 'PARTLY SUPPLIED — kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md
    — needs the principle that a claim inheriting phrasing stronger than the captured
    body asserts more than the capture preserves, which it applies to claim strength
    and scope, not to quoted wording. The title states that principle. The body develops
    it only for exact-wording citations: a pass is relative to the compared evidence,
    and the binding stops at the capture. It does not address a paraphrased claim
    whose strength exceeds an abstract-only capture; the closest it comes is the context
    question, which it leaves to a reader and calls unmeasured.'
- scope: document
  quotes: []
  reason: 'PARTLY SUPPLIED — kb/tags/claims-and-grounding-README.md — the tag head
    glosses the note as ''capture fixes the evidence a citation can claim; stronger
    notation cannot restore lost fidelity''. The section ''Which evidence a pass is
    relative to'' supplies the first half: a pass is relative to the evidence the
    check used. No passage states the second half, that stronger notation cannot restore
    lost fidelity. The note''s own description presents it as a general account of
    quote checking, which the gloss does not convey.'
- scope: passage
  quotes:
  - Missing bytes therefore report as unverified, never as passed.
  reason: 'PARTLY SUPPLIED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — argues from the note as its premise (''grounds''): a capture-time bound decides
    which sources can take the quoting route, and a passage never captured word for
    word cannot be quoted into that route without returning to the source. The note
    supplies that a check passes only against bytes that are retained, accessible
    and bound to a recorded capture, and that missing bytes report as unverified.
    It does not state the capture-time framing directly: that how a source was captured,
    such as an excerpt or abstract-only fetch, limits which passages can be quoted
    at all, or that the remedy is returning to the source.'
- scope: passage
  quotes:
  - For an exact-wording claim, an inexpensive occurrence check can justify treating
    mismatch as failure rather than warning.
  reason: 'DUPLICATED — kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
    — the dependent''s passage states that failing a quote on mismatch is a local
    enforcement choice within the checking-cost versus reliance-risk trade-off, and
    that a paraphrase needs judgment about support rather than the wording check.
    The note states both points: mismatch as failure is a choice within that trade-off,
    and judging support is costlier and noisier. The dependent''s version is better
    for its own use because it ties the choice to Commonplace''s mechanism (ADR 046,
    ADR 073); the note''s is the general statement.'
outcome: report
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/role/artifact/reviews/52b802b194f36b6a423378f3/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/role/artifact/reviews/52b802b194f36b6a423378f3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/role
launch: 3fbaf5ec591241c483a9f8625946f02a
completed-at: '2026-11-18T16:07:44Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/role/calls/launches/3fbaf5ec591241c483a9f8625946f02a/outputs/review.md
raw-output-sha256: adf659af5bdcbd9ff1b1f1e534f3870228c96d9481428d2a5e48765adc52dc11
format: 2
---

# Role in the KB: A citation cannot assert more fidelity than its capture preserved

## Role

Dependents use the note as the principle that a citation's fidelity is bounded by what its capture preserved. It explains why only exact-wording markers can be mechanically falsified (ADR 046) and serves as a premise for the quoting route in the atomic-step note. Two source ingests cite it to bound what a claim may assert. Most cite the title claim more than the body, whose own description presents it as a general account of quote checking. The body develops the bound for exact-wording checks and leaves paraphrased claim strength largely undeveloped.
Relied on: the title claim (capture bounds citation fidelity); the claim that markers not claiming exact wording give the check nothing to match; paraphrase needs judgment of support rather than a wording check; a pass is relative to the compared evidence; missing bytes report as unverified; failing a quote on mismatch is a choice within the cost/risk trade-off. Unused: the four-question enumeration as such (attribution, truth); the normalization-rule section; occurrence versus location, uniqueness and the no-concatenation rule; checksum and name pairing for source identity; multi-read context retrieval for oversized sources; chained exact checks through intermediaries; the Scope bullets.

## Dependents

- `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` — needs the reason paraphrase and second-hand markers are unchecked by construction.
- `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md` — needs the premise that paraphrase-layer passages are unverifiable; offers bias evidence.
- `kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md` — needs the principle that a claim cannot be stronger than its capture, applied to claim scope.
- `kb/tags/claims-and-grounding-README.md` — needs a summary claim matching its gloss; tag-head citation only, with no argument from the note.
- `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` — needs the capture-time bound on which passages can take the quoting route, as a premise.

## Duplication

- ADR 046's passage and the note's opening paragraph both state that exact-wording markers are falsifiable and that paraphrase markers are not. The ADR's version is better for its readers because it names the markers.
- The atomic-step note's passage and the note both state that failure on mismatch is a choice within the checking-cost trade-off and that paraphrase needs support judgment. The dependent's version is better for its use because it is tied to Commonplace's validator.

## Untaken recommendations

- `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md` offers itself as evidence for the note: paraphrase is biased toward broader scope, which favours retaining scope-bearing qualifiers verbatim. The note does not cite it or state that point. The passage frames this as evidence, not as an explicit edit request.

## Reach

- The title claim reaches ADR 046, the ROME ingest, the claims-and-grounding tag head and the atomic-step note. The atomic-step note argues from it as a premise.
- The claim that paraphrase markers give the check nothing to match, and need support judgment instead, reaches ADR 046, the Peters & Chin-Yee ingest and the atomic-step note.
- The claims that a pass is relative to the compared evidence, that the binding stops at the capture and that missing bytes are unverified reach the atomic-step note, the ROME ingest and the tag head's gloss.
- Framing mismatch-as-failure as a choice within the cost/risk trade-off reaches the atomic-step note.
- Changing the normalization, occurrence/uniqueness, source-identity mechanics, multi-read context, intermediary-chain or Scope content reaches no dependent.
