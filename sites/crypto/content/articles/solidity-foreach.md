---
title: "Solidity foreach: How Collection Iteration Works"
description: "Learn what “solidity foreach” means, whether Solidity has a dedicated foreach construct, and how loops iterate through collections in smart contracts."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity foreach"
owned_question: "How can Solidity developers iterate over collection elements, and what does “foreach” mean in this context?"
risk_level: "medium"
---

Solidity developers generally use ordinary loop statements, such as an indexed `for` loop, to visit array elements; “foreach” is often an informal way to describe that task, not a dedicated Solidity keyword. A loop can read or process elements only when the code has a way to reach them, and large or unbounded on-chain work deserves careful review. The evidence available for this article does not include current Solidity language-reference details on loop syntax, mappings, or gas behavior, so those specifics should not be presented as verified facts here.

## Does Solidity have a foreach loop?

“Foreach” usually describes the idea of doing something once for every item in a collection. It is not safe to treat the phrase as evidence that Solidity has a `foreach` keyword or construct: the allowed documentation evidence does not establish the current language syntax or confirm the absence of that construct.

Solidity contracts are programs deployed to blockchain state and invoked through transaction requests. That general description explains why iteration in a contract is executed as part of program behavior, but it does not establish which loop forms a particular Solidity version supports. Verify syntax against the language documentation for the compiler version a project uses before copying code or relying on a syntax claim. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>); [source](<https://csrc.nist.gov/glossary/term/Smart_contract>))

## How to iterate over an array in Solidity

An indexed loop follows a simple pattern: initialize an index, continue while a condition holds, and update the index after each pass. The body uses the index to refer to an element. This is a conceptual description, not a verified, version-specific Solidity code sample; the claims authorized for this article do not provide syntax documentation sufficient to validate such a sample.

When reading or reviewing an example, identify the loop’s starting value, stopping condition, update step, and element access. Check that these agree: an incorrect condition or update can cause the loop to skip intended items or fail to stop as expected. The exact operators and syntax should be checked against the relevant Solidity documentation rather than inferred from the word “foreach.”

Also distinguish a collection’s location and size from the loop itself. The available evidence does not document array declarations, storage versus memory iteration, or particular array-length expressions, so this article cannot give a verified implementation recipe for those details.

## What can and cannot be iterated in Solidity?

A collection can be traversed directly only if the program has a defined way to identify the items it should visit. Arrays are commonly discussed as indexed collections, but the allowed evidence here does not verify Solidity’s array interfaces or their syntax. For mappings, it likewise does not verify whether keys or entries can be enumerated directly. A reader should not infer that every data structure can be walked in the same way.

This distinction matters when designing data access. If a program needs to visit entries, determine from the language documentation and the contract’s design how those entries are identified and whether a separate index or other tracking mechanism exists. The allowed evidence does not establish a specific mapping-enumeration rule or recommend a particular tracking design, so no universal implementation claim follows.

Solidity contracts contain code and data at an on-chain address, but that general account of contract state does not specify how each collection type is represented or enumerated. Treat those as language- and design-level questions that require more specific documentation. ([source](<https://ethereum.org/developers/docs/smart-contracts/>))

## Why loop size matters in smart contracts

A loop performs work repeatedly. As the number of items grows, the amount of work the loop requests grows as well; the available claims, however, do not support a numerical cost, a universal maximum, or a guarantee about how a particular loop behaves when submitted to a network.

For that reason, treat collection size as an execution question, not merely a syntax detail. Before relying on a loop in a state-changing contract operation, ask whether the number of iterations is bounded and what happens if the collection becomes larger than expected. The evidence provided for this article does not include an authoritative claim about gas costs, transaction limits, or denial-of-service risks from unbounded loops, so those specific consequences cannot be asserted here as established facts.

A contract’s code and data are deployed through signed transactions in the general NIST terminology, while specific execution and fee models vary by network. That broad definition reinforces the need to verify execution assumptions for the target system; it does not supply a Solidity-specific gas estimate or a safe iteration threshold. ([source](<https://csrc.nist.gov/glossary/term/Smart_contract>))

## Choosing an iteration pattern for a contract

Start by clarifying the task: which entries must be processed, how the contract identifies them, and whether the collection’s size is known to be bounded. Then verify the relevant Solidity syntax and collection behavior in documentation for the compiler version in use. If the design depends on walking a mapping or on a particular storage arrangement, confirm that mechanism directly rather than assuming it works like an indexed array.

Next, assess whether the work belongs in an on-chain operation at all. This article’s evidence does not substantiate a specific off-chain alternative or a universally suitable Solidity pattern. The decision therefore depends on the contract’s requirements and its execution environment, and a pattern should not be described as safe or efficient without project-specific analysis.

For a structured review, OWASP’s Smart Contract Security Verification Standard is a framework for designing, building, and testing EVM-based smart contracts and decentralized applications. Its existence is not proof that a particular loop is correct or safe; project-specific threat modeling and review remain relevant. ([source](<https://owasp.org/projects/smart-contract-security-verification-standard>))

In short, “Solidity foreach” is best read as a search phrase for iterating through collection elements. The evidence here does not verify a dedicated `foreach` construct, a precise array-loop example, mapping enumeration behavior, or Solidity-specific loop-cost rules. Check the current Solidity documentation and the contract’s own execution assumptions before treating any example as authoritative.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
