---
title: "Ethereum programming language: what the term means"
description: "Learn what the term ethereum programming language means, how smart-contract languages relate to Ethereum, and why the execution environment is distinct."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "ethereum programming language"
owned_question: "What does “Ethereum programming language” mean, and which languages are used to write smart contracts for Ethereum?"
risk_level: "medium"
---

“Ethereum programming language” is a general phrase for a language used to write smart contracts for Ethereum; it does not name one required language. Solidity and Vyper are examples. The language is where developers express contract logic, while Ethereum is the network and its execution environment is where deployed contract code runs.

## What “Ethereum programming language” refers to

The phrase usually means a programming language used to author smart contracts intended for Ethereum. A smart contract is a program deployed to blockchain state and invoked through transaction requests; on Ethereum, it has code and data at a specific blockchain address. These definitions describe the contract’s role and location, not a single language that every developer must use. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>); [source](<https://ethereum.org/developers/docs/smart-contracts/>))

The phrase also does not mean that Ethereum’s protocol or client software is itself written in the same language as a contract. Protocol rules, client implementations, and application contracts are distinct parts of the broader technical system. In ordinary conversation, “Ethereum programming language” most often concerns the application-contract layer rather than the software that implements the network. ([source](<https://csrc.nist.gov/glossary/term/Smart_contract>))

## How smart-contract languages relate to Ethereum

A developer writes source code in a programming language to describe the contract’s intended behavior. That source is not the same thing as the running contract: Ethereum smart contracts are reusable programs deployed into blockchain state and invoked through transaction requests. Once deployed, the contract’s code and data are associated with its blockchain address. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>); [source](<https://ethereum.org/developers/docs/smart-contracts/>))

This distinction helps clarify the roles involved. A programming language is a way to author instructions; a smart contract is the program deployed to the network; Ethereum supplies the network state and execution context in which that program is invoked. The language does not become the network, and the network is not itself a language. ([source](<https://csrc.nist.gov/glossary/term/Smart_contract>); [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

The Ethereum Virtual Machine (EVM) is commonly discussed as Ethereum’s execution environment for contract code. The evidence available for this definition supports describing the relationship at a high level: source languages are used to author smart contracts, and Ethereum’s deployed contracts are programs invoked through transaction requests. It does not establish technical details about compilation formats or EVM instruction encoding, so those implementation details are outside this explanation. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

## Solidity and Vyper as examples

Solidity and Vyper are examples of languages used to write Ethereum smart contracts. Naming them does not imply that Ethereum requires either one, that they are interchangeable in every project, or that one is universally preferable. The general term describes a role—authoring contract code—rather than a ranking of languages. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

A language is only one part of a contract’s development context. The project’s intended behavior and the surrounding application matter too; the name of a language alone does not describe every feature or operating condition of the deployed contract. The evidence used here supports the broad relationship between Ethereum and smart-contract programs, not a detailed comparison of Solidity and Vyper. ([source](<https://ethereum.org/developers/docs/smart-contracts/>); [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

## What the term does not mean

“Ethereum programming language” does not mean Ethereum itself is a programming language. Ethereum is the network context in which deployed smart-contract programs are invoked. Nor does the phrase mean ETH or any token is “written” in Solidity or Vyper: a contract may manage code and data, while a cryptocurrency or token is a separate concept. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>); [source](<https://ethereum.org/developers/docs/smart-contracts/>))

The phrase also does not specify a token standard, framework, or security guarantee. It identifies a category of languages by their intended use for Ethereum smart contracts. A language label alone cannot establish that a particular contract’s behavior is correct or secure; that depends on the actual program and its deployment context. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

## Choosing a language requires context

A general definition can identify the role of a language, but it cannot determine which one fits a particular project. Intended contract behavior and the people building it are relevant context; the available evidence here does not support a language ranking or a detailed tool-selection recommendation. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

Most importantly, knowing that a contract was authored in a language associated with Ethereum does not establish that the deployed code behaves as intended. The term explains how developers express contract logic, not whether an individual contract is correct, secure, or appropriate for a given use. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

In short, “Ethereum programming language” refers to languages used to write smart contracts for Ethereum, with Solidity and Vyper as examples. Those languages are distinct from Ethereum itself and from the environment in which deployed contract code is invoked.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
