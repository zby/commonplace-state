---
description: "Discovery report for possible KB connections from the Erlang release-handling snapshot"
type: kb/cache/types/connect-report.md
source: kb/sources/erlang-release-handling.md
source_has_frontmatter: true
date: "2026-08-19"
depth: standard
---

# Connection Report: Release Handling

**Source:** [Release Handling](../../../sources/erlang-release-handling.md)

## Discovery Trace

**Description listing scan:**

- Generated complete title surfaces with `rg -N --no-heading -m1 '^# '` over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` (354, 134, 172, 12, and 492 titles respectively).
- Ran `rg -n -i '^description:.*(instantiat|idealiz|reflect|definition|deployment|migration|version|govern|runtime|release)'` over all authorised local destinations. The two direct note matches were substantially stronger than system-review matches about generic versioning or governance.

**Topic indexes:**

- Read `kb/notes/README.md`, `tags-README.md`, `computational-model-README.md`, `deploy-time-learning-README.md`, and `self-improving-systems-README.md`, plus the `README.md` heads for reference, agent-memory systems, agentic systems, and sources. These routed the source to the governed-definition-change cluster.

**Body search:**

- `rg -n -i "hot[- ]code|code replacement|code swap|code_change|release handling|runtime mutation|class mutation|migration callback|governed transformation|change-as-deployment|versioned upgrades"` over notes, reference, agent-memory systems, and agentic systems found the instantiation note's exact claim, the domain-pricing signature, and a proposal that records the same review episode.
- `rg -n -i "erlang|code_change|code replacement|migration callback|versioned upgrade"` confirmed that the instantiation note is the intended consumer and that the domain-pricing note needs this as routing evidence rather than an adequacy verdict.
- The complete source-title scan and a body search for `code_change`, `hot code`, and `class mutation` found reflection and dynamic-component sources, but none duplicated the official OTP upgrade workflow.

**Link following:**

- Followed the instantiation note to the domain-pricing assessment and proposal-selection loop. Kept the first because `.appup`, `relup`, synchronized `code_change/3`, rollback, and explicit permanence directly instantiate its governance-ritual signature. Rejected the proposal-selection loop because OTP's release handler selects a requested version but the documentation does not describe a learning loop that searches and evaluates candidate changes.
- Followed Release Handling back to Code Replacement. The runtime page is the technical substrate; this page is the governance layer and stronger pricing attestation.

## Connections Found

- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) -- **is-evidence-for**: OTP turns live definition change into a versioned deployment workflow with application-specific upgrade/downgrade scripts, ordered release instructions, synchronized state transformation through `code_change/3`, rollback, and a separate permanence step.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) -- **is-evidence-for**: the official workflow is a direct governance-ritual attestation, but it supplies routing evidence only; the page does not measure frequency, consequence bounds, or explanatory dominance for the class/instance idealization.
- [Erlang/OTP Compilation and Code Loading](../../../sources/erlang-compilation-and-code-loading.md) -- **see-also**: the companion page defines the current/old code-version mechanism on which release handling operates.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Instantiation alone cannot model agent learning across sessions](../../../../notes/instantiation-alone-cannot-model-agent-learning-across-sessions.md) → source -- **evidenced-by**: cite the official release workflow for the note's claim that production code change is treated as deployment with versioned upgrades and migration callbacks.
- [Domain pricing routes an exception to idealization assessment but does not decide it](../../../../notes/domain-pricing-routes-an-exception-to-idealization-assessment.md) → source -- **evidenced-by**: cite `.appup`, `relup`, `code_change/3`, rollback, and permanence as the concrete governance ritual, bounded explicitly to routing evidence.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- release installation, failure rollback, and permanence resemble evaluation and retention, but the documentation does not establish candidate search or improvement-relative evaluation; treating it as an instance would overread an operator-directed deployment mechanism.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- the release handler is a good illustration of structure exposing control surfaces, but that general connection is secondary to the explicit pricing-attestation role requested here.
- [Repair dispositions for defeated claims](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) -- its Erlang mention records the review episode; the two theory notes are the durable claims this source should support.
- Agent-memory and agentic-system governance reviews -- their versioning and gate mechanisms are comparison cases, not direct consumers of OTP release documentation.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- The user-named `kb/notes/a-domain-priced-exception-does-not-refute-an-idealization.md` was replaced during this work by the current domain-pricing note; the candidate above targets the path that exists now.

## Flags

None
