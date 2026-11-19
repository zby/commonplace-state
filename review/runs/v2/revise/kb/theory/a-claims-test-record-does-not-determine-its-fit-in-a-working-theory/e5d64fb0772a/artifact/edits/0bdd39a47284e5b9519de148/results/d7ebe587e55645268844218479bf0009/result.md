---
type: types/edit-result.md
outcome: changed
changes:
- Narrowed the independence condition in the test-record bullet from not presupposing
  the working theory to not presupposing the claim under test or an auxiliary claim
  whose acceptance would make the outcome automatic.
- Made the 'So use of a claim inside the theory can be a test' paragraph consistent
  with the narrowed definition by adding 'without presupposing it'.
- Split 'repeatedly fails to predict … has earned a new independent test' into failing
  to yield a useful prediction (poor fit, not evidence of falsity) and yielding wrong
  predictions (a reason for a new independent test); dropped 'earned'.
- Narrowed 'force a change of fit' / 'may require restructuring' to 'bear on fit'
  / 'may give a reason to restructure'.
- Narrowed "'This claim is well tested' is not a reason to retain it" to 'is not by
  itself a reason'.
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/narrow-overclaims.md
  on kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
format: 1
operation: kb/instructions/simplification-passes/narrow-overclaims.md
operation-sha256: 2e627d71a54ea21109203837b00e1da8deff0bcaca0260d779f9a0e95a3b9857
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
input-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/artifact/edits/0bdd39a47284e5b9519de148/results/d7ebe587e55645268844218479bf0009/candidate.md
candidate-sha256: e4e43bc2745bef5ac3d5156e880a71ed65253f5bc8b49d1a9f8d98c47ad000e2
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/artifact/edits/0bdd39a47284e5b9519de148/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a
launch: d7ebe587e55645268844218479bf0009
completed-at: '2026-11-16T17:48:16Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/calls/launches/d7ebe587e55645268844218479bf0009/outputs/result.md
raw-output-sha256: 90df64868e2eddf72f7c62e5d742a07dc64a59dacb2aff6f11b7d98d5538ece2
---

# Report

Five sentence-level narrowings, all inside the supplied scope. No links, quotations, title, H1 or frontmatter changed.

- Before: "A test is independent when its outcome could have gone against the claim and does not presuppose the working theory."
  After: "A test is independent when its outcome could have gone against the claim and does not presuppose the claim under test or an auxiliary claim whose acceptance would make the outcome automatic."
  Bound: the note's own could-have-failed condition (§82) and its next paragraph, which allows use inside the theory to count as a test. "Does not presuppose the working theory" excluded every such use and contradicted that paragraph. kb-role lists this clause as unused, so narrowing it touches no relied-on term.

- Before: "What decides is whether the use could have gone against the claim, not where the evidence was produced."
  After: "What decides is whether the use could have gone against the claim without presupposing it, not where the evidence was produced."
  Bound: aligns the paragraph with both halves of the narrowed independence definition. The could-have-failed condition, which kb-role lists as relied on, is unchanged.

- Before: "A claim that repeatedly fails to predict, to guide recovery or to transfer has not been refuted by that alone, but it has earned a new independent test."
  After: "A claim that repeatedly yields no useful prediction, recovery guidance or transfer shows poor fit, which is not evidence that it is false. A claim whose predictions repeatedly come out wrong in use has not been refuted by that alone, but it is a reason for a new independent test."
  Bound: the note's fit/test distinction. An idle claim is a fit failure, while a wrong prediction bears on truth. "Earned" implied an entitlement that the evidence does not establish.

- Before: "A new test result can likewise force a change of fit: a claim that survives a severe test may require restructuring the working theory …"
  After: "A new test result can likewise bear on fit: a claim that survives a severe test may give a reason to restructure the working theory …"
  Bound: the note's own last section says that which repair to make is a decision. A test result supplies a reason for that decision. It does not force or require one.

- Before: "\"This claim is well tested\" is not a reason to retain it in this theory."
  After: "\"This claim is well tested\" is not by itself a reason to retain it in this theory."
  Bound: the Scope section says a well-tested claim is more likely to fit, so a good test record is some reason. The relied-on claim is that the test record does not make the retention decision, and that claim is unchanged.

Defended claims are unchanged, including "Neither may be substituted for the other" and the repair-as-decision sentence. No other sentences were flagged or changed.
