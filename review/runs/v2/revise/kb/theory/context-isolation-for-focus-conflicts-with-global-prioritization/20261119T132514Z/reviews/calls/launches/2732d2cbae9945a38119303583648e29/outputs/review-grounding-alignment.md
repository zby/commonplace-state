---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "a general priority rule cannot order a local branch against competing work the worker cannot see"
    reason: "The intent note claims that an intent controls a local choice only when it changes which live alternatives are admissible, preferred or sufficient to stop. A high-level purpose compatible with every live option needs a bridge. The note applies this to a rule like 'focus on high-leverage work', whose discrimination among local options depends on the worker knowing relative leverage, which requires unseen work. The transfer is plausible, and the next sentence supplies the bridge idea (static rules can eliminate named non-priorities). Still, the step from 'cannot see the competing work' to 'the rule does not distinguish the live alternatives' is left implicit."
    level: info
outcome: pass
---

# Review

## Linked library artifacts

- **Context efficiency note.** It says feasibility, the per-window face, binds first. The note invokes exactly that.
- **Intent note.** The invoked claim matches the title claim. The application to standing priority rules is a reasonable transfer with one implicit step (see finding).
- **Guard note.** The note invokes test-oracle asymmetry pushing local guarding, which matches the target's description.
- **Bounded-context orchestration.** It is cited only as "consistent with". The target separates a scheduler holding state from bounded calls that receive less than the full state. The citation makes no stronger claim than that.
- **Insufficient-summary note.** The target says an insufficient summary keeps the source path in any reliability-compliant route, and that skipping it is unsafe substitution. The note's "fall back to deep context or ... misclassify severity under unsafe substitution" matches this at the target's scope.
- **Traversal-logging note.** The target separates noticing from fixing through a one-line log entry. Represented accurately.
- **ADR 138.**
  - The ADR says a stop ends the run with a continuation record. Represented accurately.
  - Kept answers carry over so later runs do not re-ask. Represented accurately.
  - Rewrite runs are separate commands. Represented accurately.
  - Overall the note's mapping to the three decisions is a fair illustration and is scoped as one.
- **Unresolved frontier definition.** Quoted accurately ("discoverable field of possible further work").
- **Epistemic-layer note.** Cited only for the boundary that allocation does not choose objectives. The citation is adjacent, not evidential.

## Quoted sources

The Nostalgebraist quotations are marked verbatim and paired with the ingest link. On the page:

- The babysitting quotations support equal-urgency escalation, and the note attaches the qualification that the account does not isolate worker from workflow causes.
- The "silly low-value tangents" and "Everything is flattened out" quotations support earnest tangents and flattened importance.

None of these reads as lifted from a qualifying context. The note limits all of them to origin, not corroboration.
