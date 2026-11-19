---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The spread is what shows it generalizes
  reason: 'The contract says a universal claim is a new hypothesis that no number
    of singular observations establishes, and that cases the claim was built from
    explain its origin without corroborating it. The four Commonplace surfaces are
    origin cases and illustrations: one is enforced, one only states the rule, one
    is resolved by omission, and one has not applied it yet. None reports a refutation
    attempt the claim could have failed. Saying their spread ''shows it generalizes''
    presents origin as support for generality. Reframe the section as illustrations,
    or as applications of the law to Commonplace''s initial conditions.'
  level: warn
- scope: passage
  quotes:
  - 'evidenced-by: the `complete` mark is the shipped, validator-enforced instance
    of the rule; the mark contract lives here'
  - 'evidenced-by: source-of-truth for the byte-identical `AGENTS.md.template` duplication
    cited as the fourth instance'
  reason: Under 'Origin is not corroboration', an evidenced-by context phrase must
    say either what the claim risked and when the evidence was recorded relative to
    the claim, or that the evidence qualifies or bounds the claim. Both phrases only
    call the target an instance or a source-of-truth for an instance. That reads as
    implied corroboration. These cases appear to be ones the rule was generalized
    from, so they fit `abstracted-from`. If they stay `evidenced-by`, the phrase should
    state that the evidence illustrates or bounds the claim.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/theory/COLLECTION.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: 23ede037003607491dace7447a749ba3d1865aa8fd8cd08a03da6749af864112
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/e5acfb7c990ee45af19eb7b2/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/e5acfb7c990ee45af19eb7b2/observation.json
contract-sha256: d6cb429f353da63ee3eb956257dc3c0d9e6080b42cb7c2554e2042f242c9fcbf
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T123635Z
launch: 06f87208a8044d749aad26547fbc825e
completed-at: '2026-11-15T12:37:19Z'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/06f87208a8044d749aad26547fbc825e/outputs/review.md
raw-output-sha256: e5d7424f99d4036f3ed1d851642c2e7c88b9a95a4396d23a0831e591596c16b2
format: 2
---

# Review

## Placement and quality goal

The note belongs in `kb/theory/`. Once every Commonplace choice is scoped, a substantive claim about the design space remains. Copies of recomputable truth have only two safe states, checked or absent. The reason is the asymmetry between the bounded cost of an absent copy and the unbounded cost of a false one. The argument has explanatory-reach. It names the premise that flips the regime: check price falling to Level A. It says what happens when that premise changes: managed staleness and judgment review. It lists four preconditions where enforcement fails. The Commonplace particulars (the `complete` mark, the hot-path skill contract lists, the `AGENTS.md.template` copies) are scoped with enough identifying detail to serve as illustrations. They are not the note's contribution.

## Linking

Outbound links follow the label table:

- `grounds`, `extends` and `contrasts` point to theory notes.
- `evidenced-by` points to `types/` and `reference/`, which are allowed destinations.
- Nothing links into `kb/work/`.
- No tracked sources are cited, so the source-grounding bound does not apply.

Inline links use connective phrasing, for example "This is the sharpest case of".

## Unmet conventions

The gaps are about how the note uses evidence, and they share one cause. The instances section and the two `evidenced-by` footer entries treat Commonplace's own surfaces as support for the universal rule. These surfaces are where the rule came from, plus states the rule describes. They are not tests the rule could have failed. The fix is local: reword the section's framing sentence, and either relabel the two footer entries or rewrite their context phrases. The theoretical claim does not depend on these cases, so the theory-independence constraint is still met.
