---
title: "Solidity hashmap: what mappings mean and how they work"
description: "Learn what “solidity hashmap” refers to in Solidity, how mappings associate keys with values, and why they do not behave like iterable collections."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity hashmap"
owned_question: "What does “hashmap” mean in Solidity, and how do Solidity mappings store and retrieve values?"
risk_level: "low"
---

In Solidity, “hashmap” is an informal way to refer to a mapping: a contract data structure that associates keys with values. A mapping supports lookup by a key, but it does not behave like a general-purpose collection with a built-in list of keys or direct iteration over every entry. The term “hashmap” is not the Solidity type name.

## What “hashmap” means in Solidity

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. In Ethereum, a contract has code and data in its state at a blockchain address. Solidity mappings are one way to organize contract data for key-based access; they should not be treated as an entire database or as interchangeable with every other data structure. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/>)

In ordinary programming discussions, “hashmap” often names a key-to-value collection. When someone uses that term in a Solidity context, they usually mean a mapping. For accurate Solidity terminology, use “mapping,” which is the language construct’s name.

The distinction from an array matters at a high level: a mapping is organized around querying by a known key, while an array has a different access and enumeration model. This article focuses on the mapping lookup model, not on array operations.

## How a Solidity mapping associates keys and values

Conceptually, a mapping relates keys of an allowed key type to values of a declared value type. A contract can request the value associated with a key. For example, a hypothetical mapping from account identifiers to balances represents the idea “look up the value for this identifier.” This is an illustration of the key/value relationship, not a claim about a particular contract’s implementation or its accounting rules.

The key is supplied to access the associated value. That makes mappings useful when the contract’s task is to retrieve information by a key it already has. It does not imply that the mapping itself offers a way to discover all keys that have been used.

The available evidence for this article does not establish Solidity’s exact declaration syntax, full list of permitted key types, or the language’s precise lookup and default-value rules. Those details should be checked against the Solidity documentation for the compiler version used by a project. The general description here is limited to mappings as key-to-value access structures; it is not a substitute for version-specific language documentation.

## Mapping defaults and missing-key behavior

A mapping lookup should not automatically be interpreted as proof that a value was explicitly set. The available evidence does not verify the exact default value returned for each Solidity value type or whether a mapping provides a built-in presence check. Accordingly, this article does not state those details as language rules.

For a concrete contract, consult the applicable Solidity documentation and examine the contract’s own representation of its data. In particular, if the application needs to distinguish “no entry has been recorded” from “an entry has the type’s default value,” confirm whether the chosen design tracks that distinction separately. A key/value association alone does not establish what the application considers a valid, present, or initialized record.

This limitation is important when reading contract code: a lookup result is meaningful only in the context of the value type and the application’s rules for recording and interpreting entries. Do not infer application-specific meaning from the informal label “hashmap.”

## What mappings cannot do by themselves

A mapping is not a built-in key directory. The available evidence does not verify Solidity’s detailed enumeration behavior, so this article does not make a version-specific claim about iteration mechanics. It also does not establish that a mapping exposes a key list or a direct operation for walking every entry. Readers should therefore not assume that knowing a mapping exists means a contract can ask it for all stored keys.

If an application requires enumeration, ordering, or a count of recorded entries, that requirement needs to be addressed by a broader data design. The exact auxiliary structures and their trade-offs depend on the contract and are outside the evidence available for this article. A mapping alone should not be presented as a complete database abstraction or as equivalent to a collection designed around listing its members.

## Choosing a mapping for a contract’s lookup need

A mapping is a reasonable concept to consider when the contract knows the key it wants to query and needs the corresponding value. Before settling on that model, ask whether the application also needs to list keys, preserve an order, or report how many entries it has recorded. Those requirements are not answered merely by choosing a key-to-value structure.

Keep the decision bounded: this explanation does not compare gas costs, security properties, recovery options, or deployment approaches. Those questions require evidence about the specific Solidity version and implementation. For a first understanding of “Solidity hashmap,” the key point is simpler: the term usually refers to a mapping, which associates keys and values for lookup, but should not be assumed to supply collection-wide enumeration or other database features.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
