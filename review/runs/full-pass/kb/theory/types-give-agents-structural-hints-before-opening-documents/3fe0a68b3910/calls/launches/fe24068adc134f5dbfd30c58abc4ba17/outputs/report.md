# Compression Bundle Review: Types give agents structural hints before opening documents

**Target:** `kb/theory/types-give-agents-structural-hints-before-opening-documents.md`
**Bundle:** [compression-bundle/](./compression-bundle/README.md)

## Overall Result

WARN

## Gate Results

| Gate | Result | Summary |
|---|---|---|
| compression/core-claim-obscured | INFO | The title claim appears early in paragraph 2. The sharper claim is the type/description split: type gives the kind, description picks the instance. It sits in paragraph 3 and is missing from the title and opening. |
| compression/branch-bloat | PASS | Each side paragraph supports the routing claim: description as filter, verifiability as the condition for useful hints, enforcement as the condition for reliable metadata. Each is one paragraph or less and delegates by link. |
| compression/detail-overhang | PASS | The examples (`spec`, `structured-claim`, `index`; "design note" vs "Evidence and Reasoning sections") are one clause each and do contrastive work. The setup paragraph is three sentences. |
| compression/marginal-value-redundancy | WARN | The "informed routing decision" point closes three consecutive paragraphs. Paragraph 4's last sentence only restates that paragraph's opening sentence. |

## Findings

### compression/core-claim-obscured

- INFO: The title and paragraph 2 say that *types* give structural hints. The frontmatter description and paragraph 3 make a more specific claim: "The type tells the agent *what kind of thing* a document is; the description tells it *which instance* … Together they let an agent narrow from hundreds of files to the few it needs without opening any of them." That split is the note's most memorable and actionable commitment, but it comes third, after the setup and the type-only examples. One fix is to move the two-part statement up into or right after paragraph 2. Another is to align the title with the description. See synthesis item 1 for the choice between these.

### compression/marginal-value-redundancy

- WARN: Paragraph 4 ("The [verifiability criterion] …"): the closing sentence "The structural promise is what makes the routing decision informed rather than blind" repeats the paragraph's opening ("is what makes this work") and the "informed routing decisions" phrase from paragraph 2. It adds nothing beyond the paragraph's own opening. Cut it, or merge its "rather than blind" contrast into the opening sentence.
- WARN (minor): Paragraph 2's closing sentence, "These hints enable informed routing decisions: the agent reads a type and description, then decides whether to load the full document", previews paragraph 3's "Together they let an agent narrow … without opening any of them." Paragraph 2 brings in the description before the note explains its role. Either drop "and description" here and let paragraph 3 introduce it, or fold the two sentences into one statement of the type+description routing step.

## High-impact Simplification Opportunities

### 1. Make the type/description split the stated thesis

- Location: Title and paragraph 2 ("Types solve this by giving agents structural hints *before* opening a document…") vs. paragraph 3 ("The type tells the agent *what kind of thing* a document is; the description tells it *which instance*…").
- Reader problem: A reader who stops after the title and paragraph 2 gets "types are routing hints". They miss that type alone cannot select among same-type documents, which is the reason descriptions matter. The note's working claim is spread over paragraphs 2–3, and the "informed routing" sentence repeated at three paragraph ends stands in for that claim.
- Direction: Put the two-part claim right after the setup: type gives kind and affordances, description chooses the instance, and together they support a load/skip decision without opening files. Paragraphs 4 and 5 then become the two conditions for this to work: types must assert verifiable structure, and the metadata must exist reliably. Drop the repeated "informed routing" closers. One possible framing, for illustration only: "Type and description together let an agent decide whether to open a document: the type says what operations it affords, the description says which instance fits the task."
- Combines: compression/core-claim-obscured (INFO), compression/marginal-value-redundancy (both WARNs).
- Preserve or decide: The note does not choose its scope. The title and filename claim something about *types*; the frontmatter description and paragraph 3 claim something about *types and descriptions jointly*; and paragraph 3 calls the description "the most important field". The author must decide whether this note argues for types, with description as a supporting filter, or for the type+description pair. Retitling would also change the filename, link texts and the `title-as-claim` trait. Keep the conditional reading in paragraphs 4–5: hints help only when types are verifiable and metadata is enforced. The two links carry these conditions and should not be compressed away.
