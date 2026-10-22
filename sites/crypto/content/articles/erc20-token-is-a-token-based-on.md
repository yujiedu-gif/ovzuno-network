---
title: "ERC20 token is a token based on: Ethereum’s standard explained"
description: "Learn what an ERC20 token is a token based on, how Ethereum’s ERC-20 standard shapes token interactions, and what it does not guarantee."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["erc20 token token based on"]
author: "editorial_team"
primary_keyword: "erc20 token is a token based on"
owned_question: "What is an ERC-20 token based on, and what does the ERC-20 standard define?"
risk_level: "medium"
---

An ERC-20 token is a fungible token whose Ethereum contract uses the ERC-20 standard’s common interface. The standard defines ways for applications to check balances, transfer tokens, authorize spending, and observe transfer and approval events. It does not define what a token is for, how it is issued, or whether it has backing or value.

## What an ERC-20 token is based on

ERC-20 is a token standard: a shared set of interface expectations for fungible tokens on Ethereum-compatible systems. A token contract is the particular program that keeps token-related state and provides operations that applications can call. When that contract follows the ERC-20 interface, compatible applications have a common way to interact with it.

“Fungible” means units of the same token are treated as interchangeable under the token’s rules. ERC-20 is not a separate blockchain or a currency in itself. It describes an interface for tokens, not one specific token or its economic design.

The standard’s scope matters. It tells an application which kinds of interactions to expect, but it does not establish what the token represents or why someone might use it. Those questions depend on the particular token and its surrounding systems.

## What the ERC-20 standard specifies

The ERC-20 interface includes functions for querying total supply and account balances, transferring tokens, and approving another address to spend up to an authorized amount. It also defines `Transfer` and `Approval` events, which can signal token movements and changes to spending permissions to applications and observers. These are interface elements, not a guarantee that every token contract has identical internal logic or policies. [source](<https://eips.ethereum.org/EIPS/eip-20>)

An approval is distinct from a transfer: it authorizes another address to spend tokens up to a specified amount. The standard provides a common interface for expressing that permission; what an application does with it depends on the contract and the application’s workflow. A reader should not infer from the word “standard” that every interaction has the same user experience or consequences.

The interface also does not make every possible behavior mandatory. For example, the ERC-20 specification describes some functions as optional. Implementations and integrations therefore need to account for the specific contract they interact with rather than assuming every contract exposes every optional feature in the same way.

## How ERC-20 tokens interact with wallets and applications

A wallet or application can use the common interface to request token information or initiate supported interactions with a token contract. That shared pattern can make it easier to build integrations across different token contracts, but it does not mean every wallet or application supports every token or handles every contract identically. Support depends on the application, the specific contract, and the network context.

Token balances recorded by a token contract are also distinct from ETH, Ethereum’s native cryptocurrency. An ERC-20 token is not simply another name for ETH. A wallet may display both, but they are separate assets with different roles: ETH is native to Ethereum, while an ERC-20 token is represented through a token contract’s state and interface.

For a user-facing action, the application is responsible for presenting the relevant token and operation clearly, and the user is responsible for checking what they authorize. The standard itself specifies the interface; it does not promise that an application’s display, token identification, or handling is correct.

## What ERC-20 does not tell you about a token

ERC-20 compliance does not establish a token’s purpose, issuance policy, backing, governance, market value, legal status, or safety. A token contract may implement the standard while the token’s design and surrounding arrangements remain specific to that project. The interface alone does not verify claims made about a token or its issuer. [source](<https://eips.ethereum.org/EIPS/eip-20>)

Nor does the standard establish that a token is audited, legitimate, recoverable, or guaranteed to remain available. Those are separate, token-specific questions. The ERC-20 interface provides no basis for treating compliance as proof of any such property.

Tokenization more broadly means representing assets or liabilities on programmable digital ledgers; that description does not mean that a particular token automatically conveys ownership or other rights in an offchain asset. [source](<https://www.imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921>) Where a token is described as connected to an asset or issuer, the reader must distinguish the onchain token record from the specific arrangements that determine what it represents.

## ERC-20 terminology and network scope

The standard’s name is conventionally written “ERC-20,” with a hyphen; “ERC20” is a common unhyphenated search spelling. In this article, both spellings refer to the Ethereum token standard, not to a claim that similarly named standards or tokens on other networks behave the same way.

The practical takeaway is narrow: an ERC-20 token is based on a shared interface for fungible tokens, and the standard defines common ways to query balances, transfer tokens, approve spending, and signal transfers and approvals. It does not tell you what a particular token is worth, represents, or guarantees. Those details require evidence about the specific token and its context.

## Sources and references

- [ERC-20: Token Standard](https://eips.ethereum.org/EIPS/eip-20) — Ethereum Improvement Proposals; retrieved 2026-10-19.
- [Tokenized Finance](https://www.imf.org/en/publications/imf-notes/issues/2026/04/01/tokenized-finance-574921) — International Monetary Fund; retrieved 2026-10-18.
