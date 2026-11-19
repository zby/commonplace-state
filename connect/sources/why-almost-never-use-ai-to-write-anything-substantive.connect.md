---
description: "Discovery report for possible KB connections from Erich Grunewald's argument against delegating substantive writing to AI"
type: kb/cache/types/connect-report.md
source: "kb/sources/why-almost-never-use-ai-to-write-anything-substantive.md"
source_has_frontmatter: true
date: "2026-08-07"
depth: standard
---

# Connection Report: Why You Should Almost Never Use AI to Write Anything Substantive

**Source:** [Why You Should Almost Never Use AI to Write Anything Substantive](../../../sources/why-almost-never-use-ai-to-write-anything-substantive.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh full-title and full-description surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` for all five authorised local destinations: `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`.
- The notes surface flagged [Writing commissions imply a contribution, not merely a form](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md), [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md), [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md), [Generation confidence does not by itself certify soundness](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md), [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md), and [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md). The first four survived full-text evaluation; the latter two were rejected as adjacent but not established by the source.
- The sources surface flagged [Human Routers of Machine Words](../../../sources/borretti-human-routers-of-machine-words.md) as the direct comparator and [Infinite midwit](../../../sources/adam-mastroianni-infinite-midwit.md) as a weaker writing-quality comparator. Only Borretti survived because it shares the source's cognitive and ethical claims rather than merely its topic.
- The reference surface had no shipped-system target: its matches concerned Commonplace authoring and holistic rewrite mechanics, while this source argues about the epistemic and social effects of prose delegation.
- The agent-memory and agentic-system surfaces had no trigger-level match. The source describes neither a memory architecture nor an agent harness, and its workflow remarks do not analyze a named system.

**Topic indexes:**

- Read [Tags](../../../../tags/README.md), [Foundations](../../../../tags/foundations-README.md), [LLM reliability](../../../../tags/llm-reliability-README.md), and [Failure modes](../../../../tags/failure-modes-README.md). Foundations routed to the existing writing-is-thinking response; LLM reliability routed to the typicality, verification, and separate-check cluster. Failure modes offered no additional durable candidate.
- Read the curated heads for [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). They confirmed the collection-boundary rejections above.

**Body search:**

- `rg -n -i 'writing (is|as) thinking|think(ing)? (through|by) writing|AI[- ]written|AI writing|generate(d|s|ing)? prose|substantive writing|vague(ness)?|approximate word|reader[- ]writer|authorship|typicality|reverse compression|holistic rewrite|productive generation' kb/notes --glob '*.md'` -- found the writing-is-thinking, hidden-relaxation, typicality, reverse-compression, and defensive-generality cluster. Full reads kept the first three.
- `rg -n -i 'article[- ]shaped|writing commission|interesting angle|worth saying|epistemic objective|intended contribution|output form' kb/notes --glob '*.md'` and `rg -n -i 'generic (prose|text|output)|plausible (prose|text)|in[- ]weights|parametric knowledge|retrieval.*(purpose|goal)|RAG|task interpretation|goal formation' kb/notes --glob '*.md'` -- isolated the new writing-commission note. It survived because it explains a concrete asymmetry in the source's worked example: a sparse commission can cue an expert to supply distinctive judgment while cueing a model only to instantiate the named prose form.
- `rg -n -i 'writing (is|as) thinking|AI[- ]written|AI writing|generate(d|s|ing)? prose|authorship|disclosure|substantive writing|vague(ness)?|holistic rewrite' kb/reference --glob '*.md'` -- returned only authoring and rewrite machinery, rejected as a collection-boundary mismatch.
- `rg -n -i 'writing (is|as) thinking|AI[- ]written|AI writing|prose|authorship|vague(ness)?|human review|deliberate.*accept|holistic rewrite' kb/agent-memory-systems --glob '*.md'` and the same query over `kb/agentic-systems` -- returned incidental wording rather than systems that share the source's claim; both destinations were rejected.
- `rg -n -i 'writing (is|as) thinking|think(ing)? (through|by) writing|AI[- ]written|AI writing|generate(d|s|ing)? prose|substantive writing|vague(ness)?|reader[- ]writer|authorship|typicality|reverse compression|productive generation' kb/sources --glob '*.md'` -- found Borretti as the direct comparator and Mastroianni as a weaker taste-centered one.
- `rg -n -i 'implicit contract|reader.*writer|AI[- ]generated.*(disclos|label)|label.*AI[- ](written|generated)|trust.*AI[- ](written|generated)|authorship.*AI' kb/sources kb/notes --glob '*.md'` -- found no existing durable note for the disclosure/trust-contract claim; Borretti's burden-shift analysis was the closest prior source-side treatment.

**Link following:**

- Followed the writing-is-thinking note to the hidden-relaxation, typicality, verification-boundary, error-correction, vibe-noting, and Borretti artifacts. This confirmed that the KB already contains the source's main mechanism and a qualified defense of agent-assisted writing. Grunewald's new contribution is the sharper challenge that post-hoc endorsement can degrade into passive assent and miss tacit expert sensitivities.
- Followed the hidden-relaxation note to typicality and the separate-check cluster. The chip-smuggling paragraph is a worked instance: fluent prose silently substitutes generic or underspecified statements for domain constraints, and finding the substitutions requires expert re-derivation.
- Followed Borretti's snapshot and ingest. Grunewald repeats its writing-is-thinking and reader-burden claims, but adds a detailed domain-expert audit, clearer exceptions, and an explicit reader-writer trust contract.
- Followed the writing-commission note to the underspecification and contextual-activation notes. Those links confirmed that its contribution is narrower than either parent mechanism: it distinguishes supplying or activating facts from reconstructing the epistemic purpose that selects what an article should contribute.

## Connections Found

- [Writing commissions imply a contribution, not merely a form](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) -- **compares-with**: the note isolates a task-interpretation asymmetry latent in the chip-smuggling example. The expert treats the sparse request as a commission to contribute domain judgment and find what is worth saying, while the model may satisfy only the requested prose form; this qualifies what the single output demonstrates and explains why retrieval alone would not equalize the effective tasks.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- **compares-with**: both accept that naive prose delegation skips a cognitive filter, but Grunewald challenges whether editing or endorsing generated prose reconstructs it, because generated wording anchors the reviewer toward passive assent and hides tacit expert distinctions.
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- **is-evidence-for**: the chip-smuggling audit gives a worked expert example of fluent generation replacing specific constraints with weaker, vaguer statements while leaving no visible marker at the failure point.
- [Generation confidence does not by itself certify soundness](../../../../notes/generation-confidence-does-not-by-itself-certify-soundness.md) -- **is-evidence-for**: the expert audit shows that fluent surface form can hide factual and inferential errors and therefore supports the note's operational call for separate checking; it does not test any token-probability association.
- [Human Routers of Machine Words](../../../sources/borretti-human-routers-of-machine-words.md) -- **compares-with**: Grunewald independently repeats Borretti's writing-is-thinking and reader-burden arguments in a less polemical form, then adds a domain-expert error audit, explicit exceptions, and a disclosure-based trust claim.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Writing commissions imply a contribution, not merely a form](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) → source -- **abstracted-from**: the note generalizes from the sparse chip-smuggling commission and the expert's reaction to a broader difference between requesting an output form and pragmatically inferring a distinctive contribution.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → source -- **evidenced-by**: this source supplies the strongest local objection to the note's reconstruction claim: reviewing a generated draft may be cognitively weaker than generating it, even for an expert, unless the adversarial loop overcomes anchoring and passive assent.
- [LLM generation relaxes a goal it can't satisfy and hides the constraint a human writer stalls on](../../../../notes/llm-generation-relaxes-goals-where-human-writing-stalls.md) → source -- **evidenced-by**: Grunewald's line-by-line chip-smuggling audit is a concrete instance of hidden constraint relaxation in an oracle-poor prose task.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) -- the source identifies empty and vague phrases, but it does not compare the output's information content with a compact seed, so it does not establish reverse compression as defined by the note.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- the chip-smuggling example contains vague abstraction, but the source does not show that the model abstracted defensively to evade a counterexample, which is that note's distinguishing mechanism.
- [Infinite midwit](../../../sources/adam-mastroianni-infinite-midwit.md) -- both criticize AI writing, but Mastroianni's taste and subjective-intelligence thesis does not sharpen the current source's cognitive-filter, hidden-error, or disclosure arguments enough to justify traversal.
- [A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation](../../../../notes/evolving-understanding-needs-holistic-rewrite-not-composition.md) -- both discuss substantive writing, but this note is about representation and maintenance under bounded context, not who performs the prose generation.

## Index Membership

None

## Synthesis Opportunities

- Grunewald and [the adversarial-loop note](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) together sharpen the note's contingent bet: reconstructing the writing filter requires a review operation that escapes anchoring and passive assent, not merely a human who reads and approves generated prose. This belongs as a qualification and falsification condition in the existing note rather than as a new synthesis note.

## Maintenance Observations

None

## Flags

- Unresolved tension: the existing note argues that adversarial review can reconstruct the writing-is-thinking filter; Grunewald argues that review of generated prose is intrinsically less sensitive than productive generation. The current source is anecdotal and does not resolve the empirical question, but it makes the note's failure condition more precise.
