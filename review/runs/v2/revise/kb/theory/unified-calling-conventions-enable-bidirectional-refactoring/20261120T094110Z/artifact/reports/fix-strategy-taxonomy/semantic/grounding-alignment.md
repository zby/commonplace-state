
# Report

Two changes, both by `fix-strategy-taxonomy.md#hedge-strength-mismatch`: the source's weaker claim is stated, and the note's stronger claim is marked as its own extension ("The source describes X; we extend this to Y").

- Passage: "The [underspecified instructions framing](…) says components should move between … relax rigid code back to LLM. But the framing doesn't say how …" — the attribution now matches the target's English account and code-extraction remark; the bidirectional premise is kept unnarrowed as the note's own; "the framing" became "that premise".
- Passage: "[Instructions are typed callables](…) argues that prompts, skills, and tools share a callable structure … type-theoretic view practical rather than just analogical." — attribution narrowed to the target's actual scope; extension to tools made explicit; "practical rather than just analogical" kept.

Relied-on claims from kb-role (shared interface, local refactoring, reversibility, llm-do hybrid VM, scheduler contrast, local scope) and all must-keep items are untouched.

Findings not touched:

- Finding 3 (info, llm-do claims rest on an un-ingested external repository): outside the supplied scope, and it calls for a source ingest rather than a text edit.

Noticed but not applied (outside scope): the footer gloss for `instructions-are-typed-callables` still says "the type-theoretic view that llm-do operationalises", which carries the same overstatement finding 2 names.
