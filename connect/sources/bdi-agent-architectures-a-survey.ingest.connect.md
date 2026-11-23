---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/bdi-agent-architectures-a-survey.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: BDI Agent Architectures: A Survey (de Silva, Meneguzzi and Logan, IJCAI-20)

**Source:** [Ingest: BDI Agent Architectures: A Survey](../../../../sources/bdi-agent-architectures-a-survey.ingest.md)

The ingest already authors ten outbound edges: five sources (Wooldridge and Jennings, SEP practical reason, Soar chunking, Russell and Wefald, Suchman 1985) and five theory notes (goal-holding interpreter, backtracking, failure explanation, skills as routing, methodology selection). All ten resolve. This report adds candidates that the occasion makes relevant. The occasion asks whether a BDI architecture learns or revises its plans, by what keep/drop rule, and whether that rule is bound to one fixed measure. It also covers reverse edges, which do not exist yet: no artifact outside the reports links to this ingest.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. No external target was supplied, so external prospecting was skipped. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). For reverse edges, `kb/theory/COLLECTION.md` authorises `evidenced-by`, `abstracted-from` and `see-also` toward sources. The `kb/theory/COLLECTION.md` rule "Origin is not corroboration" requires an `evidenced-by` context phrase to say that the evidence qualifies or bounds the claim unless it tested the claim.

**Prior discovery reused:** `kb/reports/state/connect/sources/bdi-agent-architectures-a-survey.connect.md` (a connect run on the snapshot before the ingest existed). Its kept candidates were checked against the ingest. Eight of its eleven outbound candidates were authored. It also proposed `agent-runtime-analysis-should-separate-scheduling-context-state` and Voyager, which were not authored and are re-evaluated below. Its rejections of the Fishkin and Minton-adjacent sources were made before the ingest's occasion was known, so they were re-evaluated.

**Existing-link check:** a loop with `test -f` over the ten linked paths showed that all of them resolve.

**Curated heads:**
- `kb/tags/method-guided-action-README.md` (`complete: true`; the source's own tag). By-tag `rg` was skipped. Its selection entries are already linked (`capable-agents-need-methodology-selection`). `theory-and-methodology-form-a-two-layer-execution-system` was considered: BDI has no live-theory fallback layer, so it was rejected.
- `kb/tags/learning-theory-README.md` (`complete: true`) and `kb/tags/goal-prioritization-README.md` were read for Index Membership.

**Titles listing (theory):**
- `ls kb/theory | grep -i -E 'deliberat|learn|retry|fallback|applicab|precondition|trigger|routing'`. Flagged: `learning-inside-a-fixed-decomposition-inherits-its-mistakes`, `memory-management-policy-is-learnable-but-oracle-dependent`, `factory-learning-is-experience-responsive-retention-that-improves`, `continual-learning-requires-governing-behaviour-changing-writes`, `agent-statelessness-makes-routing-architectural-not-learned`, `llm-debugging-starts-with-retry-versus-rewrite-triage`, `diagnostic-richness-constrains-outer-loop-learning-quality`, `silent-disambiguation-is-the-semantic-analogue-of-tool-fallback`. I read their descriptions. I read the full body of `learning-inside-a-fixed-decomposition...` and the opening of `memory-management-policy...`.
- `ls kb/theory/definitions/`: no `deliberat*` definition. The deliberative-learning term lives only in `kb/work/` (excluded).

**Body search:**
- `rg -n '\bBDI\b|Bratman|belief-desire|plan library|plan-rule|context condition|means-ends' . --glob '!work/**' --glob '!reports/**'` found only the sibling sources `sep-practical-reason` and `wooldridge-jennings`. Other hits were substring noise.
- `rg -l -i 'deliberative learning' . --glob '!work/**' --glob '!reports/**'` found the four occasion siblings: `sep-practical-reason`, `wooldridge-jennings`, this ingest and `fishkin-mansbridge-deliberative-democracy-intro`.
- `rg -l 'learning-method-name' sources/` returned the same four ingests, which confirms the occasion cluster.
- `rg -n -i 'case-based|HTN|hierarchical task|STRIPS|subsumption|reactive planning|Soar|ACT-R' theory/ agentic-systems/topics sources/*.ingest.md -l` flagged `minton-utility-of-ebl-aaai88`, `skill-acquisition-compilation-weak-method-solutions` and `chunking-in-soar` (already linked).
- `rg -n 'bdi-agent' sources/ reports/state/connect/`: no inbound link to the ingest exists. All reverse edges are therefore new.

**Descriptions:**
- `rg -m1 '^description:'` over `minton-utility-of-ebl-aaai88`, `skill-acquisition-compilation-weak-method-solutions`, `introspective-multistrategy-learning`, `procedural-graphs-self-evolving-execution`, `fishkin-mansbridge-deliberative-democracy-intro` and `agent-memory-systems/reviews/voyager.md`. Minton kept: its description names an explicit retain/discard rule for learned control rules, which answers the occasion's keep/drop question in the symbolic tradition.

**Link following:**
- `minton-utility-of-ebl-aaai88.ingest.md` "Connections Found" links Soar as its "cost-blind counterpart". The three ingests (Soar, Minton, BDI) form a contrast chain on how a symbolic architecture admits learned rules.
- `learning-inside-a-fixed-decomposition...` "Relevant Notes" links `memory-management-policy...` and `diagnostic-richness...`. This confirms that the two kept learning notes sit together.
- `chunking-in-soar...ingest.md` line 36 links `learning-inside-a-fixed-decomposition`. That precedent is a same-genre source using the note for the same reason.

### Candidate origins

- kb/sources/minton-utility-of-ebl-aaai88.ingest.md — body-search, descriptions, link-following
- kb/theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md — titles, link-following
- kb/theory/memory-management-policy-is-learnable-but-oracle-dependent.md — titles, link-following
- kb/sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md — body-search, descriptions
- kb/agent-memory-systems/reviews/voyager.md — known, descriptions
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — known, body-search
- kb/sources/sep-practical-reason.ingest.md — known, body-search
- kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md — known, link-following
- kb/theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md — known
- kb/theory/backtracking-keeps-lightweight-search-control-provisional.md — known

## Connections Found

Candidates for the ingest's `Connections Found` section. They add to the existing ten edges and do not replace them.

- [Ingest: Minton 1988, the utility of explanation-based learning](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) -- **compares-with**: the axis is the rule for keeping or dropping a learned rule, which is the occasion's direct question. PRODIGY admits learned control rules by estimated utility and discards rules whose validated utility is negative. The BDI survey reports no learned plan-rules and so no keep/drop rule. Its selection measures (priority, past success rate, utility) are fixed by the programmer. With Soar, which keeps every chunk, Minton gives the ingest's Extractable Value 1 a symbolic precedent that answers the question the survey cannot.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: the only BDI learning the survey cites (Singh and Hindriks) learns context conditions for hand-written plan-rules. The trigger set, rule bodies and goal types stay fixed. That is learning inside an update space limited to applicability, so it cannot repair a missing plan-rule or a wrong goal decomposition. The axis is what the update space admits. Use `compares-with`, not `is-evidence-for`, because the survey reports no learning outcomes. The Soar ingest already uses the note the same way.
- [Feedback-trained memory management is oracle-dependent even when its operations are hand-designed](../../../../theory/memory-management-policy-is-learnable-but-oracle-dependent.md) -- **compares-with**: the note separates fixed rules, rules that respond to runtime signals with fixed parameters, and policies updated from outcomes. Only the last needs a ranking oracle. BDI plan selection fits the first two: program order and priority are fixed, and JACK's past-success-rate meta-rules respond at runtime. The keep/drop signal is binary goal achievement. The axis is whether the selection rule itself updates from outcomes. It sharpens Extractable Value 2's "fixed criterion per program" claim.
- [Ingest: Fishkin and Mansbridge, deliberative democracy introduction](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) -- **compares-with**: the axis is what "deliberation" names. The ingest's opening paragraph sets this survey among the occasion's senses of the word but omits the fourth sibling ingest from the same occasion. Fishkin and Mansbridge give the group-weighing sense. BDI gives single-agent goal selection without weighing in practice. Its Extractable Value 3 asserts exactly that gap. The snapshot-level report rejected this edge before the occasion was known; the naming occasion now makes the shared axis load-bearing.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: the axis is how a retained procedure declares applicability. Voyager retrieves learned skills by embedding similarity over generated descriptions, and the review flags missing precondition metadata. BDI plan-rules carry a context condition checked against beliefs, and re-checked after failure. This gives Extractable Value 4 (applicability as a checked condition) a concrete learned-skill-library contrast. The target collection is frozen-historical, so author this only if Extractable Value 4 is developed.

## Bidirectional Candidates

- [Ingest: Intelligent Agents (Wooldridge and Jennings)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: the Wooldridge ingest's Limitations say PRS, a BDI system, is misfiled by the deliberative/reactive split. A return link would let its reader check that against the dedicated BDI survey. The two share the naming occasion.
- [Ingest: SEP Practical Reason](../../../../sources/sep-practical-reason.ingest.md) <-> source -- **compares-with**: the SEP ingest says the entry gives little procedure for deliberation. The BDI ingest is the KB's procedural counterpart for Bratman's model, and the two share the naming occasion.
- [Ingest: Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) <-> source -- **compares-with**: from the Soar side, BDI is the architecture that leaves rule acquisition to the programmer. It is the zero-learning endpoint of the Soar–Minton–BDI contrast on how symbolic architectures acquire rules.

## Reverse-edge Candidates

- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) → source -- **evidenced-by**, phrased as *bounds*: BDI interpreters hold the triggering goal over hand-written procedures and re-route through alternative applicable plan-rules. Fail-soft re-routing therefore does not require a natural-language interpreter. The survey was not a test of the note.
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) → source -- **evidenced-by**, phrased as *qualifies*: goal-level backtracking in agent programming languages (CAN, JACK, RAE) is a worked instance. The survey's unrestorable cases, concurrent branches and executed external actions, mark the note's scope boundary.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- proposed as weak by the snapshot-level report, conditional on the ingest discussing intention scheduling. The ingest mentions scheduling only in its summary and draws no inference from it, so the condition is not met.
- [Factory learning is experience-responsive retention that improves](../../../../theory/factory-learning-is-experience-responsive-retention-that-improves.md) -- the definition is relevant to "learning", but BDI performs no experience-responsive retention in its library. The link would only restate the absence that Minton and the fixed-decomposition note already frame more specifically.
- [Continual learning requires governing behaviour-changing writes](../../../../theory/continual-learning-requires-governing-behaviour-changing-writes.md) -- BDI makes no behaviour-changing writes to its plan library, so the note has nothing to govern here.
- [Agent statelessness makes routing architectural, not learned](../../../../theory/agent-statelessness-makes-routing-architectural-not-learned.md) -- BDI routing is hand-written, but its cause is not session statelessness (BDI agents keep beliefs). The two mechanisms differ.
- [LLM debugging starts with retry-versus-rewrite triage](../../../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md), [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- the shared words (retry, fallback) cover different mechanisms. BDI re-selection is not sampling-variance triage or spec ambiguity.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- BDI has no theory fallback layer. When applicable plan-rules run out, the goal fails.
- [Diagnostic richness constrains outer-loop learning quality](../../../../theory/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- BDI has no outer learning loop whose evidence surface could be judged.
- [Skill acquisition: compilation of weak-method solutions (Anderson)](../../../../sources/skill-acquisition-compilation-weak-method-solutions.ingest.md), [Introspective multistrategy learning](../../../../sources/introspective-multistrategy-learning.ingest.md), [Procedural Graphs](../../../../sources/procedural-graphs-self-evolving-execution.ingest.md) -- adjacent rule- or procedure-learning sources. Soar and Minton already cover the acquisition and retention contrasts more directly. Procedural Graphs' validated graph revision would be the LLM-era counterpart for the occasion, but the BDI ingest makes no claim about LLM procedure revision that would need it.
- `kb/reference/` -- no shipped-system artifact concerns plan-rules, goal types or deliberation cycles.

## Index Membership

- [method-guided-action](../../../../tags/method-guided-action-README.md) -- already carried. It fits through Extractable Values 4 and 5 and the methodology-selection connection.
- [learning-theory](../../../../tags/learning-theory-README.md) -- possible. The occasion is about learning, and Extractable Values 1–2 analyse what BDI does and does not learn or revise. The analysis is mostly negative, though: the survey's only learning content is one citation. Add the tag only if the ingest gains the Minton or fixed-decomposition connections, which would make the learning analysis substantive.
- [goal-prioritization](../../../../tags/goal-prioritization-README.md) -- weak. Extractable Value 3 (goal adoption) and the priority/deadline/utility measures touch which goal gets effort, but the ingest does not analyse authority or stopping. Not recommended unless that analysis is added.

## Synthesis Opportunities

The four occasion ingests (Wooldridge and Jennings, SEP practical reason, Fishkin and Mansbridge, BDI survey) together give four senses of "deliberation": architectural, normative weighing, group weighing and computational goal selection. None of them is a learning sense. Soar, Minton and BDI together give three policies for admitting learned symbolic rules: keep all, keep by measured utility, and acquire none. Combined, the two sets imply a higher-order claim for the naming workshop: "deliberative" in its established senses names choice among given options, not the revision of the options or of the measure. Authoring belongs in `kb/work/learning-method-name/`, not in connect.

## Maintenance Observations

- The sibling occasion ingests (`wooldridge-jennings-intelligent-agents`, `sep-practical-reason`, `fishkin-mansbridge-deliberative-democracy-intro`) and this ingest do not yet link one another consistently. This ingest links two of the three. A pass over the four occasion ingests would make the "senses of deliberation" cluster navigable from any member.
- The stale snapshot-level report `kb/reports/state/connect/sources/bdi-agent-architectures-a-survey.connect.md` still says the ingest "does not exist yet". It is gitignored and regenerable, so it can be deleted or ignored.

## Flags

- Not a split candidate. The ingest makes one organising assertion about the survey, and its added connections cluster on two axes: senses of deliberation and acquisition of symbolic rules.
- Tension to keep visible: Extractable Value 2 calls BDI keep/drop "outcome-driven plan revision bound to one fixed criterion". Under the memory-management note's taxonomy, BDI selection is fixed or responds at runtime, not outcome-updated. "Revision" may overstate it. Within-goal exclusion of a failed instance is re-selection, not revision of the plan.
