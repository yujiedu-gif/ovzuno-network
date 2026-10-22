---
title: "ERC20 standard: What its interface specifies and what it does not"
description: "Learn what the ERC20 standard defines for fungible-token contracts, how applications use its interface, and which implementation details it does not guarantee."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "erc20 standard"
owned_question: "What does the ERC-20 standard specify for fungible-token contracts, and what does it leave to implementers and applications?"
risk_level: "medium"
---

The ERC-20 standard defines a shared interface for fungible-token contracts on Ethereum-compatible systems: functions for supply, balances, transfers, and approvals, plus events that applications can observe. It does not define a token’s value, backing, issuance policy, legal status, or implementation safety. A compatible interface can help applications communicate with a contract, but it is not a guarantee that every token or integration behaves as expected.

## What the ERC20 standard is designed to standardize

ERC-20 is an interface specification: it describes how a fungible-token contract exposes common operations and information. Fungible means that units of the same token are treated as interchangeable under the contract’s rules. The standard gives wallets, applications, and other contracts familiar methods for interacting with a token without requiring every integration to invent a different set of function names and behaviors.

That common interface is the boundary of what the standard establishes. ERC-20 does not create or issue a token, and it does not establish why a token exists or what it represents. A token’s issuer, contract implementation, and surrounding application determine matters outside the interface. The standard itself does not establish issuance policy, backing, market value, compliance, or code safety.

This distinction is important when comparing token standards. ERC-20 is designed for fungible tokens. ERC-1155, by contrast, allows one contract to manage multiple token types, including fungible, non-fungible, and semi-fungible configurations; a token ID can have a quantity greater than one. The standards describe different interface models, not interchangeable guarantees about assets or their economics.

## The core functions and events applications rely on

The ERC-20 interface includes functions that expose supply and balances, move tokens, and manage delegated spending. In practical terms, `totalSupply` reports the token’s supply according to the contract, while `balanceOf` reports the balance associated with an address. `transfer` lets a caller initiate a transfer from their own token balance to a recipient. These functions provide a common vocabulary for applications, but their presence does not determine the token’s value or how the issuer manages it.

Delegated spending uses three related functions. `approve` lets an account authorize another address to spend up to an approved amount. `allowance` reports the remaining authorized amount for an owner-and-spender pair. `transferFrom` lets an authorized spender transfer tokens from the owner within that allowance. The allowance is a contract-level authorization; it is distinct from the token holder’s own direct transfer.

The interface also defines `Transfer` and `Approval` events. Events are records emitted by contract execution that applications can process. A `Transfer` event indicates a token transfer under the contract’s event rules, and an `Approval` event indicates an approval-related change. Applications may use such signals to update their views or trigger other processing, but an event is not a substitute for checking the relevant contract and transaction context.

Some token contracts also expose metadata such as a name, symbol, or decimal precision. These are commonly useful to applications for presentation, but the ERC-20 interface’s core functions and events do not make metadata a guarantee of authenticity, correctness, or consistent display. An application should not treat a familiar name or symbol as proof that it has identified the intended contract.

## How allowances enable delegated token transfers

An allowance creates a limited permission relationship between a token owner and a spender. The owner is the address whose tokens may be moved; the spender is the address authorized to call `transferFrom`; and the recipient is the address that receives the tokens. The spender and recipient may be different addresses.

A typical sequence is: an owner authorizes a spender with `approve`, an application or contract checks the authorization with `allowance`, and the spender calls `transferFrom` to move tokens to a recipient. The token contract enforces the allowance according to its implementation. This mechanism lets an application arrange a token transfer initiated by an authorized spender rather than requiring the owner to submit each transfer directly.

For integration design, approval scope matters: an application should make clear which spender is being authorized and what amount the user is approving. The interface standardizes the relevant operations, but it does not determine whether a particular approval request is appropriate or whether the spender’s broader behavior is safe. Approval should therefore be understood as permission for a specific contract interaction, not as a general endorsement of an application.

## What ERC-20 compatibility does not guarantee

ERC-20 conformance is not a promise about a token’s economics or an issuer’s conduct. The interface does not establish backing, market value, issuance policy, legal status, or compliance. Two contracts can expose the same common interface while differing in their terms, administration, and internal behavior. Avoid inferring shared economic or governance properties from a shared interface.

Nor does interface compatibility prove that a contract is secure or that every application will handle it correctly. A token contract may implement the interface, while a wallet, exchange, or other application may make additional assumptions about transfer behavior, event handling, or metadata. The standard alone does not establish that those assumptions are correct. Application behavior and contract behavior must be considered separately.

The same boundary applies to security claims. A standard interface is not a contract-specific security review, and it does not guarantee recoverability or unrestricted transferability in every context. Those questions require evidence about the relevant contract and application; the ERC-20 label by itself is insufficient.

## Questions to check before integrating an ERC-20 token

Before an integration, identify the intended network and verify the token contract identity using evidence appropriate to that network and application. Do not rely on a displayed name or symbol alone. Then confirm that the integrating application uses the expected interface and understands the token’s actual implementation behavior.

Review the contract’s documentation and any contract-specific security evidence separately from the standard. If the integration uses delegated transfers, check which spender receives authorization, what scope is requested, and how the application represents the resulting permission to the user. Also decide how the application will process transfer and approval events, and avoid assuming that an event alone resolves every application-level state question.

Finally, treat claims about value, backing, fees, yields, availability, recovery, compliance, or legal and tax status as separate questions requiring current, relevant evidence. ERC-20 conformance answers a narrower technical question: whether a contract presents a common interface for fungible-token operations. It does not answer those broader questions for implementers, applications, or users.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
