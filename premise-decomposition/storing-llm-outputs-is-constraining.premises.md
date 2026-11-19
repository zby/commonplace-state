# Premise decomposition: Selecting an LLM output fixes a result, not its interpretation

**Note:** kb/notes/storing-llm-outputs-is-constraining.md
**Register:** claim
**Central commitment (one sentence):** When one LLM output is selected, persisted, versioned, and given operative reuse, it fixes the result identity for that consumption path without by itself proving a unique interpretation, creating an artifact-testing target distinct from the generator.

## Premises and counterexamples
1. **For a specified consumption path, selecting one candidate for operative reuse makes that candidate, rather than merely any archived completion, the result with downstream force.** — HOLDS — An active hunt found only audit-only retention, retaining every candidate, and later re-selection; none selects one candidate for operative reuse on the same path.
2. **Persisting and versioning the selected output fixes the exact bytes that every later consumer on that path receives.** — DEFEATED — A selected text stored as a Git blob with LF line endings can be checked out with CRLF conversion before a Windows program reads it; the versioned blob is fixed, but the consumer receives different bytes. — LOCAL — instance
3. **Fixing an artifact's identity or bytes does not by itself establish that its natural-language content has a unique legitimate interpretation.** — HOLDS — An active hunt found exact literals interpreted under closed grammars, but their uniqueness comes from the grammar and context, not from the act of fixing their bytes.
4. **For selection to determine what later behavior is based on, a consumer must receive the selected artifact through a channel that gives it force.** — HOLDS — An active hunt found consequential audit, compliance, and training uses, but each supplies a consumer, channel, and force; an archive with no such path does not determine later behavior.
5. **A fixed selected artifact is a stable target for semantic and corpus-level contract testing without also pinning the context and dependencies against which those contracts are judged.** — DOUBTFUL — The fixed output “follow the policy at `/policies/latest`” can denote different rules after that mutable target changes, and an unchanged note can pass or fail a corpus-level uniqueness check as the surrounding corpus changes. — LOCAL — instance
6. **For every generator, a good selected artifact says nothing about what another run will produce.** — DEFEATED — A generator defined to replay one immutable, content-addressed artifact for its sole supported input produces that same artifact on every successful run, so the selected artifact is informative about the next run even though inspecting it still does not test execution failures. — LOCAL — instance

## For the human
Look first at the stability premise: fixed artifact bytes do not freeze mutable referents or corpus context, so the note should locate exactly what remains stable for semantic and corpus-level tests.
