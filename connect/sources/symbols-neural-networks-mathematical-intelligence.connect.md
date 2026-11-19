---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/symbols-neural-networks-mathematical-intelligence.md"
source_has_frontmatter: true
date: "2026-09-27"
depth: standard
---

# Connection Report: Symbols, neural networks, and mathematical intelligence

**Source:** [Symbols, neural networks, and mathematical intelligence](../../../../sources/.snapshots/symbols-neural-networks-mathematical-intelligence.md)

The source is an immutable snapshot. Every outbound candidate below is for the future tracked ingest `kb/sources/symbols-neural-networks-mathematical-intelligence.ingest.md`, which did not exist when this report was written. No durable link may point at the snapshot itself.

Source claims used for judging candidates:
1. Classical symbol manipulation is learned with effort and is not innate to human cognition.
2. Humans and neural networks therefore gain from using external symbol systems (equations, programs, solvers) as tools. With practice they internalize fallible, graded approximations of those systems.
3. Neural networks are effective across many problems because they learn both regular and irregular structure.
4. Case evidence: DeepMind's 2024 IMO system reasoned inside Lean, with the model guiding tree search over manually formalized problems, and reached silver. The 2025 system reasoned end-to-end in natural language and reached gold. Removing the strict symbolic constraint improved performance. The 2026 Jacobian and unit-distance counterexamples came from general-purpose language models.
5. Formal verification of a result is "irrelevant for the cognitive issues": the intelligence driving a proof is intuition and pattern-seeing, not a symbol system.

## Discovery Trace

**Collection contract:** Read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations are notes, reference (see-also only), sources, agent-memory-systems, agentic-systems, tags, and external. `kb/work/` and `kb/instructions/` are excluded. Labels: `derived-from` (external), `is-evidence-for` (notes, agent-memory-systems), `abstracted-from` (notes), `rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external).

**Title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (421 titles), filtered with `rg -i "symbol|codif|formal|natural.language|bitter|representational|verif|intuition|tool|external|scaffold|oracle|proof|internali|distill|weight|parametric|neural|prose|calcul|compil|exact|stochastic|underspec"`. Flagged: scaling-absorbs-scaffolding, codification-and-relaxing, both bitter-lesson selection notes, code-complements-weight-prompt, unified-calling-conventions, verifiability-gradient, boundary-of-automation, treat-continual-learning-as-representational-form-coevolution, unformalized-improvements pre-formal stage, weight-resident-methodologies, and the codification and representational-form definitions.

**Description listing scan:**
- `rg -N '^description:' kb/sources/*.ingest.md | rg -i "symbol|neural|connectionis|lean|formal|math|proof|bitter|intuition|natural language|verif|analog|olympiad|conjecture|reasoning"`. Flagged: language-models-like-humans (Lampinen is first author), when-is-it-better-to-think-without-words, pattee-physics-of-symbols-2001, FunSearch, prove2me, sutton bitter lesson, lamport 21st-century proof, an-enigma-of-artificial-reason (LRM production/evaluation gap), dario-amodei (verifiable domains get confident timelines), symbolic-learning-enables-self-evolving-agents.
- Descriptions read for the 18 flagged notes to confirm claim, scope, and tags.

**Topic indexes / tag heads:**
- The snapshot carries no `tags:`, so no tag-head pass was run. No tag head was used as a routing surface.

**Body search:**
- `rg -il "connectionis|fodor|systematicity|lean\b|formal verification|neuro-symbolic|neurosymbolic|symbol manipulation|physical symbol"` over notes, sources, reference, agent-memory-systems, agentic-systems. Mostly noise from the word "lean". It surfaced the prove2me review and ingest, and formal-systems-assess-explanatory-reach.
- `rg -n -i "lampinen|infinitefaculty|Jacobian|IMO|olympiad|AlphaProof|Lean\b"`. Only hit on the author: the content-effects ingest. No note yet cites the IMO Lean-versus-natural-language case, so this source would add a new case rather than duplicate one.
- `rg -l -i "internaliz|internalis" kb/notes`. Hits: human-llm-differences, llm-learning-phases, skills-derive-from-methodology, process-structure, underspecification. Only human-llm-differences engages internalization as a design assumption; the others use the word in passing.
- `rg -n -i "external(ized|ised)? (symbol|tool)|symbols? as tools|extended mind|cognitive offload"` over notes and ingests. Hits were agent-harness and context-scheduling material about offloading work to code, not claims about where intelligence resides. The content-effects ingest's "single-system dual-process" point is the closest match.

**Link following:**
- scaling-absorbs-scaffolding. Read the body. Its "Observed at both ends" section has two practitioner cases and says recurrence is "a live hypothesis, not a measured trend". The IMO case is a named fixed-difficulty absorption event across model generations, which is the case type that section lacks. It links to codification-and-relaxing and both bitter-lesson notes, which confirmed that cluster.
- codification-and-relaxing. Read the body. It defines relaxing as replacing a codified component with a general one when scale allows. Lean-guided tree search replaced by end-to-end natural-language reasoning is a clean relaxing instance.
- code-complements-weight-prompt. Read the opening. It separates model-mediated operations from symbolic operations that a runtime executes. Lampinen's "symbol systems as external tools, not the intelligence" is the cognitive-science version of the same split.
- language-models-like-humans ingest. Confirmed that Lampinen and McClelland are authors and that the essay cites the same PNAS Nexus paper for its content-mixing argument.
- pattee-physics-of-symbols ingest. Its Connections section says the source "constrains analogies" in representational form and "should not be used to redefine" codification. That makes it an axis comparison, not support.
- when-is-it-better-to-think-without-words ingest. Karlsson separates wordless exploration from written testing and stabilization, and draws on Hadamard's mathematicians. This closely parallels Lampinen's use of Cohen and Mac Lane.

## Connections Found

- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- **is-evidence-for**: The IMO sequence is a fixed-difficulty absorption case across model generations. Lean formalization plus model-guided tree search (silver) gave way to end-to-end natural-language reasoning (gold). The source is silent on whether frontier work (open conjectures) still externalizes verification. It says solvers "may" have been used but calls that irrelevant to cognition. It therefore bears on the absorption half, and the frontier-recurrence half stays open. The case is secondhand essay reporting, not a controlled comparison: the 2025 system also changed model, training, and compute.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **is-evidence-for**: Moving from Lean-constrained search to free natural-language reasoning is an instance of relaxing. A codified decomposition (every step formally verifiable) was replaced by a general method and gained performance. The source also keeps the symbolic layer as an optional external checker, which fits the note's "hybrid" conclusion.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **compares-with**: shared axis: what scale selects against. Lampinen reads the IMO result as a verdict against symbolic *cognition* (a representational claim). The note says the lesson's axis is production method, not representational form. Following this link helps an ingest writer avoid reading Lampinen as a verdict on symbolic artifacts as such.
- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../notes/code-complements-weight-prompt-with-symbolic-operations.md) -- **compares-with**: shared axis: the role of symbolic operations beside a learned model. Both treat symbol systems as tools a learned system uses, not as its core. Lampinen gives a cognitive and historical (PDP) argument. The note gives an execution-semantics argument about runtime-assigned state transitions.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **compares-with**: shared axis: movement of competence between forms. Lampinen's "external symbols are partially internalized through practice and remain graded" is a symbolic-to-parametric transfer that the note's coevolution framing treats as one of several coupled loops.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- **compares-with**: shared axis: movement between loose natural language and formal artifacts. The IMO case moves reasoning *down* the gradient (from Lean to prose) and improves results. That is the relaxing direction the note says learning can take.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **compares-with**: shared axis: the role of formal verification. Lampinen calls verification irrelevant to *cognition*. The note makes verification cost decide where *automation is warranted*. The claims answer different questions and do not conflict. An ingest should say so explicitly so readers do not treat the essay as counter-evidence.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **compares-with**: shared axis: formal versus informal stages in producing results. Cohen's "forget that all proofs are eventually transcribed in this formal language" and the removal of the Lean-only constraint are mathematical cases of a productive pre-formal stage upstream of a formal gate.
- [Representational form](../../../../notes/definitions/representational-form.md) -- **defined-in**: The ingest analysis will need the KB's symbolic versus distributed-parametric distinction to restate "classical symbol systems" versus "neural network intelligence" without importing Lampinen's cognitive-science vocabulary unmarked.
- [Codification](../../../../notes/definitions/codification.md) -- **defined-in**: The removal of "strict symbolic structure" should be described with the KB's codification term, and the definition bounds what counts as codified (unique operational semantics).
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- **compares-with**: shared axis: human and LLM reasoning as content-sensitive rather than systematic symbol processing. Same first author. The essay cites this paper as its empirical basis for the "both humans and LMs mix content into logic" claim, so the ingest supplies the controlled evidence the essay only summarizes.
- [When is it better to think without words](../../../../sources/when-is-it-better-to-think-without-words.ingest.md) -- **compares-with**: shared axis: informal exploration versus explicit formal or written testing. Both use mathematicians' testimony (Hadamard in Karlsson's case; Cohen and Mac Lane in Lampinen's) to separate generative intuition from later formal checking.
- [Pattee, physics of symbols (2001)](../../../../sources/pattee-physics-of-symbols-2001.ingest.md) -- **compares-with**: shared axis: what a symbol is relative to dynamics. Pattee's epistemic cut treats symbols as rate-independent constraints. Lampinen treats symbols as "inherently subjective and graded" (footnote 1). The contrast limits how far either can be used as the KB's account of symbolic form.
- [Mathematical discoveries from program search with large language models](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md) -- **compares-with**: shared axis: how LLMs reach new mathematical results. FunSearch keeps a fixed symbolic evaluator and program skeleton around a frozen model. Lampinen's cases are general-purpose models without a math-specific scaffold. Together they bracket the scaffold question for math discovery.

## Bidirectional Candidates

None beyond the reverse-edge candidates below. Among the source-side comparisons, the content-effects ingest is the one whose return path would help readers: it could note this later essay by the same author extending its argument to mathematics. That is authored as a sources-to-sources `compares-with` edge.

## Reverse-edge Candidates

Under `kb/notes/COLLECTION.md`, notes may link to sources with `evidenced-by` ("corroborates, qualifies, or bounds"). Notes are limited to five distinct tracked sources each (ADR 082), so check each target's current count first.

- [Scaling absorbs scaffolding at fixed task difficulty, not at the deployment frontier](../../../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) → ingest -- **evidenced-by**: The "Observed at both ends" section could add the IMO Lean-to-natural-language case as a third absorption example. It is the only one of the three that spans model generations at fixed task difficulty. The sentence must record that the comparison also changes the model, training, and compute, so it illustrates absorption rather than isolating it. This is the strongest reverse edge.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) → ingest -- **evidenced-by**: The note's relaxing examples are all from vision and hardware (edge detection, FlashAttention, tokenizers). A formal-reasoning relaxing case would widen its evidence into the domain where codification looks safest.
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) → ingest -- **compares-with** (sources contract): the same author's later extension of the content-effects argument to mathematical reasoning.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- Related, but its axis is claim warrant (asserted versus earned scope). The source says nothing about why the Lean scaffold lost beyond "strict structure constrained the model". The production-methods note is the sharper comparison, and adding both would duplicate it.
- [Unified calling conventions enable bidirectional refactoring between neural and symbolic](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) -- Concerns call-site engineering in llm-do. Lampinen's neural/symbolic movement is cognitive internalization, not component substitution behind an interface. The resemblance is a keyword match only.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) -- "Internalized approximations" is suggestive, but the note concerns cue-activated methodology in context, not learning symbolic skill through practice.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- This note stresses human/LLM *differences* for KB design. Lampinen stresses a *similarity* in reasoning style. The tension is real but indirect: the note concerns statelessness and routing, not reasoning systematicity. A link would mislead more than it helps.
- [Prove2Me ingest](../../../../sources/prove2me-collaborative-math-formalization.ingest.md) and [Prove2Me review](../../../../agentic-systems/reviews-archive/prove2me.md) -- Lean-centred formalization coordination. Lampinen explicitly treats formalization as downstream tooling, so this adds a topic match but no shared axis the ingest would use.
- [Sutton, The Bitter Lesson](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) -- The KB reaches Sutton through the bitter-lesson notes already listed. A direct source-to-source link would be redundant.
- [Lamport, How to write a 21st-century proof](../../../../sources/lamport-how-to-write-a-21st-century-proof.ingest.md) -- Concerns proof *presentation* for checking, not how proofs are found. Only weakly related to the formal-versus-intuitive-discovery axis.
- [An enigma of artificial reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- Relevant to "LRMs solve math but cannot evaluate invalid reasoning". That would qualify Lampinen's dismissal of verification, but the essay makes no evaluation claim to compare against. Reconsider if the ingest analysis turns to verification.
- [Dario Amodei, near the end of the exponential](../../../../sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md) -- Math as a verifiable domain is the only shared point. Too thin.
- [Symbolic learning enables self-evolving agents](../../../../sources/symbolic-learning-enables-self-evolving-agents.ingest.md) -- "Symbolic" there means language-mediated prompt and pipeline artifacts, a different sense of the word. Linking them would confuse readers about the term.

## Index Membership

- No curated index is an obvious home. When the ingest is written, the learning-theory and constraining tag heads (`kb/tags/learning-theory-README.md`, `kb/tags/constraining-README.md`) are the tags to test against their inclusion conditions. The source substantively addresses when symbolic constraint helps or hurts a learned system.

## Synthesis Opportunities

Scaling-absorbs-scaffolding, codification-and-relaxing, and this source together suggest a narrower, testable claim. *Formal-verification scaffolding inside the reasoning loop is absorbable at fixed difficulty, while formal verification outside the loop (checking a finished result) persists.* Lampinen's own framing separates solving (in natural language) from optional external checking. That would split "scaffolding" by its position relative to generation. The claim is only suggested by one essay's reading of announcements and needs better-controlled evidence before it is written.

## Maintenance Observations

- The IMO Lean-to-natural-language transition is a much-discussed scaling case, and no KB artifact cited it before this source. The bitter-lesson cluster relies on vision, hardware, and practitioner-harness cases. A formal-domain case is a gap that this ingest partly fills.

## Flags

- Tension to record in the ingest, not resolve: Lampinen calls formal verification "irrelevant for the cognitive issues", while the KB's verification-boundary cluster treats verification as central. The claims answer different questions (the nature of intelligence versus warrant for automation). The ingest should keep them apart so the essay is not cited as counter-evidence to the verification boundary.
- Evidence strength: the IMO and conjecture cases come secondhand from announcements. The author himself says "we don't know the full details of how these proofs were achieved". Keep `is-evidence-for` edges scoped to illustration, not controlled comparison.
- Not a split candidate: the source makes one connected argument.
