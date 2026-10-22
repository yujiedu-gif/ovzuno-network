---
title: "ERC20 What Is: A Definition of the Ethereum Token Standard"
description: "ERC20 what is explained: learn how this Ethereum token interface standard defines common functions and events for compatible tokens."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["smart_contract_dapps"]
tags: ["erc20"]
author: "editorial_team"
primary_keyword: "erc20 what is"
owned_question: "What is ERC-20, and what does the standard specify for compatible tokens?"
risk_level: "medium"
---

ERC-20 is a standard interface for fungible tokens on Ethereum-compatible systems. It defines a common set of functions for querying token information, transferring tokens, and authorizing spending, along with `Transfer` and `Approval` events. The standard describes how a compatible contract communicates through that interface; it does not define a token’s value, purpose, or economic design.

## ERC20 What Is? The Standard in Brief

ERC-20 is a technical specification for a shared token interface. An interface is the set of functions and events that other software can use to interact with a contract. When a token contract supports the ERC-20 interface, applications can use those specified operations without needing a different interaction pattern for each token.

The standard concerns the contract’s communication surface, not what the token represents or how it is meant to be used. ERC-20 does not determine a token’s price, backing, issuance policy, legal status, or implementation safety. Those are separate questions about a particular token and its surrounding systems.

## What the ERC-20 Interface Specifies

The interface includes functions for reading the total supply and an account’s balance, transferring tokens, and checking or setting an allowance. An allowance is an amount an address has approved another address to spend on its behalf. The functions give applications a common vocabulary for these operations; they do not describe a token’s broader economic purpose.

ERC-20 also specifies two events. `Transfer` reports a token transfer, while `Approval` reports an authorization or allowance change. Applications can process these events as part of their interaction with a contract.

The ABI, or application binary interface, defines how function selectors, arguments, return values, errors, and events are encoded between applications and EVM contracts. An application therefore needs an ABI that matches the contract interface and deployed network address it is using. [source](<https://docs.soliditylang.org/en/latest/abi-spec.html>)

## Required Functions and Optional Metadata

The standard distinguishes its core interface from optional metadata functions. Optional metadata can provide a token’s name, symbol, and decimal precision. Because these functions are optional, readers and applications should not assume that every ERC-20-compatible contract exposes them.

This distinction is useful when interpreting token information: metadata can describe a token for an application, but it is not the same as the core functions and events specified for interaction. Its presence—or absence—does not establish the token’s value, backing, or quality.

## What ERC-20 Compatibility Does—and Does Not—Mean

Compatibility means that a contract supports the relevant ERC-20 interface. It gives applications a shared way to request functions and process events, but the interface alone does not establish that a token is secure, valuable, legally compliant, or suitable for a particular purpose. Those properties are not guaranteed by the standard.

ERC-20 is also only one token-standard design. For example, ERC-1155 allows one contract to manage multiple token types, including fungible, non-fungible, and semi-fungible configurations. That separate standard illustrates that token standards define interfaces and capabilities; they are not interchangeable descriptions of a token’s economics. [source](<https://eips.ethereum.org/EIPS/eip-1155>)

In short, ERC-20 specifies a common interface—core functions and events—for compatible tokens. Questions about how a particular token operates, how its balance is represented, or how a contract is implemented require separate explanations beyond this definition.

## Sources and references

- [ERC-1155: Multi Token Standard](https://eips.ethereum.org/EIPS/eip-1155) — Ethereum Improvement Proposals; retrieved 2026-10-18.
- [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html) — Solidity Documentation; retrieved 2026-10-19.
