---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - One producer-side study reports that
  reason: The brevity-pressure bullet is the longest item in Unsettled. It holds two
    verbatim quotes, the same source cited twice in one sentence, an evidence caveat
    and a separate log conjecture, and its open question comes only at the end. As
    a result it reads as the note's centre of gravity, although it is one of six frontiers.
    A revision could lead with the open question (how to apply selection pressure
    without encoding distortion), keep one quote or a paraphrase under a single citation,
    keep the measurement caveat, and leave the remaining quote-level evidence to the
    linked ingest. The thoroughness-plus-length-pressure conjecture needs an explicit
    placement decision rather than a silent cut.
- scope: passage
  quotes:
  - Systems like Commonplace combine **natural language and code**, which adds prose,
    conventions, links, and routing surfaces that lack static reachability checks.
  reason: The note's description says it covers where software anti-bloat advice falls
    short. That distinctive point sits as the third sentence of Stakes, after two
    sentences of general setup. Its partner point, 'No reachability oracle for natural
    language', appears only as the first Unsettled bullet, far from Stakes. A reader
    can miss that these two passages make one argument. A revision could open Stakes
    with the falls-short claim and make it explicit that the first Unsettled bullet
    is the open half of that claim, so the reader carries the thesis through Current
    answer.
outcome: report
description: Retained report review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
criterion-sha256: c7ee82f0ff41ddcb59d841986fcc47111cf98d676924cffe53a7a9a98dfa6d1c
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/synthesis/calls/launches/6dfff48415eb49c3b63cbc8b72a40cb0/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/synthesis/artifact/reviews/41e8d1aab5ff0f2fc571da57/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/synthesis
launch: 6dfff48415eb49c3b63cbc8b72a40cb0
completed-at: '2026-11-25T05:28:47Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/synthesis/calls/launches/6dfff48415eb49c3b63cbc8b72a40cb0/outputs/review.md
raw-output-sha256: 00e4d1f99e799a89a3c5fe676b0f9b424dddd247808dff373266747c8065df67
format: 2
---

# Simplification synthesis: How do we fight bloat in agent-produced systems?

All four compression checks passed. Their info findings mostly converge on one passage, the brevity-pressure bullet. The core-claim check adds a separate placement issue for the note's distinguishing thesis. No other passage was flagged, and the rest of the note keeps a proportionate Stakes / Current answer / Unsettled structure.

## Opportunities

### 1. Rebalance the brevity-pressure bullet around its open question

- Location: Unsettled, the bullet "**Brevity pressure can distort wording without cutting content.**", from "One producer-side study reports that" through "without triggering that encoding distortion."
- Combines: branch-bloat (the log conjecture is a second causal hypothesis whose home is unclear), core-claim-obscured (the bullet outweighs its siblings and its question comes last), detail-overhang (the second quote could become a paraphrase), and marginal-value-redundancy (one source cited twice in a sentence and again in the footer).
- Direction: Lead with the frontier statement and the open question. Ground it with one quote, or with one quote plus a paraphrase, under a single citation. Keep the caveat that human reading cost was inferred rather than measured. One possible resolution, given only as an illustration: "Brevity pressure can distort wording without cutting content: we do not know how to apply selection pressure without pushing models into denser, harder-to-parse syntax. One study finds AI text uses such difficult features more often than round-trip paraphrases, and that a length penalty causes the divergence ([source](…)); reading cost is inferred, not measured."
- Preserve or decide:
  - Decide where the log conjecture about thoroughness plus superficial length pressure belongs: it could stay in this bullet, go back to `kb/log.md` only, move to the linked source analysis, or become a workshop lead. The branch-bloat check left this open.
  - Decide whether a quote-grounding convention requires an attribution next to each retained verbatim quote before merging the two citations.
  - Preserve the measurement caveat, because it limits the evidence claim.
  - Preserve the distinction the marginal-value check drew between this frontier and the Current answer's "not word count" mechanism. If you add a cross-reference between them, keep their roles separate.

### 2. Surface the "software defenses fall short" thesis and join it to its open half

- Location: Stakes, first paragraph, "Systems like Commonplace combine **natural language and code**, which adds prose, conventions, links, and routing surfaces that lack static reachability checks."; and Unsettled, the bullet "**No reachability oracle for natural language.**"
- Combines: core-claim-obscured (first finding).
- Direction: Make the falls-short claim the opening of Stakes, then let the first Unsettled bullet name itself as the open half of that same claim instead of restating it independently. The reader then keeps one thesis through the note: software has partial reachability checks and natural language has none.
- Preserve or decide:
  - Preserve the Unsettled bullet's added point that code reachability checks "miss live but over-engineered code". It qualifies the contrast and is not a duplicate of the Stakes sentence.
  - Preserve the Stakes sentence noting that no software defense has settled bloat even for pure software, so moving the thesis forward does not overstate how well code-side defenses work.
  - This is a reordering and cross-reference, not a change of thesis. The description already selects the falls-short framing, so no choice among different theses is needed.
