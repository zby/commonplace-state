---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - routing and loading the relevant artifacts
  reason: 'Boundary case between the harness column and the three competences: choosing
    which uncodified artifacts are relevant to a new task. The note assigns routing
    and loading to harness code, but routing a novel case to prose procedures that
    lack a rule-ready signal is a meaning-dependent relevance judgment. It is not
    interpreting text into action (1), diagnosing a failure (2), or weighing a trade-off
    (3). Under the note''s own criteria, this case falls outside both columns, yet
    the note says only three semantic competences remain.'
  level: warn
- scope: passage
  quotes:
  - Diagnosing novel failures and synthesizing candidates across text and code
  reason: 'Boundary case: proposing an improvement when no failure has occurred, such
    as generalizing a successful pattern or noticing an opportunity. Competence 2
    ties candidate synthesis to an unanticipated failure. The store-maintenance paragraph
    stretches 2 and 3 to cover refactoring, so coverage is possible but strained.'
  level: info
- scope: passage
  quotes:
  - spotting semantic conflicts between prose rules, refactoring them into a cleaner
    abstraction, or proposing a revised check reduces to competences 2 and 3 applied
    to the store and its criteria
  reason: 'Adjacent case: store maintenance and criterion revision are mapped onto
    competences 2 and 3 by assertion. Spotting a conflict between two prose rules
    is not a failure diagnosis unless a failure has occurred, so this mapping depends
    on reading competence 2 more broadly than its stated wording.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/7e0f32a9da4f9a6a92b4ca37/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: cccda05d8a25440b842c04af9c04b834
completed-at: '2026-11-24T13:17:57Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/outputs/review-completeness-boundary-cases.md
raw-output-sha256: ea175eb10457ba303d82714e0fb0edb272fcafe94c65f13c10672ee7644efa1f
format: 2
---

# Review

## Summary

The framework has two parts. Harness code takes over the mechanical loop functions. Three semantic competences remain on the model: interpreting text into action, diagnosing and synthesizing, and judging trade-offs. The note's own grounding is that harness code relocates mechanical and structural work while semantic work remains.

Boundary cases tested:

- **Simplest instance:** a loop whose store is fully codified. The open-ended-work condition excludes it, so it maps cleanly.
- **Between columns:** relevance routing of uncodified artifacts. The note gives artifact routing to harness code. For new artifacts without rule-ready features, routing is semantic and fits none of the three competences. This case clearly falls outside the claimed coverage.
- **Between items:** proposals that do not respond to a failure, and conflicts between rules. These can be forced into competences 2 and 3, but the fit is strained.
- **Extreme instance:** a loop running entirely without humans across many store revisions. Competences 2 and 3 cover candidate synthesis and selection. Evaluation design is covered under the "checks" in competence 2.

The Scope section allows the list to grow. The central sentence still names exactly three irreducible competences. Clarifying the scope of the harness column, or saying where relevance selection belongs, would likely work better than adding a category.
