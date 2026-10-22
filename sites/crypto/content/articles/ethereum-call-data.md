---
title: "Ethereum call data: what transaction input means"
description: "Learn what ethereum call data is, where it appears in a transaction, how smart contracts use it, and why encoded input is not the same as stored state."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: ["ethereum calldata"]
author: "editorial_team"
primary_keyword: "ethereum call data"
owned_question: "What is Ethereum call data, where does it appear in a transaction, and how is it used when a transaction calls a smart contract?"
risk_level: "medium"
---

Ethereum call data is the byte input supplied to a contract as part of a request to run its code. The contract’s implementation determines how it interprets those bytes; they are not the same as the contract’s persistent state, an attached amount of ETH, or proof that an operation succeeded.

## What Ethereum call data means

Call data, also written *calldata*, is input supplied when a request invokes a smart contract. A smart contract is code and data deployed on a blockchain, and an Ethereum contract has executable functions and persistent state at an on-chain address. Call data is the input presented to that code; it is not, simply by being submitted, a new persistent state record. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)] [[source](<https://csrc.nist.gov/glossary/term/Smart_contract>)]

The input consists of bytes. A contract may treat those bytes as information for an operation, but their meaning depends on the contract’s code and the conventions expected by the interface used to interact with it. The general definition of a smart contract does not establish that every contract uses the same input format, or that arbitrary bytes have a common meaning across contracts. [[source](<https://csrc.nist.gov/glossary/term/Smart_contract>)]

This distinction is useful at the outset: call data describes what was supplied to a contract, while contract state describes data maintained at its address. Code can use supplied input when it runs, but input and state remain different parts of the interaction. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)]

## Where call data appears in an Ethereum transaction

A transaction that requests an operation from a contract can include input for that contract. In that setting, call data is part of the submitted request. It is not a separate receipt or record of the operation’s outcome. Ethereum smart contracts are programs at network addresses that users can invoke by submitting transactions, and their executable functions determine what happens when they are invoked. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)]

Not every transaction should be described as containing meaningful contract-call input. Some transactions may carry no input intended for a contract operation. The presence of a transaction alone therefore does not establish that it contains call data with an interpretable function request. Whether bytes are supplied, and what they mean, depends on the transaction and the target contract’s implementation. [[source](<https://csrc.nist.gov/glossary/term/Smart_contract>)]

## How contracts use call data

When a contract is invoked, its code can use supplied bytes as input while executing a function. The contract’s implementation determines how it interprets that input and how it relates to persistent data. This is why the same general description—“input bytes”—does not, by itself, explain the behavior of every contract call. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)]

The interaction is best understood as distinct parts: supplied input, contract code that may process it, and persistent state maintained at the contract address. A smart contract is code and data deployed on a blockchain, but that definition does not mean every submitted input produces a particular state change. The outcome depends on the contract’s code and execution, not merely on the fact that bytes were provided. [[source](<https://csrc.nist.gov/glossary/term/Smart_contract>)] []

Nor does the input alone establish that the requested operation completed successfully. It identifies what was submitted, not the full result of contract execution. A definition of call data should therefore avoid treating a request as though it were an execution result or a complete description of the state that follows.

## Call data, transaction value, and storage are different

Call data is input. Transaction value, where applicable, is a separate part of a transaction: it refers to an amount of the native asset attached to the request. A contract interaction can be discussed in terms of input without treating that input as an asset amount. Call data and transaction value answer different questions—what bytes were supplied and what value was attached.

Storage is different from both. Persistent contract state is data maintained at the contract’s on-chain address. Call data is supplied as input to code, while storage is part of the contract’s continuing state. A contract may use input when processing an operation that affects its state, but this does not make the submitted input itself the stored result. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)]

These distinctions also prevent overreading a transaction description. Input bytes do not reveal, by themselves, what amount of native currency was attached or what persistent state a contract maintained after execution. Each is a separate element of the interaction, and the contract’s code determines how its input is handled.

## What encoded call data can—and cannot—tell you

Encoded call data may not be self-explanatory. To assign meaning to the bytes, a reader needs context about the target contract and the interface conventions that apply. Without that context, the bytes alone do not establish which operation or arguments they represent. The contract’s code and data define the relevant behavior, so an interpretation should not be generalized from one implementation to another. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)] [[source](<https://csrc.nist.gov/glossary/term/Smart_contract>)]

Even when input has an interpretable meaning, it tells you what was supplied—not, on its own, whether execution succeeded or what state resulted. Contract functions, persistent data, and events are distinct aspects of a contract’s operation; events are information available for applications to process, rather than the supplied input itself. [[source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>)]

In short, call data is transaction input for contract execution. Its interpretation depends on the target contract and applicable interface conventions, while attached value, persistent storage, and execution outcomes remain separate concepts. This definition does not decode a particular payload or establish what any specific transaction did.

## Sources and references

- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
