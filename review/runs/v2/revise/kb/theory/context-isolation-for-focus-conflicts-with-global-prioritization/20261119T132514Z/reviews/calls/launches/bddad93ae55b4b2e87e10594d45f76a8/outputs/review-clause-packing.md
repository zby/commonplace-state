---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A system operating under those conditions whose isolated task workers reliably make decisions whose right answer depends on unseen competing work—or that loads full live portfolio state alongside deep task context without degrading execution competence—would refute the claim."
    reason: "The refutation sentence holds its subject open across two nested whose-clauses and a dash-delimited alternative of about 25 words before reaching the verb 'would refute'. Two long dependencies are open at once. Fronting the verdict helps: 'The claim would be refuted by a system operating under those conditions whose isolated task workers reliably make decisions whose right answer depends on unseen competing work, or by one that loads full live portfolio state alongside deep task context without degrading execution competence.'"
    level: warn
  - scope: passage
    quotes:
      - "**Global prioritization**—deciding how much effort a local branch deserves relative to other work, when to stop or defer it, and whether a blocker warrants interrupting scarce operator attention—moves in the opposite direction."
    reason: "A three-item definition of about 30 words separates the subject 'Global prioritization' from its verb 'moves'. Reorder so the short predicate comes first: 'Global prioritization moves in the opposite direction: it decides how much effort a local branch deserves relative to other work, when to stop or defer it, and whether a blocker warrants interrupting scarce operator attention.'"
    level: warn
  - scope: passage
    quotes:
      - "it supplies the local judgments its deep context uniquely supports—**scale-bearing local facts** such as what will break, how soon, whether waiting is reversible, whether the main path is blocked, and what decision would change—recorded on a discoverable surface or in a typed stop record."
    reason: "About 60 words with an opening when-clause. A five-item appositive list separates 'the local judgments' from the participle 'recorded on a discoverable surface or in a typed stop record' that modifies them, so the reader must carry the head noun across the list. Move the recording phrase next to its head ('it records, on a discoverable surface or in a typed stop record, the local judgments its deep context uniquely supports: scale-bearing local facts such as ...') or put the recording destination in its own sentence."
    level: warn
  - scope: passage
    quotes:
      - "an isolated worker that emits an uninformative blocker (\"blocked on operator input\") or drops the local detail that makes an issue severe forces triage either to fall back to deep context or to misclassify severity under unsafe substitution."
    reason: "The sentence opens with a Because-clause and then delays the main verb 'forces' behind a subject carrying two coordinated relative clauses, a parenthetical example and a further nested 'that makes an issue severe'. About 50 words with two long dependencies open at once. Splitting the grounding clause off ('An insufficient summary precedes the source rather than replacing it.') and shortening the subject would let the main relation register."
    level: warn
  - scope: passage
    quotes:
      - "Solving a hard problem in a bounded LLM context pushes an agent system toward **context isolation**: load deep task-relevant material and exclude unrelated work so the task stays within the model's usable attention budget, because [context efficiency binds first on per-window feasibility]"
    reason: "About 45 words combining the push toward isolation, its definition, its purpose and its grounding reason. Each piece is short and ordered, so the load is tolerable, but the trailing because-clause could become its own sentence."
    level: info
  - scope: passage
    quotes:
      - "Those choices remain bounded by whatever compressed proxy of global priority—intent, tolerances, concern depth, or budget—fits cheaply inside the local window without eroding focus."
    reason: "A dash list interrupts 'whatever compressed proxy of global priority' and its verb 'fits'. The interruption is short and the sentence is under the threshold, so this is minor; moving the examples to the end ('...without eroding focus, such as intent, tolerances, concern depth, or budget') would remove it."
    level: info
outcome: warn
---

# Review

Most sentences in the note stay within two or three ideas and keep subjects close to their verbs. Four sentences overload the reader, mostly through distance rather than raw clause count: a long dash-delimited definition or list sits between a subject and its verb, or between a head noun and the phrase that modifies it. Three of these come from definitional or enumerating material inserted mid-sentence (the definition of global prioritization, the list of scale-bearing facts, the refutation alternatives), and the fourth stacks a grounding because-clause on a heavily modified subject. Each has a reordering or a single split that keeps its content.

The opening sentence and the micro-prioritization sentence are noted as minor; neither needs a change to be read correctly.
