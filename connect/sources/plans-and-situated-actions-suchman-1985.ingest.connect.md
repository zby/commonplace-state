---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/plans-and-situated-actions-suchman-1985.ingest.md"
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: Ingest: Plans and Situated Actions (Suchman 1985 PARC thesis, ISL-6)

**Source:** [Ingest: Plans and Situated Actions (Suchman 1985)](../../../../sources/plans-and-situated-actions-suchman-1985.ingest.md)

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` "Outbound links" section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources, external (known targets only). Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external; sparingly). No inverse-direction hint, but sources are cited from theory, so reverse edges were prospected for theory and for sibling ingests.

**Existing outbound surface (not re-proposed):** the ingest already links inline to agentic-systems-interpret-underspecified-instructions, theory-and-methodology-form-a-two-layer-execution-system, fix-what-the-executor-cant-determine, silent-disambiguation, natural-language-meaning-is-coordination, intent-framed-delegation, MCDP 1, human-analogies-suggest-functions, naur-equates-machine-execution, the Naur ingest, actionable-methodology, Schegloff/Jefferson/Sacks, Purver/Ginzburg/Healey, Norman, and the three Suchman secondary ingests. The footer carries six of these plus the external `derived-from`.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (source's tag; `complete: true`, so by-tag rg skipped). Members re-checked against the source: two-layer execution, fix-what-the-executor, intent-framed delegation (all already linked); specification-strategy-should-follow-where-understanding-lives (new candidate); borrowed-patterns-transfer-only-over-shared-mechanism (rejected, see below).

**Title / description listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory --glob '*.md' | rg -i "instruction|plan|situat|context|execut|interpret|ambig|delegat|operator|breakdown|repair|clarif|tacit|access|description"` -- flagged changing-requirements-conflate-genuine-change-with-disambiguation, legal-drafting-solves-the-same-problem, out-of-spec-output, soft-bound-traditions, llm-executed-methodologies-are-metacircular-interpreters.
- `rg -m1 '^description:'` over flagged theory and source files to triage.

**Body search (kb/theory, kb/reference, kb/agentic-systems, kb/agent-memory-systems, kb/sources):**
- `rg -l -i "uchman" kb` -- only the source, the three Suchman secondaries, Purver and Schegloff ingests. No theory note cites Suchman yet.
- `rg -l -i "situated"` -- specification-strategy, actionable-methodology (line 31, "situated actionability"; already linked), information-value-is-observer-relative (TODO mentions situated cognition; rejected), ai-agent-book review ("situated loop"; rejected), CMMN ingest, knowledge-engineering ingest (incidental use), MCDP 1 (already linked).
- `rg -l -i "indexical"` -- only Suchman cluster plus logic sources (Tarski, liar paradox); off-topic.
- `rg -l -i "breakdown"` -- two-layer (already linked), specification-strategy ("the environment keeps surprising the initial plan"; kept).
- `rg -l -i "garden path|garden-path"`, `"plans? as resources?"`, `"shared access|description of the situation"`, `"map.{0,20}terrain"` -- only Suchman cluster; no theory precedent for the "situation description" framing (confirms Extractable Value 1 is unclaimed).
- `rg -l -i "out-of-spec"` -- out-of-spec-output, llm-output-deviation, traditional-software-can-bracket-executor-conformance; evaluated, rejected.
- `rg -l -i "tacit|Polanyi|Dreyfus|Heidegger"` and `"ethnomethodolog|Garfinkel|accountab"` -- Argyris ingest (theories-in-use; kept), US Army ADRP 6-0 (rejected as redundant with MCDP 1), CMMN (kept).
- `rg -l -i "Winograd|Flores|\bAgre\b|Chapman|Lave\b|Hutchins|Sch[oö]n\b|reflection-in-action|Clancey|plan recognition|common ground"` -- Norman (already linked), soft-bound-traditions (Argyris & Schön row), Argyris ingest; no other situated-action tradition texts in the KB.
- `rg -n -i "situated|plan recognition|user's situation" kb/agentic-systems kb/agent-memory-systems` and `rg -l -i "situat|clarif" kb/reference` -- no candidate with a shared axis.

**Link following:**
- specification-strategy -> bidirectional-spec and deploy-time-learning: confirmed the "plan surprised by execution" zone matches plans-as-resources.
- changing-requirements -> agentic-systems-interpret-underspecified-instructions: its "projection nobody noticed until consequences surfaced" is the garden-path structure.
- CMMN ingest -> fix-what-the-executor and progressive-constraining: CMMN is the institutional design response (run-time planning by humans) to the plan-as-controller assumption Suchman attacks.
- Dittrich, PD of HCI, Duguid ingests: each names the primary text as missing; none links to this ingest yet (`rg -l "plans-and-situated-actions-suchman-1985" kb` returns no other file).

## Connections Found

- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- **compares-with**: on where a plan's missing detail is supplied. The note's bidirectional-spec zone ("the environment keeps surprising the initial plan") stores discovery back into a live artifact; Suchman's plans-as-resources says the detail is supplied at the time of action and the plan stays vague by design. Comparing the two shows what retaining discoveries adds over situated use alone.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- **compares-with**: on late-surfacing faults. The note's unnoticed downstream projection has the same structure as Suchman's garden path (a faulted action satisfies the design under another interpretation and surfaces only later). Suchman also suggests a third category beside world change and disambiguation failure: significance that depends on circumstances the spec could not carry.
- [CMMN 1.1 specification](../../../../sources/cmmn-1-1-specification.ingest.md) -- **compares-with**: on whether a plan controls or resources the executor. CMMN institutionalizes run-time planning by case workers over a declared discretion catalogue, which is a design that treats plans as resources. Suchman's copier assumed the plan-as-controller view. Both cases are pre-LLM with human executors.
- [Argyris, Organizational learning and MIS](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) -- **compares-with**: on the gap between stated guidance and what actually produces action. Argyris's espoused theories versus theories-in-use treat the gap as a learning defect that can be surfaced and corrected. Suchman treats plan and action as constitutively different. Argyris's local versus distant information systems also parallel Suchman's situation access versus situation description.
- [Constraining](../../../../theory/definitions/constraining.md) -- **defined-in**: the ingest's first theory comparison and its Extractable Value 5 contrast indexicality with gaps that "constraining can narrow". A reader needs the KB's technical sense to see what Suchman's claim bounds.

## Bidirectional Candidates

- [Duguid, On rereading Suchman](../../../../sources/duguid-on-rereading-suchman-situated-action.ingest.md) <-> source -- **compares-with**: Duguid's limitations defer Suchman's own claims to the primary text. A return link lets its readers check plans-as-interpreted-resources against the 1985 wording.
- [Dittrich, Re-re-reading Suchman](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) <-> source -- **compares-with**: Dittrich's ingest says "the primary book remains uncaptured". The return link should name the edition caveat, because Dittrich cites the book, not the 1985 thesis.
- [PD of HCI Suchman summary](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) <-> source -- **compares-with**: the return path is useful mainly to flag that the summary's three design problems are absent from the 1985 thesis.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) → source -- **evidenced-by** (theory label; qualifies or bounds): the source's Recommended Next Action. Suchman's §4.6 indexicality claim bounds how far constraining can close the instruction-action gap. The context phrase must mark the copier-to-LLM transfer as analogy, and the note's unquoted-source limit (five) applies unless a quote is retained via `cp-skill-ground`.
- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) → source -- **evidenced-by** (bounds): breakdown-triggered explication of rules (§4.2) is a human-operator counter-case to method-first default execution.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by** (qualifies): the garden path is a pre-LLM named case of a breakdown invisible to the executing system.
- [Purver, Ginzburg and Healey](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) → source -- **compares-with**: it currently compares with the Dittrich and PD of HCI secondaries on the repair asymmetry; the primary text is the better anchor for "a machine that can neither issue nor recognize clarification".
- [Schegloff, Jefferson and Sacks](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) → source -- **compares-with**: currently compares with the Dittrich secondary on interactional repair; Suchman's Chapter 5 builds directly on this repair tradition.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Legal drafting solves the same problem as context engineering](../../../../theory/legal-drafting-solves-the-same-problem-as-context-engineering.md) -- shares "writing ahead for unforeseen circumstances", but the indexicality comparison is already carried by the underspecified-instructions link. A second link would add no new axis.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- Suchman's breakdowns are failures of mutual intelligibility, not interpreter output outside a spec's public meaning; linking would blur the two.
- [Soft-bound traditions as sources for context engineering strategies](../../../../theory/soft-bound-traditions-as-sources-for-context-engineering-strategies.md) -- its traditions share a bounded-processor structure; situated action is not about a context bound, so it fits neither the table nor a compares-with axis.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- mentions situated cognition only in a TODO; observer-relativity of extractable structure is a different claim from the situational significance of instructions.
- [US Army ADRP 6-0, Mission command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md) -- would compare on the Trukese navigator's "objective rather than a plan", but MCDP 1 already carries that axis in the ingest; adding it would be redundant.
- [Parasuraman, Sheridan, Wickens](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- automation-level allocation, not plan-action relations; keyword overlap only.
- [AI Agents in Depth review](../../../../agentic-systems/reviews/ai-agent-book.md) -- "situated loop" is harness-boundary vocabulary, not situated-action theory.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- relevant to the copier-to-LLM transfer caveat, but the ingest already states that caveat and the Naur note carries the comparable inference gap. No new axis for the reader.

## Index Membership

None. The source already carries `tags: [method-guided-action]`, and sources are outside the tag's participating collections, so no tag-head entry is expected.

## Synthesis Opportunities

The ingest's Extractable Value 1 ("context is a substituted situation description") is unclaimed in theory. Searches for "shared access" and "description of the situation" found no theory note. It would join this source, [Argyris](../../../../sources/argyris-organizational-learning-and-mis-1977.ingest.md) (local versus distant information systems), [fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) and [silent disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md). As the ingest says, the mechanism must be worked out before it meets the quality bar. Do not create it during connect.

## Maintenance Observations

- No theory note cites any Suchman source. The cluster is four source ingests that cite each other and theory, with no inbound theory edges. If any theory note adopts the counterpoint, it should cite this primary ingest rather than the secondaries.
- The ingest's inline Connections Found section names about fifteen targets, but its footer lists six. That is acceptable under the contract (inline is the stronger commitment), so this is not a defect.

## Flags

- Edition tension: Dittrich and PD of HCI cite the 1987 book, while this ingest is the 1985 thesis. Return links from those ingests must keep the edition boundary explicit, especially for the three design problems absent from the thesis.
- No split candidate: the ingest makes one connected argument.
