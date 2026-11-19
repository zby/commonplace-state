---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/fernando-borretti-human-bottlenecks.md"
source_has_frontmatter: true
date: "2026-06-15"
depth: standard
---

# Connection Report: Human Bottlenecks

**Source:** [Human Bottlenecks](../../../sources/fernando-borretti-human-bottlenecks.md)

Borretti's core claim: **AI's transformative value is capped by internal human bottlenecks software cannot substitute for** — executive function/neurochemistry, raw intelligence, and (most critically) foundational knowledge. "If you don't have the knowledge, you don't understand the question" — without knowledge you can't pose the question, judge the answer, or know what to ask. A secondary polemic targets the notetaking / "digital garden" crowd: AI-tool fantasies built without a serious context of use, "no output, no deliverables — the deliverable is a screenshot of your Obsidian graph."

This is an **immutable snapshot** with **no `.ingest.md` companion**, so it has no authored outbound surface. Per [`kb/sources/COLLECTION.md`](../../../../sources/COLLECTION.md), the active signal for a snapshot is **reverse-edge**: which library notes should add `evidence`/`derived-from` links pointing at this source. Those are the primary deliverable below. A sibling snapshot by the same author ([Human Routers of Machine Words](../../../sources/borretti-human-routers-of-machine-words.md)) was connected on 2026-06-14 under the same posture.

## Discovery Trace

**Topic indexes:**
- `kb/notes/tags-README.md` (via README listing) — routed toward `llm-interpretation-errors` (the augmentation/automation cluster) and `distillation` for the "serious context of use" angle.
- `kb/notes/distillation-README.md` (`complete: true`) — links every distillation note, so the by-tag rg for `distillation` was **skipped**. Flagged `definitions/distillation` (use-shaped artifact requires a real downstream consumer) as the home for the digital-garden polemic.
- `kb/notes/foundations-README.md` — surfaced via the knowledge-as-prerequisite search; pointed at `human-llm-differences-are-load-bearing-...`.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md'` (implicit via README + targeted reads) — strongest description matches: `the-augmentation-automation-boundary-is-discrimination-not-accuracy` ("the human IS the oracle"), `soft-bound-traditions-...` (Zettelkasten/PKM tradition row), `a-functioning-kb-needs-a-workshop-layer-...` (consumed-value / deliverable framing).

**Body search:**
- `rg -i "you don't understand the question|binding constraint|knowledge.*(constraint|prerequisite|bottleneck)|judge.*answer|know what to ask|understand the question" kb/notes/ kb/reference/` — top hits: `the-augmentation-automation-boundary-...`, `human-llm-differences-...`, `elicitation-requires-maintained-question-generation-systems`, `designing-agent-memory-systems`. The "knowledge is the prerequisite for judging/asking" claim is **not held as a standalone note** — see Synthesis Opportunities.
- `rg -i "digital garden|obsidian|zettelkasten|pkm|deliverable|no output" kb/notes/ kb/reference/` — `soft-bound-traditions-...` (Zettelkasten row), `short-composable-notes-...` (Luhmann ancestry), `title-as-claim-...`, `traversal-improvements-should-be-deferred-...`. None polemicize about missing deliverables; the KB treats these traditions as design sources, not as a failure pattern.
- `rg -i "serious context|genuine (need|use)|intrinsic motivation|use.shaped|consumer" kb/notes/distillation-README.md kb/notes/definitions/distillation.md` — `definitions/distillation` repeatedly insists the artifact is shaped "for a particular downstream consumer." This is the precise home for Borretti's "serious context of use" requirement.
- `rg -rln -i "borretti|human bottleneck|obsidian graph|executive function" kb/` — no existing library artifact cites this source.

**Link following:**
- From `the-augmentation-automation-boundary-...` → `the-boundary-of-automation-is-the-boundary-of-verification` (synthesis hub) → `oracle-strength-spectrum`. The verification synthesis is about oracle *construction cost*; Borretti's knowledge bottleneck is a distinct claim about the *human oracle's competence floor* — adjacent, not identical (kept the discrimination note as the precise anchor, routed the synthesis note to Rejected).
- From `definitions/distillation` → `distillation-README` confirmed the use-shaped-for-a-consumer framing is the existing treatment of Borretti's "no serious context of use."

## Connections Found

None. The source is an immutable snapshot with no `.ingest.md` companion, so there is no authored outbound surface to recommend edits to. If an ingest report is later created (`cp-skill-ingest kb/sources/fernando-borretti-human-bottlenecks.md`), the Reverse-edge Candidates below become its outbound `evidence` citations.

## Bidirectional Candidates

None. (No outbound edges from the snapshot; bidirectional pairs do not apply.)

## Reverse-edge Candidates

These library notes could author an `evidence` link **to** this snapshot under `kb/notes/COLLECTION.md` rules. Each passes the articulation test.

- [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) → source — **evidence**: the note's terminal case is "only self-assessment available, low discrimination → augmentation is the ceiling; **the human IS the oracle**." Borretti supplies the human-side floor that note leaves implicit: the human-as-oracle is itself bottlenecked by foundational knowledge — "if you don't have the knowledge, you don't understand the question." This is real-world corroboration that the human oracle is not free or unbounded. Strongest match. (Note is `status: seedling`; `evidence` is additive, not load-bearing.)
- [definitions/distillation](../../../notes/definitions/distillation.md) → source — **evidence**: distillation is defined as reshaping material "for a particular downstream consumer" — the artifact only has value when a real consumer needs it. Borretti's "serious context of use" critique (flashcard/tutor/digital-garden fantasies built with no genuine need, "no output, no deliverables") is the field-evidence inverse: distillation aimed at a non-existent consumer produces screenshot-of-the-graph theater. Useful as a humanities-side illustration that the consumer must be real. (Consider whether a definition note wants a polemic as `evidence`; if not, route via the synthesis note below.)
- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → source — **evidence**: the note argues the human reader "can fill gaps from background knowledge." Borretti hardens this into a constraint — when the human *lacks* that background knowledge, they cannot judge the LLM's output at all, so the dual-audience design assumption (the human supplies discrimination) silently fails. (Seedling; additive.)

## Off-authorisation Candidates

None. `evidence` covers the useful reverse edges; no candidate needed a label outside the authorised set.

## Raw Text Candidates

None. (No outbound prospecting into raw text files from a snapshot.)

## Rejected Candidates

- [the-boundary-of-automation-is-the-boundary-of-verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — adjacent synthesis, but its claim is that *verification cost* (oracle construction) bounds automation. Borretti's claim is about the *human's knowledge competence* as a bottleneck on AI value — a different axis (the quality of the human oracle, not the cost of building one). Linking would blur two distinct claims; the augmentation/automation note above is the precise attachment point.
- [soft-bound-traditions-as-sources-for-context-engineering-strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — contains a Zettelkasten/PKM row, so it keyword-matches Borretti's digital-garden target. But the note treats those traditions as *productive design sources*; Borretti dismisses the hobbyist *practice* of those traditions. The overlap is the tradition name, not a load-bearing claim — a link would mislead.
- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — its "value is consumed, not accumulated" framing rhymes with Borretti's "no deliverables" jab, but the note is about KB workshop/library lifecycle, not about whether a knowledge practice has any external output. Too loose to help traversal.
- [elicitation-requires-maintained-question-generation-systems](../../../../notes/elicitation-requires-maintained-question-generation-systems.md) — reachable from the "know what to ask" query, but the note is about review-architecture question generation, not about a human's knowledge floor limiting what they can ask an AI. Coincidental phrase match.
- [oracle-strength-spectrum](../../../../notes/oracle-strength-spectrum.md) — one hop from the discrimination note; the discrimination note is the correct, more specific attachment point for the human-oracle-floor reading. Linking the spectrum directly adds nothing the discrimination edge doesn't already carry.

## Index Membership

- A future `.ingest.md` for this source would itself be the index entry; the snapshot does not belong in a notes index. No curated index addition recommended for the snapshot.

## Synthesis Opportunities

The source asserts a claim the KB does not yet hold as a note: **AI augmentation has a competence floor on the human side — without foundational knowledge the human cannot pose the question, judge the answer, or know what to ask, so AI cannot lift a user past their own knowledge bottleneck.** This sits at the intersection of `the-augmentation-automation-boundary-...` (the human as oracle), `human-llm-differences-...` (humans fill gaps from background knowledge), and `definitions/distillation` (a use-shaped artifact needs a real, competent consumer). If promoted, it would be the note that earns Borretti as `derived-from`/`evidence` and give the three reverse-edge candidates above a single shared anchor rather than three parallel `evidence` links. Note the companion connect report for [Human Routers of Machine Words](./borretti-human-routers-of-machine-words.connect.md) flagged a *different* Borretti synthesis (writing-is-thinking); both authors' snapshots are accreting toward a "where the human stays load-bearing in an AI loop" cluster. Do not create the note during connect.

## Maintenance Observations

- No `.ingest.md` companion exists for this snapshot, so its claims have no authored landing surface in the KB. If these reverse edges are wanted, the cheapest path is `cp-skill-ingest kb/sources/fernando-borretti-human-bottlenecks.md`, which would produce the ingest report carrying the `evidence` citations as outbound links (the inverse of the reverse edges above).
- Two Borretti snapshots (`human-bottlenecks`, `human-routers-of-machine-words`) now sit in `kb/sources/` with overlapping "human-in-the-AI-loop" arguments and no ingest companions. A later triage step may want to ingest both together and decide whether they share one synthesis note or two.

## Flags

- **No outbound deliverable**: immutable snapshot, no authored companion. The real product of this run is the Reverse-edge Candidates and the Synthesis Opportunity.
