### Summary

Claimed scope: for agents navigating a typed KB, document types (together with descriptions) supply structural hints before opening. These let an agent "narrow from hundreds of files to the few it needs without opening any of them". The title says "types" without restriction, so a reader would take the claim to cover every document type in such a KB. The support on the page is derivation from premises (stateless agents, finite context, verifiable structural types), plus inherited results from the verifiability and enforcement notes. There is no direct evidence or worked case.

The derivation reaches types that make a structural promise, illustrated by `spec`, `structured-claim` and `index`. It does not reach the base `note` type. The note does not acknowledge that type, yet it is the KB's default and the type of this note itself. The linked verifiability note describes it as "Default — read it to find out what you can do with it", which is a type that gives no pre-open operational hint. The derivation also does not cover the efficacy claim "without opening any of them". That claim depends on descriptions being discriminating, which the linked enforcement note says the type system does not guarantee ("remains a judgment-level check"). There is no Scope section, no transfer argument and no conjecture marking for either surplus.

### Findings

- WARN: The title and description invite reliance on "types" giving pre-open structural hints across all document types. The supporting derivation only covers types that assert a distinctive structural property. The note gives no transfer relation to the base `note` type, which most documents use, and marks no boundary for it. For those documents the hint comes almost entirely from the description, which is not what the title credits.
- INFO: "Together they let an agent narrow from hundreds of files to the few it needs without opening any of them" is a supporting claim. It presents an efficacy outcome that the derivation does not exercise. The premises establish that routing is *informed*, not that it is complete without opening. That would require discriminating descriptions, which linked material says are not enforced.

### Suggested Revision

Add a `## Scope` section. It should state that the structural hint is carried by narrower types and traits. For the base `note` type, routing rests mainly on the description and title. The "without opening any" outcome also depends on descriptions being discriminating, which validation does not check.

## Result: WARN
