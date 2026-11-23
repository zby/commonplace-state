---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Separately, the team's goal may not have changed, yet the extracted Python rule
    proves to be a brittle proxy theory that fails on edge cases or distribution shift—or
    a stronger, cheaper model now handles the broader task well enough
  reason: 'About 44 words packing four ideas: the unchanged goal, the contrastive
    ''yet'' clause, the proxy-theory rule with its two failure conditions, and a second,
    independent trigger (a stronger, cheaper model) attached by a dash. The two relaxing
    triggers are separate conditions and read more easily as two sentences, e.g. ''The
    goal may not have changed. Either the extracted rule proves a brittle proxy theory
    that fails on edge cases or distribution shift, or a stronger, cheaper model now
    handles the broader task well enough.'''
  level: warn
- scope: passage
  quotes:
  - the mechanism whose movement across prompts and code a unified interface lowers
    call-site friction for
  reason: 'Distance problem: ''whose movement across prompts and code'' opens a dependency
    that resolves only at the stranded final ''for'', while the clause subject ''a
    unified interface'' and verb ''lowers call-site friction'' sit between. A reordering
    keeps every relation: ''the mechanism for which a unified interface lowers call-site
    friction when it moves across prompts and code''.'
  level: warn
- scope: passage
  quotes:
  - But in a system that exposes agents and tools through different invocation surfaces,
    a codification step that moves a component from one surface to the other is a
    breaking change
  reason: About 48 words including the colon list. A long fronted condition and a
    subject with its own relative clause precede the main verb, then three consequences
    follow. The colon list is a separate unit, so the load is tolerable; noted rather
    than flagged.
  level: info
- scope: passage
  quotes:
  - treats an instruction as permitting a set of readings, from which an LLM executor
    produces one, and treats extracting a repeated operation into code as a separate
    intervention whose trade-off must be assessed
  reason: About 39 words joining two independent attributions, each with an embedded
    relative clause. Near the threshold and still retainable; splitting into two sentences
    would ease it slightly.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/sentence/clause-packing.md
contract: verdict
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
criterion: kb/instructions/review-gates/sentence/clause-packing.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/909fcbc07636d535697b8b5c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: a13de1717c1c4bc3b58012768ccdd1bf
completed-at: '2026-11-20T11:11:48Z'
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/a13de1717c1c4bc3b58012768ccdd1bf/outputs/review-clause-packing.md
raw-output-sha256: 38151904781ccce1f15671d087aa5548bc9f92a5c178e93d6160039d69221825
format: 2
---

# Review

Most sentences in the note stay under the threshold or carry at most two ideas. Two passages overload the reader.

The relaxing bullet in "Why this matters for constraining" packs two independent relaxing triggers into one contrastive sentence. The reader must hold the unchanged goal, the proxy-theory rule and its failure conditions, and then a different trigger joined by a dash. Splitting it at the dash keeps the meaning.

The `Constraining` footer gloss strands its preposition at the end. The `whose movement ...` phrase stays unresolved across the embedded subject and verb. Moving to "for which" fixes it without dropping any word or relation.

Two further long sentences are noted at info level: the codification-step sentence and the opening attribution to the English account. Each is long, but its structure stays retainable.
