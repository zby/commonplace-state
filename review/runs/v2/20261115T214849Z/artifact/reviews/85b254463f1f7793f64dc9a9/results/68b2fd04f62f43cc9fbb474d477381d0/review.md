---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - An unenforced copy is always one missed edit away from the catastrophic state,
    with nothing watching.
  reason: 'DEFEATED — Universal (no stated mode): every unenforced copy can be made
    false by one missed edit. — Counterexample: a copy of an immutable source, such
    as text copied from a pinned snapshot, a released spec version or a fixed commit.
    No edit to the source can occur, so the copy cannot drift and nothing needs watching.
    Any reader can check this case. The commitment survives if its scope is narrowed
    to copies of sources that can change after the copy is made; that qualification
    belongs in a Scope section. — LOCAL — instance'
- scope: passage
  quotes:
  - copy can cause silent, unbounded wrongness when it tells consumers to stop looking
  reason: 'DOUBTFUL — Stated as possibility (''can cause''), but the ''forbidden rather
    than merely risky'' conclusion treats it as the governing case: a false copy''s
    harm is silent and unbounded. — Two cases make it doubtful. First, some stale
    copies fail loudly on first use, such as a hardcoded name list where a missing
    or renamed entry raises an error when used. Second, some staleness is low-stakes,
    such as an approximate count in a landing page. In both cases the harm is signalled
    or bounded, so the asymmetry that justifies an absolute ban does not appear. The
    rule survives if it is restricted to copies whose staleness is silent and whose
    consumers act on them consequentially. — LOCAL — instance'
- scope: passage
  quotes:
  - costs the consumer one bounded recomputation
  reason: 'DOUBTFUL — Universal: an absent copy costs only one bounded recomputation.
    — The linked note on LLM recompute cost says recompute is dear for a model, and
    some derivations are corpus-wide sweeps or full builds. ''Bounded'' then holds
    only in principle, not at a price that makes omission a cheap fallback. This does
    not rescue the trusted copy, because checking is still available. It weakens the
    ''bounded, recoverable'' side of the asymmetry and the claim that checked copies
    ''degrade gracefully''. A cost qualification fixes it. — LOCAL — instance'
- scope: passage
  quotes:
  - mechanical derivation makes verification Level A
  reason: 'DOUBTFUL — Universal: mechanical derivability implies a deterministic,
    near-zero-cost check runnable on every pass. — Mechanical and cheap are separate
    properties. Deterministic derivations can be expensive, such as regenerating a
    large generated index (ADR 025 moved such indexes to build time) or recomputing
    derived artifacts over a big corpus. A check like that cannot run on every pass,
    so ''trusting an unchecked copy now saves nothing'' fails there. The note''s own
    boundary is the check price, so it should key on cheap deterministic checks, not
    on mechanical derivability alone. — LOCAL — instance'
- scope: passage
  quotes:
  - a validator is centralized, versioned, reviewed on every change, and amortized
    across every copy it protects
  reason: 'DOUBTFUL — Comparative: a validator''s cost of correctness assurance is
    far lower than that of N hand-maintained copies. — The amortization argument needs
    N to be large. A single-purpose validator guarding one or two copies (the two
    AGENTS.md.template copies are N=2) amortizes almost nothing. A buggy validator
    that falsely passes also carries a stronger trust signal than an unchecked copy.
    ''Reviewed on every change'' describes good practice, not a property validators
    have by construction. The claim holds where one validator guards many copies or
    is itself tested, and that condition should be stated. — LOCAL — instance'
- scope: passage
  quotes:
  - a compiled cue (a memory system's derived retrieval hint)
  reason: DOUBTFUL — The cited instances are mechanically recomputable copies, so
    their spread shows the rule generalizes. — Many memory systems compile cues and
    views by LLM summarization or abstraction. Precondition 1 excludes such summaries
    as having no derivation rule. The compiled-cue and compiled-view instance therefore
    partly falls outside the rule's own domain and weakens the 'four surfaces' generalization
    evidence. Restrict the instance to mechanically compiled cues. — LOCAL — instance
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: 'DOUBTFUL — Universal: no hand-maintained copy can be safely trusted. —
    Dated or advisory copies are a priced middle state. Examples are a retained report
    quoting counts ''as of'' a commit, or a copy marked as a hint that consumers confirm
    before acting. Consumers trust such a copy only as a record of a moment, or only
    as a starting point. The staleness risk is marked and charged for in the artifact''s
    own domain. Whether these count as ''trusted'' or as ''checked by the consumer''
    should be stated so that legitimate dated records are not swept into the ban.
    — LOCAL — priced-exception'
- scope: passage
  quotes:
  - because verification there is judgment
  reason: 'HOLDS — Universal: outside deterministic derivation, verifying a dependent
    artifact against a changed source is a judgment, so hand-maintained dependents
    are unavoidable and managed staleness applies. — No counterexample was found.
    Fidelity or support checks between a revised source and abstracted text have no
    mechanical comparison, and the note fences this regime off from the rule instead
    of forbidding it.'
- scope: document
  quotes: []
  reason: 'HOLDS — Unstated: the maintainer controls the artifact that holds the copy
    and its validation pipeline, so checking or deleting is always open to them. —
    The hunt considered copies in externally hosted surfaces such as package-registry
    descriptions and published pages. These are generated at build time from the repository
    and can be checked at that point, so the dichotomy remains available within the
    KB''s own artifacts.'
outcome: report
description: Retained report review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: 96acb3ea8677a52982b11837caff4733bcbb766cbc165c93135b05845388c82c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/85b254463f1f7793f64dc9a9/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T214849Z/artifact/reviews/85b254463f1f7793f64dc9a9/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T214849Z
launch: 68b2fd04f62f43cc9fbb474d477381d0
completed-at: '2026-11-15T21:50:29Z'
raw-output: kb/reports/state/review/runs/v2/20261115T214849Z/calls/launches/68b2fd04f62f43cc9fbb474d477381d0/outputs/review.md
raw-output-sha256: a8905ccff01a490b886c6905915b0c7d86b5cbeceba227dafd02382d2264a67a
format: 2
---

# Premise decomposition: A derived copy of recomputable truth must be checked or absent

**Register:** claim
**Central commitment (one sentence):** When an artifact carries a copy of information mechanically recomputable from a ground-truth source, the copy must be machine-checked against that source or not exist; a hand-maintained copy that consumers trust is forbidden.

## Premises and counterexamples

The commitment is normative, and it rests on two lines of support.

**The ban on the middle state.** The note forbids hand-maintained, trusted copies because of an asymmetry:

- An absent copy costs a bounded recomputation.
- A false copy can do silent, unbounded harm.
- Any unenforced copy is one missed edit away from becoming false.

The ban consumes all three premises. It also consumes the stated "no safe middle" exclusion.

**The checked branch.** The note says checking is cheap and available. That requires three premises:

- Mechanical derivation gives a Level A check that costs almost nothing.
- The validator bottoms out instead of reopening the regress.
- The cited instances really are mechanically recomputable copies, which is the note's evidence that the rule generalizes.

Two background premises fence the rule's domain:

- Judgment-based verification belongs to managed staleness, not to this rule.
- The maintainer can add a validator or delete the copy.

The weak points cluster where the note states a premise universally but the argument needs it only under conditions:

- The source can change.
- Staleness is silent and consequential.
- The check is cheap, not merely mechanical.
- One validator guards many copies.
- The copy is not explicitly dated or advisory.

None of these failures reaches the central commitment. Each can be repaired by a scope qualification, so all are routed LOCAL. Taken together, they suggest the note needs a `## Scope` section stating these conditions.

## For the human

Start with the asymmetry premise ("silent, unbounded wrongness"). It is what turns "risky" into "forbidden". It fails for stale copies that fail loudly or matter little, and for copies of immutable sources. Scoping the rule to mutable sources with silent, consequential staleness is the key repair.
