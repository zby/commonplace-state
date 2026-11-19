---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:10Z'
findings:
- scope: passage
  quotes:
  - the general source-of-truth requirement, stated for memory systems in
  reason: 'Conflates a source account with an object of application. The bullet sits
    in a list of ''Four surfaces in the system'' that ''instantiate the rule'', but
    its content is a prior requirement stated in another note for memory systems in
    general, not an identified surface in this system. Reading A: Commonplace has
    compiled cues where the rule is stated but unenforced, so this is instance evidence.
    Reading B: the linked note is an antecedent account that this note generalizes
    (as the footer''s ''extends: generalizes its compiled-view source-of-truth rules''
    suggests), so it is inherited theory, not an instance. The choice changes what
    the note claims to inherit versus contribute and whether the bullet counts toward
    ''The spread is what shows it generalizes''. The author must decide whether this
    is an instance surface or a prior account.'
  level: warn
- scope: passage
  quotes:
  - It is the general form of
  reason: 'The unattributed maxim ''a cache must never be the only copy'' is presented
    as the special case this note generalizes. The relation is unclear: the maxim
    concerns durability (a cache needs a backing store), while this note concerns
    consistency checking. It is unclear whether the note inherits the maxim''s concept
    or only borrows its phrasing. The sentence is a closing remark rather than load-bearing,
    so this is INFO.'
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/20d9dd5d89419f861f19b92b/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/20d9dd5d89419f861f19b92b/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-conceptual-role-conflation.md
raw-output-sha256: eef1d804f1c2baab3b79bc80914f10202a8d62ae45ed84f6de6dd0d3ffe9c43b
---

# Review

Most role assignments in the note are explicit. It applies the text-testing pyramid's Level A/B distinction to its own regime boundary. It names the tag-readme `complete` mark as a shipped object of application, with the contract in the type spec. It positions itself against the frontloading and determinability notes as adding a third class. Its relation to the managed-staleness notes ("specializes", "contrasts") is stated in context.

The one material blur is in the instances list. The list is framed as surfaces in the system in four states of application. Its second bullet instead points to another note's general requirement for memory systems. A reader cannot tell whether the bullet is evidence that the rule already has a stated-but-unenforced instance here, or a predecessor theory the note extends. The footer leans toward the latter. The list's claim that the spread shows generality leans toward the former.
