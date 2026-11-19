---
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
sources:
  - path: kb/types/tag-readme.md
    role: Exact local completeness-mark contract, authorized stopping shortcut, reactive enforcement and fallback; supports the concrete example, not a universal prohibition.
  - path: kb/types/connect-report.md
    role: Candidate-only report contract; illustrates a judgment-based discovery result with potentially broad dependencies, not a mechanically recomputable copy.
  - path: kb/theory/frontloading-spares-execution-context.md
    role: Reuse and context-saving mechanism, repeated-work amortization and validity-window limits; use its argument, not external study claims.
  - path: kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md
    role: Conditional mechanism of a trusted exhaustive view suppressing retrieval, including the requirement that fallback would actually find more and the explicit utility trade-off.
---

# Commission: Checking retained results as a cost–risk trade-off

## Intended contribution

Explain why retaining a derived result can save work, how reuse amortizes producing and checking it, and why checking frequency depends on the cost of checking relative to the risk of reliance on stale or incorrect information. Write a compact explanatory theory note for agents and KB maintainers, with two concrete contrasting examples doing most of the explanatory work. Replace the old categorical argument; do not surround it with exceptions.

## Must keep

The user approved this shape: reuse benefit, completeness mark versus connect report, then compact checking conditions and limits. A false trusted copy can suppress work that would expose its error; preserve this conditional mechanism without calling every error catastrophic or every hint harmless. The completeness mark permits skipping a membership search; its deterministic check makes enforcement attractive where inexpensive, with reactive enforcement rather than an invented always-current guarantee. A connect report supplies candidate links for evaluation; new material anywhere in the KB may change what a renewed search finds. Reusing it can be reasonable when rerunning discovery costs more than the risk accepted for the task. Do not infer that suggestions have no risk or that their failure is always loud.

Keep mechanical checking distinct from semantic review: the connect report is a contrast case for retained results generally, not a claim that discovery can be re-derived by a fixed rule. Keep the definition of a mechanical check as deriving/comparing against identified available inputs, but distinguish verification cheaper than recomputation in at most one sentence. Checking by full recomputation on every use largely defeats the computational saving from retaining the copy; verification and context-loading costs may differ. Avoid conflating computation amortization across uses with amortization of validator development across artifacts.

Several dependents cite the four existing conditions by number. Preserve a compact numbered treatment where defensible: 1 derivation/comparison rule, 2 locatable copy and source, 3 source available at check time, 4 a sufficiently trustworthy checker. Preserve numbering and recognizable concepts, not unsupported guarantees. Explain briefly that testing or centralizing a validator lowers assurance cost but does not prove correctness; do not open a long regress discussion. Explicitly identify any necessary dependent corrections in the report.

## Must exclude

No universal 'valid/invalid' or 'safe/unsafe' dichotomy for retained copies. No universal prohibition on unchecked copies. No assumption that mechanical checking is free, that every relevant dependency can be enumerated or monitored, or that assurance remains current merely because no change is known. No 'per unchanged version' rule as a general solution for broad dependencies. No invented refresh interval, risk estimate or empirical reliability claim. Do not preserve an enforce-or-omit slogan as universal while nominally softening it elsewhere.

Do not expand into a risk-factor taxonomy or catalogue of maintenance policies. Drop the three nonessential old examples (compiled memory views, hot-path contract values, duplicated AGENTS.md.template files), cache maxim, repeated asymmetry summaries and unrelated open questions. No ADRs as authority for general reasoning; link actual contracts at the examples where useful. No external literature or new named external-source claims are commissioned. The sources' external links do not authorize importing those sources or their observations. No historical narration of this rewrite in the note.

## Reserved decisions

Keep types/note.md and the existing path. The workflow requires the existing title/H1; keep it temporarily, even though the user-authorized new argument no longer supports its universal wording. Treat that as a transition constraint, not a reason to preserve the old body claim. Propose one concise replacement title in the report; do not retitle or edit dependents. Publication needs the user's separate approval. Do not create a lasting brief or edit indexes/contracts as part of this run.

## Current direction

The operator first judged the hint counterexample weak: checking on use remains checking, and 'valid' overstates the property's scope. They then explicitly approved replacing both categorical validity and absolute safety with risk weighing. They emphasized amortization: if checking fully recomputes on every use, the copy loses much of its benefit. They rejected a rigid 'per unchanged version' framing because a result such as a connect report can depend on any part of the KB; incomplete dependency tracking and reuse between reviews are accepted in practice according to risk. They approved a shorter replacement organized around the completeness-mark/connect-report contrast, and requested revision now.

This authorizes narrowing or dropping the role report's relied-on checked-or-absent/forbidden-middle rule, enforce-or-omit regime flip, guaranteed graceful degradation, and automatic omission of judgment-based material. Do not preserve those claims merely because dependents cite them. Keep the genuine conditional mechanism and compact checking conditions. The role report inspected only 30 of 38 linking files; state that limitation in the reconciliation report and do not imply a complete dependency audit. Explain which classes of dependent rationale need correction without modifying them.

Aim for 600–800 words of body, with 850 as an editorial ceiling unless a necessary condition genuinely requires more. Count it rather than guess in the report. Prefer two developed examples over several abstract lists. The proposed mechanism is a qualitative design trade-off, not a numerically calibrated expected-loss policy. State reasoning directly, qualify conditions next to claims, and put evidential bookkeeping in the report. Before returning the candidate, do a sentence-level redundancy pass: delete restatements, contrasts already settled by the previous sentence and source-status disclaimers that add no reader-relevant qualification. The independent reviewer should check compactness as well as support and intent.
