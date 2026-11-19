# Claim account: Quote checking

No write brief was supplied, so the commission is the only statement of intent.
It does not contradict itself. The note is an explanatory topic treatment of
quote checking in general. It covers what each kind of check establishes, which
assumptions make a result meaningful, and what stays unverified. It is not a
procedure and not a description of Commonplace commands. It does not need to
defend one overarching claim. ADR 046, ADR 073 and ADR 094 (S1–S3) are one
system's design records. They may be used as bounded cases, abstracted-from
origins, or illustrations. None of them is universal authority, and none
corroborates the general claims (collection contract, "Origin is not
corroboration"). The derived-copy note (S4) is a theory note. The note applies
it only as far as its preconditions reach (see §12).

Claim mode: unless a section says otherwise, the general claims below are
universal conceptual claims about what a check's inputs can license. A reader
refutes one by giving a re-derivable case: a check of the named kind that
licenses the denied inference. Mark inferences and reasoning beyond the sources
as such in the prose. Put open points in `## Open Questions` and limits in
`## Scope` (type contract).

Ordering is advisory. Lead with §1 and §2, the core distinction between a label
and a check, and what a match is relative to. Follow with the inferences a match
does and does not license (§3–§6), then the evidence a check read (§7–§10), then
the derived-copy framing (§12). Section headings are the writer's choice, and
the commission does not require an outline.

## 1. A label asserts fidelity; only a check that could fail it makes the label informative

- **Treatment:** state it. This is the supported core of the commission's "a
  label alone cannot establish fidelity" point. Do not reuse the incumbent's
  wording or taxonomy.
- **Basis:** A1 (the `verbatim` marker was "hand-maintained and trusted" before
  checking), A3 (only `verbatim` can be mechanically falsified, while the other
  markers "never claimed exact text"), I5, H2, inference N7.
- **Scope and qualifiers:** a check has three outcomes: confirmed, refuted, and
  unresolved. An unresolved result neither confirms nor refutes the label (H2).
  A label whose claim has no mechanical test, such as a paraphrase or a
  provenance label, stays an authored assertion. Give the reason: such a label
  makes no claim about exact text, and no derivation rule exists for it (A3, I3).
  Do not cite A3's reference to the incumbent note as support. It is
  compatibility information only.
- **Dependencies:** none. Most of the note builds on this section.
- **Destination:** opening, as the mechanism the note explains.

## 2. Wording agreement is decidable only relative to a quoted span, an identified source text and a normalization rule

- **Treatment:** state it as the note's main mechanism, and mark the
  over-normalization direction as inference.
- **Basis:** A2 (strict substring test against the linked source), C1
  (normalization is "load-bearing", and under-normalization gives false
  mismatches, "worse than no check"), C3, C4 (S3 establishes occurrence "under
  its normalization rule"), C5, G1–G2, inference N1.
- **Scope and qualifiers:** "matches" means "matches under rule R against bytes
  B". If any of the three inputs changes, the verdict can change. Under-
  normalization produces false failures (sourced). Over-normalization passes
  differences a reader could care about, such as case, emphasis and punctuation.
  That direction is inference (gap G-f). Support it with B1's mismatch
  categories, framed as the kinds of difference involved, not as prevalence.
  C2's choice of normalization by source kind may illustrate that the rule can
  be fixed per source kind and not per citation. It is one design's choice, not
  a requirement.
- **Dependencies:** §1.
- **Destination:** early body, right after §1.

## 3. Whether choosing a normalization rule is itself mechanical is unsettled

- **Treatment:** leave it as an open question and give both sides. Do not
  resolve it.
- **Basis:** conflict K2. S1 calls the test "strict substring" while calling
  normalization load-bearing, and S3 selects normalization by source kind. S4's
  fourth precondition says a derivation rule that is a judgment call is "the
  forbidden state, just relocated one layer down" (I3). Inference N8 also leaves
  this open.
- **Scope and qualifiers:** once a rule is fixed, applying it is mechanical.
  Choosing the rule may embed a judgment about which differences matter. The
  sources do not settle whether that choice weakens the mechanical status of the
  check.
- **Dependencies:** §2, §12.
- **Destination:** `## Open Questions`, with a sentence in the body near §2 or
  §12.

## 4. Finding the words in a source is weaker than locating the cited passage

- **Treatment:** state it. Present uniqueness and containment as ways to narrow
  the match, not as required policy.
- **Basis:** D1 ("Presence and range bounds alone do not establish that the cited
  passage occupies the location an author gives it"), D2, D3 (disjoint extracts
  cannot be concatenated into a synthetic passage), D4 (guidance alone cannot
  enforce containment), inference N2.
- **Scope and qualifiers:** S3's "exactly one occurrence, or exactly one inside a
  given range" is one policy that makes occurrence identity mechanical. A policy
  that accepts any occurrence licenses a weaker inference: the words appear
  somewhere, not "this passage". Present the trade-off, not the policy. The
  point about concatenation can stand as a general hazard: separately matched
  pieces can pass while the passage they imply never exists.
- **Dependencies:** §2.
- **Destination:** body, after §2, as the second thing a check can establish.

## 5. A passing match licenses no inference about context, support, relevance or truth

- **Treatment:** state it firmly. It transfers beyond S3 because string
  comparison carries no semantic test (Scope note in the reconstruction).
- **Basis:** E1 ("Finding one occurrence cannot establish that its context
  supports the attached claim"), E2 ("does not establish truth, relevance, or
  semantic support"), E3 (unchanged words with changed interpretive context go
  undetected), E4 (storing exact copies of claims would still not establish
  support), inference N3.
- **Scope and qualifiers:** support and contextual interpretation are semantic
  judgments. Truth of the quoted claim is a further step that the sources do not
  treat as checkable (gap G-d). The note may say truth is outside every check
  discussed here. It must not describe how truth would be assessed.
- **Dependencies:** §2, §4.
- **Destination:** body, central. This is the main limit the note explains.

## 6. Wording agreement, attribution, contextual interpretation and truth are distinct questions

- **Treatment:** the commission requires this distinction. State it as a
  conceptual distinction built by explicit reasoning. Present only wording
  agreement and contextual support as treated by the sources. Mark attribution
  and truth as questions the discussed checks do not reach.
- **Basis:** wording agreement: §2, §4. Contextual interpretation and support:
  E1–E5. Truth: E2 only (G-d). Attribution: no support (G-b). The sources treat
  source identification (H1, G1–G2), not whether quoted words are correctly
  ascribed to a speaker inside the source.
- **Scope and qualifiers:** define each term in the note, because the sources
  leave "fidelity", "attribution" and "contextual interpretation" undefined
  (G-h). For attribution, give the reasoning and label it as reasoning: a
  source can itself quote someone else, so the words can match the source
  exactly while being misattributed to the source's author. Do not cite support
  for this. Keep "source identification", meaning which document the check
  read, separate from "attribution", meaning who said the words.
- **Dependencies:** §2, §5, §11.
- **Destination:** early. It frames the other sections and can sit with §1 or
  just after it.

## 7. A result's meaning depends on which evidence the check actually read

- **Treatment:** state it. The commission requires three separate states:
  material the system retains, material currently accessible to this checker,
  and material this check used.
- **Basis:** F1 (a fresh checkout keeps identity and checksum, "not the complete
  captured source"), F3, F4 (a quotes-only route "never silently falls back to a
  local snapshot"), F5 (falling back to whatever is available makes a pass or a
  fail depend on "ambient cache state"), F6 ("does not imply that the separate
  snapshot check ran on this machine"; missing bytes "never count as verified"),
  G2, inference N4.
- **Scope and qualifiers:** the general point does not depend on Commonplace's
  untracked-snapshot storage (reconstruction Scope). Use S2 and S3 as a bounded
  case of a design that keeps these states apart. Missing source bytes are a
  different outcome from a mismatch. They leave the label unverified, not false.
  Do not merge any of these states with "current model context" (see §8).
- **Dependencies:** §1, §2, §11.
- **Destination:** body, start of the evidence half of the note.

## 8. A bounded selection of a source can keep each passage exact while losing the context some judgments need; context budget is one cause of selection

- **Treatment:** state the retained-evidence point with a qualifier. State the
  context-budget point as the commission's premise plus reasoning, with no cited
  support. Keep it subordinate to the note's purpose and do not make it an
  organizing argument.
- **Basis:** F3 (a bounded verbatim passage "may contain enough"; some claims
  depend on "broad, distributed, or contextual material"), F7 (minimum passages
  for a later check), A1, inference N5. The context budget appears in no source
  (G-e).
- **Scope and qualifiers:** if a source is larger than the available model
  context, the context holds a selective or compressed representation. That
  implies neither lossy storage in the wider system nor inexactness of any
  selected passage (commission, Must keep). Selection limits which judgments are
  possible, especially contextual and support judgments. It does not limit the
  exactness of what was selected. Model context, retained evidence and the
  evidence a check used are three different things and must not be conflated
  (commission, Must exclude).
- **Dependencies:** §5, §7.
- **Destination:** body, inside or right after §7, kept short.

## 9. Checking against an interpretation of a source adds a semantic hop

- **Treatment:** state it for paraphrase and analysis. Its extension to quote
  chains is inference (§10).
- **Basis:** F2 (checking a note against a paraphrase "creates two semantic hops,
  and rewording at either hop can change the proposition"), F1 (summaries "are
  interpretations. They are not source text"), inference N6.
- **Scope and qualifiers:** each hop is a separate place where the proposition
  can shift. A check is direct only when its input is source text.
- **Dependencies:** §5, §7.
- **Destination:** body, evidence half.

## 10. With an intermediary source, exactness against the intermediary and fidelity to the original are separate checks

- **Treatment:** state it as inference, and flag it as reasoning that no
  supplied source makes.
- **Basis:** gap G-a. J1 (the `second-hand` marker exists and is unchecked) is
  the only mention. Inference N6 is an analogy. Conflict K1: S1 presents the
  markers as alternatives, but the commission forbids treating second-hand
  provenance and verbatim wording as mutually exclusive, and the commission
  governs.
- **Scope and qualifiers:** a quotation can be verbatim against the intermediary
  that the checker holds while it remains unverified against the original. Each
  link in the chain needs its own check against the text at that link, with
  that link's identity and normalization (§2, §11). Provenance and wording are
  separate properties of one citation. Do not offer a chain-checking design.
  Upstream authenticity, meaning whether the captured source faithfully
  represents its origin, is unverified by any check discussed (G-c). Name it as
  a remainder, not as a solved or solvable step.
- **Dependencies:** §2, §7, §9, §11.
- **Destination:** body, evidence half, followed by a `## Scope` or
  `## Open Questions` entry.

## 11. Source identity and version determine which text a verdict is about

- **Treatment:** state it with a qualifier. Present the version-binding
  trade-off as inference.
- **Basis:** G1 (changed bytes are a new observation), G2 ("Equal bytes do not
  bind a local path to the ingest being cited"), G3 (current-byte checks catch a
  removed passage but not unrelated appends; hash-pinning "cannot distinguish
  relevant changes from unrelated appends"), E3, G4, inference N9.
- **Scope and qualifiers:** a checksum establishes byte identity, not which
  source a citation means. Pairing a citation with a source is a separate step.
  Checking against current bytes is stable under unrelated edits, but it misses
  interpretive context that changed while the quoted words stayed the same.
  Pinning detects every edit but does not separate relevant edits from
  irrelevant ones. Neither approach shows that the context the author read is
  the context present now. Avoid Commonplace terms such as "ingest" and
  `snapshot_sha256` as general stages. If the note uses them, scope them to the
  case (commission, Must exclude).
- **Dependencies:** §2, §7.
- **Destination:** body, evidence half.

## 12. The rule for checking derived copies covers wording agreement, but not quote checking as a whole

- **Treatment:** state it as inference. Assess S4's applicability and do not
  import S4's strongest claims.
- **Basis:** I1–I3 (checked-or-absent; the asymmetry between an absent copy and
  a false copy; four preconditions, with natural-language judgments excluded),
  I4 (judgment-based dependents need managed staleness and review), I6 (S1
  claims all preconditions hold for `verbatim`), inference N8.
- **Scope and qualifiers:** for wording agreement, the preconditions plausibly
  hold: a fixed rule, a locatable span with a named source, and source bytes
  present. That explains why exact-wording checks are worth having, and why an
  unchecked label risks silent error and not just an absent assurance. The
  preconditions fail for context and support, which have no derivation rule.
  They also fail at validation time when source bytes are absent (F1, F6). The
  normalization question (§3) bears on the fourth precondition. Link S4 as a
  theory note that the argument extends or applies. It is not corroboration.
- **Dependencies:** §1, §2, §3, §5, §7.
- **Destination:** body, late. This section explains why some checks are
  mechanical and others are not.

## 13. Contextual support needs a separate judgment against adequate evidence

- **Treatment:** state it with a qualifier, as the consequence of §5 and §12.
  Do not describe a gate or command.
- **Basis:** E5 (a separate semantic check reads retained quotes or the full
  pinned source), F3, F4 (if retained quotes are insufficient, the check fails
  and does not fall back), I4.
- **Scope and qualifiers:** this judgment is not mechanical, and its result
  depends on the evidence it read (§7). Mention Commonplace's semantic gate at
  most as a scoped example. The commission excludes documenting current
  commands.
- **Dependencies:** §5, §7, §12.
- **Destination:** body, near §12.

## 14. Every result is conditioned on extraction assumptions: which spans count as assertions and which source each span is paired with

- **Treatment:** state it with a qualifier, briefly.
- **Basis:** H1 (the source is the adjacent link, paired by proximity), H2
  (extraction is incomplete, and "unresolved" reports that openly), H3
  (demonstrations "show" rather than "assert"; scanning them gives false
  mismatches), H4 (ground truth lies outside the document), inference N10.
- **Scope and qualifiers:** proximity pairing and fence neutralization are one
  design's heuristics. The general point is that a checker must decide what is a
  quotation claim and what it cites. Errors in that decision produce false
  mismatches or silent omissions before any matching runs.
- **Dependencies:** §1, §2.
- **Destination:** body or `## Scope`, short.

## 15. Observed mismatch kinds in one prototype

- **Treatment:** state it with a qualifier, as an illustrative case.
- **Basis:** B1. Of 87 candidates, 63 matched, 18 mismatched and 6 were
  unresolved, with no false mismatch on manual audit. Mismatches were dominated
  by editorial omission, bracketed substitution, case changes and punctuation
  moved inside the quotation.
- **Scope and qualifiers:** one prototype, one sibling corpus, one
  normalization, one historical measurement. It shows which kinds of
  divergence occurred there, not how common they are. Do not use it as
  corroboration of a general claim. Optional: the writer may use only the
  mismatch categories, or leave the case out.
- **Dependencies:** §2.
- **Destination:** optional illustration inside §2.

## 16. Whether marked editorial alterations should count as verbatim

- **Treatment:** leave it as an open question.
- **Basis:** gap G-g. Ellipses and bracketed insertions appear only as causes of
  mismatch (B1).
- **Scope and qualifiers:** the note may say that accepting marked alterations
  would change what a match certifies, which bears on §2's normalization point.
  It must not propose a convention.
- **Dependencies:** §2, §15.
- **Destination:** `## Open Questions`.

## 17. Severity policy, referential-check cost and historical syntax

- **Treatment:** leave it out, or at most use it as a scoped example.
- **Basis:** A4 (fail, warn and pass severities), H4's cost framing, C2 and D2
  policy details, and K3 (S2's list-item form and unverified locators were
  amended by S3, and S3 was partly amended by ADR 105).
- **Scope and qualifiers:** these are Commonplace selections. If the note
  mentions S2's "authored locators rather than mechanically verified anchors"
  (D5), treat it as a historical case of the presence-versus-location gap, not
  as current state. A locator note that carries context but is not evidence
  (D5, S3) may illustrate §4.
- **Dependencies:** none.
- **Destination:** omit, or use as a brief scoped example.

## 18. Decisions reserved for the operator

- **Title and path:** the user authorized the topic title "Quote checking" and
  the collection-convention exception. The workflow keeps the incumbent title,
  H1 and path for this candidate. Do not shape the body to defend that heading.
  Report that the retitle remains for the session agent after publication
  approval.
- **Type and traits:** keep `types/note.md` and remove `title-as-claim`. Choose
  other traits by content. `has-external-sources` does not apply, because no
  external sources are commissioned.
- **Dependents:** ADR 046, the atomic-step note, the Peters–Chin-Yee and ROME
  ingests, and the claims-and-grounding tag head. Do not edit them. The
  reconciliation report names the changes they need, including removal of
  implications that rest on the old capture-time-ceiling claim, the
  "re-capture is the only remedy" claim, or the three-layer taxonomy.
- **Write brief and publication:** do not add a write brief. Propose its
  content after the candidate. Publication needs separate user approval.
- **Collection contract, sources, tags, indexes and ADRs:** do not change any of
  them.

## Commitments the note must not make

- Do not say that a string match establishes contextual support, relevance,
  upstream authenticity, correct attribution or truth (E1–E4; G-b, G-c, G-d).
- Do not cite source support for attribution, intermediary chains, upstream
  authenticity, model context budgets, over-normalization or editorial
  conventions (G-a to G-g). Each may appear only as explicit reasoning or as an
  open question.
- Do not claim that fidelity is fixed permanently at capture or ingest, that
  re-capture is the only remedy, that retention is necessarily lossy, that
  locator fields are mandatory, or any same-offset argument. None is in the
  reconstruction, and the commission excludes keeping them for their own sake.
- Do not treat "ingest", "capture", "grounding layer" or "Level A/B" as
  universal stages or settled terms without defining or scoping them (G-h).
- Do not treat second-hand provenance and verbatim wording as mutually
  exclusive (K1, commission).
- Do not conflate retained evidence, evidence accessible to a checker, evidence
  a check used, and model context (commission, F4–F6).
- Do not present S3's exactly-one-occurrence rule, normalization by source kind,
  or the fail-closed snapshot route as required for any quote checker. Each is
  one design's selection (Scope).
- Do not claim that quote checking as a whole is mechanical (Level A) on the
  strength of S4 (N8).
- Do not settle whether choosing a normalization rule is mechanical (K2).
- Do not cite S1–S3 or B1 as corroboration of the general claims. Link them as
  `abstracted-from` or as scoped examples.
- Do not add external literature on quotation practice or citation accuracy
  (G-i). If the argument seems to need it, report the gap.
- Do not write procedural checklists or documentation of commands.
