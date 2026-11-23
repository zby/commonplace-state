---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - |-
        In a practitioner account that motivated this analysis, Nostalgebraist quotes a public Anthropic write-up about internal coding-agent use comparing multi-agent supervision to babysitting: "I need my juice box opened and it's an emergency that my juice box is opened. And that is voiced with the same level of concern as the one who has sliced their finger and is bleeding." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md), verbatim) and "When you are babysitting, every child brings to you concerns with an equal demand for your attention and the various [Claudes] also do that." ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md), verbatim).
      - |-
        In the same practitioner account, Nostalgebraist describes coding agents as "liable to go off on silly low-value tangents (which they treat with the utmost seriousness)" ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md), verbatim) and observes that "Everything is flattened out; everything is assigned equal importance; every interaction looks and feels the same" ([Nostalgebraist](../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md), verbatim).
    reason: "Four verbatim quotes, verbose repeated attribution, and four duplicate inline links devote roughly half the mechanism section to one practitioner account scoped as motivating origin rather than corroboration. Keep one vivid quote per bullet (the juice-box/bleeding-finger contrast in the first and the tangent description in the second), drop the restating second quotes, and tighten the source setup while retaining the causal caveat on interruption defaults."
    level: warn
  - scope: passage
    quotes:
      - |-
        Three mechanisms in Commonplace illustrate this split at different scales (scoped as local design examples, not corroboration that the split outperforms alternatives):
      - |-
        [ADR 138](../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md) unbundles the three decisions for unattended note revision—a run ends at its first stop with a typed continuation record, an operator's answer to a stop can be recorded so the next run does not re-ask, and commissioning follow-up work such as a rewrite remains a separate decision.
    reason: "The lead-in parenthetical duplicates the evidential caveat already stated in Scope, and the ADR 138 bullet re-walks the three-way unbundling enumerated five lines earlier (echoing 'does not re-ask'). Compressing the ADR 138 gloss to a tighter parallel clause and leaving the evidential scope note in Scope would trim overhead, though the concrete mapping may still aid grounding."
    level: info
outcome: warn
---

# Review

The note is generally well-proportioned across its thesis, causal split, architectural interface, residual frictions, scope, and open questions, with one clear source-quotation overhang in the failure-manifestation bullets and one mild repetition in the Commonplace design examples.

Most of the note's supporting detail earns its space and should not be trimmed. In particular, the brief human-specialist contrast, the preemption of standing priority instructions in always-loaded context, the causal caveat noting that the Anthropic babysitting account does not isolate worker behavior from workflow defaults, and the three residual frictions at the execution–triage boundary each carry a necessary inference step or prevent an obvious objection. By contrast, stacking two verbatim quotes per bullet from the same motivating practitioner ingest—alongside repeated attribution boilerplate and four identical inline citations—expands an illustrative origin far beyond its argumentative role and makes the first two bullets noticeably heavier than the surrounding mechanism.
