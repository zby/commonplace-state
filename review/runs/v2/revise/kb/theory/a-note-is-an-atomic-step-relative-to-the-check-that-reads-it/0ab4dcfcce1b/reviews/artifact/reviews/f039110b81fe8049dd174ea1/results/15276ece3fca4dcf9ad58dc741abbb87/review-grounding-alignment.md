---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - on this evidence it is not a reviewer capacity exhausted at current corpus sizes
  reason: The linked report records that the three 21-23-artifact tail cases returned
    PASS. But it also says the assay 'does not identify a general attention price'
    and that the production observation 'does not prove the tail safe'. A PASS with
    no reference outcome cannot show that no finding was lost. The note's inference
    from 'no observed loss' to 'not a reviewer capacity exhausted' goes beyond what
    the report supports, and the note does not state how the evidence transfers.
  level: warn
- scope: passage
  quotes:
  - an absence of that kind is a validator's result rather than a reviewer's finding
  reason: The validator the note cites, ADR 046, resolves verbatim-marked quotations
    that are present against their linked source. It does not detect a claim that
    lacks a retained passage. The report's two findings (missing retained support
    for HyperAgents details; ingest analysis used as evidence beyond retained Quotes)
    were found by a reviewer. ADR 046 grounds only the following counterfactual ('had
    the details been quoted... the quote would match or the note would have failed'),
    not the claim that such absences are a validator's result.
  level: warn
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old.
  reason: The quoted second precept sizes the parts to what is 'necessary for its
    adequate solution', and the note itself says 'the parts are sized to the solution'.
    The quote does not show sizing to a checker. The paragraph then makes Lamport
    the one who names the checker and calls the whole transfer an analogy, so the
    overreach is in the topic sentence only and is not load-bearing for the central
    claim.
  level: info
- scope: passage
  quotes:
  - Commonplace's own measurement that language-model verdicts disagree with themselves
    on unchanged input
  reason: This measurement has no link where it is used. The linked five-link report
    does contain it (one of five capped repeats disagreed), so it can be supported,
    but the route is left implicit.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f039110b81fe8049dd174ea1/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/f039110b81fe8049dd174ea1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:09Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-grounding-alignment.md
raw-output-sha256: a1bba43cd7eeed8455a118136bf6806809a682f6c3b32144021f7bc200b6ba13
format: 2
---

# Review

**Linked library artifacts.** The note represents its linked notes at their stated scope:

- short composable notes: co-loading under bounded context;
- warranted autonomy: domain is what an oracle can assess with the required confidence;
- the boundary of automation: dependence on verification;
- the derived-copy rule: a checked copy, or no copy;
- citation fidelity: a quote cannot exceed what capture preserved;
- the linked-note discharge note: a citing note owes representation, not re-grounding.

ADR 046 supports substring validation of verbatim quotes with failure on mismatch. ADR 073 supports retaining verbatim-only quotes in ingests. The note represents both correctly when it introduces them.

**Quoted sources.** The Lamport passages support the claims attached to them. "Depends on the sophistication of the reader" and the "slightest possibility" criterion come from the same section-3 paragraph, in the context the note gives (writing for others versus writing for oneself). "Possible, not inevitable" refers to eliminating errors, which matches the note's use. The Descartes passages occur as quoted. They support "simple and easy" links in long chains, but they size the parts to the solution, not to a checker, as the topic sentence implies.

**Retained report.** The report supports the description of the paired experiment: four uncapped-only findings after opening 6, 11, 14 and 16 artifacts, one finding about missing retained support, one about ingest analysis used as evidence, and up to 22 artifacts and 322 kB read. Two of the note's inferences from it go beyond its support. The first reads PASS outcomes on tail cases as showing reviewer capacity is not exhausted, which the report explicitly declines to conclude. The second calls absences of retained support "a validator's result", which no linked validator provides.
