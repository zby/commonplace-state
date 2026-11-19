---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-domain-priced-exception-does-not-refute-an-idealization.md"
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: A domain-priced exception does not refute an idealization

**Source:** [A domain-priced exception does not refute an idealization](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md)

## Discovery Trace

**Description listing scan:**
- Read the `notes` collection's outbound-link rules and scanned the authorised local destinations: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/`. `kb/work/` was excluded by contract.
- Generated a fresh full title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorised local destination.
- Ran the scoped description query `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/sources kb/instructions --glob '*.md' | rg -i 'counterexample|refut|idealiz|model|boundary|rival|exception|adequacy|warrant|review|claim'`.
- The reference proposal on repair dispositions was retained as a companion. Agent-memory-system descriptions supplied no system-specific evidence for the idealization criterion, so that destination produced no candidate.

**Topic indexes:**
- Read `kb/notes/tags-README.md`, `document-system-README.md`, `failure-modes-README.md`, and `kb-maintenance-README.md`; the source already carries the corresponding tags, but it is absent from the curated failure-modes head.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. The reference proposal is the only directly relevant curated/system surface found.

**Body search:**
- `rg -n -i "idealiz|counterexample|refut|immuniz|bounded|subordinate|intended use|model adequacy|priced exception|pricing" ...` -- surfaced the one-way rival test, formal reach-assessment, the repair-dispositions proposal, and the two existing inbound citers.
- `rg -l -i 'Lakatos|Popper|ideal gas|idealization|immunizing stratagem' ...` -- found Popper-adjacent snapshots but no captured source that directly establishes the note's domain-pricing discriminator; those broad mentions were rejected as grounding.
- `rg -n "a-domain-priced-exception-does-not-refute-an-idealization|A domain-priced exception does not refute an idealization" ...` -- found existing inbound dependencies from the repair-dispositions proposal and the instantiation/agent-learning note.

**Link following:**
- Followed the source's existing narrowing, generality, Popperian-maintenance, worked-case, and methodology links. They already cover the neighboring repair modes and the two repository episodes.
- Followed `a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md` to its boundary-invariant and first-principles links; its one-way rival rule directly qualifies the source's rival-paradigm pricing signature.
- Followed `formal-systems-assess-explanatory-reach-through-causal-and-proof.md` to its formalization boundary; it supplies the missing distinction between a routing signal and adequacy relative to a declared model and intended consequence.

## Connections Found

- [A framework rule with a boundary-preserving rival is not an inherited constraint](../../../../notes/a-framework-rule-with-a-boundary-preserving-rival-is-not-inherited.md) -- **grounds**: its one-way rule explains why the existence of a rival paradigm can show that a commitment is contestable without certifying that departures are bounded, subordinate exceptions.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **grounds**: its formalization boundary shows that adequacy is indexed by the intended intervention, counterfactual, proof domain, or other declared use, so sociotechnical pricing can route assessment but cannot settle it alone.
- [Repair dispositions for defeated claims are an epistemic policy with an option space](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- **see-also**: the proposal is the system-design companion that tries to give the source's idealization option an operational verdict and records the adoption risk if the discriminator is too weak.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

None. The two strongest reverse directions already exist: the repair-dispositions proposal and the instantiation/agent-learning note both link to this source.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) -- relevant only to the source's secondary claim about two review episodes establishing a pipeline bias; it does not help a reader assess idealization or exception pricing directly.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- shares boundary language, but its subject is trace-to-lesson generalization rather than model adequacy after a counterexample.
- [The Nature of Theory in Information Systems](../../../sources/the-nature-of-theory-in-information-systems-gregor-2006.md) -- mentions Popper and theory boundaries but does not directly establish the proposed pricing criterion or the conditions under which an idealization survives.
- `kb/agent-memory-systems/` -- no reviewed system makes a domain-pricing or idealization-adequacy claim specific enough to improve traversal from this source.

## Index Membership

- [Failure modes](../../../../tags/failure-modes-README.md) -- the source already carries the `failure-modes` tag and would add the idealization/immunization escape to the curated narrowing and generality pair if the source's final claim survives review.

## Synthesis Opportunities

None. The strongest synthesis surfaced by traversal -- domain marks can route attention while intended-use and adequacy obligations decide -- belongs in the source's own central claim rather than a separate note.

## Maintenance Observations

- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) currently treats the pricing criterion as sufficient to preserve its strong idealization. If this source is weakened or reframed, that inbound premise and its footer summary require substantive review, not just link-text maintenance.
- [Repair dispositions for defeated claims are an epistemic policy with an option space](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) treats the five pricing signatures as the transferable honesty test for a new verdict. Any change to the source's sufficiency claim changes the proposal's adoption criterion and gate design.

## Flags

- Tension: the source lists a rival paradigm as positive pricing evidence, while the one-way rival note establishes that finding a rival can demote or contest a rule but cannot certify the original rule's status.
