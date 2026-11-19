---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/church-turing-thesis-sep.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: The Church-Turing Thesis (Stanford Encyclopedia of Philosophy)

**Source:** [Ingest: The Church-Turing Thesis (SEP)](../../../../sources/church-turing-thesis-sep.ingest.md)

The ingest already authors eight connections (actionable methodology, methodological/computational closure, Naur note, Programming as Theory Building ingest, underspecified-instructions note, executor-conformance note, competence-theory ingest, codification). All eight paths exist, and their labels (`compares-with`, `is-evidence-for`) are authorised for sources -> theory/sources. This report lists only additional candidates, reverse edges and flags.

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` / `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (sparingly), `derived-from` (external). External prospecting skipped (no external target supplied beyond the ingest's own `source` URL).

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (source tag; head is `complete: true`, so by-tag rg skipped). Flagged: methodological/computational closure (already linked), fix-what-the-executor-cant-determine, theory-and-methodology two-layer system, specification-strategy note.
- `kb/sources/README.md` — no curated lists; no index membership.
- Workshop `kb/work/operationalization-executability-automation/exploration.md` read only for occasion context (excluded destination). Its source table pointed to sibling ingests: `model-types-levels-human-interaction-automation`, `ironies-of-automation`, `competence-theory...`.

**Title / description listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "execut|operational|codif|automat|judgment|underspecif|determinis|mechanical|resum|external state|definition|stipulat|interpret|semantic|formal|precise|prose|spec"` — ~100 titles; shortlisted: underspecification-and-indeterminism, code-complements-weight-prompt, semantic-work-relocated, fix-what-the-executor-cant-determine, the-boundary-of-automation-is-verification, definitions/tentative-theory, definitions/representational-form, llm-executed-methodologies-metacircular, codify-versus-llm-heuristics, active-work-state, agent-statelessness, execution-indeterminism, model-resolved-indirection.
- Description pass over the shortlist with `rg -m1 '^description:'`.

**Body search:**
- `rg -n -i "church.turing|turing machine|effective method|effective procedure|mechanical procedure|human computer|clerical|without insight|no insight" kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags kb/sources` — only hits: Sutskever-list NTM chapters and `cost-sensitive-formalisms-for-tentative-theory-search.md` (bounded NTM as formalism). Neither is about effective methods; rejected.
- `rg -l "church-turing" --glob '*.md' kb/` — only the ingest itself and the workshop exploration; no existing inbound links.
- `rg -n -i "turing|church|effective" ` over the MAKER and Parasuraman ingests — no direct mention; kept on conceptual grounds below.
- `rg -n -i "prose|notation|consumer|unique|operational semantics"` over `definitions/codification.md` and `definitions/representational-form.md` — found representational-form's "interpretive, not editorial" boundary and its "fixed prompt and model ... repeatability is not a unique operational semantics" failure mode; bears directly on the ingest's open codification tension and on Extractable Value 1.
- `rg -l -i "resumab|resume from|externaliz" kb/theory` — no note on resumability-from-external-artifacts that fits Turing's "note of instructions"; EV5 stays unlinked.

**Link following:**
- `operationalism-sep.ingest.md` Connections Found — Bunge's "indicator hypotheses" and construct-validity points parallel Post's "continual verification" objection (ingest EV4).
- `semantic-work-can-be-relocated-but-not-eliminated.md` -> codification as limiting case; "looks free or deterministic at the point of use ... was paid earlier" matches condition 4.
- `code-complements-weight-prompt-with-symbolic-operations.md` -> representational-form: "same bytes, different consumer" mirrors EV1's level-relativity.
- `the-boundary-of-automation-is-the-boundary-of-verification.md` -> MAKER ingest; MAKER explicitly separates "execution" from "insights".
- `theory/COLLECTION.md` linking table read for reverse-edge labels (`evidenced-by` to sources; "origin is not corroboration").

## Connections Found

- [Representational form](../../../../theory/definitions/representational-form.md) -- **defined-in**: the ingest's codification tension asks whether the criterion is notation or a non-reinterpreting consumer; this definition is where the KB states the criterion ("unique operational semantics", "interpretive, not editorial", repeatability is not symbolic form). A reader judging the tension needs it.
- [Code complements the weight–prompt pair with independently executed symbolic operations](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md) -- **compares-with** (axis: whether execution is fixed by the artifact or by its consumer): the note's "same code can be read or executed" is the KB counterpart of EV1, where an LLM run is mechanical at the weights level but not at the task-instruction level.
- [Semantic work can be relocated but not eliminated](../../../../theory/semantic-work-can-be-relocated-but-not-eliminated.md) -- **compares-with** (axis: where insight is paid): an effective method is the classical case of all meaning-dependent judgment paid upstream by the method author, so condition 4 holds at use time; the note supplies the general rule this case instances.
- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -- **compares-with** (axis: which executor defect a definition excludes): condition 4 (no insight) excludes underspecification and condition 2 ("if carried out without error") brackets faulty execution — the two phenomena the note separates. The definition removes both by stipulation.
- [Tentative theory](../../../../theory/definitions/tentative-theory.md) -- **defined-in**: EV4 says a workshop definition replacing an informal predicate should be "held as a tentative identification"; "tentative" is a registered term, and Post's "continual verification" is its Popperian sense.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with** (axis: allocation of choices between author and executor): an effective method is the limit where the executor is allowed to determine nothing, so the author must fix every choice. That limit shows what the note's bidirectional rule gives up when execution-time evidence is excluded.
- [Operationalism (SEP) ingest](../../../../sources/operationalism-sep.ingest.md) -- **compares-with** (axis: whether an operational/effective identification is a definition or a hypothesis): Post's objection to masking the thesis as a definition parallels Bunge's "indicator hypotheses" and the construct-validity critique. Both sibling ingests serve the same workshop question.
- [MAKER ingest](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) -- **compares-with** (axis: LLM executors as human computers): MAKER runs a given algorithm through single-step LLM microagents and secures condition 2 ("without error") by voting. It separates "execution" from "insights" in the same place condition 4 does. It is the KB's nearest empirical case of an effective method run by an LLM.
- [Parasuraman, Sheridan & Wickens ingest](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with** (axis: function allocation versus decision autonomy): EV2's human-computers-to-ACE case is function-level automation with zero decisions left to either executor. That is the degenerate cell of the stage × level matrix, useful as a baseline.

## Bidirectional Candidates

- [Operationalism (SEP) ingest](../../../../sources/operationalism-sep.ingest.md) <-> source -- **compares-with**: the return path lets a reader of the operationalism ingest reach the effective-method case, where an informal predicate was replaced by a formal one and held between "theorem and definition".

## Reverse-edge Candidates

- [Naur's human-only conclusion needs more than the absence of explicit criteria](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) → source -- **evidenced-by** (bounds): premise 2 ("a computer can make a judgment only by executing such criteria") matches the classical 1936 notion. Copeland's thesis/Thesis M separation shows the thesis does not license that premise for all machines. Context phrase must say it bounds, not corroborates (theory "origin is not corroboration" rule).
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) → source -- **evidenced-by** (qualifies): EV1 shows "computationally closed" must name which artifact counts as the method, or LLM runs (mechanical at the weights level) look closed at every level. The note's "exact checklist, human applies" row is the human-computer case.
- [Semantic work can be relocated but not eliminated](../../../../theory/semantic-work-can-be-relocated-but-not-eliminated.md) → source -- **evidenced-by** (qualifies): the effective-method tradition is a historical instance of the "free at use-time means paid earlier" rule. It is weak as corroboration because the note was not tested against it.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- mentions bounded nondeterministic Turing machines as a search formalism. That is a keyword match, not effective-method content.
- [LLM-executed methodologies are metacircular interpreters](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- the interpreter/compiler framing sits near the converse of the thesis, but the representational-form and code-complements candidates carry the same axis more precisely.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- EV2 ("operationalization entails automatability for no-insight methods") is in some tension with verification cost as the determinant. The MAKER ingest carries the concrete link, so a direct edge would duplicate it. See Flags.
- [Active work state is not retrospective memory or chat history](../../../../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md) / [agent statelessness](../../../../theory/agent-statelessness-means-the-context-engine-should-inject-context.md) -- Turing's "note of instructions" (EV5) is only an analogy to externalized work state; the ingest itself marks it just-a-reference.
- [Ironies of Automation ingest](../../../../sources/ironies-of-automation.ingest.md) / [Norman ingest](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- workshop siblings about human-machine monitoring and feedback. They share no axis with effective-method definitions.
- Sutskever-list Neural Turing Machine chapters -- keyword only.

## Index Membership

None — `kb/sources/` has no curated index, and sources do not participate in tag heads (the `method-guided-action` tag is search-only).

## Synthesis Opportunities

The ingest's EV1, together with [code complements the weight–prompt pair](../../../../theory/code-complements-weight-prompt-with-symbolic-operations.md), [representational form](../../../../theory/definitions/representational-form.md) and [methodological and computational closure](../../../../theory/methodological-and-computational-closure-track-different-changes.md), implies a candidate claim: whether an execution is "mechanical" depends on which artifact counts as the method. Closure and form claims should therefore name that level. This is the workshop's natural theory output; do not write it during connect.

## Maintenance Observations

- The workshop source table (`kb/work/operationalization-executability-automation/exploration.md`, row "Church–Turing history") still says "No matching ingest". The ingest's own Recommended Next Action already notes this.

## Flags

- **Codification tension is partly addressed already.** Representational form places the symbolic boundary at consumer-assigned "unique operational semantics", not at notation, and explicitly denies symbolic status to a fixed prompt plus model. The open question narrows to this: does a human computer bound by conditions 1–4 count as a consumer with a unique operational semantics? A future edit of the ingest should cite the definition rather than leave the tension phrased as notation-versus-consumer.
- **Possible tension with the verification-boundary synthesis:** EV2 makes operationalization (to no-insight level) sufficient for automatability. The automation-boundary note makes verification cost the primary determinant. The two may agree if per-step conformance of an effective method counts as a hard oracle, as MAKER suggests. This is left unresolved.
