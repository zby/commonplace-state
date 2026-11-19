---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: bdb15b9082614770b69f37ba9041d8ae
completed-at: '2026-11-16T22:39:19Z'
findings:
- scope: passage
  quotes:
  - 'also has no content until the pass is named: a step is atomic relative to a particular
    check, which is an instance of the general rule that'
  reason: 'About 60 words carrying four ideas: the pass must be named, atomicity is
    check-relative, this instantiates the oracle-domain rule (with an inline definition
    of a checker''s domain after a dash), and a second linked rule about automation
    and verification. The reader has to hold the opening claim across two link-borne
    propositions and a definition. Split after ''particular check''; give the oracle-domain
    identification and the domain definition their own sentence, and attach the automation-verification
    link to it or drop it to the footer.'
  level: warn
- scope: passage
  quotes:
  - now archived, identified when it concluded that any partition would have to be
    by claim rather than by link
  reason: 'The appositive after the dash nests a reduced relative clause (''the hazard
    [that] the review-side proposal ... identified'') whose subject is separated from
    its verb by an italic title and ''now archived'', and then adds a ''when it concluded
    that ...'' clause. Together with the preceding causal clause the sentence runs
    to about 55 words. Reorder: state the hazard, then a separate sentence such as
    ''The archived review-side proposal ... identified this hazard when it concluded
    that ...''.'
  level: warn
- scope: passage
  quotes:
  - A claim whose joint support cannot be quoted within a note the reader can still
    co-load has only the snapshot route or a split left
  reason: The subject carries a relative clause with a second embedded relative clause
    ('a note [that] the reader can still co-load') before the main verb 'has', and
    the sentence then adds two more clauses about how the split must be made. Long
    subject-verb distance plus three further ideas. Move the condition first ('If
    a claim's joint support cannot be quoted within a co-loadable note, only ... remain')
    and put the split requirement in its own sentence.
  level: warn
- scope: passage
  quotes:
  - Read as a fact about notes, it says the reviewer honoured its cap and the notes
    had put their support beyond it
  reason: 'About 50 words with four ideas: the reviewer honoured the cap, the notes
    placed support beyond it, this is what an artifact-side bound relies on, and under
    such a bound the notes would have had to split or quote. The dash-plus-''which''
    continuation and the trailing ''and under such a bound'' clause both hang off
    the first half. End the sentence at ''beyond it'' and state the two consequences
    separately.'
  level: warn
- scope: passage
  quotes:
  - whether a passage was lifted out of a qualifying context still costs a trip to
    the source, so the audit the bound buys is of the step the validator did not do,
    not of the one it cannot
  reason: The sentence that begins 'What the page re-checks' joins a dash definition,
    a semicolon clause, a causal 'so' clause and a closing contrast across about 55
    words. The final contrast relies on the reader still holding which step is which.
    Keep the support-judgment sentence, then give the source-trip limitation and its
    consequence their own sentence.
  level: warn
- scope: passage
  quotes:
  - Commonplace's own measurement that language-model verdicts disagree with themselves
    on unchanged input is the reason auditability
  reason: Under 40 words after the dash, but the subject (a noun plus a full 'that'
    complement clause) separates 'measurement' from its verb 'is', and the sentence
    opens with a 'not X but Y' contrast. Reorder so the short phrase comes first,
    e.g. 'Auditability is worth paying for because Commonplace has measured language-model
    verdicts disagreeing with themselves on unchanged input.'
  level: info
- scope: passage
  quotes:
  - persuaded him that anything within reach of knowledge could be reached that way
  reason: 'The subject is a 25-word quotation plus its citation link, so the verb
    ''had persuaded'' arrives only after the whole quotation and locator. Reordering
    keeps every word: ''He had been persuaded by "The long chains ..." ([Part II],
    verbatim) that anything within reach ...'', or introduce the quotation after a
    short lead clause.'
  level: warn
contract: verdict
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/98764cb365877fe0fbe0c8c8/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/98764cb365877fe0fbe0c8c8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/bdb15b9082614770b69f37ba9041d8ae/outputs/review-clause-packing.md
raw-output-sha256: d52bb054815b5706ede75adbfc36080c7c33e38391c7e735a5fe5e66bfe6110e
---

# Review

The note's argument is clear at paragraph level, but several sentences carry three or four ideas at once, or keep a long subject open before its verb. The worst cases are in the sections that link many notes or rely on archived and experimental evidence. In those places the author added qualifications inline instead of giving them separate sentences.

Most of the flagged sentences can be fixed by reordering or by ending the sentence at a natural boundary. None of them needs content removed. The Descartes sentence is a pure distance problem: the quotation is the grammatical subject, and the verb comes only after it. A lead clause would remove the load without changing the citation.

Sentences of about 40 words that hold one contrast (for example, the sentence comparing a fourteen-artifact verdict with a three-source verdict) were checked and not flagged.
