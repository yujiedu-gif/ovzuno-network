---
title: "Solidity Import Contract: How Source-File Imports Work"
description: "Learn how a Solidity import contract makes declarations from another source file available, which import forms exist, and what to check when resolution fails."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Solidity import statement", "importing contracts in Solidity", "Solidity source units"]
author: "editorial_team"
primary_keyword: "solidity import contract"
owned_question: "How do Solidity import statements make declarations from another source file available to a contract, and what should developers check when using them?"
risk_level: "medium"
---

A Solidity `import` statement tells the compiler to make declarations from another source file available to the importing file. It does not deploy the imported contract, inherit from it, or call it. Choose an import form that makes references clear, then check the source name, compiler inputs, configuration, and version constraints when compilation cannot resolve the dependency.

## What a Solidity import brings into scope

A Solidity source file can contain contracts, interfaces, libraries, and other declarations. An import connects source files during compilation so that the importing file can refer to declarations provided by another file. The import is therefore a source-level dependency: it helps the compiler understand names used in the importing file, rather than causing a contract to run on a blockchain.

This distinction separates three actions that can look related in code but have different meanings. An import makes a declaration available to the source file. Inheritance is expressed separately in a contract declaration. A contract-to-contract interaction requires code that performs a call through the relevant interface or contract reference. Importing a declaration alone does none of the latter two things.

Imports can participate in a larger design in which contracts reuse or call independent on-chain components through public interfaces. That composability adds behavior and assumptions to the caller’s system, including assumptions concerning upgrades, permissions, availability, and economics. The import statement itself does not assess those assumptions; it only establishes a source dependency for compilation.

## Solidity import contract syntax and common forms

Solidity offers import forms that differ in how declarations are named in the importing file. The examples below are illustrative: the source name still has to be resolved by the compiler and the build configuration.

A direct import names the source file without assigning an alias:

```solidity
import "./Token.sol";
```

This form allows the importing source to refer to declarations from that file. Because it does not put the declarations behind a file alias, a project may prefer a more explicit form when the origin of a name would otherwise be unclear.

A namespace-style import assigns an alias to the imported source:

```solidity
import * as TokenModule from "./Token.sol";

contract Sale {
    // A declaration can be referenced using the TokenModule namespace.
}
```

The namespace makes the imported source explicit at the point where its declarations are referenced. It can also distinguish declarations when names would otherwise be easy to confuse. The alias is local to the importing source; it does not rename declarations in the original file.

A selective import lists particular declarations and can assign local aliases:

```solidity
import {Token as SaleToken, TokenConfig} from "./Token.sol";
```

In this example, the importing source refers to the declaration `Token` by the local name `SaleToken`; it can refer to `TokenConfig` by its listed name. Selective imports make the intended dependency and any local naming choice visible in the import statement. They do not modify the declarations in the imported file.

These forms affect how names are introduced and referenced, not whether a contract is deployed or executed. When selecting a form for real source code, check it against the Solidity documentation for the compiler version used by the project. A short syntax example does not establish compatibility with every compiler version or configuration.

## How paths and compiler versions affect imports

An import string is a source-unit name that must be resolved during compilation. Resolution depends on the source names supplied to the compiler and, where configured, rules such as remappings. As a result, a path that appears to be relative to a file on disk may not resolve as expected if the build supplies different source names or applies different configuration.

The useful question is not only “Does this file exist?” but also “What source-unit name did the compiler receive, and how is that name mapped?” A build tool may arrange inputs differently from another toolchain. Relative paths, package prefixes, and remappings should therefore be checked against the actual compilation inputs rather than assumed to follow one universal layout.

Compiler version constraints are a separate part of the check. A Solidity source file should declare an SPDX license identifier and a compiler-version pragma. The pragma constrains which compiler versions are acceptable, but does not itself select the compiler. An exact version pin prevents a file from being compiled automatically with a different compiler version that may introduce breaking behavior. The compiler actually used, along with dependencies and build tools, should be recorded; the pragma alone does not establish the build’s compiler version.

When several source files are imported, compare their version pragmas with the compiler selected for the complete build. If the selected compiler does not satisfy the constraints of the sources, address that compatibility issue separately from path resolution. A compiler-version conflict and a missing source file are different failure categories, even if both prevent compilation.

## Diagnosing unresolved or ambiguous imports

Use a repeatable checklist so a file-location problem does not get confused with a declaration-name problem:

1. **Inspect the import string.** Check spelling and letter casing, and compare the string with the source-unit name supplied to compilation.
2. **Confirm the compiler received the file.** Verify that the imported source is present in the build environment and included among the compilation inputs.
3. **Review path configuration.** Check configured remappings and confirm that the imported source name matches the rules in effect. A package prefix or relative path should not be assumed to mean the same thing in every toolchain.
4. **Check compiler constraints.** Compare the compiler selected for the build with the version pragmas in both importing and imported files. Record the compiler actually used instead of treating the pragma as a selector.
5. **Separate file resolution from name resolution.** If the source file is found but a declaration is unavailable, check that the declaration exists and that the spelling and local name at the import site match.
6. **Clarify overlapping names.** If references are ambiguous or difficult to read, consider a namespace alias or selective imports with local aliases so the intended declaration is explicit.

This sequence is useful because “cannot find source” and “cannot find declaration” point to different inputs. The first calls for checking source-unit names, compiler inputs, and path configuration. The second calls for checking declarations and the names under which the importing file refers to them. Changing a path will not fix a misspelled declaration name, and renaming a local reference will not add a file missing from the compiler inputs.

## Import boundaries: what this syntax does not establish

An import does not establish that the imported code is correct, secure, verified, deployed, or available at a particular address. Nor does importing a contract automatically make the importing contract inherit from it or interact with an on-chain instance. Those are separate questions involving source code, contract structure, and, for runtime behavior, the relevant execution context.

An import also does not settle storage compatibility for upgradeable designs. Proxy-based upgradeable contracts require initializer discipline and compatible storage layout across implementations to avoid takeover or corrupted state. Merely importing an implementation or related declaration does not establish that those requirements are met.

Keep the conclusion bounded: an import connects source declarations for compilation, while inheritance, external interaction, deployment, and security properties require separate mechanisms and review. When an import fails, first identify whether the compiler cannot resolve the source name, cannot satisfy version constraints, or cannot find the declaration being referenced. That diagnosis points to the right next check without treating import syntax as a runtime or security guarantee.

## Sources and references

- [Layout of a Solidity Source File](https://docs.soliditylang.org/en/latest/layout-of-source-files.html) — Solidity Documentation; retrieved 2026-10-19.
- [Solidity Documentation](https://docs.soliditylang.org/_/downloads/en/latest/pdf/) — Solidity; retrieved 2026-10-19.
- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Writing Upgradeable Contracts](https://docs.openzeppelin.com/upgrades-plugins/writing-upgradeable) — OpenZeppelin Documentation; retrieved 2026-10-19.
