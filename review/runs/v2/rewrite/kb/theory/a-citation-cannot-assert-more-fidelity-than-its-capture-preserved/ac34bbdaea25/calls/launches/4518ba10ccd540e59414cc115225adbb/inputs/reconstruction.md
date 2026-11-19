# Reconstruction: Quote checking

Basis for a compact theory note on quote checking in general: what different
checks establish, the assumptions that make their results meaningful, and what
remains unverified. No write brief was supplied; the commission alone states
intent. The commission and the inputs do not contradict each other.

Source keys used below:

- S1 = `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md` (input `source-1`)
- S2 = `kb/reference/adr/073-untracked-source-snapshots-require-ingest-grounding.md` (input `source-2`)
- S3 = `kb/reference/adr/094-quotations-require-a-unique-occurrence-or-a-containing-range.md` (input `source-3`)
- S4 = `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md` (input `source-4`)

Line locators refer to the captured inputs.

S1, S2 and S3 are Commonplace decision records. They support claims about what
one checking design selected and why, plus the general reasons they give for
those selections. S4 is a theory note whose strongest claims are themselves
under assessment. S1 line 39 links to the note being rewritten. That link is
compatibility information, not evidence; nothing below relies on it.

## Support

### 1. A quote marker is an assertion. Unchecked, it is trusted on the author's word

- S1 Context, ln 17: "A `verbatim` citation asserts that a quoted span is copied exactly from a source retained in the KB." Before the decision, "nothing checked it: an author wrote a quote, wrote `verbatim`, and the claim was hand-maintained and trusted."
- S1 Consequences, ln 39: once checked, the `verbatim` marker "becomes load-bearing rather than decorative"; it is "the only one that can be mechanically falsified." `paraphrase layer` and `second-hand` "remain unchecked by construction — they never claimed exact text, and no derivation rule exists for them."
- S4 Consequences, ln 40: "Never write the unenforced natural-language version of a checkable claim … A checkable claim is enforced as a check or not asserted at all." (This is S4's strongest form; see Inference 6 for its applicability.)

### 2. A string check tests wording agreement only

- S3 Context, ln 21–23: "The evidence boundary must remain separate from mechanical matching. Finding one occurrence cannot establish that its context supports the attached claim."
- S3 Consequences, ln 121–123: "The checker establishes occurrence, uniqueness, and range containment under its normalization rule. It does not establish truth, relevance, or semantic support."
- S2 Considered alternatives, ln 128–131: storing a verbatim copy of every note claim would make exact matching possible, "but … string equality would still not establish source support."
- S4 precondition 1, ln 32: a derivation rule exists for "extractable lists, set memberships, and file identity"; "natural-language summaries and judgments do not — there is no comparison a machine can run."

### 3. Exactness is relative to a normalization rule, and the rule matters in both directions

- S1 ln 21: a prototype run found 63 match, 18 mismatch, 6 unresolved across 87 candidates, "with no false mismatch on manual audit." Mismatches were "real failures of the strict assertion, dominated by editorial omission (`...`), bracketed substitution, case changes, and punctuation moved inside the quotation boundary." Scope: one sibling casebook corpus.
- S1 ln 43: normalization ("quote-mark folding, whitespace collapse, emphasis stripping, `NFKC`") "is load-bearing, not polish: an under-normalized checker would produce false mismatches on correct quotes, which is worse than no check."
- S3 Decision, ln 52–59: normalization differs by source kind. Git blobs, analysis captures and repository snapshots use whitespace-only normalization; ordinary KB Markdown and web or paper snapshots also normalize typography and Markdown emphasis. "The source resolver selects the rule, never a per-citation switch."
- S3 ln 47: "Slice original source lines before normalization."

### 4. Occurrence is not location: presence, uniqueness and containment are different tests

- S3 Context, ln 15–18: "A quotation can occur in a source without identifying one occurrence. A plausible line range can point elsewhere in the same file. Presence and range bounds alone do not establish that the cited passage occupies the location an author gives it."
- S3 Decision, ln 45–50: require exactly one occurrence in the eligible region; with a range, exactly one complete occurrence inside it. "Separate extracts and disjoint ranges remain separate regions; they cannot form a synthetic passage by concatenation." A repeated quote without a range fails with its occurrence count; two occurrences on one line require more quoted context.
- S3 Decision, ln 62–64: a path "may carry a checked line range; a trailing locator note supplies context but is not evidence."
- S2 Consequences, ln 166–168: "source locations remain authored locators rather than mechanically verified anchors" (pre-ADR-094 state, amended per S2 ln 15).
- S1 Decision, ln 25 (historical): pairing is by proximity to "the markdown source it links"; S1 ln 19 called the derivation rule "a strict substring test".

### 5. Which source? Identity of the compared bytes

- S2 Context, ln 19–23: snapshots are "ignored local reading copies. A fresh checkout therefore retains an ingest's source identity and snapshot checksum, but not the complete captured source." Ingest analysis is tracked, but its summaries and judgments "are interpretations. They are not source text."
- S2 Decision, ln 68–73 (snapshot route): the checker derives one exact path, "verifies exact-byte SHA-256 and canonical source equality against the ingest", and treats missing, mismatched or unreadable bytes as failure, "not a warning or an invitation to find another copy."
- S2 Considered alternatives, ln 154–156: "Equal bytes do not bind a local path to the ingest being cited. Exact name pairing makes the declared dependency inspectable; the checksum then verifies the bytes at that path."
- S2 ln 99–104: a snapshot checksum is immutable; "changed source bytes are a new observation and require a distinct snapshot basename and ingest path."
- S3 Decision, ln 68–73: KB prose citations "remain unversioned and are checked against current bytes"; an append does not invalidate every citation; "a removed or changed supporting passage can still fail its next check." "Missing source bytes are reported separately from an absent quotation and never count as verified."
- S3 Considered alternatives, ln 100–103: hash-pinning every living target "detects all target edits but cannot distinguish relevant changes from unrelated appends." Current-byte verification "does not detect a changed interpretive context when the quoted words remain unchanged."

### 6. Retained material, accessible material, and the material a check actually used

- S2 Context, ln 30–34: "A bounded verbatim passage may contain enough source material to judge the note's use. Some claims instead depend on broad, distributed, or contextual material that cannot be represented soundly by a small set of retained quotes. The full snapshot is then required, but it cannot be assumed to exist on every machine."
- S2 Decision, ln 62–67 (quotes route): reviewers read only the retained verbatim extracts as support and ignore analytical sections; "If the quotes are insufficient, the check fails; it never silently falls back to a local snapshot."
- S2 Considered alternatives, ln 142–145: automatic fallback "would make the same note pass or fail according to ambient cache state without declaring that dependency."
- S3 Decision, ln 64–66: notes citing an ingest search only its Quotes blockquote bodies; "Verification against those bodies does not imply that the separate snapshot check ran on this machine."
- S3 ln 72–73 and ln 118–119: unavailable ingest snapshots "remain explicitly unverified".
- S2 ln 50–54: retained passages are appended only after the exact snapshot's canonical source and checksum are verified, and each passage is checked to occur in those bytes.

### 7. Intermediaries and semantic hops

- S2 Context, ln 25–28: checking a note against an ingest paraphrase "that was itself checked against the source creates two semantic hops, and rewording at either hop can change the proposition; the ledger makes the judgment easier to run but not sound."
- S2 Consequences, ln 160–163: "The semantic check is direct: note claim to source quote, or note claim to the full pinned source. Ingest analysis … cannot acquire source authority by being tracked."
- S2 ln 116–118 (corpus measurement): only 4 of 65 sampled note-to-ingest pairs reused the normalized claim string. Scope: one Commonplace corpus.
- S2 ln 77–79: target-specific transfer reasoning stays in the citing artifact and is checked as an inference, "rather than asking the source to contain the target's conclusion."

### 8. Semantic judgment is a separate check with a different cost

- S2 Decision, ln 58–60: source-dependent claims are checked directly against source material with a semantic grounding-alignment test.
- S4 ln 20: where verification is judgment, it is "a Level B check … an LLM reading both and judging fidelity or support — too costly to run always and too noisy to block on."
- S4 ln 22: mechanical derivation makes verification "Level A — deterministic, near-zero cost, binary, runnable on every pass."

### 9. What the checker does not see

- S1 Decision, ln 30 and Consequences, ln 43: "The extraction heuristic is not complete, and `unresolved` is how it says so rather than passing silently." Unresolved means "an unpaired verbatim citation" — a marked candidate the parser found but could not pair with a source. S1 warns on it only in notes with at least one resolvable verbatim quote, to avoid firing in text that merely writes about the convention.
- S1 Decision, ln 35 and S3 Consequences, ln 110–112: quotations shown inside code blocks or recognized quotation bodies are demonstrations, not assertions; checkers exclude them so "source examples are not treated as author assertions."

### 10. Severity follows the asymmetry between a false and an absent claim

- S1 Decision, ln 29: "mismatch → fail. The note asserts a falsehood. Per the derived-copy rule the false-copy failure mode is silent and unbounded, so it cannot be a warning."
- S4 ln 14–16: an absent copy costs "one bounded recomputation"; a false copy "can cause silent, unbounded wrongness when it tells consumers to stop looking".
- S4 ln 30–35: enforcement requires (1) a derivation rule, (2) a machine-locatable region naming its source, (3) ground truth that exists at validation time, (4) a validator that is a strict mechanical extraction, centralized and amortized.
- S1 Context, ln 19: claimed all four preconditions held for its quote check, including "the source snapshot is a checked-in file present at validation time."

## Inference

I1. **A check verifies one relation between two specified texts under a rule.**
A quote check takes a quoted span, a resolved source and a normalization rule.
It returns whether the span occurs (once, inside a range) in that source.
Rests on Support 2, 3, 4. Consequences: (a) the result has no meaning without
saying which bytes were compared (Support 5, 6); (b) "exact" means "equal after
this normalization", so a policy choice, not the text alone, fixes what counts
as agreement (Support 3).

I2. **Four questions are separable, and a string check answers only the first.**
(i) Wording agreement: do these words occur in the compared text? (ii)
Attribution: is the compared text the source the citation names, and did the
named author produce it? (iii) Context: does the passage, read where it occurs,
support the use the citing text makes of it? (iv) Truth: is the quoted claim
true? Support 2 rules out (iii) and (iv) from occurrence. Support 5 shows that
identity checks (checksum, canonical-source equality, name pairing) address
part of (ii): they bind the compared bytes to a recorded capture. Nothing in the
sources checks that the capture faithfully represents the original or that the
attributed author wrote it. That upstream part of (ii) is therefore unverified
by any mechanism in the sources (see Gaps).

I3. **Normalization is a two-sided error budget.** Too little normalization
fails correct quotes (S1 ln 43); too much could let substantive edits pass
(inferred: the editorial omissions and bracketed substitutions S1 ln 21 counts
as real mismatches would pass a rule that ignored them). Per-source-kind rules
(S3 ln 52–59) follow from the fact that typography and emphasis are noise in
prose snapshots but can be content in code. Rests on Support 3. S3 states the
rule split but does not state this reason explicitly; the code-content reason is
inference.

I4. **Uniqueness and containment address location, not intent.** A unique
occurrence, or one occurrence inside a checked range, removes ambiguity about
*which* passage the quote is equal to (Support 4). It does not show that the
author meant that passage or that the passage supports the use (Support 2,
S3 ln 21–23). Forbidding concatenation of disjoint ranges (S3 ln 47–49) blocks a
check from certifying a passage that never existed contiguously in the source.

I5. **A pass is relative to the evidence the check actually had.** The same
citation can be checked against (a) an original source, (b) a retained
capture of it, (c) an intermediary's retained extract, or (d) nothing, if bytes
are missing. Support 6 shows a design that keeps these apart: checking against
retained extracts does not imply the capture was checked on this machine; missing
bytes never count as verified; no silent fallback to whatever copy is present.
Generalization: a check result should be read as "agrees with the evidence used",
and retained-but-unavailable material or material merely present in a model's
context is not the evidence a given check used. Rests on S2 ln 30–34, 62–67,
142–145; S3 ln 64–66, 72–73.

I6. **Exactness and second-hand provenance are independent axes.** A quote of
an intermediary's retained extract can be exact with respect to that extract
(S3 ln 64–66) while being second-hand with respect to the original. S2's
retention step checks extracts against the capture at append time (S2 ln 50–54),
so a chain of exact checks is possible; each link verifies only its own pair.
S1's marker set (ln 17) treats `verbatim` and `second-hand` as alternative
markers on one citation; the inference here is that this is a labelling choice,
not a property of quotation. Rests on Support 1, 6, 7.

I7. **Semantic hops compound; string hops can chain.** Paraphrase-to-paraphrase
checking adds a judgment at each hop (S2 ln 25–28). Exact extracts verified
against pinned bytes let a later semantic check go directly to source wording
(S2 ln 160–163). Inference: retaining exact source material moves the single
necessary judgment to one place; it does not remove it. Rests on Support 7, 8.

I8. **The derived-copy argument applies to the wording relation only, and only
when its preconditions hold.** The quoted span is a copy of a source span, and
occurrence is mechanically recomputable (S4 precondition 1). Two limits:
(a) the *choice* of span and its claimed use are not recomputable, so S4's
enforce-or-omit rule covers wording agreement, not support (Support 2, S4 ln
32); (b) precondition 3 (ground truth present at validation time) fails where
captures are untracked local copies (S2 ln 19–23); S1 ln 19 asserted it held
for its corpus. Where it fails, a design must either retain enough exact
material (quotes route) or declare the dependency and fail closed (snapshot
route) — S2's two routes. Whether S4's "forbidden" (rather than "risky") verdict
transfers depends on S4's asymmetry argument (ln 14–16), which the sources do
not test for quotations specifically.

I9. **A version pin records identity; detection needs a comparison.** S3 ln
100–103 says hash-pinning living targets "detects all target edits"; that
detection occurs only when a later check compares current bytes to the pin.
A frozen capture (S2 ln 99–104, S3 ln 70–71) is stable by construction and
therefore cannot show later changes to the upstream original. Current-byte
checking catches changed or removed passages at the next check but misses a
changed surrounding context when the quoted words survive (S3 ln 102–103).
Rests on Support 5.

I10. **`unresolved` reports pairing failures among recognized candidates.** A
quotation the extractor never recognized as a verbatim-marked candidate does
not appear in any outcome. Rests on S1 ln 30, 43 (defines unresolved as an
unpaired verbatim citation). The sources give no measure of such misses.

I11. **Context budget (reasoning only, no source support).** A source larger
than a checker's or reader's available context must be represented there by
selected passages or a compressed form. S2 ln 30–34 is the nearest supported
point: some claims depend on broad or distributed material that a small set of
retained quotes cannot soundly represent, so the full capture is required. The
inference that selection in context implies neither lossy storage in the larger
system nor loss of exactness in each selected passage follows from Support 6
(full captures retained with checksums; extracts checked exactly) but no source
discusses model context budgets.

## Conflicts

C1. **Substring presence vs. unique occurrence.** S1 ln 19 treats the derivation
rule as "a strict substring test" and ln 25 pairs by proximity. S3 ln 15–18 and
45–50 hold that presence alone does not establish the cited passage and require
uniqueness or range containment. S3 is the later, amending decision; it settles
the policy for that system. As general theory the sources disagree on whether
presence suffices as the tested property; S3 gives the reason (repeated
occurrences, misleading ranges).

C2. **Ground truth present at validation time.** S1 ln 19 says the source
snapshot "is a checked-in file present at validation time." S2 ln 19–23 says
primary-source snapshots are ignored local copies absent from a fresh checkout.
These may concern different source kinds (S1's prototype ran over a casebook
corpus linking Markdown sources), but S1 states its precondition generally. Not
settled by the sources beyond S2 being later and S3 ln 72–73 treating ingest
snapshot absence as "conditional and non-blocking".

C3. **Normalization scope.** S1 ln 43 lists one normalization set as load-bearing
(quote folding, whitespace, emphasis, NFKC). S3 ln 52–59 restricts some source
kinds to whitespace-only. S3 is later and settles the selected policy; S1's
general claim that under-normalization is worse than no check and S3's
narrowing for code-like sources pull in different directions for a general
theory.

C4. **Hash pins: "detects all edits" vs. insufficiency.** S3 ln 100–101 says
hash-pinning "detects all target edits". The commission forbids implying that a
version pin by itself detects every later edit. Not a conflict between sources;
I9 reconciles by locating detection in the later comparison. Flagged so the
author does not import S3's wording unqualified.

C5. **Hand-maintained claims: forbidden vs. unavoidable (internal to S4).** S4
ln 10 and 16 forbid hand-maintained-and-trusted copies; S4 ln 20 says in the
judgment regime the hand-maintained dependent artifact "is not forbidden; it is
unavoidable". S4 resolves this by regime (check price). For quote checking this
splits wording (Level A) from support (Level B); see I8.

## Scope

- S1–S3 describe one system's quotation-checking design over Markdown KB
  sources, Git blobs, analysis captures and web/paper/repository snapshots. Their
  general reasons (Support 2, 4, 5, 6, 7) stand without the specific commands,
  marker syntax or file layouts; their policies (thresholds such as "two to ten
  occurrences", per-kind normalization sets, append-only Quotes, severity
  levels) are selections.
- S1's numbers (87 candidates; 63/18/6) and S2's (4 of 65; 119 paraphrased vs
  374 extracts) come from single Commonplace corpora; they illustrate
  mismatch kinds and paraphrase drift but do not estimate rates elsewhere.
- S1 is historical and amended (by S3; terminology note ln 13). S2's ingest
  syntax is amended by S3 (S2 ln 15); its route distinction remains.
- S3's constructor clauses are amended by ADR 105 (S3 ln 11); S3 says
  normalization and uniqueness remain current. ADR 105 is not an authorized
  source.
- S4's preconditions and asymmetry are stated for derived copies of
  recomputable truth generally; their application to quotations is the
  inference in I8, not something S4 tests.
- All support concerns textual sources with retrievable bytes. Nothing covers
  audio, images, oral quotation, or sources whose original is no longer
  retrievable.

## Gaps

- **Upstream authenticity and authorship attribution.** No source gives a
  mechanism or argument for checking that a capture faithfully represents the
  original publication or that the attributed author produced the words. Only
  binding of compared bytes to a recorded capture is supported (Support 5).
- **Model context budget.** No source discusses context limits, selective or
  compressed in-context representation, or its relation to storage. Commission
  requires the point; it must rest on explicit reasoning (I11).
- **Legitimate editorial alteration.** S1 counts ellipsis, brackets and case
  changes as mismatches of the strict assertion; S3 forbids concatenating
  disjoint ranges. No source discusses a contract under which marked editorial
  alterations could be checked as such (e.g. segment-wise), or whether quoting
  conventions that permit them should be supported.
- **Extractor miss rate.** No measurement of quotations the extractor never
  recognizes (I10).
- **Reliability of semantic checks.** S4 calls Level B checks costly and noisy;
  no source measures how well semantic grounding judgments detect
  out-of-context use.
- **Context drift with unchanged words.** S3 ln 102–103 names the blind spot;
  no source proposes or evaluates a detector.
- **Definitions.** "Fidelity", "attribution", "contextual interpretation",
  "intermediary source" and "capture" have no definitions in the sources. "Ingest"
  and "snapshot" are defined only as Commonplace artifacts (S2 ln 19–23,
  36–39); the commission forbids using "ingest" as an unexplained universal
  stage.
- **External evidence.** No external (non-repository) evidence on quotation
  practice in scholarship, journalism or other KB systems is authorized. Any
  claim that the distinctions transfer beyond agent-operated KBs rests on
  reasoning alone.
