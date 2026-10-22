---
title: "erc20 what is it? A Definition of Ethereum’s Token Standard"
description: "erc20 what is it? Learn what Ethereum’s token standard defines, how its shared interface supports common interactions, and what it does not guarantee."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["erc20 it"]
author: "editorial_team"
primary_keyword: "erc20 what is it"
owned_question: "What is ERC-20, and what common interface does it define for fungible tokens on Ethereum?"
risk_level: "medium"
---

ERC-20 is a technical standard for a common interface used by fungible tokens on Ethereum. It describes how applications and contracts can interact with a token through shared functions; it is neither a token itself nor a separate blockchain. Compatibility with the interface does not establish what a particular token is worth, what backs it, or how its contract behaves beyond that interface.

## erc20 what is it? The short definition

A standard is a shared set of interface expectations. In this case, ERC-20 lets token contracts present common ways for other software to query and interact with them. “Fungible” means that units are treated as interchangeable within the token’s rules, rather than identified as individually distinct items.

ERC-20 therefore describes an interface, not a single universal token implementation. Many different token contracts can follow the same standard while having distinct code, configurations, and operating rules. The standard helps define how software can communicate with them; it does not make the contracts identical.

## What the shared ERC-20 interface supports

The ERC-20 interface includes methods for querying total supply and account balances, transferring tokens, and authorizing another address to spend up to an approved amount. It also specifies `Transfer` and `Approval` events. These common elements give applications a familiar way to request token information or initiate supported interactions, while events provide activity signals for software that processes them.

The distinction is between an interface and the application using it. An interface describes the expected form of an interaction; an application still needs to communicate with the relevant contract and interpret its responses. A shared interface can support reuse, but it does not mean every application supports every contract or handles every token-specific detail in the same way.

## What ERC-20 compatibility does not establish

The ERC-20 standard does not establish a token’s backing, issuance policy, market value, compliance status, or implementation safety. Those are separate questions about the particular token and its context. A token can expose familiar ERC-20 functions without the interface itself explaining the economic or operational arrangements behind it.

Nor should compatibility be treated as a guarantee that every wallet, application, or service will support a token, or that a mistaken interaction can be reversed. The standard defines a common interface; it does not promise universal support, recovery, or a particular outcome from a transaction.

## The standard versus an individual token contract

When considering an ERC-20 token, keep two levels separate. First, the standard describes the common interface: the methods and events applications may expect. Second, the individual contract has its own code and configuration, which determine its implementation-specific behavior. Further details may also depend on systems or terms outside the interface.

For a question about a particular token, the relevant contract documentation and verified code are more informative than the ERC-20 label alone. That label indicates a claimed relationship to a shared interface; it is not a complete description of the token. ERC-20 is best understood as a compatibility convention for common token interactions, not as a certification of a token’s qualities or guarantees.

## Sources and references

- [Smart contract composability](https://ethereum.org/developers/docs/smart-contracts/composability/) — ethereum.org; retrieved 2026-10-19.
