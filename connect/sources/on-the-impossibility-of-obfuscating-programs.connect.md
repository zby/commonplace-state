---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: On the (Im)possibility of Obfuscating Programs

**Source:** [On the (Im)possibility of Obfuscating Programs](../../../../sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md)

The source is an immutable snapshot (Barak, Goldreich, Impagliazzo, Rudich, Sahai, Vadhan, Yang; 2010 full version of CRYPTO '01). No tracked `on-the-impossibility-of-obfuscating-programs.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest, which is the authored surface under `kb/sources/COLLECTION.md`. Durable links must target the ingest, never this snapshot.

Source contribution as read for discovery: (1) the virtual-black-box (VBB) definition: an obfuscated program O(P) keeps P's function, and anything efficiently computable from O(P) is computable from oracle access to P; (2) the main result: there are unobfuscatable function families whose source code is efficiently reconstructible from *any* program computing the same function but not from oracle access, so VBB obfuscation is impossible in general (extended to approximate, inefficient and TC0 obfuscators); (3) a scaled-down complexity analogue of Rice's theorem (deciding properties of a function from its circuit description); (4) the definition of indistinguishability obfuscation (Def. 7.1) and the remark that an efficient iO is "as good as" any obfuscator. The KB context that requested the source is the workshop `kb/work/formal-semantics-and-codification/` (opaque-modifier, "deliberate obfuscation" as a third source of opacity); that workshop is an excluded link destination.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels for theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` (theory/definitions), `see-also`. Sources: `compares-with`, `see-also`. External: `derived-from`, `see-also` (not prospected; no external targets supplied).

**Description/title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` filtered by `grep -i -E 'opac|readab|inspect|symbolic|black.?box|codif|formal|semantic|interpret|legib|readable|scale|reference|test|verif|program|form'` -- flagged: opacity-is-a-scale-threshold, representational-form, codification, inspectable-artifact-not-supervision-defeats-the-blackbox-problem, statecharts-and-programs-differ-in-what-they-show-not-compute, verifiability-gradient, the-boundary-of-automation-is-the-boundary-of-verification, traditional-software-can-bracket-executor-conformance-llm-systems, readable-artifact-loop-is-the-tractable-unit-for-continual-learning.
- Descriptions read via `rg -N -m1 '^description:'` for verifiability-gradient, the-boundary-of-automation, readable-artifact-loop, axes-of-artifact-analysis, definitions/codification, reflective-coverage-is-graded-across-representational-forms, code-complements-weight-prompt-with-symbolic-operations, revision-guided-by-rationale-needs-faithfulness-not-just-legibility, information-value-is-observer-relative.

**Topic indexes:**
- No tag heads read in full: the snapshot carries no `tags:`. Candidate tags from the targets (`artifact-analysis`, `learning-theory`) noted for the future ingest under Index Membership.

**Body search:**
- `rg -n -i 'obfuscat|barak|virtual black.box|black-box obfusc|rice.s theorem' kb --glob '*.md' --glob '!kb/sources/.snapshots/**'` -- only hits are in `kb/work/formal-semantics-and-codification/` (sources.md, codification-as-commitment.md, candidate-definitions.md, README.md) plus unrelated code identifiers in oh-my-pi analyses and a Barak co-author citation in sutskevers-list. No library artifact cites the paper yet.
- `rg -n -i "rice'?s theorem|undecidab|halting problem|oracle access|same function|functional(ly)? equivalen|reverse.engineer|source code" kb/theory kb/reference kb/agentic-systems kb/sources` -- no substantive hit; "oracle access" hits in a reference proposal are about answer oracles, not black-box access. Rejected all.
- `rg -n -i 'opaq' kb/theory kb/reference -l` -- 30 files; inspected opacity-relevant lines in axes-of-artifact-analysis (l.39), information-value-is-observer-relative, human-llm-differences (l.43, "opaque to human maintainers", editorial sense, rejected), verifiability-gradient (no hit).
- `rg -l -i 'obfusc|formal semantics|operational semantics|cryptograph|interpretab' kb/sources --glob '*.ingest.md'` -- 10 ingests; checked the-flawed-ephemeral-software-hypothesis (ambiguity vs formal semantics), tarski-truth-and-proof (formalized languages for codification), concept-bottleneck-models (interpretability). None shares an axis tight enough with obfuscation; rejected.
- `rg -l -i 'obfusc|cryptograph|reverse.engineer' kb/agentic-systems kb/agent-memory-systems` -- exo review and oh-my-pi archive only (session-context obfuscator in code, not program obfuscation theory). Rejected.

**Link following:**
- opacity-is-a-scale-threshold -> axes-of-artifact-analysis and inspectable-artifact-not-supervision: the three form an opacity cluster that all state opacity as scale-dependent and readable artifacts as "inherently inspectable at useful scales". The source supplies the counter-case these notes lack: small, symbolic, opaque by construction.
- representational-form -> codification, opacity note: the definition's inspection rule ("test or statically check symbolic artifacts") and misuse case ("opacity ... appears at sufficient scale") are the two sentences the source bears on.
- Workshop `codification-as-commitment.md` l.70 and `candidate-definitions.md` l.31 read for intent only (excluded destination): they state VBB impossibility and iO as bounding the opaque modifier "in both directions".

**Destinations skipped:** reference (no reference doc describes inspection of symbolic artifacts at the level this source addresses); agent-memory-systems and agentic-systems (no shared axis); tags (no source tags to anchor; see Index Membership); external (not a prospecting surface).

## Connections Found

All for the future `kb/sources/on-the-impossibility-of-obfuscating-programs.ingest.md`.

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) -- **is-evidence-for**: the note says any form becomes opaque only "at sufficient scale" and that readable forms stay readable at large aggregates; obfuscation (and the iO definition in §7) gives small symbolic programs that are opaque by construction, so opacity is not monotone in scale. The VBB impossibility bounds this the other way: for unobfuscatable families any equivalent program leaks the source. Bears on the note as a counterexample/qualification, not support.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **is-evidence-for**: the definition's inspection rule says symbolic artifacts are tested or statically checked, and its first misuse case places opacity only at scale. The source shows a symbolic artifact can be transformed so reading yields no more than oracle access (probing), and its scaled-down Rice's-theorem section bears on static checking of functional properties from a description. Also usable as `defined-in` from the ingest when it uses "symbolic"/"distributed-parametric"; prefer `is-evidence-for` as the load-bearing edge.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- **is-evidence-for**: the note claims deterministic code is "inherently inspectable at useful scales" because of its form; obfuscated code is the same form with inspectability removed, which shows inspectability is a property of the particular artifact, not guaranteed by the form.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- **is-evidence-for**: the note lists computational capacity as a determinant of extractable structure and contrasts this with Kolmogorov-style observer-free measures. Obfuscation is the cryptographic formalization of that point: O(P) contains all of P's information, yet an efficient observer extracts no more than from black-box queries.
- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- **compares-with**: shared axis is "function-equivalent representations differ in what a reader can recover". The note treats native vs encoded display of control structure; obfuscation is the limiting case where an equivalence-preserving transformation is chosen to show nothing, and VBB impossibility marks function families where the code cannot be made to show less than any equivalent program.

## Bidirectional Candidates

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) <-> source -- the note would gain a return `evidenced-by` link (qualifies/bounds, not corroborates) once the ingest exists; this is the main revision the workshop's open question 6 asks about.
- [Representational form](../../../../theory/definitions/representational-form.md) <-> source -- the misuse case "opacity ... appears at sufficient scale" would cite the ingest as qualifying evidence if the opaque-modifier wording is promoted.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md`, theory -> sources edges use `evidenced-by` (qualifies or bounds unless a risked test is named), and must target the ingest.

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) → source ingest -- **evidenced-by**: bounds the claim; deliberate obfuscation is a non-scale source of opacity. The note's title claim ("scale threshold, not a class property") would need revision or a scope condition, not just a link.
- [Representational form](../../../../theory/definitions/representational-form.md) → source ingest -- **evidenced-by**: qualifies the inspection rule and the opacity misuse case.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) → source ingest -- **evidenced-by**: qualifies "inherently inspectable" for code.
- [Axes of artifact analysis](../../../../theory/axes-of-artifact-analysis.md) → source ingest -- **evidenced-by**: l.39 repeats the scale-only account of opacity; weaker than the opacity note, author only if the note itself is not revised to carry the point.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Codification](../../../../theory/definitions/codification.md) -- obfuscation preserves function, so the codification test (independent implementations held to one reference) is unaffected; the source bears on inspection, which representational-form owns. Too indirect.
- [Axes of artifact analysis](../../../../theory/axes-of-artifact-analysis.md) -- as an outbound target it duplicates the opacity note it defers to; kept only as a weak reverse-edge candidate.
- [The verifiability gradient](../../../../theory/verifiability-gradient.md) -- about verifiability of artifact types, not about reading vs running; keyword-adjacent only.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- verification cost as automation determinant; no shared mechanism with obfuscation.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- about conformance norms, not inspectability; obfuscation keeps conformance intact.
- [The flawed ephemeral software hypothesis](../../../../sources/the-flawed-ephemeral-software-hypothesis.ingest.md) -- "formal semantics" keyword match; its axis is ambiguity of specification, not hiding of implementation.
- [Concept bottleneck models](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md) -- interpretability of learned models; opposite direction (making parametric content readable) and no shared formal axis worth a `compares-with`.
- [Indistinguishability obfuscation from well-founded assumptions](../../../../sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md) -- the natural `compares-with`/`see-also` companion (constructive counterpart to this impossibility result), but it is only a snapshot with no ingest; durable links may not target snapshots. Re-evaluate once its ingest exists.

## Index Membership

- [artifact-analysis tag head](../../../../tags/artifact-analysis-README.md) -- candidate `tags: [artifact-analysis]` for the future ingest if its analysis centres on the opacity/inspection bearing; check the head's inclusion condition first.

## Synthesis Opportunities

The opacity note, the representational-form misuse case, the inspectable-artifact note and axes-of-artifact-analysis l.39 all state one account: opacity is a scale effect and readable forms are inspectable by default. This source (with the iO paper) implies the higher-order claim the workshop is drafting: opacity has sources other than scale (the reference's form, deliberate obfuscation), so inspectability is a property of an artifact under a consumption path and an observer's resources, not of its form or its size. That synthesis belongs to the workshop's promotion, not to connect.

## Maintenance Observations

- No tracked ingest exists for this snapshot or for `indistinguishability-obfuscation-well-founded-assumptions.md`; the workshop sources list says both are "not yet ingested". Every candidate here is blocked on the ingest.
- Four library artifacts carry the same scale-only opacity account (listed under Synthesis Opportunities); if the workshop promotes the opaque modifier, all four need consistent revision, not only the opacity note.

## Flags

- Tension: the source contradicts the universal reading of [opacity is a scale threshold](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) ("any representation becomes practically opaque at sufficient scale" is fine, but "scale threshold, not a class property" implies scale is the only route). Flagged, not resolved; the workshop's open question 6 owns it.
- Scope caveat for the ingest writer: the paper's results are asymptotic and cryptographic (efficient adversaries, negligible advantage); transferring them to "an agent reading code" is an analogy unless the ingest states which part carries over.
