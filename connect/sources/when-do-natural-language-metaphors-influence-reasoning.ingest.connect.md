---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: kb/sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md
source_has_frontmatter: true
date: "2026-02-15"
depth: standard
---

# Connection Report: When Do Natural Language Metaphors Influence Reasoning?

**Source:** [When Do Natural Language Metaphors Influence Reasoning?](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md)

## Discovery Trace

**Source collection:** `kb/sources/` (ingest report)

**Source COLLECTION.md outbound rules (ingest reports):**
- Authorized labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external)
- Excluded destinations: `kb/work/`, `kb/instructions/`
- Scan targets: theory, reference, sources, agent-memory-systems, agentic-systems, tags

**Existing connections in source (from ingest's own Connections Found section):**
- `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` — compares-with
- `human-writing-structures-transfer-to-llms-because-failure-modes.md` — is-evidence-for
- `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` — is-evidence-for
- `first-principles-reasoning-selects-for-explanatory-reach-over.md` — see-also

**Discovery procedure:**

**1. Curated heads (README.md + tag READMEs):**
- Read `kb/theory/README.md` — topical overview; no specific metaphor/reasoning cluster identified
- Read `kb/reference/README.md` — operational reference; no specific experimental-methodology cluster
- Checked `kb/tags/` for matching tags (metaphor-framing, experimental-methodology, cognitive-science, figurative-language) — none exist as dedicated tag READMEs
- Read `kb/tags/learning-theory-README.md` and `kb/tags/discovery-README.md` — relevant conceptual terrain but no direct match

**2. Full titles listing (theory):**
- Generated `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` — 140+ notes
- Scanned for metaphor, framing, reasoning effect, cognitive science, experimental methodology themes
- Flagged candidates: `human-writing-structures-transfer-to-llms-because-failure-modes.md`, `human-llm-differences-are-load-bearing-for-knowledge-system-design.md`, `first-principles-reasoning-selects-for-explanatory-reach-over.md`, `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md`, `llm-learning-phases-fall-between-human-learning-modes.md`

**3. Full titles listing (reference):**
- Generated `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` — 90+ notes
- Flagged candidate: `source-adoption-policy.md` (cognitive science gate for source adoption)

**4. Full titles listing (sources):**
- Listed `kb/sources/*.ingest.md` — found `metaphors-we-think-with.ingest.md` (the original Thibodeau & Boroditsky 2011 paper that Steen et al. 2014 critiques)
- Listed `kb/sources/*.ingest.md` — found `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` (already linked)

**5. Scoped description listing:**
- Ran `rg '^description:' kb/theory/ --glob '*.md'` — 140+ descriptions scanned
- Ran `rg '^description:' kb/reference/ --glob '*.md'` — 90+ descriptions scanned
- No additional candidates beyond title-listing hits

**6. Body search:**
- `rg -n "metaphor" kb/theory/ --glob "*.md"` — found metaphor mentions in `frontloading-is-partial-evaluation-not-divide-and-conquer.md`, `agent-statelessness-makes-routing-architectural-not-learned.md`, `legal-drafting-solves-the-same-problem-as-context-engineering.md` — all using "metaphor" in the sense of "analogy is not mechanism," not as direct topical match
- `rg -n "framing" kb/theory/ --glob "*.md"` — found framing mentions in `prompt-ablation-converts-human-insight-to-deployable-framing.md`, `systematic-prompt-variation-serves-verification-and-diagnosis-not.md` — relevant to framing methodology but not to metaphor-framing-in-reasoning directly
- `rg -n "Thibodeau\|Boroditsky" kb/ --glob "*.md"` — no existing links to these authors in the KB
- `rg -n "content effect" kb/theory/ --glob "*.md"` — found in `human-writing-structures-transfer-to-llms-because-failure-modes.md` and `structured-prompt-gains-do-not-establish-distribution-selection.md`

**7. Link following:**
- Followed links from `human-writing-structures-transfer-to-llms-because-failure-modes.md` — confirmed it links to `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` and `structured-prompt-gains-do-not-establish-distribution-selection.md`
- Followed links from `metaphors-we-think-with.ingest.md` — confirmed it lists this Steen et al. ingest as a reverse-edge candidate in its own Connections Found section
- Followed links from `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md` — confirmed it builds on the per-convention failure-mode methodology from `human-writing-structures-transfer-to-llms-because-failure-modes.md`

**8. Key discovery — existing reverse-edge:**
- `metaphors-we-think-with.ingest.md` (Thibodeau & Boroditsky 2011, the original claim) already lists this Steen et al. 2014 ingest in its own Connections Found as a reverse-edge candidate with label `compares-with`. The relationship is: original paper → critique/follow-up.

## Connections Found

### Existing (already linked in source)

- [language-models-like-humans-show-content-effects-on-reasoning.ingest.md](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) — **compares-with**: Both studies investigate how linguistic framing/content affects reasoning outcomes. Lampinen et al. shows LLMs exhibit human-like content effects on reasoning tasks; Steen et al. shows the originally-reported metaphor framing effect was actually an exposure effect when proper controls were added. Together they illustrate the complexity of evaluating framing effects and the importance of controlled experimental design.

- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **is-evidence-for**: The Steen et al. study provides a concrete worked example for this note's methodology. The original Thibodeau & Boroditsky finding appeared to show metaphor framing affects policy reasoning; Steen et al.'s controlled replication showed the effect was actually exposure to crime information, not metaphor-specific. This demonstrates per-convention failure-mode testing: when evaluating whether a cognitive phenomenon transfers or informs system design, test whether alternative explanations account for the observed effect before accepting the original claim.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design.md](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **is-evidence-for**: The Steen et al. findings illustrate the per-convention evaluation methodology this note advocates. The original metaphor framing claim was evaluated against alternative explanations (supporting metaphors in the text, absence of non-metaphorical control, no pre-exposure baseline), revealing it was an exposure effect rather than a metaphor-specific effect. A case where a cognitive science claim required careful controls before its implications could be assessed.

- [first-principles-reasoning-selects-for-explanatory-reach-over.md](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **see-also**: The Steen et al. study is a concrete illustration of the adaptive-fit vs explanatory-reach distinction. Thibodeau & Boroditsky found an effect that worked in their experimental setup (adaptive fit); Steen et al. showed this was an experimental confound (supporting metaphors, no control condition) rather than a generalizable mechanism (explanatory-reach).

### New candidates

- [metaphors-we-think-with.ingest.md](../../../../sources/metaphors-we-think-with.ingest.md) — **compares-with**: Direct source-to-source relationship. Thibodeau & Boroditsky (2011) is the original study reporting that metaphorical framing (crime as "beast" vs "virus") shifts policy preferences by 18-22%. Steen et al. (2014) is the direct follow-up critique that added three critical controls (non-metaphorical baseline, removal of supporting metaphors, pre-exposure measurement) and found no metaphor-specific effect — only an exposure effect. The relationship is original-claim → controlled-replication-fails-to-replicate. The Steen et al. paper explicitly positions itself as a methodological critique of this specific prior work.

- [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — **is-evidence-for**: This note assembles a methodology for evaluating cognitive-science-to-agent transfer: per-convention failure-mode matching, intermediate-position warning, and the simpler-mechanism test. The Steen et al. study is a concrete worked example of the first component — it shows a case where a cognitive science claim (metaphors influence reasoning) was evaluated by testing alternative explanations, revealing the effect was an exposure confound rather than a metaphor-specific mechanism. The study demonstrates why the per-convention approach is necessary: the original claim appeared robust (five experiments, large effect sizes) but collapsed under improved controls.

- [llm-learning-phases-fall-between-human-learning-modes.md](../../../../theory/llm-learning-phases-fall-between-human-learning-modes.md) — **see-also**: The Steen et al. finding that a seemingly robust cognitive science effect disappeared under improved experimental controls illustrates the intermediate-position warning from this note: human cognitive claims need careful evaluation before transfer to LLMs because the mappings are not 1:1. The exposure-effect finding is also relevant — it shows that what appears to be a specific cognitive mechanism (metaphor processing) may actually be a more general information-processing effect, paralleling this note's argument that human learning phases don't map cleanly onto LLM phases.

- [source-adoption-policy.md](../../../../reference/source-adoption-policy.md) — **see-also**: The Steen et al. study is a concrete case study for the cognitive-science gate in this policy. The policy states that cognitive-science and HCI patterns pass only when first-principles reasoning supports them, and that "cognitive-science analogies need independent justification." The Steen et al. paper demonstrates exactly this: a high-profile cognitive science claim that did not survive independent justification through improved experimental design. The study's methodological controls (non-metaphorical baseline, supporting-metaphor removal, pre-exposure measurement) are an operationalization of the "independent justification" the policy requires.

## Bidirectional Candidates

- [metaphors-we-think-with.ingest.md](../../../../sources/metaphors-we-think-with.ingest.md) ↔ [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) — **compares-with** (both directions): These are the original claim and its direct critique. The Steen et al. ingest already links to Thibodeau & Boroditsky as `compares-with` in its Connections Found. The reverse edge (Thibodeau & Boroditsky → Steen et al.) is also useful: readers encountering the original claim should know it was later critiqued by a controlled replication that found no metaphor-specific effect. This bidirectional connection would help readers navigate the claim → critique relationship.

## Reverse-edge Candidates

- [metaphors-we-think-with.ingest.md](../../../../sources/metaphors-we-think-with.ingest.md) → [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) — **compares-with**: This reverse edge already exists in the Thibodeau & Boroditsky ingest's own Connections Found section (the connect report for that ingest flagged this Steen et al. ingest as a reverse-edge candidate). The relationship is: original paper → follow-up critique that failed to replicate the original effect.

- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) — **is-evidence-for**: This theory note uses the Lampinen et al. study as its primary empirical evidence for the failure-mode overlap claim. It does not currently cite the Steen et al. study, which provides a complementary evidence type: a case where a claimed cognitive effect (metaphor framing) did NOT survive controlled replication. Adding this citation would strengthen the note's methodology section by showing both success (Lampinen: content effects transfer) and failure (Steen et al.: metaphor framing effect was an exposure confound) cases for the per-convention evaluation approach.

- [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → [when-do-natural-language-metaphors-influence-reasoning.ingest.md](../../../../sources/when-do-natural-language-metaphors-influence-reasoning.ingest.md) — **is-evidence-for**: This note currently uses Youssef's five principles as worked examples for the failure-mode methodology. The Steen et al. study could serve as an additional worked example in the methodology section, showing a case from the cognitive science literature where the per-convention approach would have prevented overgeneralization.

## Off-authorisation Candidates

None. All articulated candidates fit within the authorized label set from `kb/sources/COLLECTION.md`.

## Raw Text Candidates

None. All candidates are structured artifacts with frontmatter.

## Rejected Candidates

- `kb/theory/frontloading-is-partial-evaluation-not-divide-and-conquer.md` — **rejected**: This note uses "metaphor" in the sense of "analogy is not mechanism" (arguing that the PE framing is structurally precise, not metaphorical). The Steen et al. study is about metaphorical framing effects on reasoning, not about the precision of analogies as technical descriptions. The connection would be indirect at best — both use the word "metaphor" but in unrelated senses. The frontloading note's metaphor is a technical term meaning "loose analogy"; the Steen et al. study's metaphor is a cognitive linguistics phenomenon. Not a genuine connection.

- `kb/theory/prompt-ablation-converts-human-insight-to-deployable-framing.md` — **rejected**: The Steen et al. study and the prompt ablation note both deal with "framing," but in different senses. Prompt ablation is about testing different prompt formulations to find which elicits reliable agent behavior; Steen et al. is about metaphorical framing (crime as beast vs virus) affecting human policy preferences. The prompt ablation note's relevant citation is Thibodeau & Boroditsky (2011) as background evidence for why framing matters — that connection was already captured in the Thibodeau & Boroditsky ingest's own connect report. The Steen et al. study doesn't add to the prompt ablation connection.

- `kb/reference/control-plane-goals.md` — **rejected**: This note describes how KB goals live in always-loaded context. The Steen et al. study is about experimental methodology and metaphor framing effects. No genuine connection; the control-plane-goals note is about KB operations, not cognitive science methodology.

- `kb/theory/agent-statelessness-makes-routing-architectural-not-learned.md` — **rejected**: Contains a passing mention of "human-LLM differences" note in a metaphor context (warning against anthropomorphism). Not directly relevant to the Steen et al. study's findings about metaphor framing and experimental controls.

## Index Membership

None identified. The source is a single ingested scientific paper with a focused claim (methodological critique showing no metaphor framing effect under proper controls). It does not span enough thematic territory to warrant index membership beyond its existing topical tags.

## Synthesis Opportunities

- **Framing effects: a cautionary tale for KB methodology**: The Thibodeau & Boroditsky (2011) → Steen et al. (2014) sequence, combined with the Lampinen et al. (2024) content-effects study, tells a coherent story about evaluating cognitive science claims for KB transfer:
  - Thibodeau & Boroditsky: large, covert metaphor framing effect found (adaptive fit)
  - Steen et al.: effect disappears under proper controls — it was exposure, not metaphor (explanatory-reach failure)
  - Lampinen et al.: content effects on reasoning DO transfer to LLMs, but with boundaries (Wason divergence)
  
  This trio could support a synthesis note on "evaluating cognitive science claims for KB transfer" or "when cognitive science findings transfer to LLMs and when they don't." The synthesis would integrate: the per-convention failure-mode methodology (from `human-writing-structures-transfer-to-llms-because-failure-modes.md`), the intermediate-position warning (from `llm-learning-phases-fall-between-human-learning-modes.md`), and the source-adoption policy's cognitive science gate (from `source-adoption-policy.md`). Not created during connect — flagged for future authoring.

## Maintenance Observations

- **Quote gap in both metaphor ingests**: Both `metaphors-we-think-with.ingest.md` and `when-do-natural-language-metaphors-influence-reasoning.ingest.md` have empty `## Quotes` sections ("No source quotes have been retained yet."). For load-bearing source-dependent claims, quotes should be retained. This is noted here as a maintenance observation, not a connection candidate.

- **Planned note not yet written**: The Steen et al. ingest's "Recommended Next Action" section calls for writing a Commonplace note on figurative wording and reasoning that incorporates this source. That note does not yet exist. The ingest's extractable value items reference `[deep-dive]`, `[quick-win]`, `[experiment]`, and `[just-a-reference]` tags suggesting planned future work.

- **Cross-ingest consistency**: The `metaphors-we-think-with.ingest.md` already lists this Steen et al. ingest as a reverse-edge candidate. The connection is noted in both directions but not yet authored into either ingest's body. A future connect run on either ingest should confirm this bidirectional candidate is still worth authoring.

## Flags

- **Split candidate check**: The source makes multiple independent assertions (no metaphor effect, exposure effect, boundary conditions question, methodological controls as requirements). It connects to candidates across theory (failure-mode methodology, explanatory-reach, human-LLM differences, psychology transfer) and sources (original paper, content-effects paper). This warrants the split-candidate flag if the source is later incorporated into a note that carries these assertions separately. For the ingest itself, the connections are coherent around a single theme (methodological critique of metaphor framing claim), so no split flag is raised for this connect result.

- **Tension flagged**: The Steen et al. finding (no metaphor framing effect) and the Thibodeau & Boroditsky finding (large metaphor framing effect) are in direct tension. The Steen et al. paper argues the original effect was an exposure confound. The `metaphors-we-think-with.ingest.md` connect report already flags this as a "complementary" relationship with a noted tension: "a future ingest could note this tension: when does a framing's effect come from structural precision versus metaphorical knowledge-activation?" This tension is captured in the bidirectional candidates section above.

- **No external prospecting**: The reserved `external` destination is authorized for `see-also` and `derived-from` labels, but external prospecting was skipped — the skill does not search or browse the open web for candidates. No external targets were supplied by the user or present in loaded context.
