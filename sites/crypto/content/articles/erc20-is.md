---
title: "ERC20 is a Token Standard: What It Defines and What It Doesn’t"
description: "ERC20 is a token standard for fungible assets on Ethereum. Learn what its interface defines, how contracts use it, and what the standard does not guarantee."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["erc20"]
author: "editorial_team"
primary_keyword: "erc20 is"
owned_question: "What does ERC-20 define for fungible tokens on Ethereum, and what does it leave to individual token contracts?"
risk_level: "medium"
---

ERC-20 is a standard interface for fungible tokens on Ethereum. It defines common ways for applications and contracts to query balances and supply, request transfers, authorize delegated spending, and report activity through events. It does not define what a token is worth, what backs it, or whether a particular contract is safe; those questions depend on the token’s implementation and the arrangements around it.

## ERC20 is a common interface for fungible tokens

ERC-20 is a standard, not a specific token or a blockchain. A token contract is the individual program that provides token behavior, while the ERC-20 interface describes a shared set of interactions that applications can use. “Fungible” means that units are treated as interchangeable within the token system, rather than each unit being distinguished as a unique item.

The standard defines a common interface covering total supply, balances, transfers, allowances, approvals, and the `Transfer` and `Approval` events. Compatibility concerns this specified interface behavior; it does not require every token contract to offer every feature an application might want, nor does it dictate all the behavior a contract may add. The interface is a shared point of interaction, not a description of a token’s purpose or economic terms. [source](<https://eips.ethereum.org/EIPS/eip-20>)

The distinction between a standard and an individual contract matters because a token’s actual behavior comes from its contract. The ERC-20 label describes the interface a contract is intended to expose. It does not name an asset, independently create token units, or establish what those units represent. A digital token can be understood as a ledger record about an asset and its owner, with programmable rules governing use or transfer; that technical record alone does not determine legal title, enforceability, or the quality of a represented asset. [source](<https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks>)

## What the ERC-20 interface specifies

At a conceptual level, balance and supply queries let software ask the contract about recorded token state. Transfer operations provide a shared way to request movement of units between addresses. Approval and allowance operations support delegated spending: one address can authorize another address to spend up to a specified amount through the token contract. The interface standardizes these interaction categories, not the business reason for using them or the complete rules of a token project. [source](<https://eips.ethereum.org/EIPS/eip-20>)

The standard also includes two named events. `Transfer` reports transfer activity, while `Approval` reports approval activity. Applications can process these events as part of their interaction with a contract. Their presence is not a statement about backing, value, issuer identity, or the rights associated with a token. An event communicates contract activity according to the interface; it does not independently verify offchain claims about the asset. [claim_erc20_interface, claim_cpmi_token_definition]

These functions and events are best read as an interaction vocabulary. An application can recognize the expected interface and use it to communicate with a contract, but the existence of familiar function names is not itself proof that a particular implementation behaves correctly in every situation. The standard’s scope is the common interface, not a complete specification for every application or token arrangement.

## How allowances and transfers interact

An allowance is a permission recorded by a token contract that lets a designated spender request transfers up to an authorized amount. In the common interaction sequence, `approve` sets or changes that permission, `allowance` queries the recorded amount, and `transferFrom` requests a transfer using the delegated authorization. These operations describe how the interface supports delegated spending; they do not guarantee that a requested transfer will occur.

An approval and a transfer are separate interactions. Recording an allowance establishes permission in the contract’s state, while a later `transferFrom` request attempts to use that permission. Whether the request succeeds depends on the particular contract implementation and the state when the transaction is processed. The ERC-20 interface supplies the shared operations, but it does not prescribe every application’s display, confirmation, or transaction-handling policy. [source](<https://eips.ethereum.org/EIPS/eip-20>)

This distinction also helps prevent a terminology mistake: an approval is not the same thing as a completed transfer. It is an authorization that the contract can use within the scope of its recorded allowance. An application may present those steps in different ways, but the standard itself defines only the relevant interface behavior, not a universal user workflow.

## What ERC-20 does not guarantee

ERC-20 does not establish a token’s value, backing, legitimacy, liquidity, or safety. The interface does not settle who may issue units, what a holder’s rights are, what an asset reference means, or which offchain arrangements support a token. A token record and its programmable transfer rules cannot by themselves establish the legal title, enforceability, or quality of a represented asset. Each of those claims needs evidence specific to the token and any related arrangements. [claim_erc20_interface, claim_cpmi_token_definition]

Interface compatibility also does not certify implementation quality. The standard does not amount to an audit or prove that contract code has no defects. Information about a particular token’s additional features or behavior must come from the relevant contract and its documentation, rather than being inferred from the ERC-20 label alone. Contract-specific documentation and independent technical review are relevant sources when assessing claims about an implementation, but neither changes the scope of the standard.

A contract can also include behavior beyond the shared ERC-20 interface. Optional extensions and implementation choices can affect what a token offers, but such additions are not automatically requirements of ERC-20. The practical distinction is between the interface conventions the standard defines and other rules or features that a particular contract chooses to implement. [source](<https://eips.ethereum.org/EIPS/eip-20>)

## Where ERC-20 fits among Ethereum token concepts

ERC-20 behavior is supplied by an individual token contract, and the standard describes a common interface for interacting with that contract. The interface therefore helps applications recognize a set of expected operations, while the contract determines the particular token state and behavior. A label alone cannot answer whether a given application supports that contract or what other systems may be involved.

Other token standards can organize token types differently. ERC-1155, for example, allows one contract to manage multiple token types, including fungible, non-fungible, and semi-fungible configurations. That is a separate standard and design, not an expansion of ERC-20’s interface requirements. This comparison is limited to how standards describe token interfaces; it does not assess any particular token or its properties. [source](<https://eips.ethereum.org/EIPS/eip-1155>)

The boundary is useful when reading a token description: ERC-20 identifies a common interface, not a guarantee about a token’s economic or technical merits. Network or application support, transaction costs, and legal treatment are separate questions that require current information specific to the relevant network, application, or circumstances. The core answer remains narrow: ERC-20 specifies common interaction conventions, while the individual contract and surrounding arrangements determine what a particular token does and represents.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Tokenisation in the Context of Money and Other Assets](https://www.bis.org/publications/tokenisation-context-money-and-other-assets-concepts-and-implications-central-banks) — Committee on Payments and Market Infrastructures, Bank for International Settlements; retrieved 2026-10-19.
- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
