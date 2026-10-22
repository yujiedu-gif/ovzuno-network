---
title: "Hello World Solidity: A Minimal Contract, Explained"
description: "Learn what a minimal hello world solidity contract contains, how its code is compiled, and how to test basic contract behavior in a controlled environment."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["smart_contract_dapps"]
tags: ["Solidity example contract", "Solidity compiler", "smart contract deployment"]
author: "editorial_team"
primary_keyword: "hello world solidity"
owned_question: "What does a minimal “Hello, world!” Solidity contract contain, and how can a reader compile and interact with it safely in a development environment?"
risk_level: "medium"
---

A minimal “Hello, world!” Solidity contract can store a greeting and expose a way to read it; adding a setter lets a caller request a change. To practice safely, treat the source as code to inspect, compile, and test in a controlled development environment—not as a live contract or a guide to public-network deployment. A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network; source code alone is not a deployed instance. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>)

## What a minimal Hello World Solidity contract demonstrates

This example shows a small contract with a greeting value and a function that updates it:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract HelloWorld {
    string public greeting = "Hello, world!";

    function setGreeting(string memory newGreeting) public {
        greeting = newGreeting;
    }
}
```

The example is intended to make a few pieces of syntax visible: a contract declaration, a stored value, and a function that changes that value. It is not a complete decentralized application, a survey of Solidity, or a recommendation for production code.

The pragma shown is a compiler-version constraint in the source. It does not establish that a particular compiler was selected or used. Before compiling, check which compiler your development environment will use and whether it is compatible with the source. No build or test result is claimed here.

## Read the contract one element at a time

`// SPDX-License-Identifier: MIT` is a license identifier in a Solidity source file. It labels the license associated with the code; it does not affect how the greeting behaves. The exact license should reflect the code’s actual licensing terms.

`pragma solidity ^0.8.20;` states which compiler versions the source accepts according to the pragma’s version expression. The caret is part of that expression. The compiler itself is selected by the tool or build configuration, so the pragma is not an installation command and does not by itself document every detail needed for reproducible builds.

`contract HelloWorld { ... }` declares a contract and encloses its contents. In Ethereum’s model, a deployed smart contract contains code and data at a specific blockchain address. A declaration in a local source file is not itself an instance at that address. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

`string public greeting = "Hello, world!";` declares a string variable and gives it an initial value. The variable represents contract state: the data associated with a deployed instance. `public` makes the variable publicly accessible through the contract interface. It describes visibility, not safety or a restriction on who may read the value.

`function setGreeting(string memory newGreeting) public { ... }` declares a function with one string argument. In this example, `newGreeting` is the input name, and `memory` marks the argument’s temporary data location while the function executes. The assignment `greeting = newGreeting;` requests that the stored greeting be changed to the supplied string. The `public` visibility allows the function to be called through the contract interface; it does not limit callers to a particular person.

The braces show the function and contract boundaries. Reading the example in order, the initial value is `

## Sources and references

- [OWASP Smart Contract Security Verification Standard](https://owasp.org/projects/smart-contract-security-verification-standard) — OWASP Foundation; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
