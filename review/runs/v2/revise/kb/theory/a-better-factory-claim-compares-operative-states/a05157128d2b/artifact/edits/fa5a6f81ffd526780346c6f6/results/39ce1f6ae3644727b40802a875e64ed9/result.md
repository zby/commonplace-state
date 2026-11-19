---
type: types/edit-result.md
outcome: changed
changes:
- 'Deduplicated the antecedence caveat: cut the Scope bullet ''Antecedence blocks
  post-hoc dimension selection…'' and moved its example (a properly declared comparison
  can still measure something that does not matter) onto the matching body sentence
  beside the prior-declaration mechanism.'
- 'Split the final paragraph of ''Improvement, retention and learning are different
  claims'' at its subject boundary: the improvement/learning summary joins the contrast-test
  paragraph; the other-objective and internal-controls sentences form their own paragraph
  under a new connective opening sentence.'
- Split the opening sentence so the software-factory definition and the retention/learning
  condition are separate sentences.
- Sentence-level parsing and tightening edits across the opening, relata, assessment-relation
  and Scope sections (semicolon splices split, pronouns given nouns, one long sentence
  split).
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/readability-and-flow.md
  on kb/theory/a-better-factory-claim-compares-operative-states.md
format: 1
operation: kb/instructions/simplification-passes/readability-and-flow.md
operation-sha256: c251205640499cde8b58fe05008ceef9e3d0319e2b3d5647ca41736cbc34fcd3
note: kb/theory/a-better-factory-claim-compares-operative-states.md
input-sha256: 1c000cb05df5ca6b9e071f1cc1d75c2532c6557e0cf02ae358f0ae6aeb9879f2
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/artifact/edits/fa5a6f81ffd526780346c6f6/results/39ce1f6ae3644727b40802a875e64ed9/candidate.md
candidate-sha256: eb62fc4cc536c7c71f81d7b7cfa822104be4c752960843c12b1d062abfbff5c8
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/artifact/edits/fa5a6f81ffd526780346c6f6/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b
launch: 39ce1f6ae3644727b40802a875e64ed9
completed-at: '2026-11-18T00:32:24Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/calls/launches/39ce1f6ae3644727b40802a875e64ed9/outputs/result.md
raw-output-sha256: 61a4f860d9d278e464120eaede3cbcdd5d27739c75303b6dce2e984e541ec596
---

# Report

Structural moves:

- Deduplicate caveats: the Scope bullet restating that antecedence blocks post-hoc selection but does not make the dimensions right was cut; its unique example now sits on the body sentence "It does not show that the requirements track factory quality", nearest the mechanism. No claim, example or link was lost.
- Split at argument boundary: the improvement-versus-learning summary sentence now closes the contrast-test paragraph; the remaining two sentences (another objective; internal controls govern adoption) form a separate paragraph introduced by "The comparison is also separate from other judgments of the factory."

Sentence-level edits: 11 (opening definition split; "it" → "the factory"; "Throughout…" sentence split; staging-comparison semicolon replaced with "but"; "the linked requirement" → "the requirement"; independent-specifiability semicolon split; "Naming it" → "Naming the scope"; model-weights clause split into its own sentence; Scope oracle semicolon split; retirement bullet semicolon → "and"; evaluator bullet "its judgment" → "the evaluator's judgment" with semicolon split).

Out-of-scope sentences, the TODO line, the predecessor bullet, the 'Antecedence guards…' Scope bullet and the footer are unchanged. All kb-role relied-on terms and claims are unchanged.

Noticed but not applied:

- "just not this audit-proof one" (Scope) uses "audit-proof" where the note elsewhere says "auditable"; it lies in the out-of-scope bullet, so it was left.
- The last Scope bullet's "Preserving factory development follows only when that capability is included in the checked scope" partly restates the body's conditional on the factory-development path. It was kept because it limits the generalization to other systems, not the factory case.
- The opening's "not a verdict on the factory's quality over its open production family" and the first Scope bullet ("What makes a successor genuinely better over an open family remains unresolved") overlap; kept because one defines the claim's sense of *better* and the other records an unresolved question.
