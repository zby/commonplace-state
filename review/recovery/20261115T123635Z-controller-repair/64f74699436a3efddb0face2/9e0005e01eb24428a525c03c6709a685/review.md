---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - An *absent* copy costs the consumer one bounded recomputation
  reason: The asymmetry assumes that recomputation by the consumer is correct. In
    this KB the consumer is often an LLM reading the source, as in the cited read-the-contract-live
    skill edits. That recomputation is neither deterministic nor Level A. It can silently
    miss items in the same way a stale copy can. Without this assumption, the bounded-versus-unbounded
    contrast that justifies 'forbidden' does not follow.
- scope: passage
  quotes:
  - Dropping one costs consumers a recomputation, never correctness
  reason: This holds only when the fallback recomputation is a mechanical query. When
    the fallback is an agent re-extracting a list from prose or a contract, dropping
    the copy moves the correctness risk to an unchecked per-call extraction. The note
    does not state the condition under which this claim holds.
- scope: passage
  quotes:
  - A *false* copy can cause silent, unbounded wrongness when it tells consumers to
    stop looking
  - that is why hand-maintained-and-trusted is *forbidden* rather than merely risky
  reason: 'The harm is stated conditionally: it occurs when the copy suppresses further
    search. The rule drops that condition and forbids every hand-maintained copy.
    A copy that does not suppress retrieval, or whose source rarely changes, falls
    under ''risky'' by the note''s own argument, not ''forbidden''.'
- scope: passage
  quotes:
  - natural-language summaries and judgments do not — there is no comparison a machine
    can run, so they stay as live reads or are omitted
  reason: The scope boundary is ambiguous. The opening defines scope as information
    that is 'mechanically recomputable'. That definition places natural-language summaries
    outside scope. This sentence instead treats them as in scope but uncheckable,
    so they must be omitted. Read the second way, the rule forbids hand-written reference
    descriptions of code and CLI behaviour, including this note's own descriptions
    of its instances. The note should say which reading it intends.
- scope: passage
  quotes:
  - Such a copy has exactly two valid states.
  reason: 'Only the ''trusted'' qualifier makes the middle state forbidden. That qualifier
    implies a third state: a hand-maintained copy presented as an unverified hint,
    which consumers re-check before relying on it. The ''exactly two'' claim needs
    either an argument that consumers cannot reliably treat a present copy as untrusted,
    or a narrower wording.'
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
launch: 9e0005e01eb24428a525c03c6709a685
completed-at: '2026-11-15T13:09:37.480640+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/9e0005e01eb24428a525c03c6709a685/outputs/review.md
raw-output-sha256: 6ef5922275bcf44dd3a7b0ba6c531fb9ba9c3fb3a3d055f1259f99c166c5add7
format: 2
---

# Critique: A derived copy of recomputable truth must be checked or absent

**Note:** kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
**Central commitment:** A copy of information that can be mechanically recomputed from a ground-truth source must either be checked by a validator against that source or not exist. Hand-maintained-and-trusted copies are forbidden because an absent copy's cost is bounded, while a false copy's harm is silent and unbounded.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a cost-weighted caching practitioner. This is the stance of database denormalization and pragmatic caching: staleness is a risk priced as drift rate × harm, not a category to forbid. Applied to an agent-operated KB, the strongest version of this objection targets the asymmetry that carries the rule.

The note says the "absent" branch costs "one bounded recomputation" and "never correctness". That is true when the consumer recomputes by running a deterministic query. In this KB, the consumer that "reads the source live" is usually an LLM. The note's own omission example is the 2026-06-10 skill edits, which chose read-the-contract per invocation. In that case, an agent reads a contract and extracts a list on every call. That extraction is a Level B operation in the note's own terms: costly, noisy and unchecked. It can silently drop an item and stop, which is the same failure the note attributes to a false copy. The linked LLM-recompute-cost note even says recomputation is expensive for a model.

So in the setting the rule targets, both branches can fail silently. The trade-off is not "bounded and recoverable against silent and unbounded". It is between two error rates:

- a hand-maintained copy whose author reviews it, which drifts only when the source changes;
- a per-call agent extraction, which errs at some rate on every invocation.

For a source that rarely changes, the hand-maintained copy can have lower expected error. If so, "forbidden" is wrong as a categorical rule. The defensible ordering is narrower: prefer checked; otherwise compare drift risk with recomputation risk.

A second argument supports this. The note states the unbounded harm conditionally: a false copy is catastrophic "when it tells consumers to stop looking". The categorical rule drops that condition. Copies that do not suppress retrieval, such as approximate counts or orientation lists, have a bounded downside even when stale.

## How the note engages it

Partially engaged.

- **What the note covers.** It admits that omission has a cost: "Omission is the fallback, not the optimum"; omission must "pay a build-time or hot-path cost". It also links the LLM-recompute-cost note for the value of keeping a checked copy. Precondition 1 limits enforcement to strict mechanical extraction. Precondition 4 rejects judgment-based derivation rules as "the forbidden state, just relocated one layer down". That shows the author sees the danger of judgment recomputation inside the validator.
- **What the note leaves out.** It does not apply the same scrutiny to the consumer's recomputation in the absent branch. "The asymmetry that forces the rule" treats absence as costing time, not correctness. The Consequences section says this outright ("never correctness"). The "forbidden" argument depends on this unexamined step.

The core preference survives: a checked copy dominates both other options when checking is possible. What is exposed is the categorical prohibition and the claim that omission is always correctness-safe.

## Constructive findings

- State the condition under which absence is correctness-safe: the consumer's recomputation is itself mechanical, such as running a query or tool, and not agent extraction from prose. Where the fallback is LLM extraction, say that omission trades drift risk for per-call extraction risk.
- Keep the condition from the asymmetry in the rule. Either restrict "forbidden" to copies that consumers use to stop searching or to skip the source, or argue that every trusted copy has this effect in practice.
- Decide whether natural-language summaries of recomputable facts are inside scope. If they are inside scope, accept and defend the consequence that hand-written reference descriptions must be omitted. If they are outside scope, move the precondition-1 sentence so it does not read as an omission mandate.
- Address the "hand-maintained but explicitly untrusted hint" state. Either show why consumers cannot reliably treat a present copy as untrusted, or weaken "exactly two valid states".
- One possible strengthening: in the read-live instance, frame enforcement as also removing per-call extraction risk, not only context cost. That would make the hot-path case argue for checking more strongly than it does now.

## Secondary objections (optional)

- **Tension with how the note presents itself.** The instance list ("enforced and shipped", the description of the two-copy `AGENTS.md.template` layout) consists of hand-maintained natural-language claims about recomputable system state. They are reasonable as dated descriptions. Under the broad reading of precondition 1, though, they illustrate the scope ambiguity above.
- **"Unbounded" is asserted, not shown.** The harm of a false copy is bounded by what consumers do with it. The note gives no instance where the wrongness actually propagated without bound. "Silent" carries the argument; "unbounded" adds rhetorical weight without evidence.
- **Precondition 4's amortization argument is a comparative claim stated as settled.** A validator's "unit cost of correctness-assurance is far lower" than N hand-maintained copies is plausible. It does not cover the N = 1 case, such as the single duplicated template file. There, a validator is one more hand-authored artifact protecting one copy.
