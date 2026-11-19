---
description: "Quote checking in general: what a wording match licenses relative to its span, source text and normalization rule; why it reaches no context, support, attribution or truth; and how the evidence a check read conditions its result"
type: types/note.md
traits: []
tags: [document-system, claims-and-grounding, kb-maintenance]
---

# A citation cannot assert more fidelity than its capture preserved

A label that marks a quotation as exact asserts something about the quotation's relation to a source. The label does not establish that relation. It becomes informative only when a check runs that could fail it. A check of this kind has three outcomes, not two. It can confirm the label, refute it, or leave it unresolved because it could not identify the span or the source. An unresolved result neither confirms nor refutes the label. A label with no mechanical test stays an authored assertion, such as a label saying a passage is a paraphrase or names an intermediary. Such a label makes no claim about exact text, so no rule exists from which its content could be recomputed and compared.

This note explains what different quote checks establish, which assumptions make their results meaningful, and what each leaves unverified. Commonplace's quotation checker, recorded in [ADR 046](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md), [ADR 073](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) and [ADR 094](../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md), supplies bounded cases. Its policies are one design's selections, not requirements for quote checkers in general.

## Four questions a quotation raises

A quotation raises four separate questions. The terms below are this note's definitions.

- **Wording agreement**: do the quoted words occur in the source text, under a stated rule for which differences count?
- **Attribution**: are the words correctly ascribed to the person or document the citation names as having said them?
- **Contextual interpretation and support**: read in its surroundings, does the passage mean what the citing claim needs it to mean, and does it support that claim?
- **Truth**: is what the quoted passage says actually so?

Only wording agreement is a matching question. The checks discussed here do not reach the other three. **Attribution** is separate from **source identification**, which asks which document a check read. The separation follows from reasoning, not from a cited source. A source can itself quote someone else. Quoted words can then match the source exactly while being misattributed to the source's author. **Truth** lies outside every check this note discusses.

## A match is relative to a span, a source text and a normalization rule

Wording agreement is decidable only once three inputs are fixed: the quoted span, an identified source text, and a normalization rule. The rule says which differences between the two are ignored, such as quote-mark style, whitespace, Markdown emphasis or Unicode compatibility forms. So "the quote matches" means "the quote matches under rule R against text T". If any of the three inputs changes, the verdict can change.

The normalization rule can fail in two directions. An under-normalizing checker rejects correct quotations, for example because the source uses curly quotes and the citation straight ones. ADR 046 records the choice of normalization as "load-bearing", because false mismatches on correct quotes are "worse than no check". The opposite direction is this note's inference, not a sourced finding. An over-normalizing checker passes quotations that differ in ways a reader could care about. Case, emphasis and punctuation can change the force or meaning of a sentence. The ADR 046 prototype illustrates which differences occur. Over one casebook corpus, its mismatches were mostly editorial omissions marked with ellipses, bracketed substitutions, case changes and punctuation moved inside the quotation marks. That measurement shows which kinds of divergence arose in one corpus under one rule. It says nothing about how common they are elsewhere. A rule can be fixed per source kind, not per citation, as ADR 094 does. That is one way to stop the same quotation receiving different verdicts for no source-related reason.

Applying a fixed rule is mechanical. Choosing the rule may embed a judgment about which differences matter. The open questions below take this up.

## Finding the words is weaker than locating the passage

A string found somewhere in a source shows that the words occur there. It does not show that the occurrence is the passage the author cited. The same words can occur more than once, and a plausible location can point elsewhere in the same file. A check therefore licenses one of two inferences, depending on its policy. If it accepts any occurrence, it licenses only "these words appear somewhere in this text". If it requires exactly one occurrence, or exactly one inside a stated range, it licenses "this is the passage". ADR 094 selects the second policy. That is a trade-off between strictness and author burden, not the only defensible choice.

Piecewise matching has a further hazard. Separately matched fragments can each pass, while the passage they jointly imply never appears in the source. A checker that matches fragments independently cannot rule this out. Ruling it out needs a containment requirement, which guidance to authors alone cannot enforce.

## A match licenses nothing about context, support, relevance or truth

String comparison carries no semantic test. A passing wording check therefore licenses no inference about whether the passage's context supports the claim it is attached to. It licenses none about the passage's relevance to that claim, and none about whether the passage is true. ADR 094 states this limit for its own checker, but the limit follows from what string comparison is, so it applies to any wording check. Exact copies do not close the gap. Even a store holding a verbatim copy of every claimed passage would allow exact matching without establishing support. Context can also change around unchanged words. A check against the current text of a source still passes if the quoted words survive while the surrounding text that fixed their meaning was edited.

Contextual support therefore needs a separate judgment. That judgment is not mechanical. Its result depends on the evidence it read, as the next sections explain.

## A result means what the evidence it read allows

The same label can be checked against different inputs, and the inputs license different inferences. Three states need to be kept apart:

- **retained material**: what the system as a whole keeps about the source;
- **accessible material**: what this particular checker can reach at the moment it runs;
- **used material**: what this check actually read.

These can come apart. A system can retain a source's identity and checksum in shared storage while the full text exists only on some machines. A check run on another machine has less accessible material than the system retains. If a checker silently falls back to whatever copy happens to be present, the same citation can pass or fail depending on local cache contents. The verdict then depends on something the citation does not declare. ADR 073 and ADR 094 record one design that keeps the states apart. A check routed to retained extracts reads only those extracts and does not fall back to a local copy. A pass against retained extracts does not imply that a full-source check ran. Missing source bytes are reported separately and never count as verified. Missing source bytes are a different outcome from a mismatch: they leave the label unverified, not refuted.

Model context is a fourth thing, distinct from all three states. When a source is larger than the context budget available to a model that reads it, the context can hold only a selective or compressed representation. That says nothing about how much the wider system stores, and it does not make any selected passage inexact. The same holds for retained evidence: a bounded set of exact extracts loses surroundings, not exactness. Selection limits which judgments are possible. A wording check against an exact extract is as sound as one against the full text. A judgment of contextual support may need broad, distributed or surrounding material that a small set of extracts cannot represent.

## Checking against an interpretation adds a semantic hop

A check is direct only when its input is source text. A summary or analysis of a source is an interpretation, not source text. Checking a claim against a paraphrase that was itself checked against the source creates two semantic hops. Rewording at either hop can change the proposition, and each hop is a separate place where meaning can shift.

The following extension is this note's reasoning by analogy; no supplied source states it. A source that quotes an earlier source is an intermediary. A quotation can be verbatim against the intermediary a checker holds while still unverified against the original. Each link in the chain needs its own wording check, against the text at that link, with that link's identity and normalization rule. Intermediary provenance and verbatim wording are therefore separate properties of one citation, not alternative categories. A quotation can be second-hand and verbatim at once. **Upstream authenticity** remains beyond every check discussed here: whether a held source faithfully represents its own origin.

## Source identity and version fix which text a verdict is about

A checksum establishes byte identity: the text read is the text recorded. It does not establish which source a citation means. Equal bytes do not bind a citation to the record it intends, so pairing a citation with a source is a separate step.

Version binding trades sensitivity for stability; that trade-off is this note's inference from the ADR 094 alternatives. Checking against a source's current text is stable under unrelated edits and catches removal of the quoted words. It misses a change to the surrounding context that leaves those words intact. Pinning a citation to an exact version detects every edit, but it cannot separate edits that matter from irrelevant ones, such as an unrelated append. Neither approach shows that the context the author read is the context present now.

## Extraction assumptions condition every result

Before any matching runs, a checker must decide which spans are quotation claims and which source each one cites. ADR 046 records one design's heuristics: it pairs a quotation with an adjacent link by proximity and skips code fences, which show a convention without asserting a quotation. Any such decision can err in two ways. It can treat a demonstration as an assertion and report a false mismatch. Or it can miss a real quotation and leave it silently unchecked. An extractor that reports unresolved cases openly makes the second error visible, instead of letting the quotation pass silently.

## Why wording checks are worth having, and where that argument stops

[A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) argues that a copy of mechanically recomputable information should be either validated or absent. A copy that is maintained by hand and trusted is the dangerous third state. An absent copy costs a recomputation. A false copy suppresses the recomputation that would expose it, so its error is silent and unbounded. That note's rule applies only where four preconditions hold. There must be a derivation rule, a locatable region naming its source, ground truth present at validation time, and a validator that does not itself rest on judgment.

Applying that rule here is this note's inference. For wording agreement, the preconditions plausibly hold. There is a fixed comparison rule, a span paired with a named source, and the source text when it is present. This explains why an exact-wording label deserves a check, and why an unchecked one is worse than no label. It risks silent error, not just an absent assurance. The preconditions fail for contextual support and relevance, because those have no derivation rule. They also fail for any check run where the source bytes are absent. So the rule justifies mechanical wording checks. It does not make quote checking as a whole mechanical. The rest falls to judgment against adequate evidence, which needs review and does not suppress recomputation.

## Scope

- The note covers checks of quotation against source text. It treats truth only negatively and does not describe how truth would be assessed.
- The treatment of attribution, intermediary chains, upstream authenticity, over-normalization and model context budgets is reasoning. None of the cited cases treats these topics.
- The Commonplace cases are one system's selections at dated points. The cases include exactly-one-occurrence matching, normalization chosen by source kind, and a retained-extract route that never falls back to local copies. They illustrate the general claims and are not evidence that those selections are required.
- The ADR 046 mismatch categories come from one prototype on one corpus under one normalization rule. They show what kinds of divergence occurred there, not their prevalence.

## Open Questions

- Is choosing a normalization rule itself mechanical? On one side, once fixed, the rule is applied without judgment, and ADR 046 treats its substring test as deterministic. On the other side, the derived-copy note warns that a derivation rule which is itself a judgment call relocates the forbidden state one layer down. Choosing which differences to ignore may be such a judgment. Fixing the rule per source kind reduces case-by-case choice but does not settle the question.
- Should marked editorial alterations, such as ellipses and bracketed insertions, count as verbatim? Accepting them would change what a passing match certifies: the words agree except at marked points, not that the words agree. This bears on what the normalization rule is taken to preserve.
- What evidence makes a contextual-support judgment adequate for a given claim, and how should a check record which evidence it used?

---

Relevant Notes:

- [A derived copy of recomputable truth must be checked or absent](./a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — extends: applies its checked-or-absent rule to quotation and marks where its preconditions stop holding
- [ADR 046 — Verbatim quotes are validated against their cited source](../reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md) — abstracted-from: one design's wording check, its normalization rationale and its prototype mismatch categories
- [ADR 073 — Untracked source snapshots require ingest grounding](../reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md) — abstracted-from: one design separating retained extracts, full sources and interpretations as check inputs
- [ADR 094 — Quotations require a unique occurrence or a containing range](../reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md) — abstracted-from: one design for occurrence identity, version binding and the stated limits of matching
