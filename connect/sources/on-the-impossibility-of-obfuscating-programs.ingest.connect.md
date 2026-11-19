---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/on-the-impossibility-of-obfuscating-programs.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: On the (Im)possibility of Obfuscating Programs

**Source:** [Ingest: On the (Im)possibility of Obfuscating Programs](../../../../sources/on-the-impossibility-of-obfuscating-programs.ingest.md)

## Discovery Trace

**Collection contract:** read the outbound section of `kb/sources/COLLECTION.md`. Destinations to prospect: theory, reference, agent-memory-systems, agentic-systems, tags, sources; `kb/work/` and `kb/instructions/` are excluded. Authorised labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). The table authorises no label into `kb/tags/`. External prospecting was skipped. The only external target is the already-linked author-hosted PDF.

**Existing footer (already authored, not re-proposed):** derived-from the PDF; is-evidence-for [opacity is a scale threshold](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md), [representational form](../../../../theory/definitions/representational-form.md), [inspectable artifact](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md), [information value is observer-relative](../../../../theory/information-value-is-observer-relative.md); compares-with [statecharts and programs](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md). All five paths exist.

**Topic indexes:**
- `kb/tags/artifact-analysis-README.md` (the source's tag; `complete: true`, so the by-tag rg was skipped). It lists opacity-is-a-scale-threshold and representational-form, both already linked. Sources do not participate in tag membership (`kb/tags/COLLECTION.md` line 46), so the ingest is not a member.

**Body search** (scope: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources kb/tags`, snapshots excluded):
- `rg -il 'obfuscat'` gives 3 hits: this ingest, the sibling [iO ingest](../../../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) (kept), and the oh-my-pi AAS result (rejected: a code identifier `deobfuscateSessionContext`, not the concept).
- `rg -il 'black.?box'` gives about 25 hits. Kept: none beyond the existing links. Checked: `spec-mining-as-codification.md` (rejected, see below), `axes-of-artifact-analysis.md` (the parent scheme, already reachable through representational form).
- `rg -il "Rice'?s theorem|Rice theorem"` matches only this ingest. The reading-versus-running claim has no KB counterpart.
- `rg -il 'opaque|opacity'` hits mostly system reviews that use "opaque" in its everyday sense. The relevant hits are the existing theory links.
- `rg -il 'reading versus running|read.*rather than run|run it'` gave no conceptual matches.
- `rg -il 'learnable from queries|query access|oracle'` hits are about "oracle" in the test-oracle sense, so none were kept.
- `rg -il 'kolmogorov|minimum description|succinct|compression' kb/theory` led to [epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) (kept) and [minimum viable vocabulary](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) (rejected).
- `rg -n -i 'bounded observer|computational(ly)? bounded|polynomial' kb/theory` confirmed the cluster around information value is observer-relative and epiplexity.
- `rg -l -i 'epiplexity' kb/sources --glob '*.ingest.md'` found the [epiplexity paper ingest](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) (kept). Its retained Theorem 9 quote says that CSPRNGs have maximal time-bounded entropy but negligible epiplexity.

**Link following:**
- From the iO ingest: its Recommended Next Action asks for this ingest by name. Its Connections section cites Barak et al. as the place to source "what obfuscation can and cannot hide", but its footer does not link here yet.
- From opacity-is-a-scale-threshold: line 9 makes scale the cause of opacity, and line 11 says readable and opaque are relative to tooling. Representational form, line 50 (misuse case), repeats "opacity ... appears at sufficient scale". Both are reverse-edge targets.
- From information-value-is-observer-relative: it links outward to minimum viable vocabulary and epiplexity. That neighbourhood is where the paper's observer-bounded extraction framing lands.

**Destinations with no plausible match:** reference (system docs; no obfuscation or opacity design), agent-memory-systems, agentic-systems (no system relies on obfuscation or reading-versus-probing guarantees).

## Connections Found

- [Indistinguishability Obfuscation from Well-Founded Assumptions (ingest)](../../../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) -- **compares-with**: same iO definition, different results. This paper defines iO (Definition 7.1) and proves only an inefficient, canonicalizing instance. Jain-Lin-Sahai construct efficient iO under four subexponential assumptions. Any use of iO in the opaque modifier needs both: the definition and its meaning come from this paper, and feasibility comes from the other.
- [From Entropy to Epiplexity (ingest)](../../../../sources/from-entropy-to-epiplexity-rethinking-information-computational.ingest.md) -- **compares-with**: both formalize what a computationally bounded observer can extract from an artifact that contains the information in full. Here, VBB asks the observer to learn nothing beyond oracle access. In the epiplexity paper, a CSPRNG has negligible epiplexity. The unobfuscatable ensemble relies on the same pseudorandomness primitive to keep a hidden string unextractable under oracle access.
- [Epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) -- **compares-with**: its encrypted-message and CSPRNG examples show content whose structure a bounded learner cannot use. Obfuscation is the program-side analogue: a function-preserving transformation chosen so that a bounded reader extracts as little as possible. The impossibility result marks where the analogy breaks: for some programs, structure is recoverable from any equivalent program.

## Bidirectional Candidates

- [Indistinguishability Obfuscation from Well-Founded Assumptions (ingest)](../../../../sources/indistinguishability-obfuscation-well-founded-assumptions.ingest.md) <-> source -- **compares-with**: the iO ingest's Recommended Next Action and Extractable Value item 2 say that statements about what iO and VBB hide must be sourced to Barak et al. The return link lets a reader of the iO ingest reach the paper that actually makes those statements.

## Reverse-edge Candidates

Under theory `COLLECTION.md` rules, `evidenced-by` with a context phrase that says the evidence qualifies or bounds the claim. It is not corroboration, because the claims were not tested against this source.

- [Opacity is a scale threshold, not a class property](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) → source -- **evidenced-by**: this paper bounds the scale-only account. It treats deliberate function-preserving obfuscation as a definable, size-independent goal. It also shows that for some families, every equivalent program leaks the source, so obfuscation is not achievable in general.
- [Representational form](../../../../theory/definitions/representational-form.md) → source -- **evidenced-by**: this paper qualifies the opacity misuse case (line 50) and the "test or statically check symbolic artifacts" inspection rule. Reading can strictly exceed probing for function classes not learnable from queries. The current workshop on formal semantics and the opaque modifier is the likely author of this edit.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) → source -- **evidenced-by** (secondary): code inspectability holds for artifacts that have not been adversarially transformed. The edge is weaker than the two above. Author it only if the note gains a scope sentence about deliberate obfuscation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Spec mining as codification](../../../../theory/spec-mining-as-codification.md) -- it extracts verifiers from observed behaviour, which looks like the paper's "learnable from queries" condition. But spec mining derives rules from stochastic behaviour; it does not recover a program from oracle access. The shared axis would be invented.
- [Minimum viable vocabulary](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) -- it shares the bounded-observer framing but concerns naming as a way to lower extraction cost. It adds nothing beyond the already-linked information-value note.
- [Codification](../../../../theory/definitions/codification.md) -- `defined-in` would only fit if the ingest used "codification". It uses "symbolic form", which is already linked through representational form.
- oh-my-pi AAS result (`kb/agentic-systems/reports/retained-archive/AAS-2026-09-26-oh-my-pi-01/result.md`) -- keyword hit on a code identifier only.

## Index Membership

None. The ingest already carries `tags: [artifact-analysis]` for source-scoped search. Sources are not in the tags participating set, so the complete head should not list it.

## Synthesis Opportunities

The two obfuscation ingests, the epiplexity ingest, and information value is observer-relative together imply a higher-order claim. On this claim, opacity has at least two independent sources: scale, and deliberate observer-bounded transformation. Neither is a property of the form. And for some function classes, the artifact itself guarantees that a reader can recover more than a prober. This is the opaque-modifier question already open in `kb/work/formal-semantics-and-codification`. It should be consumed there, not authored as a new note from connect.

## Maintenance Observations

- Tension: the misuse case in [representational form](../../../../theory/definitions/representational-form.md) (line 50) and the title of [opacity is a scale threshold](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) name scale as the source of opacity in symbolic systems. Two new ingests (this one and the iO ingest) both report a non-scale source. The recent commit "Define symbolic form by closeness to a formal semantics, with opacity as a modifier" suggests revision is under way. The scale note's title is still universal in mode.
- The occasion's quote retention is still pending: the Quotes section reads "No source quotes have been retained yet". Theory notes cannot cite this ingest without counting it as an unquoted source until `cp-skill-ground` runs.

## Flags

- Tension (not resolved here): scale-only opacity in the theory layer versus deliberate-transformation opacity in both obfuscation ingests.
- Any transfer carries the analogy gap that the ingest itself names: probabilistic polynomial-time adversaries versus agents or humans reading finite programs.
