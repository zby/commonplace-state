---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Indistinguishability Obfuscation from Well-Founded Assumptions

**Source:** [Indistinguishability Obfuscation from Well-Founded Assumptions](../../../../sources/.snapshots/indistinguishability-obfuscation-well-founded-assumptions.md)

The source is an immutable snapshot (Jain, Lin and Sahai, arXiv 2008.09317). No matching `kb/sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md` exists yet, so every outbound candidate below is for the future ingest report, which is the authored surface under `kb/sources/COLLECTION.md`. The report is useful only after that ingest is written.

## Discovery Trace

**Source read:** frontmatter, abstract, Theorem 1.1 and section 1.1 (lines 1-260 of 2499). Claim: iO for all polynomial-size circuits exists assuming subexponential hardness of SXDH, LWE, LPN and an NC0 Boolean PRG; all four are well-studied assumptions introduced for other primitives, unlike earlier iO candidates whose bespoke assumptions were repeatedly broken. Polynomial hardness also yields collusion-resistant public-key functional encryption. KB relevance: the KB has no cryptography scope; the only bridge is the opacity modifier on symbolic form under development in the `formal-semantics-and-codification` workshop.

**Collection rules:** `kb/sources/COLLECTION.md` "Outbound links" section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels per destination read from the labels table.

**Body search:**
- `rg -l -i "obfuscat|indistinguishab|virtual black.?box" kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/reports/cache/**'` -- hits outside `kb/work/` are unrelated senses (session-context obfuscation in oh-my-pi analyses, "obfuscate" in ordinary prose). The relevant hits are all in `kb/work/formal-semantics-and-codification/` (`sources.md:24` lists this paper "for the opaque modifier ... not yet ingested"; `codification-as-commitment.md:70` "Deliberate obfuscation" paragraph; `candidate-definitions.md:31,77`). Workshop is an excluded destination; used only to find the library targets it points at.
- `rg -l -i "opaque|opacity" kb/theory kb/reference kb/tags kb/sources` -- ~40 files; filtered by title/description to `kb/theory/opacity-is-a-scale-threshold.md`, `kb/theory/definitions/representational-form.md`, `kb/theory/axes-of-artifact-analysis.md`, `kb/theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`, `kb/tags/artifact-analysis-README.md`.
- `rg -n -i "opaque|opacity|symbolic" kb/theory/definitions/representational-form.md` -- line 50 misuse case ("opacity ... appears at sufficient scale in natural-language and symbolic systems too") and line 64 link to the opacity note.
- `rg -n -i "sources" kb/theory/COLLECTION.md` -- theory may author `evidenced-by` ("corroborates, qualifies, or bounds") into sources; used for reverse-edge candidates.

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md' | rg -i "readab|inspect|opaq|opacity|black.?box|symbolic|legib|hidden|reading|interpretab"` -- 15 titles; kept opacity note and inspectable-artifact note; rejected the symbolic-program/select-call and code-complements notes (symbolic execution, not readability of symbolic artifacts), readable-artifact loop (continual learning; no adversarial-readability axis), rationale legibility (different object).

**Topic indexes:**
- `kb/tags/artifact-analysis-README.md` -- line 17 lists the opacity note; confirms the cluster. No crypto or security tag exists (`ls kb/tags | rg -i "artifact|security|crypt"`).

**Link following:**
- Opacity note -> axes-of-artifact-analysis and inspectable-artifact note (its two Relevant Notes). Representational-form definition -> opacity note (contrasts). The cluster is three theory notes plus one definition; the source joins at the opacity note.

**External:** `derived-from` external authorised; target already in hand (snapshot `source` URL). No web prospecting.

## Connections Found

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) -- **is-evidence-for**: the source bears materially on the claim's scope. The note makes opacity a function of scale; iO from standard assumptions gives a small symbolic program that is opaque by construction (reading it yields no more than any equal-size functionally equivalent program would), so opacity is not monotone in scale. The bearing is disconfirming or bounding, not supportive; see Maintenance Observations on the label.
- [Representational form](../../../../theory/definitions/representational-form.md) -- **defined-in**: an ingest that reads the paper for the KB's purposes must say an obfuscated circuit stays *symbolic* (its consequences fixed by a reference) while becoming *opaque*; a reader needs the form definition and its misuse case against treating opacity as a form (line 50).
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- **is-evidence-for**: the note relies on code being an inspectable artifact; iO shows code can be transformed to defeat inspection while computing the same function, which bounds the claim to artifacts not adversarially transformed. Secondary; author only if the ingest discusses the inspection-by-reading consequence.
- [arXiv 2008.09317](https://arxiv.org/abs/2008.09317) -- **derived-from**: the ingest's analysis is worked out from this paper.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) -> future ingest -- **evidenced-by** (theory label, "qualifies, or bounds"): the note currently names only scale as an opacity source; if the workshop's three-source account is promoted, the note should cite this ingest for the deliberate-obfuscation source.
- [Representational form](../../../../theory/definitions/representational-form.md) -> future ingest -- **evidenced-by**: only if the candidate opaque-modifier text in `kb/work/formal-semantics-and-codification/candidate-definitions.md` is adopted, since that text names deliberate obfuscation as a source.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Axes of artifact analysis](../../../../theory/axes-of-artifact-analysis.md) -- line 39 redefines "opaque" as practical inspectability; it adds nothing the opacity note does not, and linking both would duplicate the route.
- [Code complements the weight-prompt pair with independently executed symbolic operations](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md) -- about symbolic execution, not readability of symbolic artifacts; keyword match only.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../theory/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- presupposes non-adversarial artifacts; the obfuscation result does not bear on the learning-loop claim.
- [Revision guided by rationale needs faithfulness, not just legibility](../../../../theory/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) -- concerns rationale text, not program opacity.
- oh-my-pi analyses (`kb/agentic-system-analyses/retained/can1357--oh-my-pi/boundary.md`, archived AAS result) -- "obfuscator" there is session-context redaction, a different sense.

## Index Membership

- [artifact-analysis tag](../../../../tags/artifact-analysis-README.md) -- tags apply to ingests only if the ingest substantively treats artifact inspectability; check the tag's inclusion condition when writing the ingest.

## Synthesis Opportunities

This source together with the sibling snapshot `kb/sources/.snapshots/on-the-impossibility-of-obfuscating-programs.md` (Barak et al.), the opacity note and the representational-form definition implies the workshop's claim: opacity has a deliberate-obfuscation source independent of scale, bounded from both sides (iO achievable; virtual black-box impossible for some families). This synthesis is already being developed in `kb/work/formal-semantics-and-codification/codification-as-commitment.md`; do not create a separate note.

## Maintenance Observations

- Label gap: `kb/sources/COLLECTION.md` authorises only `is-evidence-for` for a source that bears on a theory claim, and its name reads as support. Here the source bounds or partly disconfirms the target (non-monotone opacity). The reader-need text ("bears materially ... without asserting that the target has incorporated it") covers it, but the label name may mislead; the theory side's `evidenced-by` explicitly includes "qualifies, or bounds". Consider whether the sources table should say so too.
- No ingest exists for this snapshot or for the sibling Barak snapshot; the workshop `sources.md` still says both are "not yet ingested" and "claims from memory".

## Flags

- Once the Barak et al. snapshot is ingested, the two ingests are a natural **compares-with** pair (sources -> sources) on the axis "what obfuscation can and cannot hide": iO achievable from standard assumptions versus impossibility of virtual black-box obfuscation. Not listed under Connections Found because no ingest target exists yet.
- The KB has no cryptography scope; the source earns links only through the opacity modifier. Keep the ingest's analysis narrow to that bearing, per the KB scope in AGENTS.md.
