# Assessment: system-use-provides-evidence-of-theory-fit-not-an-independent-test

Purpose (as given): Make the note easier to read for KB maintainers without changing its claims.

No review findings, earlier decisions, depth 1 reports or role report came with the artifact. The argument does not need restructuring: the claims are distinct and run in a sensible order. Passes can work on the whole text.

## Ranked changes

1. **One name for each of the two things being separated.** The note's point is a split between "fit" and "independent test". But the fit side is named five ways: "integrated into the working theory and causally useful", "fit", "operative fit", "participates usefully in the theory's operation" and "integration and causal usefulness". The test side moves between "independent test record", "independent test", "independent factual, formal, source, and scope evidence" and "a test of the claim's truth, validity or scope". The evidence source also has several names: "putting a claim to work in a live system", "consequential use", "system use" and "system-building consequences". A maintainer cannot tell whether "operative fit" is narrower than "fit", or whether "system-building consequences" means the same as "system use". Cost: about six word-level swaps across the body. Pass: `abstractions`.
2. **Put the point where readers will find it, and repair the connectives.** The paragraph that states the note's division ("The useful division is therefore not 'system evidence versus real evidence'…") is the clearest statement of the claim. It is buried at the end of the "both directions" section, where it does not belong. It also repeats the opening's last sentence and scope bullet 3 ("could have gone against the claim"). "Conversely" opens a paragraph that continues the previous paragraph's direction (negative evidence) rather than reversing it. The opening paragraph packs a seven-item list ("proposal, diagnosis, branch allocation, modification, recovery, transfer, or later operation") and a conditional into one sentence that needs a second reading. Cost: moving one paragraph, merging the duplicate, and splitting one sentence. Pass: `readability-and-flow`.
3. **Plain wording for a few unexplained terms.** "Read-back" is used once and never explained. "Branch allocation" is opaque outside one subsystem. "Reward its own misconceptions" is a figure where a literal phrase ("confirm its own errors") would do. Cost: three or four per-item proposals. Pass: `plain-wording`, run after the structural moves land.

Not recommended: `opening-and-title` — the title states the claim plainly, and the readability pass already covers the dense opening sentence. `narrow-overclaims` — the purpose excludes claim changes, and no sentence is a supporting overclaim worth narrowing (see below).

## Sentence a hostile reviewer would attack first

"A claim that changes search, helps distinguish rival repairs, reduces later repair, or transfers to a new case has stronger evidence that it participates usefully in the theory's operation." The paragraph after next lists "transfer outside the cases that shaped the current theory" as an *independent* check. So transfer is counted on both sides of the division the note draws, and the note does not say which transfers count as fit evidence and which count as tests. (The operator should resolve this. See the claim questions below.)

## What reads well

The self-confirmation paragraph ("Earlier implementation choices may already assume the claim; … an evaluator may share the same error") names concrete mechanisms in short clauses, and that is the note's strongest support.

## Candidate overclaims: support or divergence

- "It does not by itself add to the claim's independent test record, and it does not show that the claim is true." — **divergence (defend).** This is the note's thesis.
- "System-building consequences are real evidence for integration and causal usefulness." — **divergence (defend).** This is the positive half of the thesis. The self-confirmation paragraph could also undercut fit evidence, but that is an argument for the operator to settle, not for a pass.
- "They become a test of the claim's truth, validity or scope only through an additional argument showing that the observed consequence could have gone against the claim." — **divergence (defend).** It is the criterion the description repeats.
- "Successful use can therefore be self-confirming." — support, but already hedged ("can"). No narrowing is needed.

## Stale qualifications and claim questions for the operator (not passes)

- **Transfer is placed on both sides of the division** (paragraphs 2 and 4), as described above. The operator should decide whether transfer to a new case is fit evidence, an independent test, or a test only when the case lies outside the cases that shaped the theory.
- **The title and filename disagree.** The title says "evidence of theory fit and causal usefulness". The filename slug is `…-evidence-of-theory-fit-not-an-independent-test` and drops "causal usefulness". A relocation, if wanted, is its own commit.
- **Scope bullet 3 restates the body's criterion** instead of qualifying it. If the readability pass merges the "useful division" paragraph into the opening, the bullet becomes a third copy. The operator may want it cut or turned into a real scope limit.

## Findings not acted on

None were supplied.
