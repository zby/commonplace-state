---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: Plans and Resource-Bounded Practical Reasoning (Bratman, Israel and Pollack, 1988)

**Source:** [Ingest: Plans and Resource-Bounded Practical Reasoning](../../../../sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` / `abstracted-from` / `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting skipped: the only external target is the already-recorded `source` URL. Reverse edges checked against `kb/theory/COLLECTION.md` labels (`evidenced-by` to sources, with the unquoted-source limit of five).

**Already linked from the source (known):** eight targets in the ingest's Connections Found and Learning Claims; all resolve.

**Curated heads:**
- `kb/tags/goal-prioritization-README.md` (the source's tag) -- not `complete: true`; it says sources are linked by hand. Lists productive-deferral, intent-controls, lightweight-search-control and open-ended-improvement under effort allocation; the source is not listed.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` filtered with `rg -i "commit|defer|stop|reconsider|revis|reopen|deliberat|bounded|cost|trigger|plan|intent|stab|retain|cheap|filter|search|worth|invest"` -- flagged: Checking retained results trades cost against reliance risk; Current-task fit alone does not warrant costly structural entrenchment; Lightweight search control allocates further search without licensing adoption; Reflection makes retained lessons second-order; Commitment, not derivation, creates new ground truth; A theory's prototype standing is its revision cost; Theory building and capacity building make the same kind of fallible commitment; Periodic KB hygiene should be externally triggered.
- Same listing over `kb/sources/ --glob '*.ingest.md'` filtered for `simon|satisf|bounded|plan|intention|agent|deliberat|metareason|practical|decision|commit|option|anytime` -- flagged: Provably Bounded-Optimal Agents; The Architecture of Complexity (Simon); the four already-known sibling sources.

**Descriptions:** read for each flagged title; plus `kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md`, `kb/sources/bdi-agent-architectures-a-survey.ingest.md`, `kb/sources/provably-bounded-optimal-agents.ingest.md`.

**Body search:**
- `rg -n -i "reconsider|commitment|bratman|intention|BDI\b|deliberation cost|metareason|value of computation|stability of (plan|commitment)"` over theory, reference, agentic-systems, agent-memory-systems, tags -- too broad (60+ files); used only to locate commitment notes.
- `rg -n -i "bratman|IRMA|\bBDI\b|reconsideration|reopen(ing|ed)? (a |the )?(decision|commitment)|deliberation cost|value of (computation|information)|metareason"` over all destinations -- `IRMA` matched "confirmation" noise; real hits: reasoning-limits (neutral/guided reconsideration), reusable-commitment-support proposal (cites Russell-Wefald), Wooldridge and SEP ingests. Nothing in agentic-systems or agent-memory-systems concerns reconsideration policy.
- `rg -l -i "bratman|belief-desire|intention reconsideration|bounded rationality|satisficing"` over sources, theory, reference -- BDI survey ingest (5 Bratman mentions, no link to this ingest), SEP ingest, Wooldridge ingest; theory hits are passing Simon mentions (information-value, soft-bound traditions), rejected.
- `rg -n -i "reconsider|revisit|reopen"` in on-balance and productive-deferral notes -- productive-deferral transfers a reopened choice to a decision procedure; on-balance has no reconsideration-policy treatment.

**Link following:**
- Source links of candidate theory notes (`rg -o '\.\./sources/...'`): on-balance, intent-controls and checking-retained-results cite no sources; productive-deferral already cites five unquoted sources (at the theory collection's limit); reasoning-limits cites two.
- `kb/theory/COLLECTION.md` outbound section read for reverse-edge labels.

**Candidate evaluations:**
- checking-retained-results -- kept: same structure as caution/boldness (check cost against reliance risk; accepting risk between checks as explicit choice).
- lightweight-search-control -- kept: the filter override readmits an option to deliberation without adopting it.
- current-task-fit / entrenchment -- kept: stability-vs-revocability of plans against reversible adoption vs costly entrenchment.
- BDI survey ingest -- kept: sibling source; the survey reports plan-library learning as open work, which this ingest identifies as the paper's omission.
- reflection-makes-retained-lessons-second-order -- kept as compares-with: names the operation (lesson targeting a prior commitment) that IRMA lacks for its plan library.
- Others rejected (see Rejected Candidates).

### Candidate origins

- kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md — titles, descriptions
- kb/theory/lightweight-search-control-does-not-license-adoption.md — curated-head, titles
- kb/theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md — titles
- kb/theory/reflection-makes-retained-lessons-second-order.md — titles
- kb/sources/bdi-agent-architectures-a-survey.ingest.md — titles, body-search
- kb/sources/sep-practical-reason.ingest.md — known, body-search
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — known, body-search
- kb/theory/intent-controls-choices-by-distinguishing-live-alternatives.md — known, curated-head
- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — known
- kb/theory/reasoning-limits-may-select-for-design-commitments.md — known, body-search
- kb/theory/productive-deferral-requires-option-evidence-and-convergence.md — known, curated-head

## Connections Found

- [Checking retained results trades cost against reliance risk](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) -- **compares-with**: same two-sided policy on when to reopen a retained result; the note trades check cost against stale-reliance risk and accepts risk between checks as an explicit choice, the paper trades wasted against missed reconsideration and proves no trigger avoids both. Best landing for Extractable Value item 2 (Commonplace review and re-ingest triggers).
- [Lightweight search control does not license adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) -- **compares-with**: the filter override has exactly lightweight authority; it readmits an option to deliberation but only deliberation can replace an intention, so the paper is a classical architecture separating attention allocation from adoption.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- **compares-with**: on the axis of how hard a commitment should be to reopen; the paper justifies stability by deliberation savings while keeping plans revocable and partial, the note confines costly entrenchment to enduring constraint, transfer warrant or coordination value.
- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) -- **compares-with**: on the axis of operations on a retained commitment; IRMA has rejection of intentions driven by belief change but no lesson that rejects, rescopes or revises a plan-as-recipe, which is the gap the ingest's Learning Claims identifies.
- [BDI agent architectures: a survey](../../../../sources/bdi-agent-architectures-a-survey.ingest.md) -- **compares-with**: the survey reports the lineage this paper founded and states that plan libraries are hand-written and learning them is open work, confirming that the outcome-to-recipe step this ingest marks as missing stayed missing in later BDI languages.

## Bidirectional Candidates

- [BDI agent architectures: a survey](../../../../sources/bdi-agent-architectures-a-survey.ingest.md) <-> source -- **compares-with**: the survey ingest mentions Bratman five times without linking the primary statement; a return link lets its reader check the original account of deliberation and filtering.
- [SEP: Practical Reason](../../../../sources/sep-practical-reason.ingest.md) <-> source -- **compares-with**: the SEP ingest discusses Bratman's plans as defeasible constraints second-hand; a return link reaches the architectural statement and its reconsideration taxonomy.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: its item 3 notes IRMA's missing weighing criterion; the primary paper confirms the criterion is set aside as a common design problem.

## Reverse-edge Candidates

- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) → source -- **evidenced-by**: qualifies the note's set of control routes; IRMA's filter override is a readmission route the note lacks. The note cites no sources, so the unquoted-source limit is not a constraint.
- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) → source -- **evidenced-by**: bounds the investigation rule with a classical case where deliberation cost sits inside the comparison (Situations 2, 4a, 4b) and the override policy is judged on balance across cases. A qualifying, not corroborating, phrase is required since the paper does not test the note's claim.
- [Reasoning limits may select for design commitments](../../../../theory/reasoning-limits-may-select-for-design-commitments.md) → source -- **evidenced-by**: an established precedent that bounded reasoning motivates stable commitments; it bounds rather than corroborates, since the paper says nothing about the human-versus-model comparison.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../theory/productive-deferral-requires-option-evidence-and-convergence.md) -- already linked from the source; as a reverse edge it would be the sixth unquoted tracked source, exceeding the theory collection's unquoted-source limit unless a quote is retained or another citation dropped.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- about unentailed resolutions becoming ground truth at commit; the paper's commitment is a computational economy device, so the shared word is a keyword match.
- [A theory's prototype standing is its revision cost](../../../../theory/prototype-standing-is-revision-cost-binding-plus-lost-investment.md) -- revision cost of stated theories; the paper's cost is deliberation time, not binding or lost investment. Adjacent but would mislead.
- [Theory building and capacity building make the same kind of commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) -- plans are not stated theories (the ingest itself judges them weak as theory); too indirect.
- [Periodic KB hygiene should be externally triggered](../../../../theory/periodic-kb-hygiene-should-be-externally-triggered-not-embedded-in.md) -- trigger placement, not trigger tuning; checking-retained-results carries the trade-off better.
- [Provably Bounded-Optimal Agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) -- another bounded-rationality answer, but Russell-Wefald (already linked) is the closer comparison; adding it would be a see-also spray.
- [Reusable commitment support across kinds of knowledge work](../../../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md) -- "reconsideration" there is a project milestone trigger; no shared mechanism.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- passing Simon mention only.

## Index Membership

- [Goal prioritization](../../../../tags/goal-prioritization-README.md) -- the head links sources by hand; the source fits "Allocating effort under uncertainty" as the classical account of how much deliberation to spend on reopening adopted commitments and why no reconsideration policy avoids both error directions.

## Synthesis Opportunities

The paper's caution/boldness trade-off, [checking retained results trades cost against reliance risk](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) and [lightweight search control does not license adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) together suggest a general claim: any trigger for reopening a retained commitment (review, re-ingest, re-check) is a cheap, defeasible filter whose authority stops at allocating attention, and its policy can be judged only across cases, never per case. No existing note states this for reconsideration triggers as such.

## Maintenance Observations

- `kb/theory/productive-deferral-requires-option-evidence-and-convergence.md` sits at the five-unquoted-source limit; further source evidence there requires retained quotes.
- The BDI survey ingest (untracked at time of run) discusses Bratman substantively without linking this ingest; both were ingested the same day.

## Flags

- The source's existing Connections Found is already dense (eight targets); the five new candidates should be weighed against the ingest's stated occasion (the deliberative-learning workshop) before all are added.
