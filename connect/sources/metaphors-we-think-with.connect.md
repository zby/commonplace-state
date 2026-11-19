---
description: "Discovery report for possible KB connections from metaphors-we-think-with snapshot"
type: types/connect-report.md
source: kb/sources/.snapshots/metaphors-we-think-with.md
source_has_frontmatter: true
date: "2026-02-26"
depth: standard
---

# Connection Report: Metaphors We Think With

**Source:** [Metaphors We Think With: The Role of Metaphor in Reasoning](./../../../../kb/sources/.snapshots/metaphors-we-think-with.md)

**Target artifact:** `kb/sources/.snapshots/metaphors-we-think-with.md`

**Note on authored surface:** This snapshot has no matching `.ingest.md` in `kb/sources/`. Per `kb/sources/COLLECTION.md`, snapshots are immutable and the authored connection surface is normally the matching ingest report. Connection suggestions below target a future ingest report for this snapshot.

## Discovery Trace

**Source collection:** `kb/sources/`

**Authorized destinations (from sources/COLLECTION.md outbound section):**
- theory (labels: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`)
- reference (label: `see-also`)
- sources (labels: `compares-with`, `see-also`)
- agent-memory-systems (labels: `is-evidence-for`, `compares-with`, `see-also`)
- agentic-systems (labels: `compares-with`, `see-also`)
- external (label: `derived-from` — reserved for already-known targets only)

**Excluded destinations:** `kb/work/`, `kb/instructions/`

**Description listing scan:**

- **theory:**rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' returned 89 titles. Flagged candidates: `knowledge-storage-does-not-imply-contextual-activation.md`, `human-writing-structures-transfer-to-llms-because-failure-modes.md`, `frontloading-is-partial-evaluation-not-divide-and-conquer.md`, `prompt-ablation-converts-human-insight-to-deployable-framing.md`, `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`, `recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md`

- **reference:** 50 titles scanned. No candidates with substantive metaphor/framing relevance.

- **sources:** rg -l '*.ingest.md' returned existing ingest files. Flagged: `gick-holyoak-analogical-problem-solving.ingest.md` (analogical reasoning connection), `agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md` (framing/exploration connection via prompt-ablation link)

- **agent-memory-systems:** 30 titles scanned. Reviews mentioning "metaphor" as design element: `openviking.md` (filesystem metaphor), `MemoryOS.md` (OS metaphor), `virtual-context.md` (OS metaphor). Connections are loose — the paper is about metaphor's cognitive effects, not whether system metaphors are effective design.

- **agentic-systems:** 30 titles scanned. No direct candidates.

**Body search — theory:**

- `rg -n "metaphor" kb/theory/ --glob "*.md"` — returned hits in `frontloading-is-partial-evaluation-not-divide-and-conquer.md` (PE framing vs metaphor distinction), `agent-statelessness-makes-routing-architectural-not-learned.md` (metaphors mislead), `legal-drafting-solves-the-same-problem-as-context-engineering.md` (shared metaphorical vocabulary caveat). Evaluated: the frontloading note's "not metaphorical" claim is directly relevant; the others use "metaphor" in passing.

- `rg -n "framing" kb/theory/ --glob "*.md"` — returned hits in `prompt-ablation-converts-human-insight-to-deployable-framing.md` (framing selection methodology), `systematic-prompt-variation-serves-verification-and-diagnosis-not.md` (prompt framing variation), `frontloading-is-partial-evaluation-not-divide-and-conquer.md` (PE framing). Evaluated: prompt-ablation is the strongest candidate — the metaphor paper is empirical evidence for why framing matters.

- `rg -n "reasoning" kb/theory/ --glob "*.md"` — too broad; filtered to notes with framing/activation relevance.

**Body search — sources:**

- `rg -n "metaphor" kb/sources/ --glob "*.ingest.md"` — returned 14 ingest files mentioning "metaphor". Most use it in passing (e.g., "metaphorically", "OS metaphor"). The Gick & Holyoak ingest is the strongest analogical-reasoning connection.

- `rg -n "framing" kb/sources/ --glob "*.ingest.md"` — returned framing mentions in context-engineering and text-optimization sources. `agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md` explicitly links to prompt-ablation.

**Link following:**

- From `knowledge-storage-does-not-imply-contextual-activation.md`: links to Gick & Holyoak ingest as evidence for the activation gap. This creates a triangle: metaphor paper → activation note ← Gick & Holyoak. The metaphor paper provides a different angle on the same problem — how framing activates knowledge structures.

- From `prompt-ablation-converts-human-insight-to-deployable-framing.md`: links to `agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md` as an example. The metaphor paper could strengthen this lineage with foundational framing-effect evidence.

## Connections Found

- [knowledge-storage-does-not-imply-contextual-activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The metaphor paper provides empirical evidence that framing can instantiate "frame-consistent knowledge structures" and invite "structurally-consistent inferences" — directly supporting the note's core distinction between storage, read-back, and activation. The paper demonstrates that a single metaphorical word shifts reasoning by 18-22% (larger than partisan differences) without people recognizing the influence — a clean demonstration of the "expert-witness pattern" where knowledge is present but not self-triggering. The covert-effect finding is particularly relevant to the note's claim that "the model knows X" is often the wrong operational question.

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **is-evidence-for**: The paper provides empirical evidence about content effects on reasoning — how the same information framed differently (virus vs. beast) leads to systematically different conclusions. This supports the failure-mode overlap argument that LLMs share human-like reasoning vulnerabilities. The paper's finding that metaphors act through "elaborated knowledge structures" rather than simple lexical priming (Experiment 3 dissociation) is relevant to understanding what kinds of human cognitive patterns transfer and at what mechanism depth.

- [frontloading-is-partial-evaluation-not-divide-and-conquer](../theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md) — **compares-with**: The paper explicitly argues that metaphors are not "mere rhetorical flourishes" but have "profound influences on how we conceptualize and act" — directly relevant to the frontloading note's argument that the PE framing is "structurally precise, not metaphorical." These are complementary, not contradictory: the metaphor paper shows metaphors have real cognitive effects (so framing is never nothing), while the frontloading note clarifies that in a shared-token medium, some framings are precise substitutions rather than loose metaphors. A future ingest could note this tension: when does a framing's effect come from structural precision vs. metaphorical knowledge-activation?

- [prompt-ablation-converts-human-insight-to-deployable-framing](../theory/prompt-ablation-converts-human-insight-to-deployable-framing.md) — **see-also**: The metaphor paper is a foundational empirical study of how framing affects what reasoning strategies come to mind. The prompt ablation methodology tests different framings to find which cognitive moves agents can reliably execute; the metaphor paper demonstrates that minimal framing changes (single word) produce significant behavioral shifts. Relevant as background evidence for why ablation studies matter and as a model of controlled framing experiments.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design](../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **see-also**: The paper's finding that metaphorical framing influence is "covert" — people do not recognize metaphors as influential in their decisions, instead pointing to "more substantive" information — is relevant to the naive anthropomorphism warning. If humans don't recognize how framing affects their own reasoning, treating LLMs as "junior colleagues who'll learn" becomes even more problematic. The paper also demonstrates that political affiliation predicts metaphor congruence (Democrats/Independents 63% vs Republicans 49%), adding nuance to the dual-audience design problem.

## Bidirectional Candidates

None. The source is a scientific paper providing evidence; the theory notes it connects to are methodological claims that use evidence rather than providing evidence back. No target note makes claims that need validation from this source in the reverse direction.

## Reverse-edge Candidates

- [gick-holyoak-analogical-problem-solving](../sources/gick-holyoak-analogical-problem-solving.ingest.md) → metaphors-we-think-with — **compares-with**: Both papers examine how mental representations affect problem-solving behavior. Gick & Holyoak show that memory alone doesn't guarantee analogical use (hinting is the differentiator); the metaphor paper shows that metaphors instantiate knowledge structures that guide reasoning even without awareness. Complementary evidence about the recognition/activation gap — Gick & Holyoak from the analogical-transfer side, the metaphor paper from the framing side. The metaphor paper's Experiment 3 (lexical prime vs. embedded metaphor) is particularly relevant: it shows that mere word activation isn't enough, paralleling Gick & Holyoak's finding that recall ≠ use.

- [agents-explore-but-agents-ignore-llms-lack-environmental](../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) → metaphors-we-think-with — **see-also**: The explore paper links to prompt-ablation as a methodology connection; the metaphor paper provides foundational evidence about framing effects that the ablation methodology operationalizes for agent contexts. The explore paper's finding that agents ignore available environmental information parallels the metaphor paper's finding that people ignore metaphorical framing — both are activation failures, though at different levels (agent tool-use vs. human conceptual reasoning).

## Off-authorisation Candidates

- **theory/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md** — Passes articulation test (the metaphor paper shows that people don't recognize metaphor as influential, which is a recognition failure), but no authorised label fits. The `is-evidence-for` label would be appropriate if the note's claim were specifically about recognition failures, but the note is about linking cost structure, not recognition phenomenology. Suggest either extending the `is-evidence-for` authorisation to cover this note's specific claim, or reclassifying as `see-also` if the collection author agrees the connection is tangential.

- **agent-memory-systems/reviews/openviking.md** (and similar OS-metaphor reviews) — The metaphor paper could inform evaluation of whether system metaphors (filesystem-as-metaphor, OS-as-metaphor) are merely descriptive or actually influence behavior. However, the authorised labels for agent-memory-systems (`is-evidence-for`, `compares-with`, `see-also`) require the source to bear materially on the system's design or operation. The paper is about human reasoning, not system design. Off-authorisation unless a future ingest makes the bridge explicit (e.g., "this system's X metaphor may have the covert-influence effect the Thibodeau paper documents").

## Raw Text Candidates

None. The source has frontmatter and is a structured scientific paper.

## Rejected Candidates

- Generic "reasoning" theory notes (e.g., `title-as-claim-enables-traversal-as-reasoning.md`, `retained-theories-may-improve-sample-efficiency.md`) — Mention reasoning but without specific framing/metaphor relevance. Keyword overlap insufficient.

- Crime/social-policy-specific notes — Out of KB scope. The paper uses crime as a test domain; its findings generalize to framing effects broadly, but KB notes about crime policy would be scope violations.

- Notes mentioning "framing" only in passing (e.g., `llm-frameworks-should-keep-the-tool-loop-optional.md` — "retry with a different framing") — Framing mentioned as a retry tactic, not a phenomenon under study. Insufficient connection depth.

- `legal-drafting-solves-the-same-problem-as-context-engineering.md` — Notes shared metaphorical vocabulary as a caveat, but doesn't engage with metaphor's cognitive effects. The connection is to the caveat, not to the paper's claims.

## Index Membership

None identified. The source is a single empirical paper; it doesn't warrant a new index.

## Synthesis Opportunities

- **Covert framing effects as a cross-cutting concern:** The metaphor paper + Gick & Holyoak + knowledge-storage-does-not-imply-contextual-activation together suggest a pattern: knowledge/framing can be present without being active, and the gap is often covert (people/agents don't recognize the influence). This could support a synthesis note on "covert activation effects" but the claim needs more anchoring before promotion.

- **Framing experiment methodology for agent evaluation:** The metaphor paper's controlled experiments (single-word manipulation, dissociated priming, time-course variation) could inform how to design agent framing tests. The prompt-ablation note already references this lineage indirectly; making it explicit could strengthen the methodology.

## Maintenance Observations

- **Missing ingest:** This snapshot has no matching `.ingest.md`. The `kb/sources/` collection contract expects ingest reports to own durable source identity and carry the active outbound surface. A future ingest would be the natural place to author the connections identified above.

- **Sibling snapshot without ingest:** `kb/sources/.snapshots/when-do-natural-language-metaphors-influence-reasoning.md` is in the same directory but also lacks an ingest. These two papers (Thibodeau & Boroditsky 2011; and the "when-do" paper) form a natural pair on metaphor and reasoning — a future ingest could address both or link them.

- **No existing KB references:** `rg -n "Boroditsky\|Thibodeau" kb/ --glob "*.md"` returned no hits. This paper is not yet cited anywhere in the KB. The connect report is the first traversal signal.

## Flags

- **Split candidate:** The source makes multiple independent assertions relevant to different theory areas (activation, failure-mode overlap, framing precision, prompt ablation methodology). If a future ingest authors all five `Connections Found` candidates, it would connect across four distinct theory topics — flag as a split candidate for tracking.

- **No-connections finding for agent-memory-systems/agentic-systems:** Despite scanning review titles and body content, no strong connection emerged to existing agent-memory-system or agentic-system reviews. The paper is about human cognitive psychology, not system implementation. This is an honest negative, not a gap — the authorised labels require material bearing on system design, which the paper doesn't provide without an explicit bridge.
