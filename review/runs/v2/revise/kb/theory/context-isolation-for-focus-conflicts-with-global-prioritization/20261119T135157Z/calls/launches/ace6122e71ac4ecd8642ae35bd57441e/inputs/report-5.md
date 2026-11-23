---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/role-in-the-kb-gate.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 98f7838948665034dd2b847d164d723c388dd02ebf7eb40e06bc45766ad3b663
outcome: report
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role
launch: d7347748d00b4ed78be0338203f9cabd
completed-at: '2026-11-19T14:06:07Z'
findings:
- scope: document
  quotes: []
  reason: SUPPLIED — kb/reference/where-change-candidates-come-from-in-commonplace.md
    — needs a see-also explanation of why local noticing channels require a separate
    wide-shallow triage pass instead of prioritizing fixes inside the task that noticed
    them; supplied by the isolation-prioritization conflict, the narrow-deep execution
    versus wide-shallow triage split, and the mid-task noticing and cross-surface
    queueing illustrations.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md
    — needs reciprocal abstracted-from attribution citing the Nostalgebraist account
    of earnest low-value tangents and Anthropic's babysitting urgency-flattening quotes
    as motivating origin rather than corroboration; supplied by the verbatim quotes,
    the Scope origin-not-corroboration caveat, and the reciprocal Relevant Notes entry.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/architecture-README.md — needs a tag-head citation showing
    why bounded-context execution and global prioritization require separate narrow-deep
    worker and wide-shallow triage views, and the interface friction between them;
    supplied by the two-view split section and the residual interface friction section.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/context-engineering-README.md — needs a tag-head citation
    showing why scoping context for per-window focus removes the live comparison set
    global prioritization requires, forcing a narrow-deep execution versus wide-shallow
    triage split; supplied by the opening argument and the execution-triage split
    section.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/goal-prioritization-README.md — needs a tag-head citation
    stating that isolating an agent for task focus removes the live comparison set
    relational prioritization requires, flattening urgency and tangents unless execution
    is split from wide-shallow triage; supplied across the opening thesis, failure-mode
    bullets, execution-triage split, and relational-prioritization scope.
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent, compounding
    the oracle asymmetry analyzed in [a guard against a conjectured requirement removes
    the experiment that would test it](./a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md).
  reason: SUPPLIED — kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md
    — needs a contrasts citation isolating the context-scoping mechanism (missing
    system-wide complexity budgets and competing work inside isolated windows) that
    compounds test-oracle asymmetry in local over-specification; supplied by the local
    over-specification bullet and the missing-comparison-set account.
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md
    — needs a contrasts citation exposing the opposing cost of context isolation:
    aiding focus and decorrelated verification while removing the comparison set required
    for global prioritization and escalation calibration; supplied by the opening
    isolation trade-off, the uncalibrated escalation bullet, and the reciprocal Relevant
    Notes contrast.'
- scope: document
  quotes: []
  reason: SUPPLIED — kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md
    — needs an exemplifies citation to the narrow-deep execution versus wide-shallow
    triage split instantiated by logging noticed defects for a later pass instead
    of prioritizing them inside a focused reading context; supplied by the execution-triage
    split and the mid-task noticing illustration.
- scope: document
  quotes: []
  reason: PARTLY SUPPLIED — kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md
    — needs an extends citation identifying context isolation as a structural reason
    stopping and redirection degrade when interactive oversight is removed, plus the
    narrow-deep execution versus wide-shallow triage split; the note supplies the
    execution-triage split and shows that isolation removes the comparison set needed
    for relational stopping, deferral, and avoiding low-value tangents, but its body
    does not analyze the removal of interactive oversight or name redirection (that
    bridge appears only as a gloss in Relevant Notes, while the body cites unattended
    note revision only as one ADR 138 illustration and notes that local stopping under
    injected rules stays within an isolated worker's competence).
- scope: document
  quotes: []
  reason: SUPPLIED — kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md
    — needs a contrasts citation developing the rival mechanism—missing live competing-work
    context inside isolated task windows—rather than unequal oracle discrimination
    across iterations; supplied by the missing-comparison-set account and the reciprocal
    Relevant Notes contrast.
contract: report
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role/calls/launches/d7347748d00b4ed78be0338203f9cabd/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role/artifact/reviews/399f634c9da840717e4281ef/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T135157Z/role/calls/launches/d7347748d00b4ed78be0338203f9cabd/outputs/review.md
raw-output-sha256: 34ce33c744375781e73b67928fb7c1fee39944b42cae52e9093b8ab0da698b02
---

# Role in the KB: Context isolation for focus conflicts with global prioritization

## Role

Ten files link to this note—three tag heads, five theory notes, one reference survey, and one source ingest—all through index bullets or footer link annotations rather than inline prose arguments. Across those citations, the note serves as the KB's structural account of why context isolation for per-window focus removes the live comparison set required for global (relational) prioritization, explaining priority flattening (uncalibrated escalation, earnest low-value tangents, and local over-specification) as a rival or compounding mechanism alongside oracle-asymmetry accounts. It also supplies the **narrow-deep execution** versus **wide-shallow triage** split—and its interface friction—as the architectural pattern cited for deferring locally noticed defects and structuring unattended work.

Relied on: context isolation removing the live comparison set for global/relational prioritization; uncalibrated escalation (escalation calibration), earnest low-value tangents, and local over-specification (missing complexity budgets and competing work compounding test-oracle asymmetry); the narrow-deep execution versus wide-shallow triage split and its interface friction; mid-task noticing deferral as an instantiation; Nostalgebraist/Anthropic origin-not-corroboration attribution. Unused: local technical assessment caveat; `universal` claim mode and falsification condition; human-specialist versus stateless-agent contrast; indiscrimination versus default failure direction (including the silent-continuation default); insufficiency of standing priority instructions in static context; the term **scale-bearing local facts**; unbundling the three stop/retain/act decisions; the ADR 138 and unresolved-frontier illustrations; the three specific interface-friction sub-mechanisms (compression hides emergencies, tractability bias in global scans, local micro-prioritization); non-relational scope caveats (small single-thread tasks, intrinsic local checks, objective choice); open questions.

## Dependents

- `kb/reference/where-change-candidates-come-from-in-commonplace.md` — `see-also` explanation of why local noticing channels need a separate wide-shallow triage pass instead of prioritizing fixes inside the noticing task (`SUPPLIED`).
- `kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md` — reciprocal `abstracted-from` attribution for Nostalgebraist's tangent account and Anthropic's babysitting urgency-flattening quotes as origin, not corroboration (`SUPPLIED`).
- `kb/tags/architecture-README.md` — tag-head index entry for the narrow-deep worker versus wide-shallow triage split and the interface friction between them (`SUPPLIED`).
- `kb/tags/context-engineering-README.md` — tag-head index entry for per-window focus scoping removing the live comparison set and forcing the narrow-deep execution versus wide-shallow triage split (`SUPPLIED`).
- `kb/tags/goal-prioritization-README.md` — tag-head index entry for context isolation removing the relational-prioritization comparison set, flattening urgency and tangents unless execution is split from wide-shallow triage (`SUPPLIED`).
- `kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md` — `contrasts` citation to the context-scoping mechanism (missing complexity budgets and competing work) that compounds test-oracle asymmetry in local over-specification (`SUPPLIED`).
- `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` — `contrasts` citation exposing isolation's countervailing cost to global prioritization and escalation calibration alongside its benefits for focus and decorrelated verification (`SUPPLIED`).
- `kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md` — `exemplifies` citation to the narrow-deep execution versus wide-shallow triage split instantiated by logging noticed defects for a later pass (`SUPPLIED`).
- `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md` — `extends` citation identifying context isolation as a structural reason stopping and redirection degrade when interactive oversight is removed, plus the narrow-deep execution versus wide-shallow triage split (`PARTLY SUPPLIED`: the split and relational-stopping/tangent mechanism are supplied, while removed interactive oversight and redirection appear only in the footer gloss).
- `kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md` — `contrasts` citation developing missing live competing-work context inside isolated task windows as a rival mechanism to unequal oracle discrimination across iterations (`SUPPLIED`).

## Duplication

None. All ten supplied inbound passages are one-line tag-head entries or footer relation glosses rather than prose passages restating the note's claims.

## Untaken recommendations

None. No supplied inbound passage recommends a change to the note.

## Reach

- **Core conflict (context isolation for per-window focus removes the live comparison set required for global/relational prioritization):** `kb/tags/context-engineering-README.md`, `kb/tags/goal-prioritization-README.md`, `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md`, `kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md`, `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md`.
- **Narrow-deep execution versus wide-shallow triage split (terms and architectural separation):** `kb/reference/where-change-candidates-come-from-in-commonplace.md`, `kb/tags/architecture-README.md`, `kb/tags/context-engineering-README.md`, `kb/tags/goal-prioritization-README.md`, `kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`, `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md`.
- **Uncalibrated escalation / flattened urgency, earnest low-value tangents, and origin-not-corroboration source attribution:** `kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md`, `kb/tags/goal-prioritization-README.md`, `kb/theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md` (escalation calibration).
- **Local over-specification compounding test-oracle asymmetry:** `kb/theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md`.
- **Interface friction between the narrow-deep and wide-shallow views:** `kb/tags/architecture-README.md`.
- **Mid-task noticing / logging deferral as an instantiation of the split:** `kb/reference/where-change-candidates-come-from-in-commonplace.md`, `kb/theory/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`.
- **Footer bridge linking isolation to stopping and redirection under removed interactive oversight:** `kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md`.
- **Reaches no current dependent:** changes to the local technical assessment caveat, the `universal` claim mode and falsification condition, the human-specialist versus stateless-agent contrast, the indiscrimination-versus-default-direction distinction (and silent-continuation default), the standing priority instructions argument, the term **scale-bearing local facts**, the three-decision unbundling, the ADR 138 and unresolved-frontier illustrations, the individual interface-friction sub-mechanisms (provided interface friction as a topic remains), the non-relational scope caveats (small single-thread tasks, intrinsic local checks, objective choice), or the open questions.
