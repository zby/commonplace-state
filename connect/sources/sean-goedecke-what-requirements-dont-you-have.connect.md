---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/sean-goedecke-what-requirements-dont-you-have.md"
source_has_frontmatter: true
date: "2026-10-19"
depth: standard
---

# Connection Report: What requirements don't you have? (Sean Goedecke)

**Source:** [What requirements don't you have?](../../../../sources/.snapshots/sean-goedecke-what-requirements-dont-you-have.md)

The source is an immutable snapshot. All outbound candidates below are for the authored surface, the future `kb/sources/sean-goedecke-what-requirements-dont-you-have.ingest.md` (not yet present at report time). The ingest must link these targets, never the snapshot.

Source reading: the essay makes three moves. (1) Elegant designs come from deliberately dropping requirements (Unicorn, S3, StatsD, edge caches, SQLite, Cursor's git backend). (2) Choosing which requirements to drop needs joint business and technical judgment, which engineer–PM distrust often blocks. (3) Coding agents, shaped by RLVR and lacking business context, invent hypothetical requirements (mutexes, re-checks, TOCTOU guards, consistency edge cases). Goedecke's repairs are stating tolerances in the prompt ("stale is fine") and human review that scans for unrequested coordination. He claims that unchecked invented requirements "petrify" a codebase over time. The evidence is practitioner anecdote, including an unquantified "about half the time" review hit rate.

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md` § Outbound links. Destinations scanned: notes, reference, agent-memory-systems, agentic-systems, tags, sources. `kb/work/` and `kb/instructions/` are excluded. Labels: `derived-from` (external), `is-evidence-for` (notes, agent-memory-systems), `abstracted-from`/`rests-on` (notes), `compares-with` (notes, sources, ams, agentic-systems), `defined-in` (notes/definitions), `see-also` (sparingly).

**Description listing scan:**
- I did not run a scoped `rg '^description:'` over all of `kb/notes/`. I pulled descriptions for body-search hits instead (see below). Flagged: weakly-discriminated-qualities, fix-what-the-executor-cant-determine, agentic-systems-interpret-underspecified-instructions, brainstorming-maintainability-oracles, llm-output-deviation-requires-three-way-diagnosis, and the sibling sources why-llms-cant-make-your-code-simpler and simplification.

**Topic indexes:**
- `kb/tags/llm-reliability-README.md`: its inclusion condition (output deviation from intent: underspecification, interpreter failure, indeterminism) fits the source's agent section. Its lead entry is llm-output-deviation-requires-three-way-diagnosis, which became a candidate.
- `kb/tags/failure-modes-README.md` (`complete: true`): its scope is KB knowledge or claim failures. The source does not qualify, so no by-tag rg was run.
- `kb/tags/constraining-README.md`: I checked the description. The source's prompt-stated tolerances do narrow interpretation, but the three-way-diagnosis and fix-what-the-executor notes cover that more precisely.

**Body search** (scope `kb/notes kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags`, later `kb/notes kb/sources`):
- `rg -l -i -e "requirement"` -- broad. The hits are mostly ADR, review and definition noise. Kept: fix-what-the-executor (via the spec cluster) and specification-strategy-should-follow-where-understanding-lives (rejected below).
- `rg -l -i -e "over-engineer|overengineer"` -- only `kb/agent-memory-systems/README.md` (historical, frozen). No candidate.
- `rg -l -i -e "RLVR|reward hacking|sycophan"` -- the-boundary-of-automation-is-the-boundary-of-verification and the aide2 archive reviews. The RLVR mention is about verifiability, not grader-obsessed behaviour, so rejected.
- `rg -l -i -e "edge case"` -- agentic-systems-interpret-underspecified-instructions, constraining-and-extraction-both-trade-generality-for-reliability, plus many ams reviews. Kept the first as a candidate (projection of an underspecified spec).
- `rg -l -i -e "code review"` -- elicitation-requires-maintained-question-generation-systems, underspecification-and-indeterminism-complicate-programming-for, designing-agent-memory-systems. These cover generic review; none addresses invented requirements.
- `rg -l -i -e "defensive"` -- generality-bought-to-avoid-counterexamples-is-paid-for-in. The title suggested an analogy, but the body is about claim vocabulary in notes, so rejected.
- `rg -l -i -e "simplicity|elegan"` -- no design-elegance note. The hits are incidental.
- `rg -l -i -e "tacit|business context|domain context"` -- the-boundary-of-automation, brainstorming-maintainability-oracles (human judgment supplies "tacit codebase and domain knowledge").
- `rg -l -i -e "underspecif|under-specif"` -- the spec cluster: agentic-systems-interpret-underspecified-instructions, fix-what-the-executor-cant-determine, specification-strategy, underspecification-and-indeterminism, plus the llm-reliability and constraining tag heads.
- `rg -l -i -e "negative constraint|non-goal|what not to"` -- no relevant note. Nothing in the KB names "state the requirements you don't have" as a specification move.
- `rg -l -i -e "maintainab"` (notes+sources) -- weakly-discriminated-qualities, brainstorming-maintainability-oracles, maintenance-capacity-must-match-harmful-artifact-inflow, sources why-llms-cant-make-your-code-simpler, simplification-2090443748077416467, why-software-factories-fail, programming-as-theory-building.
- `rg -l -i -e "slop"` and `"scope creep|bloat|thousand-line|diff size"` -- maintenance-capacity, reverse-compression (via `reinforcement learning|reward` and `accretion|ossif|petrif` queries), SlopCodeBench ingest.
- `rg -l -i -e "goedecke"` -- sibling ingest `defense-of-not-understanding-your-codebase.ingest.md`.
- `rg -n -i "RLVR" kb/notes/the-boundary-of-automation-is-the-boundary-of-verification.md` -- no RLVR body hit (the file match came from another term), confirming rejection.

**Link following:**
- why-llms-cant-make-your-code-simpler.ingest → weakly-discriminated-qualities, brainstorming-maintainability-oracles, why-software-factories-fail, learning-inside-a-fixed-decomposition. This confirmed the cluster where agent-code complexity sources already land. That ingest separates *weak discrimination* from *information omission*, and Goedecke's essay supplies a case of each.
- weakly-discriminated-qualities → its Scope asks for an "adverse directional mechanism" for absolute decline and lists "production biased toward locally expedient changes" and "irreversible accumulation". Goedecke's RLVR-induced requirement invention plus "petrify" is a candidate mechanism of that kind.
- fix-what-the-executor-cant-determine → intent-framed-delegation-is-a-control-regime-not-a-short-prompt. Its description is general handoff doctrine, which is less specific than the parent, so not kept separately.
- llm-output-deviation-requires-three-way-diagnosis → agentic-systems-interpret-underspecified-instructions, out-of-spec-output…. This confirmed the I/V/D framing applies.

## Connections Found

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **is-evidence-for**: Goedecke names a candidate *adverse directional mechanism*, which the note says absolute degradation needs. RLVR-shaped generators systematically add coordination and re-checks, tests do not penalise them (the code is still correct), and he reports that the accumulated additions "petrify" the system. He also reports human review catching the unneeded requirement in about half of large AI changes, so review acts as the operative discriminating oracle for this quality. The evidence is anecdotal practitioner report, with no candidate cohort or enrichment measurement. It bounds and illustrates; it does not corroborate the statistical conjecture.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: the acceptable staleness or inconsistency level is a business acceptance condition the executor cannot determine from code. Goedecke's practice of stating "I don't mind the data sometimes being stale" in the prompt is an author fixing exactly that choice. It is also a practitioner instance where the omitted fix is a *non*-requirement (a tolerance), which the note's examples do not yet show.
- [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) -- **is-evidence-for**: invented requirements are mostly an underspecification case. A silent spec admits both the mutex and the no-mutex design (`V` wider than `I`), and the RLVR prior biases the projection toward over-satisfaction. Goedecke's two repairs map onto different relations: the prompt tolerance narrows `V`, while post-hoc review filters `D`. This illustrates why the remedies do not substitute for each other.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) -- **is-evidence-for**: the source supplies a concrete, cheap candidate signal the brainstorm lacks. It detects requirements present in the diff but absent from the task, such as added mutexes, layers of indirection or mid-flight re-checks. It also supplies a human-review base rate ("about half" of large AI changes), which is an uncalibrated anecdote but a usable starting hypothesis.
- [Ingest: Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) -- **compares-with**, axis *the source of LLM-added complexity*. Alvarez Vecino attributes it to missing situated design theory (information omission) and offers ADRs as the repair. Goedecke attributes it to missing business tolerances *plus* a training-induced disposition to satisfy a grader, and offers stated tolerances and human review as repairs. Both cases also show simplicity bought by dropping a product requirement: Indian-card auto-top-up there, consistency or freshness here.
- [Ingest: Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) -- **compares-with**, axis *who decides what is unnecessary in agent code*. Briggs keeps the architectural verdict with the experienced developer and treats agent hunches as candidates. Goedecke likewise keeps the "is this requirement real?" verdict in human review, but his target is agent-*added* scope rather than agent-led *removal*.
- External: `https://www.seangoedecke.com/what-requirements-dont-you-have/` -- **derived-from**: the ingest analysis is worked out from this essay (already in hand as the snapshot `source` URL).

## Bidirectional Candidates

- [Ingest: Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) <-> source -- **compares-with**: the return path helps readers of that ingest. Its "information omission vs weak discrimination" split gains a second case in which *both* are present, and in which the omitted information is a tolerance rather than a design theory. `compares-with` is authorised sources→sources in both directions.

## Reverse-edge Candidates

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) → future ingest -- **evidenced-by** (notes COLLECTION authorises notes→sources). The context phrase should say the source *qualifies* the claim by naming a directional production mechanism (RLVR-shaped requirement invention) and an accumulation claim. Under the notes collection's "origin is not corroboration" rule it should not say the source *corroborates* the claim, because the anecdote reports no refutation attempt.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → future ingest -- **evidenced-by**: an illustrative case where the author-only knowledge is a tolerated non-requirement. This complements the QEMU hidden-acceptance case already in the note.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) -- the "four-line change into a thousand-line monster" resembles expansion, but Goedecke's additions change behaviour (new requirements and coordination). Reverse compression concerns verbosity without new structure. Linking them would conflate two mechanisms.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- a tempting analogy (guarding against every edge case at a cost), but the note is about claim vocabulary in KB notes, not system design. It is too indirect to help traversal.
- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- relevant, but llm-output-deviation-requires-three-way-diagnosis already carries the underspecification framing and links here. A second edge would be redundant.
- [Maintenance capacity must match harmful-artifact inflow](../../../../notes/maintenance-capacity-must-match-harmful-artifact-inflow.md) -- "petrify over time" is an accumulation claim, but Goedecke says nothing about capacity versus inflow rates. The weakly-discriminated edge already covers the accumulation mechanism.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- the source's "code review is not dead" aside is adjacent, but it offers no verification-cost argument. Keyword match only.
- [Constraining and extraction can trade generality for reliability, speed, or cost](../../../../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) -- it shares the trade-off vocabulary, but it concerns narrowing interpretation in artifacts, not dropping system requirements. The analogy is loose.
- [Ingest: In defense of not understanding your codebase](../../../../sources/defense-of-not-understanding-your-codebase.ingest.md) -- same author, different subject (partial understanding of legacy code). There is no shared axis beyond authorship.
- [Ingest: Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) -- this case is about delayed maintainability oracles in lights-off runs. Goedecke's essay reaches it only through weakly-discriminated-qualities, which is already linked.
- `kb/notes/specification-strategy-should-follow-where-understanding-lives.md` -- about spec lifecycle phases. The source does not engage when understanding becomes available.

## Index Membership

- [llm-reliability tag head](../../../../tags/llm-reliability-README.md) -- if the ingest analyses the agent section (invented requirements as underspecification plus a biased interpreter prior, repaired by prompt tolerances and review), it meets the inclusion condition "diagnoses those deviations … or improves the machinery that … corrects them". The ingest author should confirm substantive treatment before tagging.

## Synthesis Opportunities

The KB has no claim that *stating non-requirements (tolerances, accepted staleness, acceptable failure) is a distinct specification move*. Existing specification notes (fix-what-the-executor-cant-determine, three-way-diagnosis) frame fixes as adding constraints, while Goedecke's repair *widens* the acceptable set explicitly to stop the interpreter from narrowing it on its own. Together with why-llms-cant-make-your-code-simpler (simplicity bought by dropping a product requirement), this suggests a candidate claim: "agents narrow underspecified specs toward over-satisfaction, so explicit tolerances are a constraint type, not an absence of constraint". It is evidence-thin (two practitioner anecdotes), so it belongs in `kb/log.md` until a mechanism or test exists. Do not create the note from this report.

## Maintenance Observations

- The target ingest `kb/sources/sean-goedecke-what-requirements-dont-you-have.ingest.md` did not exist when this report was written (an ingest was running concurrently). Connections are pre-staged for it.

## Flags

- The source makes three loosely coupled assertions (design elegance via dropped requirements; the business+technical expertise and trust problem; LLM requirement invention). Only the third lands in this KB's scope. The first two are general software design and out of scope per AGENTS.md, so the ingest should foreground the agent section.
- Evidence strength: every agent-related claim is practitioner anecdote ("about half the time", "invariably", "in every single system I've worked on"). Link phrases should say *illustrates/qualifies*, not *corroborates*.
