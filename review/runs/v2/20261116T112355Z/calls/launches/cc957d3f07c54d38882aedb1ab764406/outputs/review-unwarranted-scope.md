---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The stronger design is a workshop surface"
    reason: "This supporting design claim invites reliance across active-work systems generally, but the only exercised case is one single-user, repo-local Claude Code kit. That kit's read-back faithfulness is untested, and the linked ingest's limitations note that teams, regulated audit or non-git work may need different machinery. No transfer relation or conjecture marking covers that surplus. The finding is INFO because the claim is supporting, not central."
    level: info
outcome: pass
---

# Review

Claimed scope of the central claim: in agent systems that retain state across sessions, active work state is distinct from retrospective memory and chat history, and collapsing them preserves the wrong state.

Support on the page: the claim is mainly a derivation. Each surface is defined by the question it answers, and the failure on collapse follows from what each surface lacks. Linked notes supply inherited results: the workshop-layer lifecycle, the separation between "retrospective memory" and "active work" in serve-multiple-consumers, the session-history and chat-history notes, and storage vs activation. The kit and the practitioner ingest supply one worked case.

The derivation's premises hold for the whole claimed class: any chronological trace lacks liveness ordering, and any lesson store lacks closure fields unless extended. The central scope is therefore covered by derivation rather than by the single case.

The design paragraph reaches further. Its preference for a pointer-plus-ledger workshop surface, and the requirement for executable validators in higher-authority systems, rest on one kit. That is a non-central overreach.
