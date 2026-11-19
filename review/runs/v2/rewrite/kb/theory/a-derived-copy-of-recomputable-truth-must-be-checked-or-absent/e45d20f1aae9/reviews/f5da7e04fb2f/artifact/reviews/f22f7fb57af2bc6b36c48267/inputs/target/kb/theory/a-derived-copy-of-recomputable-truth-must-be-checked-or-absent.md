---
description: "Retaining a derived result saves rederivation; how often to check it is a qualitative trade-off between checking cost and the risk of relying on it stale or wrong, shown by contrasting a completeness mark with a connect report, with four conditions for a mechanical check"
type: types/note.md
traits: [title-as-claim]
tags: [context-engineering, kb-maintenance, claims-and-grounding]
---

# A derived copy of recomputable truth must be checked or absent

Retaining a derived result saves the work of producing it again. As in [frontloading spares execution context](./frontloading-spares-execution-context.md), one computation can serve many later uses that would otherwise each repeat the derivation. A check that reruns the full derivation on every use does that work again, so the copy keeps little of its computational saving. Verification that only compares the copy against its inputs can cost less than recomputing it.

The risk is relying on a copy that is stale or was wrong. When a consumer treats a false copy as licence to stop, the copy suppresses the work that would have exposed its error, because [indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md). That harm requires the suppressed route to actually find more for the task, and an imperfect copy can still have greater overall utility.

How often to check a retained result therefore depends on the cost of checking relative to the risk of relying on it unchecked. This is a qualitative design trade-off, not a calibrated policy or a rule about which copies may exist.

## A completeness mark: cheap to check, relied on as a stop

A tag head's [`complete: true` mark](../types/tag-readme.md) says the head reaches every artifact carrying its tag, across the declared participating collections, in one hop. Readers may then skip the by-tag `rg` sweep. A false mark is the suppressing case: it tells readers to stop while members are still out there, and the sweep it replaced would have found them.

A mechanical check derives the result from identified, available inputs, or compares the copy against them. Here the inputs are the `tags:` lines of artifacts in an enumerable set of collections and the rule is one-hop reachability, so a validator compares the head against them cheaply, which makes enforcement attractive. Enforcement is reactive: the validator flags a gap when the head is next validated, so between a tagging change and that validation the mark can be false. The assurance is "checked when validated", not "always current". Dropping the mark costs readers one fallback `rg` sweep; that protects readers who fall back, not readers who trust a stale mark. The check also covers only declared tags. Whether an artifact fits a tag's meaning is judged in authoring and review.

## A connect report: costly to rerun, consumed as suggestions

A [connect report](../types/connect-report.md) retains the result of a discovery run: candidate links for a future writer to evaluate, chosen by judgment about what a reader gains from following each one. No fixed rule rederives that result, so reviewing it semantically does not stand in for a missing mechanical check. Its searches range over KB-wide discovery surfaces, so new material anywhere in the KB may change what a renewed search finds, and its dependencies cannot be listed as a fixed input set.

The report does not license a stop the way the mark does, so suppression bites less directly. It still carries risk: a writer who relies on a stale report instead of renewed discovery can miss connections, and the report has no freshness field that would signal the miss. Because rerunning discovery is a full judgment-based search, reusing a report can be reasonable when rerunning costs more than the risk the task accepts.

## How the trade-off places the two

The mark is cheap and exact to check and is relied on as a stop, so frequent mechanical checking pays. The report is costly to rederive, has dependencies that cannot be enumerated, and is consumed as advice, so reuse between reruns is a decision about accepted risk. Either way, assurance does not stay current merely because no change is known.

## Conditions for a mechanical check

A mechanical check is available only when four conditions hold:

1. **A derivation or comparison rule.** A fixed rule re-derives the result from its inputs or compares the copy against them. A result produced by judgment has no such rule.
2. **A locatable copy and source.** The checker can find the copy and the inputs it depends on, through the copy's [lineage](./definitions/lineage.md).
3. **Source available at check time.** The inputs exist and can be read when the check runs.
4. **A sufficiently trustworthy checker.** The checker is itself an artifact whose rederivation can be wrong.

The mark meets all four. The connect report fails 1 and 2 and meets 3 only partly. Failing a condition makes reliance a risk judgment without mechanical assurance; it does not by itself require removing the copy.

Testing a validator, or centralizing it so that one checker serves many artifacts, lowers the cost of assuring condition 4 but does not prove the validator correct. That saving spreads validator development across artifacts, not one result across uses.

## Scope

- The two examples are local contracts that illustrate the trade-off. They do not establish how often either situation occurs.
- The trade-off has no calibrated thresholds, refresh intervals or risk estimates.
- Dependency tracking is often incomplete. Not every dependency can be enumerated or monitored, and the note gives no general refresh rule for results with broad dependencies.
- Condition 4 has no established measure of checker trustworthiness.

---

Relevant Notes:

- [Indexes lower recall when they suppress retrieval that would find more](./indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — grounds: the conditional mechanism by which a trusted false copy suppresses the work that would expose it
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — grounds: the amortization argument and the validity window behind the reuse side of the trade-off
- [LLM recompute cost inverts the store-vs-recompute default](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — grounds: recomputation being dear to a model is what makes retaining a derived result worth its risk
- [The boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: mechanical checking exists only where a deterministic oracle can re-derive and compare
- [tag-readme type spec](../types/tag-readme.md) — evidenced-by: the `complete` mark contract is the example the cheap-check end of the trade-off was abstracted from; it bounds the claim to one local, reactively enforced contract and does not corroborate it
- [connect-report type spec](../types/connect-report.md) — evidenced-by: the advisory, judgment-based report contract bounds the costly-to-rerun end of the trade-off; it does not corroborate the claim
- [An enforced tag-README is a MOC with a machine-checked contract](./an-enforced-tag-readme-is-a-moc-with-a-machine-checked-contract.md) — extends: develops the completeness-mark example into the fuller MOC-plus-contract argument
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](./artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — contrasts: lineage that surfaces review targets for judgment-dependent artifacts, where checking is review rather than mechanical comparison
- [History has one chance to become checkable](./history-has-one-chance-to-become-checkable.md) — contrasts: where condition 3 fails because no later source remains to check against
