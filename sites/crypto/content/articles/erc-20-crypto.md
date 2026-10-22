---
title: "ERC-20 crypto: what the token standard means"
description: "Learn what ERC-20 crypto means, what the Ethereum token standard specifies, and what compatibility does—and does not—guarantee about a token."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["erc20 crypto", "erc 20 crypto"]
author: "editorial_team"
primary_keyword: "erc-20 crypto"
owned_question: "What does ERC-20 mean in crypto, and what does the standard define for compatible Ethereum tokens?"
risk_level: "medium"
---

ERC-20 is a standard interface for fungible-token contracts on Ethereum. It defines a common set of functions and events that applications can use to communicate with compatible contracts. It is not a particular cryptocurrency, and the standard alone does not establish what a token represents or guarantee its value, safety, or legal status.

## What ERC-20 means in crypto

ERC-20 refers to an interface standard, not to a single token. The letters and number identify a specification for how a token contract can expose common operations to applications. A token, by contrast, is an asset represented and managed by an individual contract. That contract may follow the ERC-20 interface, but it remains a distinct implementation.

This distinction helps avoid treating the standard as a brand, issuer, or asset. A token’s name or ticker may be used to describe it, but “ERC-20” by itself does not name a specific token. It says that the contract is intended to expose a familiar interface for token-related interactions.

The scope here is Ethereum tokens using that interface. ERC-20 should not be taken as a general description of every cryptocurrency or token on every blockchain. The interface standard, the contract implementing it, and the network where that contract operates are separate parts of the picture.

## What the ERC-20 interface specifies

The ERC-20 interface defines common functions and events. Its function set includes ways to expose total supply and account balances, transfer tokens directly, and approve another address to spend up to an authorized amount. The standard also defines `Transfer` and `Approval` events, which communicate transfer and approval-related activity to applications that process them. These are interface conventions: they tell an application what kinds of operations and signals it can expect to work with when interacting with a compatible contract.

An allowance is an authorized spending limit for another address. This is one reason ERC-20 includes more than a basic transfer operation: applications may need to interact with a token contract on a user’s behalf, subject to the approval that the contract records. The standard gives this interaction a common shape; it does not make a particular application, wallet, or service responsible for the token contract’s behavior.

The interface is useful as a shared vocabulary. An application can be built to call expected functions and process expected events, rather than requiring an entirely different interface for every token. But interface compatibility is not identical to universal support: a specific application or service still determines which contracts it can interact with and how it handles them.

## What ERC-20 compatibility does and does not mean

Compatibility means that a contract presents the ERC-20 interface so that software designed for that interface can make the corresponding calls and process the defined events. It can support interaction across applications that recognize the standard. It does not mean that every contract has the same implementation, additional features, or behavior in every circumstance.

The standard also does not establish a token’s backing, issuance policy, market value, compliance, or implementation safety. Those characteristics are not guaranteed by the common interface. A token can conform to an interface without that fact proving what claims, if any, stand behind it or whether its code is free of defects. In particular, the ERC-20 label should not be treated as a quality assessment or a recommendation.

That boundary is important when reading descriptions of tokens. A claim that something is “ERC-20” is a claim about an interface category. It does not, on its own, answer questions about the token’s purpose, issuer, economic arrangements, or risks. Those questions concern the specific token and its surrounding systems, not the definition of the standard.

## ERC-20 standard, token, and network: the distinctions

These three terms refer to different things:

- **Standard:** ERC-20 defines a common interface for token contracts.
- **Token contract:** A particular deployed program that implements the interface and manages a token according to its code.
- **Network:** The blockchain environment on which the contract is deployed and used.

Keeping these categories separate makes the meaning of “ERC-20 crypto” clearer. ERC-20 identifies the interface convention; it is not the name of the blockchain, and it is not enough by itself to identify a particular token contract. A displayed token name or ticker likewise does not define the interface or establish which contract is meant.

In short, ERC-20 is a technical standard for a shared token interface. It specifies common operations and event signals so compatible software can communicate with token contracts in a recognizable way. It does not define every feature of every token, certify an implementation, or settle what the token represents. Detailed token mechanics and balance representation are separate topics from this definition.

## Sources and references
