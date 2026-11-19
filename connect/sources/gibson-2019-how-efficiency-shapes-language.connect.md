---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/gibson-2019-how-efficiency-shapes-language.md"
source_has_frontmatter: true
date: "2026-10-26"
depth: standard
---

# Connection Report: How Efficiency Shapes Human Language

**Source:** [How Efficiency Shapes Human Language](../../../../sources/.snapshots/gibson-2019-how-efficiency-shapes-language.md)

The source is an immutable snapshot. Under `kb/sources/COLLECTION.md`, the snapshot never authors links and no durable link may point at it. Every outbound candidate below is a recommendation for the matching tracked ingest, `kb/sources/gibson-2019-how-efficiency-shapes-language.ingest.md`. That ingest did not exist when this report was written.

Source reading (claims used for judging candidates). Gibson et al. (2019) review information-theoretic evidence that pressure for efficient communication, balanced against learnability and complexity, shapes language from the lexicon to syntax. The load-bearing mechanisms for this KB are:

1. Ambiguity out of context is efficient. Context resolves communicatively relevant ambiguity, and conversation partners can cheaply ask for clarification. Leaving out context-inferable information makes speech more concise. Legal contracts and programming languages are given as zero-ambiguity registers that become wordy.
2. Optimal signal length depends on predictability in context, not raw frequency.
3. Lexicons sit near an informativeness–complexity Pareto frontier.
4. Dependency locality and information locality: related words, or more generally words with high mutual information, should sit close together because comprehenders have noisy, bounded memory.
5. Word order and morphology are alternative encodings of one latent dependency tree, and they trade off. Redundant marking acts like parity bits that make the signal robust to noise.
6. Compositionality may arise from a cultural-transmission bottleneck: a non-compositional system cannot survive input sparsity across generations.
7. Stated challenges: specifying counterfactual baselines is often the hardest part of an efficiency claim. Information theory idealizes communication, so the processor's limits on computing expectations must constrain the theory.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags (scan only, no label), other sources, external. Excluded: `kb/work/` and `kb/instructions/`. Labels: `derived-from` (external); `is-evidence-for` (theory, agent-memory-systems); `abstracted-from`, `rests-on` (theory); `compares-with` (theory, sources, agent-memory-systems, agentic-systems); `defined-in` (theory/definitions); `see-also` (sparingly). The snapshot is never the link author, so all edges target the future ingest.

**Description listing scan:**
- Theory: generated the full claim-title listing with `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (427 titles). Filtered it with `grep -i -E 'ambigu|context|compress|redundan|concise|brev|informat|predict|learn|complex|composit|baseline|counterfactual|tradeoff|trade-off|writ|prose|sentence|word|language|vocabul|term|code|noise|robust|specif|underspec|efficien|channel|reader|natural language'`. Then I read the `description:` and `tags:` of 20 flagged notes: writing-styles, legal-drafting, natural-language-meaning, information-value, epiplexity-by-example, minimum-viable-vocabulary, fix-what-the-executor, silent-disambiguation, agentic-systems-interpret-underspecified, reverse-compression, human-writing-structures, local-materialization, link-strength, three-simplification-passes, two-rewrites, underspecification-and-indeterminism, changing-requirements, vocabulary-collisions, warranted-reader-update, instruction-specificity, an-experiment-identifies-only-the-contrast.
- Sources: ran `rg -l -i 'zipf|surprisal|shannon|psycholinguist|iterated learning|compositional|uniform information density|rate.distortion|noisy.channel|information bottleneck|kinship|color term|linguistic' kb/sources --glob '*.ingest.md'` (about 40 hits). I read the descriptions of fodor-pylyshyn, symbols-neural-networks (Lampinen), smolensky, when-is-it-better-to-think-without-words, mesa-optimizers-and-language-recursion, driven-by-compression-progress, borretti, and semantic-leakage.
- Reference, agentic-systems, agent-memory-systems: ran `rg -l -i 'ambiguit|information theor|zipf|surprisal' kb/reference kb/agentic-systems kb/agent-memory-systems --glob '*.md'`, excluding adr/ and reports/. The hits were proposals and system reviews that use "ambiguity" in an operational sense. None bears on linguistic efficiency, so these destinations were skipped. `kb/agent-memory-systems/` is also historical and frozen.

**Topic indexes:**
- `kb/sources/README.md`: a collection landing with no topical index of ingests.
- Tag heads: the snapshot carries no `tags:`. `kb/tags/COLLECTION.md` lists participating collections as `[theory, reference, instructions, agent-memory-systems, agentic-systems, reports]`. Sources do not participate, so there is no tag membership. `kb/tags/learning-theory-README.md` declares `complete: true`; I read its scope, but no by-tag rg was needed.

**Body search:**
- `rg -l -i 'gibson|futrell|dependency locality|dependency-locality' kb --glob '*.md'` (excluding snapshots): only `kb/sources/gavel-graph-world-models.ingest.md`, an incidental name match, so rejected. The KB has no prior treatment of this literature. Two companion snapshots exist without ingests: `gibson-dependency-locality-theory.md` and `futrell-levy-gibson-dependency-locality.md`.
- `rg -n -i 'locality|dependency length|next to (its|their) claim' kb/theory kb/reference kb/agentic-systems kb/tags kb/sources --glob '*.md'`: the hits use locality in the code, change or retention sense (ModularRSI, metaobject protocols, directory placement). The only "dependency length" hit is in the Sutskever list, about neural architectures. No theory note covers linguistic locality as a reading-cost mechanism.
- `rg -n -i 'pareto|redundan(cy|t) .*robust|parity|clarif(y|ication) (question|request)|ask (the user|for clarification)|interactive repair' kb/theory`: this surfaced `design-for-the-first-time-human-except-on-access-cost.md:63`, which says an agent may resolve an underspecified instruction where a maintainer would ask for clarification. It is a one-line aside, so I rejected it as a target but used it to support the silent-disambiguation axis.
- I read the bodies of legal-drafting, minimum-viable-vocabulary, two-rewrites, natural-language-meaning, agentic-systems-interpret-underspecified, fix-what-the-executor, information-value, silent-disambiguation, reverse-compression, instruction-specificity and an-experiment-identifies-only-the-contrast (first 10–45 non-blank lines each).
- `rg -n -i 'gibson|compositional' kb/sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md`: line 57 says the meaning note's claim that compositionality emerges under communication pressure "must explain the linked capacities and semantic stability at issue; naming approximation does not yet supply that mechanism". Gibson's transmission-bottleneck account is a candidate supply for that gap, which is why both the Fodor–Pylyshyn ingest and the meaning note were kept.

**Link following:**
- natural-language-meaning → fodor-pylyshyn ingest, smolensky ingest, Lampinen ingest, vocabulary-collisions. This confirmed the open compositionality-mechanism gap. Smolensky and Lampinen were rejected because their axis is representation, not language evolution.
- legal-drafting → agentic-systems-interpret-underspecified → underspecification-and-indeterminism. This is a cluster on irreducible ambiguity in natural-language specifications. Gibson supplies the missing "why": ambiguity persists because it is efficient wherever context disambiguates.
- information-value → reverse-compression, epiplexity-by-example, minimum-viable-vocabulary. information-value already owns the "Shannon abstracts away the observer" point and the retention-gap rule, so I kept it as the single representative of the cluster.
- silent-disambiguation → final-task-success / out-of-spec notes. These are not needed because the silent-disambiguation note itself carries the axis.

## Connections Found

All edges are candidates for `kb/sources/gibson-2019-how-efficiency-shapes-language.ingest.md`. Relative paths below resolve from this report. From the ingest, use `../theory/...` and `./...` respectively.

- [https://socsci.uci.edu/~rfutrell/papers/gibson2019efficiency.pdf](https://socsci.uci.edu/~rfutrell/papers/gibson2019efficiency.pdf) -- **derived-from**: the ingest analysis is worked out from this review paper. The URL is already in the snapshot's `source` frontmatter.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- **is-evidence-for**: the note treats semantic underspecification as a property of natural language itself. Gibson et al. give the efficiency explanation for why that property persists: ambiguity out of context lets speakers omit what context supplies, and the paper cites a formal proof (Piantadosi et al., ref. 14). This bears on the note's framing without the note having incorporated it.
- [Legal drafting solves the same problem as context engineering](../../../../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md) -- **is-evidence-for**: the source names legal contracts and programming languages as registers that pursue zero ambiguity and become wordy or pedantic as a result. This is independent support for the note's premise that drafting narrows interpretation at a cost. It also explains why no natural-language specification eliminates all ambiguity: ordinary language is optimized for the opposite trade.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- **is-evidence-for**: the note says classical information theory abstracts away the observer, and that retained content should be the gap between what the use requires and what the consumer can contribute. The source corroborates both points from linguistics. Speakers omit context-inferable information. The concluding remarks say information theory "assumes an idealized version of communication", so the processor's capacity to compute expectations must constrain the theory. Information locality is derived from comprehenders' noisy memory.
- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **is-evidence-for**: the hypothesis says compositionality arises approximately under communication pressure, and it still lacks a mechanism. The source offers a usage-based candidate: diachronic selection through the cultural-transmission bottleneck. A non-compositional system cannot survive input sparsity across generations. The source presents this as one possibility beside an innate inductive bias, so the ingest should carry that hedge. The mechanism does not by itself answer Fodor and Pylyshyn's systematicity condition.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with** (axis: whether residual ambiguity gets surfaced and repaired): Gibson's efficiency argument assumes that "participants can easily query each other to rapidly clarify any residual uncertainties". An agent executing a spec usually lacks that cheap repair channel, so ambiguity that is efficient in conversation becomes a silent contract gap. The comparison names exactly which assumption fails.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with** (axis: what a sender may leave out given the receiver's context): both say to omit what the receiver's context resolves and supply what it cannot. Gibson grounds this in source coding over shared context. The note grounds it in choice-specific authority and evidence boundaries. A reader gains the information-theoretic version of the same boundary.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) -- **compares-with** (axis: alternative encodings of relational structure): the source says fixed word order and morphology are two encodings of one latent dependency tree, and that they trade off, with redundant marking adding robustness. The evidence note found that sentence syntax carried semantic relations, and that replacing it with explicit restatement cost 4.9% more words. Its first-pass failure ("moved a temporal qualifier away from the definition it limited") is a dependency-length increase in the source's sense.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **compares-with** (axis: the comparison condition determines what claim is licensed): the source names specifying counterfactual baselines as "often the most challenging part of making an efficiency claim". Examples are random reorderings for dependency length and enumerated possible kinship systems. This is an observational, simulated-baseline instance of the note's point that a claim is indexed by its contrast. The fit is moderate, because the note is framed around interventions.
- [Connectionism and Cognitive Architecture: A Critical Analysis (Fodor & Pylyshyn)](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) -- **compares-with** (axis: the origin of compositional structure): Fodor and Pylyshyn require structured representations as an architectural commitment. Gibson et al. offer a cultural-transmission account in which compositionality is selected under learnability pressure. Reading the two together sharpens the gap the Fodor–Pylyshyn ingest records at line 57.

## Bidirectional Candidates

- [Connectionism and Cognitive Architecture: A Critical Analysis (Fodor & Pylyshyn)](../../../../sources/fodor-pylyshyn-1988-connectionism-cognitive-architecture.ingest.md) <-> source -- **compares-with**: the return path helps a reader of the Fodor–Pylyshyn ingest. Its analysis says the learned-approximation account must supply a mechanism for linked capacities, and this source names one candidate. Both are sources→sources edges under the same authorised label.

## Reverse-edge Candidates

Theory outbound edges to sources use `evidenced-by` (per `kb/theory/COLLECTION.md`). None of these is a refutation attempt, so each context phrase must say the source qualifies or bounds the claim, not that it corroborates it.

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) → future ingest -- **evidenced-by**: the Fodor–Pylyshyn paragraph says the hypothesis "still needs a mechanism explaining why related capacities develop together". Citing the transmission-bottleneck account there qualifies the gap with a named candidate mechanism. This is the strongest reverse edge.
- [Legal drafting solves the same problem as context engineering](../../../../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md) → future ingest -- **evidenced-by**: the claim "No natural language specification eliminates all ambiguity" could cite the source's efficiency explanation and its explicit legal-contract example. This bounds the claim: eliminating ambiguity costs length.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) → future ingest -- **evidenced-by**: the prior-work list and the "Classical information theory is the exception" paragraph could cite a working information-theoretic research program that concedes its idealization must be constrained by processor limits. This answers part of the note's TODO about relevant traditions.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reverse compression is when LLM output expands without adding information](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) -- both concern length versus information, but the source's length results are about code-word length under predictability. The note is about added extractable structure in prose. The overlap is a keyword match, and information-value already carries the observer-relative point.
- [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md) -- a Zipf-style "frequent means short" analogy to always-loaded context is suggestive, but the note's mechanism is attention competition in a loading hierarchy, not code length. The link would be metaphorical.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost](../../../../theory/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) -- this is information-theoretic vocabulary design for a bounded observer. The source's lexicon results (informativeness–complexity frontier) concern population-level evolution of word meanings, not term selection for an observer. Weak.
- [Local materialization should outperform distant declarations](../../../../theory/local-materialization-should-outperform-distant-declarations.md) -- information locality (put high-mutual-information items close) resembles "local beats distant". But the note's mechanism is generated materialization versus declaration and maintenance authority, not reading-time memory cost. Kept only as a synthesis signal below.
- [Vocabulary collisions should be prevented at write time](../../../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) -- this is a real tension rather than a support edge (see Flags). silent-disambiguation carries the comparison axis more directly.
- [Epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) -- an entropy-versus-observer explainer already covered through information-value. A duplicate route.
- [Symbols, neural networks, and mathematical intelligence (Lampinen)](../../../../sources/symbols-neural-networks-mathematical-intelligence.ingest.md) -- concerns symbol systems in mathematics. Its connection to this source runs through the meaning note, which is already kept.
- [Mesa optimizers and language recursion](../../../../sources/mesa-optimizers-and-language-recursion.ingest.md) -- a speculative essay on compression into generative rules. The overlap with compositionality is thematic only.
- [Design for the first-time human except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- it mentions clarification asking in one line. That is not load-bearing for the note.
- `kb/sources/gavel-graph-world-models.ingest.md` -- a name-match hit only.

## Index Membership

None. Sources do not participate in tags (`kb/tags/COLLECTION.md` `participating:` list), and `kb/sources/README.md` is a landing page without a topical index.

## Synthesis Opportunities

- **When omission is efficient, and when it fails.** Gibson's ambiguity argument, together with [silent disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md), [fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) and the retention-gap rule in [information value is observer-relative](../../../../theory/information-value-is-observer-relative.md), implies a higher-order claim. Leaving out context-inferable content is efficient only under two conditions: the receiver shares the disambiguating context, and repair is cheap. Agent handoffs and executed specifications often break the second condition. Check first whether fix-what-the-executor or intent-framed delegation already owns this before writing anything.
- **Locality as a reading-cost mechanism for KB prose.** AGENTS.md's writing rule "Keep necessary conditions next to their claims" has no theory note explaining it. The source's dependency and information locality, the qualifier-displacement failure in [two rewrites](../../../../theory/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md), and the two unprocessed dependency-locality snapshots together could ground one. Open question: whether bounded-memory locality transfers to transformer readers, given that attention is not a decaying working memory. That transfer is untested and must stay hedged.

## Maintenance Observations

- The companion snapshots `kb/sources/.snapshots/gibson-dependency-locality-theory.md` and `kb/sources/.snapshots/futrell-levy-gibson-dependency-locality.md` have no tracked ingests yet. Once they are ingested, they are natural sources→sources **compares-with** targets for this ingest: the same research program, at primary-study grain.
- The target's tracked ingest (`kb/sources/gibson-2019-how-efficiency-shapes-language.ingest.md`) did not exist at report time, so every outbound candidate here is pending that ingest.

## Flags

- **Tension (do not resolve here):** the source argues that ambiguity out of context is efficient because context disambiguates. [Vocabulary collisions should be prevented at write time](../../../../theory/vocabulary-collisions-prevented-at-write-time-not-read-time.md) and the KB's one-term-per-concept rule treat unscoped multiple senses as a defect to prevent. These are compatible if technical senses are the region where context does not reliably disambiguate, but no note states that boundary.
- **Transfer caution:** most mechanisms in the source concern human processors (working-memory retrieval, child acquisition, cultural transmission). Any ingest or theory claim that transfers them to LLM readers needs a stated mechanism, not analogy, per [human writing structures transfer to LLMs because failure modes overlap](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md).
- No split candidate: the source is a review with one organizing claim.
