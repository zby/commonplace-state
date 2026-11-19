# How Commonplace machinery helped create the reachability article

## Result

The record supports a strong but bounded conclusion: this article was not a
single model draft followed by cosmetic editing. It emerged through a
human-directed, machine-executed search over claims, organization, evidence,
and wording. Commonplace supplied the persistent source graph, collection
contract, workshop boundary, adversarial review methods, retained review state,
and version-control discipline. Agents used those surfaces to propose and apply
changes. The operator selected direction, authorized claim-level revisions,
rejected or restored edits, and decided when the accumulated argument should be
rebuilt.

The evidence does **not** establish that Commonplace alone caused the article
or that every selected session made a causal contribution. The strongest
causal links are exact commit patches tied to model/session trailers, review
packets tied to before-and-after hashes, and session commands that produced the
commits. File presence, a link, or a session match is weaker evidence and is
reported as context only.

The machine-readable collection result records the exact lineage-commit,
distinct-blob, workshop-revision, review-pair, session, and supporting-input
counts for the latest capture. The article was still receiving small edits as
this report was assembled, so [`collection-results.json`](./collection-results.json)
and the last row of [`git/version-manifest.tsv`](./git/version-manifest.tsv),
rather than prose counts, define the capture boundary.

## Evidence chain

### 1. The article began as a routed synthesis, not an isolated document

The lineage starts on 2026-08-29 as a series-hub article, then splits the
program statement into its own article on 2026-08-30. It moves through these
titles and paths:

1. *A research program for theory-guided program modification*
2. *A research program for theory-mediated system learning*
3. *A research program for learning software factories*
4. *The reachability conjecture: train the house, not the LLM*
5. *The reachability conjecture: the LLM stays fixed, the software house
   learns*

The exact sequence, including rename status, is in
[`git/version-manifest.tsv`](./git/version-manifest.tsv). Every corresponding
file is in [`git/versions/`](./git/versions/). This matters because the final
article did not merely receive a new headline: the 2026-09-02 restart replaced
the old staged research-program body with a constructive reachability
conjecture, while preserving selected concepts and evidence that had survived
earlier work.

The article's live `source_notes` and reader-facing links point into the KB for
the software-house definition, representational forms, program theory, Naur,
the Bitter Lesson, governed behaviour-changing writes, Gödel machines,
opacity, theory-mediated learning, and nearby fixed-model systems. Across all
historical versions, 98 linked or declared inputs were recoverable. Their live
or last-available snapshots are in
[`supporting-inputs/`](./supporting-inputs/), with temporal semantics stated in
its manifest. This is evidence that the KB acted as a source and distinction
store; it is not evidence that every linked note changed every draft.

### 2. The article contract repeatedly shaped the reader-facing form

The articles collection requires a self-contained explanation for a highly
technical reader with no KB context, concrete cases before abstractions where
useful, direct prose, a draft banner, and an onward path into the KB. The exact
contract used at collection time is captured at
[`supporting-inputs/live-checkout/kb/articles/COLLECTION.md`](./supporting-inputs/live-checkout/kb/articles/COLLECTION.md).

The history shows repeated operations that directly implement that contract:
adding and revising the TL;DR, identifying Naur and Schmidhuber for an outside
reader, splitting packed sentences, defining the resource envelope, adding the
draft banner, replacing KB-local shorthand, and checking whether a metaphor
clarified or obscured the claim. The full-pass reports explicitly name the
collection reader and collection fit when selecting edits. This is stronger
than a retrospective resemblance between the article and the contract: the
review machinery loaded the contract and cited it as the basis for concrete
changes.

### 3. Automatic reviews found concrete defects and preserved exact inputs

Two persisted catalog sweeps cover earlier states of the same lineage:

- The research-program version received 35 pairs: 23 pass, nine warn, two
  fail, and one open critique report. The failures were undefined terms and
  unidentified references; warnings covered confidence, orphan references,
  proportion, grounding, underspecification, clause packing, framing, link
  text, and stock phrasing.
- The first reachability-conjecture version received 35 pairs: 29 pass, five
  warn, and one open critique report. The warnings concerned an unidentified
  reference, anthropomorphic framing, pseudo-formalism, an underspecified
  assertion, and parsing ambiguity.

The exact job prompts, note snapshots, criteria, model metadata, and outputs
are in [`reviews/review-jobs/`](./reviews/review-jobs/). The normalized store
export is in [`reviews/database/`](./reviews/database/), and
[`reviews/summary.json`](./reviews/summary.json) gives the combined counts.
This is direct evidence of what the automatic gate machinery saw, not a review
reconstructed against the current article.

The open critiques also changed the argument's burden. The earlier critique
said the proposed experiments could not yet distinguish held theory from
generic structured-context use and lacked a credible better-successor oracle.
The later critique pressed the user-feedback boundary: a user can formally
remain outside the house while functionally supplying the theory selection and
credit assignment that the house is supposed to acquire. Both reports are
preserved as `pair-1-critique-note.md` in review jobs 8736 and 8776.

### 4. Full passes converted many independent judgments into bounded edits

Three full-pass packets are preserved under
[`reviews/full-pass/`](./reviews/full-pass/):

- `20260831T215211Z-db2ad4` selected `keep`, attempted a bounded repair, then
  handed back after the recovery still had a parsing ambiguity. Its later
  resolution became `superseded` because the live article had moved beyond
  the packet's version guard.
- `20260901T221819Z-aa7ecf` selected `revise`. It found two global defeaters in
  the research-program framing: the acquisition probe could pass without
  production-caused acquisition, and the declared assessment could pass while
  missing ordinary family regressions. The operator accepted a revision that
  made the claim relation-relative, added a counterfactual-experience contrast,
  applied local repairs, and deliberately retained three disputed passages.
- `20260902T145819Z-fd6963` selected `keep` for the rewritten conjecture. It
  identified semantic admission and credit assignment as the missing main
  mechanism, added that burden at the update loop, repaired the terms after a
  closing accessibility warning, and finished `ready` without claiming that
  the conjecture was proved.

These packets are especially strong evidence for machinery contribution. Each
retains the source hash, individual review outputs, the selected update, edits,
closing review, recovery when allowed, and final hash. They also retain
non-automatic authority boundaries: claim-changing decisions are handed back
to the operator, and a stale packet is superseded rather than silently applied
to a changed file.

### 5. The workshop layer enabled refoundation instead of endless local repair

The lineage accumulated definitions, experiment design, causal-identification
machinery, and review residue. On 2026-09-02 the operator directed a restart
because the core argument had become hard to see. The
`factory-theory-restart` workshop first decomposed the problem into Naur's
theory burden, where theory could live, learning, bootstrapping, the
theory-builder consequence, and why the route might now work. A later
consolidation replaced seven drafts with one theory centered on fixed LLMs and
computational training over software and notes. The plain-reading revision of
that theory then became the new article body.

All Git-visible revisions of that workshop and the earlier
`agentic-system-learning-refoundation` workshop are in
[`workshops/git-versions/`](./workshops/git-versions/), indexed by
[`workshops/version-manifest.tsv`](./workshops/version-manifest.tsv). The
closing commit says the promoted `theory.md` was byte-identical to the article
at that point and deletes the consumed workshop. This is direct evidence for
the workshop lifecycle: intermediate reasoning was allowed to branch and then
was consumed into the library rather than left as permanent navigation noise.

### 6. Git made revision reversible and preserved disagreement

The lineage is unusually fine-grained. Many commits change one sentence or one
inference direction. Same-commit patches are retained in
[`git/full-commit-patches/`](./git/full-commit-patches/) so the article can be
read with the notes, redirects, or review resolution changed alongside it.

One small episode is diagnostic. A literal-language pass removed the
buy/pay/price framing and several single-word metaphors. Four minutes later,
the next commit restored most of them while keeping four clearer literal
replacements. The record therefore does not show a gate mechanically imposing
one style. It shows an agent applying a criterion, the operator/agent process
judging that the application overshot, and Git allowing a selective
restoration with the reasoning retained in the commit message.

The two pure relocation commits similarly preserve path history while updating
consumers and redirects. The final title emerged after the shorter “train the
house, not the LLM” wording was judged to make “house” read as a gambling
idiom. These are concrete examples of the repo's relocation and atomic-commit
rules supporting semantic as well as mechanical revision.

Twenty-nine pull-request numbers occur in the lineage's commit subjects. The
GitHub capture preserves their branch names, bodies, commits, changed-file
summaries, and merge state. The API returned no discussion comments, review
summaries, or inline review comments for this set. In this case Git and the
agent/review records carry the substantive review evidence; the PR layer mainly
corroborates how branch work was stacked, restacked, merged, or abandoned.

### 7. Agent sessions show the execution, while commit trailers bind outputs

Lineage commits name seven public Claude session IDs and several models,
including GPT-5, GPT-5.6 variants, Claude Fable variants, and Claude Opus. The
local session corpus contains the user instructions, agent analysis exposed by
the runtime, file reads, review orchestration, edit commands, validation, and
commit commands for the available sessions. It is indexed at
[`sessions/session-index.tsv`](./sessions/session-index.tsv).

Commit trailers provide a stronger binding than a text match: for example, the
restart/promotion sequence names `session_018LdxVWUNtrShvRUuhRyMWC`, while the
late title, readability, metaphor, nearest-system, and rival-hypothesis edits
name `session_01BdwF6UcMSvKcaotcd66hrF`. The older research-program lineage is
dominated by `session_012Ma4T7JFQG5nfkHfM5A91a`. Their local JSONL sources are
included where available. Other selected Codex files are often catalog-review
workers; their outputs should be interpreted through the persisted review job
rather than treated as independent authorship.

### 8. The record shows human–machine co-creation, not autonomous authorship

The operator's role is load-bearing throughout the evidence:

- user messages choose the subject, reject accumulated complexity, and direct
  the restart;
- the accepted `revise` packet records `resolution_authority: user`;
- full-pass rules prevent a model from silently choosing a new thesis when the
  strongest objection requires a claim change;
- commit history records deliberate divergences from review advice as well as
  accepted repairs;
- later sessions weaken overstrong statements about nearby systems, add a
  rival hypothesis, and restore wording after an over-literal pass.

The machinery's contribution was to make more of the search executable and
inspectable: retrieve relevant distinctions, produce candidate prose, attack
premises, test collection fit, retain exact judgments, guard versions, apply
bounded repairs, and preserve every accepted or reversed state. The operator
still supplied research direction and final authority over substantive
choices. That division is the best-supported account of how this article was
created.

## Completeness limits

- The capture contains all article versions reachable through the local Git
  object's `--all --follow` lineage at collection time. It cannot contain an
  uncommitted version that neither an agent file-history store nor a session
  retained.
- Three matching Claude file-history snapshots were found. Git provides far
  broader version coverage; file-history is included only as independent
  corroboration.
- The two review sweeps are the persisted Commonplace-store reviews for exact
  historical paths. The final slug has no additional persisted catalog sweep
  in the store at collection time; its ancestor path has the relevant sweep
  and full-pass packet.
- Session selection is broad and 33 captured session files contain 62
  credential-shaped redactions. The session index preserves original hashes;
  no claim in this report depends on the redacted strings.
- Seven Claude server-side session URLs occur in commits. One or more may lack
  a direct local file containing the public URL. The commit, patch, and local
  article/session evidence remain, but the bundle does not claim a complete
  server-side export.
- GitHub metadata and comments are captured only for pull-request numbers
  visible in lineage commit subjects. The local Git commits and patches remain
  the exact content record; [`github/`](./github/) should not be described as a
  complete GitHub archive.
