---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
findings:
- scope: passage
  quotes:
  - and treats extracting a repeated operation into code as a separate intervention
    whose trade-off must be assessed
  reason: The target does say this ('Extracting a repeated operation into code is
    a different intervention ... The code-extraction trade-off should be assessed'),
    but in its shared 'What the distinction changes in practice' section, which applies
    under both accounts, not as a feature of the English account specifically. The
    attribution is supported in substance; only its placement under 'the English account'
    is slightly narrow.
  level: info
- scope: passage
  quotes:
  - describe the learning mechanisms — narrowing the interpretation space, changing
    medium
  reason: '''Narrowing the interpretation space'' matches the constraining definition.
    ''Changing medium'' is a loose gloss of codification: the definition says codification
    moves a rule into symbolic form either by rewriting it or by adopting a consumer
    as its reference, and in the adoption case ''the text does not change''. In this
    note''s prompt-to-code context the rewrite case applies, so the gloss holds for
    the case in view, but it does not capture the definition in full.'
  level: info
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/9baad2ac251306b587dd8fe6/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-concept-attribution.md
raw-output-sha256: b5fc5fbc014bee54415c65e76dc67855e17c4a6254c66faf4c1453dbb2fadc1d
---

# Review

I checked each sentence that identifies a concept in this note with one from a linked note.

- **English account of prompting.** The target's English account treats an instruction as permitting a set of behaviors from which the executor produces one. This matches. The extraction point is also in the target, though in its account-neutral practice section. Recorded as info.
- **Constraining and codification.** The constraining gloss matches. The codification gloss "changing medium" fits the rewrite case discussed here. It omits the definition's adoption case, where the text stays the same. Recorded as info.
- **Spec mining.** The target's pattern is to observe behavior and extract regularities into deterministic artifacts. The ticket example of checking decisions against resolving queues and keeping a rule matches.
- **Relaxing and proxy theory.** The bitter-lesson note defines relaxing as replacing an extracted component with a more general one and names the proxy-theory regime. The relaxing-signals note covers brittleness and distribution shift. The note's use matches both.
- **Typed callables.** The target says skills, tasks and workflows are callable in a limited sense, can declare signatures, and are not made into conventional functions by them. The paraphrase is accurate.
- **Footer glosses.** The RLM/Tendril/llm-do and host-language scheduler notes are consistent with their footer glosses.

No attribution is substantively different from its target.
