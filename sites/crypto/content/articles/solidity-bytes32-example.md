---
title: "Solidity bytes32 example: declaration, assignment, and use"
description: "A Solidity bytes32 example showing declaration, assignment, and function use, with concise notes on fixed-size values, conversions, and interpretation."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["bytes32 solidity example"]
author: "editorial_team"
primary_keyword: "solidity bytes32 example"
owned_question: "How do you declare and use a bytes32 value in Solidity, and what should developers check when converting or interpreting it?"
risk_level: "medium"
---

A Solidity `bytes32` value has a fixed width of 32 bytes. In a contract, you can declare one, assign a compatible value, pass it as a function argument, and return it. The type specifies the value’s size—not whether its contents are text, an identifier, or some other application-defined format.

## A minimal Solidity bytes32 example

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bytes32Example {
    bytes32 public storedValue;

    function setValue(bytes32 newValue) external {
        storedValue = newValue;
    }

    function getValue() external view returns (bytes32) {
        return storedValue;
    }
}
```

This example uses a Solidity compiler-version pragma to state a permitted compiler range. A pragma constrains which compiler versions are acceptable; it does not itself select or install the compiler. Before relying on version-sensitive syntax or behavior, check the documentation that corresponds to the compiler actually used. The snippet is a focused illustration of declaration and function syntax, not a claim that the contract is ready for production.

`storedValue` declares a state variable of type `bytes32`. In the Ethereum model, contract code and data are associated with an on-chain address, and contract state persists as part of that model. The variable name is only a human-readable label in the source; it does not determine what the stored bytes mean.

`setValue` accepts a parameter named `newValue`, also declared as `bytes32`. Its assignment copies that value into `storedValue`. `getValue` returns the current variable value and is marked `view` because the example’s function body reads rather than assigns the variable. The Solidity language defines code and data as parts of a contract, but the application’s interpretation of this particular data remains a separate choice. [source](<https://ethereum.org/developers/docs/smart-contracts/>) [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

## What bytes32 represents in Solidity

The name `bytes32` indicates a fixed-size byte sequence with 32 bytes. It is not the same as the dynamically sized `bytes` type, which can represent a byte sequence whose length varies. The fixed width is useful when the interface expects a value of that size, but it does not automatically establish a schema for the contents.

A schema is an agreed description of what the bytes represent and how to read them. For example, an application might define a value as an identifier or as data encoded from text. Those are possible conventions, not meanings built into `bytes32`. The contract, the calling application, and any later reader need to follow the same convention if they are to interpret the bytes consistently.

This distinction matters when choosing a type. If a function expects `bytes32`, a caller must provide data in the form the contract interface expects. The type’s fixed width does not by itself tell a caller whether a particular value is valid for a business purpose. That requires application-specific rules, such as which input formats are acceptable and what a value is allowed to represent.

## Assigning and passing a bytes32 value

In the example, assignment occurs inside `setValue`: the function receives one `bytes32` value and writes it to the state variable. The return declaration on `getValue` tells the interface that the function returns a `bytes32` value. These declarations provide a clear function boundary: a caller supplies a value, and a read retrieves the stored value in the declared type.

For an application to call an EVM contract correctly, it also needs the contract’s ABI. The ABI, or application binary interface, defines how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. The application should use an ABI that matches the deployed contract interface and the network address it intends to call.

That interface check is distinct from deciding what the bytes mean. A matching ABI helps encode a function call and decode its declared return value; it does not supply an application’s interpretation scheme. For instance, a decoded `bytes32` return value is still just a fixed-size byte value until the application applies the format it expects.

The example keeps the operation simple so the type declarations remain visible. It does not define restrictions on who may call `setValue`, validate whether a particular value is appropriate, or specify how a client should convert text into bytes. Those behaviors would require additional, explicitly designed rules. Avoid inferring them from the presence of a `bytes32` parameter or state variable.

## Checks before converting or interpreting bytes32

Before converting or decoding a value, identify the intended format and consult the Solidity documentation for the compiler version in use. Conversion and decoding are not interchangeable descriptions: a conversion changes or re-expresses a value according to language rules, while decoding reads a sequence according to a chosen format. The type alone does not establish that incoming bytes follow that format.

When input originates outside the contract, validate that it meets the application’s expected format and length before treating it as meaningful content. If the application intends to represent text, it needs an agreed text encoding and a defined way to handle the fixed-width value. In particular, decide what should happen when input is shorter than the available width or does not meet the expected format. Do not assume that a particular conversion or decoding path will produce the intended text without checking the applicable rules and verifying the input conditions.

Keep the following distinctions in view:

- **Width:** `bytes32` specifies a fixed size of 32 bytes.
- **Representation:** conversion rules determine how a value is represented under the language’s rules.
- **Meaning:** the application’s documented convention determines what the bytes signify.
- **Validation:** application logic checks whether a supplied value follows the expected format and is acceptable for the intended use.

These are separate responsibilities. A value can have the correct width while failing an application’s format checks, and a well-formed byte sequence can still have no agreed meaning between the contract and its caller.

A `bytes32` declaration also should not be treated as an encryption, privacy, or security guarantee. It identifies a data type, not a protection mechanism. Likewise, the short example’s assignment and return functions do not prove that a broader contract is correct or secure. Solidity documentation notes that using the language does not by itself guarantee correctness or security; software, compiler, and platform bugs remain possible, and development practices such as review and testing are recommended.

For a small learning example, the practical takeaway is to keep the declaration and the interpretation separate: declare `bytes32` when the interface calls for a fixed-width value, pass and return it using a matching interface, and define and validate the format wherever the application assigns meaning to those bytes. That describes the type’s role without treating it as a complete encoding scheme or a guarantee about the surrounding contract.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
