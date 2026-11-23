---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/fishkin-mansbridge-deliberative-democracy-intro.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Introduction (Fishkin and Mansbridge, Daedalus 2017, deliberative democracy)

**Source:** `kb/sources/.snapshots/fishkin-mansbridge-deliberative-democracy-intro.md` (not linked: snapshots are ignored and have no paired ingest yet)

The source is an immutable snapshot. No `fishkin-mansbridge-deliberative-democracy-intro.ingest.md` exists yet. Every outbound candidate below is for that future ingest, which would be the authored connection surface. Candidates are judged from the introduction alone. It summarizes the issue's essays in a sentence or two each, so claims that depend on those essays (Manin, Lafont, Siu, Lupia and Norton) are thin here.

Source claims used for judging: (1) deliberation is "weighing" competing arguments with good information in civil, diverse discussion; (2) a mini-public's rationale is that a representative random sample deliberating under good conditions shows what the population would think under those conditions, so much depends on representativeness and on the account of good conditions; (3) Schumpeter's competitive model yields a "manufactured will", in which leaders shape the will meant to legitimize them, so "the normative causal arrow goes in the wrong direction"; (4) Lafont: a citizen outside a mini-public cannot know whether she would have joined the post-deliberation majority, so binding it means "blind deference"; (5) inequality among participants can distort outcomes, which remains an open empirical question.

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` "Outbound links". Destinations scanned: theory, reference, agent-memory-systems, agentic-systems, tags, other sources. Excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting was skipped. The only external target is the source's own URL, which the ingest would cite under `derived-from`.

**Context check (excluded destination, read only to know why the source was captured):**
- `rg -il "on-balance|on balance" kb --glob '*.md' --glob '!kb/reports/**'` found the workshop `kb/work/learning-method-name/`. Its `draft-definition.md` (section "The basis: deliberation") cites this article's URL as the group-deliberation basis for the term "deliberative learning". The README records the rename to "deliberative learning". This tells us the article's main use is definitional support for weighing reasons. No candidate is proposed into `kb/work/`.

**Curated heads:**
- The snapshot has no `tags:`. `kb/tags/self-improving-systems-README.md` declares `complete: true`, so no by-tag `rg` was run for that tag. `kb/tags/evaluation-README.md` was not read in full; the candidates relevant to evaluation came from titles and body search.

**Titles listing (theory):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i "judg|balanc|weigh|argu|critic|review|consensus|disagree|group|plural|divers|adversar|debate|objective|legitim|representativ|sampl|reason|evaluat|deliber|commit|decision"`. This flagged: "On-balance judgments can guide improvement without a global measure" (kept); "Decorrelated reviewers still share the field's prior..." (kept); "Self-improvement is relative to a declared objective" (kept); "An adversarial human-agent loop can reconstruct the writing-is-thinking filter" (rejected); "Reasoning production is not reasoning evaluation" (rejected); "Revising an improvement objective is licensed from outside it or is not improvement" (rejected); "Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions" (rejected); "Routine approvals do not show that human judgment is dispensable" (rejected).
- Paths were resolved with `rg -l -F -x '# <title>' kb/theory`.

**Body search:**
- `rg -il "deliberat" kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/**'`: about 50 hits. Almost all use "deliberately" in passing (ADRs, proposals, theory). None treats deliberation as weighing reasons. Spot checks of `commonplace-doctrine.md`, `theory-and-methodology-form-a-two-layer-execution-system.md`, `claim-modality-is-the-inference-form-of-the-refuter.md` and `commitment-not-derivation-creates-new-ground-truth.md` confirmed only incidental use.
- `rg -n "deliberat|Fishkin|Mansbridge|mini-public|weigh"` over the on-balance, epistemic-stance, declared-frame and self-improvement notes: only the on-balance note weighs considerations substantively (lines 27–35, 65: "the weighing of whose costs count cannot be checked that way").
- `rg -n -i "debate|adversarial principle|opposing positions|competing arguments|weigh(ing)? (competing|reasons|arguments)" kb/theory kb/agentic-systems kb/reference kb/tags`: `synthesis-is-not-error-correction.md` mentions multi-agent debate only as a topology result. This was rejected as keyword-only for this source.
- `rg -il "deliberat|weigh.*reason|reflective equilibrium|mini-public|jury|consensus" kb/sources --glob '*.ingest.md'`: the hits that mattered are `wooldridge-jennings-intelligent-agents.ingest.md` (deliberative agent), `making-reflective-equilibrium-precise.ingest.md` (weighted revision of judgments) and `epistemic-case-study-competition.ingest.md` (missing-perspective detection, crux handling). The rest matched "consensus" incidentally.
- `rg -il "deliberat" kb/agentic-systems kb/agent-memory-systems --glob '*.md' --glob '!**/reports/**'`: 10 reviews matched, all on "deliberately". Neither collection yielded a candidate.
- Reference: no candidate. Only the incidental "deliberately" uses above.

**Link following:**
- From `making-reflective-equilibrium-precise.ingest.md` line 37 to the on-balance note. That ingest already ties a formal weighted-sum model to the note's question of which weights deserve consideration. This confirms the on-balance note as the hub where weighing sources land.
- From the on-balance note "Relevant Notes" to `self-improvement-is-relative-to-a-declared-objective.md`. Its section "The causal clause does not close the post-hoc gap" (independent specifiability of the objective) is the comparison point for the manufactured-will argument.
- From the reviewers-prior note to `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`. Reviewed and not kept: the source has no oracle or error-rate content.
- `ls kb/sources/.snapshots | rg -i "delib|...|reason|equilib"` showed a `sep-practical-reason.md` snapshot with no tracked ingest, so no link target exists for it.

### Candidate origins

- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — titles, body-search, link-following
- kb/theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md — titles
- kb/theory/self-improvement-is-relative-to-a-declared-objective.md — titles, link-following
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — body-search
- kb/sources/making-reflective-equilibrium-precise.ingest.md — body-search

## Connections Found

All of these are for the future `kb/sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md`.

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) -- **compares-with**: weighing competing considerations without a global score. Both define a good judgment by reasons weighed rather than a single measure. Fishkin and Mansbridge add group-level conditions: good information, balance, diverse participants and competing experts. The note's "whose costs count" (the library-hours case) parallels Lafont's objection: a citizen who did not deliberate cannot tell whether the majority's weighing is hers. Both texts say the factual part of the reasons can be checked while the weighing cannot simply be delegated. This is the primary edge.
- [Decorrelated reviewers still share the field's prior, so read their findings by the claim's stance](../../../../theory/reviewers-share-the-fields-prior-so-interpret-findings-by-stance.md) -- **compares-with**: why to sample a group of judges. A mini-public samples at random to reproduce the population's considered view, so a shared prior is the goal. Review gates use several judges to catch errors, and there a shared prior is the failure the note names. The comparison shows that "more diverse judges" serves opposite aims depending on whether one wants representation or error detection. The note gains a reason why diversity by sampling cannot remove a prior the whole population shares.
- [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- **compares-with**: a criterion produced by the process it is meant to judge. In Schumpeter's model, leaders manufacture the public will that is supposed to legitimize them, "the normative causal arrow goes in the wrong direction". This has the same structure as the note's relabelling case: an objective specifiable only by reference to the change it licenses is not antecedent. This is an analogy from politics, not evidence; keep it in the ingest's analysis rather than as support for the note.
- [Wooldridge and Jennings, Intelligent Agents (ingest)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) -- **compares-with**: two senses of "deliberative". This source uses it for weighing competing arguments among people. Wooldridge and Jennings use it for an agent architecture with a symbolic world model and logical action selection, with no weighing of reasons. A reader who meets "deliberative" in Commonplace needs the pair to see which sense is meant. That ingest is currently untracked.
- [Making reflective equilibrium precise (ingest)](../../../../sources/making-reflective-equilibrium-precise.ingest.md) -- **compares-with**: how competing considerations are weighed. That source makes weighing a fixed weighted sum and proves when results hold across weights. Fishkin and Mansbridge make it a discursive process under conditions that shape which arguments are heard. Both already bear on the on-balance note, so the pair marks the formal and the discursive ends of the same question.

## Bidirectional Candidates

- [Wooldridge and Jennings, Intelligent Agents (ingest)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: the disambiguation of "deliberative" is useful from both ends. A reader of the agent-architecture ingest should learn that the group-weighing sense also exists, and which sense a Commonplace term uses.

## Reverse-edge Candidates

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) → future ingest -- under the theory collection's own rules, the paragraph on "whose costs count" and the closing paragraph on criticizable reasons could cite the ingest as an external account of weighing competing arguments by a group. Check `kb/theory/COLLECTION.md` for the authorised label before authoring.
- Future theory definition `kb/theory/definitions/deliberative-learning.md` (planned destination in the workshop draft; does not exist yet) → future ingest -- when the draft is promoted, its group-deliberation basis should link the tracked ingest, not the bare URL. Under `kb/sources/COLLECTION.md` "Declaring how a source use is checked", a durable source-dependent claim links the ingest. The "weighing competing arguments" sentence should get a retained quote: "deliberation requires “weighing” competing arguments for policies or candidates in a context of mutually civil and diverse discussion in which people can decide on the merits of arguments with good information".

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- Manin's "adversarial principle" (confrontation of opposing positions) looks relevant. The introduction reports it in two sentences, though, with no mechanism. The comparison would rest on Manin's essay, which has not been captured.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) -- Bächtiger and Beste's Discourse Quality Index (whether deliberators justify assertions) touches route-versus-conclusion evaluation. The introduction only names the index; this is too thin.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- the manufactured-will point concerns where a criterion comes from, not revision of an objective. The self-improvement note is the closer target.
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) -- the question of how much decisional status a mini-public should have resembles delegating decisions. The source discusses delegation from citizens to a sample of citizens, not from people to a computational system, so the mechanism differs.
- `kb/theory/routine-approvals-do-not-show-that-human-judgment-is-dispensable.md` -- keyword match on "judgment"; no shared mechanism.
- [Synthesis is not error correction](../../../../theory/synthesis-is-not-error-correction.md) -- "debate" appears only as a multi-agent topology result; keyword-only.
- [Epistemic case study competition (ingest)](../../../../sources/epistemic-case-study-competition.ingest.md) -- its missing-perspective detection resembles the diversity condition. The overlap is a single requirement word with no shared argument.
- `kb/sources/.snapshots/sep-practical-reason.md` -- this is the individual-deliberation counterpart cited by the workshop draft, but it has no tracked ingest. Never link a snapshot; revisit once the ingest exists.

## Index Membership

None. Sources are outside tag participation. If the future ingest carries `tags:`, `evaluation` is the plausible candidate, pending a read of `kb/tags/evaluation-README.md` and its inclusion condition. The source's contribution is about judgment by weighing, not about evaluating KB artifacts, so this may not qualify.

## Synthesis Opportunities

None durable yet. A possible later claim: *what a group of judges is for decides whether a shared prior is a feature or a defect*. Representation (mini-publics) wants the population's prior reproduced under good conditions; error detection (review gates) wants errors decorrelated. It would join this source, the reviewers-prior note and the error-correction note. It needs a source that treats the representation aim in more depth than this introduction does.

## Maintenance Observations

- `kb/sources/wooldridge-jennings-intelligent-agents.ingest.md` and `kb/sources/minton-utility-of-ebl-aaai88.ingest.md` are untracked in git, and the workshop draft already links the first. Until committed, links to them from tracked artifacts would point at untracked files.
- The workshop draft cites this article by bare URL as a "page summary" read. Once an ingest exists, the draft's basis section can cite the ingest and retain the weighing quote. Per the draft, an SEP Practical Reason ingest is "in progress", and only its snapshot is present.

## Flags

- No ingest exists for this snapshot, so all outbound candidates wait on `cp-skill-ingest`.
- Its main use in Commonplace is definitional (the group sense of deliberation as weighing competing arguments). Its political-science findings, such as Deliberative Polling outcomes and inequality effects, are outside KB scope unless a note uses them as evidence about group judgment.
