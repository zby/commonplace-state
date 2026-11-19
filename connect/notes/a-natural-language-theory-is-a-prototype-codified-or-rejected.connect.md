---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-natural-language-theory-is-a-prototype-codified-or-rejected.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Representational form does not determine whether a theory is a prototype

**Source:** [Representational form does not determine whether a theory is a prototype](../../../../notes/prototype-standing-is-revision-cost-binding-plus-lost-investment.md)

## Discovery Trace

### Notes

**Curated heads and complete surfaces:**

- Read `kb/notes/README.md`, `tags-README.md`, `learning-theory-README.md`, `constraining-README.md`, and `self-improving-systems-README.md`. None of the three matching tag heads declares `complete: true`; `learning-theory-README.md` declares `covered_by` rather than completeness, so all three by-tag scans were run.
- Generated the complete 366-title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and the 363-entry description surface with `rg '^description:' kb/notes/ --glob '*.md'`.
- Ran `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`, plus the same command for `constraining` and `self-improving-systems`. These scans isolated the artifact-analysis, codification-decision, progressive-constraining, verifiability, cross-form-learning, and authority neighborhoods.

**Body search:**

- `rg -n -i '(prototype|cheap to (revise|reject|discard)|revision cost|rollback cost|operational coupling|downstream depend|entrench)' kb/notes/ --glob '*.md'` — confirmed that the existing entrenchment link carries replacement cost, while collection prototypes are a lexical collision. It also exposed artifact-level ephemerality notes whose subject is not theory standing.
- `rg -n -i '(codif|formaliz|symbolic|natural[- ]language|representational form).*(authority|binding|operative|depend|adopt)|(?:authority|binding|operative|depend|adopt).*(codif|formaliz|symbolic|natural[- ]language|representational form)' kb/notes/ --glob '*.md'` — kept `axes-of-artifact-analysis.md` because it explicitly separates representational form from behavioral authority. `behavioral-authority.md` was followed one hop but not kept separately because the axes note already routes to the definition and adds the needed independence claim.
- `rg -n -i '(accept|warrant|proof|verification).*(formal|symbol|codif|model)|(?:formal|symbol|codif|model).*(accept|warrant|proof|verification)' kb/notes/ --glob '*.md'` — exposed direct tension with `codify-versus-llm-decision-heuristics.md` and `progressive-constraining-commits-only-after-patterns-stabilize.md`: both make codification itself a post-stability commitment, while the source permits exploratory formalization before acceptance.
- `rg -n -i '(model[- ]to[- ]world|correspondence|translation boundary|faithful encoding|formal assumptions|external claim)' kb/notes/ --glob '*.md'` — the formal-systems result was already linked by the source; its neighborhood led to the controlled Model Discovery Agent source evaluated below.
- `rg -n -i '(invocation frequency|wrong reading|misread|volatil|pattern stabil|interpretation cost)' kb/notes/ --glob '*.md'` — the codification-decision and progressive-constraining notes were the strongest matches. `verifiability-gradient.md` and `specification-strategy-should-follow-where-understanding-lives.md` were rejected at the source's theory grain: their claims govern behavior-shaping components and durable specifications, which the source expressly distinguishes from theories.

**Link following:**

- Followed `axes-of-artifact-analysis.md` through representational form, behavioral authority, codification, continual-learning governance, and the readable-artifact loop. This confirmed that the axes note is the smallest useful foundation; the downstream governance notes add applications already reachable through the source's authored coevolution link.
- Followed `codify-versus-llm-decision-heuristics.md` through exact-spec/proxy-theory, oracle strength, interpretation space, pattern stability, and progressive constraining. Its statements that codification “collapses [interpretation space] to a point” and that the codification definition requires a stable pattern are not merely adjacent to the source; they conflict with its parameterized-formal-model and pre-acceptance cases.
- Followed `progressive-constraining-commits-only-after-patterns-stabilize.md` through the projection model, codification, constraining, and selection-without-semantic-fixity. Its operational recommendation is useful, but its claim that codification “taken seriously” waits for stability makes representational transition and adoption timing coextensive, which the source denies.
- `rg -n 'a-natural-language-theory-is-a-prototype-codified-or-rejected' kb/ --glob '*.md'` found one library backlink, from `the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md`. That edge already exists in both directions, so it is not a candidate; its stale anchor text is recorded under Maintenance Observations.

### Types

**Curated head, titles, descriptions, and body search:**

- Read `kb/types/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'` (10 titles) and `rg '^description:' kb/types/ --glob '*.md'` (13 descriptions).
- `rg -n -i '(codif|formaliz|symbolic|natural[- ]language|representational form)' kb/types/ --glob '*.md'` found the type-spec validator/reviewer split, but it is a structural Commonplace contract rather than an observation or premise about theory lifecycle. No type candidate passed the articulation test.

### Reference

**Curated head, titles, descriptions, and body search:**

- Read `kb/reference/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (151 titles) and `rg '^description:' kb/reference/ --glob '*.md'` (150 descriptions).
- `rg -n -i '(prototype|cheap to (revise|reject|discard)|revision cost|rollback cost|operational coupling|entrench)' kb/reference/ --glob '*.md'` mostly found the explicitly excluded clone-once collection-prototype sense.
- `rg -n -i '(codif|formaliz|symbolic|natural[- ]language|representational form)' kb/reference/ --glob '*.md'` isolated `proposals/bidirectional-codification-comparative-test.md`. Its four-arm experiment is a concrete downstream use, but the source shows that the protocol must vary form without silently varying adoption, authority, or rollback coupling.
- Following the proposal's links to codification/relaxing, relaxing signals, scheduler separation, oracle accumulation, and its ablation companion confirmed a useful two-way relation: the source should expose the test as an application, while the proposal should rest on the source's form-versus-binding control.

### Agent-memory systems

**Curated head, titles, descriptions, and body search:**

- Read `kb/agent-memory-systems/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (173 titles) and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` (171 descriptions).
- `rg -n -i '(representational form|natural[- ]language|symbolic).*(authority|force|operative|binding)|(?:authority|force|operative|binding).*(representational form|natural[- ]language|symbolic)' kb/agent-memory-systems/ --glob '*.md'` found many reviews that correctly inventory form and authority separately. Napkin was the strongest prose-authority hit, while Closure-SDK was the strongest symbolic-without-agent-activation hit.
- `rg -n -i '(codif|formaliz|formal semantics|proof-gat|typed execution)' kb/agent-memory-systems/ --glob '*.md'` and `rg -n -i '(rollback|revert|discard|reject).*(prompt|code|schema|skill|rule|artifact)|(?:prompt|code|schema|skill|rule|artifact).*(rollback|revert|discard|reject)' kb/agent-memory-systems/ --glob '*.md'` added rich artifact lifecycle cases but no theory whose acceptance, rejection, and operational coupling are observed. Napkin and Closure-SDK were therefore rejected rather than used as cross-kind analogies.

### Agentic systems

**Curated head, titles, descriptions, and body search:**

- Read `kb/agentic-systems/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (12 titles) and `rg '^description:' kb/agentic-systems/ --glob '*.md'` (10 descriptions).
- `rg -n -i '(natural[- ]language|symbolic|formal|typed).*(authority|operative|binding|activation)|(?:authority|operative|binding|activation).*(natural[- ]language|symbolic|formal|typed)' kb/agentic-systems/ --glob '*.md'` found GBrain's natural-language host-adoption contract. It demonstrates prose instruction force, not a theory's prototype standing, so it failed at the content-kind boundary.
- `rg -n -i '(candidate|proposal|revision).*(commit|adopt|install|rollback|reject)|(?:commit|adopt|install|rollback|reject).*(candidate|proposal|revision)' kb/agentic-systems/ --glob '*.md'` found Autogenesis and Compound Engineering candidate lifecycles, again for code, prompts, and procedures rather than theories.
- `rg -n -i '(proof|Lean|correspondence|graph claim|formal model)' kb/agentic-systems/ --glob '*.md'` confirmed that Eigenius is the one theory-relevant proof/correspondence case, and the source already links it. No new agentic-system candidate survived.

### Sources

**Curated head, titles, descriptions, and body search:**

- Read `kb/sources/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'` (311 entries each).
- `rg -n -i '(cheap|cheaper|cost).{0,80}(formal|symbolic|code|proof|theor)|(?:formal|symbolic|code|proof|theor).{0,80}(cheap|cheaper|cost)' kb/sources/ --glob '*.md'` kept `a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md` as a bounded current-practice signal for cheaper symbolic theory work. Its single uncontrolled self-report cannot establish the source's prevalence conjecture, so the candidate context preserves that limit.
- `rg -n -i '(theory|hypothesis).{0,100}(prototype|reject|accept|formaliz|codif)|(?:prototype|reject|accept|formaliz|codif).{0,100}(theory|hypothesis)' kb/sources/ --glob '*.md'` found Popper and Programming as Theory Building, but neither supplies the operational coupling comparison the source needs.
- `rg -n -i '(proof|formal model).{0,100}(world|correspondence|translation|assumption)|(?:world|correspondence|translation|assumption).{0,100}(proof|formal model)' kb/sources/ --glob '*.md'` led through the existing formal-systems neighborhood to `model-discovery-agent-bayesian-experiment-design.ingest.md`. Its stochastic NEURONBENCH result is a controlled case where correct Bayesian machinery confidently ranks the wrong mechanism under a misspecified likelihood.
- Followed Model Discovery Agent through formal-systems reach assessment, fixed-decomposition learning, theory-mediated learning, and DiscoverPhysics. It adds a measured likelihood-misspecification failure rather than duplicating DiscoverPhysics's explanation-versus-implementation split. Followed the theory-driven-AI-research ingest through the discovery lifecycle and automation boundary; it adds a cost signal only, not acceptance evidence.

### Instructions and reverse-edge pass

**Curated head, titles, descriptions, and body search:**

- Read `kb/instructions/README.md` and `kb/instructions/COLLECTION.md`; generated `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` (48 titles) and `rg '^description:' kb/instructions/ --glob '*.md'` (100 descriptions).
- Because the notes contract says the usual instruction direction is inverse, ran a first-class reverse pass with `rg -n -i '(codif|formaliz|symbolic|natural[- ]language|representational form)' kb/instructions/ --glob '*.md'` and `rg -n -i '(binding|behavioral authority|operative authority|adoption|operative retention|consumer.*force|downstream depend)' kb/instructions/ --glob '*.md'`.
- `analyse-agentic-system/SKILL.md` was the only close match. It already rests on behavioral authority and tells analysts to separate form from force; adding a theory-prototype dependency would not improve execution or maintenance. Its phrase “more binding representation” for natural-language-to-schema/code movement is instead a local precision issue, recorded under Maintenance Observations. No reverse-edge candidate survived.

### External and excluded destinations

- The notes contract authorizes `external`, but no external target was supplied by the user or already present in loaded context. Open-web prospecting was skipped as required.
- `kb/work/` was not searched because the notes contract excludes workshop artifacts as outbound targets.
- No search service was used and no similarity scores were available; all evaluations came from repo-local titles, descriptions, bodies, and one-hop link neighborhoods.

## Connections Found

- [Axes of artifact analysis](../../../../notes/axes-of-artifact-analysis.md) — **grounds**: supplies the source's load-bearing separation between representational form and behavioral authority, explaining why symbolic semantics do not by themselves create adoption or rollback coupling and why prose can still bind through a consumption path.
- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) — **contradicts**: says codification collapses interpretation space to one point and treats pattern stability as part of codification itself, while the source permits parameterized or nondeterministic formal models and exploratory codification before acceptance.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — **contradicts**: makes symbolic transition and post-stability commitment one move; the source separates formal expression from the later authority, dependency, and migration costs that end prototype standing.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) — **see-also**: proposes the clearest experiment over natural-language-only, symbolic-only, one-way, and bidirectional regimes; the source identifies the necessary control that representational form must vary without silently varying adoption or rollback coupling.
- [Model Discovery Agent: LLM-assisted Bayesian Experiment Design](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **evidenced-by**: stochastic NEURONBENCH supplies a controlled case where valid Bayesian updating confidently selects the wrong mechanism because the likelihood misrepresents channel noise, concretely supporting the source's formal-model-to-world boundary.
- [A new Era Of Theory-Driven AI Research](../../../../sources/a-new-era-of-theory-driven-ai-research-2084779496549548323.ingest.md) — **evidenced-by**: provides bounded practitioner evidence that coding agents can lower the cost of mathematical and symbolic theory work; it supports the source's cheap-formalization condition but not its prevalence conjecture or faithful-formalization claim.

## Bidirectional Candidates

- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) ↔ source — reverse **contradicts**: readers of the decision heuristic need the source's counterexamples to “one point” semantics and post-stability-only codification, not just a source-side warning.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) ↔ source — reverse **contradicts**: the progressive strategy remains useful only after separating the optional formalization step from the authority and coupling decision; the reverse edge would expose that unresolved scope.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) ↔ source — reverse **rests-on**: the proposal's arm definitions need the source's theory that form does not encode adoption status, or the comparison risks testing authority and rollback cost together with form.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The verifiability gradient](../../../../notes/verifiability-gradient.md) — rejected because it places behavior-shaping deployment artifacts by verification maturity; the source is about a theory's prototype standing and explicitly allows accepted prose where no formal consumer is needed.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — rejected because its spec-first, live-spec, and spec-mining lifecycle governs durable specifications and procedures, whose displacement the source excludes from its theory-rejection account.
- [Behavioral authority](../../../../notes/definitions/behavioral-authority.md) — rejected as a separate direct edge because the kept axes note already routes to this definition while adding the independent-form argument the source needs.
- [Napkin](../../../../agent-memory-systems/reviews/napkin.md) — rejected because the same Markdown bytes carrying advice or instruction authority corroborate the general artifact-axis distinction but do not observe a theory's acceptance, rejection, or prototype exit.
- [Closure-SDK](../../../../agent-memory-systems/reviews/Closure-SDK.md) — rejected because symbolic state without LLM activation is a substrate case, not evidence about a formalized theory's revision cost; the source's existing Eigenius case is closer to the proof and correspondence claim.
- [GBrain as an agentic system](../../../../agentic-systems/reviews/gbrain.md) — rejected because its strongly binding natural-language surface is an adoption protocol and instruction set, not an accepted or conjectural theory.
- [Collection prototypes](../../../../reference/collection-prototypes.md) — rejected because it is the clone-once contract-template sense of “prototype” that the source explicitly excludes.
- [The Flawed Ephemeral Software Hypothesis](../../../../sources/the-flawed-ephemeral-software-hypothesis.ingest.md) — rejected because cheap generation versus durable software trust concerns deployed artifact stacks; it does not separate theory acceptance from representational transition.
- [Analyse an Agentic System](../../../../instructions/analyse-agentic-system/SKILL.md) — rejected as a reverse `rests-on` candidate because the instruction already embeds the form/force distinction and links its general authority foundation; its remaining problem is wording precision, not a missing theory dependency.

## Index Membership

- [constraining](../../../../tags/constraining-README.md) — candidate for “Deciding and reversing”: the source separates when symbolic form becomes useful from when operational coupling makes a commitment costly to reverse.
- [artifact-analysis](../../../../tags/artifact-analysis-README.md) — candidate application membership, accompanied by an `artifact-analysis` tag if adopted: the source applies the collection's form-versus-authority separation to theory lifecycle. The head is `complete: true`, so tag membership and any curated placement must remain consistent.

## Synthesis Opportunities

None

## Maintenance Observations

- [The bitter-lesson defense portfolio has one load-bearing member for the form-only rebuttal](../../../../notes/the-bitter-lesson-defense-portfolio-has-one-load-bearing-member.md) is the target's only library backlink, but its anchor text still states the prior title, “A natural-language theory is a prototype that may later be codified or rejected.” The edge's explanatory role remains valid; the visible claim text is stale after the target's rewrite.
- The contradiction candidates indicate corpus-level codification drift rather than two unrelated links: `codify-versus-llm-decision-heuristics.md` quotes an older stability-and-code definition, and `progressive-constraining-commits-only-after-patterns-stabilize.md` calls post-stability commitment codification “taken seriously,” while the current codification definition and source treat codification as a representational crossing independent of adoption.
- [Analyse an Agentic System](../../../../instructions/analyse-agentic-system/SKILL.md) tells analysts to keep form and force separate but describes natural-language-to-schema/code movement as a “more binding representation.” That wording can cause the exact conflation the source rules out: symbolic form assigns formal consequences, while stronger behavioral force requires a distinct consumer/channel/force change.

## Flags

- **Split candidate:** the source makes independent claims about prototype standing, pressure-to-codify prevalence, formal proof/correspondence, and the effect of cheap formalization. With more than five useful connections spanning artifact analysis, codification strategy, experimental design, and external evidence, a future writer should test whether the pressure-to-codify and cheap-formalization sections remain composable applications or should become separate notes.
- **Unresolved contradiction:** the report does not decide whether the two older constraining notes should be narrowed to operational adoption or revised to use the current representational definition of codification. Until resolved, any authored `contradicts` edge should name that semantic mismatch explicitly rather than implying the progressive strategy itself is rejected.
