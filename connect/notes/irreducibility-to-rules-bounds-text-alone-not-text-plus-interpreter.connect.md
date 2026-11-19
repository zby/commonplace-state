---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/irreducibility-to-rules-bounds-text-alone-not-text-plus-interpreter.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Naur's retained passages do not establish a human-only theory bearer

**Source:** [Naur's retained passages do not establish a human-only theory bearer](../../../../notes/naur-equates-machine-execution-with-formulated-criteria.md)

## Discovery Trace

**Source contract and existing-edge scan:**

- Read `kb/notes/COLLECTION.md`. It authorises local prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; excludes `kb/work/`; and authorises already-known `external` targets without making the web a prospecting surface. Labels were filtered per destination. Because note-to-instruction links are exceptional and the usual direction is `instruction -> note` via `rests-on`, instructions also received a reverse-edge pass under `kb/instructions/COLLECTION.md`.
- `rg -n 'irreducibility-to-rules-bounds-text-alone-not-text-plus-interpreter|Naur.s retained passages do not establish a human-only theory bearer' kb/ --glob '*.md'` found existing inbound edges from [Theory-mediated self-improvement needs both interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md), and [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md). The source already links back to all three, so they were followed but not proposed again.

### `kb/notes/`

- **Curated heads read:** `kb/notes/README.md`, `kb/notes/foundations-README.md`, and `kb/notes/context-engineering-README.md`. Neither tag head declares `complete: true`, so no by-tag search was skipped.
- **Full title surface:** `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` generated 366 titles. The scan surfaced the semantic-work, evidence-scope, human-allocation, interpreter, and retained-rationale clusters.
- **Description listings:** `rg '^description:' kb/notes/ --glob '*.md' | sort`; `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; and the same by-tag command with `context-engineering`. [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md), [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md), [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md), and [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) survived full reads and the articulation test.
- **Body searches:** `rg -n -i 'Naur|Programming as Theory Building|theory-holder|theory bearer' kb/notes/ --glob '*.md'`; `rg -n -i 'text[- +]plus[- +]interpreter|application judgment|world-sensitive|limited (set|list) of (criteria|rules)|program theory' kb/notes/ --glob '*.md'`; `rg -n -i 'decision premises|cannot (faithfully )?regenerate|unregenerable|retain(ed|ing)?.*(rationale|reason|premise)|recover.*premise' kb/notes/ --glob '*.md'`; and `rg -n -i 'human[- ]only|human exclusivity|substrate-neutral|only (a )?human|human.*(bear|capacity|judg)' kb/notes/ --glob '*.md'`. [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) was rejected because natural-language ambiguity does not entail Naur's world-side novel-case judgment. [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../notes/llm-executed-methodologies-are-metacircular-interpreters.md) was rejected because successful artifact consumption does not establish program-specific theory acquisition. [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) was rejected as a useful but redundant downstream generalisation already reached through the source's design-rationale connection.

### `kb/types/`

- Read `kb/types/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'` (10 titles).
- The surface contains structural contracts, while the only authorised source-to-types relation is `evidenced-by`. No type contract could corroborate or bound the source-reading claim, so description/body prospecting was skipped for lack of a plausible trigger.

### `kb/reference/`

- Read `kb/reference/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (151 titles).
- Ran `rg '^description:' kb/reference/ --glob '*.md' | rg -i 'interpret|rationale|premise|theor|human|judg|rule|specification|artifact|retention'`, `rg -n -i 'Naur|Programming as Theory Building|text[- +]plus[- +]interpreter|theory-holder|theory bearer|world-sensitive judgment|human exclusivity' kb/reference/ --glob '*.md'`, and `rg -n -i 'decision premises|cannot (faithfully )?regenerate|unregenerable|design rationale|retained (text|artifact).*interpreter' kb/reference/ --glob '*.md'`.
- [ADR 077](../../../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md), [Content routing](../../../../reference/content-routing.md), and [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) apply the recovery distinction in Commonplace. They were rejected as direct targets because the source already reaches their theoretical owner through its design-rationale link; the current-system documents add no independent evidence about Naur's bearer inference.

### `kb/agent-memory-systems/`

- Read `kb/agent-memory-systems/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (173 titles).
- Ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg -i 'interpret|rationale|premise|theor|human|judg|rule|specification|artifact|retention|world'`, `rg -n -i 'Naur|Programming as Theory Building|theory-holder|theory bearer|text[- +]plus[- +]interpreter|world-sensitive|program-specific' kb/agent-memory-systems/ --glob '*.md'`, and `rg -n -i 'retained (text|artifact).*(interpret|judg)|interpreter.*retained (text|artifact)|decision premises|cannot regenerate|design rationale' kb/agent-memory-systems/ --glob '*.md'`.
- No direct Naur or theory-holder match survived. [memwiki](../../../../agent-memory-systems/reviews/memwiki.md) was evaluated as a concrete retained-Markdown-plus-host-agent architecture, but its review finds no faithfulness or behavioral test; it does not show that the host acquires or reliably exercises a particular program theory. [Closure-SDK](../../../../agent-memory-systems/reviews/Closure-SDK.md) requires code-mediated interpretation of retained algebraic artifacts, but that representational fact does not bear on human exclusivity or world-sensitive application judgment.

### `kb/agentic-systems/`

- Read `kb/agentic-systems/README.md`; ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (12 titles), `rg '^description:' kb/agentic-systems/ --glob '*.md'`, and `rg -n -i 'Naur|Programming as Theory Building|theory-holder|text[- +]plus[- +]interpreter|world-sensitive|decision premises|design rationale|retained (text|artifact).*interpret' kb/agentic-systems/ --glob '*.md'`.
- No body match survived. [Exo](../../../../agentic-systems/reviews/exo.md) was followed from the source's existing theory-mediated neighbor: it demonstrates a running artifact-mediated reflective loop, but its build/test/liveness oracles do not assess Naur's world-side modification capacity. It therefore remains useful one hop away rather than a direct target.

### `kb/sources/`

- Read `kb/sources/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' | sort` (312 titles).
- Ran `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'Naur|theory.build|interpret|rationale|premise|human.only|world-sensitive|artifact.*memory|knowledge.*reason|retained.*text|specification.*wrong'`, `rg -n -i 'Naur|Programming as Theory Building|theory-holder|theory bearer|world-sensitive|human exclusivity|limited (set|list) of (criteria|rules)' kb/sources/ --glob '*.md'`, and `rg -n -i 'text[- +]plus[- +]interpreter|retained (text|artifact).*(interpret|judg)|interpreter.*retained (text|artifact)|program-specific (ability|theory|competence)' kb/sources/ --glob '*.md'`.
- The already-linked [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) was followed and not duplicated. [Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) survived: its billing case supplies a contemporary world-premise example, while its ingest explicitly rejects the stronger inference that code and documentation can never carry theory. [Intention Is All You Need](../../../../sources/intention-is-all-you-need-2022428696595108152.ingest.md) was rejected because its artifact-plus-interpreter reading is local synthesis resting on the already-linked theory-mediated note. [Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) was rejected as direct evidence: it demonstrates an implemented text-plus-runtime architecture, but its benchmark ablations test task performance and evaluator alignment, not acquisition of Naur's program-specific theory or dispositional reliability.

### `kb/instructions/` and reverse-edge pass

- Read `kb/instructions/README.md` and `kb/instructions/COLLECTION.md`; ran `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` (48 titles), `rg '^description:' kb/instructions/ --glob '*.md' | rg -i 'ground|source|evidence|interpret|rationale|premise|human|judg|rule|specification'`, and `rg -n -i 'Naur|Programming as Theory Building|theory-holder|text[- +]plus[- +]interpreter|world-sensitive|human exclusivity|decision premises|cannot regenerate' kb/instructions/ --glob '*.md'`.
- The semantic grounding and unwarranted-scope gates operationalise general evidence-scope rules. Their direct theoretical owner is the claim-granular warrant note, not this source-bounded Naur reading. Under the instruction collection's exceptional-link posture, no `rests-on` reverse edge survived.

### `external`

- The notes contract authorises already-known external targets, but external is not a prospecting surface. No user-supplied external target was present, and the relevant Naur and Answer.AI materials have tracked ingests, so open-web prospecting was skipped.

**Link following:**

- Followed the source's three existing neighbors and their return links. They already cover the primary source, the text/interpreter composite, and the interpreter-relative recovery test; candidate edges below add only a general semantic mechanism, a general allocation rule, an evidence-scope rule, a more specific retention consequence, or a bounded contemporary case.
- Followed the kept notes' one-hop neighborhoods. The semantic-work note led to codification and rule-ready signals; the human-analogy note led to target-side allocation tests; the warrant note led to scope and grounding gates; and the specific-intent note led back through the source's existing design-rationale and theory-mediated neighbors. These paths confirmed that the kept candidates add distinct reader value rather than duplicate one another.

## Connections Found

- [Semantic work can be relocated but not eliminated](../../../../notes/semantic-work-can-be-relocated-but-not-eliminated.md) -- **mechanism**: the required application judgment is a semantic-work placement case; retained text can supply premises without eliminating the unresolved case-specific judgment, which remains with the interpreter.
- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) -- **exemplifies**: the Naur reading is a concrete instance where identifying a needed function and its human contributor does not by itself fix the bearer boundary for an engineered system.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- **exemplifies**: the retained passages warrant a scoped capacity requirement and Naur's named contributor, but not the stronger universal claim that no nonhuman bearer can meet the requirement.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- **extends**: develops the source's open text/interpreter division into a testable priority claim about which retained premises may help a fresh interpreter, while preserving contingent facts and accurate judgment as separate requirements.
- [Ingest: Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) -- **evidenced-by**: the billing case shows that code and static metrics can omit world-side expectations and trade-off premises, while the ingest's analysis rejects the unsupported step from that insufficiency to inherent human-only or document-impossibility conclusions.

## Bidirectional Candidates

- [Human analogies can motivate functions without determining component boundaries](../../../../notes/human-analogies-suggest-functions-not-component-boundaries.md) <-> source -- **evidenced-by** (target -> source): the Naur analysis gives the general allocation rule a worked source-reading case in which capacity, observed contributor, and engineered bearer are kept distinct.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) <-> source -- **grounds** (target -> source): the Naur analysis supplies the missing bound behind the intent conjecture—retained intent can seed judgment, but neither text nor general language competence establishes accurate program-specific theory.
- [Ingest: Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) <-> source -- **compares-with** (target -> source): the ingest's contemporary Naur application and the source note share the distinction between artifact insufficiency in one case and the stronger claim that no artifact-plus-interpreter system could bear the required understanding.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- natural-language specs admitting multiple projections is not the same limit as a fully understood demand still requiring world-sensitive similarity judgment; a direct mechanism edge would conflate ambiguity with application judgment.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) -- genuinely shares the interpreter-relative recovery boundary, but the source's existing design-rationale edge already supplies that route more directly.
- [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../notes/llm-executed-methodologies-are-metacircular-interpreters.md) -- establishes that models can execute retained natural-language methodology, not that they acquire and reliably exercise a particular program theory.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../notes/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) -- no contradiction exists: the source denies that the retained passage proves human exclusivity while explicitly leaving bearer-specific competence differences open; the broad dual-audience note adds no sharper premise.
- [Content routing](../../../../reference/content-routing.md) -- applies the recovery criterion in Commonplace but is downstream system state already reachable through the source's design-rationale connection.
- [memwiki](../../../../agent-memory-systems/reviews/memwiki.md) -- demonstrates a retained-Markdown-plus-host-agent allocation, but has no faithfulness or behavioral test and therefore does not bear on program-specific theory possession.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- demonstrates artifact-mediated self-revision, but its acceptance oracles do not test Naur's theory-holder capabilities; it remains correctly reachable through the existing theory-mediated note.
- [Ingest: Natural-Language Agent Harnesses](../../../../sources/natural-language-agent-harnesses.ingest.md) -- demonstrates a text-plus-runtime architecture and evaluator-aligned performance effects, but not the program-specific acquisition or dispositional reliability required by the source.
- [Ingest: Intention Is All You Need](../../../../sources/intention-is-all-you-need-2022428696595108152.ingest.md) -- its text/interpreter account is local synthesis dependent on an already-linked note rather than independent evidence.
- [Grounding alignment](../../../../instructions/review-gates/semantic/grounding-alignment.md) -- the procedure checks citation-to-claim fit generally; its meta-reader theory belongs at the claim-granular warrant note, so a source-specific `rests-on` edge would violate the instruction collection's shallow, exceptional-link posture.

## Index Membership

- [Foundations](../../../../tags/foundations-README.md) -- the source supplies a foundational inference boundary: an argument that rules cannot replace a capacity does not identify every possible bearer of that capacity.
- [Context engineering](../../../../tags/context-engineering-README.md) -- the source separates what retained context may supply as premises from the semantic competence and case-by-case judgment its consumer must still provide.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
