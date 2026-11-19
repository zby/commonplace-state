# Reconstruction: Quote checking

Basis for a theory note on quote checking in general: what different checks
establish, the assumptions that make their results meaningful, and what stays
unverified. No write brief was supplied; the commission is the sole statement of
intent. Sources: S1 = ADR 046 (`kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`),
S2 = ADR 073 (`kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md`),
S3 = ADR 094 (`kb/reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md`),
S4 = the derived-copy note (`kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`).

S1–S3 are Commonplace design records. Each records what one system selected and
why; per the commission, they supply bounded cases and stated rationales, not
universal authority. S4 is a theory note whose transfer to quotation needs
assessment (see Inference I1 and Scope).

## Support

### A. What a verbatim claim asserts, and that it is mechanically falsifiable

- A1. A `verbatim` citation "asserts that a quoted span is copied exactly from a
  source retained in the KB." Before ADR 046 nothing checked it; the marker was
  "hand-maintained and trusted." (S1, Context ¶1.)
- A2. The check is a "strict substring test" of the quoted span against the
  source the adjacent markdown link names; S1 classifies it as deterministic,
  near-zero cost ("Level A"), not a judgment-based gate. (S1, Context ¶2.)
- A3. The `verbatim` marker is "the only one that can be mechanically
  falsified"; `paraphrase layer` and `second-hand` "remain unchecked by
  construction — they never claimed exact text, and no derivation rule exists
  for them." (S1, Consequences ¶1.) Note: this paragraph also cites the
  incumbent note by its old title as the reason. That citation is compatibility
  information about S1, not independent support (commission, Current direction).
- A4. Outcome severities chosen: mismatch fails (the note "asserts a
  falsehood"); unresolved warns only in notes with at least one resolvable
  verbatim quote; match passes. The rationale for failing mismatch is the
  derived-copy rule's "silent and unbounded" false-copy failure mode.
  (S1, Decision, outcome list.)

### B. Observed mismatch cases (wording-agreement failures)

- B1. Prototype over a sibling casebook corpus: 63 match, 18 mismatch,
  6 unresolved of 87 candidates, "no false mismatch on manual audit."
  Mismatches were "dominated by editorial omission (`...`), bracketed
  substitution, case changes, and punctuation moved inside the quotation
  boundary." (S1, Context ¶3.) Scope: one corpus, one prototype, Commonplace's
  normalization; a single historical measurement.

### C. Normalization is part of what "exact" means

- C1. Normalization (quote-mark folding, whitespace collapse, emphasis
  stripping, NFKC) is "load-bearing, not polish: an under-normalized checker
  would produce false mismatches on correct quotes, which is worse than no
  check." (S1, Consequences ¶3.)
- C2. Normalization is selected by source kind, not per citation: Git blobs,
  analysis captures, repository snapshots and their retained extracts use
  whitespace-only normalization; ordinary KB Markdown and web or paper
  snapshots also normalize typography and Markdown emphasis. "The source
  resolver selects the rule, never a per-citation switch." (S3, Decision ¶4.)
- C3. Original source lines are sliced before normalization. (S3, Decision ¶3.)
- C4. S3's closing statement: the checker establishes "occurrence, uniqueness,
  and range containment under its normalization rule." (S3, Consequences ¶2.)
  The result is relative to the normalization rule.
- C5. Different matching implementations "let the same quotation receive
  different treatment without a source-kind reason" — the motive for a shared
  matcher. (S3, Context ¶1.)

### D. Occurrence, uniqueness and containment

- D1. "A quotation can occur in a source without identifying one occurrence. A
  plausible line range can point elsewhere in the same file. Presence and range
  bounds alone do not establish that the cited passage occupies the location an
  author gives it." (S3, Context ¶1.)
- D2. Chosen policy: exactly one occurrence in the eligible source region; with
  a range, exactly one complete occurrence inside it; a repeated quote without a
  range fails with its occurrence count; two occurrences on one line require
  more quoted context. (S3, Decision ¶3.) The commission flags this as one
  design's policy, not a universal requirement.
- D3. Separate extracts and disjoint ranges "cannot form a synthetic passage by
  concatenation." (S3, Decision ¶3.)
- D4. Guidance alone "cannot enforce containment or distinguish repeated
  occurrences." (S3, Considered alternatives.)
- D5. S2: source locations in ingests "remain authored locators rather than
  mechanically verified anchors" (S2, Consequences ¶2); S3 later lets a path
  carry a checked line range, while "a trailing locator note supplies context
  but is not evidence." (S3, Decision ¶5.)

### E. Matching does not establish context, support, relevance or truth

- E1. "The evidence boundary must remain separate from mechanical matching.
  Finding one occurrence cannot establish that its context supports the
  attached claim." (S3, Context ¶2.)
- E2. The checker "does not establish truth, relevance, or semantic support."
  (S3, Consequences ¶2.)
- E3. Current-byte verification "does not detect a changed interpretive context
  when the quoted words remain unchanged." (S3, Considered alternatives, hash-pin
  entry.)
- E4. Storing a verbatim copy of every note claim in the ingest would allow
  exact string matching, but "string equality would still not establish source
  support." (S2, Considered alternatives.)
- E5. Source-dependent claims are checked semantically by a separate gate
  (`semantic/grounding-alignment`), applied by a writer/reviewer, against either
  retained quotes or the full pinned snapshot. (S2, Decision ¶3–4, ¶7.)

### F. Retained material vs. analysis vs. full source; what a check had access to

- F1. Primary-source snapshots are ignored local copies; a fresh checkout
  retains source identity and checksum but "not the complete captured source."
  Ingest analysis is tracked, but its summaries and judgments "are
  interpretations. They are not source text." (S2, Context ¶1.)
- F2. Checking a note against a paraphrase that was checked against the source
  "creates two semantic hops, and rewording at either hop can change the
  proposition." (S2, Context ¶2.)
- F3. Two possible inputs to a direct check: "A bounded verbatim passage may
  contain enough source material to judge the note's use. Some claims instead
  depend on broad, distributed, or contextual material that cannot be
  represented soundly by a small set of retained quotes. The full snapshot is
  then required, but it cannot be assumed to exist on every machine."
  (S2, Context ¶3.)
- F4. Quotes route: retained verbatim extracts are read as the only support;
  analytical sections are ignored; "If the quotes are insufficient, the check
  fails; it never silently falls back to a local snapshot." Snapshot route:
  exact-byte checksum and canonical-source equality are verified; missing or
  mismatched bytes are a failure. (S2, Decision, routes.)
- F5. Automatic fallback to any available snapshot "would make the same note
  pass or fail according to ambient cache state without declaring that
  dependency." (S2, Considered alternatives.)
- F6. "Verification against those [retained blockquote] bodies does not imply
  that the separate snapshot check ran on this machine." (S3, Decision ¶5.)
  "Missing source bytes are reported separately from an absent quotation and
  never count as verified." (S3, Decision ¶6.)
- F7. Retained quotes are selected as "the minimum one or more exact passages
  needed for a sound later check" (S2, Decision ¶2); "Quotes retain only the
  minimum passages that ordinary checks need." (S2, Considered alternatives.)

### G. Source identity and version

- G1. The ingest is authoritative for durable source identity; the checksum is
  authoritative for exact captured bytes (S2, Context ¶4, citing ADR 072).
  `snapshot_sha256` is immutable; "Changed source bytes are a new observation
  and require a distinct snapshot basename and ingest path." (S2, Decision ¶8.)
- G2. "Equal bytes do not bind a local path to the ingest being cited."
  Name pairing makes the dependency inspectable; the checksum then verifies the
  bytes. (S2, Considered alternatives, checksum-first.)
- G3. KB prose citations are unversioned and checked against current bytes; an
  append does not invalidate them, but "A removed or changed supporting passage
  can still fail its next check." Snapshots and Git sources keep frozen
  identities. (S3, Decision ¶6.) Hash-pinning every target "detects all target
  edits but cannot distinguish relevant changes from unrelated appends."
  (S3, Considered alternatives.)
- G4. Parsed citation record holds quoted text, source reference, optional
  version, optional line ranges and citing line. (S3, Decision ¶1.)

### H. Pairing a quote with its source, and coverage limits of the checker

- H1. The quote names its source "via the adjacent markdown link" (S1,
  Context ¶2); the checker pairs elements by proximity (S1, Decision, code-fence
  paragraph).
- H2. The extraction heuristic "is not complete, and `unresolved` is how it says
  so rather than passing silently." (S1, Consequences ¶3.)
- H3. A code fence demonstrating the convention is "showing it, not asserting
  it"; scanning one reports a false mismatch. Fences are neutralized. (S1,
  Decision.) S3 likewise excludes quotation bodies from link scans "so source
  examples are not treated as author assertions." (S3, Consequences ¶1.)
- H4. Quote checks are "referential checks": ground truth lives outside the
  document, so they dereference a second artifact. (S1, Consequences ¶4–5.)

### I. The general rule for checking derived copies (S4)

- I1. A copy of information mechanically recomputable from a ground-truth source
  must be "checked" or "absent"; hand-maintained-and-trusted is forbidden.
  (S4, opening ¶.)
- I2. Asymmetry: an absent copy costs a bounded recomputation; a false copy
  causes "silent, unbounded wrongness" by suppressing the recomputation that
  would expose it. (S4, "The asymmetry".)
- I3. Four preconditions: a derivation rule ("natural-language summaries and
  judgments do not" qualify); machine-locatability (a marked region naming its
  source); ground truth existing at validation time; a centralized validator
  that bottoms out. "A derivation rule that is itself a judgment call ... is the
  forbidden state, just relocated one layer down." (S4, "What 'checked'
  requires".)
- I4. Where verification is judgment (Level B), hand-maintained dependent
  artifacts are "unavoidable" and handled by managed staleness and review.
  (S4, "Where the rule applies".)
- I5. "Never write the unenforced natural-language version of a checkable
  claim." (S4, Consequences.)
- I6. S1 applies S4 to `verbatim` quotes, claiming all four preconditions hold.
  (S1, Context ¶2.)

### J. Second-hand provenance (thin)

- J1. The only source mention: the convention has a `second-hand` marker, and it
  is unchecked because it "never claimed exact text." (S1, Context ¶1;
  Consequences ¶1.) No source discusses checking an intermediary's quotation of
  an original, or a chain of checks.

## Inference

- N1. **Wording agreement is a mechanical check only relative to three fixed
  inputs: the quoted span, an identified source text, and a normalization rule.**
  Rests on A2, C1–C4, G1–G3. Change any one and the verdict can change: C1 says
  under-normalization falsely fails correct quotes; by symmetry (not stated in
  the sources) over-normalization would pass quotes that differ in ways a reader
  could care about (case, emphasis, punctuation — cf. B1's mismatch categories).
  So "matches" means "matches under rule R against bytes B."
- N2. **Presence is weaker than location.** Rests on D1–D4. A string found
  somewhere in a source does not show that the author's cited passage is that
  occurrence; uniqueness or containment narrows which passage was meant. S3's
  "exactly one" is one policy that makes occurrence identity mechanical; other
  policies (e.g. accepting any occurrence) would license a weaker inference.
- N3. **A passing mechanical match licenses no inference about context,
  attribution-as-meaning, support or truth.** Rests on E1–E4 and I3's first
  precondition (judgments have no derivation rule). Contextual interpretation
  and support are semantic judgments (E5; S4's Level B, I4), so the derived-copy
  rule's "checked" branch does not reach them. Truth of the quoted claim is a
  further step neither source addresses as checkable.
- N4. **The meaning of a result depends on which evidence the check actually
  read.** Rests on F1, F3, F4, F6, G2. A check against retained extracts, a
  check against a full pinned snapshot, and a check against whatever copy is
  locally present license different inferences; F5 and F6 show a design that
  keeps these distinct rather than letting availability silently change the
  input. The distinction among "what the system retains", "what this checker
  could access" and "what this check used" is supported by F4–F6 as separate
  states; the commission requires not conflating them.
- N5. **Retaining a bounded selection does not make the retained passages
  inexact.** Rests on F3, F7, A1. Retained extracts are exact copies (checkable
  per A2/S3); what they lose is the surrounding context, which can matter for
  claims depending on "broad, distributed, or contextual material" (F3). This
  bears on the commission's context-budget point: selection limits which
  judgments are possible, not the exactness of each selected passage.
- N6. **Intermediate interpretations add semantic hops.** Rests on F2, F1.
  Checking against a paraphrase or analysis compounds judgment; each hop is a
  place the proposition can shift. Applying this to quote chains (intermediary
  quoting an original) is an inference by analogy, not stated by the sources.
- N7. **Label vs. check.** Rests on A1, A3, I5, H2. A label such as `verbatim`
  asserts fidelity; it becomes informative only when a check that could fail it
  runs. Unchecked labels (`paraphrase`, `second-hand`) remain authored claims.
  Unresolved results (H2) are a third state: the label was neither confirmed nor
  refuted. This is the supported core of "a label alone cannot establish
  fidelity."
- N8. **Mechanical checking applies to quotation only partially.** Rests on I3,
  I6, N3. S4's preconditions plausibly hold for the wording-agreement question
  (strict substring under a fixed normalization, adjacent link as locator,
  retained bytes present). They fail for context/support (no derivation rule)
  and fail precondition 3 when the source bytes are absent (F1, F6). So S4
  explains why wording checks should exist; it does not make quote checking as
  a whole Level A. Whether normalization choice is "strict mechanical
  extraction" or a judgment embedded in the validator (I3's warning) is open.
- N9. **Version binding trades sensitivity for stability.** Rests on G1, G3.
  Checking against current bytes catches removal of the quoted words but not
  changed surrounding context (E3); pinning catches all edits but cannot
  separate relevant from irrelevant ones. Neither alone establishes that the
  context the author read is the one now present.
- N10. **Code examples and quoted demonstrations show rather than assert.**
  Rests on H3. A checker must decide which spans are assertions; this is an
  extraction assumption that conditions every result.

## Conflicts

- K1. **Whether `second-hand` and `verbatim` are exclusive.** S1 presents
  `verbatim` / `paraphrase layer` / `second-hand` as alternative "grounding-layer
  marker[s]" (S1, Context ¶1) — read literally, one marker per citation. The
  commission forbids forcing second-hand provenance and verbatim wording into
  mutually exclusive categories. No source argues for exclusivity on
  theoretical grounds; S1 records a convention. Not a conflict between sources,
  but between S1's taxonomy and the commission's direction; the commission
  governs the note.
- K2. **S1's claim that all four derived-copy preconditions hold vs. S4's
  judgment-call warning and S1's own normalization remarks.** S1 calls the test
  "strict substring" (Context ¶2) while also stating normalization is
  load-bearing (Consequences ¶3) and S3 later selects normalization per source
  kind. S4 precondition 4 says a rule that is a judgment call is the forbidden
  state relocated. The sources do not settle whether normalization selection
  counts as mechanical. Keep both sides.
- K3. **Historical vs. amended designs.** S2's list-item Quotes form and
  unverified locators (S2, Decision ¶1; Consequences ¶2) were amended by S3
  (attributed blockquotes, optional checked ranges, uniqueness). S3 itself is
  amended by ADR 105 for analysis citation construction (S3, header), while
  "normalization and uniqueness remain current." Use S2's locator remark as a
  historical case, not current state.

## Scope

- S1–S3 describe one system (Commonplace) at dated points; their policies
  (fail/warn severities, exactly-one occurrence, source-kind normalization,
  fail-closed snapshot route, append-only quotes) are selected values. They can
  illustrate or bound general claims; they do not establish them.
- B1's numbers come from one prototype on one sibling corpus with one
  normalization; they show which mismatch kinds occurred there, not prevalence.
- S4's rule applies only where its four preconditions hold; its own text limits
  the "checked" branch to deterministic derivation and leaves judgment-dependent
  dependents to managed staleness (I4). Applying it beyond wording agreement is
  unsupported.
- S3's "does not establish truth, relevance, or semantic support" is stated for
  its own checker but follows from the general fact that string comparison
  carries no semantic test (N3), so it transfers.
- S2's retained-quote vs. full-snapshot split assumes a design where snapshots
  are local and untracked; the general point (bounded passages may not suffice
  for contextual claims; access varies across checkers) does not depend on that
  storage choice.
- None of the sources discusses model context budgets. The commission's
  statement that a source larger than the available context needs a selective
  or compressed representation in context is the commission's own premise; S2's
  "bounded verbatim passage" vs. "broad, distributed, or contextual material"
  (F3) is the nearest support and concerns retained evidence, not context.

## Gaps

- G-a. **Source chains / intermediary sources.** No source analyses checking a
  quote that an intermediary made of an original, distinct checks at each link,
  or how a second-hand verbatim quote can be exact against the intermediary
  while unverified against the original. Only J1 exists. Any treatment must be
  explicit reasoning, flagged as such.
- G-b. **Attribution as a separate question.** The sources treat source
  identification (link pairing H1, identity G1–G2) but not attribution in the
  sense of whether the quoted words are correctly ascribed to a speaker/author
  within the source (e.g. a source quoting someone else). No support.
- G-c. **Upstream authenticity.** Nothing addresses whether the captured source
  is authentic or faithfully represents its origin; G1 binds bytes to a recorded
  observation only.
- G-d. **Truth of the quoted claim.** Only the negative statement (E2); no
  account of how truth would be assessed.
- G-e. **Model context budget.** No source treats context-window limits (see
  Scope). The commission's constraint must stand as reasoning, not cited support.
- G-f. **Over-normalization risk.** Sources state only the under-normalization
  failure (C1); the opposite direction is inference (N1).
- G-g. **Editorial conventions** (ellipsis, bracketed insertions) appear only as
  mismatch causes (B1). No source discusses whether or how a checker should
  accept marked editorial alterations.
- G-h. **Terms without definition in the sources:** "fidelity", "attribution",
  "contextual interpretation", "capture", "ingest" as a general stage (S2 uses
  it as a Commonplace artifact; the commission forbids using it as an
  unexplained universal stage), "grounding layer", "Level A/B" (S4 points to the
  text testing framework, not supplied), "eligible source region" (S3, not
  defined beyond the Quotes-section and range rules).
- G-i. **External evidence.** No external literature on quotation practice,
  citation accuracy or scholarly verification is authorized; if the note needs
  such claims, it must report the gap.
