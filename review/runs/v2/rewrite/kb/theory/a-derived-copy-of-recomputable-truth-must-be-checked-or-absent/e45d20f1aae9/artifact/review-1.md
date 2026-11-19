---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: 4101fdddf38fcdf94fdf1ef44b927edb69b71aae479a1d742ba2239f51a73b44
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
criterion-sha256: 6f5d24343fe9fd8387ed345957325abbae4ecf50e222df7b992b3b1b8ef484e2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/1b728b6842ec
launch: 5f562484d9b94a19aba2f0222f374bbb
completed-at: '2026-11-17T15:54:50Z'
findings:
- scope: passage
  quotes:
  - Re-running the sweep on every read would remove the saving. Instead the mark has
    a deterministic check
  reason: 'Basis: The commission''s intended contribution is that checking frequency
    depends on check cost relative to reliance risk, and claim account §2 and §5 say
    the mark example should show this: re-running the sweep on every read would defeat
    the saving, while the validator re-derives the same membership at validation time
    (reconstruction E, Inference 2 and 4). In the candidate, ''Instead'' sets the
    per-read sweep against ''a deterministic check'' as if they were different mechanisms.
    The reader is not told that the check is the same derivation, which keeps the
    saving only because it runs when the head is validated rather than on every read.
    That frequency is exactly what the note''s central claim is about, and the reader
    has to infer it from the later ''Enforcement is reactive'' sentence. Required
    change: say directly that the validator performs the same derivation at validation
    time, not on each read, so the example shows a choice of check frequency. Without
    that, the ''Instead'' contrast reads as if a cheaper check replaced the sweep.'
  level: warn
- scope: passage
  quotes:
  - '# A derived copy of recomputable truth must be checked or absent'
  reason: The title and H1 still state the categorical rule, which the body no longer
    supports and the claim account says the body must not support. The commission
    reserves this decision and requires the title to be kept for now as a transition
    constraint, and the report proposes a replacement title. No change is asked of
    the candidate. The operator should decide the retitle together with publication,
    because the `title-as-claim` trait makes the mismatch visible to readers who cite
    the note.
  level: info
- scope: document
  quotes: []
  reason: kb-role lists the 'inline-safety third class' (recomputable-and-checked,
    between arbitrary and situational) as relied on by the context-engineering tag
    head. The candidate drops it. The commission's explicit narrowing list does not
    name it. However, the commission's direction to replace the old categorical argument
    with the approved shape covers it, because the third class presents enforcement
    as the general resolution. The report records the omission and flags it for dependent
    correction, so no change to the candidate is needed.
  level: info
contract: verdict
target-sha256: 4101fdddf38fcdf94fdf1ef44b927edb69b71aae479a1d742ba2239f51a73b44
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/1b728b6842ec/artifact/reviews/b47f9ab00b73d470df213b7d/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/1b728b6842ec/artifact/reviews/b47f9ab00b73d470df213b7d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/1b728b6842ec/calls/launches/5f562484d9b94a19aba2f0222f374bbb/outputs/review.md
raw-output-sha256: 46c2c154ff4a20a32576e6f15c153cbc16120b315a76048b2a0eff06ae25325f
---

# Review

The candidate makes the commissioned contribution. It replaces the checked-or-absent rule with a qualitative trade-off between check cost and reliance risk, following the approved shape: reuse benefit, then the completeness mark contrasted with the connect report, then the freshness conclusion, then the compact numbered conditions and their limits. It does not frame the new argument as exceptions to the old rule.

**Delta and claim account.** Every material commitment of `start` is kept, replaced or omitted, and the report gives a reason for each. The claim account covers each claim in the candidate. The suppression mechanism keeps both conditions: the consumer actually stops, and the suppressed search would find more. The cheaper-verification point is a single conditional sentence. Full recomputation on every use "largely" defeats the saving, so it is not claimed to defeat it entirely. The connect report is described as candidate-only and as calling for judgment, and its mechanically checkable properties are kept separate from that judgment. The dependency difficulty is stated as tracking a sufficient set, not as an impossibility. The mark is said to supply conditions 1–3 and not to establish condition 4.

**Commission exclusions.** The candidate contains none of the excluded material: no valid/invalid or safe/unsafe dichotomy, no universal prohibition, no per-unchanged-version rule, no invented numbers, no old examples, no ADR used as authority, no external literature and no history of the rewrite. The description is under 250 characters. The section after the examples adds only the freshness conclusion and does not summarize the examples. Scope lists actual limits and is not a list of general disclaimers. The report's estimate of about 790 prose words is consistent with the text and sits within the 850 ceiling.

**Dependents.** The commission's current direction authorizes dropping the relied-on two-state rule, the asymmetry, the regime flip, graceful degradation and the omission rule, and the report says so for each. Condition 3 and the complete-mark instance, which dependents rely on, are kept. The report states the 30-of-38 coverage limit. The one relied-on item outside the explicit narrowing list is recorded as an info finding.

**Contracts and evidence.** The candidate meets the note type: it has frontmatter, `## Scope` and `## Open Questions`. It meets the theory collection contract: a design-space claim remains, and the Commonplace examples are scoped illustrations. Links are inline at the point of use, and the remaining footer links add navigation not supplied inline. Each claim has the support or inference the reconstruction gives, and transfers such as the frontloading amortization are marked as extensions.

**Why the outcome is warn.** One passage weakens the example that carries the central claim: it leaves implicit that the mark's check keeps the saving because of when it runs. This needs a small clarifying edit but does not block publication. The title mismatch is a decision reserved for the operator.
