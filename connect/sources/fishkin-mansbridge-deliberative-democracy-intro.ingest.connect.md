---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: Introduction to Deliberative Democracy (Fishkin and Mansbridge, Daedalus 2017)

**Source:** [Ingest: Introduction to Deliberative Democracy (Fishkin and Mansbridge, Daedalus 2017)](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md)

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section read. Prospectable destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for`, `abstracted-from`, `rests-on` (theory; latter two irrelevant, the source is political theory, not a KB claim's origin), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). No label row names `tags`, so tags can only appear under Index Membership. External prospecting skipped (no externally supplied targets). The source carries no `tags:` field, so no tag heads or by-tag listings apply.

**Known links (already in the source):** the ingest links inline to `on-balance-judgments-can-guide-improvement-without-a-global-measure`, `reviewers-share-the-fields-prior-so-interpret-findings-by-stance`, `self-improvement-is-relative-to-a-declared-objective`, `wooldridge-jennings-intelligent-agents.ingest`, and `making-reflective-equilibrium-precise.ingest`. All five resolve. None carries a label (all inline); a labelled footer is absent.

**Titles listing (theory):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` -- 442 titles, filtered with `rg -i "judg|review|divers|consensus|disagree|prior|weigh|reason|argument|objective|legitim|evaluat|oracle|group|multi|crowd|vote|debate|critic|stance|values|trade"`. Flagged: "Error correction works with above-chance oracles and decorrelated checks" (Condorcet aggregation of independent judges, the non-deliberative way of pooling judgments); "Decorrelated reviewers still share the field's prior" (known); "On-balance judgments can guide improvement without a global measure" (known); "Routine approvals do not show that human judgment is dispensable" (rejected below); "Revising an improvement objective is licensed from outside it or is not improvement" (rejected below).
- `ls kb/theory/definitions/` -- no definition of deliberation, weighing or judgment exists; no `defined-in` candidate.

**Description listing (sources):**
- `rg '^description:' kb/sources --glob '*.ingest.md' | rg -i "judg|weigh|reason|argument|deliber|agent architect|equilibrium|explanation-based|debate|consensus|group|social"` -- flagged: `greco-ordinal-regression-revisited.ingest` (comparisons robust across all weightings consistent with judgments), `mustajoki-interval-smart-swing.ingest` (interval trade-off weights), `persona-assigned-llms-motivated-reasoning.ingest` (identity-congruent judgment), plus the two known source links. Greco, Mustajoki and the persona study were evaluated and rejected (below).

**Body search:**
- `rg -n -i "deliberat" kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources --glob '*.md' -l` -- ~55 files, almost all the adverb "deliberately"; noise.
- `rg -n -i "deliberation|deliberative|weighing|weigh competing|mini-public|considered judgment" kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources` -- only the source itself and the on-balance note's "whose costs count" passage (line 65). No other KB artifact uses the group sense of deliberation.
- `rg -n -i "condorcet|wisdom of crowds|jury|social epistem|argumentation|habermas|rawls|reflective equilibrium|practical reason|consensus" kb/theory kb/sources kb/reference kb/tags -l` -- surfaced `error-correction-works-above-chance-oracles-with-decorrelated-checks` (Condorcet), `reviewers-share-the-fields-prior...` (known), `purdue-owl-toulmin-argument.ingest` and `claim-notes-should-use-toulmin-derived-sections...` (argument structure, not group weighing; rejected).
- `rg -n -i "multi-agent debate|\bdebate\b|council|panel of|jury|deference|defer to|legitima|veto|filter bubble|echo chamber" kb/theory kb/agentic-systems/reviews kb/agent-memory-systems/reviews kb/reference` -- surfaced `synthesis-is-not-error-correction` (open question: adversarial debate as a third category, "iterative refinement through disagreement"); `brainstorming-maintainability-oracles-for-agentic-development` (expert veto; rejected).
- `rg -n -i "deliberation|deliberative" kb/reference kb/agentic-systems/reviews kb/agent-memory-systems/reviews` and `rg -n -i "multiple (judges|reviewers)|several judges|judge panel|ensemble of" ...` -- no system review or reference doc implements deliberation among judges; reference, agentic-systems and agent-memory-systems yield no candidates.

**Link following:**
- `reviewers-share-the-fields-prior...` -> `error-correction-works-above-chance-oracles-with-decorrelated-checks` (its `grounds` link) -- confirmed the independence condition the source's random-sample-plus-discussion design sets aside.
- `error-correction...` -> `synthesis-is-not-error-correction` cluster -- the voting / synthesis / debate trichotomy; the source's deliberation is the human-institution case of the third, unexplained category.
- `on-balance-judgments...` line 65 -- "the weighing of whose costs count cannot be checked that way" matches the source's Lafont objection.
- `rg -n -l "greco-ordinal|mustajoki|making-reflective-equilibrium" kb` -- only the source links the reflective-equilibrium ingest; neither Wooldridge-Jennings nor the reflective-equilibrium ingest links back.

### Candidate origins

- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — known, titles, body-search
- kb/theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md — known, titles, body-search
- kb/theory/self-improvement-is-relative-to-a-declared-objective.md — known
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — known, descriptions
- kb/sources/making-reflective-equilibrium-precise.ingest.md — known, descriptions
- kb/theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md — titles, body-search, link-following
- kb/theory/synthesis-is-not-error-correction.md — body-search, link-following

## Connections Found

Existing inline links (confirmed; labels proposed if a labelled footer is added):

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) -- **compares-with**: on the axis "judging by weighed reasons without a global score"; the source supplies the group-level conditions under which weighing is trusted, and Lafont's "blind deference" objection parallels the note's claim that the weighing of whose costs count cannot be checked independently of who weighed. `compares-with` rather than `is-evidence-for`, because the source argues by political analogy and reports no test of the note's claim.
- [Decorrelated reviewers still share the field's prior](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- **compares-with**: on the axis "what a group of judges is for"; a mini-public wants the population's shared prior reproduced, while review gates treat a shared prior as the defect.
- [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- **see-also**: the manufactured-will argument has the structure of a non-antecedent objective; the ingest itself says this is analogy, not evidence, so `see-also` is the honest label.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) -- **compares-with**: on the sense of "deliberative": group weighing of arguments versus a symbolic-world-model agent architecture.
- [Making reflective equilibrium precise](../../../../sources/making-reflective-equilibrium-precise.ingest.md) -- **compares-with**: on how weighing is modelled: a fixed weighted sum versus a discursive process whose conditions decide which arguments are heard.

New candidates:

- [Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- **compares-with**: on the axis "how a group's judgments are pooled". The note's Condorcet route needs independent judges and fails when errors correlate; deliberation deliberately makes participants exchange arguments before judging, giving up independence for argument exposure. A reader drawing on this source for "diverse judges" in Commonplace needs to know which pooling regime its diversity condition serves.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- **compares-with**: on the voting / synthesis / debate trichotomy. The note leaves "iterative refinement through disagreement" as an unexplained third category; the source is the established human-institution form of it, with named conditions (balanced materials, competing experts, diversity, civility) and named failure modes (domination by advantaged participants, like-minded discussion). It does not explain the mechanism either, so the link offers conditions and failure modes, not an answer.

## Bidirectional Candidates

- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: the Wooldridge ingest serves the same draft's "Deliberative agents" bullet; a reader landing there needs the group sense to see that the architectural sense is a different term. Sources -> sources `compares-with` is authorised.
- [Making reflective equilibrium precise](../../../../sources/making-reflective-equilibrium-precise.ingest.md) <-> source -- **compares-with**: a reader of the formal weighing model benefits from the discursive pole; weaker than the Wooldridge return link.

## Reverse-edge Candidates

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) → source -- **evidenced-by** (qualifies, not corroborates): under `kb/theory/COLLECTION.md`, the note's line-65 claim that the weighing of whose costs count cannot be checked independently of who weighed could cite Lafont's deference objection as a bounding parallel from deliberative democracy. The context phrase must say it qualifies the claim and was not a test the claim could have failed. Optional; `see-also` is also authorised theory -> sources if the author judges the parallel too loose for `evidenced-by`.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) → source -- **see-also**: its open question on debate as a third category could point to the human institution that operationalises it. Low priority.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Greco, ordinal regression revisited](../../../../sources/greco-ordinal-regression-revisited.ingest.md) -- formal account of weighing under unresolved trade-offs; the formal pole is already covered by the reflective-equilibrium comparison, and a second formal source adds no distinct axis for this source.
- [Mustajoki, interval SMART/SWING](../../../../sources/mustajoki-interval-smart-swing.ingest.md) -- same reason as Greco.
- [Persona-assigned LLMs show motivated reasoning](../../../../sources/persona-assigned-llms-motivated-reasoning.ingest.md) -- identity-congruent judgment resembles the "like-minded discussion" failure mode only at keyword level; the source treats it in one clause.
- [Routine approvals do not show that human judgment is dispensable](../../../../theory/routine-approvals-do-not-show-that-human-judgment-is-dispensable.md) -- about individual human approval in pipelines, not group weighing.
- [Revising an improvement objective is licensed from outside it](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- the manufactured-will analogy is already carried by the self-improvement link; a second analogy-only link would dilute it.
- [Claim notes should use Toulmin-derived sections](../../../../theory/claim-notes-should-use-toulmin-derived-sections-for-structured.md) -- argument structure for one author; the source's "reasons given" is only a contributor quality measure.
- [Brainstorming: maintainability oracles](../../../../theory/brainstorming-maintainability-oracles-for-agentic-development.md) -- "expert veto" is a keyword hit; the source's veto concern is intense minorities under consensus rules.

## Index Membership

None. No tag head covers deliberation or group judgment, and the source has no `tags:` field; `kb/tags/review-system-README.md` or `kb/tags/evaluation-README.md` would need substantive KB-review content, which the source lacks.

## Synthesis Opportunities

[Error correction works with above-chance oracles and decorrelated checks](../../../../theory/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), [Decorrelated reviewers still share the field's prior](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md), [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) and this source together suggest a claim the ingest's extractable-value item 6 anticipates: what a group of judges is for (error detection, representation, or argument exposure) decides whether independence or a shared prior is a feature or a defect, and which pooling regime (vote, synthesis, deliberation) fits. The source alone states the representation side too briefly; a fuller deliberative-democracy source would be needed before writing it.

## Maintenance Observations

- The only KB-wide body hits for "deliberat" outside this source are the adverb "deliberately"; if the workshop draft adopts "deliberative learning", the [vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) has no record yet distinguishing the group sense (this source) from the architectural sense (Wooldridge and Jennings).

## Flags

- Several connections from the ingest's own inline prose are analogy-only (self-improvement link) or cross-domain parallels (on-balance link); a future labelled footer should keep them at `see-also` / `compares-with`, not `is-evidence-for`.
