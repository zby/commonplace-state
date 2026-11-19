---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/alien-space-of-science.ingest.md"
source_has_frontmatter: true
date: "2026-10-23"
depth: standard
---

# Connection Report: Ingest: The Alien Space of Science

**Source:** [Ingest: The Alien Space of Science](../../../../sources/alien-space-of-science.ingest.md)

The ingest already authors ten connections (seven notes, three sources, one external `derived-from`). All ten target paths exist, and each label is authorised for its source->destination pair in `kb/sources/COLLECTION.md`. This report lists only additional candidates and the reverse edges that the ingest's own Recommended Next Action implies.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section read. Prospected destinations: notes, reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/`, `kb/instructions/`. `external` is authorised only for `derived-from` and `see-also`; external prospecting was skipped because no new external target was supplied.

**Existing-link verification:** `test -f` passed on all ten in-repo targets already linked by the ingest.

**Title listing scan (notes):**
- `rg -N --no-heading -m1 '^# ' notes --glob '*.md' | rg -i "synthes|novel|divers|discover|recombin|prior|creativ|homogen|search|explor|candidate|connect|serendip|generat|oracle|backcast|origin"`. Flagged: open-ended-improvement-allocates-search-before-evaluation, lightweight-search-control-does-not-license-adoption, oracle-strength-spectrum, weakly-discriminated-qualities-tend-to-be-underselected, quality-signals (via oracle note), recognition-not-linking, synthesis-is-not-error-correction, oracle-accumulation, discovery-lifecycle, cost-sensitive-formalisms. Most are already in the oracle cluster's neighbourhood.

**Topic indexes:**
- `kb/tags/discovery-README.md` (`complete: true`; by-tag rg skipped). Its conditions-for-discovery and operation groupings contain every note the ingest already links, plus recognition-not-linking and epiplexity. No new note candidate passed.
- Sources do not carry tags. `tags/COLLECTION.md` lists participating collections `[notes, reference, instructions, agent-memory-systems, agentic-systems, reports]`, so sources are not tag members.

**Body search:**
- `rg -il "homogeni|mode collapse|ideation|cognitive(ly)? unavailab|community prior|recombin" notes sources agentic-systems agent-memory-systems reference tags`. Hits were short-composable-notes (already linked) and several sources/reviews with incidental use. No note develops LLM homogenization as a claim.
- `rg -il "oracle" notes`. The oracle cluster was confirmed. quality-signals-for-kb-evaluation was reached through the oracle note's footer.
- `rg -il "scientific discovery|research ideation|idea generation|novel idea|hypothesis generation|autoresearch|AI scientist" notes sources agentic-systems agent-memory-systems`. About 50 hits. Descriptions were evaluated for hypothesis-generation-and-updating, discoverphysics, ai-scientists-results-without-scientific-reasoning, primescientist, how-agents-fail-on-autoresearch, swarmworld, position-ai-agents-in-scientific-teams, llms-scientific-method, model-discovery-agent, when-code-is-free, self-revising-discovery-systems, scienceflow, AutoSci, ARIS.
- `rg -il "novelty|originality" sources notes`. Flagged interpolation-extrapolation-hyperpolation and beyond-not-novel-enough.
- `rg -il "ideation|novelty|idea generation|co-scientist|ai scientist" agentic-systems agent-memory-systems reference`. Only incidental hits (compound-engineering, primescientist archive, swarmworld archive, AutoSci). None models ideation selection.
- `rg -n "homogen|mode collapse|attractor" notes`. Only claim-modality (a reframe attractor, an unrelated mechanism).
- `rg -l "giants-generative|geometry-of-knowledge|llms-cant-jump"`. Inbound to sibling sources: automated-synthesis note, interpolation-extrapolation-hyperpolation, beyond-not-novel-enough, hot-take-llm-can-jump. This surfaced hyperpolation and beyond-not-novel-enough as cluster neighbours.

**Link following:**
- automated-synthesis-is-missing-good-oracles: read in full. Its "Current attempts" lists only tip consolidation and Geometry of Knowledge. Its first open question asks for a tiered oracle and cites Bystroński's missing first-tier detector. The alien paper is the natural next attempt (reverse edge).
- known-target-discovery-benchmarks-show-reachability-not-discovery: read the body and footer. It says GIANTS "leaves parent selection, problem selection, and candidate triage outside the test". The alien whole-space backcast exercises candidate triage, so it is the positive contrast case (reverse edge). The note currently cites GIANTS by external URL only and links no tracked sources.
- reviewers-share-the-fields-prior: footer checked. It has no source evidence for the generation-side homogenization, and nothing links to it from sources except this ingest.
- Source summaries were read for hyperpolation, beyond-not-novel-enough, model-discovery-agent and when-code-is-free.

## Connections Found

- [Interpolation, extrapolation, hyperpolation](../../../../sources/interpolation-extrapolation-hyperpolation.ingest.md) -- **compares-with** (axis: whether a creative move leaves the span of existing primitives): Ord defines creativity as finding good points outside the affine hull of known examples. Alien sampling seeks low-availability *combinations* inside a fixed 273-atom vocabulary. Following the link lets a reader place the method precisely: off the community's realized distribution, but not off the primitive subspace. This is sharper than the llms-cant-jump comparison, because Ord supplies the geometric vocabulary and pairs off-manifold generation with an environmental quality test, the same generator/filter split as alien's coherence model.
- [Beyond "Not Novel Enough"](../../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.ingest.md) -- **compares-with** (axis: how novelty relative to existing work is estimated): Afzal et al. assess novelty per submission through structured related-work retrieval and a reviewer-derived pipeline. Alien estimates availability at community scale with a learned author-matching score. Both try to harden a soft novelty oracle. They differ on unit (one paper versus an atom combination), on mechanism (LLM pipeline versus trained dual encoder) and on validation (alignment with human reasoning versus matching unseen 2025 authors).
- [When code is free, research is all that matters](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) -- **compares-with** (axis: whether research problem selection can be scored without ground truth): Tam argues that problem selection, or "research taste", resists automation because it lacks ground truth. Alien sampling is a direct attempt to learn a problem-selection prior from publication history. Its weak quality and novel-recovery evidence leaves Tam's claim standing for producing better science, while its diversity result shows that a selection *policy* can be learned and tested.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- **compares-with** (axis: separating open-ended proposal from a principled selector inside a fixed decomposition): MDA lets an LLM propose mechanisms and Bayesian inference select among them. Alien lets learned scorers select and an LLM decode. Both report gains bounded by a fixed domain decomposition, and both concede that the selector can be confidently wrong (MDA's wrong likelihood; alien's LLM-judged β sweep). The comparison shows the decomposition-bound limitation recurring across two independent systems.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- **compares-with** (axis: how a cheap first-tier oracle is built from weak signals): the note catalogues hand-chosen graph-topology and content-proxy signals for a composite oracle, untested for synthesis. Alien shows the alternative of two corpus-trained scorers, each with its own falsification check. The ingest's Extractable Value item 2 (score KB connections for coherence and for distance from existing co-citation) maps directly onto that catalogue's graph-topology signals.

## Bidirectional Candidates

- [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) <-> source -- **compares-with**: the ingest already links GIANTS. A return edge from GIANTS would let readers of the conditional backcast find the whole-space backcast with a novel/non-novel split. GIANTS does not currently link back.
- [Interpolation, extrapolation, hyperpolation](../../../../sources/interpolation-extrapolation-hyperpolation.ingest.md) <-> source -- **compares-with**: hyperpolation already links GoK and llms-cant-jump. Alien is a concrete in-span-recombination case paired with a learned quality filter, which tests Ord's generator/selector framing on science.

## Reverse-edge Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) → source -- **evidenced-by** (notes collection label): add under "Current attempts" and in the tiered-oracle open question. The context phrase should say that the evidence *qualifies* the claim. It shows a cheap learned first tier in a bounded, enumerable vocabulary. It does not corroborate or refute the oracle gap, because survivor quality evidence is weak (novel recovery 2.35–3.24× chance). This is the ingest's own Recommended Next Action. The note currently cites one tracked source, so it stays well under the five-unquoted-source limit.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source -- **evidenced-by**: the note says GIANTS leaves "candidate triage outside the test". Alien's frozen whole-space backcast is the case that does test triage, and its 35.9× overall versus 2.35× novel split bounds what such a backcast shows. Strong fit: it qualifies the note with a positive example the note lacks.
- [Decorrelated reviewers still share the field's prior](../../../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) → source -- **evidenced-by**: generation-side homogenization (frontier models selecting from one concept region; autoresearch drift to interpretability, 2/10 to 8/10). The context phrase must say this *bounds or extends* the note to generators rather than corroborating the reviewer claim, and that the counts are small.
- [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) → source -- **compares-with** (sources label), as in Bidirectional Candidates.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- a true fit (scorers allocate decoding effort before quality evidence exists), but the already-linked search-controller and candidacy notes carry the more specific claim. A third link adds traversal cost without a new reader gain.
- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- duplicates the role of the linked candidacy-evidence note.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- the autoresearch drift is a generator attractor, not an oracle-discrimination asymmetry. The β sweep's shared LLM judge is suggestive but untested. Too speculative to label.
- [Recognition, not linking, is the hard problem in knowledge systems](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -- the coherence model scores co-occurrence; it does not recognize shared structure. Keyword-level overlap.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- reachable through the automated-synthesis note. A direct link adds nothing specific.
- [PrimeScientist](../../../../sources/primescientist-research-effort-allocation.ingest.md) -- also evaluates selection among research plans, but its budget-sensitive allocation axis duplicates the search-controller link. A weak compares-with at best.
- [SwarmWorld](../../../../sources/swarmworld-stigmergic-technological-evolution.ingest.md) -- portfolio results concern shared-artifact accumulation, not off-prior selection. The overlap is topical only.
- [Hypothesis generation and updating in LLMs](../../../../sources/hypothesis-generation-and-updating-in-large-language-models.ingest.md), [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), [AI scientists: results without scientific reasoning](../../../../sources/ai-scientists-results-without-scientific-reasoning.ingest.md), [How agents fail on autoresearch](../../../../sources/how-agents-fail-on-autoresearch.ingest.md) -- each is about reasoning or execution quality in scientific agents, not idea selection or availability.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md), [ARIS](../../../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) -- research-memory systems with no ideation-selection mechanism to compare.
- [hot-take-llm-can-jump](../../../../sources/hot-take-llm-can-jump.ingest.md) -- reached via llms-cant-jump. The ingest's recombination-versus-premise point is already carried by its llms-cant-jump link.

## Index Membership

None. Sources carry no tags, and no curated source index covers scientific-ideation sources.

## Synthesis Opportunities

Geometry of Knowledge (generation broadening with no quality detector), Alien Space of Science (off-prior selection with a learned coherence filter), Ord's hyperpolation (off-manifold generation needs an environmental selector) and MDA (LLM proposal plus Bayesian selector) jointly suggest a claim that the automated-synthesis note only partly states. Escaping the generator's prior is cheap. What gives the escape value is the paired filter, and in every case that filter's validity is the weakest-evidenced component. A future note could name this as "off-prior generation is bounded by its paired selector" and test it against these four sources.

## Maintenance Observations

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) cites GIANTS only by external URL, although a tracked ingest exists at `kb/sources/giants-generative-insight-anticipation-scientific-literature.ingest.md`. The notes contract says source edges should point to the tracked ingest.
- No note in `kb/notes/` develops LLM output homogenization or iterative-refinement attractor drift as a claim. The alien ingest (Extractable Value 4) and Geometry of Knowledge both record it. It is a candidate log entry until more cases accumulate.

## Flags

- None. No split candidate: the ingest makes one analysis of one paper. The tension it already records (the paper relies on LLM judges, which the reviewers-share-prior note predicts will under-credit low-availability ideas) is left unresolved.
