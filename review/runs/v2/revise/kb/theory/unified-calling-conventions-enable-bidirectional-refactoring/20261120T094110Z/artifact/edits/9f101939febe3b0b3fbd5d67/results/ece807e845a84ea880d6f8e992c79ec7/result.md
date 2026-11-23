---
type: types/edit-result.md
outcome: changed
changes:
- 'fix-strategy-taxonomy.md#unframed-domain-examples: ''This requires **name-based
  dispatch**: ...'' → ''llm-do achieves this shared interface through **name-based
  dispatch**: ...'', framing name-based dispatch as llm-do''s means rather than a
  requirement of the general mechanism.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
input-sha256: 8a68d80eb4f779b8b90de828142f985e323d8b319154afbec7167b005296cd46
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/ece807e845a84ea880d6f8e992c79ec7/outputs/candidate.md
candidate-sha256: 16df14fe441f5f528d2446ab0a130a2c7b4187fead42ad5db7b5a790eab30522
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/artifact/edits/9f101939febe3b0b3fbd5d67/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z
launch: ece807e845a84ea880d6f8e992c79ec7
completed-at: '2026-11-20T09:58:49Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/ece807e845a84ea880d6f8e992c79ec7/outputs/result.md
raw-output-sha256: 0a32f6e1832fa1abf02177ed780179a581ebac8a420b0f5bc134eda5ff198337
---

# Report

Finding 1 (source-residue, warn): applied `fix-strategy-taxonomy.md#unframed-domain-examples`.
The passage "This requires **name-based dispatch**: components are identified by
string name rather than direct object reference." now reads "llm-do achieves this
shared interface through **name-based dispatch**: ...". This takes the finding's
second option: name-based dispatch is how llm-do achieves the shared interface. It
is no longer stated as a requirement of every unified calling convention.

The following sentence, which lists what names enable, is unchanged. It is in
scope, but it already describes properties of names, and its first item ("the LLM
outputs a string, the runtime looks it up") already marks the LLM-emitted-call
case the finding identifies. Relied-on content from kb-role is kept: "the same name
can resolve to either neural or symbolic" and the opening paragraph's general
claim. The description field still says "llm-do demonstrates this with name-based
dispatch", which matches the new framing.

No links, quoted spans or other passages changed. The result has no findings that
were left untouched.
