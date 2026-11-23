---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Basis: the candidate''s frontmatter `description` (unchanged from supplied-start.md)
    says the article covers ''the bet that a fixed-weight LLM can build the preference
    model and make the robust comparison; weight-training contrast, Bitter Lesson,
    empirical test''. The candidate body has no preference-model argument and no weight-training
    contrast; the candidate report says so itself. The type contract (supplied-type-contract.md)
    makes `description` the agents'' retrieval filter, and the commission''s reserved
    decisions (supplied-commission.md) cover the title, path, byline, draft status
    and banner, not the description. A stale filter will send agents to this article
    for content it no longer contains. Required change: rewrite the description to
    match the body. For example: the software house turning its development capability
    on its own test-selection workflow; the bet that an LLM can select self-edits
    without per-edit human judgment; conditional Bitter Lesson compatibility; retained
    hypotheses for sample efficiency and bounded explanation; evidence status. If
    the rewrite workflow requires the description to stay fixed, the operator should
    make this change at publication.'
  level: warn
- scope: passage
  quotes:
  - The client's test rule decides which tests a client edit gets.
  reason: 'Basis: in note.md, the article first calls this rule the house''s own method:
    ''Its test-selection workflow skips the build tests''. It then says the house''s
    ''test-selection rule is unchanged'' and treats editing that workflow as the house''s
    self-edit. The commission''s must-keep asks the article not to conflate the client
    product''s test rule with the house''s own criterion for adopting workflow revisions.
    Calling the house''s rule ''the client''s test rule'' blurs a different line that
    the article depends on: a fix to a client''s product versus a change to the house''s
    own method. A reader may conclude that the rule belongs to the client, which would
    make editing it look like product work. Required change: name the rule the same
    way as elsewhere, e.g. ''The house''s test-selection rule decides which tests
    a client edit gets.'''
  level: warn
- scope: document
  quotes: []
  reason: The candidate runs to roughly 1,600–1,700 body words, slightly above the
    commission's 'roughly 1000–1500 words'. Each section carries a must-keep item
    and no passage repeats what the example already shows, so no cut is required.
  level: info
- scope: passage
  quotes:
  - and in later work he argues for continual weight updates
  reason: The attribution is supported by supplied-source-8, which cites the 2026
    Sutton and Javed interview arguing that continued weight updating is necessary
    for forming new concepts. The candidate gives no citation. A reader can reach
    the interview through the linked production-methods note, so this is an observation,
    not a required change.
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deployment-time-machine-learning-llm-selected-updates.md
  against kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
contract: verdict
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
criterion: kb/instructions/rewrite-a-note/review-a-rewrite-candidate.md
note-sha256: c7bd5078a73f345bea635194a966243d4bfb09e3c0ac9fb18b53d6cdb132ecc8
criterion-sha256: 72878e536fd897c07be2c1dec0230689269ff118d9e862eef66f6fc8b814c3b2
target-sha256: c7bd5078a73f345bea635194a966243d4bfb09e3c0ac9fb18b53d6cdb132ecc8
target-capture: kb/reports/state/review/runs/v2/rewrite/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T170948Z/reviews/f07fba2cffb5/calls/launches/70b14e7a45a84cb8adc14b814a3096ef/inputs/note.md
observation: kb/reports/state/review/runs/v2/rewrite/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T170948Z/reviews/f07fba2cffb5/artifact/reviews/0ec749c14686919307319558/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/rewrite/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T170948Z/reviews/f07fba2cffb5
launch: 70b14e7a45a84cb8adc14b814a3096ef
completed-at: '2026-11-22T17:14:15Z'
raw-output: kb/reports/state/review/runs/v2/rewrite/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T170948Z/reviews/f07fba2cffb5/calls/launches/70b14e7a45a84cb8adc14b814a3096ef/outputs/review.md
raw-output-sha256: b67e4ec0a4d7f8ed8423a417b9e3febbdc9b54d4a39149023d838d0ac0f544fd
format: 2
---

# Review

## Summary

The candidate can be published as a draft. It makes the commissioned contribution: a short, self-contained article built on one explicitly hypothetical failure, with one empirical bet and two conditional arguments, written for an external reader. Two nonblocking changes remain: a stale frontmatter description and one mislabelled reference to the test-selection rule.

## Commission coverage

Every must-keep item is present and in its own place:

- **Two repairs.** The product fix is followed by an explicit statement that it is not evidence the house learned.
- **The self-edit.** The house compares all four named remedies on missed failures against cost. It can investigate facts, reject every candidate or try a variant under review.
- **Search.** Search produces both candidates and a discriminating test: the replay of last quarter's edits.
- **Selection.** The comparison does without a single score, and the article says outright that choosing a remedy is not proof that it helps.
- **Causal effect on later work.** The changelog job shows later work changed by the retained method. The article gives the with/without rerun as the check and notes that no weights changed.
- **Downstream test.** Gain is measured against credible baselines, counting compute, review time and rollback costs.
- **Automation boundary.** External requirements stay outside the house, matching supplied-source-1. Only internal decisions by people make the loop human-assisted.
- **Double-loop.** The article separates editing the workflow under a fixed adoption criterion from revising that criterion, and marks double-loop as a further capability rather than a membership condition, matching supplied-source-4.

Everything the commission excluded is gone. The candidate has no comparison table, historical tour, decision-analysis tutorial, list of hazards or obligatory reading list. The body contains no commission language. The title, byline, draft status and banner are unchanged, and `source_notes` lists exactly the theory notes the text distils.

## Evidence

The verbatim Sutton quotation matches the retained quote in supplied-source-9.

The Bitter Lesson section rests on three sources:

- **Production method, not form.** Supplied-source-8 supports the reading that the lesson concerns how knowledge is produced, not how it is represented. The candidate labels this as an interpretation.
- **Compatibility condition.** Supplied-source-7 supports the condition that additional computation must do the domain-specific discovery and selection, and that hand-written methods fit only if learning outgrows them. The candidate keeps the point that unattended scripts encoding a person's diagnosis do not qualify, and that scaling still has to be measured.

The second argument also stays within its sources:

- **Hypothesis example.** The included-snippet case follows supplied-source-10 closely.
- **Sample efficiency.** The definition and baseline match source-10: fewer new target observations under a shift that preserves structure, compared with the same model and history kept only as case records, and explicitly not a claim of lower compute.
- **Bounded explanation.** The claim of explanation is limited to the operative rule. It is tested by intervention and kept apart from legibility, matching supplied-source-12.

The closing section gives a mixed result for each claim. It also states the evidence honestly: Commonplace is human-assisted and has not demonstrated an end-to-end autonomous loop, matching source-8.

## Findings in context

**Description.** The description still advertises a preference-model argument and a weight-training contrast, and the body has neither. The writer kept it on purpose and flagged the mismatch. The supplied commission does not reserve the description, and the type contract makes it a retrieval filter, so it should be updated. It does not block publication of a draft.

**"The client's test rule."** The paragraph that separates the two criteria is the place where the reader most needs consistent naming. Elsewhere the rule is the house's own workflow. Attributing it to the client works against the article's central distinction between improving a product and improving the producer.

## Affected-citations report

The report covers all five inbound files and identifies the lost uses accurately:

- The robust-comparison clause and the "weight-training contrast" description in the testing companion no longer match the candidate.
- The `kb/index.md` claims about the no-single-score argument and grounding in necessary preference no longer match.
- The README summary and the improvement-loop tag remain supported.
- The citation in `automating-kb-learning-is-an-open-problem.md` remains largely supported.

These lost uses are repair work for the dependents. They do not require the candidate to restore the dropped claims.
