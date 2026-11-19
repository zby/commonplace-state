---
description: "Candidate connections between Popper's Conjectures and Refutations and KB claim criticism, testing, and repair."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/popper-conjectures-and-refutations.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Conjectures and Refutations

**Source:** [Conjectures and Refutations](../../../../sources/.snapshots/popper-conjectures-and-refutations.md)

## Discovery Trace

Source reading was selective across this book-length capture: preface, contents, Introduction XIII–XV, Chapter 1 opening and numbered demarcation conditions, and Chapter 10's discussion of content, background knowledge, and three requirements. The complete extracted book is preserved; this discovery pass does not claim an exhaustive chapter-by-chapter reading. Candidate passages are locators for independent verification by the drafting worker.

Read the source collection's outbound rules and the connect-report type. Read the notes README, tags hub, discovery and evaluation heads; the discovery head is marked complete, so no discovery-tag enumeration was needed. Read the reference and sources READMEs and the opening navigation of agent-memory-systems and agentic-systems. Generated fresh title listings with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of the five destinations. The combined output exceeded the tool window; repeated a filtered title pass for `popper|falsif|refutat|candidacy|conjectur|claim modality|claim mode|repair|discovery|corroborat` over the complete listings (429 notes, 162 reference, 400 sources, 175 memory-system, 20 agentic-system titles).

Ran `rg -n -i 'popper|conjectur|refutat|falsif|corroborat'` over those destinations; the broad result exceeded the output window, so narrowed to `rg -l -i 'popper' ... | xargs -r rg '^description:'`. Read the claim-title maintenance, mechanistic Popperian practices, narrowing, widening, discovery-lifecycle, candidacy-evidence, claim-modality, disposable-ad-hoc-explanation, prior Popper ingest, and FALSIFYBENCH candidate material. Followed the claim-title note to the mechanistic practices note, narrowing to widening, and discovery to candidacy. Read the notes collection's reverse-link authorization.

Reference prospecting found ADR 066 and the repair-dispositions proposal; the directly relevant theoretical notes provide the more useful landing points, so no reference edge was retained. The memory and agentic-system collections had no direct Popper title matches, and their implementation reviews are too distant from the source's claims for a useful direct edge. No external prospecting was performed; only the supplied primary URL is an external candidate.

## Connections Found

- [Claim titles expose commitments](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — **is-evidence-for**: Chapter 1's account of a theory's forbidden outcomes supplies the philosophical premise for exposing criticizable commitments; the source does not establish the note's maintenance-cost claim.
- [Narrowing bought to survive review](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) — **is-evidence-for**: Chapter 1, numbered point 7, and Chapter 10 distinguish information-bearing revision from rescue that reduces testable content; the note supplies the KB repair witness.
- [Generality bought to avoid counterexamples](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — **compares-with**: Chapter 10 relates content to testability and precision, providing a comparison for the note's content-preservation test; verify the exact tradeoff rather than treating this as a substitute for its named Logic of Scientific Discovery source.
- [Candidacy evidence and acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — **compares-with**: Chapter 10, sections XVIII–XX, separates formal requirements for a serious candidate from the empirical success requirement. The distinction resembles staged assessment but is not the note's complete cost or warrant argument.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **compares-with**: Chapter 10's tests and new problems provide a contrasting account of knowledge growth; Commonplace's acceptance and integration phases and Peircean induction are additional commitments.
- [Mechanistic Popperian KB practices](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — **is-evidence-for**: the Introduction's error-elimination question and Chapter 1's risky predictions ground the epistemic premise. Bounded-context mechanics and the efficacy of falsifier blocks remain the note's own argument.
- [A Realist View of Logic, Physics, and History](../../../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md) — **compares-with**: compare this collection's severe-test and content criteria with the later essay's explicit problem–theory–error-elimination–new-problem cycle and objective artifacts.
- [FALSIFYBENCH](../../../../sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md) — **compares-with**: contrast philosophical criticism of confirmation-seeking with a bounded empirical operationalization in rule-discovery games; neither establishes effectiveness for natural-language KB review.
- [Primary source](https://padron.entretemas.com.ve/documentos/Popper-Conjectures-Rwefutations-GrowthOfKnowledge.pdf) — **derived-from**: external primary source of the prospective ingest analysis.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Narrowing bought to survive review](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) → prospective ingest — **evidenced-by**: the source can support the content-reduction premise, with a retained quote or snapshot-required citation, while leaving the local witness separate.
- [Claim titles expose commitments](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) → prospective ingest — **evidenced-by**: supports the attributed Popper premise, with the same grounding requirement; it does not prove that every claim title declares an adequate falsifier.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Claim modality](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md): relevant but its Peircean and abductive typology is not directly established by Popper. Its probabilistic-claim attribution needs a separate exact passage check, not an inferred endorsement from general falsifiability.
- [Ad hoc explanation can be rational](../../../../notes/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md): the note explicitly distinguishes disposable local guesses from Popper's content-reducing rescues, so the shared phrase alone is no disagreement and adds little traversal value.

## Index Membership

- [Discovery](../../../../tags/discovery-README.md): a future curated primary-source reference on tests and theory growth, if useful beyond the existing prior Popper ingest.

## Synthesis Opportunities

The narrowing and widening notes, combined with Chapter 10's independent-test requirement, suggest inspecting whether a repaired claim still forbids something beyond the failures used to repair it. This is a candidate inquiry, not a new established policy.

## Maintenance Observations

The sources README describes plain WebFetch for generic captures, while the executed snapshot skill specifies Trafilatura and Poppler. No repair was made.

## Flags

The source spans epistemology, philosophy of physics, and political criticism. Keep the ingest source-wide but selective for the KB; any later extracted notes should isolate their claims rather than reproduce the book's scope in one note. This is a multi-claim source with connections across discovery, foundations, maintenance, and writing failure modes.
