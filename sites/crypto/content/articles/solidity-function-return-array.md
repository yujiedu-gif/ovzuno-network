---
title: "Solidity Function Return Array: Syntax and Key Rules"
description: "Learn how a Solidity function return array is declared and used, including data-location choices, state reads, and important compiler-version caveats."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity function return array"
owned_question: "How does a Solidity function return an array, and what determines whether that array is returned from a function or read from contract state?"
risk_level: "medium"
---

A Solidity function returns an array by declaring an array type in its `returns` clause and supplying a compatible value when execution completes. The function may provide an array it creates or a result based on an array in contract state; the returned output is not, by itself, a change to that stored array. To understand which case applies, inspect the function’s implementation, declaration, and data-location annotations.

## What does it mean to return an array from a Solidity function?

A return value is data a function supplies to its caller when execution completes. In Solidity, a smart contract contains code in functions and data in state at an on-chain address. The function’s declared return type specifies the kind of output it provides, while its implementation determines where that output comes from.

For an array-returning function, the output could be an array value created during execution, or a value based on array data already held in contract state. These are different sources for a return value, but both involve a function supplying output to its caller. Returning an array does not by itself mean the contract’s stored array was modified.

This distinction also helps avoid treating the returned value as a writable reference to persistent contract storage. The function returns data according to its declaration and execution; that alone does not grant the caller a way to change the stored array. To determine whether state changes, examine the function’s code rather than inferring behavior from the return type alone.

## Solidity function return array syntax

The basic pattern places an array type in the function’s `returns` clause. This illustrative example declares a function that returns a memory array:

```solidity
pragma solidity ^0.8.0;

contract ArrayExample {
    function sample() external pure returns (uint256[] memory) {
        return new uint256[](2);
    }
}
```

The declaration `uint256[] memory` says that the output is an array of `uint256` values and identifies a data location for the reference-type value in this function context. The `return` statement supplies the expression that fulfills the declaration. In this example, `new uint256[](2)` creates the value returned by the function.

The example is for explaining the shape of a declaration, not a universal template for all compiler versions or use cases. Its pragma specifies a range of acceptable compiler versions; it does not establish that every version in that range has identical rules or behavior. Use the compiler version selected for the project and check the corresponding Solidity documentation before copying syntax into a contract.

The returned expression must be compatible with the declared array type. That means reviewing the element type as well as the fact that the output is an array. If the declaration and returned expression do not correspond, the function does not describe the intended output. Do not infer validity solely from a superficially similar declaration in another function or compiler context.

The ABI, or application binary interface, describes how applications and EVM contracts encode function selectors, arguments, return values, errors, and events. For an array return, the ABI is part of the interface the caller uses to interpret the output. A caller should use an ABI that matches the deployed contract interface; a mismatched description can lead the application to expect a different output than the contract provides.

## Memory, calldata, and storage in array returns

A data location describes where reference-type data is accessed or held in a particular context. Solidity’s `memory`, `calldata`, and `storage` annotations are not interchangeable labels. An array’s element type answers what its elements are; its data location concerns the context in which that reference-type data is used.

In the illustrative function, `memory` appears with the array return declaration. By contrast, `storage` relates to data that forms part of the contract’s state. `calldata` is another location that can appear in function contexts. These distinctions matter when interpreting an array declaration, but the precise rules that apply to a particular function must be checked against the language documentation for the compiler version in use.

A practical way to read an array-returning function is to ask two separate questions. First, what array type does the `returns` clause declare? Second, where does the implementation obtain or hold the data it supplies? The first question concerns the output’s declared type. The second requires reading the function body and its data-location annotations. Neither question, considered alone, establishes that the function modifies persistent contract state.

## Returning an array read from contract state

A function can provide a result based on an array held in contract state. The return declaration describes the output, while the function body determines how it is derived from state. The returned output is not the same thing as exposing a writable reference that lets a caller directly edit the stored array. If the function also changes state, that behavior must be determined from its implementation rather than assumed from the existence of a return value.

Do not conflate an explicitly declared function with a public state-variable getter. A function that declares an array in its `returns` clause has an explicit output interface. A public state variable is a separate contract declaration and interface mechanism; the fact that an array is public does not, on its own, establish that its getter has the same signature or output shape as an explicitly declared array-returning function. Inspect the actual declaration and compiled ABI to identify what callers can invoke and what output they should expect.

The broader contract context matters here. A Solidity contract consists of code, including functions, and data representing its state. That distinction makes it possible to describe a function’s output separately from the persistent data on which the function may operate. When reviewing a function, follow the path from state access to the returned expression. This reveals whether the result is constructed, derived from stored data, or supplied through another route, without treating “returns an array” as a complete description of the function’s behavior.

## What to verify before using an array return

Start by checking the Solidity compiler version selected for the project. Consult version-matched language documentation for the applicable return and data-location rules. Confirm that the array return declaration is valid in that context, and that the expression supplied to `return` is compatible with the declared array type. A syntax example should not substitute for checking the specific compiler version and function declaration.

Next, inspect the ABI output and the deployed contract interface. Confirm that the ABI describes the return value the function actually declares, and that the application uses an ABI matching that deployed interface. For an array, verify that the caller’s expected element type and output structure correspond to the contract’s declared output. This step addresses how the caller interprets the returned data; it does not establish what the function reads or changes internally.

Then inspect the function body to determine whether its output is created in the function or based on an array in contract state. Check data-location annotations in their particular context rather than assuming that `memory`, `calldata`, and `storage` can be substituted for one another. If the function reads state, distinguish the result it returns from the persistent array itself. If you are examining a public state-variable getter, review that interface separately from an explicitly declared function.

Finally, consider the array’s size and the execution context in which the function is used. The evidence here does not establish a universal safe array size, cost, or practical limit, so a general rule about those matters would be unwarranted. Those questions require analysis of the specific function, its caller, compiler configuration, and execution path. The syntax example explains how an array return can be declared; it is not a performance guarantee or a complete strategy for handling large arrays.

## Sources and references

- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
