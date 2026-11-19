---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Basis: the commission''s Current direction asks for ''about 650–850 words
    of body'' and a result ''substantially shorter''. The candidate report says ''The
    body is about 850 words in four sections plus `## Scope`.'' A count of the candidate
    body (opening paragraph through the Scope bullets) gives roughly 1,000 words,
    and about 900 even without Scope and headings. The report misstates the length,
    and the candidate is above the editorial target. Every paragraph carries claim-account
    content, so no necessary condition is at stake, but the operator asked for compaction
    specifically. Required change: tighten the body toward the 650–850 target without
    dropping a required qualifier. Candidates for this are the second half of the
    Source-identity paragraph (pin and current-byte detection, which claim account
    7 marks as peripheral: ''one or two sentences, or drop''), the restatement in
    the Occurrence paragraph that uniqueness does not show support (support is already
    ruled out in the four-questions section), and the closing sentences of the chain
    paragraph. Then correct the word count in the candidate report.'
  level: warn
- scope: passage
  quotes:
  - This asymmetry explains why a wording mismatch can fail rather than warn.
  reason: 'Basis: the preceding paragraph contrasts the cost and noise of wording
    checks with semantic checks. The paragraph this sentence opens gives a different
    asymmetry: from the derived-copy note, a false copy misleads silently and an absent
    one costs a recomputation (claim account 12). ''This asymmetry'' therefore points
    back to the cost contrast, while the justification that follows rests on the false-versus-absent
    contrast. A reader cannot tell which asymmetry licenses failing. Required change:
    name the asymmetry that does the work, the false-versus-absent cost from the derived-copy
    argument, or state that both are needed: wording checks are cheap enough to block,
    and a false copy is worse than an absent one.'
  level: warn
- scope: passage
  quotes:
  - no mechanism here checks that the capture faithfully represents the original or
    that the named author wrote it
  reason: The claim account says upstream authenticity stays unverified 'by any mechanism
    in scope'. 'Here' carries that scope, but readers could take it to mean 'in this
    note' or 'in Commonplace'. The meaning is still recoverable from the surrounding
    Gaps-faithful scope, so no change is required.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note-sha256: f7e9fd93f11c860de35542fd33c9298eb8a5c430c215557ea4b4314993e2d92d
criterion-sha256: 6f5d24343fe9fd8387ed345957325abbae4ecf50e222df7b992b3b1b8ef484e2
target-sha256: f7e9fd93f11c860de35542fd33c9298eb8a5c430c215557ea4b4314993e2d92d
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/94226063f497/artifact/reviews/7ed4f62970c3e38c658947b6/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/94226063f497/artifact/reviews/7ed4f62970c3e38c658947b6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/94226063f497
launch: d433c0792a8f469bb8e65f54c0fb3aa3
completed-at: '2026-11-17T14:25:07Z'
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/94226063f497/calls/launches/d433c0792a8f469bb8e65f54c0fb3aa3/outputs/review.md
raw-output-sha256: 5f229670437201a3b82c11a0401ea8768fc5c9e26c812547c8604775a5e47557
format: 2
---

# Review

The candidate makes the commissioned contribution. It is a general theory note on quote checking that separates wording, attribution, context and truth, and explains normalization as a two-sided error. It distinguishes occurrence from location, makes a pass relative to the evidence used, keeps retained, accessible and used material apart, and treats exactness as independent of second-hand provenance. Every claim traces to a claim-account commitment and to the reconstruction's support or inference. The qualifiers that the commission and claim account require are present: uniqueness does not prove intent, a pin detects change only at a later comparison, unresolved reporting does not catch missed quotations, semantic reliability is unmeasured, and ground truth must be present at check time. No commitment appears that the claim account does not give.

The delta from `start` matches the candidate report. The capture-time ceiling, "re-capture is the only remedy", the three-layer taxonomy, the locator corollary and the forced-lossy-retention argument are gone. The commission explicitly authorized dropping them even though `kb-role` lists the ceiling, re-capture and the layer vocabulary as relied on, and the report records each replacement and its dependent impact. The relied-on point that a paraphrase has no mechanical derivation rule survives in the opening paragraph. The title and H1 stay only as the reserved transition constraint. The `title-as-claim` trait is removed. The report flags the retitle for after approval and proposes a brief without adding one.

On the contracts, the note keeps `types/note.md` and has a `## Scope` section. All links are inline, and each resolves from `kb/theory/`. Each Commonplace ADR is cited at the claim it supports and is scoped where it supplies a single case ("In one casebook corpus"). No source ingest is cited, so the unquoted-source bound does not apply. The body leads with explanation, without drafting narration or repeated disclaimers.

Two findings remain, neither blocking. The body is noticeably longer than the operator's compaction target, and the report understates its length. One connective sentence points at the wrong asymmetry.
