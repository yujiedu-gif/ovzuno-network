---
title: "ERC20 token explained: the Ethereum token standard"
description: "ERC20 token explained: learn what the Ethereum token standard defines, how its common interface works, and what it does not guarantee about a token."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["erc20 token"]
author: "editorial_team"
primary_keyword: "erc20 token explained"
owned_question: "What does it mean for a token to follow the ERC-20 standard, and what does that standard specify?"
risk_level: "medium"
---

An ERC-20 token is managed by a smart contract that exposes a common interface for balances, transfers, spending approvals, and related events. Following the standard means the contract defines that interface; it does not establish what the token represents, whether it has value or backing, or whether its implementation is secure.

## What ERC-20 means

ERC-20 is a standard interface for fungible tokens on Ethereum-compatible systems. A fungible token’s units are treated as interchangeable under the contract’s rules. The interface provides a familiar set of functions and events through which compatible applications can interact with a token contract.

An ERC-20 token is not a separate blockchain. It is managed by a contract on a network. The contract’s address identifies that deployed contract, so a token name or ticker alone is not enough to identify which contract is meant.

Conformance describes interface behavior, not a token’s purpose, issuance policy, transfer restrictions, or economic arrangement. Those depend on the particular implementation and any systems around it. The standard’s interface also does not determine whether a token is backed or redeemable, or what rights a holder has.

## What the ERC-20 interface specifies

The ERC-20 interface defines functions for querying supply and balances, transferring tokens, and authorizing spending. In plain language, its commonly encountered operations include:

- **`totalSupply` and `balanceOf`:** query the supply and the balance recorded for an address.
- **`transfer`:** request a transfer to another address, subject to the contract’s rules.
- **`approve`:** authorize another address to spend up to an approved amount on the holder’s behalf.
- **`transferFrom`:** request a transfer from a holder’s balance using an allowance granted to the caller.

An allowance is a permission recorded through the token contract. It is separate from a direct transfer: the holder authorizes a spender, and the spender may then request transfers within the applicable allowance and contract rules. Readers should distinguish the spender being authorized from the address receiving tokens.

The interface also defines two events. `Transfer` reports token-transfer activity, while `Approval` reports an allowance approval. Applications can process these events, but the event names alone do not establish that an application’s display is current or complete.

An interface standard does not specify every possible implementation detail. The ERC-20 interface itself does not establish a token’s issuance policy, backing, market value, compliance, or code safety. To understand a specific token, readers need information about the actual contract, not just the name of the standard.

## How an ERC-20 token transfer works

A user generally interacts through a wallet or application that prepares a request to the token contract. The user authorizes the request, and the contract applies its own rules. If the requested operation is allowed, the contract updates its recorded balances and may report the transfer through an event.

The direct-transfer and delegated-spending paths differ in authorization. For a direct transfer, the holder calls `transfer`. For delegated spending, the holder first uses `approve` to set an allowance. The authorized spender can then call `transferFrom` to request a transfer within that allowance and the contract’s other rules. An approval is not itself a token transfer; it grants a defined permission.

The contract’s recorded data is distinct from a wallet or application’s presentation. Interfaces may use contract data and processed event records to show balances or activity. The ERC-20 interface does not prescribe how every application displays that information, so a displayed description should not be treated as a substitute for verifying the relevant contract and network.

## What ERC-20 does not guarantee

ERC-20 does not establish a token’s backing, redemption rights, market value, usefulness, or holder entitlements. Nor does an ERC-20 label by itself prove that a contract is secure, audited, immutable, or free of administrative controls. These are questions about the specific implementation and its surrounding arrangements, not conclusions supplied by the interface standard.

The familiar function names also do not prove that every implementation behaves exactly as a user might assume. A contract can have implementation-specific behavior beyond the common interface. Claims about security, availability, fees, yields, recovery, or regulatory or tax treatment require separate, current evidence relevant to the particular contract, service, or jurisdiction. The ERC-20 label alone cannot support those claims.

## How to read an ERC-20 token description

When a description names a particular token, first match its stated network and contract address to reliable records. The contract address matters because the token name or ticker alone does not identify a deployed contract. Then review information for that specific contract to understand its interface and any implementation-specific behavior or permissions.

Keep three kinds of statements separate: what the standard interface defines, what the particular contract implements, and what an application or other arrangement claims about the token. The interface explains common ways to query balances, transfer tokens, grant spending permissions, and observe related events. It does not, by itself, establish the token’s purpose, economic properties, security, or legal and tax treatment.

## Sources and references
