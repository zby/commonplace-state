---
description: "Discovery report for possible KB connections from kb/sources/.snapshots/when-do-natural-language-metaphors-influence-reasoning.md"
type: types/connect-report.md
source: "kb/sources/.snapshots/when-do-natural-language-metaphors-influence-reasoning.md"
source_has_frontmatter: true
date: "2026-02-15"
depth: standard
---

# Connection Report: When Do Natural Language Metaphors Influence Reasoning?

**Source:** [When Do Natural Language Metaphors Influence Reasoning?](kb/sources/.snapshots/when-do-natural-language-metaphors-influence-reasoning.md)

**Note:** This snapshot is immutable. Connections below are recommendations for the matching `.ingest.md` (when created) or for other artifacts that cite this source. No ingest exists yet for this snapshot.

## Discovery Trace

**Source collection:** `kb/sources/` (COLLECTION.md read; outbound labels: `derived-from`, `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, `see-also`; excluded destinations: `kb/work/`, `kb/instructions/`)

**Destination prospecting:**

### Theory collection

**Titles listing scan** — full `rg -N --no-heading -m1 '^# ' kb/theory/` returned ~380 titles. Manual scan for metaphor, framing, reasoning, cognitive science, experiment methodology terms. No title directly about metaphor framing effects.

**Body search — `metaphor`:**
- `rg -n "metaphor" kb/theory/ --glob "*.md"` — 7 hits, all using "metaphor" in the loose sense (e.g., "compiled vs. source as a productive systems-engineering metaphor", "the PE framing structurally precise, not metaphorical"). No hits about natural-language metaphor influencing reasoning.

**Body search — `framing`:**
- `rg -n "framing" kb/theory/ --glob "*.md"` — hits in `prompt-ablation-converts-human-insight-to-deployable-framing.md` (about prompt framings for LLMs), `minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md` (conceptual thresholds framing), and a few others. The `prompt-ablation` note is thematically adjacent (framing affects outcomes) but operates in a different domain (LLM prompt design vs human cognitive psychology). Rejected as too distant for a load-bearing label.

**Body search — `reasoning`:**
- `rg -n "reasoning" kb/theory/ --glob "*.md"` — many hits but most are about reasoning *production vs evaluation*, reasoning in agents, etc. The most relevant is `reasoning-production-is-not-reasoning-evaluation.md` but that is about evaluation methodology, not about how framing affects reasoning content.

**Body search — `Thibodeau|Boroditsky|Steen`:**
- `rg -n "Thibodeau|Boroditsky|Steen" kb/theory/ --glob "*.md"` — no hits. The specific authors/study are not cited anywhere in theory.

**Body search — `content.*effect|content effect`:**
- Found `human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md` which cites Lampinen et al. on content effects on reasoning. This is the strongest theoretical connection point.

**Link following from relevant theory notes:**
- `human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md` → cites Lampinen et al. source ingest; no existing link to Steen et al.
- `human-llm-differences-are-load-bearing-for-knowledge-system-design.md` → discusses cognitive science transfer methodology; no existing link to Steen et al.
- `first-principles-reasoning-selects-for-explanatory-reach-over.md` → discusses adaptive-fit vs explanatory-reach; Steen et al. is a concrete worked example of this distinction.

### Sources collection

**Titles listing scan** — full `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.ingest.md'` returned ~200+ ingests. Manual scan for metaphor, cognitive science, framing terms.

**Body search — `metaphor`:**
- `rg -l "metaphor" kb/sources/ --glob "*.md"` — 8 ingests. Checked each:
  - `a-new-way-to-think-about-composing-skills-to-increase.ingest.md` — metaphor used loosely
  - `greenfield-short-software-factories-oopsla-2003.ingest.md` — metaphor in software design
  - `the-thing-we-refer-to-as-memory-in-llms-is-just-a-bunch-of.ingest.md` — metaphor as loose analogy
  - `psychology-solves-ai-memory-identity-construction-2025307030651.ingest.md` — cognitive science but not metaphor framing
  - Others — not about metaphor framing effects on reasoning

**Body search — `framing`:**
- `rg -l "framing" kb/sources/ --glob "*.md"` — 16+ ingests. The most relevant is `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` which studies content/framing effects on reasoning tasks.

**Targeted candidate evaluation:**
- `language-models-like-humans-show-content-effects-on-reasoning.ingest.md` — **KEPT**. Both studies address how linguistic framing/content affects reasoning. Steen et al. shows metaphor framing effect was actually exposure effect under proper controls; Lampinen et al. shows LLMs exhibit human-like content effects. Thematic overlap is strong; connection is comparative.

### Agent-memory-systems collection

**Titles + body search** — `rg -n "metaphor" kb/agent-memory-systems/ --glob "*.md"` — only OS metaphor mentions (MemoryOS, OpenViking filesystem metaphor). No cognitive science metaphor framing content. **SKIPPED** — no plausible match for destination trigger.

### Agentic-systems collection

**Titles + body search** — `rg -n "metaphor" kb/agentic-systems/ --glob "*.md"` — no hits. **SKIPPED** — no plausible match.

### External destination

**Status:** Reserved for already-known external targets, not prospecting surface. No external target supplied by user or present in loaded context. **SKIPPED.**

## Connections Found

### To sources collection

- [language-models-like-humans-show-content-effects-on-reasoning.ingest.md](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) — **compares-with**: Both studies investigate how linguistic framing/content affects reasoning outcomes. Steen et al. (crime as beast/virus) shows that the originally-reported metaphor framing effect was actually an exposure effect when proper controls were added (non-metaphorical condition, pre-exposure measures, removing supporting metaphors). Lampinen et al. shows LLMs exhibit human-like content effects on reasoning tasks (syllogisms, NLI, Wason). Together they illustrate the complexity of evaluating framing effects and the importance of controlled experimental design when attributing reasoning changes to specific linguistic mechanisms. The Steen study provides a cautionary tale for the Lampinen findings: content effects are real, but attributing them to specific mechanisms requires ruling out alternative explanations.

### To theory collection

- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **is-evidence-for**: The Steen et al. study provides a concrete worked example for this note's methodology. The original Thibodeau & Boroditsky finding appeared to show metaphor framing affects policy reasoning; Steen et al.'s controlled replication showed the effect was actually exposure to crime information, not metaphor-specific. This demonstrates exactly the per-convention failure-mode testing the note advocates: when evaluating whether a cognitive phenomenon transfers or informs system design, test whether alternative explanations account for the observed effect before accepting the original claim.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design.md](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **is-evidence-for**: The Steen et al. findings illustrate the per-convention evaluation methodology this note advocates. The original metaphor framing claim was evaluated against alternative explanations (supporting metaphors in the text, absence of non-metaphorical control, no pre-exposure baseline), revealing it was an exposure effect rather than a metaphor-specific effect. This is a case where a cognitive science claim required careful controls before its implications could be assessed — relevant to the note's argument that "each convention needs individual evaluation: what specific problem does this convention solve, and does the LLM agent have the same problem?"

- [first-principles-reasoning-selects-for-explanatory-reach-over.md](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **see-also**: The Steen et al. study is a concrete illustration of the adaptive-fit vs explanatory-reach distinction. Thibodeau & Boroditsky found an effect that worked in their experimental setup (adaptive fit); Steen et al. showed this was an experimental confound (supporting metaphors, no control condition) rather than a generalizable mechanism (explanatory-reach). A useful pointer for readers of the explanatory-reach note who want a concrete worked example of why distinguishing adaptive fit from mechanism matters.

### To reference collection

None found. The reference collection holds system documentation, ADRs, and architecture decisions — no natural landing points for a cognitive science methodology paper.

## Bidirectional Candidates

- [language-models-like-humans-show-content-effects-on-reasoning.ingest.md](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) <-> [when-do-natural-language-metaphors-influence-reasoning.md](../../../../sources/.snapshots/when-do-natural-language-metaphors-influence-reasoning.md) — **complementary**: The Lampinen ingest could benefit from a forward link to this Steen et al. source as a related study on framing effects. The Lampinen paper studies content effects in LLMs; Steen et al. studies framing effects in humans and provides methodological lessons about controls. Either direction is useful; the sources collection outbound rules permit `compares-with` for source-to-source links.

## Reverse-edge Candidates

- [human-writing-structures-transfer-to-llms-because-failure-modes.md](../../../../theory/human-writing-structures-transfer-to-llms-because-failure-modes.md) → this source — **evidence**: This theory note cites Lampinen et al. as evidence for LLM-human failure-mode overlap. Adding this Steen et al. source as additional evidence would strengthen the note's worked example of the failure-mode methodology: it shows a case where an apparent cognitive effect (metaphor framing) was defeated by a better-controlled experiment. The note's own COLLECTION.md (theory) authorizes `is-evidence-for` → theory links from sources.

- [human-llm-differences-are-load-bearing-for-knowledge-system-design.md](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → this source — **evidence**: This note argues for per-convention evaluation of cognitive science claims. Steen et al. is a worked example: a high-profile cognitive science finding (metaphor framing effects) that did not survive improved experimental controls. Adding this source would provide a tangible case study for the note's methodological argument.

## Off-authorisation Candidates

None. All candidates that passed the articulation test had an authorised label available from the sources COLLECTION.md.

## Raw Text Candidates

None. The source snapshot has frontmatter and is a classified scientific paper.

## Rejected Candidates

- `prompt-ablation-converts-human-insight-to-deployable-framing.md` (theory) — **rejected**: Thematically adjacent (both about "framing" affecting outcomes) but operates in a fundamentally different domain. The prompt ablation note is about designing LLM prompt framings to elicit specific reasoning behaviors; Steen et al. is about whether natural-language metaphor framing causally affects human policy reasoning. The connection would be "both involve framing" which fails the articulation test — an agent gains nothing concrete by following this link.

- `reasoning-production-is-not-reasoning-evaluation.md` (theory) — **rejected**: About evaluation methodology (can a model evaluate reasoning validly?), not about how framing/content affects reasoning. Keyword overlap on "reasoning" is insufficient.

- Any agent-memory-systems or agentic-systems candidate — **rejected**: No plausible match for destination trigger. These collections are about agent architectures and memory systems, not about cognitive science experiments on metaphor framing.

## Index Membership

None proposed. The source is a specific experimental study; it doesn't define an indexable topic that would aggregate multiple artifacts.

## Synthesis Opportunities

- **Framing effects across human and LLM reasoning**: Steen et al. (humans, metaphor framing, exposure confound) + Lampinen et al. (LLMs, content effects, chain-of-thought mitigation) together suggest a research question: do LLMs exhibit the same vulnerability to metaphor framing that humans were thought to exhibit, and do proper controls (like Steen et al.'s) change the picture? Neither study tests this directly. A future synthesis note could explore whether the Steen et al. methodological critique applies to how we evaluate LLM framing susceptibility.

## Maintenance Observations

- **Missing ingest**: This snapshot has no matching `.ingest.md`. The source is captured (DOI, full text, capture date) but the durable analysis surface that would carry outbound connections doesn't exist yet. A future ingest creation would be the natural point to add the connections identified in this report.

- **No existing citations**: Neither Thibodeau & Boroditsky (2013) nor Steen et al. (2014) are cited anywhere in the KB. The specific debate about metaphor framing effects is not currently represented.

## Flags

- **Split candidate? No.** The source makes one central claim (metaphor framing effect was an exposure effect; boundary conditions needed for when metaphors influence reasoning) across four experiments. It does not make independent assertions across multiple topic areas.

- **No-connections finding? No.** Genuine connections exist to the content-effects source ingest and to theory notes on cognitive science transfer methodology.

---

*Report generated by cp-skill-connect. This report is gitignored and regenerable from the source artifact plus current KB state.*
