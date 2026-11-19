# Claim account: Quote checking

No write brief was supplied, so the commission alone states intent. The
commission and the reconstruction do not contradict each other. The note is a
compact explanatory theory note (about 650–850 body words) on what quote
checks establish, what assumptions make the results meaningful, and what stays
unverified. Commonplace ADRs serve as bounded cases cited at the claims they
illustrate. They are not a tour and need no repeated discounting. Each limit is
stated once. Evidential accounting goes to the reconciliation report, not the
body.

Suggested shape, not mandatory: (1) opening mechanism: a check is a relation
between two specified texts under a rule; (2) what a wording check establishes
and what it leaves open (the four questions, stated once); (3) what makes
"exact" meaningful: normalization, plus occurrence and location; (4) which
evidence a pass is relative to: source identity, retained versus accessible
versus used material, context budget, intermediaries and chains; (5) `## Scope`.
Sections 1 and 2 may merge.

## 1. A quote check tests one relation between two specified texts under a rule

- **Treatment:** state. This is the opening mechanism.
- **Basis:** I1; Support 2, 3, 4.
- **Content:** a check takes a quoted span, a resolved source text and a
  normalization rule. It reports whether the span occurs in that text (once,
  or inside a range). A result therefore has no meaning until the compared
  bytes and the rule are named.
- **Scope/qualifiers:** applies to textual sources with retrievable bytes.
- **Dependencies:** none; commitments 3–7 depend on it.
- **Destination:** opening paragraph.

## 2. Four separable questions: wording, attribution, context, truth

- **Treatment:** state. Attribution is partly qualified, see below.
- **Basis:** I2; Support 2 (S3 ln 21–23, 121–123; S2 ln 128–131).
- **Content:** (i) wording agreement: do these words occur in the compared
  text? (ii) attribution: is the compared text the named source, and did the
  named author produce it? (iii) context: does the passage, read where it
  occurs, support the use the citing text makes of it? (iv) truth: is the
  quoted claim true? A string check answers only (i). Identity checks
  (commitment 6) answer part of (ii): they bind the compared bytes to a
  recorded capture. Upstream authenticity and authorship stay unverified by
  any mechanism in scope.
- **Scope/qualifiers:** state the limit "string matching does not establish
  meaning, attribution or truth" once, here. Do not restate it in later
  sections.
- **Dependencies:** 1.
- **Destination:** first explanatory section, directly after the opening.

## 3. A quote marker is an assertion; a label alone cannot establish fidelity

- **Treatment:** state.
- **Basis:** Support 1 (S1 ln 17, 39).
- **Content:** marking a span as exact asserts that the wording agrees with a
  source. Without a check, that assertion rests on the author's word. A check
  makes the marker falsifiable for wording agreement only. Markers that never
  claimed exact text (paraphrase) have nothing to match against.
- **Scope/qualifiers:** "falsifiable" covers wording agreement under the
  stated rule, not support or truth (already stated in 2; do not repeat at
  length).
- **Dependencies:** 1, 2.
- **Destination:** with 1–2, preferably as their motivation in the opening or
  first section. This carries the Must-keep insight. Do not reuse the
  incumbent's wording or taxonomy.

## 4. Exactness is relative to a normalization rule, and the rule errs in both directions

- **Treatment:** state with qualifier. Under-normalization is supported. The
  over-normalization side and the code-versus-prose reason are inference,
  presented as plain reasoning.
- **Basis:** Support 3 (S1 ln 21, 43; S3 ln 47, 52–59); I3; conflict C3.
- **Content:** "exact" means "equal after this rule". With too little
  normalization, correct quotes fail on typography or whitespace; S1 judges
  that worse than no check. With too much, substantive edits could pass.
  S1's observed mismatch kinds illustrate this: ellipsis omission, bracketed
  substitution, case changes. Typography and emphasis are noise in prose but
  can be content in code. That explains why a design may choose the rule by
  source kind (S3) and not by citation.
- **Scope/qualifiers:** the S1 counts (87; 63/18/6) are optional. If used,
  give at most one clause and scope it to one corpus. C3 is resolved as a
  two-sided tradeoff, not as one correct rule set. Slicing before
  normalization (S3 ln 47) is optional detail.
- **Dependencies:** 1.
- **Destination:** "what makes exact meaningful" section.

## 5. Occurrence is not location: presence, uniqueness and containment are different tests

- **Treatment:** state.
- **Basis:** Support 4 (S3 ln 15–18, 45–50, 62–64); I4; conflict C1.
- **Content:** a span can occur in a source without identifying which
  occurrence the author means, and a plausible range can point elsewhere.
  Requiring exactly one occurrence, or one complete occurrence inside a
  checked range, removes ambiguity about which passage the span equals.
  Forbidding concatenation of disjoint ranges prevents certifying a passage
  that never existed contiguously. An unchecked locator note supplies context
  but is not evidence.
- **Scope/qualifiers:** uniqueness establishes location, not authorial intent
  or support. This must be explicit (commission). Present C1 as a difference in
  tested property: S1's bare substring presence is a weaker test, and S3 gives
  the reason to strengthen it. Do not narrate the amendment history.
- **Dependencies:** 1, 4.
- **Destination:** same section as 4.

## 6. A pass is relative to which bytes were compared: source identity

- **Treatment:** state.
- **Basis:** Support 5 (S2 ln 19–23, 68–73, 99–104, 154–156).
- **Content:** a check result is meaningful only if the compared bytes are the
  source the citation names. An identity check, such as a checksum against a
  recorded capture with explicit name pairing, binds the compared bytes to
  that capture. Equal bytes at an arbitrary path do not bind them. A mismatch
  or unreadable bytes is a failure, not an invitation to find another copy.
- **Scope/qualifiers:** binds compared bytes to a recorded capture only, not
  the capture to the upstream original (commitment 2). Define "capture" in
  plain words on first use (a retained copy of source bytes taken at one
  time). Do not use "ingest" as a universal stage; if mentioned, it must be
  scoped as Commonplace's artifact.
- **Dependencies:** 1, 2.
- **Destination:** "which evidence" section.

## 7. Version pins and current-byte checks detect different changes

- **Treatment:** state with qualifier, briefly. This is peripheral; one or two
  sentences, or drop.
- **Basis:** I9; Support 5 (S3 ln 68–73, 100–103; S2 ln 99–104); C4.
- **Content:** a pin records identity, and detection happens only when a later
  check compares current bytes against it. A frozen capture is stable and so
  cannot reveal later upstream changes. Checking current bytes catches a
  changed or removed passage at the next check. It misses a changed
  surrounding context when the quoted words survive.
- **Scope/qualifiers:** must not say or imply that a pin by itself detects
  every later edit. Do not import S3's "detects all target edits" unqualified.
  Version-policy comparison gets no section of its own.
- **Dependencies:** 6.
- **Destination:** a sentence within the source-identity paragraph, or Scope.

## 8. Retained, accessible and actually used material are different; missing evidence is not verification

- **Treatment:** state. This is central.
- **Basis:** I5; Support 6 (S2 ln 30–34, 50–54, 62–67, 142–145; S3 ln 64–66,
  72–73, 118–119).
- **Content:** a citation can be checked against an original, a retained
  capture, an intermediary's retained extract, or nothing if bytes are
  missing. A pass means "agrees with the evidence this check used". Material
  that is retained somewhere but absent on this machine is not that evidence.
  Neither is material merely present in a model's context. Missing bytes are
  reported as unverified, never as passed. A silent fallback to whatever copy
  is present makes one citation pass or fail with ambient cache state,
  without declaring that dependency. Some claims depend on broad or
  distributed material that a few retained extracts cannot soundly represent.
  Such claims need the full capture, so they need its availability declared.
- **Scope/qualifiers:** must not conflate current model context, retained
  evidence and the evidence a check used (commission Must exclude).
- **Dependencies:** 1, 6.
- **Destination:** "which evidence" section, as its core.

## 9. Context budget forces selection in context, not lossy storage or inexact passages

- **Treatment:** state as explicit reasoning, briefly and subordinate. It is
  not an organizing argument.
- **Basis:** I11; nearest support S2 ln 30–34; Support 6 (full captures kept
  with checksums, extracts checked exactly). No source discusses model context
  budgets (Gap).
- **Content:** a source larger than a checker's available context must appear
  there as selected passages or a compressed form. This implies neither lossy
  storage in the larger system nor loss of exactness in each selected passage.
  It does mean that a judgment needing broad context cannot be made from the
  selection alone.
- **Scope/qualifiers:** present as reasoning directly, with no "no source
  states this" narration; the gap goes in the reconciliation report. Do not
  revive the universal forced-lossy-retention claim.
- **Dependencies:** 8.
- **Destination:** one to three sentences adjoining 8.

## 10. Exactness and second-hand provenance are independent; checks chain link by link

- **Treatment:** state as inference, presented as reasoning.
- **Basis:** I6, I7; Support 1, 6, 7 (S2 ln 25–28, 50–54, 160–163; S3 ln
  64–66).
- **Content:** a quote can be exact with respect to an intermediary's extract
  and second-hand with respect to the original. Each exact check in a chain
  (capture to extract, extract to note) verifies only its own pair. Semantic
  hops compound: checking a paraphrase against a paraphrase adds a judgment at
  each hop, and rewording at either hop can change the proposition. Exact
  extracts verified against pinned bytes let the semantic check go directly
  to source wording. That moves the one necessary judgment to a single place;
  it does not remove the judgment. Reasoning specific to a target stays in the
  citing text and is checked as inference, not expected in the source
  (S2 ln 77–79; optional).
- **Scope/qualifiers:** do not force verbatim and second-hand into mutually
  exclusive categories (commission). S1's alternative-marker set is a
  labelling choice. Mention it only if needed, without discounting.
- **Dependencies:** 2, 6, 8.
- **Destination:** "which evidence" section, after 8–9.

## 11. Semantic judgment is a separate check with a different cost profile

- **Treatment:** state with qualifier.
- **Basis:** Support 8 (S2 ln 58–60; S4 ln 20, 22); C5.
- **Content:** wording agreement is deterministic, cheap and binary, so it
  can run on every pass. Judging context and support needs a reader of both
  texts. That judgment is costlier and noisier, so it cannot simply block the
  way a wording check does.
- **Scope/qualifiers:** the reliability of semantic judgments is unmeasured
  (Gap); say so plainly beside the claim if it bears on a conclusion. Do not
  present S4's Level A/B terms as settled vocabulary unless linked and
  explained.
- **Dependencies:** 2.
- **Destination:** a sentence or two in section 2, or closing the "which
  evidence" section.

## 12. The derived-copy argument covers the wording relation, when its preconditions hold

- **Treatment:** state with qualifier, briefly. The full derived-copy argument
  gets no section of its own.
- **Basis:** I8; Support 10 (S1 ln 19, 29; S4 ln 14–16, 30–35); C2, C5.
- **Content:** a quoted span is a copy of a source span, and its occurrence is
  mechanically recomputable. So the reason for checking derived copies (a
  false copy misleads silently; an absent one costs one recomputation) applies
  to wording agreement. That is why a wording mismatch can reasonably fail
  rather than warn. It does not apply to the choice of span or its claimed
  use, which are not recomputable. It also needs the ground truth to be
  present at check time. Where captures are local and possibly absent, a
  design must either retain enough exact material or declare the dependency
  and fail closed.
- **Scope/qualifiers:** do not import S4's "forbidden" verdict as proven for
  quotations; the sources do not test that transfer. C2 is resolved by
  treating presence at check time as a condition, not a given. Link S4
  inline at this point as the argument it rests on.
- **Dependencies:** 1, 2, 8.
- **Destination:** one short paragraph, either after 3 (why the marker is
  worth checking) or after 8.

## 13. What a checker does not see

- **Treatment:** leave out of the body, or one Scope bullet with qualifier.
- **Basis:** I10; Support 9 (S1 ln 30, 35, 43; S3 ln 110–112).
- **Content if kept:** an "unresolved" report covers marked candidates the
  extractor found but could not pair. Quotations it never recognized appear
  in no outcome, and their rate is unmeasured.
- **Scope/qualifiers:** must not imply that unresolved reporting detects
  missed quotations. The exclusion of demonstration quotes and extraction
  heuristics is peripheral: leave it out.
- **Dependencies:** 1.
- **Destination:** `## Scope`, if kept.

## 14. Corpus measurements

- **Treatment:** leave out, or at most one illustrative clause, scoped.
- **Basis:** S1 ln 21 (87 candidates); S2 ln 116–118 (4 of 65 pairs reused
  the claim string).
- **Reason:** these are single-corpus observations. The commission names
  historical mismatch measurements as peripheral. The mismatch kinds (in 4)
  carry the explanatory point without the numbers.

## 15. Scope of the whole note

- **Treatment:** state in `## Scope`.
- **Basis:** reconstruction Scope and Gaps.
- **Content:** textual sources with retrievable bytes. Audio, images, oral
  quotation and sources whose original is gone are not covered. The
  transfer beyond agent-operated KBs rests on reasoning, not external
  evidence. Legitimate marked editorial alteration (ellipsis, brackets) has
  no checked contract in the sources. Under a strict wording assertion it
  fails, and whether a segment-wise check could support it is open. Context
  drift under unchanged words has no evaluated detector.
- **Qualifiers:** keep each gap to one line. Use `## Open Questions` only
  for items not already explained in the body.

## Reserved to the operator or workflow

- **Title/H1 and path:** keep the incumbent title and path temporarily for
  this candidate. Do not shape the body to defend the old claim title. Report
  that the authorized retitle to "Quote checking" remains for the session
  agent after publication approval.
- **Frontmatter:** type `types/note.md`; remove the `title-as-claim` trait.
  The collection-contract exception for a topic title is authorized; do not
  edit the contract.
- **Dependents:** do not edit ADR 046, the atomic-step note, the
  Peters–Chin-Yee and ROME ingests, or the claims-and-grounding tag head.
  Report the needed changes in the reconciliation report, including removal
  of implications that rest on "fixed at capture/ingest", "re-capture is the
  only remedy" or the three-layer taxonomy.
- **Write brief:** not authorized; propose its content after the candidate.
- **Publication:** requires the user's separate approval.

## Commitments the note must not make

- Must not infer semantic support, relevance, upstream authenticity,
  authorship or truth from string matching or identity checks (Gap: upstream
  authenticity).
- Must not claim that a unique occurrence proves authorial intent.
- Must not claim that a version pin by itself detects every later edit (C4).
- Must not claim that unresolved reporting catches quotations the extractor
  misses (Gap: extractor miss rate).
- Must not claim measured reliability for semantic grounding checks (Gap).
- Must not present one normalization set as universally correct (C3), or bare
  substring presence as sufficient to locate a passage (C1).
- Must not claim that ground truth is always present at check time (C2).
- Must not keep the universal forced-lossy-retention claim, a mandatory
  locator-layer field, the same-offset argument, "fixed at capture/ingest"
  as a universal ceiling, "re-capture is the only remedy", or "does not
  suppress recomputation".
- Must not treat "ingest" as a universal stage. Must not treat verbatim and
  second-hand as mutually exclusive.
- Must not cite external sources or claim external corroboration; none is
  authorized (Gap: external evidence).
- Must not include an operator procedure, a checklist, or documentation of
  current Commonplace commands.
- Must not narrate the drafting process or repeat source-scope disclaimers.
