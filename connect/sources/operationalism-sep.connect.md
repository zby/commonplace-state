---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/operationalism-sep.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Operationalism (SEP, Hasok Chang)

**Source:** [Operationalism (SEP)](../../../../sources/.snapshots/operationalism-sep.md)

The source is an immutable snapshot. No tracked `operationalism-sep.ingest.md` exists yet (checked `ls kb/sources | grep -i operational`). Every outbound candidate below is for the future ingest report, which is the authored surface under `kb/sources/COLLECTION.md`. Do not link the snapshot itself.

Source summary used for judging: Bridgman's operational analysis ties a concept's meaning to its measurement operations; different operations in different domains create conceptual "joints" (§1.2). The critiques (§2): operational definitions do not exhaust meaning; not every useful concept needs one; "operation" is undefined; operations may be private. Chang's reconstruction (§3): operations are units for analysing practice; operationalism regulates extending concepts into new domains (Wedgwood's pyrometry); it increases empirical content in Popper's sense; a theoretical construct is worthwhile when it mediates between two or more operationally meaningful concepts; operational analysis exposes complexity ("can always be pushed to the point where sharpness disappears").

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` outbound section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources. `kb/work/` and `kb/instructions/` are excluded. `external` is authorized only for `derived-from`/`see-also`; there is no external target already in hand besides the SEP URL itself, so external prospecting was skipped. The ingest's `derived-from` edge to `https://plato.stanford.edu/entries/operationalism/` is the ingest workflow's job, not a connect candidate.

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles) plus targeted `rg -m1 '^description:'` over candidates. Flagged: natural-language meaning as coordination, constraining, proximate target, generality-for-precision, actionable methodology, abstract-only-with-boundary, two-layer execution system.
- `kb/tags/` listing read; heads checked for `claims-and-grounding`, `constraining`, `evaluation`, `method-guided-action`.

**Body search:**
- `rg -il 'operationali[sz]|operationalism|operational definition|Bridgman' kb --glob '*.md'` -- ~200 hits, almost all the KB's own `operationalized-from` lineage relation or ordinary "operational". No artifact outside `kb/work/` discusses Bridgman or philosophical operationalism.
- `rg -n -i 'operationalism|Bridgman|operational definition|empirical content|measurement operation' kb --glob '!kb/sources/.snapshots/**' --glob '!kb/work/**'` -- "empirical content" appears only in the Popper LSD ingest (kept as a sources candidate). "Operational definition" appears in `kb/types/definition.md` and several source ingests in an everyday sense (rejected).
- `rg -l -i 'empirical content|falsif|testab|measur|proxy|goodhart|construct validity|operational meaning' kb/theory` -- 60 files. Kept: generality-for-precision (Popperian content), proximate target (proxy levels). Rejected: quality-signals (Goodhart only for link metrics).
- `rg -l -i 'hasok chang|inventing temperature|logical positiv|verificationism|hempel|quine|goodhart|construct validity'` over sources/theory/agentic-systems/agent-memory-systems -- no Chang/Hempel/positivism treatment; Goodhart hits are all metric-gaming asides.
- `rg -n -i 'out of (its )?domain|domain of application|extend(ed|ing)? (a |the )?(term|concept|claim) to|scope line|transfer to new' kb/theory` -- surfaced the two-layer execution system (effective theories with breakdown boundaries) and the generality note's scope lines.
- `rg -l -i 'operational definition|measurement' kb/agentic-systems kb/agent-memory-systems` -- 46 files, sampled: everyday usage in system reviews; no axis shared with a philosophy-of-science source. Destination skipped.
- `ls kb/sources | grep -i -E 'popper|lakatos|kuhn|gregor|peirce|dewey|pragmat'` -- Popper (LSD, C&R, 1966, 1968) and Gregor ingests found.

**Link following:**
- Constraining definition -> lists "definition notes that replace vague terms with operational meanings" as a constraining instance. That is the KB's direct use of the operationalist vocabulary.
- Natural-language-meaning note -> constraining, oracle-strength spectrum, underspecified instructions. It is the KB's nearest theory of what fixes a term's meaning.
- `kb/reference/epistemic-stance.md` -> point 3 (anti-essentialism; instruction meaning = reading a reference set of interpreters converges on) and point 4 (intersubjective testability). Both contrast with Bridgman's reductive doctrine and private-operations problem (§2.4).
- Excluded workshop read for context only: `kb/work/operationalization-executability-automation/README.md` and `exploration.md` require reading "the actual discipline's meaning" of operationalization; this snapshot appears to serve that. Not a link target.

## Connections Found

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with**: same axis (what fixes a term's meaning). Bridgman ties meaning to measurement operations and finds "joints" where operations change. The note ties meaning to checks that align approximations and predicts meaning is sharpest where correction is cheap. Bridgman's claim that a construct reachable by several independent operations is "real" parallels the note's claim that independent checks stabilize meaning.
- [Constraining](../../../../theory/definitions/constraining.md) -- **compares-with**: the definition counts "definition notes that replace vague terms with operational meanings" as constraining. The SEP critiques (§2.1 operational definitions do not exhaust meaning; §2.2 not every useful concept needs one) and Bridgman's proliferation problem (one concept per operation) name what this narrowing costs. That is the axis an ingest should state.
- [A proximate target is checked for achievement, not for warrant](../../../../theory/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **compares-with**: the note separates objective, proximate target, operational criterion and oracle. Bridgman's reductive doctrine collapses concept and measurement criterion; Chang's reading (§3.2-3.3: the concept extends beyond any one measure) keeps them apart. Shared axis: whether the measurable criterion is the concept or a stand-in for it.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- **compares-with**: both use Popper's empirical content. Chang's §3.3 reads operationalism as a strategy that increases content by keeping concepts operationally well defined. Bridgman's electron-diameter passage shows the opposite failure: concepts fuse, the number of testable relations falls, and content drops. Shared axis: how vocabulary choice changes what a claim can be tested against.
- [Popper, *Logic of Scientific Discovery* (ingest)](../../../../sources/popper-logic-of-scientific-discovery.ingest.md) -- **compares-with**: the SEP entry explicitly frames operationalism's legacy through Popper's definition of empirical content as the class of potential falsifiers. Shared axis: meaningfulness vs. falsifiability as the criterion a concept or theory must meet. Useful for the ingest to note that Commonplace inherits Popper's criterion, not Bridgman's.
- [Abstract an experience only when you can state the boundary](../../../../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **compares-with**: Bridgman's main worry was concepts extended "unthinkingly" into domains where their defining operations no longer apply (§3.2). The note's over-generalized lesson that "drops the condition clause" is the KB-side analogue. Shared axis: the conditions under which a term or lesson may be carried beyond the cases that fixed it. Chang adds a positive mechanism the note lacks: extension through overlapping operational links (Wedgwood).

## Bidirectional Candidates

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) <-> source -- **evidenced-by** (theory side, qualifies): the note's hypothesis is untested. Bridgman/Chang give an independently developed account from physics in which multiple operations make a concept stable or real. A return link would qualify or bound the hypothesis without claiming to corroborate it.

## Reverse-edge Candidates

- [Constraining](../../../../theory/definitions/constraining.md) → future `operationalism-sep.ingest.md` -- **evidenced-by** (qualifies/bounds, under `kb/theory/COLLECTION.md`): the definition's instance "replace vague terms with operational meanings" borrows the operationalist term. The SEP critique bounds how far a definition can fix a term's meaning.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../theory/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) → future ingest -- **evidenced-by** (qualifies): the note already grounds content in Popper. Bridgman's fusion-of-concepts passage is a second-discipline case where vocabulary change reduces testable relations.
- [Epistemic stance](../../../../reference/epistemic-stance.md) → future ingest -- reference-collection rules govern; plausible as a "not inherited" or contrast entry. Commonplace's convergence-based reading of instruction meaning is a cousin of operational meaning. It avoids Bridgman's reductive doctrine by fixing meaning through an intersubjective reference set rather than one person's operations (§2.4).

## Off-authorisation Candidates

- [Epistemic stance](../../../../reference/epistemic-stance.md) -- sources→reference authorizes only `see-also`. The real relation is a comparison: operational meaning vs. the stance's convergence-based meaning plus intersubjective testability. `see-also` would hide the axis. Suggest either a reverse edge authored from the stance page (above) or extending `compares-with` to `reference` in `kb/sources/COLLECTION.md`. Rejection is also reasonable, because the stance page "grows from the connections notes make to it", so inbound is the natural direction.

## Raw Text Candidates

None

## Rejected Candidates

- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- operator- and setting-relative like Bridgman's operation-relative meaning, but it concerns whether guidance can be used, not what a term means. A link would invite conflating "operational" in two senses.
- [Theory and methodology form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- its physics illustration (effective theories with breakdown boundaries) is near Bridgman's domain-limited operations, but the note is about maintenance architecture. Keyword proximity only.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- relevant only through the natural-language-meaning note, which already carries the axis. A second link is redundant.
- [Quality signals for KB evaluation](../../../../theory/quality-signals-for-kb-evaluation.md) and [oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) -- Goodhart/proxy talk is metric gaming, not concept-meaning. The proximate-target note carries the useful axis.
- [Gregor 2006 ingest](../../../../sources/the-nature-of-theory-in-information-systems-gregor-2006.ingest.md) -- theory taxonomy. No shared axis with operational meaning beyond "philosophy of science".
- [`kb/types/definition.md`](../../../../types/definition.md) -- its "One-paragraph operational definition" placeholder uses the everyday sense. Types are not an authorized sources destination either way.
- Source ingests using "operational definition" (cedar-grpo, prompt-stability, language-models-dont-always-say) -- everyday metric-definition usage. No comparison axis.
- `kb/agentic-systems/`, `kb/agent-memory-systems/` -- no target treats concept meaning or measurement theory.

## Index Membership

- [constraining tag head](../../../../tags/constraining-README.md) -- a source tag `constraining` would fit if the ingest analyzes operational definition as a way to narrow a term's interpretation and records the SEP critiques of that narrowing. Apply only if the ingest gives that substantive treatment. Source tags do not affect generated membership.
- [evaluation tag head](../../../../tags/evaluation-README.md) -- weaker. It fits only if the ingest develops the empirical-content and measurement-as-proxy material.

## Synthesis Opportunities

The KB currently has three partial accounts of what fixes a term's meaning: constraining (an artifact narrows interpretation space), natural-language meaning as coordination (checks align approximations), and the epistemic stance's convergence rule (a reference set of interpreters). Operationalism is the historical extreme of the same family, tying meaning to a single procedure. Its known failure modes are proliferation, loss of meaning beyond the measure, and private operations. Together they suggest a claim not yet stated anywhere: a check-fixed definition buys sharpness inside the check's domain and creates a joint at its edge, so extension needs overlapping checks rather than a wider definition. Do not write it from connect. It depends on the natural-language-meaning hypothesis, which is untested.

## Maintenance Observations

- Vocabulary collision risk: "operational/operationalize" already carries two KB senses. The `operationalized-from` lineage relation ([link vocabulary](../../../../reference/link-vocabulary.md)) is one; the workshop's provisional "operationalization = making K usable for T by E" is the other. The constraining definition uses "operational meanings" in a third, operationalist-adjacent sense. Psychology's operationalization (construct → measurable variable) and Bridgman's operationalism are further senses this source brings in. `kb/reference/vocabulary-collision-ledger.md` has no entry for "operational". Worth a ledger check if the ingest or workshop adopts any of these terms.
- The excluded workshop `kb/work/operationalization-executability-automation/` separates "generalizing to T'" from operationalization for T. That mirrors Chang's §3.2 point that extending a concept to a new domain needs new operational links, not just the old definition. This is consumed context for the workshop, not a link.

## Flags

- No ingest exists yet. All candidates wait on `kb/sources/operationalism-sep.ingest.md`. Re-run connect on the ingest once it is written; its analysis sections will sharpen which comparisons carry weight.
- Tension to state in the ingest, not resolve here: Commonplace's epistemic stance is Popperian, and Popper rejected meaning criteria such as operationalism's in favour of demarcation by falsifiability. Chang's §3.3 reconciles operationalism with Popperian content. An ingest that cites operationalism approvingly should say which half it takes.
- Not a split candidate: one source, one topic.
