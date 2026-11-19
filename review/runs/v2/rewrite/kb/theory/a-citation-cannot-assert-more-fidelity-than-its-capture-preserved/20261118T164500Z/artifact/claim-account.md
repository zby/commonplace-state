# Claim account: a citation cannot assert more fidelity than its capture preserved

No write brief was supplied. The commission alone carries intent, must-keep,
must-exclude, reserved decisions and current direction. It does not conflict
with the reconstruction's source list. No problem file is needed.

Overall shape the commitments below assume: a short `kb/theory/` note with a
claim title (title and path are reserved; keep them). It opens with a
constructed paraphrase-versus-direct-quotation example, states the general
principle, gives the two exits (narrow the citation, or return to the source),
says what a passed wording check does and does not show, uses Commonplace's
quote checker in at most one illustrative sentence, and ends with `## Scope`.
It stops once the reader knows when to narrow and when to return to the
source. The claim is universal: a citation's asserted fidelity is bounded by
what the retained capture preserves. Its origin is the two ADRs, linked as
`abstracted-from`, not as corroboration.

## 1. Lead example: paraphrase versus direct quotation

- **Commitment.** A writer who retained only a paraphrase of a passage cannot
  present that passage as a direct quotation. A writer who retained the exact
  passage can.
- **Treatment.** State it, as a constructed example. The commission requires
  the note to lead with it.
- **Basis.** No source supplies such an example (Gaps). The author constructs
  it. S2's mismatch kinds are allowed as raw material for how quotation marks
  end up around words that are not the source's words (C2): editorial
  omission with `...`, bracketed substitution, case changes, and punctuation
  moved inside the quotation boundary. The prototype counts must not be used.
- **Scope and qualifiers.** Keep it generic: a writer, a source, a retained
  note or excerpt. Do not tie it to Commonplace's ingest or snapshot
  machinery.
- **Dependencies.** It sets up commitments 2 and 3.
- **Destination.** The opening paragraph or paragraphs, before the general
  statement.

## 2. A paraphrase can preserve an idea without preserving the author's words

- **Commitment.** Paraphrase and quotation preserve different things.
  Rewording can keep the idea, but it drops the wording. Rewording can also
  change the proposition.
- **Treatment.** State it with a qualifier. The commission requires the
  positive half ("can preserve an idea"). The sources do not state it. It
  rests on the author's own argument: rewording is what makes something a
  paraphrase. Present it as the note's own reasoning, not as a sourced
  finding. Add the sourced cautionary half: rewording can change the
  proposition, and an interpretation is not source text.
- **Basis.** C1. S1, Context ¶1: interpretations "are not source text".
  S1, Context ¶2: rewording at either hop "can change the proposition". The
  positive half has no source support (Gaps).
- **Scope and qualifiers.** "Can". Do not claim a paraphrase reliably
  preserves the idea. Do not cite S2's paraphrase or second-hand markers as
  support for this note, because that S2 passage cites this note (Conflicts).
- **Dependencies.** None. Commitments 3 and 5 depend on it.
- **Destination.** Directly after the example, as the principle the example
  shows.

## 3. Quotation marks cannot recover words the capture did not keep

- **Commitment.** A direct quotation asserts that the quoted words are the
  source's words. If the retained material holds only a paraphrase, it has
  no words that could back that assertion. Adding quotation marks to the
  paraphrase claims fidelity the capture did not preserve. This is the
  note's central claim and the title's proposition.
- **Treatment.** State it as inference. It is the note's own argument and is
  the general claim abstracted from the cases (I1, I5).
- **Basis.** I1, which combines C1 with C2. S2, Context ¶1: a verbatim
  citation "asserts that a quoted span is copied exactly from a source
  retained". S2, Decision: a mismatch means the note "asserts false textual
  fidelity". A reader who trusts the assertion may skip source comparison and
  miss the error. This reader consequence may be used as the reason the limit
  matters.
- **Scope and qualifiers.** General, not Commonplace-specific. "Fidelity"
  and "capture" are not defined in either source (Gaps). The note should make
  them plain in context. "Capture" means what was retained. "Fidelity" means
  how closely the citation claims to reproduce the source: exact words,
  idea, or location and context. Do not build a definition around them.
- **Dependencies.** Commitments 1 and 2.
- **Destination.** Opening claim, immediately after commitment 2. It may be
  generalized in one sentence beyond wording to any fidelity claim (greater
  precision, broader support), which leads into commitment 4.

## 4. A bounded retained passage supports some uses; others need the full source

- **Commitment.** A small exact retained passage can be enough to judge some
  uses of a source. Uses that depend on broad, distributed or contextual
  material cannot be soundly supported by a few retained passages and need
  the full source.
- **Treatment.** State it, framed generally. This is the criterion for the
  reader's decision.
- **Basis.** C3. S1, Context ¶3 gives the bounded-versus-broad, distributed
  or contextual contrast. S1, Decision ¶2: retain the minimum exact passages
  needed for a sound later check.
- **Scope and qualifiers.** S1 gives no finer test for deciding which class a
  claim falls into (Scope, Gaps). The note must not invent one. Name the
  absence in `## Scope` or `## Open Questions` if useful. The note may add
  that transfer reasoning belongs to the citing text: do not ask the source
  to contain the citer's conclusion (S1, Decision). It is optional; keep it
  only if it fits the brevity requirement.
- **Dependencies.** Commitment 3.
- **Destination.** Body, after the central claim. It sets up the exits.

## 5. Two honest exits: narrow the citation or return to the source

- **Commitment.** To claim greater precision or broader support than the
  retained material preserves, consult evidence that supplies what is
  missing. Otherwise, narrow the citation to what the capture supports, for
  example a paraphrase attribution instead of a quotation, or a narrower
  claim. Silently relying on material that is not available is not an
  option.
- **Treatment.** State the return-to-source half (must-keep, C3). State the
  narrow half as inference (I2). This commitment is where the note stops: the
  commission ends the note when the reader knows when to narrow and when to
  return.
- **Basis.** C3. S1: when the retained material is insufficient, "the full
  snapshot is then required". C4: failure, not silent fallback. I2:
  narrowing is not named by any source as a remedy (Gaps). It is the author's
  inference, informed by the existence of weaker-fidelity citation forms.
- **Scope and qualifiers.** Do not attribute "narrow the citation" to the
  sources. Do not cite S2's paraphrase or second-hand markers as independent
  support (circular; Conflicts). Use the decision rule from commitment 4 only
  at its stated grain.
- **Dependencies.** Commitments 3 and 4. It also depends on commitment 7
  (missing evidence is not a pass).
- **Destination.** The closing body section, before `## Scope`. End the
  argument here.

## 6. The limit is one of evidence, not a ban on assertion

- **Commitment.** The principle bounds what a citation may claim about its
  evidence. It does not forbid a writer from making a claim. A writer can
  still make the claim at the fidelity the retained material supports, or
  as their own assertion.
- **Treatment.** State it as inference (I4). The commission requires this
  framing ("Make the limit one of evidence").
- **Basis.** I4, from C2 and C4. S1 frames the gate as matching each claim to
  the input that can support it.
- **Scope and qualifiers.** One sentence is enough. The collection contract
  says not to defend against objections already closed, so do not repeat
  this framing.
- **Dependencies.** Commitment 3.
- **Destination.** Near the opening claim, as its framing. Alternatively,
  inside commitment 5's exits, where "narrow" shows that the claim survives
  at lower fidelity.

## 7. Missing evidence is not a pass

- **Commitment.** When the material needed to check a citation is absent,
  the citation is unsupported, not confirmed. Treating an absent source or an
  unresolved check as success makes the result depend on whatever happens to
  be at hand.
- **Treatment.** State it. It is a must-keep, and the sources support it
  directly.
- **Basis.** C4. S1: missing or unreadable bytes are "a failure, not a
  warning". Falling back to an ambient copy would make the same note pass or
  fail according to cache state. S2: `unresolved` is how the check reports
  incompleteness "rather than passing silently". It is never counted as a
  match.
- **Scope and qualifiers.** State it generally. Do not describe the snapshot
  route, ingest routes, or which notes the `unresolved` warning appears in.
  That would teach the validator (excluded).
- **Dependencies.** None. It supports commitment 5.
- **Destination.** One sentence in or beside commitment 5, or beside
  commitment 8.

## 8. A successful wording check verifies a match under its rule against the text used, nothing more

- **Commitment.** A passed wording check shows that the quoted span matches
  the text actually linked, under the check's comparison rule. It does not
  certify that the linked text is the original author's words, that the span
  keeps its original context, or that the quoted claim is true.
- **Treatment.** State the positive part directly (C5). State the "does not
  certify author, context or truth" part as inference (I3), worded as
  following from what the check compares. It is a must-keep.
- **Basis.** C5. S2: the comparison is a substring test under normalization,
  against the linked Markdown source. S1: "string equality would still not
  establish source support". Locators are authored, not mechanically
  verified. Equal bytes do not bind a path to the cited ingest. I3: neither
  source names "original author" or "truth" (Gaps).
- **Scope and qualifiers.** S2 internal tension (Conflicts): S2 says a
  verbatim citation asserts exact copying, but its check is a normalized
  substring test. A pass is a match under the rule, not exact identity. The
  note should say "match under its comparison rule", not "exact".
- **Dependencies.** Commitment 3.
- **Destination.** Body, after commitment 5 or folded into the illustration
  in commitment 9. Keep it brief.

## 9. Commonplace's quote checker as a single illustration

- **Commitment.** Commonplace mechanically checks `verbatim`-marked
  quotations against the Markdown source they link. That check illustrates
  commitment 8: it can falsify a false fidelity claim, but a pass shows only
  a normalized match against the linked text.
- **Treatment.** State it with a qualifier, as an explicitly scoped
  illustration. It is preferably one sentence. It is an illustration, not
  corroboration.
- **Basis.** C5 and S2, Decision ¶1. S2: `verbatim` is the only marker that
  can be mechanically falsified.
- **Scope and qualifiers.** Name it as Commonplace's choice so the
  collection's scoping rule holds. Do not list the normalization steps, the
  extraction heuristic, the `unresolved` rule or the code-fence exclusion.
  Do not explain the tracked/untracked storage design or its history. Link
  ADR 046 (and ADR 073 if cited) as `abstracted-from`, never as evidence that
  corroborates the claim. S1 is amended by ADRs 076 and 094 and records an
  earlier decision. Do not rely on S1's mechanism details.
- **Dependencies.** Commitment 8.
- **Destination.** One sentence attached to commitment 8. Source links go in
  the footer with `abstracted-from` labels. If either ADR is cited in the
  body, use it there as the origin.

## 10. The principle generalizes beyond Commonplace

- **Commitment.** The bound on a citation's fidelity by its capture holds
  for any citing practice, not only Commonplace's markers and validator.
- **Treatment.** State it as the note's universal hypothesis (I5). Do not
  present the ADRs as corroborating it.
- **Basis.** I5, the Scope section, and the collection contract ("Origin is
  not corroboration"; `abstracted-from`).
- **Scope and qualifiers.** Undeclared mode reads as universal. That is
  intended here. `## Scope` should say the claim was abstracted from one
  system's citation design and name the open gap: there is no finer test for
  when a bounded passage is enough.
- **Dependencies.** Commitments 3 to 8.
- **Destination.** Implicit in how the opening claim is phrased. Make it
  explicit in `## Scope` and through the footer `abstracted-from` labels.

## Commitments the note must not make

- Do not claim that any source states that a paraphrase preserves the idea
  while losing the words, or that quotation marks cannot recover words.
  These are the note's own argument (Gaps; I1).
- Do not attribute "narrow the citation" as a remedy to S1 or S2 (Gaps; I2).
- Do not cite S2's `paraphrase layer` and `second-hand` sentence as support.
  It cites this note, so using it would be circular (Conflicts).
- Do not equate a passed check with exact or byte identity (S2 internal
  tension).
- Do not claim that the check source is always available, or that location
  establishes availability (S2 Context ¶2; availability conflict). Do not
  explain the storage layers that cause this (excluded).
- Do not offer a finer decision rule than bounded versus broad, distributed
  or contextual (Gaps).
- Do not claim the checker is trustworthy or complete. S2 says its
  trustworthiness "needs separate support" and its extraction is incomplete.
- Do not use the prototype or corpus counts, legal or copyright reasoning, a
  survey of checking techniques, or instruction in how the validator works
  (commission exclusions).
- Do not define "fidelity" or "capture" as terms. No source defines them.
  Use them plainly.
- Reserved for the operator: the title and path stay as they are. Do not
  split the note or edit its dependents. Publication needs operator
  approval. This account does not decide any of these.
