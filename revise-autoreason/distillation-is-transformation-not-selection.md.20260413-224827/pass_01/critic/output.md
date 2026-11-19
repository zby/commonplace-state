# Critic report — pass 01

## 1. The core insight is stated three times before the reader gets new material

The introduction says distilled artifacts are "of a different kind." The paragraph after the table restates this at length ("None of these artifacts is 'part of' the trace…"). The opening of "Implication for memory-system design" restates it again ("no amount of trace compression produces a preference, an ADR, or a skill"). Each repetition adds a nuance, but the reader traverses essentially the same ground three times before reaching the design implication (memory primitives as an inventory of shapes) that is actually new. The note would read faster if the post-table paragraph were tightened so it doesn't fully re-argue the point the table just demonstrated.

## 2. "The substrate must persist" is weakly connected to the main claim

The preceding sections argue that distillation is transformation. This final section shifts to a different concern — that raw traces should be retained because distillates are derived and the shape inventory evolves. The connection is real (if distillates are transformations, then they don't subsume their source), but the note doesn't make this bridge explicit. The section reads as a separate point tacked on rather than a consequence of the transformation framing. The title introduces "substrate" without setup; the reader must infer that it means "raw trace."

## 3. The long sentence in the second paragraph of "Implication" is overloaded

"Memory primitives, then, are not denser traces but different kinds of objects — each with its own structure, invariants, retrieval affordances, and lifecycle." continues into an example and a contrast clause. The sentence carries the section's main claim, a four-item enumeration, a concrete example (preference), and a negation of the wrong frame, all chained with dashes and commas. The density works against readability at the moment the note introduces its most actionable idea (design the inventory of shapes).

## 4. The third paragraph of "Implication" feels orphaned

"'Traces → memory primitives' as a single arrow is too coarse…" elaborates the family-of-transformations idea, which is closely related to the inventory-of-shapes point in the paragraph above. Standing alone as a one-paragraph closer to the section, it reads more like a footnote than a progression. Either it belongs with the preceding paragraph or it needs a clearer signal for why it's separate.

## 5. "The richest concrete case in hand" is unsupported

The scoping sentence (line 13) claims memory distillation is "the richest concrete case in hand" but gives no reason. The note only demonstrates memory-distillation examples, so the reader can't evaluate the comparison. "The concrete case in hand" would be accurate without the unsupported superlative.
