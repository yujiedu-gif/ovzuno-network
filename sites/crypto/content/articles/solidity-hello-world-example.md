---
title: "Solidity hello world example: a minimal contract explained"
description: "See a solidity hello world example with a minimal greeting contract, annotated Solidity syntax, and a clear explanation of compilation and execution."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "solidity hello world example"
owned_question: "What does a minimal Solidity “Hello, world” contract look like, and how do its source code, compilation, and execution fit together?"
risk_level: "medium"
---

A minimal Solidity “Hello, world” example can store a greeting and return it through a getter. The code below is illustrative: it shows how a contract’s source describes state and functions, but it does not deploy or run the contract by itself.

## Solidity hello world example: the smallest useful contract

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Greeting {
    string public greeting;

    constructor() {
        greeting = "Hello, world!";
    }

    function setGreeting(string memory newGreeting) public {
        greeting = newGreeting;
    }
}
```

This example declares a contract named `Greeting`, initializes a stored greeting when the contract is created, and allows a caller to assign a different greeting. The `public` state variable also provides a getter, so a separate getter function is not needed here.

The version pragma, `^0.8.20`, states a range of compiler versions the source accepts; it does not install or select a compiler. Solidity source files should declare a compiler-version pragma, and an exact compiler pin can prevent automatic compilation with a different version that may introduce breaking behavior. Before adapting the example, check the compiler version actually used and its documentation.

## What each part of the contract means

`contract Greeting` begins a contract declaration. A smart contract is code and data deployed through signed transactions on a blockchain network; in Ethereum, the contract’s code and state reside at a specific blockchain address. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/>)

`string public greeting;` declares a state variable. A state variable is data associated with the deployed contract, rather than a temporary value that exists only while a function is running. Here, `string` holds text, and `public` makes the variable available through a generated getter interface.

The `constructor()` block runs as part of creating the contract and sets the initial greeting to `"Hello, world!"`. The assignment uses `=` to store that text in `greeting`.

`setGreeting` is a function that accepts `newGreeting` as a text value and assigns it to the stored variable. `memory` marks the function’s text parameter as temporary input for that call. Because the function changes contract state, invoking it on a deployed contract requires an execution path that can change that state; this example does not specify that path.

The `public` state variable supplies the read interface. Calling that getter returns the current stored text as a result. A returned value is what the function gives back to its caller; it is not a second stored copy of the greeting.

## From Solidity source to contract behavior

Solidity source is the human-readable program. Compilation transforms source into outputs that can include EVM bytecode and ABI data. The ABI, or application binary interface, describes how applications encode function calls and decode results, errors, and events when interacting with EVM contracts.

Compilation is not deployment: producing bytecode does not by itself create a contract at a blockchain address. In an Ethereum-compatible deployment model, a deployment transaction carries compiled bytecode and constructor data; after successful inclusion, it creates a contract at a new address. This article does not provide deployment instructions.

Execution is a later step. A deployed smart contract is invoked through transaction requests, and its programmed behavior depends on the code and inputs. A state-changing function such as `setGreeting` is not executed merely because the source was compiled; execution requires a transaction or another supported trigger and enough gas. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

For an application to interact correctly with a contract, it needs an ABI that matches the deployed interface and the relevant network address. An ABI mismatch or wrong address can make an otherwise valid source example unsuitable for the interaction being attempted.

## Limits and safety checks before adapting the example

This short example illustrates a stored value and a function that changes it. It does not demonstrate access control, upgradeability, or production security, and it should not be treated as audited or tested code. Smart-contract security review involves a structured process; a verification framework can help organize design, building, and testing, but a framework is not proof that any particular contract is safe. [source](<https://owasp.org/projects/smart-contract-security-verification-standard>)

Before adapting the example, confirm the intended compiler version, inspect the resulting compiler warnings and outputs, and make sure any application interface corresponds to the deployed contract. Keep the distinction clear: source expresses intended behavior, compilation produces artifacts, and a compatible runtime processes interactions with a deployed contract. A greeting contract is a learning example, not a complete application or production template.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
