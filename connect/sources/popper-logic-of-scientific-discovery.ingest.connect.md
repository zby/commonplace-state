---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/popper-logic-of-scientific-discovery.ingest.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: Ingest: The Logic of Scientific Discovery

**Source:** [Ingest: The Logic of Scientific Discovery](../../../../sources/popper-logic-of-scientific-discovery.ingest.md)

The ingest already carries a substantial inline Connections Found section (13 targets, all verified to exist). This report lists only candidates that are **not** already linked, plus reverse edges and grounding gaps. All items are candidates; nothing has been authored.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md`, "Outbound links". Destinations: notes, reference, agent-memory-systems, agentic-systems, tags, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (notes, agent-memory-systems), `abstracted-from` (notes), `rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). No label is authorised for `kb/tags/`. External prospecting skipped (no externally supplied targets beyond the ingest's own `source` URL).

**Existing outbound links (excluded from candidates):** `grep -o '](\.\./[^)]*)\|](\./[^)]*)'` on the target, then an existence check on each. All 13 resolve: the Wikipedia ingest, Conjectures and Refutations ingest, POPPER automated-hypothesis ingest, sound-agentic-science ingest, claim-modality, narrowing, ad-hoc, domain-pricing, generality, tentative-theory, theory-builder (+ `#addressability`), learning-inside-a-fixed-decomposition, reference/freshness-architecture.

**Inbound check:** `rg -l "popper-logic-of-scientific-discovery" kb` -> no inbound links. `rg -l "the-logic-of-scientific-discovery-wikipedia" kb` -> only the target links the superseded Wikipedia ingest.

**Tag heads:** the target has no `tags:`, and `kb/tags/COLLECTION.md` lists `participating: [notes, reference, instructions, agent-memory-systems, agentic-systems]`; sources do not participate. Read Popper lines from `foundations-README.md`, `kb-maintenance-README.md`, `theory-builder-README.md`, `self-improving-systems-README.md` for routing signal only.

**Description / title listings:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md' | rg -i "general|evidence|warrant|refut|falsif|test|abstract|particular|instance|universal|repair|confirm|counterexample|criticism|critici|re-exam|reproduc|dated|snapshot"` -- flagged: system-use-provides-evidence..., retaining-episode-evidence..., checked-outcome-licenses..., derivation-and-inheritance..., candidacy-evidence..., theory-warrant-tracked..., superseded-choices..., compounding-is-tested..., a-claims-warrant-does-not-determine-its-fit, use-tests-a-decomposition-locally.
- `rg -m1 '^description:'` on each flagged note plus Popper-adjacent source ingests (realist-view 1966, epistemology-without-knowing-subject 1968, both FALSIFYBENCH ingests, scaffold-not-vocabulary, think-before-you-act, error-centric-intelligence, HEP, Corral, PoPE, Zhang et al., Socratic agents, self-revising-discovery, no-free-lunch).

**Body search** (scope `kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags`, plus `kb/sources` for the first):
- `rg -l -i "popper|logic of scientific discovery|logik der forschung"` -- 24 notes/reference/tag files, 25 source ingests. Per-file context via `rg -n -i -o ".{0,160}popper.{0,160}"`. Unlinked Popper attributions found in abstract-an-experience, title-as-claim-exposes-commitments, mechanistic-constraints, notes/COLLECTION.md (claim-modality paragraph).
- `rg -l -i "corroborat"` -- 20 hits; relevant: an-accepted-edit-verifies-the-change, reference/source-adoption-policy, notes/COLLECTION.md; rest topical (memory requirements, agent-memory reviews).
- `rg -l -i "severe test|severity of (the )?test"` -- 0 hits.
- `rg -l -i "basic statement"` -- 0 hits.
- `rg -l -i "falsifi"` -- 20+ hits; relevant: a-claim-without-external-assessment, theory-warrant-tracked, a-proximate-target, technical-constraints-make-kb-objective, retained-theories-may-improve-sample-efficiency.
- `rg -l -i "reproducib"` -- mostly agentic-system reviews and ADRs about reproducible builds; relevant: commitment-not-derivation (reproduction vs re-examination).
- `rg -l -i "inter-?subjective"` -- 0 hits.
- `rg -l -i "immuniz|immunis"` -- candidacy-evidence, a-framework-rule-with-a-boundary-preserving-rival, domain-pricing (already linked), ADR 066, ADR 080, two tag heads.
- `rg -l -i "auxiliary hypothes"` -- 0 hits.
- `rg -l -i "numerically universal|strictly universal|singular statement"` -- 0 hits.
- `rg -l -i "use-novelty|used to construct|accommodat"` -- no relevant hits.
- `rg -l -i "remov(e|ing) (the )?particulars|universaliz|de-?particulariz"` -- 0 hits.
- `rg -n -i "corroborat|falsifi|popper|particular|universal" kb/notes/COLLECTION.md` -- placement test (lines 5-18) and the claim-modality paragraph (line 63).

**Link following:**
- candidacy-evidence -> theory-warrant-tracked (warrant non-distribution): both belong to the evidence-role cluster.
- system-use-provides-evidence -> a-claims-warrant-does-not-determine-its-fit: fit vs warrant pair; the system-use note carries the self-confirmation mechanism, so it is the better target.
- checked-outcome -> trace-extracted-memory-earns-authority-per-operation: ladder context; checked-outcome is the specific singular/universal claim.
- abstract-an-experience -> first-principles-reasoning (explanatory-reach): Deutsch lineage, not Popper's LoSD; not kept.
- mechanistic-constraints -> title-as-claim notes: these three form the "Popperian maintenance" cluster; none links any Popper source.

## Connections Found

- [System use provides evidence of theory fit and causal usefulness, not independent warrant](../../../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) -- **is-evidence-for**: the note says "successful use can be self-confirming" and that independent evidence "must remain able to overturn the claim". Appendix *ix (C(h, e) counts only when e reports "sincere efforts to overthrow h") and §30 (no "stray basic statements") are the primary-source form of that rule. This is also the closest note to Extractable Value 4.
- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- **is-evidence-for**: §29 accepts test records ("certificates of tests") because they "can be re-examined", and §§8, 27 make re-examinability with stated instructions the condition of objectivity. This supports the note's central claim and Extractable Value 2 (classify internal evidence by re-examinability, not origin).
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **is-evidence-for**: §§13-14 hold that singular statements do not yield universal ones by abstraction, and §22 treats one case as short of a reproducible effect. Both back the note's split between a case-level claim and an abstracted explanation.
- [Derivation and inheritance give starting warrant; discriminating evidence or proof earns scope](../../../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md) -- **is-evidence-for**: Extractable Value 1 says a de-particularized claim is a new conjecture that reference-side evidence corroborates only to the extent it severely tested that claim. §83 adds that new instances add little unless from "a new field of application". This matches "evidence earns only the scope it covers".
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- **is-evidence-for**: §22 gives the refutation-side version of the two-role split. A single failed case justifies a reproduction attempt (candidacy), and only a corroborated falsifying hypothesis falsifies (verdict). §§19-20's conventionalist stratagems are the source of the "immunizing slot" vocabulary the note uses. The note's current external anchor is Peirce only.
- [A claim without external assessment carries three obligations](../../../../notes/a-claim-without-external-assessment-carries-three-obligations.md) -- **is-evidence-for**: the first obligation is "a rule for what counts as contradiction and what support licenses each use". §§27-30 (basic statements accepted by rule-governed decision, open to further test) and §22 (falsification needs a reproducible effect) are Popper's rule for that exact slot.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- **is-evidence-for**: §18 is the refutation-side mirror of warrant non-distribution. Modus tollens falsifies the whole premise set, and blame reaches one component only through an identified route (e.g. a newly introduced hypothesis). The note argues the support side; the book supplies the symmetric falsification side.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **is-evidence-for**: the note cites "Karl Popper" in Sources with no link for the success/failure asymmetry. The book states the verification/falsification asymmetry (§6, the Wikipedia ingest's quoted passage) and §§13-14 on why a lesson drawn from one episode is a new universal conjecture.
- [Title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) -- **is-evidence-for**: the note invokes "Popper's criterion" with no source. §§21, 31-35 define empirical content as the class of basic statements a theory forbids, which is what "declare what would make them wrong" relies on.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) -- **is-evidence-for**: its falsifier blocks state a claim's potential falsifiers (§21), and its contradiction-first connection practice matches §22's deductive-testing direction. The note has no Popper source link at all.
- [Popper: A Realist View of Logic, Physics, and History](../../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) -- **compares-with** on the axis *how test outcomes are accepted*: that ingest's description says the problem-theory-criticism cycle "leaves acceptance and operational checks unspecified"; LoSD §§27-30 supplies acceptance of basic statements by rule-governed decision.
- [Popper: Epistemology Without a Knowing Subject](../../../../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md) -- **compares-with** on the axis *what makes knowledge objective*: 1934 locates objectivity in inter-subjective testability (§8); 1968 locates it in objective conjectural contents separate from acts of thought. Both bear on whether internal records count as evidence.
- [FALSIFYBENCH full text](../../../../sources/falsifybench-rule-discovery-games-full-text.ingest.md) -- **compares-with** on the axis *severity versus count of tests*: FALSIFYBENCH links negative (falsification-seeking) test selection to rule recovery; §82 makes corroboration depend on test severity, not instance count. (The abstract-level [FALSIFYBENCH ingest](../../../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) is the weaker alternative target.)
- [Hypothesis Evolution Protocol](../../../../sources/hypothesis-evolution-protocol-auditable-ai-scientists.ingest.md) -- **compares-with** on the axis *how a corroboration record is kept*: HEP enforces evidence attachment before belief changes and records elicited beliefs; §84 makes corroboration a dated appraisal relative to accepted basic statements, not a belief. This bears directly on Extractable Value 3 (claim-level corroboration links).
- [Source adoption policy](../../../../reference/source-adoption-policy.md) -- **see-also**: its "Direct observation: a separate path" section is where Commonplace currently places internal evidence (improvement log, friction notes, prose reviews). Extractable Value 2 proposes classifying that evidence by re-examinability; a reader acting on the occasion's internal/external distinction needs this page.

## Bidirectional Candidates

- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) <-> source -- **evidenced-by** (notes-side label): the note uses "immunizing" as its central failure term, and §§19-20 are its origin; the return edge gives the note a Popper anchor next to Peirce.
- [System use provides evidence of theory fit and causal usefulness, not independent warrant](../../../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) <-> source -- **evidenced-by**: appendix *ix grounds the self-confirmation warning; useful once a quote is retained.

## Reverse-edge Candidates

Notes-side label is `evidenced-by` ("the target observation, case, or source corroborates, qualifies, or bounds this assertion"). The ingest's Quotes section is empty, so each of these should go through cp-skill-ground first.

- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) → source -- **evidenced-by** (qualifies): the note cites §36 by title only; the ingest finds that the "content held constant" trade is the note's own extension, since Popper calls the universality/precision pair non-comparable. Highest-priority reverse edge because it corrects an attribution.
- [Tentative theory](../../../../notes/definitions/tentative-theory.md) → source -- **evidenced-by**: §§82-85 "tentative for ever"; the ingest's Recommended Next Action already names this grounding.
- [Claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) → source -- **evidenced-by**: its two unlinked Popper attributions are §§65-68 and §2.
- [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md), [Ad hoc explanation can be rational when error is cheap and local](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md), [Domain pricing routes an exception to idealization assessment](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) → source -- **evidenced-by**: §§19-20 is the original statement of the rescue moves each note guards against.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) → source -- **evidenced-by**: replaces its bare "Karl Popper" Sources bullet with a linked ingest.
- [Title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) → source -- **evidenced-by**: grounds "Popper's criterion".
- [Theory builder](../../../../notes/definitions/theory-builder.md) → source -- **evidenced-by**: §16's requirement that each new assumption be recognizable as a revision supports the localized-content condition.
- [The Logic of Scientific Discovery (Wikipedia ingest)](../../../../sources/the-logic-of-scientific-discovery-wikipedia.ingest.md) → source -- **see-also** (sources-side): the target says it supersedes the Wikipedia ingest, and that ingest's Recommended Next Action asked for this text; a forward pointer stops readers stopping at the tertiary source.

## Off-authorisation Candidates

- [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md) -- the claim-modality paragraph (line 63) states "Popper's treatment of probabilistic claims" with no citation; §§65-68 is that treatment. Separately, the placement test (lines 5-18) governs exactly the reference→notes move the occasion plans, and §§13-14 bear on it. A COLLECTION.md is a system-definition artifact, not a claim or analysis, so `is-evidence-for` does not fit and `see-also` would under-describe it. Suggest: route as a reverse edge (a citation added by the notes collection's maintainer) rather than extending the sources label set.

## Raw Text Candidates

None

## Rejected Candidates

- [A framework rule with a boundary-preserving rival is not inherited](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) -- uses "immunize" only for circular boundary declarations; the §20 link is already carried by domain-pricing and candidacy-evidence.
- [First-principles reasoning selects for explanatory-reach](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- relevant to §12's warning, but its lineage is Deutsch; linking LoSD would blur the attribution.
- [Commonplace builds a theory builder and tests whether it learns](../../../../notes/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md) -- already cites the 1966/1968 texts for the method; the ingest states LoSD does not ground the learning hypothesis, so it adds nothing load-bearing.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- same singular/universal point as checked-outcome, which is the sharper target; one link suffices.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md) -- §85's supersession-by-better-testable-theory is adjacent but the note concerns retention, not supersession criteria.
- [False-positive generation is filtered before retention](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- "Popperian reread" is a keyword-only match.
- Source ingests scaffold-not-vocabulary, think-before-you-act, error-centric-intelligence, form-not-content (PoPE), Corral, Zhang et al., Socratic agents, no-free-lunch -- use "Popperian" as a label for LLM procedures; none shares a named axis with the book's doctrines strong enough for `compares-with`.
- [kb/agentic-systems/reviews/evoontology.md](../../../../agentic-systems/reviews-archive/evoontology.md) -- "falsifiable hypothesis" in a host method description; keyword only.
- [ADR 066](../../../../reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) -- the claim-modality note is the better target; the ADR records the decision, not the theory.

## Index Membership

None. Sources do not participate in tags (`kb/tags/COLLECTION.md`), and `kb/sources/README.md` has no per-source index.

## Synthesis Opportunities

Five notes and the book together imply one claim not yet stated anywhere: **evidence counts toward a claim's corroboration by how it was produced, not by where it came from. It must be re-examinable, gathered as an attempt to refute the claim, and severe for the claim's stated scope.** The inputs are [system-use-provides-evidence](../../../../notes/system-use-provides-evidence-of-theory-fit-not-independent-warrant.md) (self-confirmation), [retaining-episode-evidence](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) (re-examinability), [checked-outcome](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) (singular vs universal), [derivation-and-inheritance](../../../../notes/derivation-and-inheritance-give-starting-warrant-earns-scope.md) (scope earned by evidence), [candidacy-evidence](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) (candidacy vs verdict), plus §§8, 22, 29, 82-84 and appendix *ix. This is the operator's occasion (internal vs external evidence, corroboration links) stated as a claim. Per the fold-don't-spawn preference, check first whether it fits as a ≤200-word section in system-use-provides-evidence before writing a new note.

## Maintenance Observations

- Three notes attribute doctrines to Popper with no source link: abstract-an-experience (Sources bullet "Karl Popper"), title-as-claim-exposes-commitments ("Popper's criterion"), mechanistic-constraints (whole note). notes/COLLECTION.md line 63 does the same for probabilistic claims.
- The target has no inbound links, and the superseded Wikipedia ingest is linked only from the target. Once reverse edges move to this ingest, the Wikipedia ingest may have no inbound links; decide whether to keep it as the record of the earlier tertiary reading.
- The target's Quotes section is empty while its Connections Found makes section-level attributions (including the correction to the generality note). Every reverse edge above needs cp-skill-ground first to be semantically checkable.
- Searches for "basic statement", "severe test", "inter-subjective", "auxiliary hypothesis", and "strictly/numerically universal" return 0 hits across notes/reference. The KB has no vocabulary yet for the book's concepts that the occasion needs (corroboration severity, re-examinable basic statements, singular vs strictly universal claims).

## Flags

- **Tension (unresolved):** the notes placement test (notes/COLLECTION.md lines 5-18) admits a claim bounded to Commonplace when the particular's scope is recoverable. Extractable Value 1 says that deleting the particular yields a new strictly universal conjecture whose support from reference-side evidence has to be re-earned. The occasion's plan (move reference claims to notes by removing particulars) must satisfy both, and it is not yet decided which route is the default: a scoped singular claim, or a new universal one.
- **Attribution correction pending:** the generality note's §36 attribution is flagged by the ingest as the note's own extension; a reviser should act on it before any further citation of §36.
- Not a split candidate: the target is an ingest report, which is expected to land across many clusters.
