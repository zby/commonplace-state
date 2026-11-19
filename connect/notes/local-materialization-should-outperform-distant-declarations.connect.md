---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/local-materialization-should-outperform-distant-declarations.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Local materialization should outperform distant natural-language declarations

**Source:** [Local materialization should outperform distant natural-language declarations](../../../../notes/local-materialization-should-outperform-distant-declarations.md)

## Discovery Trace

**Scope and source contract:**

- Verified the source against the supplied stable SHA-256: `sha256sum kb/notes/prose-has-no-dereference-reinforce-facts-at-point-of-use.md` returned `1a1da1f64251d4f814fdbc4713cc7b21c57f62f4c5e642184d56212846d044b6`.
- Read the connect skill, connect-report type, source artifact, and `kb/notes/COLLECTION.md` before discovery. The source is an untested statistical conjecture: for distant declarations or non-obvious application, generated point-of-use materialization should improve correct, non-contradictory application over declaration-only presentation. Its mechanism is the absence of assigned natural-language resolution semantics; its implementation boundary is one canonical symbolic value plus generated or checked local views; its experiment separately varies distance, interference, and inferential non-obviousness.
- The notes contract authorises local prospecting in `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`, and excludes `kb/work/`. The reserved `external` destination is authorised, but no external target was user-supplied or already loaded, so open-web prospecting was skipped.
- Existing source edges were removed from the candidate pool: agentic systems interpret underspecified instructions, representational form, codification, frontloading, the checked-derived-copy rule, links as conditional possibilities, and unscoped LLM context.

**Curated heads and lexical surfaces:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the three matching tag heads: `learning-theory-README.md`, `artifact-analysis-README.md`, and `computational-model-README.md`. `artifact-analysis-README.md` declares `complete: true`, so the artifact-analysis by-tag `rg` was skipped. The other two tag scans were run exactly as `rg -l '^tags:.*\blearning-theory\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`.
- Read the curated destination heads `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No matching tag heads exist in those destination roots.
- Generated the complete title surface once for every authorised local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, substituting `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Generated the whole-destination description surface for every authorised destination with `rg '^description:' kb/<destination>/ --glob '*.md'`. These lexical commands emit no relevance scores, so no scores were available to record.

**Notes:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|distant natural[- ]language|declaration[- ]only|generated.*restatement|restatement.*generated|denormali[sz]' kb/notes/ --glob '*.md'`, `rg -n -i 'contextual activation|presence.*application|loaded.*behavior|fact.*appl(y|ication)|recover.*declaration|non-obvious inference' kb/notes/ --glob '*.md'`, `rg -n -i 'matched control|ablation|held[- ]out|preregister|controlled variation|experiment.*contrast|contrast.*experiment' kb/notes/ --glob '*.md'`, and `rg -n -i 'recompute.*(cost|expensive)|materiali[sz].*(value|fact)|derived (value|label)|canonical (value|fact)|single maintenance authority' kb/notes/ --glob '*.md'`.
- Kept contextual activation as the directly evidenced premise that visible content need not affect action; the recompute-cost note as the complementary value theory for model-consumed materialized values; the linked-note payload note as a concrete omission-boundary application with a three-arm behavioral test; and the experimental-contrast note as the rationale for the matched filler control and treatment-grain limits.
- Rejected prompt ablation because it varies cognitive framings against a known human finding rather than declaration placement or local restatement. Rejected the two-rewrite repetition case because it measures semantic preservation during sentence splitting, not whether local repetition improves downstream LLM application. Rejected the indirection note because placeholder/abstraction resolution cost is not the source's behavioral uptake contrast, and the source already carries the more specific frontloading comparison.

**Types:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|user-verified|derived (value|label)|recomputable' kb/types/ --glob '*.md'` and `rg -n -i 'natural[- ]language|machine[- ]parseable|validator|validation|frontmatter|symbolic' kb/types/ --glob '*.md'`.
- `tag-readme.md` supplies a validated-cache instance and `type-spec.md` separates deterministic and semantic checks, but neither independently supports point-of-use application. The source already links the checked-derived-copy and representational-form claims that explain these cases, so no additional type edge passed the articulation test.

**Reference:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|single maintenance authority' kb/reference/ --glob '*.md'`, `rg -n -i 'user-verified|reader-facing banner|inline blocks|checked.*(copy|block|view)|generated.*(banner|label|view)|shared instruction text' kb/reference/ --glob '*.md'`, `rg -n -i 'matched control|ablation|held[- ]out|preregister|controlled variation|experiment.*contrast|contrast.*experiment' kb/reference/ --glob '*.md'`, and `rg -n -i 'dereferenc|natural[- ]language.*(application|use|instruction)|frontmatter.*(agent|model|read)' kb/reference/ --glob '*.md'`.
- Read the reader-facing-banner and checked-inline-block proposals fully. Each already authors a `rests-on` edge to the source; both pass the return-path articulation test because a reader of the general conjecture gains a worked Commonplace design case. Retained them as bidirectional `see-also` candidates, not as new source evidence.
- Rejected `validation-contract.md` and `type-spec.md` hits that use “dereference” for a schema or validator following another artifact; that deterministic tooling limit is not the source's model-behavior claim.

**Agent-memory systems:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|single maintenance authority' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'contextual activation|loaded.*behavior|present.*behavior|push.*(tested|behavior)|injected.*(use|behavior)|ignore.*(memory|solution|instruction)' kb/agent-memory-systems/ --glob '*.md'`, `rg -n -i 'checked (copy|mirror)|generated (view|context|instruction)|hot (cache|fact)|always[- ]loaded|prompt.*inject|context pack' kb/agent-memory-systems/ --glob '*.md'`, and `rg -n -i 'ablation|controlled variation|held[- ]out|preregister|matched control' kb/agent-memory-systems/ --glob '*.md'`.
- Read the comparative review's “automatic activation is shipped on faith” finding and the LLM Wiki runtime-mirror case. The comparison establishes that behavioral read-back testing is rare, not that local materialization works; LLM Wiki checks cross-runtime packaging equality rather than application at a distant use site. Both were rejected.

**Agentic systems:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|single maintenance authority' kb/agentic-systems/ --glob '*.md'`, `rg -n -i 'natural[- ]language.*(adoption|instruction|prompt)|prompt.*(position|surface|inject)|context.*(assembly|inject)|symbolic.*(reference|enforcement)|ignore.*instruction' kb/agentic-systems/ --glob '*.md'`, and `rg -n -i 'ablation|controlled variation|held[- ]out|matched control|behavior.*test' kb/agentic-systems/ --glob '*.md'`.
- GBrain demonstrates that host behavior depends on adoption of natural-language instructions, while Swamp replaces prompt-mediated handoff with symbolic references. Neither tests local restatement, distance, or non-obvious application, and the source's existing representational-form and codification edges already carry their useful distinction.

**Sources:**

- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|single maintenance authority' kb/sources/ --glob '*.md'`, `rg -n -i 'solution.*(present|inject|visible|environment)|present.*(ignore|fail|use)|context presence|loaded.*behavior|injected.*(behavior|use)|ignore.*(solution|instruction|memory)' kb/sources/ --glob '*.md'`, `rg -n -i 'instruction surface|system prompt|prompt surface|instruction.*position|position.*instruction|relocat(e|ing).*rule|same rules|surface.*precedence' kb/sources/ --glob '*.md'`, `rg -n -i 'distance.*(instruction|fact|declaration|context)|position bias|lost in the middle|long context|intervening.*content|non-obvious inference' kb/sources/ --glob '*.md'`, and `rg -n -i 'matched control|declaration only|human-authored.*restatement|generated.*restatement|point[- ]of[- ]use.*restatement' kb/sources/ --glob '*.md'`.
- Kept Agents Explore but Agents Ignore as bounded evidence for the prerequisite context-to-action failure: agents often observed explicit solutions yet did not use them. Rejected Harness-IF as evidence for the conjecture itself: its controlled pilot varies instruction surfaces and conflicts, not declaration distance or local restatement, though it remains useful through the retained experimental-contrast note. No repo-local source ran the source's proposed generated-local-view comparison.

**Instructions and reverse-edge pass:**

- Read `kb/instructions/COLLECTION.md` because the notes contract says the usual notes/instructions direction is inverse. Its frontloaded posture permits `instruction -> note` only as a meta-reader `rests-on` edge.
- Ran `rg -n -i 'local materiali[sz]|point[- ]of[- ]use|declaration[- ]only|restatement|denormali[sz]|canonical (value|fact)|single maintenance authority' kb/instructions/ --glob '*.md'`, `rg -n -i 'self-contained|frontload|inline block|must read|read .*contract|load .*contract|report substance|task brief' kb/instructions/ --glob '*.md'`, `rg -n -i 'ablation|controlled variation|matched control|held[- ]out|preregister' kb/instructions/ --glob '*.md'`, and the inbound check `rg -n -F 'prose-has-no-dereference-reinforce-facts-at-point-of-use' kb/instructions/ --glob '*.md'`.
- `write-instruction.md` already rests on frontloading for self-contained execution. The marginal-value-redundancy gate exempts repetition that does reader or workflow work, but it does not depend on the source's untested LLM-performance conjecture. No instruction gained a distinct, warranted `rests-on` dependency, so the first-class reverse-edge pass produced no candidate.

**Link following, inbound state, and verification:**

- Ran `rg -n -F 'prose-has-no-dereference-reinforce-facts-at-point-of-use' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'`. It found two reference proposals and five note/tag surfaces linking to the source; no instruction, type, agent-memory, agentic-system, or source artifact currently links to it.
- Followed each promising neighborhood one hop with `rg -l -F '<slug>' kb/notes kb/types kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` for `knowledge-storage-does-not-imply-contextual-activation`, `llm-recompute-cost-inverts-the-store-vs-recompute-default`, `linked-note-durable-payload-is-what-consumption-path-cannot-supply`, `an-experiment-identifies-only-the-contrast-it-actually-runs`, `prompt-ablation-converts-human-insight-to-deployable-framing`, `agents-explore-but-agents-ignore-llms-lack-environmental`, and `harness-if-instruction-following-across-instruction-surfaces`. The neighborhoods confirmed that activation, materialization economics, and causal-contrast discipline are separate reader needs, while Harness-IF already reaches the source's experiment through the contrast note.
- Verified every retained candidate with `test -f`, checked that each starts with YAML frontmatter, and rechecked the source SHA-256 before writing this report. All retained paths exist and all retained targets have frontmatter.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **grounds**: the source predicts that changing where a declaration appears will improve its application; this target establishes the prerequisite distinction between content being visible and content changing action, supplies direct context-to-action evidence, and names distance as an open activation variable.
- [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **extends**: the source supplies a refutable behavioral claim about local materialization, while this target supplies the complementary value theory for model-read materialized values and explains why a checked derived view can be worth its storage and context cost.
- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — **extends**: the source studies whether proximity improves use of a declaration; this target applies the same activation boundary to note compression and compares name alone, name plus local recognition anchor, and full restatement to decide what must remain at the use site.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **grounds**: the source's matched local filler arm is needed because declaration-only versus local restatement otherwise bundles semantic content with position, emphasis, and token budget; this target explains why the conclusion may name only the independently varied contrast.
- [Ingest: Agents Explore but Agents Ignore](../../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) — **evidenced-by**: solution-injection experiments show that agents can observe explicit task solutions and still fail to integrate them into action, corroborating the source's prerequisite claim that presence does not guarantee application. The study does not vary declaration distance or compare local restatement, so it does not test the source's statistical conjecture.

## Bidirectional Candidates

- [A reader-facing banner for user verification](../../../../reference/proposals/a-reader-facing-banner-for-user-verification.md) <-> source — **see-also**: the proposal already links to the source via `rests-on`; a return link would give readers the exact motivating case for a generated or checked point-of-reading view, including positive-only versus binary presentation, semantic restraint, and drift enforcement.
- [Checked inline blocks for shared instruction text](../../../../reference/proposals/checked-inline-blocks-for-shared-instruction-text.md) <-> source — **see-also**: the proposal already links to the source via `rests-on`; a return link would expose the instruction-reuse case where a bounded literal block is present in each worker context while deterministic equality preserves one maintenance authority.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) — uses controlled prompt variation, but its treatment is a family of cognitive framings scored against a known human finding. It does not compare a distant declaration with local materialization.
- [Two rewrites exposed a syntax-or-repetition tradeoff](../../../../notes/evidence/two-rewrites-exposed-a-syntax-or-repetition-tradeoff.md) — reports that repetition preserved semantic relations during sentence splitting, but explicitly did not measure downstream extraction, comprehension, or application, so it cannot evidence the source's behavioral conjecture.
- [Model-resolved indirection adds interpretation work to LLM execution](../../../../notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md) — addresses the work of model-side placeholder resolution, not whether a visible declaration governs a distant use. The source's existing frontloading contrast already serves the adjacent context-cost need.
- [Tag README](../../../../types/tag-readme.md) and [Type spec](../../../../types/type-spec.md) — provide checked-cache and deterministic/semantic-check examples, but neither supports the claimed application-rate improvement; the source already links the underlying representational-form and checked-copy theory.
- [What the matrix shows across 148 agent memory systems](../../../../agent-memory-systems/agentic-memory-systems-comparative-review.md) and [LLM Wiki](../../../../agent-memory-systems/reviews/llm-wiki.md) — the former shows that behavior-changing read-back is rarely tested, while the latter tests cross-runtime mirror equality. They establish an evaluation gap and packaging consistency, not local uptake.
- [GBrain](../../../../agentic-systems/reviews/gbrain.md) and [Swamp](../../../../agentic-systems/reviews/swamp.md) — contrast model-mediated natural-language adoption with symbolic enforcement and references, but neither tests distance or point-of-use materialization. Existing source edges already carry this representational distinction.
- [Ingest: Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) — its counterbalanced pilot moves conflicting rules between instruction surfaces and establishes scoped precedence, not an effect of local repetition or textual distance. Its useful experimental lesson already reaches this source through the retained contrast-method candidate.
- [Write an Instruction](../../../../instructions/write-instruction.md) and [Marginal-value redundancy](../../../../instructions/compression-bundle/marginal-value-redundancy.md) — self-contained execution and purposeful repetition overlap topically, but neither procedure gains a distinct maintenance dependency on this untested statistical claim; frontloading and the gate's own deletion test are the more specific rationales.

## Index Membership

None.

The source is already a member of the complete artifact-analysis head and the selective computational-model head. Its learning-theory membership is covered through the validator-enforced artifact-analysis child tag, so no missing index placement was found.

## Synthesis Opportunities

None.

## Maintenance Observations

- Several inbound surfaces still state the source's former universal claim even though the final target now presents an explicitly untested statistical conjecture. The stale or over-strong formulations occur in [artifact-analysis](../../../../tags/artifact-analysis-README.md), [computational-model](../../../../tags/computational-model-README.md), [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md), [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md), [Load-bearing vocabulary collisions should be prevented or visibly scoped at write time](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md), and both bidirectional reference proposals. Their link text or context says natural-language content “lacks reliable dereference” and therefore “needs reinforcement,” whereas the final source predicts a conditional performance difference and states that it has not been tested. Future maintenance should reassess those dependency strengths and update contextual link prose without changing the source during connect.

## Flags

- Evidence gap: no repo-local experiment compares declaration-only presentation with human-authored and generated point-of-use restatement while independently varying distance, intervening competition, and inferential non-obviousness. Agents Explore supports only the context-presence/application premise; none of the retained evidence establishes the source's predicted advantage.
