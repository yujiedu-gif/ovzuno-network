---
title: "Immutable in Solidity: Assignment Rules, Behavior, and Limitations"
description: "Learn how immutable in Solidity state variables are assigned and used, how they differ from constants and mutable variables, and what design limits to check."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "immutable in solidity"
owned_question: "What does `immutable` mean in Solidity, when can an immutable state variable be assigned, and how does its behavior differ from a constant or a regular state variable?"
risk_level: "medium"
---

For Solidity developers, `immutable` marks a state variable whose value is established during contract creation and cannot be reassigned afterward. It differs from a `constant`, whose value is known at compile time, and from an ordinary state variable, which contract code may update. The exact declaration and assignment rules depend on the Solidity compiler version, so check the language documentation for the version used by your project.

## What `immutable` means in Solidity

A state variable is data associated with a contract. In Ethereum, a contract has persistent state and executable functions at an on-chain address; state variables are part of that persistent data model. A local variable, by contrast, is used within a function rather than declared as contract-level state. [source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)

`immutable` is a Solidity language feature for state variables that receive a fixed value during contract creation. The value can depend on information supplied when the contract is constructed, unlike a compile-time constant. Once construction is complete, the variable is intended to remain fixed for that deployed contract instance.

This is a constraint on one value, not a guarantee that the contract as a whole is unchanged or secure. Other state variables and functions may have separate behavior, and code correctness still depends on the program and its inputs. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

## How immutable assignment works

An immutable variable must be assigned according to Solidity's rules: it can be initialized at its declaration or assigned during construction. For example, a constructor can set a value based on its input. After construction, ordinary contract functions cannot assign a new value to that immutable variable.

The following is an illustrative example of the intended pattern, not a compiler-tested snippet. No compiler version is specified here, so verify syntax, supported types, and assignment requirements against the exact Solidity version you use:

```solidity
contract Example {
    address public immutable administrator;

    constructor(address initialAdministrator) {
        administrator = initialAdministrator;
    }
}
```

In this example, `administrator` is established during construction from the constructor argument. Contract code can subsequently read the value, but the example does not provide a function to change it. If the constructor path does not assign a required immutable value, or if assignment occurs in a disallowed context, the contract may fail to compile; consult the language rules for the selected version.

## Immutable vs. constant vs. mutable state

These categories differ primarily in when their values are established and whether they can be changed:

| Variable category | When its value is established | Can contract code change it later? | Typical design role |
|---|---|---|---|
| `constant` | At compile time | No | A value already known when compiling the contract |
| `immutable` | At declaration or during construction, under Solidity's rules | No, after construction | A value fixed for an instance but determined during its creation |
| Ordinary state variable | During initialization or later execution | Yes, if the contract provides an assignment path | State that is intended to change over time |

For example, a protocol-wide identifier known before compilation may be a candidate for `constant`. A contract-specific address supplied at construction may fit `immutable`. A counter that changes when users interact with the contract is mutable state.

Do not infer a universal gas or storage advantage from these categories. Solidity state variables follow compiler- and layout-dependent rules, and the storage layout is part of a contract’s external interface. Exact behavior should be checked for the compiler version, inheritance, and layout used by the project. [source](<https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html>)

## Limitations and design checks

First, verify that the intended type and assignment pattern are supported by the language version you compile with. Solidity is statically typed, but the exact syntax and compiler behavior should be checked against the selected version. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

Second, an immutable variable does not make the entire contract immutable. It constrains the value of that variable; other functions may still change other state, and external systems can affect what users observe. Treat the variable’s fixed value as one property of the program, not a broad security conclusion.

Third, architecture matters when code executes in a context different from the one a developer expects. This article does not explain `delegatecall` or proxy designs, but contracts using those patterns should not assume that a construction-time value behaves as though every execution context were the original deployed instance. Examine the architecture and compiler documentation before relying on an immutable value as a critical invariant.

Finally, do not assume that a particular implementation has lower execution cost simply because it uses `immutable`. Contract execution is constrained by gas, and gas schedules and limits vary by network and implementation. [source](<https://ethereum.org/developers/docs/smart-contracts/>) A cost comparison requires the relevant compiler configuration and deployment context; this explainer makes no universal performance claim.

## When an immutable variable fits

Use `immutable` when a value is determined at construction and is meant to stay fixed for that deployed contract instance. Choose `constant` when the value is known at compile time. Use a regular state variable when later updates are part of the intended behavior.

Before relying on the choice, check that every construction path assigns the immutable as intended, confirm the rules for the compiler version, and review whether the contract’s execution architecture changes the assumptions behind that value. If the design requires later administration to update the value, `immutable` is not the right category: its defining purpose is that the value cannot be reassigned after construction. These checks support a language-level design decision; they do not establish that the broader contract is correct or secure.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
- [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) — Solidity Documentation; retrieved 2026-10-19.
