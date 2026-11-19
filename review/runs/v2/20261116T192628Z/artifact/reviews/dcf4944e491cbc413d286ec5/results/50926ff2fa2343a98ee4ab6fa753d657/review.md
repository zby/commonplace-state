---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'grounds: bounds what one successful configuration can establish beyond its originating
    context'
  reason: The `grounds` label promises the premise a reader would verify. Its context
    phrase instead says that the target bounds what this claim can establish. Bounding
    is closer to a scope qualification than to a premise. The edge is still permitted
    (theory to theory), and the target plausibly supplies the transfer item in the
    fit portfolio. A context phrase that names the premise it supplies would make
    the label and phrase agree.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
criterion: kb/theory/COLLECTION.md
note-sha256: fb19806c2e87991bc90a6b8984abf7c2e81a20a64dd98415a4e45501f128c317
criterion-sha256: 9f74342dfb5cf7545fcb86fd25f83adcb83ac367e17d747c07a240f06854659a
target-sha256: fb19806c2e87991bc90a6b8984abf7c2e81a20a64dd98415a4e45501f128c317
target-capture: kb/reports/state/review/runs/v2/20261116T192628Z/artifact/reviews/dcf4944e491cbc413d286ec5/inputs/target/kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md
observation: kb/reports/state/review/runs/v2/20261116T192628Z/artifact/reviews/dcf4944e491cbc413d286ec5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T192628Z
launch: 50926ff2fa2343a98ee4ab6fa753d657
completed-at: '2026-11-16T19:27:06Z'
raw-output: kb/reports/state/review/runs/v2/20261116T192628Z/calls/launches/50926ff2fa2343a98ee4ab6fa753d657/outputs/review.md
raw-output-sha256: c202a949db09281c0bdc51e717a0f20367ae5cf6a4b45c6fc6a0b9e846e79cd2
format: 2
---

# Review

## Summary

The note follows the `kb/theory/` collection contract.

**Placement and the placement test.** The note names no Commonplace selection
or system state. Its intended contribution is a design-space claim: when no
complete fixed oracle decides theory fit, live system use supplies a
provisional selection environment, and that environment can confirm the
system's own misconceptions. Nothing needs scoping, and a substantive
transferable claim remains. It is not a proposal, procedure, definition or
evidence note, so the base collection is the right place.

**Quality goal (explanatory-reach).** The note explains why selection works.
Counterfactual effect separates retrieval from operative fit. It also maps
where selection fails: self-confirmation, workloads that never reach a bad
scope, and blame assignment. Qualifiers in the title and description carry
weight. "Initial" has its own section and a Scope entry. "Without a fixed
oracle" is the condition the argument depends on, and Scope marks it as an
observed current condition, not a proof. Real gaps are named in `## Open
Questions` rather than hedged in the body. The claim reads as universal by
default. Its operative assertions use "can", and its refutation conditions
are recoverable from the portfolio items.

**Defensive clauses.** An earlier finding about the first two Scope bullets
was rejected by the operator. The note's text there has not changed, and I
have no argument the operator's reason fails to address, so I do not raise it
again. The other disclaimers, "This does not make theory fit untestable" and
the paragraph on learned evaluators, add boundaries the earlier text did not
settle. They are not padding.

**Outbound links.** Every link targets `kb/theory/`. The two inline links use
fitting connectives and carry argument weight. The footer edges use authorized
labels with context phrases. One label-phrase mismatch is recorded as an info
finding. No links point into `kb/work/` or `kb/instructions/`. No sources are
cited, so the unquoted-source limit and the origin-versus-corroboration rule
are not engaged.

**Composability.** The body forms one cluster: selection by use, its
vulnerability, and its provisional status. Another note can cite it as a
premise without inheriting unrelated examples.
