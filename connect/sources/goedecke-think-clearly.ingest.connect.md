---
description: "Post-ingest discovery for Goedecke's invariant-first heuristic, separating useful comparisons from unwarranted agent-evidence and inbound links."
type: types/connect-report.md
source: kb/sources/goedecke-think-clearly.ingest.md
source_has_frontmatter: true
date: "2026-11-07"
depth: standard
---

# Connection Report: Goedecke's invariant-first reasoning heuristic

**Source:** [Ingest: You don't have to be smart if you can think clearly](../../../../sources/goedecke-think-clearly.ingest.md)

Operation: repo-local, standard-depth `cp-skill-connect`, using `kb/instructions/cp-skill-connect/SKILL.md` and the connect-report type. The accepted ingest is the discovery input; no snapshot inspection, external search, delegation, or library edits were performed. All edges below are candidate judgments for a future writer, not authored changes.

## Discovery Trace

### Shared recall surfaces

Read the source and reports collection contracts, connect-report type and schema, and the source in full before judging candidates. Read each authorized destination's `README.md`: theory, reference, agent-memory-systems, agentic-systems, tags, and sources. Generated the complete title surface once with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of those six destinations. Recovered the truncated title output from the tool's full-output file.

For each destination, ran `rg '^description:' kb/<destination>/ --glob '*.md'` filtered with `rg -i 'reasoning|intuition|psycholog|uncertain|first.princip|assumption|process structure|fallibil|debugging|analogy'`. No semantic scores are available. The source has no `tags`, so no source-tag enumeration or completeness shortcut applied.

### Theory

The description scan selected process/output structure, first-principles reasoning, psychology transfer, borrowed-pattern transfer, prompt ablation, and LLM debugging. Ran `rg -n -i 'invariant.first|intuiti|premature|dependable|negative capability' kb/theory --glob '*.md'`. Most hits concerned navigation intuition or premature formalization, not the source's reasoning habit.

Read the process/output note fully; followed its source neighborhood to Agentic Code Reasoning. Read the first-principles, borrowed-pattern, psychology-transfer, prompt-ablation, and debugging notes fully. A follow-up query, `rg -n -i 'premise|assumption|process|human'`, over the debugging and problem-match/mechanism-match notes led to a full read of the latter. Retained the process/output comparison and the borrowed-pattern reuse boundary. Rejected first-principles as an equivocal match, debugging as a different diagnostic task, and psychology transfer/prompt ablation as unnecessary extra routes without a defined agent experiment.

For inbound assessment, read the theory collection contract and note type. The process/output note already explains process-only methods with human examples; Goedecke supplies neither a test of its distinction nor a missing operational premise. No return link was retained merely because the ingest links that note.

### Reference

Read epistemic stance and source-adoption policy in full, plus the reference collection contract and note type for possible inbound use. Ran `rg -n -i 'infallib|invariant.first|psychology|first.principles'` over those two reference files. Retained the existing fallibilism boundary as useful outbound orientation. Source-adoption policy adds a more general gate already covered here by the sharper borrowed-pattern note.

Rejected inbound links from both reference documents: this essay did not establish or inform their recorded Commonplace commitments, and neither document needs a new human-debugging illustration to describe its selected policy.

### Sources

The title/description scan selected Descartes, Agentic Code Reasoning, and `/problem-first`. Ran `rg -n -i 'invariant.first|negative capability|premature (solution|conclusion)|think clearly|dependable (facts|observations)' kb/sources --glob '*.md'`; only the source itself matched. Then ran `rg -n -i 'premature|assumption|premises|indubita'` over the three selected ingests and read them fully.

Retained Descartes on the status of starting premises and Agentic Code Reasoning on evidence-before-conclusion prescriptions versus measured, bundled agent interventions. Rejected `/problem-first` as an additional anti-premature-commitment example with a different operation and no stronger comparison than the retained pair. Following the process/output note to its code-reasoning source supplied the principal one-hop discovery. No reciprocal source links were justified by these comparisons alone.

### Agent memory systems

The README identifies a frozen historical survey. Title/description screening found ReasoningBank, Cortex, and Self-Training-LLM as broad reasoning/uncertainty hits, not matches to this human debugging heuristic. Ran `rg -l -i 'invariant.first|negative capability|premature (solution|conclusion)|think clearly' kb/agent-memory-systems kb/agentic-systems --glob '*.md'`; no matches. No memory mechanism or historical review requires this essay as evidence. No candidate retained.

### Agentic systems

The README and description scan identified Eigenius as the nearest reasoning-protocol lead. In addition to the joint system query above, ran `rg -n -i 'invariant|assumption|premise' kb/agentic-systems/reviews/eigenius.md`. Its hit concerns admission relative to witnesses and assumptions at checked execution boundaries, not a method for choosing dependable initial observations. This distinction does not warrant routing a reader of the essay into that system review. No candidate retained; archived analysis records were not promoted into current comparisons.

### Tags and external

Read the tags README and ran `rg -n -i 'psycholog|first.principles|process.structure|debugging|assumption' kb/tags --glob '*.md'`. Followed the type-system head to its process/output grouping and read that head fully. The essay does not substantively treat document types, so no index inclusion is recommended. Sources are outside participating tag membership; no source tag is proposed. The source contract permits scanning tags but supplies no source-to-tags relationship label; no concrete tag edge passed the articulation test, so no off-authorization request is needed.

External prospecting was skipped. The original URL already appears in source metadata; `derived-from` would restate that provenance rather than add a discovery result. Instructions and work were excluded by the source contract.

Finally ran `rg -n 'goedecke-think-clearly' kb --glob '*.md' --glob '!reports/cache/**'`; no existing inbound reference was found in the visible search surface.

## Connections Found

- [Process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) — **compares-with**: Goedecke prescribes an order of reasoning operations without a result format, making the theory's process/output distinction concrete for a reader of the essay. Already present in the ingest; retain, not a new edge. This is a human-method comparison, not evidence of agent effectiveness.
- [Epistemic stance](../../../../reference/epistemic-stance.md) — **see-also**: the reader needs Commonplace's fallibilist boundary before interpreting dependable starting observations as infallible foundations. Already present in the ingest; retain, not a new edge.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) — **see-also**: this supplies a reuse discriminator for the ingest's experiment suggestion: test the evidence-ordering operation in agents without transferring the essay's professional-identity or panic explanation. Optional new outbound context, not a claim that Goedecke derived his method from this theory.
- [Agentic Code Reasoning](../../../../sources/agentic-code-reasoning.ingest.md) — **compares-with**: both prescribe explicit support before conclusions, but the paper measures a bundled agent template while Goedecke offers an untested human heuristic. The comparison identifies a relevant experimental neighbor without treating the paper's gains as a test of invariant-first ordering. Optional new outbound comparison.
- [Discourse on the Method](../../../../sources/descartes-discourse-on-the-method.ingest.md) — **compares-with**: compare the warrant of starting premises: Descartes explicitly demands indubitability, while Goedecke's practical dependable-observation rule needs conditional provenance and system-model checks. This helps separate useful ordering from a certainty criterion. Optional new outbound comparison; no historical influence is asserted.

## Bidirectional Candidates

None. In particular, the process/output note already has human process-only examples and stronger agent-side evidence. An additional return link to Goedecke would add another illustration, not close an independent reader need under the theory contract.

## Reverse-edge Candidates

None. The borrowed-pattern and psychology-transfer notes already supply their transfer tests; this essay offers no new target-side test. Epistemic stance and source-adoption policy describe Commonplace's commitments, not a catalog of sources to which those commitments apply. The peer ingests likewise need no return link solely because this ingest can use them as comparisons.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [First-principles reasoning selects for explanatory-reach](../../../../theory/first-principles-reasoning-selects-for-explanatory-reach-over.md) — reasoning from dependable observations does not itself select explanations for transfer across domains; shared premise language would obscure the distinction.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — it distinguishes repair targets through three comparisons; the essay offers no evidence for that diagnostic partition.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — a legitimate general assessment route, but redundant with the retained transfer discriminator here; no new failure-mode test is supplied for an inbound use.
- [Prompt ablation converts human insight into deployable agent framing](../../../../theory/prompt-ablation-converts-human-insight-to-deployable-framing.md) — requires a specific verified miss and scoring target, absent here. Do not imply that the essay supplies a ready experiment.
- [Source-adoption policy](../../../../reference/source-adoption-policy.md) — useful background but not an additional necessary outbound route; no evidence that this source informed a recorded design choice justifies inbound lineage.
- [/problem-first](../../../../sources/problem-first-skill-inverts-solution-jumps-2063186118409929161.ingest.md) — reconstructing problems from proposed solutions is not invariant-first debugging; anti-premature-commitment rhetoric alone does not warrant another edge.

## Index Membership

None.

## Synthesis Opportunities

None. The existing process/output distinction and transfer-boundary note already capture the general methodological lessons; these comparisons do not establish a new higher-order claim.

## Maintenance Observations

The `/problem-first` ingest's Connections Found section links an ignored connect report as its discovery authority. This conflicts with the current ingest-report type's prohibition on citing generated connect reports. A separate authorized maintenance action could make that section self-contained; no repair was made here.

## Flags

- Preserve source-only status. Do not label this essay `is-evidence-for` an agent-performance claim or infer that it tested any theory note.
- The source has no retained quotes. Any future source-dependent library claim needs grounding appropriate to its actual use before authoring; discovery does not append quotes or authorize snapshot dependence.
- Five outbound assessments do not indicate five required additions: two are already present, and three are optional comparisons or reuse context. They concern one reasoning-method question, not three independent topic areas warranting a split.
