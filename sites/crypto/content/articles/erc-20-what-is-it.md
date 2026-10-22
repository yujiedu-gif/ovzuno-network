---
title: "ERC 20 what is it? A clear guide to the Ethereum token standard"
description: "ERC 20 what is it? Learn what the Ethereum token standard specifies, how its core functions and events support token interactions, and what it does not guarantee."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["ERC-20 standard", "Ethereum token standard", "ERC-20 functions"]
author: "editorial_team"
primary_keyword: "erc 20 what is it"
owned_question: "What is ERC-20, and what rules and functions does it define for fungible tokens on Ethereum-compatible networks?"
risk_level: "medium"
---

ERC-20 is a technical standard that specifies a common interface for fungible-token contracts. It gives applications familiar ways to request balances and supply, transfer tokens, authorize spending, and observe events. The standard describes an interface; it does not define a particular token or guarantee that a token has value, backing, or safe code.

## What ERC-20 means

A technical standard sets out expected ways for software components to communicate. ERC-20 is such a standard for token contracts: it describes a common set of functions and events that applications can use when interacting with compatible contracts. A fungible token is a token whose units are treated as interchangeable according to the contract’s rules.

ERC-20 is not Ethereum itself, nor is it the name of a single asset. It specifies how a token contract presents certain operations. Separate contracts may use the same interface while representing different tokens and following different implementation rules. The ERC-20 standard defines a common interface for balances, direct transfers, and approvals that let another address spend up to an authorized amount. It does not establish a token’s issuance policy, backing, market value, compliance status, or implementation safety.

## What the ERC-20 interface specifies

The interface includes ways to query a token’s total supply and the balance associated with an address. These are requests to a token contract; they do not, by themselves, explain what the token represents or why its supply has a particular value.

For moving tokens, the interface includes `transfer`, which supports a direct transfer, and the delegated-spending functions `approve` and `transferFrom`. In the delegated pattern, an account authorizes another address to spend up to an approved amount. The authorized address can then request a transfer within that allowance, subject to the contract’s behavior. An allowance is a permission represented by the token contract, not a promise that a transaction will succeed.

ERC-20 also defines the `Transfer` and `Approval` events. A transfer event reports a token transfer, and an approval event reports an authorization. Applications can use events as part of their view of contract activity, but must interpret them in the context of the relevant contract and network.

Some token contracts expose descriptive metadata such as a name or symbol. Such descriptive fields are distinct from the core operations for balances, transfers, and approvals. A familiar display name does not uniquely identify a contract or prove anything about the asset it represents.

## How compatible applications use ERC-20

A wallet or application can use the common interface to request token information or initiate token actions. Other smart contracts can also call the expected functions. This shared vocabulary helps applications interact with compatible contracts without requiring a different basic method set for each one.

That common interface does not mean every integration behaves identically. An application must identify the intended contract and network, and its assumptions need to match the implementation it calls. The ERC-20 label alone does not certify that a contract conforms correctly or that an application handles its responses safely.

Allowances are a concrete point to check when an application requests delegated spending. The authorization identifies a spender and an amount the spender may use, subject to the token contract’s behavior. The standard does not dictate how a wallet explains an approval to a user, what limits an application sets, or what additional controls a separate service uses. Those are matters of the implementation and integration rather than guarantees supplied by the interface.

## What ERC-20 does not guarantee

ERC-20 does not establish who issued a token, whether it is backed by anything, its market value, or its legal or regulatory status. Those questions concern a particular token and its surrounding arrangements, not the interface specification. Nor does a standard interface guarantee that the contract code is secure or that an erroneous or unwanted action can be reversed.

The standard also does not set universal fees, service availability, or compliance requirements. Those can depend on the contract, network, wallet, application, and other services involved. ERC-20’s common function names should therefore be understood as a technical compatibility layer, not as assurance about every operational detail or outcome.

## Questions to check before relying on a token

Start by identifying the exact network and contract address. A name or symbol alone is not enough to distinguish one contract from another. Confirm that the address corresponds to the intended token and network using authoritative records relevant to that asset.

Then review documentation and security information for the specific implementation and for the application that interacts with it. The interface explains what methods are available, but does not show by itself whether the implementation follows expectations or whether an integrating system uses it appropriately.

For questions about legal or regulatory status, tax treatment, fees, or availability, consult current authoritative information for the relevant context. ERC-20 does not answer those questions. Its scope is narrower: it standardizes a common technical interface, while properties of a particular token and the behavior of systems using it require separate evaluation.

## Sources and references
