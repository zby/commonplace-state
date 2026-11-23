
# Report

Finding 1 (source-residue, warn): applied `fix-strategy-taxonomy.md#unframed-domain-examples`.
The passage "This requires **name-based dispatch**: components are identified by
string name rather than direct object reference." now reads "llm-do achieves this
shared interface through **name-based dispatch**: ...". This takes the finding's
second option: name-based dispatch is how llm-do achieves the shared interface. It
is no longer stated as a requirement of every unified calling convention.

The following sentence, which lists what names enable, is unchanged. It is in
scope, but it already describes properties of names, and its first item ("the LLM
outputs a string, the runtime looks it up") already marks the LLM-emitted-call
case the finding identifies. Relied-on content from kb-role is kept: "the same name
can resolve to either neural or symbolic" and the opening paragraph's general
claim. The description field still says "llm-do demonstrates this with name-based
dispatch", which matches the new framing.

No links, quoted spans or other passages changed. The result has no findings that
were left untouched.
