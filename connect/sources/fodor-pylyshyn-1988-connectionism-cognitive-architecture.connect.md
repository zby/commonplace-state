---
description: "Discovery context for ingesting Fodor and Pylyshyn: systematicity, causal representation, architecture levels, and the direct comparison with Lampinen"
type: types/connect-report.md
source: "kb/sources/.snapshots/fodor-pylyshyn-1988-connectionism-cognitive-architecture.md"
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: Connectionism and Cognitive Architecture

**Source:** [Fodor and Pylyshyn, Connectionism and Cognitive Architecture](../../../../sources/.snapshots/fodor-pylyshyn-1988-connectionism-cognitive-architecture.md).

This report supplies discovery context for a fresh ingest. Every recommendation is a candidate for the matching tracked ingest, not an edit to the immutable snapshot. Judgments were produced by the connect worker under `cp-skill-connect/SKILL.md` and `types/connect-report.md`; the source is the complete retained Markdown extraction, including references, read in chunks after larger reads truncated. No external search was used.

## Discovery Trace

**Contract and breadth.** Read the sources and reports collection contracts and the global connect-report type before discovery. Sources author their links through ingests. Prospected notes, reference, agent-memory-systems, agentic-systems, tags, and sources. Instructions and work are excluded. The original PDF URL is the only external candidate; external authorization does not call for web prospecting. The snapshot has frontmatter and no tags, so there is no inherited by-tag search to perform.

**Curated heads.** Read the six destination `README.md` files. Followed the tags hub to computational-model, artifact-analysis, theory-builder, and learning-theory heads. The last three declare `complete: true`; no by-tag sweep was needed. The heads led to representational form, theory builder, action-model consumption, and retained-theory intervention. Agent-memory and agentic-system indexes distinguish actual implementations and their evidence from cognitive metaphors; no reviewed system supplied a sufficiently specific link to this 1988 argument.

**Title and description surfaces.** Generated the fresh full title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'`. Follow-up collection-sized `--no-filename` listings and sorted ranges recovered titles hidden by output truncation. Description discovery used `rg '^description:' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ --glob '*.md' | rg -i 'symbol|parametric|theor|cognit|analogy|brain|representation|compos'`, and `rg '^description:.*(representation|theory|causal|symbol|connection|compos|architecture|learn)' kb/notes/definitions/ kb/notes/*theory* kb/notes/*symbol* kb/sources/*reflection* kb/sources/*thought* --glob '*.md'`.

- **Notes:** Representational form and action-model consumption passed because their distinctions prevent concrete misreadings of the source. Theory builder passed as a bounded comparison with the paper's concluding account of learning as hypothesis construction. The natural-language meaning note passed as the clearest substantive disagreement to inspect. Retained-theory intervention and theory-building precedents were read as one-hop context but add a less direct path than these four.
- **Reference:** Source-adoption policy appeared on the body query below: it restricts programming analogies to the symbolic shell. A direct source-to-policy link would add little beyond the more precise representational-form comparison. Architecture documents and ablation proposals concern shipped choices or experiments the paper does not evaluate; no edge retained.
- **Agent-memory-systems:** Description matches included Cortex, Clude, AgentFly, and trace-learning comparisons. Terms such as cognitive, parametric, and compositional do not establish that these systems instantiate or test the paper's disputed architecture. No edge retained.
- **Agentic-systems:** Description matches included ModularRSI, oh-my-pi, and Company Brain. Their runtime composition, memory representations, and correction paths are different mechanisms from compositional mental representation. No edge retained.
- **Tags:** The heads provided routing rather than a useful outgoing claim link. Sources authorizes scanning tags but gives no source-to-tag formal label. No new label was invented, and no selective index insertion is recommended merely for historical topical overlap.
- **Sources:** The direct Lampinen comparison passed. Craik passed on the named axis of structure-preserving representation versus physical resemblance. Reflection sources were screened at description level, but self-representation is not this paper's subject. Modern compositional-generalization and reasoning studies surfaced in the title scan; they were not used as a retrospective verdict on the paper without a separate architectural comparison.

**Body searches.** `rg -n -i 'Fodor|Pylyshyn|systematicity|constituent structure|language of thought' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'` found the natural-language meaning note's secondhand account and the Lampinen ingest's retained quotation. `rg -n -i 'compositional|systematicity|cognitive architecture|classical architecture' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` found the source-adoption policy and only incidental system matches. `rg -n -i 'symbolic|parametric|hypothesis|brain|representation|theory' kb/agent-memory-systems/README.md kb/agentic-systems/README.md kb/reference/README.md kb/tags/*README.md --glob '*.md'` supplied broader routing context rather than further accepted system links.

**Link following and acceptance.** Read the complete natural-language meaning note and followed its Lampinen link; this establishes a real primary-versus-secondary source opportunity. Followed representational form to its localization/consumption distinctions and the action-model note. Followed the theory-builder head to the definition and the precedents/intervention notes to distinguish causal guidance, criticism, and improved capacity. Read Craik's ingest through its links to the action-model and representational-form cluster. Read the notes collection's outbound rules and note type before recommending a reverse source citation. Candidate paths were checked before report validation.

## Connections Found

- [Symbols, neural networks, and mathematical intelligence](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) — **compares-with**: Lampinen explicitly presents Fodor and Pylyshyn as the opposing position. The primary paper separates systematic competence from perfect performance, permits neural implementations of classical architecture, and does not require explicit rules. These distinctions let a reader assess which premises Lampinen challenges, rather than treating fallible mathematical performance as a direct refutation of the whole argument.
- [Natural-language meaning is coordination among learned approximations](../../../../notes/natural-language-meaning-is-coordination-among-learned-approximations.md) — **compares-with**: the note conjectures that compositionality approximates learned coordination; the paper argues that systematicity requires shared constituents and sufficiently stable semantic contributions. The direct contrast helps specify the empirical burden on the note's hypothesis. Neither text establishes the other's falsity.
- [Representational form](../../../../notes/definitions/representational-form.md) — **compares-with**: the paper distinguishes neural distribution from semantically evaluable constituency and treats classical architecture as a relation between structured representations and structure-sensitive processes. Commonplace instead classifies retained artifacts by localization and assigned consequences. Comparing these definitions prevents importing a verdict about cognitive architecture as a verdict about symbolic artifacts or treating distributed physical realization as absence of addressable content.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) — **is-evidence-for**: Part 2 distinguishes externally assigned node labels from representations whose structure changes the machine's transitions. This is a conceptual comparison that clarifies and bounds the note's causal-use condition: a readable description of a state is insufficient to establish that the represented structure guides action. The paper supplies no experiment testing the note's agent-system claim.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **compares-with**: the conclusion contrasts statistical parameter adjustment with learning by framing hypotheses and evaluating them against evidence. This supplies a historical comparison for Commonplace's distinction between weight adaptation and criticism of stated content. It does not supply Commonplace's four conditions, persistence requirement, or evidence that a deployed system meeting them learns.
- [Craik, Hypothesis on the Nature of Thought](../../../../sources/craik-hypothesis-on-the-nature-of-thought-1943.ingest.md) — **compares-with**: Craik's model preserves relevant relations without pictorial resemblance; Fodor and Pylyshyn specify constituent structure and structure-sensitive operations while rejecting an assumed structural identity between neural implementation and cognitive architecture. Readers can compare what relation preservation requires without equating their different uses of “symbol”.
- [Original paper PDF](https://rodsmith.nz/wp-content/uploads/Pylyshyn_connectionism.pdf) — **derived-from**: this is the original external source carried by the snapshot metadata and the provenance target for the authored ingest.

## Bidirectional Candidates

- [Lampinen ingest](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) → the future Fodor–Pylyshyn ingest — **compares-with**: its current historical summary would gain a primary-source reading of the theory it disputes. Author only after the tracked ingest exists; the reverse link must not target the ignored snapshot.

## Reverse-edge Candidates

- [Natural-language meaning note](../../../../notes/natural-language-meaning-is-coordination-among-learned-approximations.md) → the future Fodor–Pylyshyn ingest — **evidenced-by**: qualify the historical claim in “Meaning sits on the pattern side” with the primary paper, especially its stable-contribution requirement, competence/performance distinction, and acceptance of neural implementation. This use bounds the note's characterization of its rival; it does not corroborate the note's learned-coordination hypothesis. The notes collection authorizes this source label. A later author should retain supporting quotes or request the snapshot under the source-grounding contract.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md) — the paper helps distinguish levels, but does not establish the note's execution-specific claims about present-day LLMs. The representational-form comparison covers the needed distinction more precisely.
- [Theory building has distinct epistemic, structural, and implementation precedents](../../../../notes/theory-building-has-distinct-precedents.md) — the paper's closing hypothesis-construction remark is too brief to establish a further operational precedent for the full theory-builder process. Retain the narrower definition comparison instead.
- [A retained-theory intervention isolates one surface](../../../../notes/retained-theory-intervention-isolates-one-explicit-surface.md) — both texts require causal rather than decorative representations, but this note supplies modern intervention controls not developed by the paper. It is useful reading behind the action-model candidate, not an additional direct edge.

## Index Membership

None. The source is best found through its substantive comparison with the existing Lampinen ingest and meaning note. A generic cognitive-architecture source would not by itself earn a pick in a head about LLM orchestration, retained-artifact classification, or theory-builder operation.

## Synthesis Opportunities

None. The primary/secondary comparison is already concrete enough to improve source use; it does not warrant a new general synthesis from this discovery pass.

## Maintenance Observations

None.

## Flags

- **Historical scope:** “Connectionism” means the paper's reconstructed class of architectures. A claim about current neural language models requires additional evidence about their representations and operations. Do not turn the paper's 1988 limitations claims into a present-day impossibility result.
- **Central dispute:** explain systematicity separately from unbounded productivity. The authors set productivity's idealization aside and argue from linked finite capacities. Also distinguish their claim that a mechanism must explain systematicity from the weaker claim that a network can be constructed to display it.
- **Rule explicitness:** classical structure-sensitive processing does not require every transition rule to be explicitly represented. Part 4 treats data structures, hardwired transitions, and stored programs separately. This matters directly to the Lampinen comparison.
- **Capture limitations:** the extraction includes figure insertion notices, references to Figures 1–3, and terminal Figure 1/2 labels without diagram content. It also contains letter-spaced and OCR-damaged passages. The prose supports the above connections; diagram topology or exact damaged wording requires checking the PDF. Do not claim the Markdown preserves the figures.
- **Source voice:** the polemical critique and its broad empirical claims belong to the authors. The ingest should separate those claims from its own limitations and transfer analysis. The conclusion's learning alternative is a proposal, not a reported implementation or measured learning result.
