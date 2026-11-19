---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The layering is not a design choice
  reason: 'UNSUPPORTED — The linked rival test cuts one way only: it can demote a
    rule to a design choice, but its note says that finding no rival ''certifies nothing''
    and that certifying inheritance needs a positive derivation from independently
    stated invariants. The note offers no such derivation. It only asserts that no
    rival exists and does not name the ''commitments the framework has already made''.
    The forcing reasons given (a finite context window and copyright trims) also explain
    only why capture of long sources is lossy. They do not force the three-layer structure,
    and they cannot force the second-hand layer, which is a property of the source
    (a court restating a complaint), not a capture constraint.'
- scope: passage
  quotes:
  - Two spans at the same file offset can differ in provenance quality by a full layer
  reason: UNSUPPORTED — The note never says which file the offset indexes. If the
    offset indexes the snapshot, the verbatim block and the paraphrase summary occupy
    different offsets, and a position-only locator already distinguishes them whenever
    the snapshot marks its layer regions. If the offset indexes the original source,
    the corollary is about locator target rather than layer. In either reading the
    'it follows' does not establish that position cannot carry the layer. It establishes
    only that position must be resolved against a layer-marked snapshot.
- scope: passage
  quotes:
  - The one chance here is ingest, and what was not preserved verbatim then is permanently
    downgraded
  reason: UNSUPPORTED — The same sentence says the downgrade is 'recoverable only
    by returning to the authoritative artifact and capturing again', so the chance
    is not single and the downgrade is not permanent while the authoritative artifact
    survives. The linked note concerns production history, which cannot be re-derived
    after the fact. Its own boundaries say that a snapshot stays re-checkable against
    its source until the source changes. Citation fidelity therefore looks like the
    re-capturable complement of that rule, not an instance of it. The claimed instance
    relation is unearned, and the note's own 'non-increasing' framing depends on treating
    re-capture as outside 'downstream'.
- scope: passage
  quotes:
  - it produces precisely the hand-maintained-and-trusted copy that rule forbids
  reason: 'THIN — A `verbatim` mark is itself a checkable claim with a mechanical
    rule (substring match), and the note''s own evidence says ADR 046 checks it. A
    paraphrase wrongly marked `verbatim` is therefore a checked copy that fails, not
    a hand-maintained-and-trusted one. The linked rule also puts natural-language
    summaries outside the recomputable regime altogether, so ''precisely'' overstates
    the fit. The conclusion that notation cannot raise fidelity may still hold, but
    the mechanism offered for it is misidentified. The step from ''no notation'' to
    ''no review gate'' is also unargued: a gate that consults the authoritative artifact
    is hard to tell apart from the re-capture the note allows.'
- scope: passage
  quotes:
  - The claim bites exactly where capture is lossy, which is to say wherever the sources
    are long.
  reason: 'THIN — The scope argument covers only the verbatim/paraphrase split. The
    second-hand layer does not depend on length: a short tweet or news snippet that
    restates an order can be captured losslessly and still be second-hand. ''Exactly
    ... wherever the sources are long'' therefore misstates where the bound applies,
    and the ''layers collapse to one'' premise holds for only two of the three layers.'
outcome: report
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/6264896e219b6062d7a5ea0a/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/6264896e219b6062d7a5ea0a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 41006f894a4042158b442da4f1590777
completed-at: '2026-11-16T22:11:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/41006f894a4042158b442da4f1590777/outputs/review.md
raw-output-sha256: 1f8925615cfa28ef644aa5827f70ec52422076c02045ff865dbe8f079b1baf6c
format: 2
---

# Friction check: A citation cannot assert more fidelity than its capture preserved

**Central claim (one sentence):** A citation's provenance fidelity is capped by the capture layer (verbatim, paraphrase or second-hand) that holds the cited passage, and only re-capture from the authoritative artifact, not downstream notation, can raise that cap.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent thing if re-capture counts as a new ingest rather than a downstream operation. Under that reading, "fixed at ingest", "non-increasing downstream" and "only re-capture raises it" can coexist. Tension appears in the wording, not in the commitment: "permanently downgraded" and "decided before any note is written" sit beside a remedy that lets an author quote-mine the authoritative artifact later. The author should make the ingest/re-capture boundary explicit, but the claim does not split into incompatible parts.

## Thinnest joints

The opening of the "Capture is layered" section ranks thinnest. It asserts that the layering is inherited by citing a test whose own note says it cannot certify inheritance, and its forcing reasons do not reach the second-hand layer. The locator corollary ranks next. It is presented as following from the main claim, but it rests on an unspecified offset whose most natural reading, a snapshot offset, would already separate the layers. The "one chance" instance ranks third because the note's own remedy (re-capture) contradicts it, and the linked note's boundaries point the other way.

The notation-cannot-repair joint is stronger: its conclusion is plausible, but its stated mechanism conflicts with the shipped checker the note cites as evidence. The scope joint is the strongest of the five. Only its wording overreaches by ignoring how the second-hand layer arises.

The evidence paragraph (eighteen of eighty-seven `verbatim`-marked spans failed to match) shows that naive marking fails. It does not show that those failures came from paraphrase-layer passages, or that the layering is forced, so it supports only the weaker half of the note.

## For the human
Look first at "The layering is not a design choice": either supply the positive derivation that the linked rival test says it cannot provide, or weaken the claim to "undemoted", and say separately where the second-hand layer comes from.
