---
title: "Solidity using for: How Library Directives Work"
description: "Learn how Solidity using for attaches library functions to types, how directive scope works, and which compiler-version details to check."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["solidity using"]
author: "editorial_team"
primary_keyword: "solidity using for"
owned_question: "How does Solidity’s `using ... for` syntax make library functions available on a type, and what changes when the directive is global?"
risk_level: "medium"
---

Solidity’s `using ... for` directive makes eligible library functions callable with method-style syntax on a specified type. A global directive can make that attachment available beyond a single contract, but its exact scope and compatibility depend on the Solidity version and where the directive is declared. Check the language rules for the compiler you use rather than assuming all declarations behave alike.

## What `using ... for` means in Solidity

A library is a collection of functions that a contract can call or reuse through public interfaces; this is one example of smart-contract composability. The `using ... for` directive connects functions from a library to a type so code can express an operation in method style. The directive changes how eligible functions are made available in source code; it does not change the type’s underlying definition. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Conceptually, if a library function takes a value of type `T` as its first argument, method-style notation can present that value as the receiver: `value.someFunction(otherArgument)`. The notation is an interface convenience. To understand what the call does, inspect the library function and confirm how the compiler resolves the receiver and arguments under the selected language version.

Do not infer that the directive deploys a library or alters contract storage. It describes how source code can use functions; the contract’s actual data layout is governed by Solidity’s storage-layout rules, which can depend on compiler version, inheritance, and other implementation details. [source](<https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html>)

## Read the directive’s syntax

A common form is `using LibraryName for TypeName;`. Read it as: make eligible functions from `LibraryName` available in method-style form for values of `TypeName`, where the compiler permits that use. The library identifies the function set; the type identifies the receiver to which the directive applies.

Here is a minimal illustrative pattern:

```solidity
library NumberOps {
    function doubled(uint256 value) internal pure returns (uint256) {
        return value * 2;
    }
}

contract Example {
    using NumberOps for uint256;

    function example(uint256 value) external pure returns (uint256) {
        return value.doubled();
    }
}
```

This snippet illustrates the intended reading, not a compiler-verified recipe for every Solidity release. Its syntax and acceptance should be checked with the exact compiler version and settings chosen for a project. A source-file version pragma constrains which compiler versions are acceptable; it does not itself select or install a compiler. Pinning an exact version can prevent automatic compilation with a different release that may introduce breaking behavior. [source](<https://docs.soliditylang.org/en/latest/layout-of-source-files.html>) [source](<https://docs.soliditylang.org/_/downloads/en/latest/pdf/>)

Some forms use `*` in place of a specific type to express broader applicability. Do not assume that wildcard form, its permitted functions, or its interaction with other declarations is identical across compiler versions. Confirm the supported form and resolution rules in the documentation for the compiler being used.

## Scope: contract, file, and global use

Where a directive is declared matters. A declaration inside a contract is scoped to that contract’s source context under the relevant Solidity rules. A global directive is intended to make the specified attachment available more broadly, but “global” is not a substitute for checking the compiler’s exact rules for declaration placement, imports, and visibility.

When a function appears unavailable, trace the declaration before changing the call. Check whether the directive is in scope at the call site, whether the relevant library is visible through the source’s imports, and whether the compiler version supports the form and placement. In particular, do not assume that importing a file, declaring a directive, and making a function callable have the same scope effect in every version.

Global availability also does not mean every function in the library can be called on every value. The receiver still needs to match the directive’s target under the applicable language rules, and the function must be eligible for the call. A broader directive changes where the attachment can be used; it does not erase type or function constraints.

## Check type matching and compiler behavior

First compare the receiver’s actual type with the target type in the directive. If the two differ, determine whether Solidity permits the relevant conversion for that specific call. Do not treat a visually similar type as a match without checking the compiler’s rules.

Next inspect the library function’s declaration. Confirm that it accepts the intended receiver in the expected position, that its visibility permits the call from the use site, and that the remaining arguments and return type fit the expression. Method-style notation can make the receiver argument less obvious, so compare the expression with the function’s declared parameters rather than relying on the method-like spelling alone.

If the compiler rejects a call, reduce it to a minimal example containing the library, directive, target type, function, and call site. Compile that example with the project’s pinned compiler and settings. This helps distinguish a syntax error from a scope, type-matching, visibility, or argument issue. Solidity compiler outputs can include bytecode, ABI data, metadata, storage layouts, warnings, and errors, depending on the selected version and configuration.

For application code that calls a contract, the ABI must match the deployed contract interface and network address. That is a separate integration check: understanding a source-level `using` directive does not establish that an application’s interface data matches a deployed contract. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

## Use directives carefully in contract code

Prefer a declaration whose scope is easy for a reviewer to trace. A narrow declaration can make it clearer which type receives the attached functions and where the shorthand is intended to be available. If using a global directive, document the intended reach and verify that imports and compiler rules produce that reach in the actual build.

Finally, treat method-style syntax as syntax, not as a safety signal. Read the function implementation and follow its inputs, state effects, and any calls it makes. Composable contracts can call or reuse independent on-chain components through public interfaces, but each dependency adds behavior, upgrade, permission, availability, and economic assumptions to the caller’s system. [source](<https://ethereum.org/developers/docs/smart-contracts/composability/>)

Before relying on the pattern, record the compiler version and settings, compile a minimal example, and check the corresponding language documentation. A version pin supports reproducibility, but it does not establish that the code is correct or secure. The directive explains how a function can be expressed as an operation on a type; it cannot replace review of what that function actually does.

## Sources and references

- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Layout of a Solidity Source File](https://docs.soliditylang.org/en/latest/layout-of-source-files.html) — Solidity Documentation; retrieved 2026-10-19.
