---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - An *absent* copy costs the consumer one bounded recomputation
  reason: The asymmetry that the note says forces the rule treats absence as costing
    only work. When a model does the recomputation, the recomputation can itself fail
    silently, for example through an incomplete search that returns a plausible but
    partial answer. Absence therefore has its own silent-wrongness mode unless the
    recomputation is done by deterministic code. The rule survives only if 'absent'
    is read as 'replaced by external deterministic derivation', which the note does
    not say.
- scope: passage
  quotes:
  - Dropping one costs consumers a recomputation, never correctness
  reason: Overstated for model consumers. The linked LLM-recompute note says model-side
    derivation can involve 'reasoning unreliably' and 'can fail'. Dropping a checked
    copy moves the consumer onto that fallible path, so correctness can degrade. The
    claim holds only when a command or other code performs the fallback recomputation.
- scope: passage
  quotes:
  - Omission is the fallback, not the optimum.
  reason: The note prices enforcement as near-zero per check but never prices building
    the validator. For a one-off copy, precondition 4's amortization argument does
    not apply. In that case, the rule forces the consumer onto per-use recomputation,
    often by a model, with no comparison against a reviewed hand-maintained copy.
    'Forbidden' needs a sentence explaining why the dominant alternative is always
    cheap enough. One explanation is that a mechanical derivation rule already implies
    a small program that can serve as either the validator or the live query.
- scope: passage
  quotes:
  - the two-copy layout is designed in
  reason: ADR 027 does not design a byte-identical two-copy AGENTS.md.template layout.
    It states that 'Editable source checkouts still read the canonical KB files directly,
    preserving the no-duplicated-scaffold invariant', and it keeps only COLLECTION.md
    templates as real files under src/commonplace/_data/templates/. The citation does
    not support the instance as described. The note also does not say whether the
    instance is checked, absent or unenforced.
- scope: passage
  quotes:
  - each in a different state of application — already enforced, stated but unenforced,
    resolved by omission, and not yet applied
  reason: 'Only two of the four instances clearly declare their state: the complete
    mark is enforced, and hardcoded contract values are resolved by omission. The
    compiled-views instance states a requirement, and the template instance states
    no state at all. The reader cannot match the four claimed states to the four instances,
    which weakens the generalization argument this list is meant to carry.'
outcome: report
attack-outcome: partially lands
description: Controller-only revalidation of retained worker output; no new judgment
contract: report
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/critique-note.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: 6a402875150a2649f57275adda6ca69ae7669f0b06ef57a14b0685e5ff6ab220
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/64f74699436a3efddb0face2/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/64f74699436a3efddb0face2/observation.json
contract-sha256: 5a084df09d1b0de08e2dcd8e2316c8ae5af96860a9ebdfc00fb62dd34597653e
profile:
  harness: claude-code
  launch_model: opus
  effort: medium
  flags:
    allowed-tools: Read,Grep,Glob,Edit(kb/reports/state/review/runs/**),Write(kb/reports/state/review/runs/**)
    disallowed-tools: Bash,NotebookEdit
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T123635Z
launch: 21126e398f51457a933fc4ef3e955aac
completed-at: '2026-11-15T13:09:37.378901+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/21126e398f51457a933fc4ef3e955aac/outputs/review.md
raw-output-sha256: 23d2fe1da73e1e0f80a13012c94decdaa1574b66bd42b47e6e2e16001ff0be46
format: 2
---

# Critique: A derived copy of recomputable truth must be checked or absent

**Note:** kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
**Central commitment:** A copy of information that is mechanically recomputable from a ground-truth source must either be machine-checked against that source or not exist; a hand-maintained copy that consumers trust is forbidden, because an absent copy fails boundedly while a false copy fails silently and without bound.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

This objection comes from the cost-ledger view of caching. Ordinary engineering takes this view when it accepts denormalized copies kept in sync by discipline. The KB's own LLM recompute cost note (`kb/theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md`) takes the same view when it asks for comparing "total expected costs" across the three paths. On this view, "forbidden" rests on an asymmetry that does not hold for the consumers this KB cares about.

The note's asymmetry has two sides. Absence costs "one bounded recomputation", and dropping a copy costs "a recomputation, never correctness". A false copy, by contrast, causes "silent, unbounded wrongness" because it suppresses the check that would expose it. But when the consumer is a model, the recomputation is not a free oracle. A model's search sweep can miss members and report a confident, plausible answer. That is the same control-flow failure the note attributes to stale copies: a plausible result ends discovery. So absence also has a silent-wrongness mode. The linked note says model-side derivation can involve "reasoning unreliably" and "can fail".

Once both sides can fail silently, the choice becomes an empirical comparison of error rates and costs, not a categorical prohibition. Take a slowly changing value that a human reviews on every edit to its source. That copy might be wrong less often than a model's fresh recomputation on each use. The validator that would make the copy "checked" also has a construction cost. The note's amortization argument, "amortized across every copy it protects", does not cover a single one-off copy. For that case, the rule forces the costlier and possibly less reliable path.

## How the note engages it

Partially engaged.

- The note defines "absent" to include "replaced by reading the source live". Read charitably, that covers external deterministic derivation: a command computes the answer and the model reads it. Under that reading, absence really is correctness-preserving. It is also always available whenever precondition 1 holds, because a mechanical derivation rule is a program. That reading defeats the core of the attack: a hand-maintained copy is dominated by either a checked copy or a code-computed live answer. However, the note never states this reading. Its stated asymmetry and its "never correctness" line describe recomputation as if it were always reliable.
- The note concedes that omission has a cost, saying that "Omission is the fallback, not the optimum". But it treats that cost as performance only (build-time or hot-path), not as a correctness risk.
- Precondition 4 answers the regress objection: who checks the validator? It does not answer the authorship-cost objection for a single copy.
- The managed-staleness section limits the rule's scope to the deterministic end, which blocks the broader caching objection for judgment-derived content. This part is well answered.

So the commitment survives in a narrower form. Hand-maintained-and-trusted is dominated whenever a deterministic program can serve as either validator or live query. The note's stated reason, that absence is always correctness-safe, is false for model-side recomputation, and the note does not show that the dominant alternative is always affordable.

## Constructive findings

- Restate the asymmetry with the consumer named: absence is bounded and correctness-preserving when the recomputation is deterministic code. When a model performs it, absence carries its own silent-failure risk. Then say that the rule's "absent" branch means external deterministic derivation where correctness matters.
- Add the dominance argument explicitly: precondition 1 (a mechanical derivation rule) already implies a program, and that program can serve as either the validator or the live query. So hand-maintenance never buys correctness that one of the two allowed states cannot buy. This argument, not the bounded/unbounded asymmetry alone, is what makes "forbidden" rather than "usually unwise".
- Address the cost of building the validator for one-off copies. Either argue that it is always negligible next to the drift risk, or admit an explicit exception regime, such as declaring the copy partial or untrusted. The linked indexes note (`kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`) already accepts this as "explicit reclassification as partial". Clarify that such a copy is untrusted, not hand-maintained-and-trusted.
- Change "never correctness" in Consequences to match the narrowed claim.

## Secondary objections (optional)

- The fourth instance's citation does not support it. ADR 027 says that editable checkouts read canonical files directly, "preserving the no-duplicated-scaffold invariant". It does not design a byte-identical two-copy `AGENTS.md.template` layout. Re-source this instance or replace it, and state whether the duplication is checked.
- The instance list claims four distinct states of application, but only two instances say which state they are in. The generalization argument depends on that spread, so make each instance's state explicit.
- "Unbounded" is stronger than the mechanism the note cites. The indexes note frames suppression as "a conditional mechanism, not a prevalence claim". "Can cause silent wrongness whose extent the copy does not limit" would say what the mechanism actually supports.
