---
title: "Solidity interface inheritance: how inherited declarations work"
description: "Learn how solidity interface inheritance combines interface declarations, what implementing contracts must provide, and how to verify behavior for a Solidity version"
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity interface inheritance"
owned_question: "How does interface inheritance work in Solidity, and what must a contract do when it implements an inherited interface?"
risk_level: "low"
---

Solidity interface inheritance lets a derived interface extend declarations from one or more parent interfaces. A contract that implements the derived interface must provide implementations for the applicable inherited function requirements. Developers and reviewers should check the exact rules against the Solidity compiler version used by the project rather than assuming every version treats a hierarchy identically.

## What interface inheritance means in Solidity

An interface is a declaration of a contract-facing surface: it describes functions and other interface members that callers or implementing contracts can refer to. Inheritance lets one interface name another as a parent. The derived interface then carries the parent’s declared surface along with any additional declarations it introduces. Inheritance composes declarations; it does not, by itself, give an interface ordinary function bodies that an implementing contract can use as implementations.

This distinction matters when reading a hierarchy. If `IChild` extends `IParent`, the implementing contract must consider declarations from both interfaces, not only the functions written directly inside `IChild`. The derived interface organizes those requirements under a more specific interface name; it does not make parent declarations disappear.

A function declaration describes an expected callable shape, but it does not establish the logic that will run. The implementing contract supplies that logic. The exact syntax and compatibility rules should be checked for the compiler version selected by the project; avoid treating examples from an unspecified release as authoritative for a different one.

An interface also has an integration role. The Solidity ABI defines how applications encode function selectors and arguments and decode return values, errors, and events between applications and EVM contracts. That means an application needs an ABI matching the deployed contract interface and network address. This integration check is related to inheritance, but it does not prove that the implementing contract’s source declarations satisfy the inherited requirements.

## How inherited function declarations reach an implementing contract

The following is a minimal illustrative example of a parent interface, a derived interface, and a contract that implements the derived interface. It is not a claim that the example was compiled or tested. Check the syntax and compatibility rules against the project’s actual compiler version before using a similar pattern.

```solidity
pragma solidity ^0.8.0;

interface IReader {
    function readValue() external view returns (uint256);
}

interface IExtendedReader is IReader {
    function isReady() external view returns (bool);
}

contract Reader is IExtendedReader {
    function readValue() external pure returns (uint256) {
        return 1;
    }

    function isReady() external pure returns (bool) {
        return true;
    }
}
```

Here, `IExtendedReader` extends `IReader` and adds another function declaration. `Reader` names the derived interface as the interface it implements and provides function bodies for the two functions in this example. The returned values are merely illustrative; inheritance does not require these particular results or dictate the internal behavior of either function.

When reviewing an implementation, compare the contract’s functions with the applicable declarations across the entire hierarchy. Check names, parameter types and order, visibility, mutability, and return types under the selected compiler’s rules. Similar names or apparent intent are not enough to establish that two declarations are compatible. Likewise, a body in the implementing contract is where behavior is supplied; the interface declaration itself is not that behavior.

This process is a source-level check. If an application also calls the deployed contract, separately verify that the application uses an ABI matching the deployed interface and the correct network address. A mismatch between application configuration and the deployed interface is a distinct integration problem; it should not be confused with whether the source contract satisfies inherited declarations.

## Solidity interface inheritance: common design and review checks

A practical review starts with the hierarchy and then follows the requirements into the implementing contract:

1. **List the parent interfaces.** Read each parent named in an inheritance clause and identify its declared functions. Then inspect the derived interface for additional declarations. This establishes the surface the implementing contract needs to address.
2. **Trace inherited requirements.** For each declaration in a parent, check where the implementing contract provides its corresponding function. Do the same for declarations added by the derived interface. Do not review only the text immediately inside the derived interface.
3. **Compare declarations carefully.** Inspect function name, parameter types and order, visibility, mutability, and return types. Confirm compatibility using language rules for the exact compiler version rather than relying on visual similarity.
4. **Investigate repeated or potentially conflicting declarations.** If multiple parents declare a function with the same name, or a derived interface redeclares a parent function, check how the selected compiler handles the specific declarations. Do not assume every repeated declaration is automatically accepted, automatically rejected, or resolved the same way across versions. The available evidence here does not establish universal duplicate-declaration or conflict-resolution rules.
5. **Check the complete implementation surface.** Review the implementing contract against both inherited declarations and declarations introduced by the derived interface. Confirm that the contract’s declaration of implementation corresponds to the interface you reviewed.
6. **Keep ABI and deployment checks distinct.** For application integration, confirm that the ABI corresponds to the deployed interface and network address. This verifies an application-facing match, not the correctness of the contract’s behavior or the compiler’s treatment of a disputed declaration.

Interfaces can also serve as public boundaries between contracts. Solidity contract composition allows contracts to call or reuse independent on-chain components through public interfaces. Each dependency adds behavior, upgrade, permission, availability, and economic assumptions to the caller’s system. That is a separate design-review concern; it does not change the basic inheritance question of which declarations the implementing contract must satisfy.

## Verify behavior with compiler documentation and a minimal test

Treat compiler verification as a project-specific step. A Solidity source-file pragma constrains which compiler versions are acceptable; it does not select the compiler itself. The example uses `^0.8.0` as a visibly stated illustrative constraint, not as evidence that a particular compiler release was used to compile it. For a project, record the compiler version actually configured and consult the Solidity documentation that matches that version.

A focused verification workflow is:

- **Record the compiler version and build configuration.** Confirm which compiler the project invokes rather than inferring it from the source pragma alone.
- **Read version-matched documentation.** Look up the rules relevant to interface declarations, inheritance, implementation, and any duplicate or conflicting declarations under that compiler version.
- **Reduce the hierarchy to a small example.** Include the parent interface, derived interface, and implementing contract. Keep the example focused so that diagnostics can be associated with the inheritance declarations being examined.
- **Compile using the project’s configured compiler.** Inspect the compiler’s diagnostics for declaration or implementation mismatches. This article does not report a compilation or test result, and the example above is illustrative rather than verified output.
- **Resolve diagnostics against the exact declarations.** Check parameter types, visibility, mutability, return types, and repeated declarations before changing code. Use the matching compiler documentation to explain the result instead of generalizing from another version.
- **Check integration separately when relevant.** If an application calls the deployed contract, confirm that its ABI matches the deployed interface and network address.

The central rule is that interface inheritance brings parent declarations into the derived interface’s surface, and an implementing contract must satisfy the applicable requirements under the selected compiler’s rules. Where a hierarchy contains repeated or potentially incompatible declarations, verification requires the exact source declarations, the project’s compiler configuration, and documentation for that version.

## Sources and references

- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
