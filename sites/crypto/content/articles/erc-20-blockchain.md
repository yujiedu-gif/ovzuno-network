---
title: "ERC-20 Blockchain: How Ethereum’s Fungible Token Standard Works"
description: "Learn what ERC-20 standardizes for fungible tokens on Ethereum, including balances, transfers, approvals, events, and compatibility limits."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["smart_contracts_dapps"]
tags: ["ERC-20 token standard", "fungible tokens on Ethereum", "ERC-20 interface", "Ethereum token smart contracts"]
author: "editorial_team"
primary_keyword: "erc 20 blockchain"
owned_question: "What is ERC-20, and how does it define fungible tokens on Ethereum?"
risk_level: "medium"
---

# What Is ERC-20? Ethereum’s Fungible Token Standard Explained

## What ERC-20 means on Ethereum

ERC-20 is a common interface for fungible tokens associated with Ethereum application contracts. It defines a set of token-related functions and events that implementations expose. It is an application-layer standard: it does not create a separate blockchain or replace Ethereum’s execution environment. An ERC-20 token is represented and managed through a smart contract, whose state and behavior are specific to that contract.

Ethereum smart contracts have persistent state and executable functions at an on-chain address, and they can emit events for applications to process. In this setting, ERC-20 describes a shared way for applications to ask token contracts about supply and balances, request transfers, and work with approvals and allowances. The standard is not itself the token’s state, nor is it a description of every internal rule in a particular contract.

ETH is Ethereum’s native asset, while ERC-20 refers to a token interface used by application contracts. The ERC-20 interface does not turn ETH into an ERC-20 token by default. This distinction matters because a shared interface for contract-managed tokens should not be confused with the native asset of the blockchain on which those contracts operate.

The standard defines common operations and event types, not a separate token network. Its purpose is to establish a recognizable interface. A contract’s implementation remains important for understanding what happens when an application calls that interface.

## How ERC-20 represents fungible tokens

Fungibility means that units within a token are treated as interchangeable with other units of that same token. ERC-20 organizes its interface around quantities, supply, and account balances. That is different from a model in which each item is individually distinguished: the ERC-20 interface provides shared operations for token amounts rather than an interface centered on the identity of each individual item.

The contract tracks balances and applies its own defined transfer rules. The standard’s common interface lets an application request a balance or transfer through a familiar operation, but it does not independently explain the economic meaning of the units. What a token represents, how it is issued, or what rules govern it cannot be inferred simply from the fact that its contract uses the ERC-20 interface.

Fungibility is also scoped to the token contract and its rules. The interface offers common vocabulary for balances and transfers; it does not mean that tokens from different contracts are interchangeable with one another, or that every contract will produce identical effects for every interaction. Applications need to distinguish a common interface from the behavior and meaning of a specific token.

A token’s technical representation should not be confused with claims about value or rights. The ERC-20 standard does not establish backing, issuance policy, market value, compliance, or implementation safety. Those properties require evidence beyond the interface. The interface describes how a contract exposes token-related operations, not whether a token has any particular economic characteristics.

## The core ERC-20 interface

The ERC-20 interface includes functions concerning supply, balances, transfers, and delegated spending. Each has a distinct conceptual role:

- `totalSupply` reports the total supply represented by the contract.
- `balanceOf` reports the balance associated with an account.
- `transfer` is the operation for requesting a direct transfer.
- `approve` records an authorization for a spender to use an allowance on an owner’s behalf.
- `allowance` reports the allowance associated with an owner and spender.
- `transferFrom` supports a transfer made using an allowance.

These operations allow an application to work with token quantities and, where relevant, an authorization involving an owner and spender. They do not mean that the standard defines a token’s full business logic. The functions describe a shared interface; the implementation of the particular contract determines its behavior within that interface.

ERC-20 also defines the `Transfer` and `Approval` events. An event is information emitted by a contract for applications to process, rather than a callable function. Applications may use event logs to observe contract activity, such as activity represented by those event types. An event log is not, by itself, a complete explanation of the contract’s state or of how an application should interpret every interaction.

Integrators should check the relevant standard specification and the particular contract implementation when relying on exact behavior or return-value handling. The interface names alone are not a substitute for checking how a given implementation responds. This is especially important where an application’s assumptions depend on a particular result, event, or interaction.

## Optional metadata and implementation differences

Token interfaces are often discussed alongside descriptive fields such as a name, symbol, or display precision. However, the accepted claims available for this article establish the core ERC-20 interface but do not establish which metadata fields are optional or required, or the precise requirements that apply to them. Their status should therefore be checked in the relevant version of the normative specification, rather than inferred from the core-interface description.

Display precision also should not be treated as an economic property or as proof that the contract stores fractional units in a particular way. A display convention and the contract’s underlying representation are distinct questions. The source material available here does not establish the detailed behavior of any metadata field, so no token-specific conclusion follows from this discussion.

More generally, a contract’s use of an ERC-20 interface does not establish identical behavior in every edge case. Applications may make assumptions about function results, events, or other contract behavior. Those assumptions should be checked against the relevant specification and the implementation at issue. A shared interface helps make interaction recognizable; it does not erase implementation differences.

## What ERC-20 compatibility does—and does not—guarantee

A recognized interface can support interoperability by offering applications common operations and event types. An application can use that shared vocabulary when interacting with a contract that exposes the interface. But compatibility does not guarantee that every integration handles every contract correctly, or that every interaction will behave as a user expects. The application’s assumptions and the specific contract’s behavior still matter.

The label ERC-20 is not a certification of safety or legitimacy. The standard does not establish backing, issuance policy, market value, compliance, implementation safety, liquidity, governance, or investment quality. Those are separate questions, and none is answered merely by identifying an interface. This article does not assess any particular token or contract.

The same distinction applies when considering an integration. Recognizing familiar functions and events can help an application communicate with a token contract, but does not by itself prove that the application’s handling is appropriate for every implementation. The interface and the implementation answer different questions: one describes the common operations, while the other determines the behavior of a particular contract.

## How to verify an ERC-20 claim

For a claim about what ERC-20 specifies, consult the canonical ERC-20 specification and identify the relevant specification version. Treat its normative requirements as the source for deciding what the interface requires; do not infer requirements for metadata or edge cases from a short summary of the core functions.

For a claim about a particular token contract, identify the specific contract and examine its implementation and behavior in relation to the interaction being considered. Keep this separate from the general question of what ERC-20 defines. The standard can establish the expected interface, while contract-specific evidence is needed to assess whether a particular implementation behaves as an application assumes.

Ethereum smart contracts have persistent state and executable functions at an on-chain address and can emit events for applications to process. That general model helps explain why both contract state and emitted events matter when examining an implementation. It does not, by itself, establish that a particular contract has been independently assessed or that it is safe.

The central point is that ERC-20 defines a common interface for fungible-token contracts on Ethereum, including supply, balances, transfers, approvals, allowances, and the `Transfer` and `Approval` events. It gives applications a shared set of operations to recognize, while leaving contract-specific behavior and broader token properties to be assessed separately.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
