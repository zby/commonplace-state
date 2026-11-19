---
type: types/edit-result.md
outcome: changed
changes:
- 'Asymmetry section: rewrote the second paragraph''s opening, which restated the
  first paragraph''s bounded-versus-unbounded contrast, as a causal sentence that
  draws the conclusion.'
- 'Where-the-rule-applies section: split the first paragraph so that the description
  of the managed-staleness machinery and the reason it stops at review are separate
  paragraphs.'
- 'Deduplicated the caveat that lineage need only be machine-followable, not visible
  to a human: removed it from the regime paragraph and kept it in precondition 2,
  where the requirement is stated.'
- 'Sentence-level edits (5): ''the rule rides entirely on that'' became ''The rule
  rests on an asymmetry between the two failure modes''; ''Enforcement is the third
  class'' became ''Enforcement adds a third class'' (enforcement is not itself a class);
  ''Here'' became ''In that class''; ''the regress'' became ''the regress of unchecked
  claims''; the closing ''It is the general form'' now names ''The rule'' as its subject.'
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/readability-and-flow.md
  on kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
format: 1
operation: kb/instructions/simplification-passes/readability-and-flow.md
operation-sha256: c251205640499cde8b58fe05008ceef9e3d0319e2b3d5647ca41736cbc34fcd3
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
input-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
candidate: kb/reports/state/review/runs/v2/20261115T222225Z/artifact/edits/0b1bd73b4f7aa17115d22667/results/0a804f21536b4cb6865d8ba83ffde714/candidate.md
candidate-sha256: ec672a779f2bcfdf202efac261d2895b30fa9d58f9001dc660e90bc7e297290e
observation: kb/reports/state/review/runs/v2/20261115T222225Z/artifact/edits/0b1bd73b4f7aa17115d22667/observation.json
contract-sha256: 7f577dba87ec6e78e7e231d2dc16d3bf36bf687b80b00dffa134973588e84c79
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T222225Z
launch: 0a804f21536b4cb6865d8ba83ffde714
completed-at: '2026-11-15T22:23:43Z'
raw-output: kb/reports/state/review/runs/v2/20261115T222225Z/calls/launches/0a804f21536b4cb6865d8ba83ffde714/outputs/result.md
raw-output-sha256: 6ae136bbed8e7e3d7e14e1c167d400415686804b516d8e62233ae1a46950f7fe
---

# Report

Structural moves:

- Merged the restatement in the asymmetry section into one causal sentence ("Because one downside is bounded and recoverable and the other is silent and unbounded, …").
- Split the dense managed-staleness paragraph at its argument boundary: what the machinery does, then why it stops at review.
- Deduplicated the machine-followable/human-visibility caveat. The caveat now appears only in precondition 2. The regime paragraph keeps its claim that the interrupt-placement problem dissolves because the validator is the edit-time surface.

Sentence-level edits: 5.

No claims, examples, links or qualifications were removed. The opening already gives the sentence a reader would repeat (exactly two valid states, checked or absent), so nothing was moved there.

Noticed but not applied: the instances section says the four surfaces are "already enforced, stated but unenforced, resolved by omission, and not yet applied". It is unclear which list item each state maps to. For example, the byte-identical `AGENTS.md.template` copies are described without saying whether a check exists. Fixing the mapping would mean choosing between readings, so it was left and is flagged here.
