---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["The comparison names the predecessor and adopted successor, the requirements under which the successor counts as better, and how those requirements apply to the predecessor's prior capabilities."]
    reason: "The opening spends two sentences on the retention definition and then gives the comparison's requirements only as empty slots. The two-component relation the reader most needs (non-regression on the predecessor's prior capabilities plus a declared gain on a named dimension, both fixed before development) first appears in the second section, and a later paragraph restates the non-regression scope a second time; a revision could compress the retention setup to one contrast clause, fill the roadmap sentence with the two components, and fold the separate non-regression-scope paragraph (keeping its threshold gloss) into the two-component sentence, so the relation section elaborates rather than introduces."
  - scope: document
    quotes: []
    reason: "The boundary that a properly declared comparison need not track real factory quality is stated four times (opening paragraph, end of the antecedence paragraph, first and second Scope bullets), and the Scope section mostly restates limits the body already draws, which blurs the few boundaries Scope adds; a revision could state the quality-tracking limit once and reduce Scope to the boundaries the body does not draw (retrospective criteria can ground a different improvement claim; a relation permitting retirement can be declared; the framework transfers to other revising systems)."
  - scope: document
    quotes: []
    reason: "The 'Improvement, retention and learning' section starts by separating this claim from its neighbours but then branches into how to establish learning (the with/without-instruction experiment paragraph), and the separate question of what controlled adoption recurs in three places (relata section, end of the improvement section, fifth Scope bullet); a revision could cut that section back to the boundary that improvement is distinct from retention and from learning, move the evidence method for learning to the factory-learning note, and state the adoption-versus-judgment distinction once, most naturally in the relata section where candidates and installed successors are already separated."
outcome: report
---

# Simplification synthesis: A better-factory claim compares operative states under an antecedent assessment relation

The note's core claim is findable from the title and opening, and its section order (relata, relation, neighbouring claims, Scope) follows the argument. The material gains come from three places: the opening withholds the relation's content, one quality-tracking boundary recurs across body and Scope, and the neighbouring-claims section plus scattered adoption asides drift away from the comparison the note is about. None of these needs a new thesis. Each needs an author decision about which of several near-duplicate statements carries a distinct meaning.

## Opportunities

### 1. Put the two-component relation in the opening and drop the second non-regression statement

- Location: opening paragraphs, from "A [software factory](./definitions/software-factory.md) undergoes experience-responsive retention…" through "…how those requirements apply to the predecessor's prior capabilities."; plus the "## The assessment relation is antecedent and scope-indexed" paragraph beginning "Non-regression needs a declared scope:".
- Combines: core-claim-obscured (both INFO findings: withheld relation content in the roadmap sentence; retention setup before the note's own claim); marginal-value-redundancy (WARN on the "Non-regression needs a declared scope" paragraph).
- Preserve or decide:
  - "This framework uses the predecessor's prior capabilities as that scope" is a framework choice. The fourth Scope bullet says other relation shapes are declarable. The folded sentence must still mark it as this framework's declared shape, not the only possible one.
  - Keep the threshold gloss: thresholds specify how much degradation is permitted. It is the one addition the non-regression paragraph makes.
  - The opening's link to the factory-learning note and the clause that retention has no quality requirement carry the reason the note exists. Compress the retention setup, but do not cut it.
  - The `TODO` blockquote leaves the choice between "software factory" and "software house" unresolved. Rewriting the opening would touch that term, so the author should settle it first rather than treat it as a compression edit.
  - One possible resolution, for illustration only: "Whether a factory got better is a separate claim: it compares the predecessor with the operative successor, requiring non-regression on the predecessor's prior capabilities and a declared gain on a named dimension, both fixed before development."

### 2. State the quality-tracking limit once and let Scope carry only new boundaries

- Location: the opening's "not a verdict on the factory's quality over its open production family"; "Prior declaration prevents that form of post-hoc selection. It does not show that the requirements track factory quality."; Scope bullets 1 ("The framework indexes and disciplines the comparison…") and 2 ("Antecedence blocks post-hoc dimension selection…"); and the trailing sentence of Scope bullet 6 ("Preserving factory development follows only when…").
- Combines: detail-overhang (INFO on the recurring quality-tracking caveat); marginal-value-redundancy (WARNs on Scope bullets 1 and 2 and on the trailing sentence of bullet 6).
- Preserve or decide:
  - The repeated statements are not obviously the same claim. "Does not supply an oracle; what makes a successor genuinely better over an open family remains unresolved" is a gap in the theory. "Can still measure something that does not matter" concerns the validity of the chosen dimensions. "Antecedence is not constitutive of improvement" (bullet 3) concerns the legitimacy of retrospective criteria. The author must decide whether the first two are one boundary or two before merging them. Bullet 3 should stay distinct.
  - Decide where the single statement lives: in the opening, which frames how the reader takes "better" throughout, or in Scope. The opening's "Throughout, *better* means better under the declared relation" defines a term, and should stay even if the caveat moves.
  - Keep the Scope bullets the marginal-value check found new: retrospective criteria, a relation that permits retirement (with its consequence for the preserved path), and the transfer to other revising systems.

### 3. Keep the neighbouring-claims section to its boundary and state adoption control once

- Location: "## Improvement, retention and learning are different claims", especially the paragraph beginning "The third case requires evidence of that contribution…"; "Internal controls on what the factory retains govern adoption…"; the relata section's "A staging comparison can supply evidence for adopting a candidate…"; and the fifth Scope bullet ("A comparison judges the adopted states…").
- Combines: branch-bloat (WARN on the experiment paragraph; INFO on the two adoption-control asides); marginal-value-redundancy (WARN on the fifth Scope bullet).
- Preserve or decide:
  - The note's description and claim concern the comparison, not how to identify learning. The three hypothetical cases do separating work, and the line "The declared comparison judges improvement; the experience-to-change link distinguishes learning" turns them into a rule. Both should survive. Whether the causal-contribution method belongs here or only in the factory-learning note is an ownership decision for the author. Cutting it also changes the "grounds" link to the experiment-contrast note in Relevant Notes.
  - The three adoption statements may carry different meanings. Staging evidence supports adoption. Internal retention controls do not establish passing the comparison. A description cannot change whether an evaluator's judgment was required for installation. The last clause is opaque, and its intended objection is not stated. The author must decide whether it makes a distinct claim, such as that relabelling an evaluator after the fact does not make it a gate, before folding or cutting it.
  - "A change that improves the factory against another objective need not pass this comparison" bounds relation-relativity rather than adoption. Keep it, or fold it into opportunity 2's single statement.
