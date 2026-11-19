# Friction check: Traditional debugging intuitions break when tool loops can recover semantically

**Note:** kb/notes/traditional-debugging-intuitions-break-when-tool-loops-can-recover.md
**Central claim (one sentence):** Because an LLM can improvise a semantically valid workaround after an intended tool path fails, a successful result in a framework-owned tool loop is weak evidence that the intended infrastructure is healthy and can therefore mislead programmers who rely on traditional success-based debugging intuitions.

## Filter
**Verdict:** SURVIVES

The claim asks semantic recovery and infrastructure-health inference to coexist, and they can: the same run can complete through an improvised path while leaving its intended path broken. Preserving semantic recovery while separately observing degraded execution is also a consistent design commitment rather than an ignored trade-off.

## Signal — thinnest joints
1. **“The misread is predictable: the task succeeded → the programmer infers the helper or script is working”** — UNSUPPORTED — The execution mechanism establishes that a workaround can hide a fault, but it does not establish how programmers actually interpret successful artifacts, how often they inspect traces, or when the proposed misread is predictable rather than merely possible.
2. **“The downstream effect is that broken helpers persist longer because they are not attached to user-visible failures, and infrastructure drift accumulates behind apparently healthy runs.”** — THIN — Lack of a user-visible failure can delay detection, but persistence and accumulated drift also depend on whether traces, tests, alerts, or repeated recovery costs expose the helper; those conditions and the comparison baseline are not stated.
3. **“In a framework-owned tool loop, the recovery path is not pre-specified.”** — THIN — Framework ownership does not by itself exclude coded retries or fixed fallbacks. The subsequent examples support the narrower claim that an LLM can synthesize an additional recovery path when tool errors and alternatives are available.
4. **“So ‘the task succeeded’ is an imperfect but usable proxy for ‘the intended machinery mostly worked.’”** — THIN — Explicit, pre-engineered recovery makes the execution path inspectable, but it does not alone show that end-to-end success is a usable health proxy; ordinary systems can also mask partial failures, and “usable” lacks a stated comparison or threshold.
5. **“That flexibility is useful for task completion — and it is exactly what breaks the inherited debugging heuristic. Success now means ‘some viable path existed ...,’ not ‘the intended mechanism was healthy.’”** — HOLDS — Once a model may complete the task through an unplanned alternative, final success entails existence of a viable path but no longer entails health of the intended one; this supports weakening that heuristic without claiming every successful run used a workaround.

## For the human
Look first at the jump from a possible hidden recovery path to a predictable programmer misread, which needs a concrete observation model or evidence about what maintainers actually inspect.
