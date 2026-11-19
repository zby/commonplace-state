---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/morgan-the-specification-statement.md"
source_has_frontmatter: true
date: "2026-11-04"
depth: standard
---

# Connection Report: On the Refinement Calculus (Morgan, Robinson, Gardiner, PRG-70, 1988)

**Source:** [On the Refinement Calculus](../../../../sources/.snapshots/morgan-the-specification-statement.md)

The source is an immutable snapshot. No tracked ingest exists yet (`kb/sources/morgan-the-specification-statement.ingest.md` is absent). Every outbound candidate below is meant for that future ingest's `Connections Found` footer. Every reverse-edge candidate points at that future ingest and cannot be authored until it exists.

Source content used for judging: the refinement calculus puts specifications and code in one language ("not all programs are executable"). It defines refinement `P ⊑ Q` as "any specification satisfied by P is satisfied by Q also", so derivation goes from abstract to concrete through laws. Theorem 2 (snapshot ~line 618) states that program constructors are monotonic with respect to refinement: "only this ensures that refining a fragment ... in place in some larger program, refines that larger program overall". The `if ... fi` extension is not monotonic, which "limits its use in program development" (~line 1141). Infeasible specifications ("miracles") refine only to miracles, so a development is "doomed" unless a feasibility test catches them. Miracles can also arise mid-derivation from "mistaken refinement tactics" (~lines 1160-1170). Program conjunction is "the worst program that is better than each member of the family" (~line 4699). Data refinement and the copy rule for procedures are the remaining topics.

## Discovery Trace

**Setup:**
- Source collection `sources`. Read `kb/sources/COLLECTION.md` outbound section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). Authored surface is the ingest; the snapshot never authors links.
- Read the snapshot's contents, introduction, the abstract and introduction of "The specification statement", and the monotonicity, feasibility/miracle and conjunction passages. Did not read the full 156-page OCR text.
- Context only, not a link target (`kb/work/` excluded): `kb/work/invariants-under-composition/README.md`, parked 2026-11-04. Its question about which component properties survive composition, and its distinction between unsettled requirements and violated settled ones, is probably why this source was captured. It shaped the theory search below.

**Titles listing / description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i 'spec|semantic|program|refin|abstract|executab|composition|compos|contract|invariant|verif|oracle|decompos|underspec|calcul|interpret'` -- about 80 titles. Flagged: specification-strategy-should-follow-where-understanding-lives, clear-instructions-can-compose-into-an-unsettled-contract, near-decomposability-may-make-local-inspection-affordable, underspecification-and-indeterminism-complicate-programming-for, symbolic-form-holds-consumers-to-a-semantic-reference, prompting-changes-failure-diagnosis-with-the-semantic-reference, out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec, implementations-do-not-establish-shared-semantics, llm-executed-methodologies-are-metacircular-interpreters, statecharts-and-programs-differ-in-what-they-show-not-compute, verification-needs-a-typed-target-before-it-needs-an-oracle.
- `rg -N '^description:'` on each flagged theory file and on the sibling source ingests listed below.

**Topic indexes:**
- `kb/tags/` listing. Read `computational-model-README.md` and `constraining-README.md` heads. The constraining head led to `kb/theory/definitions/constraining.md`. The source snapshot carries no `tags:`, so no tag rg was run. Source tags do not participate in tag membership.

**Body search:**
- `rg -l -i 'refinement calculus|stepwise refinement|weakest precondition|data refinement|Dijkstra|Carroll Morgan|predicate transformer|wide.spectrum' kb --glob '*.md'` -- 3 hits: is-ai-the-next-layer-of-abstraction.ingest (Dijkstra framing, kept), continual-harness ingest (Dijkstra's shortest-path algorithm, rejected), pageindex archive (irrelevant). The KB has no existing treatment of the refinement calculus.
- `rg -n -i 'refinement' kb/theory kb/reference kb/agentic-systems kb/tags` -- the hits use "refinement" in the editing sense (wikiwiki ladder, automated note refinement, Prime Agent harness refinement). All rejected as keyword-only.
- `rg -l -i 'hoare|design.by.contract|formal (method|verification|specification)|program derivation|correct.by.construction|monoton' kb/theory kb/reference kb/sources kb/agentic-systems kb/tags` -- kept toolgate ingest and program-synthesis ingest. Followed spec-mining-as-codification and implementations-do-not-establish-shared-semantics (both rejected, see below).
- `rg -n -i 'nondetermin|permitted variation|refine|specification|formal'` over five theory candidates -- confirmed that symbolic-form uses "permitted variation", that prompting-changes uses "an unwanted outcome that the instruction permits", and that the underspecification note says "In deterministic code there's no gap between what the code says and what it does".
- `rg -n -i 'monoton' kb/theory` -- no note discusses monotonicity of composition. Hits are spec-mining ("calculator surface grows monotonically") and thresholding monotone transforms, both unrelated senses.
- `rg -l -i 'precondition|postcondition|formal spec|weakest' kb/agentic-systems kb/agent-memory-systems kb/reference` -- swamp, beads-rust, memwiki, voyager, dense-mem and some proposals. Spot-judged by description as tool-level checks, so no candidate.
- `rg -n -i 'precondition|postcondition|hoare|contract'` on the toolgate ingest and `rg -n -i 'specification|intent|deduct'` on the program-synthesis ingest -- confirmed the shared axes used below.

**Link following:**
- near-decomposability note -> its footer (Simon, Grünwald, Scaling Monosemanticity, ROME, addressable-theory). It gave the "locating vs establishing preservation" distinction and the open question on certificate checking.
- clear-instructions note -> symbolic-form, silent-disambiguation, llm-context-is-composed-without-scoping. symbolic-form was kept. The others were rejected as further from the source.
- specification-strategy note -> spec-mining-as-codification and changing-requirements. Rejected as one hop too far.

## Connections Found

For the future ingest `kb/sources/morgan-the-specification-statement.ingest.md`:

- [Near-decomposability may make local inspection affordable](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) -- **is-evidence-for**: the monotonicity theorem states a formal condition under which an in-place replacement provably preserves the whole program's guarantees. The condition is that the replacement refines the fragment's specification and every enclosing constructor is monotonic. This bears on the note's claim that locating a repair point and establishing that a repair preserves required invariants are separate achievements. It also answers the note's open question about whether certificate checking can work without a near-decomposition: specification interfaces replace interaction summaries. In the shared conversion routine example, callers need not be rechecked if they rely only on the routine's specification and the fix refines it. The non-monotonic `if ... fi` shows the condition can fail even inside a formal language.
- [Clear instructions can compose into an unsettled contract](../../../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) -- **compares-with**: shared axis is whether combining requirements is settled. Program conjunction gives combined specifications a defined meaning ("the worst program that is better than each member"). An unsatisfiable combination becomes an infeasible "miracle" that a feasibility test can detect. Natural-language composition can instead leave the combined contract unsettled. The comparison separates settled-but-infeasible from unsettled, which is the distinction the note's scope section leaves open.
- [Constraining](../../../../theory/definitions/constraining.md) -- **compares-with**: shared axis is narrowing permitted behaviors while keeping a reference. A refinement step reduces nondeterminism while preserving every guarantee of its predecessor, so a derivation is a sequence of constraining steps in the codified region with a proof obligation at each step. The calculus adds what the definition does not state: monotonic narrowing of a part narrows the whole. (`defined-in` is also authorised for this destination. Use it instead if the ingest analysis uses the term "constraining" without explaining it.)
- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) -- **compares-with**: shared axis is conformance to a reference that declares permitted variation. Weakest-precondition semantics is a separately authored reference, and the refinement relation defines conformance as preserving every specification the reference satisfies. A deterministic implementation therefore conforms to a nondeterministic specification (the snapshot's ~line 610 example). This is a concrete formal model of the note's distinction between permitted variation and requirement adequacy.
- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -- **compares-with**: shared axis is where multiple valid outcomes live. In the refinement calculus, abstract programs in a formal language admit multiple valid behaviors, and "not all programs are executable". Underspecification is then a first-class semantic object that refinement removes in steps, not something peculiar to natural language. This qualifies the note's statement that deterministic code has no gap between what it says and what it does.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- **compares-with**: shared axis is when and in which artifact disambiguation is committed. The calculus is the formal extreme of spec-first: the specification is written where its implementation will go, and each derivation step is checked. Its "miracles from mistaken refinement tactics" is a precise version of the note's warning that a spec can commit to a projection only execution reveals as unworkable.
- [Ingest: Is AI the next layer of abstraction?](../../../../sources/is-ai-the-next-layer-of-abstraction.ingest.md) -- **compares-with**: shared axis is what makes a translation between layers trustworthy. Seemann requires a well-defined, deterministic translation to the layer below. The refinement calculus relates abstract to concrete through a correctness-preserving relation, not a function: many derivations are valid. It shows that defined meaning does not require a deterministic translation, which sharpens Seemann's two joint requirements.
- [Ingest: Program synthesis (Gulwani, Polozov, Singh 2017)](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) -- **compares-with**: shared axis is how a program is obtained from stated intent. The calculus uses human-directed derivation by laws, while synthesis searches a defined program space. The synthesis ingest's retained quote, that formal specifications for deductive techniques "often appear to the user as complex as writing the program itself", is a cost that applies directly to the refinement calculus.
- [Ingest: ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) -- **compares-with**: shared axis is where pre/postcondition obligations are discharged. ToolGate checks Hoare-style pre- and postconditions at runtime around LLM tool calls. The refinement calculus discharges the same kind of obligation once, at derivation time. Weaker than the candidates above; author only if the ingest discusses runtime versus construction-time checking.
- [Carroll Morgan, Ken Robinson, Paul Gardiner, *On the Refinement Calculus*, PRG-70](https://www.cs.ox.ac.uk/files/3391/PRG70.pdf) -- **derived-from**: the ingest's analysis is worked out from this original (external, already in hand as the snapshot's `source`).

## Bidirectional Candidates

None separately. The useful return paths are theory-side citations of the future ingest, listed under Reverse-edge Candidates.

## Reverse-edge Candidates

These all target the future ingest `kb/sources/morgan-the-specification-statement.ingest.md`, under `kb/theory/COLLECTION.md` rules (theory -> sources allows `evidenced-by`, `abstracted-from`, `derived-from`, `see-also`). Each is authorable only after the ingest exists.

- [Near-decomposability may make local inspection affordable](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) -> ingest -- **evidenced-by** (qualifies/bounds, not corroboration): the monotonicity theorem shows when locating a repair suffices for preserving the whole's guarantees, and the non-monotonic `if ... fi` shows the condition is not automatic. Most valuable reverse edge: it addresses the note's "Finding an intervention point does not establish safe repair" section and its certificate-checking open question.
- [Clear instructions can compose into an unsettled contract](../../../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) -> ingest -- **evidenced-by** (bounds): the note's Scope says it does not claim formal languages have flawless specifications. Program conjunction plus the miracle/feasibility check is a worked formal contrast in which composition is settled even when it is infeasible.
- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -> ingest -- **evidenced-by** (qualifies): it bounds the "deterministic code has no gap" statement, because formal abstract programs can be nondeterministic by design.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Spec mining is codification's operational mechanism](../../../../theory/spec-mining-as-codification.md) -- concerns extracting verifiers from observed behavior. The refinement calculus is the opposite direction (spec to program), and the specification-strategy candidate already covers the contrast.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) -- the wp semantics is an authored reference, but the note's point (implementation-derived formal accounts do not settle intended semantics) is covered more precisely by the symbolic-form candidate.
- [Prompting changes failure diagnosis with the semantic reference](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- its "permitted but unwanted outcome" point is real but more directly served through symbolic-form and the underspecification note. Linking all three would spray.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- the source has no interpreter-failure analogue. Miracles are spec infeasibility, not executor nonconformance.
- [LLM-executed methodologies are metacircular interpreters](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) and [Statecharts and programs differ in what they show](../../../../theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md) -- keyword or PL-adjacent only. The articulation test fails.
- [Ingest: Simon, Architecture of Complexity](../../../../sources/herbert-simon-architecture-of-complexity.ingest.md) -- a source-to-source comparison on local reasoning is real, but it is mediated better through the near-decomposability note, which already joins Simon to the invariant question.
- [Ingest: Efficiently intertwining widening and narrowing](../../../../sources/efficiently-intertwining-widening-narrowing.ingest.md) -- abstract interpretation is formal-methods adjacent, but its precision/termination trade-off shares no named axis with derivation by refinement.
- Wikiwiki refinement ladder, automated note refinement proposal, Prime Agent harness refinement -- "refinement" in the editing sense, so keyword collision only.

## Index Membership

- Optional source tags for the future ingest, conditional on its analysis: `constraining` (if the ingest treats refinement as narrowing permitted behaviors under a reference) and `computational-model` (only if the ingest applies the calculus to LLM-instruction execution, per that head's "merely using" exclusion). Read the heads' inclusion conditions before assigning. Source tags do not affect tag-head membership.

## Synthesis Opportunities

The near-decomposability note (locating vs preserving), the clear-instructions note (unsettled composition) and this source (monotone refinement, conjunction, feasibility) together imply a candidate claim. Local repair is safe exactly when the part has a specification the whole relies on exclusively and the composing operations are monotone with respect to it. Natural-language instruction assemblies usually lack both conditions. This is the parked `invariants-under-composition` question. Per that workshop, do not develop it unless the operator resumes it. If resumed, this source belongs on its reading queue alongside Abadi and Lamport's work.

## Maintenance Observations

- The KB has no prior treatment of formal refinement or of monotonicity as the condition for compositional preservation. The parked `invariants-under-composition` workshop's reading-lead list does not include this source, although it is directly relevant. A workshop maintainer may want to add it; connect does not edit `kb/work/`.

## Flags

- No ingest exists yet. All outbound candidates and reverse edges are blocked until `cp-skill-ingest` produces `kb/sources/morgan-the-specification-statement.ingest.md`.
- Tension to keep visible, not resolve: the underspecification note's claim that deterministic code has no say/do gap conflicts with the calculus treating formal programs as possibly abstract and nondeterministic. The two may be reconciled by scope ("executable deterministic code"), but the note does not currently state that scope.
- Discovery read only selected passages of the 156-page OCR snapshot. Locators are approximate line numbers in an OCR text with errors. Any quote retention should go through `cp-skill-ground`.
