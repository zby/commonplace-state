---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
note: kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
note-sha256: 5a63717021753277685b88f170f090dd0e2fa563e00ac9299ad4debbce2230cb
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T112355Z
launch: cc957d3f07c54d38882aedb1ab764406
completed-at: '2026-11-16T11:26:46Z'
findings:
- scope: passage
  quotes:
  - The stronger design is a workshop surface
  reason: This supporting design claim invites reliance across active-work systems
    generally, but the only exercised case is one single-user, repo-local Claude Code
    kit. That kit's read-back faithfulness is untested, and the linked ingest's limitations
    note that teams, regulated audit or non-git work may need different machinery.
    No transfer relation or conjecture marking covers that surplus. The finding is
    INFO because the claim is supporting, not central.
  level: info
contract: verdict
target-sha256: 8a85c650bd4b4d5d87aec905cd5158d082723035defc6f5e48a8490d50b93c1d
target-capture: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/19aa698f7e4913d843642162/inputs/target/kb/theory/active-work-state-is-not-retrospective-memory-or-chat-history.md
observation: kb/reports/state/review/runs/v2/20261116T112355Z/artifact/reviews/19aa698f7e4913d843642162/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/20261116T112355Z/calls/launches/cc957d3f07c54d38882aedb1ab764406/outputs/review-unwarranted-scope.md
raw-output-sha256: b78f125797ef3e40a0e2f507f91ac488c37ccba4abe9919f1d7239efdbfaffaa
---

# Review

Claimed scope of the central claim: in agent systems that retain state across sessions, active work state is distinct from retrospective memory and chat history, and collapsing them preserves the wrong state.

Support on the page: the claim is mainly a derivation. Each surface is defined by the question it answers, and the failure on collapse follows from what each surface lacks. Linked notes supply inherited results: the workshop-layer lifecycle, the separation between "retrospective memory" and "active work" in serve-multiple-consumers, the session-history and chat-history notes, and storage vs activation. The kit and the practitioner ingest supply one worked case.

The derivation's premises hold for the whole claimed class: any chronological trace lacks liveness ordering, and any lesson store lacks closure fields unless extended. The central scope is therefore covered by derivation rather than by the single case.

The design paragraph reaches further. Its preference for a pointer-plus-ledger workshop surface, and the requirement for executable validators in higher-authority systems, rest on one kit. That is a non-central overreach.
