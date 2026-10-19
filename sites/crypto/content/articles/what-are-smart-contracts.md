---
title: "What Are Smart Contracts? How Blockchain Programs Execute"
description: "Learn how smart contracts store code and state, receive transactions, execute deterministically, consume gas, use oracles, and create onchain results."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["smart-contracts-and-dapps"]
tags: ["smart contract", "blockchain program", "smart contract execution", "smart contract state"]
author: "editorial_team"
primary_keyword: "smart contracts"
owned_question: "What is a smart contract, and how is its code executed and state recorded?"
risk_level: "medium"
---

Smart contracts are programs that a blockchain network stores and executes. The name can be misleading: a smart contract is not necessarily a legal contract, and it is not intelligent. It is code plus persistent data, commonly called state, that follows the rules of a particular blockchain.

NIST defines a smart contract as a collection of code and data deployed through cryptographically signed transactions. Network nodes execute that code, derive the same result under the network's rules, and record the result on the blockchain. This shared execution model lets multiple users rely on one program without asking a single application server to maintain the authoritative state.

## What a smart contract is

A conventional web application usually runs business logic on servers controlled by its operator. Its database records account balances, permissions, or other application state. A smart contract moves some of that logic and state into a blockchain execution environment.

On Ethereum, the official developer documentation describes a smart contract as functions and state located at a specific blockchain address. The functions define operations that callers can request. The state stores persistent values such as balances, ownership records, configuration, or votes. A transaction sent to the address can select a function and provide its inputs.

The term *contract* refers to rules expressed in code. Whether those rules create a legally enforceable agreement is a separate question governed by facts, documentation, parties, and applicable law. A token program, game component, or automated market maker can be a smart contract even when it is not intended to be a legal contract.

## How a smart contract is deployed

Developers normally write source code in a language supported by the target network and compile it into the instructions understood by that network's virtual machine. Deployment then submits those instructions in a blockchain transaction. If the transaction succeeds, the network records the program at an address and initializes its state.

Deployment does not prove that the source code is correct or that users can understand it. Published source-code verification can help observers compare human-readable code with deployed bytecode, but verification is not the same as a security audit. It also does not validate the economic assumptions around the program.

The deployment transaction matters because it establishes the code, initial settings, and often the party or mechanism with administrative authority. Operators should record which network and address are authoritative. The same-looking program can exist at different addresses, on different networks, with different state and control settings.

## How smart contract execution works

A state-changing interaction usually begins when an account signs and submits a transaction. The transaction names the destination contract and carries encoded information identifying a function and its arguments. It may also transfer the network's native asset.

Nodes validate the transaction under network rules and execute the requested instructions in the blockchain's execution environment. Determinism is essential: given the same valid starting state and inputs, participating nodes must derive the same result. NIST includes this shared-result requirement in its smart-contract definition.

If execution succeeds, the resulting state changes and relevant transaction data can be included in the blockchain. If a required condition fails, the execution can revert, meaning its intended state changes are not applied. Network fees may still be charged because nodes performed work before the failure. Exact failure, fee, and finality rules vary by blockchain.

A smart contract does not wake itself up or browse the internet. Something must submit a transaction or call, and the network can only evaluate information available inside its execution context.

## Code, state, and transactions

Separating three elements makes smart contracts easier to understand.

- **Code** defines the available functions and conditions.
- **State** is persistent data maintained under that code and the network's storage rules.
- **Transactions** request state-changing execution and carry a signed instruction from an account.

A website or mobile application can make these components feel like an ordinary app, but the interface is not the contract. A frontend can display incorrect information, hide functions, or direct a user to the wrong address. Wallets and operators therefore need to distinguish interface data from the transaction that will actually be signed.

Contracts may emit logs or events that external services index for user interfaces and monitoring. Those events can help describe execution, but the authoritative meaning of a result depends on the contract code, resulting state, and network rules, not on a label shown by one interface.

## Why execution costs resources

Blockchain computation and storage consume limited network resources. Ethereum measures execution with gas. Deploying code, running functions, and changing persistent storage consume gas according to the instructions performed. A transaction specifies a gas limit, and its sender pays according to the network's current fee mechanism.

Gas does more than price a service. It bounds computation so that a program cannot run forever and consume unlimited node resources. A call that exceeds its limit fails. Other smart-contract networks use different fee units and resource controls, so Ethereum gas values should not be treated as universal.

This resource model influences application design. Repeated storage writes, loops over growing data, and calls into other contracts can raise execution costs or make a function unusable under realistic limits.

## How smart contracts use offchain information

A blockchain can agree on data that its nodes can verify under shared rules. It cannot directly know whether a shipment arrived, an exchange rate is accurate, or a sensor reading is truthful. Ethereum's documentation identifies this as a core limitation: smart contracts cannot fetch real-world information by themselves.

An oracle system brings external data into a form a contract can read. That extends what the program can do, but it also adds dependencies. The result can be affected by the source data, update timing, aggregation method, signer set, market coverage, and failure handling. Calling information *onchain* after an oracle publishes it does not prove the original observation was true.

Operators should document what data a contract depends on, how stale values are handled, and what happens when an oracle stops updating or reports an outlier.

## Immutability, upgrades, and administration

Deployed code is often described as immutable. That can be true for the code stored at one address, but it does not mean every application is permanently fixed. A system can route calls through a proxy to replaceable logic, move users to a new contract, or expose administrator functions that change parameters, pause activity, or grant roles.

Upgradeability can make bug fixes possible, yet it introduces control and governance risk. Readers should ask which parts are fixed, which can change, who can authorize changes, whether a delay applies, and how those powers are disclosed. The relevant unit of analysis is the complete system, not a single bytecode address in isolation.

## What smart contracts do not guarantee

Deterministic execution guarantees that the network follows accepted code under its rules. It does not guarantee that the code expresses the intended policy, is free from vulnerabilities, or produces a fair economic outcome.

A smart contract also does not guarantee that offchain inputs are true, that a user interface is honest, that administrators will use their powers responsibly, or that a court will treat the code as an enforceable agreement. Security reviews, source verification, access-control analysis, oracle assessment, monitoring, and legal documentation address different parts of that problem.

The useful definition is therefore narrow: a smart contract is blockchain-resident code and state executed under shared network rules. Its reliability depends on more than execution alone, including its design, inputs, administrative controls, surrounding interfaces, and the network on which it runs.

## Sources and references

- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-18.
