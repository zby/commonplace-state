---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The mark meets all four.
  reason: 'Basis: the reconstruction (C8) says source-1 meets conditions (1) through
    (3) for the mark; for (4) source-1 says only "Validator-enforced", and the Gaps
    section says no source discusses checker trustworthiness, so (4) rests on the
    commission alone. The candidate''s own Scope also says "Condition 4 has no established
    measure of checker trustworthiness." Asserting that the mark meets condition 4
    therefore claims more than the evidence gives and sits in tension with the note''s
    Scope. Required change: say that the mark meets conditions 1 to 3 and that meeting
    condition 4 depends on trusting its validator, which the note does not establish.
    Alternatively, qualify the sentence so that it does not assert condition 4 as
    met.'
  level: warn
- scope: passage
  quotes:
  - The mark is cheap and exact to check and is relied on as a stop, so frequent mechanical
    checking pays. The report is costly to rederive, has dependencies that cannot
    be enumerated, and is consumed as advice, so reuse between reruns is a decision
    about accepted risk.
  reason: 'Basis: the claim account (C6, Destination) says section D is a short synthesis
    that "must not restate" the two examples. The commission asks for a sentence-level
    redundancy pass and asks the reviewer to check compactness. These two sentences
    repeat properties already given in the two section headings ("cheap to check,
    relied on as a stop"; "costly to rerun, consumed as suggestions") and in the bodies
    of both examples, including the reuse-as-risk judgment that closes the connect-report
    section. The body is about 837 words with headings, which is above the 600–800
    target. Required change: cut this restatement. Keep only what the synthesis adds,
    namely that both cases sit on one trade-off and that assurance does not stay current
    merely because no change is known, or fold that into the end of the connect-report
    section.'
  level: warn
- scope: passage
  quotes:
  - No fixed rule rederives that result, so reviewing it semantically does not stand
    in for a missing mechanical check.
  reason: 'Basis: the claim account (C7, Scope and qualifiers) says the connect report
    is not a case where semantic review stands in for a mechanical check that is merely
    missing, because its result has no fixed rule to check against. The candidate''s
    wording can be read the other way: that a mechanical check is missing and that
    review cannot replace it. That reading reintroduces the gap the contrast is meant
    to deny. Required change: reword the sentence so that it says unambiguously that
    the report has no mechanical check to be missing. Its result can only be reviewed
    by judgment.'
  level: warn
- scope: passage
  quotes:
  - '# A derived copy of recomputable truth must be checked or absent'
  reason: The universal title no longer matches the body's trade-off claim. The commission
    keeps it as a transition constraint, and retitling is reserved to the operator.
    The report proposes a replacement title and states this mismatch, so the candidate
    needs no change here.
  level: info
- scope: document
  quotes: []
  reason: 'kb-role lists the inline-safety third class (recomputable-and-checked)
    and managed staleness for judgment content as relied on. The commission''s explicit
    authorization names neither. The report justifies dropping them: the third class
    is a form of the safe/unsafe dichotomy that the commission excludes, and managed
    staleness was part of the regime-flip argument that the commission authorizes
    removing. The report also lists the third class among the dependent corrections.
    This is noted for the operator and asks for no change to the candidate.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note-sha256: 1cf9a6bfee90f89a0bd2c48ebe8a414810f30e162639ff3de1854f0b8cc0f50e
criterion-sha256: 6f5d24343fe9fd8387ed345957325abbae4ecf50e222df7b992b3b1b8ef484e2
target-sha256: 1cf9a6bfee90f89a0bd2c48ebe8a414810f30e162639ff3de1854f0b8cc0f50e
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/f5da7e04fb2f/artifact/reviews/f22f7fb57af2bc6b36c48267/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/f5da7e04fb2f/artifact/reviews/f22f7fb57af2bc6b36c48267/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/f5da7e04fb2f
launch: e54252b8da144213ba07d0c3ff459983
completed-at: '2026-11-17T15:46:52Z'
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/f5da7e04fb2f/calls/launches/e54252b8da144213ba07d0c3ff459983/outputs/review.md
raw-output-sha256: a0535e57534a258d91a17fdf684485e9a560b217fe5bf598a5a66b8eb1528536
format: 2
---

# Review

The candidate makes the commissioned contribution. It replaces the categorical checked-or-absent argument with a qualitative cost–risk trade-off and follows the approved shape: the reuse benefit and the suppression risk, the completeness mark, the connect-report contrast, a short synthesis, four numbered conditions, and Scope. The delta from `start` matches the claim account and the report. The forbidden middle, the enforce-or-omit regime flip, guaranteed graceful degradation, the automatic-omission consequence, the three old instances, the cache maxim and the open questions are all removed, and the report gives a reason for each removal. The candidate introduces no commitment that the claim account does not give. The C2 distinction between verification and recomputation stays within one sentence. The suppression mechanism keeps its conditions: a licensed stop, a suppressed route that would find more, and overall utility as a separate question. Reactive enforcement is stated as "checked when validated", and the fallback's protection is narrowed to readers who fall back. Validator amortization is kept apart from computation amortization.

The candidate meets the contracts. Frontmatter, `## Scope` and the footer labels fit `types/note.md` and the theory collection. The tag-readme and connect-report links use `evidenced-by` phrased as bounding rather than corroborating. No tracked source is cited, so the unquoted-source bound does not apply. Condition numbering and concepts are preserved for dependents. The report lists the dependent classes that need correction and states the limit of the 30-of-38 audit.

None of the findings blocks publication. One claim overreaches the evidence: it says the mark meets condition 4. One sentence about the connect report can be misread as conceding a missing check. The synthesis section restates the examples, which the claim account asked it not to do, and cutting it would also bring the body toward the 600–800 word target.
