---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: 'The asymmetry argument only rules out copies that consumers trust. It does
    not rule out a third state: a copy that is present and unchecked, but that consumers
    treat as a hint and verify when they use it. The note should either name this
    as a valid state or explain why it collapses into ''checked'' or ''absent''. Otherwise
    the title and the ''exactly two'' claim say more than the argument supports.'
- scope: passage
  quotes:
  - can cause silent, unbounded wrongness when it tells consumers to stop looking
    or to follow a snapshot of a world that has since moved
  reason: This condition is where the argument gets its force, but the rule's statement
    drops it. A false copy causes silent, unbounded harm only when its falsity cannot
    be detected at the point of use. Completeness and other negative claims ('nothing
    else exists') are the clearest cases. A positive entry, such as a pointer or a
    listed item, fails loudly and at bounded cost when the consumer follows it. Moving
    this condition into the rule would scope 'forbidden' to the cases the asymmetry
    actually covers.
- scope: passage
  quotes:
  - a compiled cue (a memory system's derived retrieval hint)
  reason: A retrieval hint is the standard example of a copy that is safe without
    validation, because a wrong hint costs one wasted lookup and does not stop the
    search. Listing it as an instance of the rule invites the counterexample. The
    note should either say what makes a compiled cue suppress further search, or limit
    the instance to cues that are treated as exhaustive.
- scope: passage
  quotes:
  - costs the consumer one bounded recomputation
  reason: 'This assumes that a consumer without the copy will recompute. An LLM consumer
    may instead answer from priors, which is also a silent wrong result. The asymmetry
    still holds against a trusted stale copy, but the note should state the assumption:
    omission is safe only when the consumer is directed to the live source.'
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/critique-note.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/2d393307620296b55525087f/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/2d393307620296b55525087f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: b15446e19b8943d0b7c5bbd6080573fb
completed-at: '2026-11-16T22:21:32Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/b15446e19b8943d0b7c5bbd6080573fb/outputs/review.md
raw-output-sha256: b3bd49d047157e8de024c5c74f929563c9b66d6dac4b82d5f835d806cda071da
format: 2
---

# Critique: A derived copy of recomputable truth must be checked or absent

**Note:** kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
**Central commitment:** A copy of information that can be recomputed mechanically from a ground-truth source has exactly two valid states, machine-checked against the source or absent. A hand-maintained copy that consumers trust is forbidden, not just risky, because an absent copy costs a bounded recomputation while a false one causes silent, unbounded wrongness.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a systems designer in the tradition of Lampson's *Hints for Computer System Design*. That tradition treats a saved result that may be wrong as a respectable design element, the **hint**. A hint costs nothing to maintain correctly because nobody relies on it being correct. The consumer uses it to save work and checks it against the truth on use. A wrong hint costs one failed attempt and a fallback to the slow path.

Applied to this note, the argument runs as follows:

1. The note's rule is supported entirely by the asymmetry argument. That argument shows that a false copy is catastrophic only under a specific condition, which the note itself states: the copy "tells consumers to stop looking or to follow a snapshot of a world that has since moved". The harm comes from the copy suppressing the recomputation that would expose it.
2. Many derived copies do not suppress anything. Examples are a list of likely-relevant files, a pointer to a contract section, and a retrieval cue that says "start here". When such a copy is stale, the consumer follows it, finds a missing file or a mismatched section, and falls back to the source. The failure is loud and its cost is bounded, about the same as the "absent" branch.
3. So a third valid state exists: **present, unchecked, consumed as a hint**. It keeps most of the frontloading benefit that the note values. It avoids writing a validator for every copy. And it does not have the asymmetric downside, because the falsity is detected at the point of use rather than at validation time.
4. The note's own instance list includes "a compiled cue (a memory system's derived retrieval hint)". That is the canonical hint. Classifying it as necessarily checked-or-absent is the overreach in concrete form.

The conclusion is that the rule is correct for copies whose falsity cannot be detected at use: completeness marks, exhaustive lists and "nothing else" claims. Stated as "exactly two valid states" for every derived copy of recomputable truth, it forbids a well-established and safe design pattern.

Two points cannot be dismissed in one sentence. First, the note's own mechanism text concedes the condition the opponent relies on. Second, the note's flagship example, the `complete` mark, is exactly the negative-claim case where the hint escape does not apply. That suggests the rule was generalized from its strongest case.

## How the note engages it

**Partially engaged.** The note frames the forbidden state with the qualifier "maintained by hand and trusted by consumers" in the opening paragraph, and repeats "hand-maintained-and-trusted" in the asymmetry section and in Consequences. Read strictly, an untrusted hint is therefore not forbidden. The asymmetry section also names the harmful mechanism precisely ("tells consumers to stop looking"). It ties the rule to `kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`, whose title contains the same "when they suppress" condition.

The note does not carry that qualifier into its headline claims, though. The title says "checked or absent". The body says "Such a copy has exactly two valid states", and the Consequences section says "When a copy can't be checked, the resolution is omission". None of these leave room for a present-but-untrusted copy. The note never considers check-on-use as an alternative to check-at-validation. The compiled-cue instance points the opposite way. The section "What 'checked' requires" lists preconditions for validator-style checking only.

So the defensible core of the note survives: trusted completeness and negative claims must be checked or absent. The universal two-state formulation does not survive.

## Constructive findings

- Scope the rule to copies whose falsity cannot be detected when they are used. Lift the note's own condition ("tells consumers to stop looking…") from the mechanism paragraph into the rule statement, and name completeness and negative claims as the central case.
- Either admit a third state, present but untrusted and checked on use (a hint), or argue explicitly why it collapses. One possible argument is that LLM consumers do not reliably check hints on use, so in practice every present copy becomes trusted. That argument would need support. If made, it would turn the attack into a claim about consumer behaviour rather than about copies.
- Reconsider the compiled-cue instance. Either say what makes a cue suppressive, for example being treated as the retrieval result rather than as a seed, or drop it in favour of an exhaustive-list example.
- State the consumer assumption behind "bounded recomputation": omission is safe only when the consumer is pointed at the live source. The 2026-06-10 read-the-contract edits do this, and the rule should say so.

## Secondary objections (optional)

- **Absence is not automatically bounded for LLM consumers.** Without a copy and without an instruction to read the source, a model may answer from priors. This is also silent wrongness. It does not reverse the asymmetry against a trusted stale copy, but the note's "absent" branch carries an unstated precondition.
- **"Forbidden" versus expected cost.** An engineering-economics critic would say that a rarely changing, rarely consumed copy may have lower expected cost hand-maintained than the cost of writing its validator. The note partly answers this through amortization (precondition 4) and by offering omission as the fallback. But "trusting an unchecked copy now saves nothing" holds only once a validator exists or is cheap to write, and the note does not price that authoring cost.
