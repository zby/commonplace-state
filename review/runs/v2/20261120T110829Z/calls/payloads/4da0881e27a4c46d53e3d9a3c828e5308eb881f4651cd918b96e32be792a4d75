---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The H1 title asserts close to the definition of information hiding: a shared interface means callers need not change when the implementation is swapped. An informed reader would hardly argue the opposite of that literal statement. The contestable point the note actually establishes is that this prompt–code boundary leaks asymmetrically: prompt-to-code breaks loose LLM callers, and code-to-prompt breaks code callers' cost, latency and error assumptions. That point appears in the description and body but not in the title. Sharpening the title toward the asymmetric leak, or toward the condition under which caller-free swapping holds, would give it a claim someone could dispute."
    level: warn
outcome: warn
---

# Review

## Summary

The title is a proposition, but its literal content is close to a truism. "A unified interface lets programmers choose prompts or code without changing callers" mostly restates what any shared interface does. The only contestable element is the implicit assumption that prompts and code *can* sit behind one interface. The note does not defend that assumption much; it takes it as given.

The note's non-obvious contribution is the asymmetric leakage across the two swap directions, together with the practical rule that follows: enforce schemas before codification, and write call sites for fallible, higher-latency calls if they may move back to prompts. A title built on that point would pass the "could someone argue the opposite?" test more clearly. For example, someone could argue that a unified interface makes prompt–code swaps transparent, and the note disputes exactly that.
