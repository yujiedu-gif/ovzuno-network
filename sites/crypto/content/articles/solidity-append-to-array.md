---
title: "Solidity Append to Array: How Dynamic Array Growth Works"
description: "Learn how Solidity append to array operations work for dynamic arrays, how storage differs from memory, and what developers should consider about execution costs."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["solidity append array"]
author: "editorial_team"
primary_keyword: "solidity append to array"
owned_question: "How does appending an element to a Solidity array work, and what differences matter between storage and memory arrays?"
risk_level: "medium"
---

Appending to a Solidity dynamic array means adding an element at its end and increasing the array’s length. A storage array can be extended during contract execution with `push`; a memory array has a fixed size for its lifetime after allocation and cannot be extended in place using that pattern. The specific cost depends on the contract and execution context, so there is no universal gas figure for an append.

## What appending means in a Solidity array

An array holds elements of a declared type in an ordered sequence. Appending puts a new element after the existing elements. It is different from replacing the value at an existing index, and it does not mean inserting an element at an arbitrary position.

A dynamic array is one whose length can change. When an element is appended to a dynamic array in storage, the operation extends the array and its length increases. By contrast, a fixed-size array is declared with a specified length; it is not the same growable collection. The operation discussed here is specifically about appending to a dynamic array, not a general method for changing every kind of array.

In Solidity, state variables are part of a contract’s persistent data. Solidity state variables follow defined storage-layout rules, including rules for arrays, mappings, and other types. The precise layout depends on the source and compiler context. That is one reason an array’s location matters: the same type-level label, such as “dynamic,” does not mean every instance has identical behavior in every data location. [source](<https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html>)

## Solidity append to array: the basic storage pattern

A compact example of the syntax is:

```solidity
pragma solidity ^0.8.0;

contract NumberList {
    uint256[] public numbers;

    function addNumber(uint256 value) public {
        numbers.push(value);
    }
}
```

`numbers` is a dynamic state array. Calling `addNumber` executes `push(value)`, which appends the supplied value to the end of that array. The example illustrates the core operation only; it is not a complete production contract or a recommendation about access control, input validation, or interface design. The appropriate element type and who may call an append function depend on the contract’s requirements.

The contract’s code describes behavior, while its data represents state. Solidity documentation describes a contract as consisting of code, including functions, and data representing its state. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) In the example, `addNumber` is the function that requests a change, and `numbers` is the state being changed. The snippet does not establish that the surrounding contract is suitable for any particular use.

The `public` label in this illustrative declaration does not change the central point about appending: the array is a dynamic state variable and the function calls `push` on it. Readers should avoid generalizing the snippet into a claim that every array, every data location, or every operation supports the same syntax.

## Why storage and memory behave differently

`storage` refers to persistent contract data. A dynamic array stored in contract state can be extended through contract execution. In the example, `numbers` lives in storage as a state variable, so calling `numbers.push(value)` changes the persistent array state.

`memory` is temporary execution data. A memory array has a size established when it is created and cannot be extended in place after allocation using the storage-array `push` pattern. Put simply, dynamic describes a type that can have a variable length in an appropriate context; it does not mean every particular array instance can grow in place.

This distinction is especially important when reading a function signature or local variable declaration. Before choosing an operation, identify where the array lives. The sample’s `push` call works because it targets a dynamic storage array. It should not be copied as though it were a universal append operation for an array in memory or for every array type.

The claim here is limited to the storage-versus-memory distinction relevant to this append pattern. It is not a complete guide to Solidity data locations, function parameters, copying, or other array operations. Those details are separate design questions and should be evaluated against the exact code and compiler context rather than inferred from this small example.

## Execution costs and design limits

Appending changes persistent contract state, so it consumes execution resources. Ethereum contract execution is constrained by gas; gas schedules, limits, and fees can vary by network and implementation. Smart contracts also cannot directly retrieve offchain facts without an oracle or transaction mechanism. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

For that reason, do not treat an append as cost-free, and do not assume that a single fixed gas amount applies to every append. The cost depends on the contract’s state and execution context. The evidence supports that general limitation, not a numerical estimate for this code or a transaction fee quote.

Array growth also affects how the data can be used later. If a function processes every element, the collection’s size is relevant to that operation. A design that allows repeated appends should therefore consider both how much data may accumulate and what later functions do with it. This is a data-modeling consideration, not a gas-optimization recipe or a claim that a particular array will necessarily become unusable.

Keep the scope of the decision concrete: determine whether the contract needs an ordered collection that grows, and consider the operations that will read or process it. The append syntax alone does not answer whether that data model fits the intended application.

## When a different data structure may fit better

A dynamic array may fit requirements that involve ordered elements or access by index. A mapping represents a different kind of relationship between data and does not provide the same array-style sequence for straightforward enumeration. Neither structure is a universal replacement for the other; their suitability depends on how the contract needs to access and update information.

Before selecting an appendable array, consider whether order matters, whether later code needs to enumerate the elements, and how the collection’s growth relates to those operations. If those requirements do not fit an array, assess another structure against the actual access pattern. Avoid choosing a mapping merely because it appears to avoid array growth, or an array merely because `push` is simple: the operation and data model should match the contract’s needs.

The practical rule is narrow: use the `push` pattern when the code needs to add an element to the end of a dynamic storage array, distinguish that persistent state from a fixed-size memory allocation, and account for execution resources without assuming a universal cost. This explains the append operation; it does not assess a specific contract’s security or suitability for deployment.

## Sources and references

- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
