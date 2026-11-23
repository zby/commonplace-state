---
type: types/edit-result.md
outcome: changed
changes:
- 'Three-payoffs paragraph: replaced ''Adaptation takes effect immediately at deployment
  time without waiting for a retraining run'' with a sentence saying a selected change
  can be retained during deployment and shape later runs without retraining, and that
  deployment time is a lifecycle phase, not a speed.'
- 'Three-payoffs paragraph: narrowed ''Retained knowledge is inspectable now'' to
  ''Retained rules can be inspected now ... as long as each rule stays readable at
  an affordable cost'', adding that large or obscure artifacts can block inspection.'
- 'Gödel machine paragraph: replaced ''every self-rewrite requires a formal proof
  of higher expected utility under axiomatized hardware, environment priors, and scalar
  utility'' with the admission route''s actual condition: a proof that switching beats
  continuing the current search, under axioms describing hardware, environment, and
  utility.'
- 'Gödel machine paragraph: narrowed ''a formal optimality guarantee relative to those
  axioms'' to ''an optimality guarantee conditional on those axioms and that utility''.'
- 'Gödel machine paragraph: replaced ''no general real-world domain has the full axiomatization
  required'' with the statement that a valid proof does not establish that the axioms
  adequately describe the domain, so a proved switch need not deliver what its user
  wanted.'
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/narrow-overclaims.md
  on kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
format: 1
operation: kb/instructions/simplification-passes/narrow-overclaims.md
operation-sha256: fff83f2074936afa498432ab20d6f522624d8af329308aa5cdb1bd7f5cd99feb
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
input-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
candidate: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/920bccea785d45b1b7f6e29971994bb2/outputs/candidate.md
candidate-sha256: 6711b5d0f0e4ac0c45fbb5b8a772531a172505fad8c47ef99b47b0ad56040af7
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/artifact/edits/3e0904705e38c20bf2c39463/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z
launch: 920bccea785d45b1b7f6e29971994bb2
completed-at: '2026-11-21T19:38:59Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/calls/launches/920bccea785d45b1b7f6e29971994bb2/outputs/result.md
raw-output-sha256: bc12a490a6c46711e3403ec6f0fea32dbe8bf19f7b9a3545e97575018f2bb841
---

# Report

Five sentence-level narrowings in the two scoped passages. No link, quote,
heading or frontmatter field changed. No must-keep claim was touched.

## Changes

1. **Deployment-time adaptation.**
   - Before: "Adaptation takes effect immediately at deployment time without waiting for a retraining run."
   - After: "A selected change can be retained during deployment and shape later runs without a retraining run; "deployment time" places the change in the lifecycle, not its speed, since proposing, evaluating, and safely installing it still take time."
   - Evidence: the linked note `retained-artifacts-enable-persistent-deployment-time-adaptation.md`, section "Lifecycle phase is not update speed", separates lifecycle phase from update latency and says: "'During deployment' locates the change in the lifecycle; it does not by itself make the change fast." Its Boundary section adds that the claim is not "always faster than training."

2. **Inspectability.**
   - Before: "Retained knowledge is inspectable now—by people or by other agents at volumes people could not read—whatever the pace of weight interpretability research."
   - After: "Retained rules can be inspected now—by people or by other agents at volumes people could not read—whatever the pace of weight interpretability research, as long as each rule stays readable at an affordable cost; large or obscure artifacts can block that inspection."
   - Evidence: the linked note `inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md` limits the advantage to "readable rules at an affordable inspection cost, not every symbolic artifact", and says "Large or obfuscated code can likewise obstruct inspection."

3. **Gödel machine admission condition.**
   - Before: "Yet every self-rewrite requires a formal proof of higher expected utility under axiomatized hardware, environment priors, and scalar utility."
   - After: "Yet its admission route lets a self-rewrite take effect only through a formal proof that switching has higher expected utility than continuing the current search, under axioms describing the hardware, environment, and utility."
   - Evidence: `goedel-machines-are-a-proof-governed-case-of-self-modification.md` describes the admission route as requiring "a proof that switching to a proposed program has greater expected utility than continuing the current search, under axioms describing the machine, environment, and utility function." It also says self-modification can change the proof searcher, axioms or utility representation where the formalization licenses it. So "every self-rewrite" against fixed axioms says more than the note does.

4. **Optimality guarantee.**
   - Before: "That buys a formal optimality guarantee relative to those axioms"
   - After: "That buys an optimality guarantee conditional on those axioms and that utility"
   - Evidence: the same note, "Adequacy of the formalization": the Global Optimality Theorem compares a switch with continuing the search, and "Its guarantee is conditional on the encoded assumptions and utility."

5. **Axiomatization of real-world domains.**
   - Before: "and no general real-world domain has the full axiomatization required."
   - After: "and a valid proof does not establish that the axioms adequately describe the real-world domain—under an inadequate formalization, a proved switch need not deliver what its user wanted."
   - Evidence: the note does not claim that no real-world domain can be axiomatized. It says "A valid proof under an inadequate model or objective need not warrant the outcome a user actually wanted." Whether real domains can be adequately axiomatized remains an open gap; the article no longer asserts an answer.

## Kept as written

- "the machine must ignore every useful improvement it cannot prove": the note quotes the paper verbatim on this point ("must ignore those self-improvements whose effectiveness it cannot prove", §2.4). Out of scope in any case.
- "by people or by other agents at volumes people could not read": the linked note supports inspection by humans or LLMs. The volume claim is a mild inference that the note does not state. It was not flagged in scope, so it stays.

## Noticed, not applied

- The paragraph's lead-in, "Three payoffs follow directly from storing what the system retains...", is outside the two named sentences. Both linked notes call these advantages conditional, not direct ("This advantage is conditional rather than intrinsic"). A later pass could narrow "follow directly".
- The table row "When updates happen: Deployment time, taking effect on the next task that reads the store" is outside scope. It does not claim speed, so it is consistent with change 1.
- The section's opening "bottleneck was always" sentence, and the PRODIGY, EURISKO and on-balance paragraphs, were left untouched as scope required.
