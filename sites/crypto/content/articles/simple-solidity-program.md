---
title: "Simple Solidity Program: A Minimal Contract Explained"
description: "See what a simple solidity program contains, how its basic contract elements fit together, and what a minimal example does not demonstrate."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["Solidity example", "smart contract program"]
author: "editorial_team"
primary_keyword: "simple solidity program"
owned_question: "What does a minimal Solidity program contain, and how does its code define a basic smart-contract action?"
risk_level: "medium"
---

A minimal Solidity program declares a contract, stores a value in its state, and defines a function that describes an action on that value. In the example below, the function is intended to increase a stored counter by one. This is an illustrative code sample, not a claim that it has been compiled, tested, or deployed.

## What makes a Solidity program a smart contract?

A smart contract is code and data deployed through cryptographically signed transactions on a blockchain network. On Ethereum, a contract’s code and data are associated with a specific blockchain address. The deployed program can be invoked through transaction requests, and its behavior follows its code and the inputs it receives. Solidity is one language used to write such contracts for Ethereum’s execution environment. [source](<https://csrc.nist.gov/glossary/term/Smart_contract>) [source](<https://ethereum.org/developers/docs/smart-contracts/>) [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

It helps to distinguish the source text from the running contract. Solidity source is the program a developer writes. The deployed contract is code and data represented in blockchain state. A source file can describe what the contract is intended to do, but reading it does not establish that it has been compiled, deployed, or evaluated in a particular environment.

The small example here focuses on recognizing basic syntax and tracing one state-changing action. It is not a complete application or a guide to making a contract available on a network.

## Simple Solidity program: a minimal annotated example

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint256 public count;

    function increment() public {
        count = count + 1;
    }
}
```

The snippet contains a source-file comment, a compiler-version pragma, a contract declaration, a state variable, and a function. Each line contributes a different piece of the description. The source-file comment and pragma are not instructions that increment the counter; the function body expresses that action.

The SPDX line is a license identifier comment. The identifier shown is an example, not a recommendation or a statement about rights in any particular project. Solidity source-file guidance includes an SPDX license identifier and compiler-version pragma; the appropriate license is a separate project decision.

The line `pragma solidity ^0.8.20;` constrains the compiler versions the source is intended to accept. It does not select or identify the compiler actually used. The exact compiler and build configuration matter when assessing a program, so the version range in an example should not be mistaken for proof of a specific compilation.

`contract Counter { ... }` declares a Solidity contract named `Counter`; the braces enclose its members. A Solidity contract consists of code, including functions, and data representing its state. Here the state data is declared inside the contract, and the function is part of its code.

The declaration `uint256 public count;` gives the variable the name `count` and the type `uint256`, an unsigned integer type. The `public` label specifies visibility in the source. This example uses one variable so the state and function are easy to follow; it does not demonstrate more complex types or access patterns.

The line `function increment() public` declares a function named `increment`. Its parentheses are empty, so the declaration has no input parameters. The `public` label specifies the function’s visibility. The braces after the declaration contain the statements that define the action.

Inside those braces, `count = count + 1;` reads the current value of `count`, adds one, and assigns the result back to that variable. This is the central behavior the example is meant to show: a function can describe a change to a contract’s state. It is not a complete account of how a network receives, validates, or executes a request to invoke the function.

## Trace the state variable and function

A state variable is data belonging to the contract’s state rather than a temporary name used only inside this function. Ethereum contracts contain code in functions and data in state at a specific blockchain address. In this sample, `count` is the state value that the function reads and updates. [source](<https://ethereum.org/developers/docs/smart-contracts/>)

A simple way to read the function is to follow the assignment from right to left conceptually: obtain the existing `count`, add one, then store the resulting value back in `count`. If the function is invoked successfully, the code expresses that intended update. The snippet does not specify a starting value, a maximum count, or any application rules for interpreting the value.

Function declarations can include a name, parameters, and a visibility label, among other Solidity features. This one has a name, no parameters, and the `public` visibility label. It does not include a mutability label, so it should not be used to infer how read-only functions or functions that do not access state are declared. Those are separate language concepts.

The distinction between reading and changing state matters when interpreting code. The assignment in `increment` is written to update the stored value, rather than only calculate a temporary result. At the network level, an Ethereum smart contract is invoked through transaction requests, and the deployed contract’s behavior depends on the program and its inputs. The code sample alone does not describe the full transaction lifecycle or application-level handling. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

## What the example leaves out

This example does not cover compiling source code, deploying a contract, choosing a network, or submitting a transaction. Solidity compilation and deployment involve steps beyond writing the source text, and this article does not claim that those steps were performed for the snippet.

A short program also does not establish correctness, security, or suitability for an application. Solidity documentation notes that using the language does not by itself guarantee correctness or security; software, compiler, and platform bugs remain possible. Development practices such as review and testing are recommended in that documentation, but this article does not claim to have conducted them.

For a real project, check the Solidity documentation that corresponds to the compiler version and configuration being considered. The pragma is a source constraint, not evidence of the build that produced any deployed code. The example’s purpose remains limited: it illustrates one variable and one function, not a full implementation or readiness for real assets.

## Next concepts to learn

After understanding the basic structure, study Solidity types, function visibility, function mutability, and events as separate topics. Solidity is statically typed and provides multiple kinds of types; the syntax and behavior of a specific feature should be checked against the chosen compiler documentation.

It is also useful to distinguish a contract snippet from a complete decentralized application, often shortened to dApp. An Ethereum application stack can include smart contracts and blockchain nodes along with client libraries, wallets, front-end interfaces, data indexing, storage, and other off-chain services. The counter example covers only a tiny piece of that broader stack. [source](<https://ethereum.org/developers/docs/ethereum-stack/>)

Treat the sample as a reading exercise: identify the contract, locate its state, and follow the function’s assignment. It is not a token implementation, deployment guide, complete dApp, or security review. These boundaries let the example teach basic Solidity structure without implying more than its few lines show.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to the Ethereum stack](https://ethereum.org/developers/docs/ethereum-stack/) — ethereum.org; retrieved 2026-10-19.
