# Friction check: Oracle accumulation improves selection for later candidates in its maintained domain

**Note:** `kb/notes/oracle-accumulation-improves-the-selection-environment.md`
**Central claim (one sentence):** Where recurrent failures can be partially formalized, retaining their checks in a maintained enforcement channel improves selection across later candidates within the checks' domain and can reuse validation work across those candidates.

## Filter
**Verdict:** SURVIVES

The claimed properties can coexist: a check may be derived from a failure, enforced over later in-scope candidates, and reused while remaining explicitly limited by its demonstrated discrimination, maintenance, and operating costs.

## Signal — thinnest joints
1. **“Reuse can also amortize validation work” / “The claim concerns reusable validation work per improvement”** — UNSUPPORTED — Repeated application shows reuse, but the note never concretizes the accounting unit, comparison baseline, or conditions under which authoring, execution, triage, and maintenance cost less per improvement; its final empirical caveat leaves this part of the central claim unevidenced rather than derived.
2. **“The same reuse can preserve the readable-artifact loop's bounded validation radius, because a useful check is authored once and applied to later changes in its neighborhood.”** — THIN — One-time authorship and neighborhood application establish repeated local use, but not that the validation radius remains bounded: that also requires a specified scope boundary and evidence that dependencies or effects outside the neighborhood do not matter.
3. **“A failure-derived check immediately protects against the observed failure class.”** — THIN — Derivation from one observed failure establishes protection against recurrence only if the check faithfully characterizes the relevant class and is applied on every path; the note later requires broader evidence for domain expansion but does not state the corresponding minimum evidence for the originating class.
4. **“Repeating the operation and retaining its outputs strengthens the selection side independently of the proposal side.”** — THIN — Retaining additional checks can add discriminating constraints without changing proposal generation, but accumulation alone does not establish net strengthening when checks overlap, correlate, conflict, or rot; the scope section names these failure modes without supplying a composition condition.
5. **“For that fragment of retained knowledge, accumulation restores the exhaustive consumption that the retrieval wire lost.”** — HOLDS — Given the stated restriction to a check wired into a validation pass, CI run, or schema gate and to candidates in that channel's scope, automatic enforcement supports exhaustive delivery without retrieval.

## For the human
Concretize the amortization claim first: name the denominator, baseline, and cost boundary that turn repeated check execution into less validation work per improvement.
