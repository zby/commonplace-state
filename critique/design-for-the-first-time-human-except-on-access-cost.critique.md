# Critique: Design for the first-time human, except on access cost

**Note:** kb/notes/design-for-the-first-time-human-except-on-access-cost.md
**Central commitment:** The competent-first-time-human heuristic is a reliable proxy for designing for the agent on nearly all affordances, with access cost being *the single* load-bearing exception where the proxy inverts a design decision.
**Critique mode:** claim

## Strongest case against it

Hold the position of a **context-engineering / prompt-injection-security designer** — someone whose day job is making agents behave correctly under adversarial and degraded inputs. Their thesis: the first-time-human proxy does not have *one* load-bearing exception; it has *several*, and access cost is merely the one this author already happened to formalize in a prior note. Calling it "the single axis where the proxy gives the wrong answer" is a generalization from a sample of one prior insight, dressed up as a structural result.

The case has three legs, each naming a place where newcomer-human ergonomics *invert* the right agent design — not merely "differ," but point the design decision the opposite way:

1. **Authority and injection.** A newcomer human treats text on the page as inert information to be evaluated. An agent treats text it reads as potentially *instruction* — imperative sentences, "ignore previous," tool-call-shaped strings, or embedded directives in quoted source material can hijack behavior. Designing for the human says "include the verbatim quote, the example adversarial prompt, the literal error message." Designing for the agent says the opposite: neutralize, fence, or summarize that same content because loading it is not free of behavioral risk. This is a clean inversion, and it is not access cost — a single fenced line is cheap on bytes yet dangerous on authority. The note's own glossary (behavioral-authority, system-definition-artifact) shows the repo already treats "what force does consumed text carry" as first-class, which makes the omission sharper, not softer.

2. **Position and recency effects.** A competent human who reads a 2,000-word note weights the argument by its merits regardless of where the key sentence sits. An agent's effective use of loaded content is order- and position-sensitive (lost-in-the-middle, recency dominance). The right *structure* for an agent — front-load the operative instruction, repeat the binding constraint near the point of use, avoid burying the load-bearing clause in paragraph four — is structure a newcomer-human-ergonomics lens would call redundant or condescending. Here human ergonomics actively mislead on *structure*, which the note explicitly claims as a domain where the proxy holds ("naming, structure, orientation, and prose").

3. **Ambiguity and underspecification.** A competent newcomer human, hitting a gap or an ambiguous instruction, asks a clarifying question or applies judgment and defers. An agent confronted with the same gap confabulates a plausible-looking completion and proceeds. Designing for the human tolerates "the reader will figure out the edge case"; designing for the agent demands the edge case be closed or an explicit refusal path be specified. Again an inversion, again not access cost.

The opponent's punchline: the note even *lists* these divergences in its Scope section ("tolerance for ambiguity, recall of earlier context, susceptibility to injected instructions") and then dismisses them in a single subordinate clause — "this note isolates the one that most often inverts a design decision." But "most often inverts" is an unsupported empirical ranking. The note offers exactly one worked instance (the index-weight-navigation workshop) for access cost and *zero* attempts to show the other three invert less often. For a security or structure designer, injection and position effects invert decisions constantly and silently, with worse failure modes (wrong behavior) than access cost's failure mode (merely expensive behavior). So the title's "except on access cost" is not a discovered boundary; it is a spotlight on the author's prior work, and the claim that this is *the* exception is the note's softest joint.

## How the note engages it

**Partially engaged, and the engagement is the weakest part of the note.** The Scope section (lines 36-37) explicitly anticipates the objection by name — it acknowledges "tolerance for ambiguity, recall of earlier context, susceptibility to injected instructions" as other possible divergences. This is honest, and it pre-empts the lazy version of the critique ("you forgot about injection!").

But anticipation is not engagement. The note does three things that an informed opponent would reject:

- It **asserts** access cost "most often inverts a design decision" (line 37) with no comparative evidence — no instance count, no mechanism for why access cost inverts more frequently than injection or position effects.
- It **conflates "inverts" with "is interesting to me."** The body's whole machinery (access mode, per-consumer materialization, single source of truth) is built around access cost. The other divergences get one clause because the author has no fix for them, not because they invert less often.
- It **claims the structure domain is safe** ("newcomer-human ergonomics predict agent-good design on naming, structure, orientation, and prose," line 37) while position/recency effects are precisely a *structure* divergence. The note's safe-list and its own escape-hatch list overlap, and it does not notice.

So the central commitment — "the single axis where the first-time-human proxy gives the wrong answer" (line 19), "access cost is the load-bearing exception" (line 37) — is stated as a result but defended only as a preference.

## Constructive findings

- **Demote the title claim from "the one exception" to "a load-bearing exception" — or earn the ranking.** Either retitle to something like "the first-time-human proxy breaks hardest on access cost" (a strength claim, defensible by the materialization fix being unusually clean) or supply the comparative argument the current title presupposes: why does access cost invert *more* decisions than injection-authority?
- **Distinguish two kinds of exception.** Access cost is a *cost* inversion (cheap-for-human, expensive-for-agent → wrong-but-recoverable design). Injection/authority and confabulation are *correctness* inversions (safe-for-human, behavior-corrupting-for-agent → wrong-and-dangerous design). A note arguing about which exception is load-bearing should at least name the axis it is ranking on; on a correctness axis, access cost is not the leader.
- **Resolve the structure-domain contradiction.** Position/recency effects sit inside "structure," which the note lists as a domain where the proxy holds. Either carve position-sensitivity out of "structure" explicitly, or concede that structure is not uniformly safe.
- **Strengthen by generalizing the fix, not the diagnosis.** The genuinely strong, defensible core here is *per-consumer materialization over one source of truth*. That pattern survives even if access cost is not the only exception — it is the right response to *any* consumer-profile divergence with a tooling remedy. Leading with the fix (and its single-source-of-truth invariant) as the durable contribution, with access cost as the *exemplar* rather than the unique exception, would make the note far harder to attack.

## Secondary objections (optional)

- **"Competent first-time human" is underdefined and does the work silently.** A competent human with `rg`/grep-equivalent tooling and a competent human with only a scrollbar have different access modes — the note half-admits this at line 25 ("a human forced to consume an artifact with no structure... reads it linearly"). If the proxy's behavior depends on which human you imagine, the heuristic is less stable than presented; the access-mode reframing arguably *dissolves* the human-proxy framing rather than refining it.
- **The "carriers can swap" reframing undercuts the title.** Lines 21-25 argue the real divider is access mode, not human-vs-agent. Taken seriously, this means the title ("design for the first-time human") names the wrong variable, and the note should be titled around access mode. The note keeps both framings without fully reconciling which is primary.
- **Single instance for the central mechanism.** The only worked example of the exception is the index-weight-navigation workshop (line 33), which is also the note's own originating context. One instance that is also the source of the generalization is thin support for a claim pitched as a structural law about two consumer profiles.
