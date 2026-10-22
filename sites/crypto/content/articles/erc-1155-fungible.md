---
title: "ERC 1155 fungible tokens: how balances and IDs work"
description: "Learn how ERC 1155 fungible tokens use token IDs and per-account balances, and how that model differs from ERC-20 tokens and unique ERC-1155 assets."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: []
author: "editorial_team"
primary_keyword: "erc 1155 fungible"
owned_question: "How does ERC-1155 represent fungible token balances, and how do those balances differ from ERC-20 tokens and ERC-1155 non-fungible token IDs?"
risk_level: "medium"
---

For smart-contract developers and technically curious readers, ERC-1155 represents fungible assets as quantities held by accounts for particular token IDs. An ID identifies a token type, while the balance records how many units of that type an account has. ERC-1155 can manage multiple token types in one contract, including fungible, non-fungible, and semi-fungible configurations. The ID alone does not determine which behavior applies.

## What “fungible” means in the ERC-1155 standard

Fungible units are interchangeable with other units of the same token type in the token model. When an account holds units of one fungible type, the quantity—not a separate identity for each unit—is the relevant distinction. Fungibility is a property of units within a token type; it is not something a reader can infer from the number assigned to an ID.

ERC-1155 is a multi-token standard: one contract can manage multiple token types, including fungible, non-fungible, and semi-fungible configurations. This lets a contract organize different types under one standard’s interface. It does not mean every ID in that contract has identical behavior. The implementation and its conventions determine how a particular ID is intended to work.

It helps to separate a **token type** from a **unit**. An ID identifies a type within the contract’s scheme. A unit is a quantity of that type. For a fungible type, units are interchangeable; for a non-fungible configuration, the units may be distinguished or tracked as unique items. The ID’s numeric value does not itself declare which case applies.

## How ERC-1155 fungible balances work

An ERC-1155 balance is associated with both an account and a token ID. The question is not simply “What does this account hold?” but “How many units of this ID does this account hold?” The ID identifies the type, and the balance gives the quantity associated with that account and type.

For example, imagine a contract that uses ID 12 for a fungible token type. If an account’s balance for ID 12 is 40, that quantity represents 40 units of that type in the contract’s accounting. This is an illustration of the account-and-ID relationship, not a universal assignment of ID 12 or a required balance format for every contract.

The two pieces of information have different jobs:

- **ID:** identifies which token type is being referenced.
- **Balance:** gives the quantity of that type associated with an account.

For fungible units of the same type, the quantity represents interchangeable units rather than a list of separately identified items. A transfer must be read in the context of the ID and quantity involved. To interpret what it means, a reader needs the token type and amount, along with the contract’s rules for that ID.

A balance answers a narrow accounting question: what quantity is associated with this account and ID under the contract’s behavior? It does not, by itself, explain the token’s value, issuance policy, backing, or other characteristics. Those matters are separate from the relationship among ID, account, and quantity.

## ERC-1155 fungible tokens compared with ERC-20

ERC-20 and ERC-1155 can both represent fungible units, but they organize their token interfaces differently. ERC-20 defines a common fungible-token interface that includes total supply, balances, transfers, allowances, approvals, and `Transfer` and `Approval` events. ERC-1155 allows one contract to manage multiple token types, with balances associated with accounts and particular IDs.

That difference changes how a reader frames a balance. In the ERC-20 model, the balance is read in the context of the token contract’s fungible-token interface. In ERC-1155, a balance is associated with an account and an ID inside a contract that may manage multiple types. The account-and-ID pairing is central to interpreting an ERC-1155 quantity.

The interface conventions differ as well. ERC-20 includes allowances and approvals in its common interface. The ERC-1155 distinction relevant here is that one contract can manage multiple token types, including fungible and non-fungible configurations. This is a difference in organization and interface, not evidence that one standard is universally preferable or that a particular contract works with every application.

The standards describe token interfaces and behavior, but they do not establish every characteristic of a specific token or implementation. A standard’s interface alone is not a basis for inferring a token’s economic or legal characteristics, and a conforming interface does not prove that an individual contract is safe. Those questions require evidence beyond the basic standard mechanics.

## Fungible and non-fungible IDs in one ERC-1155 contract

Because ERC-1155 supports fungible, non-fungible, and semi-fungible configurations, a contract can use separate IDs for different token types and define how each is handled. A fungible ID represents interchangeable units of its type. A non-fungible configuration concerns distinguishable items. For comparison, an ERC-721 NFT is uniquely identified on an Ethereum chain by the combination of its smart-contract address and token ID.

The shared idea of an identifier should not hide the difference in what is identified. An ERC-1155 ID names a token type within a contract that may manage multiple types; it does not automatically mean that every unit is unique. Under a fungible configuration, a quantity can be represented as interchangeable units. Under a non-fungible configuration, the implementation may distinguish items rather than treating all units as interchangeable copies.

ERC-1155 allows one contract to manage multiple token types, and a token ID can have a quantity greater than one. As a result, non-fungibility depends on the implementation and supply; it does not follow from the ID alone. Readers should distinguish the identifier, the recorded quantity, and the intended behavior of that type rather than treating any one of them as a complete classification.

This distinction also prevents a common interpretive error: a type identifier is not necessarily an individual-item identifier. The standard supports configurations where units are fungible, non-fungible, or semi-fungible, so the contract’s handling of a type matters. The standard-level description establishes that these configurations are possible, but it does not establish how a particular deployed contract assigns or enforces them.

## What to verify in an ERC-1155 implementation

When interpreting a particular ERC-1155 token, start with the contract and its documentation rather than assuming behavior from the standard name or ID value. Check how the implementation describes the relevant ID, what balance it records for an account, and how it handles transfers for that ID and quantity. This gives the reader a basis for distinguishing a fungible balance from a configuration intended to represent distinguishable units.

Keep each finding within its scope. A balance associates a quantity with an account and ID; it does not, by itself, establish what rights or offchain content the units represent. Similarly, the standard’s support for multiple token types does not prove that a particular implementation follows any stated convention or is correct and secure. Questions about security, recovery, or compliance need contract-specific evidence and, where applicable, jurisdiction-specific evidence; they cannot be answered from an ID or the standard alone.

A useful reading sequence is to identify the contract, identify the relevant ID, then interpret the account’s balance and the implementation’s transfer behavior for that ID. After that, determine whether the contract describes its units as interchangeable or individually distinguished. This sequence keeps three separate questions—token type, quantity, and uniqueness—from being collapsed into one.

The core comparison is therefore straightforward: ERC-1155 associates balances with accounts and IDs and can organize multiple token types in one contract; ERC-20 defines a common fungible-token interface with balances and other named functions; and an ERC-1155 ID does not, by itself, reveal whether its units are fungible. A particular contract’s implementation and conventions are needed to interpret that ID’s behavior.

## Sources and references

- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [ERC-721: Non-Fungible Token Standard](https://eips.ethereum.org/EIPS/eip-721) — Ethereum Improvement Proposals; retrieved 2026-10-18.
