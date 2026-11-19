---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/alien-space-of-science.md"
source_has_frontmatter: true
date: "2026-10-23"
depth: standard
---

# Connection Report: The Alien Space of Science: Sampling Coherent but Cognitively Unavailable Research Directions

**Source:** [The Alien Space of Science](../../../../sources/.snapshots/alien-space-of-science.md)

The source is an immutable snapshot (arXiv 2603.01092v3, NeurIPS 2026). Under the sources `COLLECTION.md`, the snapshot never authors links; every candidate below is for the future `kb/sources/alien-space-of-science.ingest.md`, which does not exist yet.

**Source claims used for judging candidates:**
- LLM ideation inherits the field's "community prior" and recombines high-density regions of the literature; during an autoresearch loop, LLM-baseline ideas collapse toward an interpretability attractor (Claude 2/10 ideas -> 8/10 reports).
- Papers are distilled into conceptual units, then clustered into 273 "idea atoms" (191 for the pre-2025 build). Two learned scorers are trained over atom sets: coherence (an autoregressive transformer over atom tokens) and availability (an author-community dual encoder).
- Alien sampling ranks combinations that are high in coherence and low in availability. The portfolio is more diverse than frontier-LLM and batch-prompted baselines and matches or exceeds their quality under human, LLM-judge and autoresearch evaluation.
- Temporal test built only from pre-2025 data: the top 0.875% of 1.14M triples recovers 2025 combinations at 35.9x chance with coherence alone. Strictly novel combinations are recovered at only 2.35x chance. Weighting unavailability (beta = 0.4) raises novel recovery to 3.24x and the novel share from 3.8% to 8.8%. The authors call this "an early proxy rather than a final test."
- Division of labour: the cheap learned scorers do the exploratory ranking without per-candidate LLM calls, and the LLM only decodes the few selected combinations.
- Limitations: the method recombines only atoms already latent in the corpus, so it produces no new primitives. Availability is a lower bound estimated from publications. The human study is small, and LLM judges were calibrated against experts. Availability cannot distinguish cognitively unavailable directions from directions the field avoids for ethical reasons.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` § Outbound links. Authorized destinations are notes, reference, agent-memory-systems, agentic-systems, other sources, `notes/definitions` (`defined-in`) and `external` (`derived-from`, `see-also`). The excluded destinations are `kb/work/` and `kb/instructions/`. The snapshot is never the link author.

**Title listing scan (notes):**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` returned 427 titles. I filtered them with `rg -i 'novel|creativ|ideation|recombin|divers|homogen|collapse|mode|discover|prior|consensus|attractor|atom|distill|surpris|blind|explor|search|generat|scien|idea'`. The filter flagged reviewers-share-the-fields-prior, short-composable-notes-maximize-combinatorial-discovery, known-target-discovery-benchmarks, open-ended-improvement-allocates-search-before-evaluation, a-search-controller-is-tested-by-what-it-brings, cost-sensitive-formalisms, false-positive-generation, a-note-is-an-atomic-step, and natural-language-project-state-specializes-search-heuristics.
- A second title filter, `rg -i 'oracle|verif|codif|learned|bitter|scorer|rank|judge|prior'`, flagged oracle-strength-spectrum, the-boundary-of-automation, codify-versus-llm-decision-heuristics, and memory-management-policy-is-learnable-but-oracle-dependent.

**Topic indexes:**
- `kb/tags/discovery-README.md` declares `complete: true`, so I skipped the by-tag rg. The tag head surfaced automated-synthesis-is-missing-good-oracles, known-target-discovery-benchmarks, candidacy-evidence-licenses-escalation-not-acceptance, short-composable-notes, information-value-is-observer-relative, and recognition-not-linking.

**Body search** (all over `kb/notes kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags`, `-l -i`):
- `rg 'homogeni'` matched only memory-systems-table.md, which is not relevant.
- `rg 'mode collapse|collapse toward|attractor'` matched traditional-software-can-bracket, claim-modality, Closure-SDK and ADR 042. All use unrelated senses; rejected.
- `rg 'community prior|field.s prior|shared prior'` matched reviewers-share-the-fields-prior (kept) and error-correction-works-above-chance-oracles. The latter is the parent of the kept note, and I chose not to add it separately.
- `rg 'recombin'` matched short-composable-notes (kept) and full-identity-keys-decouple-a-batch-protocol, an unrelated sense.
- `rg 'novelty'` matched automated-synthesis (kept), known-target (kept) and the PrimeScientist/SwarmWorld archived reviews. The archived reviews are superseded surfaces, so I did not prospect them.
- `rg 'diversity'` matched synthesis-is-not-error-correction, hyperagents, ace, and agent-memory-requirements notes. All were evaluated below or rejected as off-axis.
- `rg 'serendip|bisociation|combinatory|combinatorial'` matched the discovery tag, short-composable-notes, information-value-is-observer-relative and recognition-not-linking.
- `rg 'ideation'` matched compound-engineering-plugin, Auto-claude-code-research-in-sleep (kept) and AutoSci. AutoSci only budgets ideation context, so I rejected it.
- `rg 'availability'` returned only the operational sense (service or artifact availability); rejected.
- `rg -l -i 'amortiz' kb/notes` found no note on the paper's "learned scorers vs prompting" amortization point.

**Sources prospecting:**
- `ls kb/sources | grep -i -E 'alien|ideation|novel|scien'` found no existing alien ingest. It listed GIANTS, ai-scientists-results-without-scientific-reasoning, beyond-not-novel-enough, scientisttwo, primescientist and others.
- `rg -l -i -e 'ideation|novelty|homogen|diversity|idea generation|research idea' kb/sources/*.ingest.md` listed about 45 ingests. I scanned their descriptions and kept geometry-of-knowledge, interpolation-extrapolation-hyperpolation, giants, llms-cant-jump and agora.

**Link following:**
- automated-synthesis-is-missing-good-oracles leads to geometry-of-knowledge, oracle-strength-spectrum and the boundary-of-automation. The open question there on a "tiered oracle" with fast heuristic first-tier filters is directly answered in kind by the alien coherence scorer.
- known-target-discovery-benchmarks leads to GIANTS, oracle-strength-spectrum and recognition-not-linking. The note says GIANTS leaves "parent selection, problem selection, and candidate triage outside the test". Alien's temporal test instead ranks the whole candidate space, so it does exercise selection.
- In the `## Connections Found` sections of the GIANTS, hyperpolation, geometry-of-knowledge and llms-cant-jump ingests, all four cluster on automated-synthesis, oracle-strength-spectrum and recognition-not-linking. This confirms that the source joins an existing discovery/oracle cluster.
- The agora ingest reports a "narrow search spine" and parallel rediscovery that escaped only after a human diversity intervention. This is the same collapse dynamic that alien targets with an explicit availability pressure.
- reviewers-share-the-fields-prior leads to error-correction-works-above-chance-oracles and narrowing-bought-to-survive-review.

**Reference and agentic-systems:**
- `rg -i 'novelty|diversity' kb/reference -l` matched gate-learning-from-accepted-edits, archive/operational-destinations-for-literature-grounding-findings and ADR 081. All are off-axis; no reference candidate.
- `ls kb/agentic-systems/reviews | rg -i 'sci|research|aris|sleep'` matched only academic-research-skills, which is not an ideation system. No agentic-systems candidate.

**External:** Skipped (not a prospecting surface). The only already-known external target is the source's own arXiv URL, for the ingest's `derived-from`.

## Connections Found

All are candidates for the future `alien-space-of-science.ingest.md`.

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- **is-evidence-for**: The paper supplies a learned, cheap, first-tier soft oracle for recombinative synthesis: a coherence model over idea atoms that ranks 1.14M triples with no per-candidate LLM call. Downstream human, LLM-judge, autoresearch and temporal checks then test it. This bears on the note's open "tiered oracle" question and adds a third current-attempts case beside the tip-consolidation and Bystroński cases. It does not refute the note, for three reasons: it works in a bounded domain (16k LLM papers, 273 atoms), the quality evidence rests mostly on calibrated LLM judges, and the authors flag feasibility as assessed "only implicitly and late."
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- **is-evidence-for**: The pre-2025 -> 2025 recovery test is a backcast that, unlike GIANTS, exercises selection: it ranks the whole candidate space, so no lineage is supplied. The numbers fit the note's caution. Overall recovery is 35.9x chance, but strictly novel recovery is only 2.35x with coherence alone and 3.24x with the availability weight, and the authors call the test "an early proxy rather than a final test." It sharpens the note by showing that a backcast can test candidate triage, not only conditional synthesis.
- [Decorrelated reviewers still share the field's prior](../../../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- **is-evidence-for**: The paper gives empirical evidence for the shared-prior mechanism on the generation side. Frontier LLMs "approximate and amplify" the community prior, return to the same narrow concept region within and across models, and drift toward an interpretability attractor under iterative refinement. This is the correlated-error term the note attributes to judges drawn from one training distribution. The paper also relies on LLM judges for most quality evidence, which the note predicts should be read cautiously for original (low-availability) claims.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **is-evidence-for**: Alien sampling is a learned search controller. It is evaluated the way the note prescribes: by the distribution of what it routes into stronger evaluation (human ratings, blind LLM comparison, autoresearch execution), under matched comparison with LLM-ideation baselines, without claiming any single routed idea is correct.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- **is-evidence-for**: The paper is a worked example of the two-role separation outside the KB. Coherence and availability scores route atom combinations to costly LLM decoding and autoresearch; the authors say explicitly that alien ideas are "not guaranteed breakthroughs" and that the claim is distributional. This makes it a third witness for the conjecture, which currently has two.
- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- **compares-with** (axis: the unit of recombination and how combinations are chosen): Both treat discovery as recombining small self-contained units. The note's units are authored one-claim notes that are co-loaded and selected by recognition. The paper's units are LLM-distilled, clustered "idea atoms" ("between keywords and full papers"), and selection uses a learned objective that favors combinations distant from existing communities. That echoes the note's claim that distant perspectives are likelier to reveal structure, but here it is measured rather than assumed.
- [Information value is observer-relative](../../../../notes/information-value-is-observer-relative.md) -- **compares-with** (axis: what makes coherent structure inaccessible): The note makes accessibility relative to a bounded observer's prior knowledge and tools. The paper's "cognitive availability" makes it relative to a research community's realized output. The comparison shows the same gap at population scale and gives a learnable estimator for it.
- [Geometry of Knowledge](../../../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md) -- **compares-with** (axis: mechanism for escaping LLM output homogeneity, and whether a quality oracle accompanies it): Geometry of Knowledge perturbs embedding-space anchors and admits it has no low-quality/OOD detector. Alien searches a discrete atom space under a learned coherence scorer, paired with an explicit off-prior (availability) term.
- [Interpolation, extrapolation, hyperpolation (Ord)](../../../../sources/interpolation-extrapolation-hyperpolation.ingest.md) -- **compares-with** (axis: what "outside the familiar region" means): Ord defines it geometrically, as off the observed subspace. Alien defines it sociologically, as off the author-community distribution, and its limitation (no new primitives) places it inside the span of existing atoms. In Ord's terms, that makes it closer to interpolation over a sparse combinatorial space than to hyperpolation.
- [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) -- **compares-with** (axis: how temporal provenance is used to validate scientific ideation): GIANTS reconstructs a downstream insight from supplied parent papers. Alien freezes the pre-2025 vocabulary and models and measures enrichment of 2025 combinations in a ranked shortlist over the whole space.
- [LLMs can't jump](../../../../sources/llms-cant-jump.ingest.md) -- **compares-with** (axis: recombination versus premise invention): Alien's stated limitation, that it "can only recombine concepts already present in the literature," puts it squarely on the deductive/recombinative side of Zahavy's distinction. The pairing tells a reader that alien sampling is not evidence for abductive invention of new primitives.
- [Agora](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) -- **compares-with** (axis: collapse of collective autoresearch onto a familiar region, and the remedy): Agora's run narrowed to one search spine until a human diversity intervention. Alien documents the same collapse in LLM-baseline autoresearch and builds the diversity pressure into candidate selection via the availability term.
- [Auto-claude-code-research-in-sleep](../../../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) -- **compares-with** (axis: how a research-ideation system avoids re-proposing familiar directions): ARIS keeps a retained `gap_map.md` and wiki pages as advisory anti-repetition context for an LLM ideator. Alien replaces prompt-level steering with trained scorers that rank combinations before the LLM sees them. This is a weaker candidate; include it only if the ingest discusses deployed ideation systems.

## Bidirectional Candidates

- [Geometry of Knowledge](../../../../sources/geometry-of-knowledge-extending-diversity-boundaries-llms.ingest.md) <-> source -- **compares-with**: The geometry ingest's connect report flagged that a second source on diversity engineering might warrant a clustering note, and alien is that second source. A return link from geometry-of-knowledge to the alien ingest would let a reader of either see the oracle-present versus oracle-absent contrast.
- [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) <-> source -- **compares-with**: GIANTS' ingest already positions itself against Meta-Harness on oracle type. Alien gives it a second scientific-ideation sibling that differs on whether selection is part of the test.

## Reverse-edge Candidates

These apply once the ingest exists. Each would be authored under `kb/notes/COLLECTION.md` rules, which should be checked for the label before authoring.

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -> alien ingest -- **evidence**: This is the strongest reverse edge. Alien belongs in "Current attempts" as a learned first-tier synthesis filter, and its own wording answers the "tiered oracle" open question in part: "the scorers do most of the exploratory work... The LLM then works out how to turn those combinations into coherent research proposals."
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -> alien ingest -- **evidence**: The note currently has only GIANTS as its backcast exemplar. Alien is a backcast that includes selection and reports the novel/non-novel recovery split, which is exactly the distinction the note needs to make concrete.
- [Decorrelated reviewers still share the field's prior](../../../../notes/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -> alien ingest -- **evidence**: The note asserts the shared prior from reasoning. Alien gives empirical citations for LLM homogenization toward the field's prior (refs [20, 37, 49] in the paper) and its own interpretability-collapse observation.

## Off-authorisation Candidates

- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) -- The paper's "why learned scorers rather than prompting" argument moves exploratory ranking out of per-call LLM work into small trained models. The stated reasons are that the vocabulary exceeds a single context at about 30k atoms and that per-run LLM cost scales poorly. This is a third option beside "codify" and "LLM interprets" (*learn a cheap specialized scorer*), so neither side of the note's dichotomy fits. `is-evidence-for` would overstate it and `compares-with` has no clean shared axis. Suggest rejecting for now, or recording a log observation if a second source shows the learned-scorer middle path.

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- The coherence scorer plus temporal recovery is a soft-oracle hardening case. The edge would duplicate the automated-synthesis edge, though, and the ingest can reach the spectrum through that note; keep it only if the ingest discusses oracle hardening specifically.
- [Open-ended improvement must allocate search before decisive evaluation](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) -- Alien is an instance, but the note's claim (search must precede decisive evidence) is a general structural argument the paper neither tests nor strains. The search-controller edge carries the useful part.
- [Recognition, not linking, is the hard problem](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -- Alien does not perform recognition of shared structure; it ranks co-occurrence plausibility over pre-clustered atoms. HDBSCAN clustering of conceptual units is a weak analogue of naming recognized structure, but the edge would mislead.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- Reachable via automated-synthesis; a direct edge adds nothing specific.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) and [synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) -- Alien does no voting, aggregation or error correction; the "diversity" hits were keyword-only.
- AutoSci and compound-engineering-plugin reviews -- These only budget or stage ideation context, with no mechanism for steering away from familiar ideas.
- Reference collection (gate-learning-from-accepted-edits, ADR 081, literature-grounding archive) -- "novelty/diversity" hits are about edits or literature disposition, not ideation.
- primescientist / swarmworld (reviews-archive) -- These are archived review surfaces. They are about research-effort allocation and swarm novelty, not the community prior; not prospected further.

## Index Membership

None. Tag membership heads such as `discovery` list notes, not ingests. The ingest's own placement is set by the sources collection, not by tag heads.

## Synthesis Opportunities

- automated-synthesis-is-missing-good-oracles + geometry-of-knowledge + alien + candidacy-evidence-licenses-escalation together suggest a higher-order claim about *diversity engineering for ideation*. A generation-side diversity pressure, whether latent perturbation or an availability penalty, is useful only when paired with a cheap candidacy filter, here a coherence model. Without the filter, broadened generation produces oracle-less noise (geometry-of-knowledge). With it, broadening becomes a routing policy whose value is judged by downstream assessment (alien). The geometry ingest's connect report already flagged this as awaiting a second source; alien is that source. Do not create it during connect.

## Maintenance Observations

- The geometry-of-knowledge ingest's recorded gap ("the KB has no dedicated note on latent-space / embedding-geometry control of generation... if a second source on this theme arrives a clustering note may be warranted") now has a candidate second source. The theme is broader than latent space: it is off-prior diversity pressure under a cheap coherence filter.
- No note in `kb/notes/` names the "LLM inherits and amplifies the community prior" mechanism on the *generation* side. reviewers-share-the-fields-prior treats only the judging side. Several ingests now evidence homogenization: geometry-of-knowledge, agora, and alien.

## Flags

- No ingest exists yet. All outbound candidates presuppose `kb/sources/alien-space-of-science.ingest.md`. `derived-from` should point to the external source URL `https://arxiv.org/abs/2603.01092`.
- Not a split candidate. The source makes one framework claim with supporting evidence; independent assertions (atoms, coherence/availability decomposition, temporal recovery) serve that one claim.
- Tension to preserve in the ingest: the headline 35.9x temporal recovery is mostly non-novel recombination. Strictly novel recovery is 2.35x-3.24x chance, and the human study is small. Edges that use the paper as evidence of prospective discovery should cite the novel-recovery figures, not the headline.
