---
title: "Using library solidity: What library functions mean in smart contracts"
description: "Learn what using library solidity means, how library functions are called or linked, and what compiler and deployment details developers should verify."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["solidity use library"]
author: "editorial_team"
primary_keyword: "using library solidity"
owned_question: "What does using a library in Solidity mean, and how does a contract call or incorporate library functions?"
risk_level: "medium"
---

For Solidity developers, using a library means making reusable library code available to a contract through Solidity’s library mechanisms. The key distinction is whether the compiler incorporates a function’s code into the caller or the application makes a call to a separately deployed library. The word “using” can also refer specifically to the `using` directive, which associates library functions with a type. Check the selected compiler’s behavior and the project’s build configuration before deciding which invocation pattern applies.

## What a Solidity library is

A Solidity library groups functions that contracts can reuse. A library is not the same thing as an ordinary deployed application contract in every respect: depending on how its functions are invoked, its code may be incorporated into a calling contract or reached through an external library call. The source-level declaration alone does not tell a developer which deployment arrangement is required.

Library reuse is one form of smart-contract composition. Contracts can call or reuse independent on-chain components through public interfaces, but each dependency brings additional behavior and assumptions into the caller’s system. That means a library’s function and its integration both matter: the calling contract must rely on the behavior the library actually implements, not merely on the fact that the code is packaged for reuse. ([source](<https://ethereum.org/developers/docs/smart-contracts/composability/>))

The word “library” does not establish that a particular function is available in every call context. The relevant function visibility and compiler rules determine how the function can be used. Because the authorized evidence here does not specify Solidity library syntax or give version-by-version rules, do not assume that a pattern from one project applies unchanged to another.

## How the `using` directive attaches library functions

The `using` directive is a source-level way to associate a library with a type. Conceptually, that association lets a developer write an eligible library function as an operation on a value of the associated type. This attached style can be distinguished from an explicit call that names the library and function.

These forms describe how a call is expressed in source code; they do not, by themselves, settle whether the compiled call requires an independently deployed library. The function’s visibility and compiler behavior still determine the call path. Therefore, an attached call should not be treated as proof that the code is embedded, and an explicit library name should not be treated as proof that a separate deployment is always necessary.

When reviewing a project, identify the library, the type association if the `using` directive is present, the function being called, and its visibility. Then consult documentation for the exact compiler version to determine the syntax and resulting call behavior. This avoids turning an illustrative description of the directive into a universal rule about every Solidity release.

## Internal functions and externally linked library calls

The practical distinction is between reuse during compilation and a call that relies on a separately deployed library. In the former case, library code can be incorporated into the calling contract’s compiled code. In the latter, the call can depend on a deployed library address and on link references being resolved in the build or deployment process. Not every use of a Solidity library requires a separate deployment.

For a project using an external library call, the developer needs to determine how its build and deployment tools represent and resolve library references. If a build artifact indicates unresolved references, the deployment configuration must supply the intended address information before the final deployed code can be relied on. If the selected pattern does not require external linking, a separate library deployment should not be added just because the source contains a library declaration.

An application that interacts with EVM contracts also relies on an ABI, or Application Binary Interface. The Solidity ABI specifies how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. The application must use an ABI that matches the deployed contract interface and network address.

That interface check is related to, but distinct from, library linking. Linking concerns whether the compiled code has the correct library references; ABI matching concerns how an application encodes and interprets contract interactions. A project may need to check both, but one check does not establish the other.

## What to verify before compiling and deploying

Use the following checks to establish which library pattern a project actually uses:

1. **Compiler version and syntax.** Record the compiler version selected for the build and confirm the relevant library syntax and visibility rules in documentation for that version. An exact Solidity version pragma can prevent automatic compilation with a different version that may introduce breaking behavior. A version pin does not, by itself, establish correctness or security.
2. **Call expression and visibility.** Identify whether source code uses an attached library function or explicitly names a library function. Check the function’s visibility and confirm that the selected compiler permits the intended call.
3. **Compiler artifacts.** Inspect the output produced by the actual build rather than inferring the compiled form from source alone. Solidity’s compiler can produce EVM bytecode, ABI data, and other outputs; the selected output fields depend on compiler version and configuration.
4. **Library references.** Determine whether the build leaves external library references that must be linked. If it does, check that the build or deployment process resolves them with the intended deployed library address. If it does not, do not assume that a separate library deployment is required.
5. **Application interface and address.** For application calls, confirm that the ABI corresponds to the deployed interface and that the configured network address is the intended one. ABI compatibility is not a substitute for checking external library links, and link resolution is not a substitute for checking the application interface.
6. **Dependency behavior.** Review what the library does and how the calling contract depends on it. Reusing code does not remove the additional behavior and assumptions introduced by contract composition. ([source](<https://ethereum.org/developers/docs/smart-contracts/composability/>))

These checks are project-specific verification steps, not a guarantee that a library or the caller is correct. The authorized evidence supports the distinction between compiler output and interfaces, but does not provide a universal linking command, a fixed deployment procedure, or version-specific syntax examples. Consult the documentation and tools applicable to the project rather than filling those gaps with assumptions.

## Where this explanation stops

This explanation defines Solidity library reuse and distinguishes attached calls from explicit calls and external linking. It does not provide an array implementation tutorial, and it does not explain delegatecall generally. Those are separate subjects; library reuse should not be taken as a complete account of delegatecall behavior.

The practical answer is that a Solidity library gives contracts a way to reuse functions, while the invocation and deployment requirements depend on the function’s visibility and the compiler’s handling of that call. Check the exact compiler version, inspect the build output for library references, and verify the application ABI and address where applicable. Avoid generalizing from one project’s source or artifacts to every Solidity compiler and deployment setup.

## Sources and references

- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
