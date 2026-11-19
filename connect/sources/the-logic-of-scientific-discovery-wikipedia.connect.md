---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/the-logic-of-scientific-discovery-wikipedia.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: The Logic of Scientific Discovery (Wikipedia)

**Source:** [The Logic of Scientific Discovery (Wikipedia)](../../../../sources/.snapshots/the-logic-of-scientific-discovery-wikipedia.md)

The source is an immutable snapshot, so it authors no links. Every "Connections Found" item is a candidate for the matching tracked ingest, `kb/sources/the-logic-of-scientific-discovery-wikipedia.ingest.md`, which did not exist when this report was written. No `.ingest.md` exists yet for this snapshot.

**What the source carries:** it is a short tertiary summary. It has two substantive claims, both quoted verbatim from Popper. (1) The verification/falsification asymmetry: universal statements "are never derivable from singular statements, but can be contradicted by singular statements" (LSD p. 19). (2) The reproducible-effect condition on refutation: "a few stray basic statements contradicting a theory will hardly induce us to reject it as falsified. We shall take it as falsified only if we discover a reproducible effect which refutes the theory" (LSD p. 66). The rest is reception: Kuhn, Harré, Jung, Ricœur, Gay, Magee on logical positivism, Sokal/Bricmont, and Taleb on confirmation bias. The article does **not** cover the book's chapters on levels of universality and precision, degrees of corroboration, or probability.

## Discovery Trace

**Authorisation read:** `kb/sources/COLLECTION.md` → Outbound links. Snapshots never author links. Ingest labels are: `derived-from` (external), `is-evidence-for` (notes, agent-memory-systems), `abstracted-from` (notes), `rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), and `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external). Linking into `kb/work/` or `kb/instructions/` is excluded. Destinations prospected: notes, sources, reference, agent-memory-systems, agentic-systems, and tags (tags is named in the scan list, but no label authorises it).

**External:** the only already-known external target is the source URL itself (`https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery`). `derived-from` fits the ingest's relation to that URL. External prospecting beyond this URL was skipped per skill rules.

**Curated heads:**
- The snapshot carries no `tags:`, so no tag head was matched by tag. I read `kb/tags/discovery-README.md` (`complete: true`) and found nothing about falsifiability or refutation conditions. `rg -n -i "popper|falsif" kb/tags/*.md` found only [foundations-README](../../../../tags/foundations-README.md), which links mechanistic-constraints, and [kb-maintenance-README](../../../../tags/kb-maintenance-README.md), which links title-as-claim-exposes-commitments. Both notes are evaluated below.

**Description / file listings:**
- `rg -il "popper" kb/notes kb/tags kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md' | xargs -r rg -N --no-heading -m1 '^description:'` gave 24 hits. Flagged: claim-modality, generality-bought, domain-pricing, tentative-theory, theory-builder, mechanistic-constraints, title-as-claim-exposes-commitments, theory-building-has-distinct-precedents, narrowing-bought, first-principles-reasoning.
- `rg -N --no-heading -m1 '^description:'` over the Popper and falsification source ingests: popper-conjectures-and-refutations, popper-a-realist-view-1966, popper-epistemology-without-a-knowing-subject-1968, automated-hypothesis-validation-sequential-falsifications, falsifybench (x2), scaffold-not-vocabulary, think-before-you-act, sound-agentic-science, optimal-choice-of-hypothesis.

**Body search (actual queries):**
- `rg -il "falsifiab|falsif" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources` gave about 95 files. Most are passing uses of "falsify" in sources.
- `rg -l "Logic of Scientific Discovery|Logik der Forschung" kb` gave one hit: [generality-bought](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md), which cites the book in prose with no ingest link.
- `rg -n "asymmetr" kb/notes`: the hits are about error-correction and lineage asymmetries. None concerns the verification/falsification asymmetry. Rejected as keyword-only matches.
- `rg -il "demarcation"` gave 0 hits KB-wide. `rg -il "Kuhn"` gave 0. `rg -il "verificationis|logical positivis|verification principle"` gave 1 source (scaffold-not-vocabulary, a passing mention).
- `rg -il "confirmation bias"` gave [reasoning-production-is-not-reasoning-evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md), falsifybench, popper-conjectures-and-refutations, and two others. The Taleb reception sentence is too thin to carry a link.
- `rg -il "reproducib|replicat"` returned no notes. The hits are sources and reviews about experiment reproduction, which is a different sense.
- `rg -n -i "one genuine instance|single (counter)?example|one counterexample|single instance|single episode|one episode|one observation|single observation|anecdot|stray" kb/notes` found [claim-modality](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) line 10 ("modus tollens on one genuine instance") and `kb/notes/COLLECTION.md` line 63 ("one genuine counterexample refutes"). These are the main landing points.
- `rg -n -i "asymmetr|demarcat|falsifiab|reproduc|verif"` over the four closest source ingests: popper-conjectures-and-refutations names falsifiability as a topic, and the POPPER ingest discusses statistical falsification tests.
- `rg -n -i "test|accept" kb/notes/definitions/discovery-lifecycle.md` found line 35 ("Later counterevidence against an integrated claim opens a new instance at observation / anomaly").

**Link following:**
- claim-modality → notes COLLECTION modality paragraph, domain-pricing, and title-as-claim-exposes-commitments. The universal mode's refuter is stated as "one genuine instance" and the word "genuine" is never defined. The source's p. 66 quote says what Popper takes a genuine refuting instance to be.
- tentative-theory → popper-1966 and popper-conjectures-and-refutations ingests. This definition is already grounded in primary Popper texts.
- mechanistic-constraints → falsifier blocks. The asymmetry is the background rationale, but the note does not rely on the book.

## Connections Found

All candidates are for the future `the-logic-of-scientific-discovery-wikipedia.ingest.md`.

- [claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) -- **is-evidence-for**: the note says a universal claim is refuted "deductively — modus tollens on one genuine instance." The source bears on this at both ends. The p. 19 asymmetry quote supports the deductive form: a singular statement can contradict a universal statement, while no set of singular statements can derive it. The p. 66 quote qualifies "genuine": Popper does not accept stray contradicting basic statements as falsification and requires a reproducible refuting effect. A reader of the ingest learns that the KB's universal-mode refuter has a Popperian gloss the note leaves unstated.
- [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) -- **is-evidence-for**: the definition sends later counterevidence against an integrated claim to "a new instance at observation / anomaly," not to immediate rejection. Popper's p. 66 condition supports that routing: a single contradicting report is an anomaly to investigate until it is shown to be a reproducible effect. The evidence is moderate, because the lifecycle cites Peirce rather than Popper.
- [Popper, Conjectures and Refutations](../../../../sources/popper-conjectures-and-refutations.ingest.md) -- **compares-with**: shared axis: *where the falsifiability and demarcation account is stated, and at what fidelity*. C&R is a retained primary source for Popper's account (its ingest names falsifiability). This article is a tertiary summary with two verbatim LSD quotes and a reception survey. Anyone grounding a falsifiability claim should prefer the primary source. The comparison shows the Wikipedia ingest carries only the two quotes and the reception facts.
- [POPPER: automated hypothesis validation with sequential falsifications](../../../../sources/automated-hypothesis-validation-sequential-falsifications.ingest.md) -- **compares-with**: shared axis: *what counts as a refutation*. The POPPER system turns falsification into sequential statistical tests with error control. Popper's p. 66 condition makes refutation depend on a reproducible effect, not on single contradicting observations. Comparing the two shows how the tool turns that methodological decision into procedure. This is a real contrast, but it is secondary to the claim-modality link.
- External `https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery` -- **derived-from**: the ingest analysis is worked out from this article, which is already in hand as the snapshot's `source`.

## Bidirectional Candidates

None. The ingest→source compares-with edges are symmetric in intent. The return direction from popper-conjectures-and-refutations is not useful, because C&R is the stronger source.

## Reverse-edge Candidates

- [claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) → future ingest -- **evidenced-by** (notes COLLECTION label, notes→sources): this is the strongest inbound edge. The note already grounds its statistical mode in Popper, but its universal mode's "genuine instance" has no source. A link carrying the retained p. 66 quote would qualify "genuine" as "reproducible refuting effect." Add it via `cp-skill-ground` (`Target: claim-modality…; Claim needed: Popper counts a universal claim falsified only by a reproducible refuting effect, not by stray basic statements`). Grounding the quote from the primary LSD text would be better if it is ever snapshotted.
- [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) → future ingest -- **evidenced-by**: this is optional. It would support routing counterevidence to observation/anomaly rather than to rejection. It is weaker because the definition's lineage is Peircean.

## Off-authorisation Candidates

- [tags/foundations-README](../../../../tags/foundations-README.md) -- `kb/tags/` is in the sources scan list, but no label in the sources table authorises tags as a destination. A tag head would not link a tertiary Wikipedia ingest anyway. Recommendation: reject as off-scope. The only possible use would be a tag on the ingest itself, and the other Popper ingests carry no tags.

## Raw Text Candidates

None

## Rejected Candidates

- [generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- this is the only note that cites *Logic of Scientific Discovery* by name ("on levels of universality and precision"). The Wikipedia article says nothing about universality or precision, so an ingest link would not support the cited content. The note needs the book itself (see Flags).
- [tentative theory](../../../../notes/definitions/tentative-theory.md) -- the asymmetry ("no number of experiments can ever prove a theory") is the logical reason tentativeness lasts. The definition is already grounded in primary Popper texts (1966, C&R), so a tertiary summary adds nothing.
- [domain pricing routes an exception to idealization assessment](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- it shares the idea that "not every exception refutes." Its scope is ideal-type claims under Lakatos, while the p. 66 condition concerns universal claims. The overlap is thematic only.
- [mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) and [title as claim exposes commitments enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) -- both depend on falsifiability as a general framing, but neither makes a claim the article's quotes would support or qualify. Linking them would add only a topic association.
- [theory-building has distinct precedents](../../../../notes/theory-building-has-distinct-precedents.md) -- its Popper section uses the P1→TT→EE→P2 schema from the 1966 and 1968 sources. The article does not cover that schema.
- [reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- this matched only on "confirmation bias." The source's Taleb sentence is a reception note, not an argument.
- FALSIFYBENCH ingests, sound-agentic-science, and scaffold-not-vocabulary -- all apply falsification to LLM behaviour or reporting. None raises the reproducibility condition or the asymmetry sharply enough to meet the compares-with standard. The POPPER ingest was kept instead.
- `asymmetr` hits in notes (scheduler-LLM separation, lineage queries, and others) -- these are other asymmetries, so they are keyword-only matches.

## Index Membership

- [kb/sources/README.md](../../../../sources/README.md) -- the future ingest would belong wherever the Popper primary sources are listed, marked as a tertiary summary.

## Synthesis Opportunities

None at this depth. There is one possible thread. Popper's reproducible-effect condition, the notes-collection rule that "one genuine counterexample refutes," and the discovery lifecycle's anomaly routing may together imply that a universal claim's refuter is a reproducible effect, not a single report. That would be a clarification inside claim-modality, not a new note (see Flags).

## Maintenance Observations

- `kb/notes/COLLECTION.md` line 63 and claim-modality line 10 both say one "genuine" counterexample refutes a universal claim, and neither defines "genuine." Popper's own condition is a reproducible refuting effect, which is stricter than a single observation. This affects how review passes treat a single reported counterexample. The gap is worth a deliberate decision, whether or not this ingest is written.
- [generality-bought](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) cites *Logic of Scientific Discovery* (levels of universality and precision) in prose with no tracked ingest. It is the only KB citation of the book. This Wikipedia snapshot cannot discharge that citation. Snapshotting the primary text would.

## Flags

- **Low source value.** The article is a thin tertiary summary. Its durable content is the two verbatim Popper quotes (pp. 19, 66). An ingest should keep only those and say that the reception section is secondary opinion. A primary LSD capture would replace this ingest as the grounding target for both quotes and would also serve generality-bought.
- **Tension:** the KB's universal-mode rule ("one genuine counterexample refutes") vs Popper's "only if we discover a reproducible effect." These may be compatible if "genuine" means "reproducible." The report does not resolve this.
- Not a split candidate.
