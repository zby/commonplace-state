---
description: "Discovery report for possible KB connections from the Erlang compilation and code-loading snapshot"
type: kb/cache/types/connect-report.md
source: kb/sources/erlang-compilation-and-code-loading.md
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Compilation and Code Loading

**Source:** [Compilation and Code Loading](../../../sources/erlang-compilation-and-code-loading.md)

## Discovery Trace

**Description listing scan:**

- Generated complete title surfaces with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` (354, 134, 172, 12, and 492 titles respectively).
- Ran `rg -n -i '^description:.*(instantiat|idealiz|reflect|definition|deployment|migration|version|govern|runtime|release)'` over all authorised local destinations. The two user-named claim areas were the strongest matches; agent-memory and agentic-system hits concerned their own governance designs rather than Erlang's code-version semantics.

**Topic indexes:**

- Read `kb/notes/README.md`, `tags-README.md`, `computational-model-README.md`, `deploy-time-learning-README.md`, and `self-improving-systems-README.md`, plus the `README.md` heads for reference, agent-memory systems, agentic systems, and sources. The computational-model and deploy-time-learning heads confirmed that the useful landing is definition change across sessions, not a general agent-system comparison.

**Body search:**

- `rg -n -i "hot[- ]code|code replacement|code swap|code_change|release handling|runtime mutation|class mutation|migration callback|governed transformation|change-as-deployment|versioned upgrades"` over notes, reference, agent-memory systems, and agentic systems found direct discussion only in the instantiation note, the domain-pricing note, and a review-workflow proposal.
- `rg -n -i "erlang|code_change|code replacement|migration callback|versioned upgrade"` over the same destinations confirmed that the instantiation note makes the load-bearing Erlang claim and that the proposal only records the episode.
- `rg -n -i "smalltalk|changeset|code_change|hot code|runtime code|code replacement|class mutation"` over sources found reflection papers and a dynamic-component paper, but none supplied this snapshot's precise current/old/two-version mechanism.

**Link following:**

- Followed the instantiation note to the current domain-pricing note and proposal-selection loop. Kept the domain-pricing note because the snapshot is direct external evidence for a marked definition-change path; rejected the proposal-selection loop because the snapshot does not itself provide search or a reject-capable evaluation of candidate definitions.
- Followed the code-loading page's own release-handling reference to the companion snapshot. The two pages are complementary: this one defines the runtime mechanism, while release handling defines the deployment protocol built on it.

## Connections Found

- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- **is-evidence-for**: current/old module versions, explicit switching through a fully qualified call, and destructive purging of a third version substantiate the note's claim that runtime definition change is a distinct protocol rather than ordinary instantiation or local execution.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- **is-evidence-for**: the runtime exposes code replacement through named version states and transition rules, supplying author-external evidence that definition change is treated as a marked path, while not establishing the adequacy half of the note's test.
- [Erlang/OTP Release Handling](../../../sources/erlang-release-handling.md) -- **see-also**: the companion documentation builds versioned release packaging, ordered upgrade instructions, state migration, rollback, and permanence on top of this module-level mechanism.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) → source -- **evidenced-by**: cite the official current/old code-version semantics behind its Erlang hot-swap example.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) → source -- **evidenced-by**: cite the named runtime path as routing evidence only, not as proof that the idealization is adequate.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- the current/old mechanism is a plausible instance, but this page alone says little about inspection, validation, or review and would broaden the source's role beyond the requested attestation.
- [Repair dispositions for defeated claims](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- it mentions Erlang `code_change`, but it records the repository review episode rather than a durable claim that this source materially advances.
- Agent-memory and agentic-system governance reviews -- keyword overlap did not yield a direct Erlang comparison; linking would be analogy-only.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The user-named `kb/notes/a-domain-priced-exception-does-not-refute-an-idealization.md` was replaced during this work by the current domain-pricing note; the candidate above targets the path that exists now.

## Flags

None
