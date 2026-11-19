---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/church-turing-thesis-sep.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: The Church-Turing Thesis (SEP, Copeland)

**Source:** [The Church-Turing Thesis](../../../../sources/.snapshots/church-turing-thesis-sep.md)

The source is an immutable snapshot. Under `kb/sources/COLLECTION.md`, the authored outbound surface is the matching ingest, `kb/sources/church-turing-thesis-sep.ingest.md`. That ingest **does not exist yet** at report time. Every candidate under Connections Found is meant for that future ingest; nothing should link to the snapshot.

**What the source contributes (as read for linking):** (1) a four-condition definition of an *effective* (systematic, mechanical) method: finite exact instructions, finite steps if carried out without error, executable by an unaided human with paper and pencil, and requiring "no insight, intuition, or ingenuity"; (2) the thesis that formally replaces that informal predicate with Turing-machine computability, together with the converse that a Turing-machine program is itself an effective method; (3) Copeland's argument that the 1936 thesis concerns *human* rote computation ("human clerical labour, working to fixed rules, and without understanding", Turing 1945), not the limits of machines (Gandy's Thesis M, the maximality thesis, and the "equivalence fallacy"); (4) a warning that the technical terms "computable" and "mechanical" differ from their everyday senses; (5) later "versions" (algorithmic, Extended/complexity, brain-simulation, physical) that are at best distant relatives of the original thesis.

## Discovery Trace

**Setup:**
- `kb/sources/COLLECTION.md` outbound section read. Destinations to scan: theory, reference, agent-memory-systems, agentic-systems, tags, other sources. Excluded: `kb/work/`, `kb/instructions/`. Authorised labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external).
- External: the source URL `https://plato.stanford.edu/entries/church-turing/` is already in hand and is the `derived-from` target for the ingest. No open-web prospecting.
- Motivation found by search: `kb/work/operationalization-executability-automation/exploration.md` lists the SEP entry in its source-availability table ("Pencil-and-paper effective methods vs broad judgment-laden execution"; "Ingest only if needed; remember SEP is secondary scholarship") and uses a "human algorithm counterexample" (long division as an effective procedure). This explains why the snapshot was captured. The workshop is an excluded link destination, so it appears only in Flags.

**Curated heads read:**
- `kb/tags/method-guided-action-README.md` (`complete: true`): surfaced methodological/computational closure, fix-what-the-executor-can't-determine, two-layer execution, and the actionable-methodology definition.
- `kb/tags/computational-model-README.md`: surfaced agentic-systems-interpret-underspecified-instructions and statecharts-vs-programs.
- The snapshot has no `tags:` (snapshots do not carry tags), so there was no by-tag rg.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles), filtered with `rg -i 'execut|procedur|mechani|determin|codif|constrain|closure|interpret|program|natural language|spec|actionable|method|judgment|underspec|algorithm|computation|automat|oracle|rote|insight|formal'`. About 95 hits; descriptions were pulled for the 21 most plausible.

**Body search:**
- `rg -l -i 'church-turing|turing machine|effective method|church.s thesis|turing' kb --glob '*.md'`: almost all hits were the substring "turing" inside "structuring/capturing/manufacturing". There is no real Church-Turing discussion anywhere outside the workshop.
- `rg -l -i 'effective (procedure|method)|church.turing|entscheidung|human computer|without understanding|rule of thumb' agentic-systems agent-memory-systems reference sources tags theory`: three incidental hits (a "rule of thumb" phrase in first-principles-reasoning, a quality-signals note, a reference proposal). All rejected as keyword-only.
- `rg -n -i 'insight|ingenuity|without understanding|rote|mechanical|effective (method|procedure)|algorithm' kb/theory`: surfaced the mechanical/judgment-dependent split in the two-layer execution note and commitment-not-derivation. These are adjacent but not tied to the source's mechanism.
- `rg -l -i 'church|effective procedure|effective method|mechanical procedure|rote|without (insight|understanding|ingenuity)' kb/work`: confirmed that the operationalization workshop is the consuming context.
- `rg -n -i 'rule|formal|criteria' kb/sources/programming-as-theory-building.ingest.md`: confirmed that Naur's quotes on "formal symbol manipulation" and inexpressible criteria are retained there.
- `rg -n -i 'equivalen|turing|expressive|comput' kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md`: equal-computational-power argument, evaluated below.

**Candidates evaluated (descriptions and body read):**
- naur-equates-machine-execution-with-formulated-criteria: body read in full. Premise 2 of its reconstructed bridge ("a computer can make a judgment only by executing such criteria") is exactly the identification that Copeland separates (effective-method computability versus what machines can generate). Kept.
- methodological-and-computational-closure: body read. Its four-way table maps onto the effective-method conditions. Kept.
- actionable-methodology (definition): body read. Effective-method condition 3 names an operator and the operations available to it, so this is the classical operator-relative case. Kept.
- codification (definition): body read. The CT converse ("a Turing machine program is itself a specification of an effective method") cuts across the definition's prose-vs-symbolic boundary. Kept; tension flagged.
- agentic-systems-interpret-underspecified-instructions and traditional-software-can-bracket-executor-conformance: openings read. Effective-method conditions 4 (no insight) and 2 ("carried out without error") are the classical forms of zero underspecification and bracketed executor conformance. Both kept.
- fix-what-the-executor-cant-determine: description read. The effective method is the limiting case where the author fixes everything. Kept.
- Other sources: programming-as-theory-building (kept), competence-theory (kept), Parasuraman automation levels (rejected).

**Link following:**
- naur note → programming-as-theory-building ingest → its ingest-side link back to the naur note. Confirms a three-node cluster that the CT ingest should join.
- methodological-and-computational-closure → reflective-system and computationally-directed-self-improvement. Neither is relevant to effective methods.
- workshop README → actionable-methodology, closure, constraining, codification, behavioral-authority. This confirms that the workshop treats the same targets as the vocabulary to reuse.

**Destinations with no candidates:** agent-memory-systems, agentic-systems, reference. Scoped rg found no effective-method or computability content, and the source has no system or reference-design trigger. Tags: no tag head is a link target for an ingest beyond optional `tags:`; see Index Membership.

## Connections Found

All of these are for the future `church-turing-thesis-sep.ingest.md`, not the snapshot.

- `https://plato.stanford.edu/entries/church-turing/` (external) -- **derived-from**: the ingest's analysis is worked out from Copeland's SEP entry. The ingest should also record that this is secondary scholarship, not Turing's or Church's original text, which matches the workshop's caution.
- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- **is-evidence-for**: Copeland documents that "computation" in the 1936 sense means human rote execution of fixed rules "without understanding". He also argues that this thesis says nothing about what machines in general can generate (Thesis M, the maximality thesis, the "equivalence fallacy"). Both points bear directly on the note's claim that premise 2 of Naur's bridge, which equates formal execution with executing supplied criteria, is an extra premise. The classical concept fits that premise. The CT thesis itself does not extend it to all computational systems.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- **compares-with** (axis: what the retained method settles vs. who or what supplies decisions): an effective method is a fully methodologically closed procedure, since condition 4 requires that no insight be needed. The thesis says such procedures are exactly the ones computation can close. The note's "unattended agent using judgment" row is exactly what the effective-method concept excludes, so the source sharpens the boundary between the note's "yes/yes" row and its "no/yes" row.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **compares-with** (axis: executor-relative executability): the four effectiveness conditions name an operator (an unaided human), its available operations (paper and pencil), and a fidelity requirement (no insight). This makes the effective method the classical historical instance of an operator-relative "can be carried out" predicate. It is also narrower: it excludes judgment entirely, whereas actionability admits judgment-heavy operators. If the ingest uses "actionable" in the technical sense, `defined-in` also applies.
- [Codification](../../../../theory/definitions/codification.md) -- **compares-with** (axis: what makes a rule's consequences fixed rather than interpreter-dependent): the CT thesis and its converse say that any procedure an unaided human can follow without insight corresponds to a Turing-machine program. Codification draws its line at a symbolic artifact with unique operational semantics, and excludes precise prose. The source shows a prose method that needs no insight from its executor, which sits right next to that boundary. See Flags.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **compares-with** (axis: whether instructions leave interpretation to the executor): effectiveness condition 4 is the classical requirement of zero semantic underspecification for the executor. The note's starting point, that LLM instructions are underspecified by design, is the deliberate abandonment of that condition. The source gives the ingest a precise name for the contrast.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- **compares-with** (axis: executor-conformance norm): condition 2 ("will, if carried out without error, produce the desired result") builds the conformance bracket into the definition of an effective method. The source thus shows the bracket at its origin in human rote computation, before any CPU or compiler existed.
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) -- **compares-with** (axis: what formal, rule-following execution can and cannot do): Naur argues that program-theory judgments cannot be reduced to rules and are therefore outside "formal symbol manipulation". Turing's own characterisation of his machines ("fixed rules, and without understanding") is the concept Naur's argument presupposes. Copeland's Thesis M distinction marks where that presupposition stops.
- [Competence theory and problem-solving method construction](../../../../sources/competence-theory-problem-solving-method-construction.ingest.md) -- **compares-with** (axis: refining a method until an executor can carry it out): Wielinga et al. trace the commitments added when competence is refined into an operational method. The effective-method definition is the endpoint where refinement has removed every call on executor insight. Together they bracket the range the operationalization question spans.

## Bidirectional Candidates

- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) <-> source -- **is-evidence-for** / theory-side `evidenced-by`: the note could cite the CT ingest where it discusses the bridge's second premise. The context phrase should say the source qualifies or bounds the premise (classical computation = rote rule-execution; the thesis does not cover machines in general), not that it corroborates. This follows theory's "Origin is not corroboration" rule.

## Reverse-edge Candidates

- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) → source -- **evidenced-by** (theory label): the "settled criterion, executed by computation" row could cite the effective-method definition as its classical bound. Use it only if the note adopts that framing; the context phrase should say "bounds", not "corroborates".
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) → source -- **compares-with** (sources label): the Naur ingest could carry a return link on the axis "what rule-following execution means". This is optional; the forward edge from the CT ingest suffices.

## Off-authorisation Candidates

- [Operationalization, executability, automation, and autonomy — exploration](../../../../work/operationalization-executability-automation/exploration.md) -- the source was captured for this workshop's "human algorithm counterexample" and source table. The sources contract excludes `kb/work/` as a destination, so reject the edge from the ingest side. The workshop may author `evidenced-by` to the ingest under the work contract (sources is an authorised work destination). That is a reverse edge for the workshop owner, not a link from the ingest.

## Raw Text Candidates

None

## Rejected Candidates

- [Statecharts and programs differ in what they show, not in what they can compute](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- shares the theme "equal computational power doesn't settle the practical question", but its equivalence is between practical representations on finite machines. Copeland's equivalence fallacy concerns analyses of human effectiveness versus machine limits. An agent following the link gains little.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../theory/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- the CT thesis is a famous informal-to-formal replacement whose bridge is a thesis, not a theorem, which superficially fits "pre-formal stage". The note, however, is about improvement loops and their admitted languages, and the source says nothing about loops. Too analogical.
- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md) -- Turing's "programming the universal machine replaces engineering" remark is adjacent, but the note's distinction (model interpretation vs runtime-assigned execution) gets no new mechanism from the source.
- [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- an interpreter analogy, but the source has nothing on interpretation strategies.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- the effective method is the degenerate "fix everything" case. That is true but too obvious to help traversal, and the closure and underspecification edges already carry the contrast.
- [Model types and levels of human interaction with automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- function-allocation levels share the workshop context but not a mechanism with effective computability.
- [First-principles reasoning selects for explanatory reach](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- keyword-only hit ("rule of thumb").

## Index Membership

- [method-guided-action tag](../../../../tags/method-guided-action-README.md) -- optional `tags: [method-guided-action]` on the ingest, if the analysis substantively treats the effective-method conditions as the limit where a method settles every decision. Sources stay outside tag membership listings, so this is search scoping only. Read the head's inclusion condition first.
- [computational-model tag](../../../../tags/computational-model-README.md) -- weaker fit. The head's subject is how LLM-based programs execute. Use it only if the ingest explicitly contrasts effective computation with LLM instruction interpretation.

## Synthesis Opportunities

Naur's bridge premise (formal execution = executing supplied criteria), the codification boundary (symbolic artifact with unique semantics), and the closure note (computational closure without explicit criteria) together suggest a higher-order claim. "Mechanical" or "computable" in the classical CT sense names a property of the *method relative to a no-insight executor*, while computational closure names a property of *who supplies decisions*. LLM execution is the case that pulls these apart, because computation supplies decisions that no effective method settled. This is a candidate for the operationalization workshop's extraction decision, not for connect.

## Maintenance Observations

- The workshop's source table records the SEP entry as "No matching ingest" with "Ingest only if needed". Once the ingest lands, that row is stale. Whoever owns the workshop should update it; connect does not edit it.
- There is a possible contract tension in [codification](../../../../theory/definitions/codification.md). The definition excludes precise natural-language rules, yet CT treats a natural-language procedure that needs no insight as equivalent to a Turing-machine program. The definition's real criterion seems to be "a consumer that does not reinterpret", not the artifact's notation. Worth checking whether the definition's Exclusions already handle a human rote-executor, or should.

## Flags

- **Ingest missing:** `kb/sources/church-turing-thesis-sep.ingest.md` does not exist at report time. All Connections Found are destined for it. Re-run or re-check after the ingest is written, since the ingest's actual emphasis may favour some candidates over others.
- **Secondary source:** the SEP entry is scholarship about Turing and Church. An ingest cited for what Turing claimed should keep that caveat, and quotes attributed to Turing come via Copeland.
- **Tension (unresolved):** codification's notation-based boundary vs. CT's executor-based notion of "mechanical"; see Maintenance Observations.
- No split candidate: the snapshot makes one main contribution, the scope of the original thesis versus its later relatives.
