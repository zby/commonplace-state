---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/acceptance-gate-language-bounds-what-a-reflective-loop-can-reach.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Natural-language candidate admission before formalization

**Source:** [Admitting nonbinding natural-language candidates lets criticism precede formalization](../../../notes/acceptance-gate-language-bounds-what-a-reflective-loop-can-reach.md)

## Discovery Trace

**Source reading:**

- Read the source completely. Its current claim is about direct admission and evaluation order, not an unconditional bound on semantic reach: a formal-only gate can receive a translated surrogate, but the mapping must preserve adoption-relevant consequences and needs its own warrant. Natural-language admission lets criticism start before that translation is trusted. Prototype cost depends separately on authority, downstream coupling, sunk cost, and rollback.
- Its existing links already cover proposal-selection stages, representational form, oracle domain, the Gödel-machine limiting case, premise-level reflection, theory-mediated learning, Commonplace's worked pathway, codification and entrenchment, false-positive acceptance, formal proof/model correspondence, exact implementation, codify-and-relax, Eigenius, and DiscoverPhysics. Those links seeded traversal but were not proposed again.

**Curated heads and collection rules:**

- Read the source contract at [notes/COLLECTION.md](../../../../notes/COLLECTION.md) and the destination heads for [notes](../../../../notes/README.md), [types](../../../../types/README.md), [reference](../../../../reference/README.md), [agent-memory systems](../../../../agent-memory-systems/README.md), [agentic systems](../../../../agentic-systems/README.md), [sources](../../../../sources/README.md), and [instructions](../../../../instructions/README.md).
- Read the three tag heads matching the source: [foundations](../../../../tags/foundations-README.md), [self-improving systems](../../../../tags/self-improving-systems-README.md), and [constraining](../../../../tags/constraining-README.md). None declares `complete: true`, so the tag heads did not replace by-tag search.
- Read [instructions/COLLECTION.md](../../../../instructions/COLLECTION.md) before assessing a possible reverse `rests-on` edge and [sources/COLLECTION.md](../../../../sources/COLLECTION.md) before assessing return `is-evidence-for` edges.

**Complete title, description, and tag surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over every authorized local destination. The title surfaces contained 366 entries in notes, 10 in types, 151 in reference, 173 in agent-memory systems, 12 in agentic systems, 312 in sources, and 48 in instructions.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over every authorized local destination. The description surfaces contained 363 matches in notes, 13 in types, 150 in reference, 171 in agent-memory systems, 10 in agentic systems, 312 in sources, and 100 in instructions; repeated template descriptions account for counts above artifact counts.
- Ran by-tag file searches for `foundations`, `self-improving-systems`, and `constraining`, then listed matching descriptions. Notes returned 66, 42, and 31 files; reference returned 4, 2, and 1; agentic systems returned 0, 4, and 0; sources returned 1, 0, and 0; types, agent-memory systems, and instructions returned zero for all three tags.

**Focused body search:**

- Notes: ran `rg -n -i "admissib|direct admission|formal-only|preformal|formaliz" kb/notes/ --glob '*.md'`, `rg -n -i "translat.*(preserv|faithful|consequence)|surrogate|cross-form|re-expression" kb/notes/ --glob '*.md'`, `rg -n -i "nonbinding|low-authority|prototype.*(authority|coupling|cheap)|criticis.*before" kb/notes/ --glob '*.md'`, and `rg -n -i "proof.*(premise|world|interpret)|model-to-world|formal validity|warrant target" kb/notes/ --glob '*.md'`. These searches produced the translation-placement, evidence-granularity, reflective-substrate, cross-form-governance, and consumption-force candidates retained below.
- Types: ran `rg -n -i "representational form|natural-language|symbolic|gate|proof|formal" kb/types/ --glob '*.md'`. Hits defined artifact and review protocols rather than adding a claim or case that passed the articulation test.
- Reference: ran `rg -n -i "admissib|formaliz|proof[- ]gate|prototype stage|natural-language.*symbolic|symbolic.*natural-language|codif|oracle domain" kb/reference/ --glob '*.md'`. The unadopted bidirectional-codification comparison was retained only as `see-also`.
- Agent-memory systems: ran `rg -n -i "formaliz(e|ed|ation|able)|proof[- ]gate|proof gate|unformalized|admissible language"`, `rg -n -i "natural-language.*symbolic|symbolic.*natural-language|codif|prototype stage|criticism-gated"`, and `rg -n -i "acceptance gate|adoption gate|reject.*candidate|candidate.*reject|promotion gate|evaluation gate"` over `kb/agent-memory-systems/ --glob '*.md'`. Secure LLM-Wiki and SkillNote expose low-authority or staged artifacts, while Decapod exposes proof gates, but none establishes the source's pre-translation criticism claim.
- Agentic systems: ran `rg -n -i "proof|formaliz|acceptance gate|evaluation gate|natural-language.*symbolic|symbolic.*natural-language|codif|self[- ]modif" kb/agentic-systems/ --glob '*.md'`. Eigenius is already linked; Exo, Autogenesis, and GBrain add oracle, mutation, or codification cases without a distinct direct-admission result.
- Sources: ran `rg -n -i "admissib(le|ility)|formal[- ]only|proof[- ]gate|proof gate|unformalized|formaliz(e|ed|ation|able)"`, `rg -n -i "prototype stage|natural-language prototype|cheap(ly)? (reject|revis|edit)|theory building|model[- ]to[- ]world|translation fidelity|correspondence"`, and `rg -n -i "acceptance gate|adoption gate|candidate.*evaluat|evaluat.*candidate|reject-capable|proposal[- ]selection"` over `kb/sources/ --glob '*.md'`. DreamCoder and Knowledge-Centric Self-Improvement supplied the strongest complementary cases.
- Instructions: ran `rg -n -i "admissib|formaliz|proof[- ]gate|prototype stage|natural-language.*symbolic|symbolic.*natural-language|codif|oracle domain"` and `rg -n -i "stabiliz|stable pattern|repeat(ed|ing)|codif|symbolic|formaliz|natural-language"` over `kb/instructions/ --glob '*.md'`. The closest hit, [Analyse an External System's Epistemic Architecture](../../../../instructions/analyse-external-system-epistemic-architecture.md), independently requires separating formal validity from fidelity to source or world; it does not depend on this source's reflective-loop or evaluation-order claim.
- Backlinks: ran `rg -n "acceptance-gate-language-bounds-what-a-reflective-loop-can-reach|admissible language|prototype stage|formal-only gate|relaxed Gödel machine" kb/ --glob '*.md'`. The only library backlink is the bitter-lesson portfolio entry described under Maintenance Observations.

**Candidate evaluation and link following:**

- Followed [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) through codification, frontloading, and rule-based selection. It supplies the residual semantic-work mechanism: faithful translation may relocate evaluation prerequisites upstream, but formal construction and checking do not themselves discharge the mapping judgment.
- Followed [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) through representational form and proof-based warrant. It states directly that proof warrants consequences inside a chosen translation, not source claims the translation omitted or changed.
- Followed [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) through the general theory-mediated-learning conjecture, reach assessment, retained-premise reflection, and the formal symbolic case. It establishes why unformalized theories about a system's own operation create the reflective setting the source analyzes.
- Followed [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) through reflective coverage, the Commonplace reference case, same-form theory-to-methodology promotion, and Knowledge-Centric Self-Improvement. It develops the governance burden when a retained prototype is later codified or its formal mapping is revised.
- Followed [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) through false-positive acceptance, behavioral authority, and rollback. It grounds the source's qualification that prose versus symbols does not determine prototype standing; force comes from authority and consumption paths.
- Followed [DreamCoder](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) into the proposal-selection, Gödel-machine, and reflective-coverage neighborhood. Its mechanically gated symbolic abstractions are the clearest bounded formal comparison, not evidence that formal form alone confers high authority.
- Followed [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) into proposal selection, addressability, oracle domain, and cross-form coverage. Its source-side analysis explicitly traces challenge, splitting, rejection, and distillation of natural-language claims before later consumption.
- Rejected reflective coverage as a direct edge because the cross-form-boundary note applies it more specifically; progressive constraining because the source now rules out a mandatory or always-persistent preformal interval; and candidacy evidence because evidential routing is not representational admission. Rejected Secure LLM-Wiki, SkillNote, Decapod, Exo, Autogenesis, GBrain, the Gödel-machine ingest, the “LLMs can't jump” ingest, and the theory-building-work ingest for the collection- or mechanism-specific reasons recorded below.

**External prospecting:**

- Skipped. No user-supplied external target or newly loaded external context required evaluation, and open-web prospecting is outside this skill.

## Connections Found

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) — **grounds**: faithful translation can move the semantic judgment ahead of a formal-only gate, but construction, proof, and checking do not make the judgment about preserved meaning disappear.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) — **grounds**: a proof over a formal surrogate warrants entailed consequences in the chosen translation, not any source commitment that the translation omitted or altered.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — **grounds**: it identifies unformalized, retained theories about a system's own operation as the reflective setting in which a semantic interpreter can begin criticism before a supplied formal language exists.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) — **extends**: it carries the source's later-codification path into a governance requirement to represent the natural-language artifact, the symbolic artifact, and the mapping that transfers or re-grounds responsibility.
- [A consumption channel delivers force without the history that earned it](../../../../notes/a-consumption-channel-delivers-force-without-the-history-that.md) — **grounds**: it explains why prototype standing cannot be inferred from prose or symbolic form alone: a consumption path can confer operative force unless authorization, version, use, and rollback are governed.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) — **see-also**: the unadopted four-arm proposal would compare natural-language-only, symbolic-only, one-way promotion, and bidirectional regimes, directly testing whether a preformal criticism interval helps under different translation costs; it supplies no result yet.
- [DreamCoder: growing interpretable knowledge with wake-sleep Bayesian program learning](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) — **evidenced-by**: DreamCoder retains mutable symbolic abstractions under a mechanical description-length gate, bounding the source with a formal-semantic case in which formal artifacts remain revisable learning objects rather than necessarily entrenched commitments.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — **evidenced-by**: its forums admit natural-language claims that agents challenge, split, reject, and distill before later consumption, instantiating criticism of nonbinding prose before any symbolic codification step.

## Bidirectional Candidates

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) ↔ source — **extends**: from that note's side, this source refines its unformalized-self-theory case by separating direct admission, faithful upstream translation, criticism, and operative authority.
- [Moving the interpretation–enforcement boundary requires cross-form coverage](../../../../notes/moving-the-interpretation-enforcement-boundary-requires-coverage.md) ↔ source — **extends**: from that note's side, this source supplies the low-authority pre-crossing stage and shows that a translation may preserve reach without eliminating the need to govern the mapping.
- [DreamCoder: growing interpretable knowledge with wake-sleep Bayesian program learning](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) ↔ source — **is-evidence-for**: the ingest's formal-semantic retention case materially bears on the source's boundary that symbolic form can remain a cheap prototype when construction, coupling, and authority permit it.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) ↔ source — **is-evidence-for**: the ingest's traced natural-language challenge, revision, rejection, and retention pathway materially bears on the source's preformal-criticism claim.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) — rejected as indirect: it supplies the general coverage axis, while the retained cross-form-boundary candidate states the specific mapping and governance consequence useful here.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — rejected: its convention-to-enforcement trajectory invites the stronger reading that a preformal interval is generally required, whereas the source now allows an interval to shrink or disappear when faithful translation is cheap and reliable.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) — rejected: it separates evidential roles in staged assessment, not the representational forms a gate can evaluate directly.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md) — rejected: it concerns same-form promotion into binding natural-language methodology, while the source explicitly confines its candidate stage to nonbinding theories and the consumption-channel note supplies the relevant authority mechanism more directly.
- [Secure LLM-Wiki](../../../../agent-memory-systems/reviews/secure-llm-wiki.md) and [SkillNote](../../../../agent-memory-systems/reviews/skillnote.md) — rejected: their low-authority candidates are imported atomic claims or executable procedures; neither establishes criticism of an unformalized theory or a translation-fidelity boundary.
- [Decapod](../../../../agent-memory-systems/reviews/decapod.md) — rejected: its proof gates govern workunit transitions and proof plans rather than accept only formalized theory candidates.
- [Exo](../../../../agentic-systems/reviews/exo.md), [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md), and [GBrain](../../../../agentic-systems/reviews/gbrain.md) — rejected: they add oracle-strength, mutation-scope, admission-polarity, or codification-placement cases without establishing when evaluation can start relative to theory translation.
- [Gödel Machines — Provably Optimal Self-Improvements](../../../../sources/goedel-machines-schmidhuber.ingest.md) — rejected as redundant: the source already links the local Gödel-machine note that interprets the proof-governed case at the needed level.
- [LLMs can’t jump](../../../../sources/llms-cant-jump.ingest.md) — rejected: it bears on search reach and iterative refinement, not on the gate's direct-admission language.
- [A new Era Of Theory-Driven AI Research](../../../../sources/a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md) — rejected: it supplies an anecdotal case for cheaper theory work but does not compare evaluation before and after formalization or establish translation fidelity.
- [Analyse an External System's Epistemic Architecture](../../../../instructions/analyse-external-system-epistemic-architecture.md) — rejected as a reverse edge: its formal-validity/fidelity guard is broader and does not rest specifically on this source's reflective-loop and evaluation-order claim.

## Index Membership

- [constraining](../../../../tags/constraining-README.md) — the source distinguishes optional low-authority preformal criticism from later codification and explains when cheaper translation can shorten or eliminate that interval.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) — the source adds direct-admission language as a loop boundary distinct from search range and oracle domain while making semantic reach conditional on translation paths.

## Synthesis Opportunities

None

## Maintenance Observations

- [The bitter-lesson defense portfolio](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) still summarizes this source under its former title and says that a gate must admit candidates before they can be formalized and that cheaper formalization cannot remove the prototype stage. The revised source now permits a faithfully translated surrogate upstream and says the preformal interval may disappear when translation is cheap and reliable, so the portfolio row is stale.

## Flags

None
