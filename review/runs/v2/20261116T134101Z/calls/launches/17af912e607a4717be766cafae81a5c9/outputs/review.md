---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["So use of a claim inside the theory can be a test, and often it is not. What decides is whether the use could have gone against the claim, not where the evidence was produced."]
    reason: "SUPPLIED — kb/theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md — needs a premise: the distinction between a claim's independent test record and its fit, with the condition that use counts as a test only where it could have gone against the claim. Its passage argues 'The distinction follows because' the note's claim, and its footer labels the link 'grounds'. The note states both the distinction and the condition."
  - scope: passage
    quotes: ["A well-tested claim may fit poorly."]
    reason: "SUPPLIED — kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md — needs a premise: claims that have each survived independent tests may still fit poorly or fail to help the system reason, modify or recover. Its footer labels the link 'grounds'. The note's section 'A good test record does not make a claim fit' supplies this, and its fit definition names explanation, prediction, search and modification."
  - scope: passage
    quotes: ["A false, overgeneral or weakly tested claim may fit smoothly, because the current implementation, the vocabulary or the neighbouring claims already assume it."]
    reason: "SUPPLIED — kb/sources/an-assumption-based-tms.ingest.md — needs a distinction to serve as a 'formal counterpoint': derivability and consistency relative to an assumption environment do not establish a member's 'independent warrant or theory fit'. The note treats agreement with retained claims as part of fit and denies that such agreement is an independent test. The ingest uses the retired term 'warrant' and the note's former title; the note's sentence on the rename from 'warrant' to 'test record' maps the ingest's 'independent warrant' to the note's test record."
  - scope: passage
    quotes: ["A test record carries a date."]
    reason: "PARTLY SUPPLIED — kb/sources/formal-learning-theory.ingest.md — needs a temporal separation: a method's convergence across complete evidence sequences does not warrant its conjecture at a finite stage. The note supplies dated test records and timeless truth via Popper §84. It says nothing about a method's convergence or eventual success, so the specific contrast the ingest claims to support is not in the note."
  - scope: passage
    quotes: ["Retaining a claim is a decision about what the theory is for. The claim's test record does not make that decision."]
    reason: "PARTLY SUPPLIED — kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — needs a separation of formal theory change from warrant: postulates constrain how membership changes while leaving the warrant of retained or introduced propositions unsettled. The note separates retention decisions and contradiction repair from test record. It does not address formally admissible contraction or revision operations, so the claim that formal admissibility leaves warrant unsettled is not stated."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/tags/evaluation-README.md — needs only a citation, glossed 'truth, test record and fit are separate questions; fit is a test only where the claim could have failed'. The note's description and sections match the gloss."
  - scope: document
    quotes: []
    reason: "SUPPLIED — kb/tags/theory-builder-README.md — needs only a citation, glossed 'distinct questions require separate assessment' under the link text 'Test record and theory fit'. The note supplies this; the gloss omits the truth question."
  - scope: passage
    quotes: ["So use of a claim inside the theory can be a test, and often it is not. What decides is whether the use could have gone against the claim, not where the evidence was produced."]
    reason: "DUPLICATED — kb/theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md — its description restates this condition: system-use consequences 'add to its independent test record only where the use could have gone against the claim'. The dependent restricts it to live system use. The note's version is general and is the one the dependent argues from, so the note states it better as a premise. The dependent states it better for its own scope."
  - scope: passage
    quotes: ["A well-tested claim may fit poorly."]
    reason: "DUPLICATED — kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md — its opening sentence restates the note's claim that claims surviving independent tests may still fit poorly or fail to help the system operate. The note states it better for the dependents' use because it names the ways a tested claim can fit poorly. The dependent's restatement serves only as setup for its own claim."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/formal-learning-theory.ingest.md — recommends revising the note to say explicitly that a method's convergence guarantee does not establish warrant for its current output, citing this ingest as the technical basis. The note neither states this nor cites the ingest."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — recommendation 2 ('Keep formal admissibility separate from warrant', tagged quick-win) says that the representation theorem's account of admissible operations shows no retained belief to be true, well supported or useful, and that this sharpens the note's distinction. The note does not discuss formal admissibility."
  - scope: document
    quotes: []
    reason: "UNTAKEN — kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md — recommends adding this ingest as the note's formal citation, with one sentence saying that AGM characterizes contraction and revision but does not supply discovery or empirical warrant. The note cites only Popper and the epistemic stance, and has no such sentence."
outcome: report
---

# Role in the KB: A claim's test record does not determine its fit in a working theory

## Role
The note is a premise that two theory notes argue from. Both system-use notes use it, under a `grounds` label, for the separation between a claim's independent test record and its fit in a working theory. Three source ingests cite it as the KB claim that their formal results (ATMS, formal learning theory, AGM) support or counterpoint. Two tag heads cite it as the reference for the test-record/fit distinction.
Relied on: the test-record/fit distinction; "fit is not an independent test" with its condition that use counts as a test only where it could have failed; "a well-tested claim may fit poorly"; agreement with neighbouring claims as part of fit rather than as a test; dated test records (formal learning theory, partly). Unused: the separation of truth from test record as a standalone question (only the evaluation tag gloss mentions truth); the section "The two kinds of evidence inform each other"; the definition of independence as not presupposing the working theory; the Scope bullets (no single scale for fit, objectives and authority, non-statistical independence); the section on contradiction repair is used only implicitly by the AGM ingest.

## Dependents
- `kb/theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md`: premise (test record versus fit; use as a test only where it could fail).
- `kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md`: premise (tested claims may still fit poorly).
- `kb/sources/an-assumption-based-tms.ingest.md`: distinction (consistency and derivability are not independent warrant or fit). It uses the retired term "warrant" and the old title.
- `kb/sources/formal-learning-theory.ingest.md`: temporal distinction (eventual convergence versus present warrant). It uses "warrant" and the old title.
- `kb/sources/logic-of-theory-change-partial-meet-contraction.ingest.md`: distinction (formal theory change versus warrant). It uses "warrant" and the old title.
- `kb/tags/evaluation-README.md`: citation only.
- `kb/tags/theory-builder-README.md`: citation only.

## Duplication
- The description of `kb/theory/system-use-provides-evidence-of-theory-fit-not-an-independent-test.md` restates the note's condition that use counts as a test only where it could have gone against the claim, restricted to live system use.
- The opening of `kb/theory/system-use-selects-theory-fit-without-a-fixed-oracle.md` restates the note's claim that tested claims may still fit poorly.
In both cases the note gives the general statement that serves as the premise; each dependent restates it only to set up its own scope.

## Untaken recommendations
- Formal learning theory ingest: state that a method's convergence guarantee does not establish warrant for its current output, citing the ingest.
- AGM ingest, recommendation 2: keep formal admissibility separate from warrant, as a sharpening of the distinction.
- AGM ingest: add the ingest as the formal citation, with one sentence on what AGM does and does not supply.

## Reach
- The test-record/fit distinction, and the claim that a good test record does not make a claim fit, reach both system-use theory notes (as their grounding premise), all three source ingests and both tag heads.
- The condition that fit evidence is a test only where the claim could have failed reaches `system-use-provides-evidence-of-theory-fit-not-an-independent-test.md` and the gloss in `kb/tags/evaluation-README.md`.
- The treatment of agreement with neighbouring claims as fit rather than as a test reaches `an-assumption-based-tms.ingest.md`.
- Dated test records reach `formal-learning-theory.ingest.md`, partly.
- The terms "test record" and "fit" reach the tag heads and both theory notes. The three ingests still use "warrant" and the note's former title, so they depend on the note's rename sentence to map their "warrant" to "test record".
- A change to the truth question, to "The two kinds of evidence inform each other", to the definition of independence or to the Scope bullets reaches no dependent.
