---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The absence of a known change is evidence of freshness only if every relevant
    change reaches the checker.
  reason: 'DEFEATED — Universal (no stated mode): absence of a known change counts
    as evidence of freshness only when every relevant change reaches the checker.
    — Counterexample any reader can re-derive: if most but not all relevant changes
    are reported to the checker (say a hook catches edits inside the participating
    collections but misses tag changes made by a bulk script), then observing no reported
    change still raises the probability that the copy is fresh. It is partial evidence,
    not establishment. The section heading (''does not establish freshness'') and
    the last line (''Assurance dates from the last check'') state the defensible version;
    the sentence overstates it by turning ''establishes'' into ''is evidence of''.
    Repair: say ''establishes freshness only if'', or call partial notification weak
    evidence. The section''s role in the argument (assurance dates from the last check)
    survives. — LOCAL — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated, universal: a consumer can see when a retained result
    was last checked, so risk accepted between checks is an explicit choice and not
    a hidden consequence. — The note requires accepted risk to be ''an explicit choice
    rather than a hidden consequence of trusting the copy'' and says ''Assurance dates
    from the last check''. Neither the mark nor the connect report as described exposes
    the date of its last check to the reader. A reader who meets `complete: true`
    on a tag head cannot tell whether the head was validated an hour ago or months
    ago, so the risk that reader takes on is exactly the hidden kind the note rules
    out. The commitment survives if the note states that explicit acceptance needs
    a visible check time, or that the choice belongs to whoever sets the check schedule
    and not to each consumer. — LOCAL — instance'
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: 'DOUBTFUL — Universal as stated: check frequency is set by trading check
    cost against reliance risk, which treats the two as commensurable and as the deciding
    factors. — Two cases dent this. (a) When relying on a wrong result has severe
    or irreversible consequences, practice often treats checking as a constraint that
    no cost saving can buy out, not as one side of a trade. (b) Check timing is often
    fixed by event triggers or workflow opportunity, not by a cost-risk choice. The
    note''s own mark example works this way: the check runs whenever the head is next
    validated. The trade-off then fixes only which triggers to install, not how often
    checks run. The commitment holds as a qualitative ideal for discretionary checks;
    Scope should say that it does not cover mandatory checks or trigger-bound timing.
    — LOCAL — priced-exception'
- scope: passage
  quotes:
  - so one production is amortized over many uses
  reason: 'DOUBTFUL — Universal as stated: a retained derived result saves work because
    its production is amortized over many uses. — Counterexamples: results retained
    but consumed once or never, such as most connect reports for a single linking
    pass; and cheap derivations, such as a one-hop rg membership listing, where reading
    and trusting the copy costs about as much as re-deriving it. In both, retention
    creates reliance risk without the matching saving. The premise holds for results
    that are reused and expensive to derive, which the linked recompute-cost note
    grounds. The commitment needs only that condition stated. — LOCAL — instance'
- scope: passage
  quotes:
  - A retained result goes stale because its source and the copy have separate update
    paths.
  reason: 'DOUBTFUL — Causal premise, unqualified: retained results go stale because
    source and copy update separately. — A result derived from immutable or content-addressed
    inputs, such as a commit-pinned snapshot or a hash-keyed derivation, cannot go
    stale, so its staleness risk is zero and the trade-off collapses to checking for
    derivation error only. Those results can still be wrong without being stale, a
    separate risk the note names (''stale or wrong'') but explains only through staleness.
    This qualifies the scope; it does not threaten the commitment. — LOCAL — instance'
- scope: passage
  quotes:
  - This requires that the consumer actually stops and that the suppressed search
    would find more task-relevant material.
  reason: 'HOLDS — Conditional premise: a stale copy hides its own error only when
    the consumer stops on it and the suppressed search would find more. — The note
    states both conditions and fences prevalence out in Scope. A hunt for a case where
    suppression occurs without stopping, or causes harm without missed relevant material,
    found none that the conditions do not already exclude.'
- scope: passage
  quotes:
  - when verification is cheaper than derivation, checking on every use can still
    save work
  reason: 'HOLDS — Conditional: checking spends part of the saving, full recomputation
    on every use largely defeats it, and checking cheaper than derivation can still
    save work. — The claim is hedged (''largely'', ''can''). Counterexample hunt,
    for example verification that costs as much as derivation, falls outside the stated
    condition.'
- scope: passage
  quotes:
  - An inexpensive, defined check on a claim that authorizes stopping makes enforcement
    attractive.
  reason: HOLDS — The completeness mark's check is inexpensive and defined (one-hop
    reach over tagged artifacts in named collections), and these properties favour
    enforcement. — Membership derivation is a scan plus link lookup that stays cheap
    relative to judgment as the KB grows. The note limits the check to reach given
    the tags and leaves tag fit to semantic review, so a wrongly tagged artifact does
    not count against the premise.
- scope: passage
  quotes:
  - Some properties remain mechanically checkable, such as link resolution and required
    sections, but checking them does not reconstruct that judgment.
  reason: HOLDS — Assessing connect-report candidates needs judgment that mechanical
    checks do not reconstruct, and the report's dependency set spans everything the
    pass searched. — A hunt for a mechanical rule that replaces candidate assessment,
    for example a lexical or embedding threshold, found only heuristics whose output
    still needs evaluation against the target's claim. The premise stands.
- scope: passage
  quotes:
  - The mark's contract supplies the first three; nothing in it establishes the fourth.
  reason: 'HOLDS — A mechanical check needs a judgment-free rule, a locatable copy
    and source, a source available at check time, and a trustworthy enough checker;
    the mark supplies the first three. — Each condition is necessary: drop any one
    and the check either cannot run or cannot be relied on. The note claims only that
    they make a check possible and worth relying on, not that they are sufficient
    for currency. No counterexample found.'
outcome: report
description: Retained report review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/ff6fe46d2b975967b570ccba/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/ff6fe46d2b975967b570ccba/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 7c06e40f73d049daa371616747d8ce51
completed-at: '2026-11-18T16:04:52Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/7c06e40f73d049daa371616747d8ce51/outputs/review.md
raw-output-sha256: b538f6a24dbe7118130854d6a4947d335867e9eb4ed30cbfb2249a1b5890b356
format: 2
---

# Premise decomposition: Checking retained results trades cost against reliance risk

**Register:** claim
**Central commitment (one sentence):** How often to check a retained derived result should be decided by weighing the cost of checking against the risk of relying on stale or wrong content, and accepting some risk between checks is right when it is an explicit choice.

## Premises and counterexamples

The commitment is a qualitative trade-off. It consumes three groups of premises.

- **The saving side:** retention amortizes one production over many uses, and checking spends part of that saving.
- **The risk side:** copies go stale through separate update paths, and a stale copy can suppress the search that would expose its gaps.
- **The explicit-acceptance side:** risk accepted between checks is visible as a choice, and no known change does not certify freshness.

The two worked examples, the completeness mark and the connect report, consume more premises about check cost, check definability and dependency breadth. The closing list of check requirements adds the conditions under which a mechanical check can carry part of that load.

No failure is global. The commitment is hedged throughout ('can be right', 'qualitative'), so the dents land on premises it consumes, and each can be repaired with a scope qualification:

- **The 'only if' sentence on freshness evidence** is the one checkable defeat. Partial change notification still gives some evidence of freshness.
- **The explicit-acceptance premise** is unstated, and it is the most consequential. The note never says how a consumer learns when a result was last checked. Without that, the accepted risk is hidden again.
- **The trade-off framing** is dented by checks that are mandatory and by check timing set by triggers rather than chosen. The note's own mark example is trigger-bound.
- **Amortization and staleness** need their conditions stated: the result must be reused and costly to re-derive, and its inputs must be mutable.

## For the human

Look first at the unstated premise that consumers can see when a retained result was last checked. Without it, the note's rule that accepted risk must be explicit has no mechanism for either of its examples.
