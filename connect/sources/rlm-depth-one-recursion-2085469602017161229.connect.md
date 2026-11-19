---
description: "Discovery report for Will Brown's depth-1 RLM recursion thread"
type: kb/cache/types/connect-report.md
source: "kb/sources/rlm-depth-one-recursion-2085469602017161229.md"
source_has_frontmatter: true
date: "2026-08-07"
depth: standard
---

# Connection Report: RLMs can do true recursion at depth 1

**Source:** [Thread by @willccbb](../../../sources/rlm-depth-one-recursion-2085469602017161229.md)

## Discovery Trace

**Description listing scan:**
- `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md' | rg -i 'recursive|recursion|RLM|subagent|delegat|orchestrat|call graph|semantic|map.?reduce|divide|depth|REPL|parallel|async|agent loop|language model'` -- retained the RLM, host-language scheduler, symbolic-program, dynamic-workflow, and λ-RLM candidates; rejected generic semantic-review and unrelated recursive-self-improvement hits.
- `rg '^description:' kb/reference --glob '*.md' | rg -i 'recursive|RLM|orchestrat|subagent|scheduler|host language'` -- only the archived harness-orchestrated review-sweep proposal matched; rejected because this source bears on general agent scheduling rather than shipped Commonplace review orchestration.
- `rg '^description:' kb/agent-memory-systems --glob '*.md' | rg -i 'recursive|RLM|orchestrat|subagent|scheduler|host language'` -- HALO, G-Memory, EQUIPA, getsentry/skills, and OpenSage matched; rejected because the thread describes an execution primitive rather than memory behavior, and HALO's use of RLM adds no useful reader path beyond the RLM theory cluster.
- `rg '^description:' kb/agentic-systems --glob '*.md' | rg -i 'recursive|RLM|orchestrat|subagent|scheduler|host language'` -- retained Claude Code dynamic workflows as a direct comparison; evaluated Fractal but rejected it as redundant with the stronger RLM theory and practitioner-source targets.
- `rg '^description:' kb/sources --glob '*.md' | rg -i 'recursive language|RLM|semantic quicksort|dynamic workflow|host-language|subagent'` -- retained the earlier RLM practitioner ingest and λ-RLM ingest as the closest source-side comparisons.

**Topic indexes:**
- Read [Computational model](../../../../tags/computational-model-README.md) -- retained its Scheduling & Orchestration cluster, especially the bounded scheduler, multi-dimensional orchestration, and dynamic-workflows placements.
- Read [Tool loop](../../../../tags/tool-loop-README.md) -- retained the host-language scheduler and RLM boundary case; the source's `ask()` primitive is a bounded returning call composed by ordinary Python control flow.
- Read [Context engineering](../../../../tags/context-engineering-README.md) -- the long-document divide/merge example fits bounded-context scheduling, but the stronger connection is already expressed by the computational-model targets.
- Read [Agentic Systems](../../../../agentic-systems/README.md) -- retained Claude Code dynamic workflows and evaluated Fractal.
- Read [Agent Memory Systems](../../../../agent-memory-systems/README.md) and [Reference](../../../../reference/README.md) -- no direct target met the source collection's reader-need threshold.

**Body search:**
- `rg -n -i '\bRLMs?\b|recursive language model|semantic quicksort|subsubagent|sub-agent|subagent|delegat(e|ion|ing)|call graph|max depth|depth.?1|divide.{0,10}merge' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- confirmed the mature RLM cluster and the captured Claude Code script-orchestration counterexample; no existing artifact states the host-recursion-depth versus LM-call-depth distinction directly.
- `rg -n -i 'recurs|agent\(|parallel|depth|return|script|host language' kb/agentic-systems/claude-code-dynamic-workflows.md kb/sources/claude-code-dynamic-workflows-docs.md kb/sources/claude-code-dynamic-workflows-docs.ingest.md` -- confirmed that the captured Claude Code feature exposes a returning `agent()` primitive to ordinary JavaScript control flow, so the thread's unqualified “Claude Code can't do this” claim needs scoping.

**Link following:**
- Followed the RLM note into [RLM, Tendril, and llm-do](../../../../notes/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md), [The practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md), [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md), and the prior RLM and λ-RLM ingests. Kept targets where the thread adds the distinct program-recursion/call-graph example; rejected persistence-only targets because the thread says nothing about retaining the generated program.
- Followed Claude Code dynamic workflows into its official-docs snapshot and analysis. Kept the system analysis as a comparison because it supplies a captured, concrete surface against which the thread's Claude Code claim can be bounded.

## Connections Found

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) -- **is-evidence-for**: the divide/merge and semantic-quicksort programs show the model-authored REPL scheduler as literal recursive host-language code whose `ask()` calls remain leaf operations.
- [The practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md) -- **is-evidence-for**: Python recursion, local variables, branching, and return values implement `select` and `K` around a returning model primitive without a reified scheduler object.
- [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) -- **is-evidence-for**: the screenshots are a worked witness in which exact symbolic recursion determines the order and prompts of bounded language-model calls.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- **compares-with**: the thread says Claude Code requires an external file that executes `claude -p`, while the captured workflow feature exposes a returning `agent()` primitive inside model-authored JavaScript; the comparison forces the claim to distinguish ordinary Claude Code from that research-preview surface.
- [Ingest: Recursive Language Models — what finally gave me the 'aha' moment](../../../../sources/recursive-language-models-what-finally-gave-me-the-aha-moment.ingest.md) -- **compares-with**: the earlier practitioner account explains REPL state, subcall results, and context protection; this thread contributes a precise separation between host-program recursion depth and LM-call-graph depth.
- [Ingest: The Y-Combinator for LLMs](../../../../sources/the-y-combinator-for-llms-solving-long-context-rot.ingest.md) -- **compares-with**: both use recursive divide-and-compose over bounded leaf calls, but this source uses arbitrary Python and semantic `ask()` prompts where λ-RLM uses a fixed typed combinator runtime.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [RLM has the model write ephemeral orchestrators over sub-agents](../../../../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) → source -- **evidenced-by**: add the source as the clearest pseudocode witness for recursive symbolic control around depth-1 model leaves.
- [The practical scheduler is the host language](../../../../notes/the-practical-scheduler-is-the-host-language.md) → source -- **evidenced-by**: the semantic-quicksort example is a compact witness that ordinary host-language algorithms can use an LM as one operator.
- [Any symbolic program with LLM calls is a select/call program](../../../../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) → source -- **evidenced-by**: the two reconstructed programs instantiate the lemma directly.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- ["agent" is a tool loop](../../../../notes/agent-is-a-tool-loop.md) -- rejected as a direct edge because the thread's strongest contribution is precisely that its `ask()` leaves need not be recursively delegating tool loops; treating each leaf as an agent would obscure the distinction.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- the reply posts mention bidirectional parent/child message queues but provide no delivery, consistency, scoping, or adjudication guarantee; topical overlap alone is insufficient.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) -- a relevant code-grounded RLM implementation, but following it adds less than the direct RLM theory note and the prior practitioner ingest for this source's narrow recursion claim.
- [HALO](../../../../agent-memory-systems/reviews/halo.md) -- uses recursive trace-analysis agents, but the reviewed system's memory and trace-learning behavior is not illuminated by the pseudocode here.
- [Harness-orchestrated review sweeps](../../../../reference/proposals/archive/harness-orchestrated-review-sweeps.md) -- shares host-language fan-out but is an archived Commonplace implementation proposal, not a useful target for this general recursion distinction.

## Index Membership

None.

## Synthesis Opportunities

The source, the host-language scheduler notes, and the dynamic-workflows analysis jointly imply a missing distinction: **host-program recursion depth, language-model invocation depth, saved-workflow nesting, and agent-delegation depth are separate properties**. “Recursive agent” and “recursive language model” discussions often collapse them. The semantic-quicksort witness shows arbitrary symbolic recursion with LM depth one; Claude Code workflows show script-level composition with an explicit one-level saved-workflow nesting cap; ordinary delegation chains can increase agent depth without symbolic recursion. This may warrant a compact claim note or a new axis in the existing multi-dimensional orchestration note.

## Maintenance Observations

None.

## Flags

- Tension: the source's unqualified Claude Code comparison conflicts with the locally captured dynamic-workflows feature unless “Claude Code” excludes that research-preview script runtime.
