---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/argyris-organizational-learning-and-mis-1977.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Organizational Learning and Management Information Systems

**Source:** [Organizational Learning and Management Information Systems](../../../../sources/.snapshots/argyris-organizational-learning-and-mis-1977.md)

## Discovery Trace

**Source framing:**

- Read the complete 861-line snapshot, `kb/sources/COLLECTION.md`, and `kb/cache/types/connect-report.md`. Argyris defines organizational learning as identifying and correcting error; distinguishes single-loop correction within objectives and policies from double-loop questioning of those governing commitments; distinguishes espoused theories of action from the theories-in-use that actually govern behavior; and models defensive organizational feedback as primary and secondary inhibiting loops that preserve error and camouflage.
- The source also develops a distinct MIS argument: local information systems preserve process detail and tacit situational knowledge, while distant systems provide abstract, comparable, publicly checkable indicators. The resulting information gap, hierarchy, unilateral control, and defensive behavior can make apparently stronger information systems suppress the inquiry needed for double-loop learning.
- The snapshot has no `tags:` field, so no tag-driven completeness shortcut applied. After direct hits identified the topic, read [Tags](../../../../tags/README.md), [Learning theory](../../../../tags/learning-theory-README.md), [deploy-time-learning](../../../../tags/deploy-time-learning-README.md), and [Self-improving systems](../../../../tags/self-improving-systems-README.md) as curated neighborhood heads.
- The snapshot is immutable. No matching `kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md` existed during discovery, so every outbound candidate below is for that future ingest; no durable artifact should link to or be authored into `.snapshots/`.

**Curated heads and complete listings:**

- Read the five authorised destination heads: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over every authorised local destination. Counts were notes 366, reference 151, agent-memory-systems 173, agentic-systems 12, and sources 311. The title pass surfaced the theory-mediated learning, action-model, reflective revision, organizational-learning, cybernetic adaptation, and theory-taxonomy neighborhoods evaluated below.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorised local destination. Counts were notes 363, reference 150, agent-memory-systems 171, agentic-systems 10, and sources 311. No candidate was accepted from title or description overlap alone.

**Notes body search:**

- `rg -n -i 'single[- ]loop|double[- ]loop|theor(y|ies)[- ]in[- ]use|theor(y|ies) of action|governing (variables|values)|organizational learning|defensive routine|self-sealing' kb/notes --glob '*.md'` — found the two existing Argyris uses. Kept `Learning is not only about generality` because it currently states the single-/double-loop distinction through a secondary web source, and kept `Soft-bound traditions` because it explicitly classifies organizational learning as an aspirational transfer source.
- `rg -n -i 'error (detection|correction)|detect(ion)? and correct(ion)? of error|action model|theory-mediated|model-mediated|selective revision|governing machinery|reflective.*lesson' kb/notes --glob '*.md'` — kept the action-model note because espoused theory versus theory-in-use is a direct historical version of its operativity condition; kept the theory-mediated and reflective-revision notes because Argyris supplies a close predecessor while also exposing their stricter addressability and computational-reflection requirements.
- Read in full `Learning is not only about generality`, `An action model matters only through its consumption path`, `Theory-mediated learning may improve sample efficiency under structured shifts`, `Theory-mediated self-improvement needs both interpretation and retention from one substrate`, `Reflection makes retained lessons second-order`, `Selective revision needs a faithful rationale`, and `Soft-bound traditions as sources for context engineering strategies`.
- Evaluated `Continual learning requires governing behaviour-changing writes`, `The readable-artifact loop is the tractable unit for continual learning`, `Error correction works with above-chance oracles and decorrelated checks`, and `Representational form does not determine whether a theory is a prototype`; rejected them where the shared words named different mechanisms or a closer note already carried the useful relation.

**Sources body search:**

- `rg -n -i 'Argyris|double[- ]loop|single[- ]loop|espoused theor|theor(y|ies)[- ]in[- ]use|organizational learning' kb/sources --glob '*.md'` — found no existing Argyris ingest. It surfaced only incidental uses of “theory-in-use” in the Gregor design-theory ingests; the mature 2006 Gregor source was kept because the same vocabulary names a sharply different relation to action.
- `rg -n -i 'theory-mediated|model-mediated|action model|governing machinery|governing assumptions|governing values' kb/sources --glob '*.md'` — surfaced the newly ingested Craik, Popper, and Pearl sources plus the current theory-mediated cluster. Read all three ingests and kept them as complementary components rather than treating any one as a synonym for Argyris.
- `rg -n -i 'error correction|detect(ion)? and correct(ion)? of error|self-sealing|feedback loop' kb/sources --glob '*.md'` — surfaced Ashby's ultrastability and the PDSA history. Read both. Kept Ashby because its “two feedback loops” are an especially important near-name/non-equivalence; rejected PDSA as a redundant learning-cycle comparator after Popper and Ashby supplied cleaner axes.
- Read the complete 2006 and 2002 Gregor ingests. Kept the mature 2006 account and rejected the 2002 precursor to avoid duplicating one taxonomy lineage.

**Reference, agent-memory, and agentic-system search:**

- Ran `rg -n -i 'single[- ]loop|double[- ]loop|theor(y|ies)[- ]in[- ]use|theor(y|ies) of action|governing (variables|values)|organizational learning|defensive routine|self-sealing|error detection and correction'` separately over `kb/reference`, `kb/agent-memory-systems`, and `kb/agentic-systems`; there were no hits.
- The complete title and description scans surfaced broad Commonplace self-improvement documentation, trace-learning systems, and reflective harnesses. None passed the articulation test. The source analyzes organizational theories of action and defensive learning systems; it does not describe the shipped Commonplace system, implement an agent-memory system, or provide code-grounded evidence about a whole agentic harness. The theoretical notes supply the useful bridge without forcing a sparse `see-also` or broad system comparison.

**Link following:**

- Followed the existing Argyris mentions from `Learning is not only about generality` and `Soft-bound traditions` into deploy-time learning, theory-mediated learning, and the self-improving-systems head. This separated the primary-source grounding need from the later computational transfer claims.
- Followed the theory-mediated learning neighborhood into the action-model, reflective second-order revision, theory-mediated self-improvement, and selective-rationale notes. The traversal exposed two independent faithfulness questions: whether a stated theory actually mediates action, and whether the recorded rationale identifies the basis that selective revision must change.
- Followed the source neighborhood through the Craik, Popper, Pearl, Ashby, and Gregor ingests. Craik supplies model-mediated action without learning; Popper supplies criticism of world-directed theories; Pearl supplies formal intervention semantics under a fixed causal model; Ashby supplies direct viability-driven parameter change; Gregor classifies communicable prescriptive theory. Argyris uniquely foregrounds the action-governing theory, the espoused/in-use gap, and organizational barriers to revising governing commitments.

**External destination:**

- The original external source is already identified in the snapshot frontmatter. External is not a prospecting surface, so no open-web search was performed and no additional external candidate was evaluated.

## Connections Found

The following are recommendations for the future matching ingest's authored surface, not edits to the immutable snapshot.

- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) — **is-evidence-for**: Argyris's primary account defines organizational learning through error identification and correction, then distinguishes correction within objectives and policies from questioning those governing commitments. It can replace the note's current secondary-source support while preserving that the note's generality-axis mapping is Commonplace's interpretation.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: the espoused-theory/theory-in-use distinction is a direct precursor to the note's operativity test. A theory people report holding can remain behaviorally inert, while the often tacit theory-in-use is the program that actually selects and structures action.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) — **compares-with**: Argyris supplies an earlier architecture in which theories govern action and double-loop inquiry can revise governing values, but the theories-in-use may be tacit and inaccessible, and the paper supplies neither theory search, reach-assessment, addressable retained theories, nor sample-efficiency evidence. The comparison sharpens what the later note adds beyond any internal action-guiding representation.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — **compares-with**: Argyris places learning in a human organization acting through individual agents and allows inquiry into the organization's own governing values. That is a socio-technical predecessor to self-directed theory revision, but not a computationally causal self-representation with separately addressable retained premises and scope.
- [Reflection makes retained lessons second-order](../../../../notes/reflection-makes-retained-lessons-second-order.md) — **compares-with**: double-loop learning and second-order retention share a target—governing commitments rather than only actions—but Argyris's mechanism is organizational inquiry into frequently hidden theories-in-use, not an explicit reject, revise, or rescope operation on a retained represented commitment.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — **compares-with**: Argyris's distinction between espoused theory and theory-in-use is a historical form of the legibility/faithfulness problem. What an actor can state about its conduct may not identify the program that produced the conduct; the source does not, however, test intervention on a recorded rationale or establish the note's selective-repair mechanism.
- [Soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) — **is-evidence-for**: the paper provides primary support for the note's organizational-learning row and for treating double-loop revision as difficult under defensive feedback. It does not by itself establish the note's stronger transfer claim that agent double-loop learning requires reflection on history.
- [Ingest: A Realist View of Logic, Physics, and History](../../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) — **compares-with**: Popper's `problem → tentative theory → error elimination → successor problem` revises objective theories about the world, while Argyris revises theories that govern action and explains why organizational defenses may suppress the criticism. Together they separate the revision cycle from the special case where the theory controls the reviser's conduct.
- [Ingest: Craik, Hypothesis on the Nature of Thought](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) — **compares-with**: Craik explains how an internal model predicts consequences and participates in choosing among possible actions but leaves learning and model revision open. Argyris explains how action-guiding theories can be corrected or have their governing assumptions questioned but does not supply Craik's internal-simulation mechanism.
- [Ingest: A Probabilistic Calculus of Actions](../../../../sources/pearl-a-probabilistic-calculus-of-actions-1994.ingest.md) — **compares-with**: Pearl formalizes predictions under intervention by replacing one named causal mechanism inside a supplied model; Argyris analyzes the often tacit theories that actually govern organizational action and the feedback that can or cannot revise them. The comparison separates formal action consequence derivation from organizational theory uptake and revision.
- [Ingest: Design for a Brain (1960)](../../../../sources/ashby-design-for-a-brain-1960.ingest.md) — **compares-with**: Ashby's two feedback loops distinguish ordinary regulation from an automatic viability-triggered change to parameters. Argyris's single-/double-loop distinction instead turns on whether error correction questions governing objectives, policies, or values, through inquiry that defensive theories-in-use can suppress. The near-name should not be treated as mechanism identity.
- [Ingest: The Nature of Theory in Information Systems](../../../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md) — **compares-with**: Gregor's theory for design and action is a communicable prescriptive theory whose classification does not require actual execution. Argyris's theory-in-use is defined by what actually governs conduct and is explicitly distinguished from the communicable theory an actor espouses. The comparison prevents two information-systems uses of “theory” and “action” from collapsing into one.

## Bidirectional Candidates

- [Ingest: A Realist View of Logic, Physics, and History](../../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) ↔ the future Argyris ingest — **compares-with**: readers entering either revision tradition benefit from the world-directed/action-governing distinction and from seeing that criticism can be architecturally present yet organizationally inhibited.
- [Ingest: Craik, Hypothesis on the Nature of Thought](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) ↔ the future Argyris ingest — **compares-with**: the pair cleanly separates model-mediated selection of action from evidence-responsive revision of the model or governing action theory.
- [Ingest: Design for a Brain (1960)](../../../../sources/ashby-design-for-a-brain-1960.ingest.md) ↔ the future Argyris ingest — **compares-with**: reciprocal comparison is useful because “two feedback loops” and “double-loop learning” invite conflation despite different triggers, update targets, and selection mechanisms.
- [Ingest: The Nature of Theory in Information Systems](../../../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md) ↔ the future Argyris ingest — **compares-with**: both are information-systems-adjacent primary sources, but Gregor classifies articulated prescriptive knowledge while Argyris diagnoses the gap between articulated and behavior-governing theory.

## Reverse-edge Candidates

- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) → the future matching ingest — **evidenced-by**: replace or supplement the current secondary web citation with Argyris's primary formulation of single- and double-loop learning, while marking the note's generality mapping as target-side interpretation.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) → the future matching ingest — **evidenced-by**: cite espoused theory versus theory-in-use as the historical action-theory case in which storage or declaration does not establish operative mediation.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) → the future matching ingest — **evidenced-by**: use Argyris as a conceptual predecessor and boundary case for behavior-governing theory revision, explicitly not as evidence for the conjectured sample-efficiency interaction.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) → the future matching ingest — **evidenced-by**: cite the organization-through-individual-agents case as a human-inclusive predecessor, then state which computational membership, interpretation, and separable-retention requirements it leaves unmet.
- [Soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) → the future matching ingest — **evidenced-by**: ground its organizational-learning summary and defensive-loop account in the primary source while leaving the agent-transfer analysis explicitly target-side.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — rejected as a vocabulary collision. Argyris's “governing values” are assumptions inside a theory-in-use; the note's “governing writes” means selection, validation, authorization, and cross-form coordination of durable updates.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — rejected because the MIS paper does not propose a natural-language/symbolic artifact coevolution loop or bounded validation radius; the action-model and theory-mediated notes already capture its useful transfer.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — rejected because Argyris uses error detection and correction for organizational learning, not probabilistic amplification through discriminating, decorrelated checks.
- [Representational form does not determine whether a theory is a prototype](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) — rejected because tacitness, espousal, and theory-in-use do not decide the prototype note's lifecycle question about operational coupling and revision cost.
- [Ingest: Foundation and History of the PDSA Cycle](../../../../sources/foundation-and-history-of-the-pdsa-cycle.ingest.md) — rejected as a durable peer edge because its explicit prediction-and-study cycle is a broad learning-loop comparator already represented more precisely by Popper; it does not add Argyris's espoused/in-use or defensive-organization distinction.
- [Ingest: Design Theory in Information Systems](../../../../sources/design-theory-in-information-systems-gregor-2002.ingest.md) — rejected in favor of Gregor's mature 2006 taxonomy, which preserves the theory/action vocabulary distinction without duplicating one lineage.
- Commonplace reference documents and external agent-memory/agentic-system analyses — rejected because they describe particular shipped systems or implementations. Argyris supplies conceptual organization-learning theory rather than evidence about those systems, and the accepted notes already carry the relevant transfer.

## Index Membership

None. The sources collection has no curated topical index for this source family; the future ingest will be the durable routing surface. The note tag heads index theory artifacts, not source snapshots.

## Synthesis Opportunities

- Argyris plus [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) and [Selective revision needs a faithful rationale](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) imply two non-substitutable faithfulness interfaces in theory-mediated learning: **theory → action** must be behaviorally operative, and **rationale → producing basis** must be faithful enough for selective revision. Espoused theory can pass readability while failing the first; a plausible rationale can pass readability while failing the second.
- Craik, Popper, Pearl, and Argyris together yield a clean decomposition already distributed across local notes: internal or formal models predict action consequences; criticism selects theory changes; theories-in-use mediate actual conduct; double-loop inquiry revises governing commitments. A future synthesis should preserve these as separable functions rather than call every model-based feedback system “theory-mediated learning.”

## Maintenance Observations

- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) currently relies on an Infed secondary page for the Argyris distinction. Once the matching ingest exists, the primary source should become the durable citation surface.
- [Soft-bound traditions as sources for context engineering strategies](../../../../notes/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) attributes double-loop revision to Argyris and Schön but then adds that it “requires a processor that can reflect on its own history.” This snapshot supports questioning governing assumptions and documents organizational inhibition; it does not directly establish that computational-reflection requirement. A later writer should separate source summary from transfer analysis.
- The capture URL and reprint front matter identify a Winter–Spring 1982 *DATA BASE* reprint of an article originally published in 1977 in *Accounting, Organizations and Society*. The future ingest should preserve both dates and venues rather than silently treating the hosted filename's 1982 date as the original publication date.
- The `pdftotext` capture has pervasive word-internal spacing artifacts and at least one apparent OCR error (“double-loop tearing”). It is adequate for conceptual discovery, but retained verbatim quotes should be checked against page images and carry human-resolvable printed-page locations.

## Flags

- The snapshot is immutable and the matching ingest did not exist during this run. Apply all outbound, bidirectional, reverse-edge, and source-comparison recommendations only after `kb/sources/argyris-organizational-learning-and-mis-1977.ingest.md` exists; never author a durable link to `.snapshots/`.
- Split-candidate signal: the paper makes multiple independent claims and connects to more than five notes across learning theory, action-model operativity, reflection/self-improvement, and context/information-system design. Source identity still calls for one ingest, but its analysis should keep the learning-loop, espoused/in-use, defensive-feedback, and local-versus-distant-MIS claim clusters visibly separate.
- Terminology tension: Ashby's “two feedback loops” and Argyris's “double-loop learning” are not interchangeable. The future ingest should state the distinction explicitly wherever both lineages are connected.
