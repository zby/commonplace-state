---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The note says what harness code takes over three times. The offload bullets say it first. The bridge sentence ('the frozen model does not need to keep track of budgets, traces, or regression suites in its head') recaps it. The criterion-revision paragraph ('Detecting bloat, stale entries, or rising regressions belongs to harness code') restates the store-bookkeeping bullet. Each restatement delays or dilutes the turn to the three residual competences, which are the part of the claim the title names. A revision could state the harness side once in the bullets. It could move the one new point, that a code-writing LLM can build further harness tools, into the list's lead-in. The pivot ('semantic work can be relocated without being eliminated') would then follow the list directly, and the criterion-revision paragraph would keep only its semantic reduction to competences 2 and 3."
  - scope: passage
    quotes: ["our working hypothesis is that three irreducible semantic competences remain on the frozen base LLM"]
    reason: "The note marks the split's status in three places: the bold opening label, this sentence, and the first Scope bullet with its 'not an established impossibility result' clause. This sentence also calls the competences 'irreducible', while the Scope bullet says any sub-task shown to be offloadable 'moves out of the LLM column'. A reader gets repeated hedging and a mixed signal about how revisable the list is. A revision could state the status once, next to the claim, and keep the Scope bullet as a revision rule only. That requires deciding what 'irreducible' means here."
outcome: report
---

# Simplification synthesis: Harness code may offload much of a selection loop, leaving three base LLM competences

The note is short, and its core claim is easy to find (the core-claim-obscured and branch-bloat checks both passed). The two opportunities below are consolidations visible only across the whole note. Neither changes the argument. The bootstrap sentence flagged by branch-bloat stays out of the list below. It is a single compact sentence, and cutting or keeping it is a local choice. If the author wants the note to claim a diagnostic bootstrap method, that would need its own grounding.

## Opportunities

### 1. State the harness side once, then pivot

- Location: opening section, from the three offload bullets through "Because an LLM that writes code can also build new harness tools…", plus the criterion-revision paragraph ("Detecting bloat, stale entries, or rising regressions belongs to harness code")
- Combines: core-claim-obscured (bridge aside delays the pivot); marginal-value-redundancy finding 2 (consequence clause restates the bullets); detail-overhang (store-bookkeeping items recur later and the bridge recaps the list)
- Preserve or decide: keep the tool-building point if the author means it as a reason the harness share can grow over time. It is the only new content in the bridge sentence. Keep enough concrete items in each bullet to support the "much of the loop" quantifier. Detail-overhang notes that this length may be deliberate. In the criterion-revision paragraph, keep the claim that semantic store work reduces to competences 2 and 3. That claim protects the count of three. One possible resolution, offered only as an illustration: "Harness code, including tools the LLM itself writes, can take over much of the loop's machinery:" as the list lead-in, followed directly by the relocation pivot.

### 2. Settle the hypothesis status and the meaning of "irreducible" in one place

- Location: bold "**Working hypothesis.**" opening; "our working hypothesis is that three irreducible semantic competences remain"; first Scope bullet
- Combines: marginal-value-redundancy finding 1 (third repetition of the label plus a defensive contrast clause); cross-cutting tension with "irreducible"
- Preserve or decide: the author must decide whether "irreducible" claims that these competences cannot be offloaded in principle or only that they currently resist offloading. The Scope bullet's revision rule supports the second reading. That choice sets how strong the core claim is, so it must not be made as a compression edit. Preserve the revision rule: offloadable sub-tasks leave the LLM column, and newly found bottlenecks can join it. Also preserve the necessary-not-sufficient boundary in the second Scope bullet. Keep the hedge beside the claim it qualifies rather than only in Scope.
