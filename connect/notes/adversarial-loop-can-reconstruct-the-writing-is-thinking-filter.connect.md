---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md"
source_has_frontmatter: true
date: "2026-06-16"
depth: standard
---

# Connection Report: An adversarial human-agent loop can reconstruct the writing-is-thinking filter

**Source:** [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md)

## Discovery Trace

**Source state:** Note already authors three footer edges — `grounds` to the relaxation note, and two `derived-from` edges to the Borretti sources. The note's argument runs: writing-is-thinking filter is a property of the loop not the pen; the loop reconstructs the stall only if (a) the human stays the judge and (b) the loop stays adversarial; architecture (workshop layer, report-only critique, review gates, human accept) forces the condition; competence floor from Borretti's second essay conceded.

**Topic indexes:**
- Read `kb/notes/tags-README.md` (hub) and `kb/notes/foundations-README.md`. Source carries `tags: [foundations]`. The foundations-README is a `tag-readme` but does **not** declare `complete: true`, so a by-tag rg was still run.
- By-tag scan `rg -l '^tags:.*\bfoundations\b' kb/notes/ | xargs rg '^description:'` — 14 notes. Flagged from foundations: the relaxation note (already linked), `charting-the-knowledge-access-problem-beyond-rag` (curation/access framing — too broad, rejected), nothing else with a load-bearing tie to the loop/judge argument.

**Body search:**
- `rg -lni 'human.{0,4}judge|review gate|adversarial|rubber.?stamp|human.in.the.loop' kb/notes/` — surfaced `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`, `semantic-review-catches-content-errors-that-structural-validation`, `synthesis-is-not-error-correction`, `an-accepted-edit-verifies-the-change-not-the-rule`, `verifiability-gradient`, `llm-generation-confidence-tracks-typicality-not-soundness`.
- `rg -lni 'report-only|critique pass|human accept' kb/notes/ kb/instructions/` — surfaced `an-accepted-edit-verifies-the-change-not-the-rule`, `kb/instructions/composition-friction-gate.md`, `kb/instructions/critique-note.md`, `text-testing-framework`.
- `rg -ln 'workshop' kb/notes/` — surfaced `a-functioning-kb-needs-a-workshop-layer-not-just-a-library` (the note names the workshop layer directly as an architectural enabler of the condition).

**Link following:**
- From the relaxation note (already linked `grounds`): followed its open-questions edge to `error-correction-works-above-chance-oracles-with-decorrelated-checks` (labelled `enables` there). The source note's "How this could be wrong" turns on whether the adversarial pass has teeth — exactly the conditions that note supplies. Strong candidate.
- From the relaxation note: `the-boundary-of-automation-is-the-boundary-of-verification` (the prose register has no oracle; the source's loop is the proposed substitute human-as-judge oracle). Candidate.
- From `inspectable-artifact-...`: confirms the "inspectable artifact, not who reviews" framing — a `contrasts` neighbour (source insists on human-as-judge; that note argues inspectability does not require a human in the loop). Genuine neighbouring-shape distinction.

## Connections Found

- [error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **grounds**: the source's contingency claim ("the defense is contingent on the adversarial pass having teeth") is exactly the discriminative-power + decorrelation condition this note formalises (TPR > FPR, independent checks); it supplies the premise under which "the loop reconstructs the filter" can actually hold. Load-bearing label on a seedling — flagged.
- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **grounds**: prose argument has no automatic oracle, so removing the composition stall leaves nothing behind it; the source's adversarial loop is the proposed human-judge substitute for that missing oracle. Verifies the premise that the filter has to be reconstructed *somewhere*. Load-bearing on a seedling — flagged.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — **contrasts**: neighbouring-shape distinction. The source insists the filter requires a *human* who stays the judge; that note argues the constrain/relax steering "requires an inspectable artifact" and explicitly *not* a human in the loop. Following the edge gives a reader the exact boundary between "human judgment is load-bearing" (prose-discovery register) and "inspectability suffices" (codified register).
- [vibe-noting](../../../../notes/vibe-noting.md) — **contrasts**: vibe-noting names the careless failure mode (a seed rendered into an article, witness search skipped) that the source explicitly distinguishes its disciplined loop from. The pair marks the same fork — delegate judgment carelessly vs. keep the human judging — that the source's whole argument turns on.

## Bidirectional Candidates

- [error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) <-> source — return `extends` worth considering: the source is a concrete instance ("disciplined human-agent loop") of the abstract amplification conditions, useful to a reader at the oracle-theory note who wants a worked application in the prose register. Optional; author from that note's side under its own rules.

## Reverse-edge Candidates

- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) → source — **see-also / extends** (authored from that note under notes→notes rules): it argues human acceptance is a strong *instance* oracle but silent at the rule level. The source treats "a human accept as the strongest check" as load-bearing for the loop's teeth; that note qualifies *what* the accept actually verifies. A reader on either note benefits from the other. Surfaced as reverse-edge because the qualification is that note's claim to make, not the source's.
- [a functioning KB needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) → source — the source cites "a workshop layer where drafts are consumed rather than shipped" as part of the architecture that forces the adversarial condition. The workshop-layer note is the definitional home of that mechanism; an `enables`/`see-also` edge authored from it (or from the source toward it) would let a reader trace why drafts-consumed-not-shipped matters for the filter. Decide direction at authoring time.

## Off-authorisation Candidates

None. (The prescriptive surfaces below — `critique-note`, `composition-friction-gate`, `REVIEW-SYSTEM` — are the report-only/review-gate machinery the source references in prose. notes→instructions edges are authorised only as `see-also`, and the source COLLECTION.md flags that the usual direction is inverse: `instruction → note` via `rationale`. These belong as reverse edges from the instructions, not as outbound `see-also` sprays from this note. See Maintenance Observations.)

## Raw Text Candidates

None.

## Rejected Candidates

- [semantic review catches content errors that structural validation misses](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) — keyword match on "review" but operates one level down (form vs. content error taxonomy); the source's "adversarial review has teeth" claim is about oracle discriminative power, not the structural/semantic split. No concrete traversal gain.
- [synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) — about multi-agent merge-vs-vote dynamics; adjacent to "adversarial agents in the loop" only by association, not by a premise the source uses.
- [charting the knowledge access problem beyond RAG](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — co-tagged `foundations` and mentions curation across a corpus (which the source raises as the part Borretti never reaches), but it is an exploratory decomposition of the access problem, not a claim the source builds on. Topical overlap only.
- [Human Bottlenecks](../../../sources/fernando-borretti-human-bottlenecks.md) — already linked `derived-from`; no new edge.

## Index Membership

- [foundations-README](../../../../tags/foundations-README.md) — source already carries `tags: [foundations]` and appears in the by-tag listing. A future writer may add a curated one-line entry to the README's `## Notes` section (the README is not `complete`, so this is editorial, not enforced). Connect does not edit the index.

## Synthesis Opportunities

None new. The source already functions as the synthesis answering the relaxation note's open question; no higher-order claim is implied by the candidate set beyond what the source states.

## Maintenance Observations

- **Reverse-edge gap from the review/critique machinery.** The source names report-only critique, review gates, and the composition-friction gate as the architecture that forces its adversarial condition, but no instruction artifact (`kb/instructions/critique-note.md`, `kb/instructions/REVIEW-SYSTEM.md`, `kb/instructions/composition-friction-gate.md`) currently carries a `rationale` edge back to this note. Per the source COLLECTION.md, that inverse direction (instruction→note `rationale`) is the intended one. A maintenance pass on those instructions could add the rationale edges; this is the prescriptive side's call, not connect's.
- **No inbound edges yet.** `rg -l 'adversarial-loop-can-reconstruct'` across `kb/` (excluding reports) found zero referencing artifacts. The note is newly authored (commit 65bc1339) and currently a sink; the reverse-edge candidates above are the first inbound links worth authoring.
- **Composition-friction note not on disk.** Git status lists `kb/notes/current-llm-inference-removes-composition-friction-filter-signal.md` as modified and an untracked `kb/cache/friction/` dir, but neither resolves to a working-tree file under that name. If a composition-friction *note* is intended (the source's "composition-friction" wording suggests a sibling claim), it may be a strong neighbour once committed — re-run connect after it lands.

## Flags

- **Two load-bearing labels on a `seedling` source proposed against targets** (`grounds` to the oracle-conditions note and to the verification-boundary note). Both are genuinely premise-supplying, not additive, so they are surfaced as `grounds` per the type contract's flag-don't-suppress rule — a writer authoring them should confirm the premise direction holds at edit time.
- Not a split candidate: the note makes one sustained argument (the filter is the loop's, under conditions) across a single topic area; it stays whole.
