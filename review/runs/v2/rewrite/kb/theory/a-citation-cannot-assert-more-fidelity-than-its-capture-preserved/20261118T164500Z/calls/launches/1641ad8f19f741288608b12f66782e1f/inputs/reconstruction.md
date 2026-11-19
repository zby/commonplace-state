# Reconstruction: what a citation can support

Basis for the commissioned contribution: help a writer decide whether the material they retained supports the citation they want to make, framed as a limit of evidence. No write brief was supplied; the commission alone states intent, must-keep, must-exclude and reserved decisions. The commission and the source list agree.

Source paths:

- S1 = `kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md` (input `source-1`). Role: what a retained passage can support versus what requires returning to the source.
- S2 = `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` (input `source-2`). Role: what the Commonplace wording check tests, for one illustration only.

## Support

### C1. An interpretation or paraphrase is not source text

- S1, Context ¶1: an ingest's "summaries, classifications, connection judgments, and limitations are interpretations. They are not source text." Tracking them does not change this (S1, Consequences ¶1: ingest analysis "cannot acquire source authority by being tracked").
- S1, Context ¶2: checking a claim against a paraphrase that was itself checked against the source "creates two semantic hops, and rewording at either hop can change the proposition". A paraphrase ledger "makes the judgment easier to run but not sound."
- S1, Considered alternatives, "Keep the paraphrased Claims ledger": review then "depend[s] on a paraphrase of a paraphrase. The semantic relation that matters remains indirect."
- S2, Consequences ¶1: the `paraphrase layer` and `second-hand` markers "never claimed exact text, and no derivation rule exists for them". (This sentence then links the note being rewritten as its rationale; see Conflicts.)

Neither source states in so many words that a paraphrase preserves the idea while losing the words. S1 supports the weaker and related point that rewording can change the proposition, and that an interpretation is not source text.

### C2. A verbatim citation asserts exact copying from a retained source

- S2, Context ¶1: "A `verbatim` citation asserts that a quoted span is copied exactly from a source retained in the KB."
- S2, Decision, mismatch bullet: a mismatch means "The note asserts false textual fidelity", and "a reader who trusts that assertion may skip source comparison and miss the error."
- S2, Context ¶3: real mismatches were "dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary". These are concrete ways quotation marks are put around words that are not the source's words. (The surrounding counts are empirical; the commission excludes arguing from them.)

### C3. A bounded retained passage can support some uses; others require the full source

- S1, Context ¶3: "A bounded verbatim passage may contain enough source material to judge the note's use. Some claims instead depend on broad, distributed, or contextual material that cannot be represented soundly by a small set of retained quotes. The full snapshot is then required, but it cannot be assumed to exist on every machine."
- S1, Decision, quotes route: when the retained quotes are used as support, "If the quotes are insufficient, the check fails; it never silently falls back to a local snapshot."
- S1, Decision ¶ after routes: writers "apply the same gate to that inference rather than asking the source to contain the target's conclusion" — transfer reasoning belongs to the citing text, not the source.
- S1, Decision ¶2: the retained material is "the minimum one or more exact passages needed for a sound later check".

### C4. Missing evidence is a failure, not a pass

- S1, Decision, snapshot route: "Missing, mismatched, or unreadable bytes are a failure, not a warning or an invitation to find another copy."
- S1, Considered alternatives, "Let the checker fall back to any available snapshot automatically": this "would make the same note pass or fail according to ambient cache state without declaring that dependency."
- S1, Consequences ¶1: a fresh checkout "must fail declared snapshot-dependent uses until the exact observation is restored."
- S2, Consequences ¶3: "The extraction heuristic is not complete, and `unresolved` is how it says so rather than passing silently."
- S2, Decision, unresolved bullet: `unresolved` warns, and only in notes carrying at least one resolvable verbatim quote. Unresolved is never counted as a match.

### C5. What a successful wording check verifies, and what it does not

- S2, Context ¶2: "the comparison rule is a substring test under the checker’s normalization; the adjacent Markdown link locates the source; and the checked-in source is available at validation time. Location alone does not establish availability." Checker trustworthiness "needs separate support".
- S2, Consequences ¶3: normalization is "quote-mark folding, whitespace collapse, emphasis stripping, `NFKC`". A match is therefore a match under that rule, not byte equality.
- S2, Decision ¶1: the check resolves the quotation "against the markdown source it links" — i.e. against the text actually linked and used.
- S1, Considered alternatives, "Store a verbatim copy of every note claim": "string equality would still not establish source support."
- S1, Consequences ¶2: "source locations remain authored locators rather than mechanically verified anchors" — the location (and so the surrounding context) is not checked.
- S1, Considered alternatives, "Use checksum-first lookup": "Equal bytes do not bind a local path to the ingest being cited."
- S2, Consequences ¶1: `verbatim` is "the only one [marker] that can be mechanically falsified".

## Inference

- I1 (quotation marks cannot recover words). From C1 (interpretations are not source text; rewording can change the proposition) and C2 (a verbatim citation asserts exact copying from a retained source): if only a paraphrase was retained, there is no retained text from which exact words could be copied, so a verbatim citation built on it asserts something the retained material cannot back. The sources do not state this directly; it combines C1 and C2.
- I2 (narrow the citation or return to the source). From C3: when the retained passage is enough to judge the use, the citation can stand on it; when the use depends on broad, distributed or contextual material, the retained passage is insufficient and the full source is needed. Combined with C4, a writer without the full source has two honest options: narrow the claim (or its fidelity marker, e.g. to paraphrase) to what the retained material supports, or obtain the source. Silently relying on unavailable material is not an option. The "narrow" option is an inference: S1 describes failure on insufficiency and the snapshot requirement, not rescoping as a remedy; S2's paraphrase/second-hand markers (C1) show weaker-fidelity citations exist.
- I3 (a pass certifies a match, not the source). From C5: the check compares the quoted span against the linked text under a normalization rule. It therefore cannot establish that the linked text is the original author's words, that the span keeps its context (locators are unverified), or that the quoted claim is true (string equality does not establish source support). "Original author" and "truth" are not named in either source; this extends S1's "string equality would still not establish source support" and S2's statement that the check runs against the linked source.
- I4 (the limit is evidential, not a ban on assertion). From C2 and C4: the check fails a citation for asserting fidelity its evidence lacks; S1 frames the gate as matching each claim to the input that can support it. Neither source frames this as forbidding unsupported claims in general; a writer may still make a claim at the fidelity its retained material supports.
- I5 (general principle beyond Commonplace). Both sources describe Commonplace choices. The general claim — a citation's asserted fidelity is bounded by what its retained capture preserves — is a generalization from these cases (`abstracted-from`), not something they corroborate.

## Conflicts

- S2 internal tension: Context ¶1 says a verbatim citation asserts the span "is copied exactly", while Context ¶2 and Consequences ¶3 define the check as a substring test under normalization (quote folding, whitespace collapse, emphasis stripping, NFKC). So a pass is weaker than "exactly". This supports the commission's "a match under its comparison rule"; a writer should not equate a pass with exact identity.
- S2 cites the note being rewritten: S2 Consequences ¶1 explains the unchecked markers with "which is precisely why [a citation cannot assert more fidelity than its capture preserved](...)". This is a dependence of S2 on the note, not independent support for it; using it as support would be circular.
- Availability: S2 Context ¶2 assumes "the checked-in source is available at validation time"; S1 Context ¶1 and ¶3 say the full captured source is not retained in a fresh checkout and "cannot be assumed to exist on every machine". These concern different source kinds (tracked retained quotes versus untracked full captures) and do not contradict each other, but the availability condition the check relies on does not hold for every source.
- Currency of S1: S1 header says it is amended by ADR 076 (quote append moved to grounding) and ADR 094 (attributed blocks, unique occurrences, checked ranges); "The text below records the earlier decision." Neither amendment is an authorized source. The distinctions used here (C3, C4) are not marked as superseded, but mechanism details in S1 may be stale.

## Scope

- Both sources describe Commonplace decisions (ADRs). Their support is for Commonplace's citation markers, routes and validator; the general claim is an abstraction from them (I5).
- S2's check applies only to `verbatim`-marked quotations with an adjacent link to a Markdown source that is available at check time. It reports `unresolved` when extraction fails, and that warning appears only in notes with at least one resolvable verbatim quote (S2 Decision). Code-fenced examples are excluded from checking (S2 Decision ¶ on code).
- S2: the checker's own trustworthiness "needs separate support"; the prototype audit gives bounded evidence only, and no check-cost measurement is recorded (S2 Context ¶2).
- S1's bounded-versus-full distinction is stated for source-dependent claims checked against ingest quotes or a pinned snapshot. "Broad, distributed, or contextual" is the stated class needing the full source; S1 gives no finer test for deciding which class a claim falls into.
- Commission exclusions bound use of the sources: do not teach the validator, survey checking techniques, explain the tracked/untracked (two-layer) storage design or copyright history, or argue from legal or empirical claims (so the prototype counts in S2 and the corpus counts in S1 are not to be used as argument). Use S2 for one illustrative sentence only.

## Gaps

- No source defines "fidelity" or "capture" as used in the title. "Capture" is closest to S1's "complete captured source" / "exact captured bytes"; "fidelity" appears only in S2's "false textual fidelity".
- No source states that a paraphrase preserves the idea while losing the words; S1 supports only that rewording can change the proposition (C1). The must-keep's positive half (a paraphrase *can* preserve an idea) is unsupported and would rest on the author's own argument.
- No source states that "quotation marks cannot recover those words"; this is inference I1.
- No source explicitly says a wording check does not certify the original author, the context, or truth. Support is partial (C5, I3): string equality does not establish source support; locators are not verified; the check runs against the linked text.
- No source names "narrowing the citation" as the remedy when retained material is insufficient; S1 names only failure and the full-source requirement (I2).
- No source supplies a decision rule for when a retained passage is "enough" beyond S1's bounded-versus-broad/distributed/contextual contrast. The commission's stopping point ("when to narrow the citation and when to return to the source") relies on that contrast plus inference.
- Neither source supplies a paraphrase-versus-direct-quotation example of the kind the commission asks to lead with; the author must construct it. S2's mismatch kinds (omission with `...`, bracketed substitution, case changes, moved punctuation) are available as raw material.
