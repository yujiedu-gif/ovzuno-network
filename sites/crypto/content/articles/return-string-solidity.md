---
title: "Return string Solidity: Function Syntax and Data Locations"
description: "Learn how to return string Solidity values from functions, including basic syntax, data-location considerations, and version-specific details to verify."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: ["solidity return string"]
author: "editorial_team"
primary_keyword: "return string solidity"
owned_question: "How can a Solidity function return a string, and what syntax and data-location rules apply?"
risk_level: "medium"
---

A Solidity function can return text by declaring `string` in its return list and using a `return` statement that supplies a string value. Because `string` is a reference type, check the data-location syntax required by the Solidity compiler version used for the project; do not assume one declaration form applies to every version.

## What it means to return a string in Solidity

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. In Ethereum, a contract’s code and data are associated with a specific blockchain address. A function’s return declaration states the type of value that its execution can provide to a caller. Here, `string` names the text value type. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/>)

Returning a string is distinct from emitting an event or storing persistent contract state. The declaration and return statement describe a function result; they do not, by themselves, say that the text is retained as contract data. Ethereum’s description of smart contracts distinguishes programs in blockchain state from how a function is invoked through a transaction request. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

This article focuses on the function signature, return statement, and data-location checks—not on storing, editing, or combining strings.

## Return string Solidity function syntax

A minimal illustrative shape is:

```solidity
function label() public pure returns (string memory) {
    return "Example";
}
```

This is a syntax illustration, not a claim that the code has been compiled or tested with a particular compiler version. In it, `returns (string memory)` declares the result type and a data location; `return "Example";` supplies a string literal as the function result. The returned expression must be compatible with the declared return type.

For a project-specific example, verify the exact declaration against the compiler version in use. The snippet’s `memory` annotation should not be treated as a universal version-independent prescription: Solidity’s data-location requirements and accepted syntax must be checked in the relevant version’s documentation.

## Check data locations and compiler version

Solidity strings are reference types, so data-location rules matter in their declarations. A data-location annotation describes where reference data is handled in the relevant context; it is separate from the function’s visibility and mutability. Check the compiler version and the function context before copying a signature, especially when reviewing older code or changing a project’s compiler settings.

A practical review sequence is:

1. Identify the Solidity compiler version the project is intended to use.
2. Check that version’s official language documentation for the required data-location syntax in the function’s return declaration.
3. Confirm that the return expression matches the declared type and that the surrounding function signature is valid for that compiler.

Do not infer a version rule from a snippet alone. The illustrative declaration above shows one familiar form, but the available evidence does not establish the complete version-by-version history of string return syntax. Consult the documentation for the exact compiler version rather than extrapolating.

## Choose a function visibility and mutability that fit

Visibility and mutability answer different questions from the return type. Visibility describes how the function may be called; mutability describes its interaction with contract state. The fact that a function returns a string does not, by itself, determine either choice. Select those parts of the declaration based on the function’s intended interface and behavior, then check that they are valid under the selected compiler version.

External callers and applications may interact with contract functions through an ABI, or application binary interface. The Solidity ABI specification defines how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. An application must use an ABI matching the deployed contract interface and network address. That encoding boundary is separate from the Solidity source-level question of which data-location annotation the compiler requires. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

Accordingly, distinguish three checks: the function’s Solidity declaration, the compiled contract’s interface, and the application’s use of the matching ABI. A source signature alone does not establish that an external application is using the correct deployed interface.

## Common return-string mistakes and checks

When reading or writing a function that returns text, check the following:

- **Type agreement:** The declared return type is `string`, and the returned expression is compatible with it.
- **Data-location syntax:** The declaration follows the rules for reference types in the compiler version and context being used.
- **Function behavior:** The return declaration is not mistaken for a statement that the text is persisted in contract state.
- **Interface matching:** If an application calls the function, its ABI corresponds to the deployed contract interface and network address. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

Do not infer a fixed gas cost, permanent storage, or a security guarantee from the fact that a function returns a string. Those conclusions are outside what the return type alone specifies. For a particular project, the reliable next step is to check the targeted compiler’s documentation and the contract interface the caller actually uses.

## Sources and references

- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
