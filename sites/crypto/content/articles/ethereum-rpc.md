---
title: "Ethereum RPC: What It Is and How It Connects Applications to Ethereum"
description: "Learn what ethereum rpc means, how JSON-RPC connects applications with Ethereum nodes, and what an RPC interface does—and does not—provide."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: ["Ethereum JSON-RPC", "RPC endpoint", "Ethereum node"]
author: "editorial_team"
primary_keyword: "ethereum rpc"
owned_question: "What is Ethereum RPC, how do JSON-RPC requests let applications communicate with Ethereum nodes, and what does that connection provide?"
risk_level: "medium"
---

Ethereum RPC (remote procedure call) is a communication interface that lets an application send requests to an Ethereum node and receive responses. Ethereum commonly uses JSON-RPC, a structured request-and-response format. The interface provides access to node methods; it is not the Ethereum network itself, and its available capabilities depend on the node and endpoint configuration.

## What Ethereum RPC means

A remote procedure call is a way for one software component to ask another to perform a defined operation or return information. In Ethereum, JSON-RPC provides a common format for making those requests to a node. An application can ask for data or, where a method supports it, request an action such as submitting a previously signed transaction.

The term “RPC” can refer to the interface or communication method, while an “RPC endpoint” is the connection point through which an application sends requests. Neither term identifies a cryptocurrency asset or describes the whole network. Ethereum’s broader application stack can include nodes and smart contracts alongside wallets, client libraries, front ends, indexing, storage, and other off-chain services; RPC is one communication path among these components. ([source](<https://ethereum.org/developers/docs/ethereum-stack/>); [source](<https://ethereum.org/developers/docs/apis/json-rpc/>))

## How an Ethereum JSON-RPC request works

At a high level, an application sends a structured request naming a method and supplying any required parameters. The node processes the request if that method is supported and available under its configuration, then returns a result or an error. The application interprets that response and decides what to do next. This is a request-response interaction between software components, not a direct interaction with every participant in the network.

Ethereum node RPC methods can query blocks and state, perform read-only calls, estimate gas, filter logs, and submit a previously signed raw transaction. These are different kinds of requests: some retrieve or calculate information, while submission asks the node to handle transaction data. Availability and behavior depend on the node and endpoint configuration, so the general interface does not imply that every endpoint supports every method. ([source](<https://ethereum.org/developers/docs/apis/json-rpc/>))

The distinction between a read-only call and transaction submission matters. A query can return information or an execution result without itself submitting a state-changing transaction. Submitting a signed transaction, by contrast, asks the node to pass it onward for network handling. The RPC response describes the outcome of that particular request; it should not be treated as a guarantee that the requested transaction will be included or reach finality. ([source](<https://ethereum.org/developers/docs/apis/json-rpc/>))

## What an RPC endpoint can expose

Depending on its supported methods, an endpoint can provide access to blockchain and account state, transaction-related information, logs, or calculations such as a gas estimate. It may also accept a previously signed raw transaction for submission. The precise set of methods available is determined by the node software and the configuration of the endpoint, rather than by the phrase “Ethereum RPC” alone. ([source](<https://ethereum.org/developers/docs/apis/json-rpc/>))

An endpoint’s response should be understood as information returned by that node through that interface. The RPC interaction itself does not establish that the application has independently verified the response against Ethereum’s rules. Nor does the interface tell a reader what access the endpoint operator provides beyond the methods and data made available through that connection.

## RPC, Ethereum nodes, and applications

An application is the software making a request. The node is the software processing it. RPC describes the interface between them. These roles are related but not interchangeable: a wallet or other application can use an RPC interface without itself being a node, and an endpoint is not the network as a whole. Ethereum applications can rely on multiple components—such as wallets, node access, contracts, and off-chain services—rather than one connection providing every function. ([source](<https://ethereum.org/developers/docs/ethereum-stack/>))

This division also helps describe responsibility. The application determines which request to make and how to use the response. The node handles supported methods according to its software and configuration. A wallet may separately manage keys and signing; an Ethereum provider interface, for example, can let an application access Ethereum through a client while the wallet manages keys and signing. The RPC concept alone does not specify a wallet’s design or the endpoint’s operational arrangements. ([source](<https://eips.ethereum.org/EIPS/eip-1193>))

## Limits and operational considerations

“RPC” does not by itself promise a particular service’s availability, supported methods, fees, rate limits, data retention, or security properties. Those details concern a specific node, endpoint, operator, and configuration; they must be checked for the connection in question. This definition does not assess any provider or endpoint, recommend a particular setup, or establish jurisdictional, compliance, or tax conclusions.

The practical summary is simple: Ethereum JSON-RPC gives applications a structured way to request information or supported actions from nodes. What an application can do through a particular connection depends on the methods exposed there, and the interface should not be confused with the node, the broader Ethereum network, or the application using it. ([source](<https://ethereum.org/developers/docs/apis/json-rpc/>); [source](<https://ethereum.org/developers/docs/ethereum-stack/>))

## Sources and references

- [JSON-RPC API](https://ethereum.org/developers/docs/apis/json-rpc/) — ethereum.org; retrieved 2026-10-18.
- [Introduction to the Ethereum stack](https://ethereum.org/developers/docs/ethereum-stack/) — ethereum.org; retrieved 2026-10-19.
- [EIP-1193: Ethereum Provider JavaScript API](https://eips.ethereum.org/EIPS/eip-1193) — Ethereum Improvement Proposals; retrieved 2026-10-19.
