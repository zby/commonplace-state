---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "These are conjectures from"
    reason: "Basis: supplied-source-1 (and supplied-source-2) opens with a 'Due for rewriting' banner: 'Commonplace's research program is now stated in terms of selection-based learning. How the theory builder relates to it has not been worked out.' The lead article (supplied-source-6) likewise frames the program as selection-based learning. The candidate's Status paragraph says the bets come from 'Commonplace's research program, which builds for fine-grained premises and long persistence and holds model weights fixed', which presents the superseded theory-builder framing as the program's current statement. The commission asks to keep provenance beside the claim. Required change: attribute the conjectures to Commonplace's theory-builder research note (or 'an earlier statement of Commonplace's research program') rather than to the research program as currently stated, or add one clause saying how the theory-builder design relates to the program is still open."
    level: warn
  - scope: passage
    quotes:
      - "It can run a discriminating test: trace which files the build actually opens and compare them with the list."
    reason: "Basis: the candidate names one discriminating test (trace reads against the list) and then lists three outcomes, the second of which ('If the failure reproduces with the snippet reverted, the snippet was not the cause at all') belongs to a different test, a revert-and-replay. The commission asks the article to show 'what observation or discriminating test could overturn its diagnosis'; the content is present, but the paragraph presents two tests as one. Required change: name the revert check as a second test (for example 'It can also revert the snippet and rebuild') so each outcome is tied to the test that produces it."
    level: warn
  - scope: passage
    quotes:
      - "(\"the list is exhaustive\") learns more than criticism aimed at the account as a whole"
    reason: "Basis: the article collection contract asks for direct, literal wording. Criticism does not learn; the system does. supplied-source-1 phrases the conjecture as criticism that identifies a part 'may yield more learning from a failure'. Required change: rephrase so the system is the learner, e.g. 'a system learns more from criticism aimed at one premise ... than from criticism aimed at the account as a whole'."
    level: warn
  - scope: passage
    quotes:
      - "The lead's loop can also select a self-edit without stating why it works."
    reason: "'The lead's loop' is KB-internal shorthand; an external reader meets 'lead article' once in the opening. 'The loop in the lead article' or 'the basic selection loop' would read more plainly. No change required."
    level: info
  - scope: document
    quotes: []
    reason: "The affected-citations report matches the supplied inbound passages: it covers all seven inbound files, separates the two passages in each of bootstrapping, testing, what-an-automated-reviewer and the harness ingest, and identifies each lost use accurately (the fixed-weight bet, the two-part learning test, the K(t) schema, the program statement, the headline counterpointed by the ingest). Its suggested repairs are correctly left as separate work."
    level: info
outcome: warn
---

# Review

The candidate makes the commissioned contribution: a short, self-standing companion (about 1,000 words, inside the 750–1,100 target) that tells a maintainer what retaining and testing an explanation adds beyond a winning patch, organised as three separable bets, each with a comparison that can come out negative or mixed. It keeps the H1, path, byline, status and banner as reserved, and updates `description` and `source_notes` to the new contribution.

## Commission coverage

Every must-keep item is present and grounded in the authorized sources:

- The explicitly hypothetical README → inspect-configured-inputs → indirect-include case follows supplied-source-4 and supplied-source-5, and the account's wording matches the lead (supplied-source-6) without duplicating the lead's loop introduction.
- The next investigation differs concretely: the retained account gives a premise to suspect, a trace that could overturn it, and a revision that changes predictions for files that have never failed. The patch-only system is explicitly allowed to succeed ("is not doomed").
- Bet one matches raw evidence, budget and diagnosis cost, counts wrong diagnoses, and separates supplying a diagnosis from discovering it.
- Bet two separates the target of criticism from edit size (supplied-source-1), checks prior and fresh cases, cites "locating a candidate premise is not identifying a cause" (supplied-source-3), and gives the intervention test with the patch held fixed and the premise withheld or contradicted (supplied-source-4). Availability is explicitly not treated as operation.
- Bet three compares carrying against reconstruction from the same case history, base model and patch, measures new target observations to a common threshold and total cost at comparable quality, says these can diverge (supplied-source-5), and gives the required mixed result.
- The theory-about-a-client versus research-on-own-method distinction is drawn, and selection of a self-edit is explicitly not counted as theory building, which follows the operator's direction not to make "theory builder" the umbrella term.
- Conjectural status is stated in the opening ("None has been tested") and in Status, together with the limit that human-staffed Commonplace is not evidence for an autonomous system.

The must-exclude items are absent: no Gödel/Naur argument, Bitter Lesson section, compounding discussion, supplement list or study results. The single pointer to the testing supplement is the optional pointer the commission allows.

## Remaining changes

None of the findings blocks publication. The most substantive one is provenance. The Status section attributes the bets to "Commonplace's research program" as if that program were still stated as a theory-builder design. Both theory-builder sources now carry banners saying the program is stated in selection-based terms and that the relation is unresolved. One clause or a narrower attribution fixes this. The other two warnings are local clarity fixes: the discriminating-test paragraph conflates a trace with a revert check, and bet two's conjecture makes criticism the learner.

## Affected citations

The writer's report identifies every lost use in the supplied inbound passages accurately. The candidate is not wrong to drop these uses. Repairing the dependents is separate work.
