---
title: "Solidity bytes example: using `bytes` and `bytes32`"
description: "Follow a Solidity bytes example that declares, assigns, and reads dynamic `bytes` and fixed-size `bytes32` values, with a brief guide to choosing between them."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: ["Solidity bytes type", "bytes32", "dynamic bytes", "fixed-size bytes"]
author: "editorial_team"
primary_keyword: "solidity bytes example"
owned_question: "How do you use Solidity's `bytes` and `bytes32` types in a small, understandable contract example, and what practical differences matter when choosing between them?"
risk_level: "low"
---

For a variable-length byte sequence, use Solidity’s `bytes`; for a value whose format is exactly 32 bytes, use `bytes32`. The example below shows how to declare, assign, and read each type. It uses Solidity 0.8.20 syntax as an illustration, so check it against the compiler version configured for your project before adapting it.

## A minimal Solidity bytes example

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ByteValues {
    bytes public dynamicValue;
    bytes32 public fixedValue;

    constructor() {
        dynamicValue = hex"4869";
        fixedValue = bytes32(hex"4869");
    }

    function readDynamicValue() external view returns (bytes memory) {
        return dynamicValue;
    }

    function readFixedValue() external view returns (bytes32) {
        return fixedValue;
    }
}
```

The two declarations establish different types: `dynamicValue` is `bytes`, while `fixedValue` is `bytes32`. The constructor assigns a sample hexadecimal byte sequence to each. The explicit conversion in the second assignment makes the intended fixed-size type visible. The two read functions return values using their respective types.

The `public` state-variable declarations also make the variables readable through Solidity-generated accessors. The explicit functions are included to make the return types apparent in the code. This is a compact type example, not a complete application or a claim about production readiness.

The pragma indicates a compiler-version range the source accepts; it does not itself select which compiler the project runs. Confirm that the build configuration uses a compatible compiler. Compiler and platform behavior can vary, so the configured version matters when you adapt syntax or compare results. A version choice alone does not establish that a contract is correct or secure.

## Dynamic `bytes`: store a variable-length byte sequence

Solidity’s `bytes` type represents a dynamically sized sequence of bytes. In the example, `bytes public dynamicValue;` declares a state variable with that type. The constructor assigns it `hex"4869"`, and `readDynamicValue` returns the stored value as `bytes memory`.

The sample sequence is short, but the type is not defined by that particular sample’s length. Choose dynamic `bytes` when the data you intend to represent can have a variable number of bytes. The declaration communicates that the value is a byte sequence whose length is not fixed by the type itself.

`bytes` should not be treated as another spelling of human-readable text. Solidity has a distinct `string` type for strings. Although text can be represented using bytes, the types express different intentions in contract code; do not assume that a `bytes` value and a `string` value are interchangeable without considering the required representation and conversion.

The example stops at declaring, assigning, and returning one value. It does not cover adding elements, broader array operations, or choices about storing arbitrary binary data in a production contract. Those topics are not needed to understand the basic type distinction here.

## Fixed-size bytes: what `bytes32` changes

`bytes32` is a fixed-size byte type with a width of 32 bytes. In the example, the hexadecimal literal contains a short byte sequence, and the explicit `bytes32(...)` conversion assigns it to the fixed-width variable. The `readFixedValue` function returns that value as `bytes32`.

The key practical distinction is the type’s fixed width. `bytes32` is suitable when the value’s intended representation is exactly 32 bytes. A variable-length input should not be assumed to fit that format without appropriate handling. The short sample illustrates assignment; it does not define how a contract should handle other lengths or encode a particular kind of data.

Using the same sample with both types helps show that the declaration and return type differ, even when the initial byte sequence is the same. It does not make `bytes32` a general-purpose replacement for dynamic `bytes`. The data’s intended shape should guide the choice.

## Choose `bytes` or `bytes32` for the data shape

Use `bytes` when the sequence’s length may vary. Use `bytes32` when the value is deliberately defined as 32 bytes. In practical terms, begin by asking whether the data format has a fixed 32-byte representation or whether its length can vary. The answer points to the appropriate type for this narrow comparison.

That choice does not, by itself, describe how an application encodes or decodes the value, or what input validation is needed. Those decisions depend on the data and the surrounding application, and they are outside this introductory example. This comparison also does not establish that either type is cheaper or more secure; no such conclusion follows from the type names alone.

Keep the distinction clear when reading function signatures as well as declarations. A function returning `bytes memory`, as `readDynamicValue` does, advertises a dynamically sized byte sequence. A function returning `bytes32`, as `readFixedValue` does, advertises a fixed-width value. Matching the declared type to the intended data shape makes the example’s purpose explicit to a reader of the code.

## Check the example against your compiler

Before adapting the snippet, confirm that the source pragma is compatible with the compiler version used by the project. The pragma constrains acceptable compiler versions; the project’s build setup determines which compiler is actually used. Compiler version and configuration can affect how source is interpreted, so use the project’s configured version when checking syntax rather than assuming every environment uses the version shown here.

Compile the snippet in the project’s existing development environment before building on it. This article does not claim that compilation or testing was performed. If the compiler reports a difference, consult the language documentation for the selected version and adjust the example accordingly.

Finally, treat the code as an illustration of type declaration, assignment, and reading only. It does not establish that a larger contract is correct, secure, or ready for production. The focused decision remains simple: choose dynamic `bytes` for a byte sequence of variable length, and choose `bytes32` when the intended value is fixed at 32 bytes.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
