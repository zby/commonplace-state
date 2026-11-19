---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: Re-re-reading Lucy Suchman's Plans and Situated Actions

**Source:** [Ingest: Re-re-reading Lucy Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md)

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section. Destinations scanned: theory (labels `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; `defined-in` for theory/definitions), sources (`compares-with`, `see-also`), agent-memory-systems, agentic-systems, reference (`see-also`), tags. Excluded: `kb/work/`, `kb/instructions/`. External prospecting skipped (no external target supplied; Suchman's book is uncaptured).

**Existing outbound links in the ingest (verified to exist):** agentic-systems-interpret-underspecified-instructions, theory-and-methodology-form-a-two-layer-execution-system, definitions/actionable-methodology, silent-disambiguation-is-the-semantic-analogue-of-tool-fallback, norman-problem-of-automation-inappropriate-feedback.ingest. These are not re-proposed; they are inline and unlabelled, which the contract allows.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (the source's tag; `complete: true`, so the by-tag rg was skipped). Flagged: fix-what-the-executor-cant-determine-not-what-it-will, theory-and-methodology-form-a-two-layer-execution-system (already linked), specification-strategy-should-follow-where-understanding-lives.

**Title listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "plan|instruct|situat|interpret|disambig|repair|executor|operationaliz|automation|checklist|underspec|tacit|circumstance|setting|context-free|ambigu"` -- flagged a-goal-holding-interpreter-fails-soft, fix-what-the-executor-cant-determine, traditional-software-can-bracket-executor-conformance, llm-executed-methodologies-are-metacircular-interpreters, out-of-spec-output-is-a-failure-of-the-interpreter, writing-styles-are-strategies-for-managing-underspecification.

**Description listing scan:**
- `rg '^description:' kb/sources/ --glob '*.ingest.md' | rg -i "checklist|automation|instruction|tutorial|plan|situat|tacit|procedure|human-machine|ironies|bainbridge|norman|ethnometh"` -- flagged programming-as-theory-building (Naur), surgical-safety-checklist-haynes-2009, cmmn-1-1-specification, model-types-levels-human-interaction-automation (Parasuraman), ironies-of-automation (Bainbridge), norman (already linked).

**Body search:**
- `rg -l -i "suchman|situated action|situated-action" kb --glob '*.md'` (non-work) -- only the source itself and definitions/actionable-methodology (hit is "situated actionability", not Suchman). No existing KB artifact cites Suchman.
- `rg -n -i "interpretive asymmetr|keyhole|opportunistic" kb --glob '*.md' -l` -- no theory hits; nothing else names the repair asymmetry.
- `rg -n -i "repair|ask|clarif|human" kb/theory/silent-disambiguation-...md` -- confirmed the note frames the agent as "repairing a contract gap", which supports the existing inline link.

**Link following:**
- Read summaries of Naur, Haynes, CMMN, Parasuraman, Bainbridge ingests; read opening of fix-what-the-executor note and description of a-goal-holding-interpreter. Naur's ingest states "prescribed methods ... cannot mechanically determine the right actions or their order" -- the closest in-KB statement of Suchman's position. Haynes reports partial adherence and site adaptation "to fit into the flow of care".

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with**: axis = how determination divides between plan and execution. The note allocates choices between author and executor by who can determine them; Suchman, as relayed, holds that circumstances always leave execution-time determination, so the plan never fully fixes action. Gives the workshop a theory-side anchor for the "operationalized artifact constrains without determining" reading in Extractable Value 2.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- **compares-with**: axis = whether the executor repairs breakdowns. The note's procedure-versus-interpreter split maps onto the Wilf/Adam interpretive asymmetry (classic machine does not repair; human and LLM interpreter do), and adds the cost of repair that the asymmetry point omits. Supports Extractable Value 3.
- [Programming as theory building (Naur)](../../../../sources/programming-as-theory-building.ingest.md) -- **compares-with**: axis = whether explicit methods and artifacts can determine skilled action. Both are 1980s accounts that place the decisive knowledge in situated capacity rather than in written plans or methods; Naur's ingest is primary-source, Dittrich's is a secondary pointer, so a reader can see which claim is better grounded.
- [Haynes 2009 surgical safety checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) -- **compares-with**: axis = plan as resource versus plan as executed program. The checklist worked while steps were still frequently omitted and sites adapted it to the flow of care, an empirical case consistent with Suchman's plans-as-resources reading; both ingests serve the same operationalization workshop.
- [CMMN 1.1 specification](../../../../sources/cmmn-1-1-specification.ingest.md) -- **compares-with**: axis = where run-time discretion lives. CMMN formalizes work that "cannot be orchestrated by a predefined sequence" by giving case workers run-time planning over discretionary items, a standards-body accommodation of the situated-action critique. Weaker than the two above; keep only if the workshop needs an engineering counterpart.

## Bidirectional Candidates

- [Programming as theory building (Naur)](../../../../sources/programming-as-theory-building.ingest.md) <-> source -- **compares-with**: Naur's ingest discusses limits of prescribed methods without a pointer to the situated-action tradition; the return link gives its reader the HCI counterpart (sources -> sources `compares-with` is authorised).
- [Haynes 2009 surgical safety checklist](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md) <-> source -- **compares-with**: the checklist ingest's partial-adherence finding gains an interpretive frame from Suchman's plans-as-resources position.

## Reverse-edge Candidates

- [Methodology with incomplete coverage and its live theory fallback form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) → source -- **evidenced-by** (theory contract; qualifies/bounds, not corroboration): Dittrich's report of opportunistic method use and methods kept to display rationality bounds the note's assumption that departures happen only outside coverage. Thin evidence (blog, unsummarized literature); the context phrase must say it qualifies rather than corroborates.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by** (qualifies): the classic HCI interpretive asymmetry is the historical baseline that LLM repair inverts. Should wait until Suchman, Wilf or Adam is captured directly; the current source is thirdhand on this point.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Model types and levels of human interaction with automation (Parasuraman et al.)](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- relevant to the workshop's decision-autonomy question, but the four-stage matrix has no repair dimension; linking would assert a comparison the source cannot support. Revisit if Extractable Value 3 becomes a note.
- [Ironies of automation (Bainbridge)](../../../../sources/ironies-of-automation.ingest.md) -- concerns operator monitoring and deskilling, not plans or interpretation; period match only.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- touches the non-interpreting classic machine, but the goal-holding-interpreter note carries the repair axis more directly; adding both would duplicate.
- [LLM-executed methodologies are metacircular interpreters](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- re-interpretation of rules per session is adjacent, but the note's claim is about codification paths, not situated action.
- [Writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- keyword overlap on underspecification; the existing link to agentic-systems-interpret-underspecified-instructions already carries the contrast.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- about conformance violation, not circumstance-dependence.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- plausible (understanding discovered during execution), but fix-what-the-executor is the sharper comparison; keep one.

## Index Membership

None. Sources are outside the participating collections for tag heads; `method-guided-action` tag on the ingest is already set and appropriate.

## Synthesis Opportunities

Naur (methods cannot mechanically determine action), Suchman via Dittrich (action depends on circumstances), Haynes (checklist effective under partial adherence) and fix-what-the-executor-cant-determine together suggest a claim for the operationalization workshop: an operationalized artifact is effective as a resource that constrains and cues execution, and its success does not require or show that it determined the executed path. Needs the primary Suchman text before promotion; the workshop, not connect, should carry it.

## Maintenance Observations

- No KB artifact other than this ingest names Suchman or the interpretive asymmetry, so the ingest is the only entry point; the primary book remains uncaptured (already noted in the ingest's Recommended Next Action).

## Flags

- The repair-asymmetry claims (Extractable Value 3, both Reverse-edge Candidates) rest on thirdhand reporting; any authored theory edge should be phrased as qualifying, not corroborating.
