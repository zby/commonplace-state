---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/dulleck-kerschbamer-doctors-mechanics-computer-specialists.md"
source_has_frontmatter: true
date: "2026-07-06"
depth: standard
---

# Connection Report: On Doctors, Mechanics and Computer Specialists — Where are the Problems with Credence Goods?

**Source:** [Dulleck & Kerschbamer — credence goods snapshot](../../../sources/dulleck-kerschbamer-doctors-mechanics-computer-specialists.md)

The source is an immutable `snapshot` (economics working paper). Per `kb/sources/COLLECTION.md`, a snapshot never authors outbound links; its authoring signal is **reverse-edge** — which library notes should add `evidence`/`derived-from` links pointing at it — plus, if an `.ingest.md` is created, that companion carries the mirror outbound edge. No `.ingest.md` exists yet.

The paper's load-bearing structure: with credence goods a consumer cannot verify the quality he received. The authors show that market institutions solve expert fraud **at zero cost** iff (i) large economies of scope, (ii) either **verifiability** of the treatment or a **liability** rule holds, and (iii) homogeneous consumers; relaxing any one condition reproduces essentially every known inefficiency result (overcharging, over/undertreatment, duplicated diagnosis, market breakdown). Verifiability-or-liability is the pivot: without either (a pure credence good) the market breaks down entirely (a hidden-action Akerlof lemons case). This is a canonical microeconomic formalization of the exact variable the KB treats as structural: *whether the consumer of an output can verify its quality.*

## Discovery Trace

**Description listing scan:**
- `rg -l -i 'verifi|credence|information asymmetr|review method|representational form|trust' kb/notes/ kb/reference/` — surfaced the verification/oracle cluster (`the-boundary-of-automation-is-the-boundary-of-verification.md`, `oracle-strength-spectrum.md`, `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`, `document-types-should-be-verifiable.md`, `definitions/representational-form.md`) plus trust notes (`agent-memory-needs-discoverable-composable-trusted-knowledge-under.md`, `charting-the-knowledge-access-problem-beyond-rag.md`).

**Topic indexes:**
- `kb/notes/llm-interpretation-errors-README.md` — the tag-README for the verification cluster. Its editorial groupings confirm `the-boundary-of-automation-is-the-boundary-of-verification.md` is the synthesis landing point for "verification cost as the structural determinant" (oracle theory + labor economics + capability predictions).
- `kb/notes/tags-README.md` families listed (evaluation, failure-modes, foundations) — no economics/asymmetric-information tag exists.

**Body search:**
- `rg -i 'information asymmetr|cannot verify|unverifiab|credence|trusted cache|verify quality'` over notes/reference/agent-memory/agentic-systems — no note uses "credence goods"; the closest framings are `the-boundary-of-automation-is-the-boundary-of-verification.md` ("research taste resists automation because problem selection has no ground truth"; "hard oracles") and `document-types-should-be-verifiable.md` ("the type is only useful if the processor can trust it, and trust requires the ability to check").
- `rg -i 'reputation|keep.*honest|incentive to|moral hazard|adverse selection|lemons'` over notes — **no** note references Akerlof, lemons, moral hazard, or adverse selection. The KB has no asymmetric-information economics coverage, so the paper is a net-new evidence domain rather than a duplicate.

**Link following:**
- From `the-boundary-of-automation-is-the-boundary-of-verification.md` one hop: `oracle-strength-spectrum.md`, `the-augmentation-automation-boundary-is-discrimination-not-accuracy.md`, `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`, `spec-mining-as-codification.md`. The synthesis note already reaches into labor economics (Tam et al.) and cites its "evidence" edges to external X/arXiv sources — the exact slot the credence-goods paper fits.

## Connections Found

The source is an immutable snapshot, so it authors nothing itself. If an `.ingest.md` companion is created, its single strongest outbound edge would be:

- [the-boundary-of-automation-is-the-boundary-of-verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **evidence**: an ingest report would cite this note as where the paper lands — the paper is a formal-economics demonstration that verifiability (or liability) is the structural determinant of whether a fraud-prone market reaches the efficient outcome. Mirror of the reverse edge below.

## Bidirectional Candidates

None. (Snapshots carry no authored surface, so there is no source-side return link to add; the useful direction is entirely inbound — see Reverse-edge Candidates.)

## Reverse-edge Candidates

- [the-boundary-of-automation-is-the-boundary-of-verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source — **evidence** (authored from the note under `kb/notes/` rules): the note argues verification cost is the *primary structural determinant of automation*, converging three domains (oracle theory, labor economics, capability predictions). Dulleck & Kerschbamer add a fourth, independent domain — mechanism-design microeconomics — reaching the same structural claim: when quality is verifiable (or liability substitutes for it) institutions eliminate fraud at zero cost, and when it is not the market breaks down. This is the note's central variable proved from a different tradition, which also *partially answers the note's own caveat* that its three sources share a "rationalist, verification-oriented worldview" (game-theoretic economics is a genuinely separate lineage). `status: current`, so the load-bearing `evidence` label is safe to flag.

## Off-authorisation Candidates

None. `evidence` (and, for a future ingest, `evidence`) covers the one strong candidate; no candidate passed the articulation test while lacking an authorised label.

## Raw Text Candidates

None. (Source has frontmatter and is a typed snapshot.)

## Rejected Candidates

- [document-types-should-be-verifiable](../../../../notes/document-types-should-be-verifiable.md) — thematically adjacent ("trust requires the ability to check") but the paper does not *corroborate* the claim that document types should assert checkable structural properties; the overlap is a shared intuition about verifiability, not evidence. An `evidence` edge here would be a keyword/theme match, not an articulable support relation.
- [oracle-strength-spectrum](../../../../notes/oracle-strength-spectrum.md) / [the-augmentation-automation-boundary-is-discrimination-not-accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) / [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — the paper is compatible with the whole oracle cluster, but linking it into every cluster member would be over-linking. The synthesis note (`the-boundary-of-automation...`) is the correct single landing point; it is where the "verification is the structural determinant" claim is made in general terms and where external evidence is already gathered.
- [agent-memory-needs-discoverable-composable-trusted-knowledge-under](../../../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) / [charting-the-knowledge-access-problem-beyond-rag](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — both make "trust" a required property of remembered knowledge, which rhymes with credence goods (consumer must trust an unverifiable seller). But the paper is about *market institutions* keeping sellers honest, not about a consumer-agent's trust criterion; the connection is an analogy, not evidence for these specific claims.

## Index Membership

None applicable. The paper is a captured source, not a note; it does not belong in a curated notes index. If a `compares-with` corpus of asymmetric-information sources ever existed it would join there, but no such index or sibling source exists.

## Synthesis Opportunities

A genuine higher-order claim is implied but **not yet captured** anywhere in the KB: *agent-produced knowledge artifacts are credence-good-like — a downstream agent/user cannot verify the quality of the knowledge it received, only detect gross undertreatment.* Under that lens, the KB's own machinery maps onto the paper's three efficiency conditions:
- **Verifiability** ≈ `representational-form.md`'s review-by-form ("test symbolic artifacts") and `document-types-should-be-verifiable.md`'s checkable types;
- **Liability** ≈ the review-gate system (`README-REVIEW-SYSTEM.md`) and marks that are "enforced-or-omitted" (a validated cache that punishes a false claim);
- and the paper's "no-verifiability-no-liability → market breakdown" ≈ the note that `automating-kb-learning` stalls precisely where no oracle exists.

This would be a note in `kb/notes/`, not a connect deliverable. Flag only — connect does not create it, and it should clear the "does it change how someone builds a KB?" quality bar before authoring (the economics is out-of-scope on its own; it earns a note only as a lens on KB verification design).

## Maintenance Observations

- **Collection coverage gap (durable):** the KB has no coverage of asymmetric-information / mechanism-design economics (Akerlof lemons, moral hazard, adverse selection) despite `the-boundary-of-automation-is-the-boundary-of-verification.md` already leaning on labor-economics evidence. This snapshot is the first such source; a future maintainer may want it findable as the economics anchor for the verification-boundary argument.
- The snapshot's capture note (lines 16) flags that this is the open-access 2001 working-paper version, not the 2006 JEL published version — worth remembering if a note later cites it as evidence and needs the canonical citation.

## Flags

- **Single strong candidate.** Not a split candidate: the paper makes one load-bearing structural assertion (verifiability/liability as the pivot for efficient outcomes) and lands cleanly on one synthesis note. No five-notes-across-three-areas fan-out.
- **Scope tension (unresolved, not blocking):** credence-goods economics is out-of-scope for this KB *on its own terms*; it is in-scope only as evidence for a KB-methodology claim about verification. The `evidence` reverse-edge into `the-boundary-of-automation...` is the one place that tension resolves in favor of keeping the source. Everything else is rejected precisely because the economics-KB bridge would be analogy rather than support.
