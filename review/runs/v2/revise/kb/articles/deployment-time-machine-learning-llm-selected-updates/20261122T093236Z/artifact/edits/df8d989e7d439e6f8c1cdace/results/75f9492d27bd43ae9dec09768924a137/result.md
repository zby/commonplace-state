---
type: types/edit-result.md
outcome: changed
changes:
- 'Opening: cut the duplicate ''The loop itself is not new.'' from the bet paragraph;
  kept the single novelty disclaimer and the readable-store scope in the first paragraph.'
- 'Robust comparison method: removed the second statement of the narrowing effect
  (''Each stated preference removes functions...''); kept stochastic dominance and
  the analogy-limit paragraph.'
- Merged the two overlapping paragraphs after the bet into one on what the model must
  do instead of computing value functions, keeping 'This says what the judge must
  do', the trial-with-a-cheap-way-back point and the open-comparison-as-decision point.
- Moved the consistency caveat ('Even consistent answers can neglect a cost...') to
  the end of the consistency paragraph.
- 'Compressed the Gödel machine paragraph: dropped the closing recap (''The machine
  is not rigid... Its limits are...'') and kept that it can rewrite its own utility
  function under proof.'
- Made 'the three precedents' a forward reference ('The three precedents below').
- 'Split the compound ''Where to go next'' bullet: the reversibility note now has
  its own bullet.'
- Split clause-packed sentences in the routing-line walkthrough, the definition paragraph,
  the inspectability and costs paragraphs, the Gödel paragraph, the robust-comparison
  and bet paragraphs, the Bitter Lesson production-method paragraph and the improvement-comparison
  paragraph.
removed-links: []
description: Retained changed result of kb/instructions/simplification-passes/readability-and-flow.md
  on kb/articles/deployment-time-machine-learning-llm-selected-updates.md
format: 1
operation: kb/instructions/simplification-passes/readability-and-flow.md
operation-sha256: 01707fd7181b99fd0fa1f7bc60fcc6d289b0dcdd5abbacf34daa5d33777123db
note: kb/articles/deployment-time-machine-learning-llm-selected-updates.md
input-sha256: 79bf5ad8dad074a0179bd03452477118357c491ce50a6d57a42610d7e7048068
candidate: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/calls/launches/75f9492d27bd43ae9dec09768924a137/outputs/candidate.md
candidate-sha256: de7364c2bdff81e4854c7b93d299ad587921f91ada3618bba09a65c7bc503253
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/artifact/edits/df8d989e7d439e6f8c1cdace/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z
launch: 75f9492d27bd43ae9dec09768924a137
completed-at: '2026-11-22T09:51:33Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deployment-time-machine-learning-llm-selected-updates/20261122T093236Z/calls/launches/75f9492d27bd43ae9dec09768924a137/outputs/result.md
raw-output-sha256: 4b682e6c87f2e6a8022e565e97d19d53f7e83687f15c86092e926dcf32964594
---

# Report

Structural moves:

- Deduplicated the novelty disclaimer: removed "The loop itself is not new." from the second opening paragraph.
- Deduplicated the narrowing statement in the preference-model exposition; the analogy-limit paragraph keeps the narrowing-versus-widening contrast, and stochastic dominance stays.
- Merged the "The bet is not..." and "The procedure need not..." paragraphs into one paragraph on what the model must do instead of computing value functions.
- Relocated the consistency caveat after the consistency claim, closing that paragraph.
- Compressed the Gödel machine paragraph and dropped its closing recap; the utility-rewrite point now closes the paragraph.
- Turned "The three precedents" into a forward reference.
- Split the necessary-preference / reversibility bullet in "Where to go next" into two bullets; the first keeps its full original description.

Sentence-level edits: 16 (splits, semicolon removals and one pronoun/antecedent fix: "that set" became "the set of those weightings").

Left untouched per scope: the PRODIGY, EURISKO and Harness Evolution/Sutton paragraph; the faithfulness sentences in the costs paragraph and the "Unfaithful rationales" bullet; the closing "If controlled runs show" paragraph; the "why did earlier AI systems not..." sentence; sentences previously narrowed (e.g. the bounded-decision and open-verdict sentences). The fuller form of the bet was not moved into the opening. All relied-on terms and claims from the kb-role and every must-keep claim are retained verbatim or in substance. No links removed.

Noticed, not applied: the definition bullet in "Where to go next" also carries a companion link; left as is because the scope named a single compound bullet.
