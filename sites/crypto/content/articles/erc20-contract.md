---
title: "ERC20 contract: functions, events, and implementation basics"
description: "Understand what an erc20 contract specifies, how its common functions and events support token interactions, and which details depend on implementation."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["ERC-20 standard", "Solidity token contract", "allowance and transfer functions"]
author: "editorial_team"
primary_keyword: "erc20 contract"
owned_question: "What does an ERC-20 contract specify, which functions and events are commonly used to interact with it, and what does the standard leave to individual implementations?"
risk_level: "medium"
---

An ERC-20 contract is a smart contract that exposes a common interface for fungible-token operations, such as querying supply and balances, transferring tokens, and authorizing another address to spend them. The interface describes how applications and contracts communicate; it does not establish the particular token’s value, backing, legal status, or safety. To understand a specific token, distinguish the standard’s interface from the behavior implemented at its deployed contract address.

## What an ERC20 contract represents

ERC-20 is a token interface standard associated with Ethereum. A smart contract is a program deployed on a blockchain and invoked through transaction requests. On Ethereum, a contract contains code in functions and data in state at a specific blockchain address. For a token contract, that code and state implement token-specific behavior, while the ERC-20 interface gives other software a shared way to request common operations.

A standard is not the same thing as a particular contract. The interface lays out a communication convention; the deployed code determines how that contract responds. A contract label or description alone does not establish that every implementation detail matches a reader’s expectations. Compatibility is a matter of the actual interface and deployed implementation, not just a name in a wallet or application.

Applications use an ABI, or Application Binary Interface, to encode and decode communication with an EVM contract. The Solidity ABI specification defines the encoding of function selectors, arguments, return values, errors, and events. The application must use an ABI that matches the deployed contract interface and network address. If either reference is mismatched, the application may encode requests or interpret responses incorrectly.

This explains the boundary of the term “ERC-20 contract”: it refers to a contract whose interface is intended to support ERC-20 token interactions. It is not, by itself, a complete description of issuance rules, additional functions, administrative controls, or off-chain arrangements.

## The ERC-20 functions callers commonly use

The ERC-20 interface groups common operations into queries and state-changing requests. The function names below are commonly used to describe those interactions:

- `totalSupply` queries the total supply reported by the contract.
- `balanceOf` queries the balance associated with an address.
- `transfer` requests a direct transfer from the caller to a recipient.
- `approve` requests authorization for a spender to use a specified amount on the caller’s behalf.
- `allowance` queries the amount authorized for an owner-and-spender pair.
- `transferFrom` requests a transfer from an owner using the caller’s authorization, subject to the contract’s implementation and applicable allowance.

A query such as `totalSupply`, `balanceOf`, or `allowance` asks the contract for information. A `transfer` or `approve` request changes contract state when successfully executed. Ethereum smart contracts are invoked through transaction requests; the transaction’s execution is governed by the deployed code and network rules.

The two common transfer paths differ in who initiates the request. In a direct path, a holder calls `transfer` to request that tokens move to a recipient. In an allowance-based path, the holder first calls `approve` to authorize a spender. That spender can later call `transferFrom` to request a transfer within the authorized amount. Approval and transfer are separate interactions: approving a spender does not itself perform the later transfer.

These descriptions explain the interface roles, not every possible implementation detail. When reading documentation for a particular contract, check how it describes function inputs and outputs, and make sure the application’s ABI corresponds to the deployed contract and network address. Do not infer detailed behavior solely from a familiar function name.

## Events and allowance-based interactions

The ERC-20 interface includes the `Transfer` and `Approval` events. An event is encoded information emitted by a contract for applications to process. In this interface, `Transfer` communicates a token-transfer record, while `Approval` communicates an approval record. These events help software and readers follow relevant interactions, but an event alone does not explain the broader purpose or establish that an action was safe.

An allowance is an authorization amount associated with an owner and a spender. The spender is the address authorized to request a transfer from the owner through `transferFrom`. The `approve` interaction sets an authorization, and `allowance` provides the interface for querying the amount associated with that owner-spender relationship. How an implementation handles a particular request should be checked in its documentation and code rather than assumed from the function name.

When reviewing an approval request, identify the spender and the amount being authorized. Then distinguish the approval from any later transfer: the approval grants a specified permission under the contract’s rules, while `transferFrom` is a separate request to use that permission. An `Approval` event is a record of an approval interaction; it does not independently establish whether the spender is appropriate or what the application intends to do with the authorization.

## What the standard does not settle

The ERC-20 interface defines a common way to interact with a fungible token, including balances, direct transfers, approvals, allowances, and the `Transfer` and `Approval` events. It does not establish issuance policy, backing, market value, compliance, or implementation safety. Those questions require evidence about the specific contract and the relevant arrangements; they cannot be answered just by identifying the interface.

The standard also does not settle every implementation choice. A contract may have behavior or functions beyond the shared interface, but what those additions do depends on the specific code and documentation. Other standards illustrate that token interfaces can be structured differently: ERC-1155, for example, allows one contract to manage multiple token types, including fungible, non-fungible, and semi-fungible configurations. That is a different interface design, not an additional requirement of ERC-20.

Security, recovery, fees, availability, and compliance are also outside what ERC-20 compatibility alone establishes. A claim about one of these properties needs evidence about the specific implementation, service, network, or context. The interface cannot certify that contract code is correct, that a recovery process exists, or that a particular fee or compliance condition applies. This explainer makes no jurisdiction-specific legal or tax conclusions.

## How to inspect an ERC-20 contract responsibly

For a specific contract, begin by identifying the deployed contract address and network to which its documentation refers. Then compare the documented interface with the claimed ERC-20 functions and events. If an application is involved, check that its ABI matches the deployed contract interface and network address; an ABI describes how calls, responses, errors, and events are encoded, not whether the contract is safe.

For an allowance-based interaction, trace the roles in order: identify the owner, the spender, the approved amount, and any later `transferFrom` request. Treat the approval and transfer as distinct operations, and read the implementation’s documentation for relevant behavior. Review additional functions separately because the standard interface does not define their purpose.

Finally, keep the conclusion proportionate to what you inspected. A match with the common interface can describe how software is expected to communicate with the contract; it is not a security audit or evidence of backing, value, recovery, fees, availability, or compliance. Those properties require separate, context-specific support. ERC-20 is best understood as a shared interaction vocabulary, while the contract’s own implementation determines details beyond that vocabulary.

## Sources and references

- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
- [Introduction to smart contracts](https://ethereum.org/developers/docs/smart-contracts/) — ethereum.org; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
