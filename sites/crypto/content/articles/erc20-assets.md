---
title: "erc20 assets: What the Ethereum token standard defines"
description: "Learn what erc20 assets are, which common contract functions and events the standard defines, and what ERC-20 compatibility does not guarantee."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["ERC-20 standard", "fungible tokens", "token contract"]
author: "editorial_team"
primary_keyword: "erc20 assets"
owned_question: "What does it mean for an asset to be ERC-20, and what does the standard define about its contract interface and interactions?"
risk_level: "medium"
---

For builders and technically curious readers, an asset is ERC-20 when its token contract provides the common interface defined by the ERC-20 standard. That interface gives applications a shared way to query balances, transfer tokens, authorize spending, and observe transfer and approval events. Compatibility describes how the contract communicates; it does not, by itself, establish the token’s value, backing, rights, liquidity, or safety.

## What makes an asset ERC-20?

ERC-20 is an interface standard for fungible tokens. Fungible means that units are treated as interchangeable under the token contract’s rules. The standard defines a common set of functions and events so that applications can interact with compatible token contracts using expected operations and data.

The phrase “ERC-20 asset” is therefore a technical description of a token contract’s interface. It does not necessarily describe what the token represents. A contract’s interface alone cannot show whether a token corresponds to an offchain asset, grants a claim against an issuer, or carries particular governance or redemption rights. Those questions concern the token’s arrangement and documentation, rather than the interface label.

A useful way to keep these ideas separate is to distinguish three things: the token contract, the units that contract records, and any external asset or rights someone associates with those units. ERC-20 specifies parts of the first two at the interface level. It does not settle the third. Applications may be able to interact with a token consistently without knowing whether its associated claims are valid or what terms govern them.

## ERC-20 assets and the standard interface

The ERC-20 standard defines a common fungible-token interface that includes total supply, balances, transfers, allowances, approvals, and the `Transfer` and `Approval` events. A function is an operation an application can request from a contract. An event is a record emitted by a contract to signal specified activity for applications and other observers to process.

The interface’s elements serve different purposes. A total-supply query asks for the quantity the contract reports as issued. A balance query asks how many units the contract associates with an address. A direct transfer requests movement of units between addresses under the contract’s rules. Approval and allowance functions concern permission for another address to spend tokens, rather than the movement itself.

The `Transfer` event signals a token transfer, while `Approval` signals a change in spending authorization. These events are part of the shared interface; their presence does not independently verify an asset’s external value or the truth of claims about it. They communicate contract activity in the form defined by the interface.

This common vocabulary can help applications support different token contracts without requiring a unique set of operation names for each one. But recognizing familiar functions and events is not the same as validating the contract’s implementation. The standard describes the interface, not every internal design choice or additional behavior that a particular contract may have.

## How token contracts represent balances and transfers

A token contract keeps track of balances associated with addresses and exposes ways to query or change that recorded state. When a user asks an application to transfer tokens, the requested operation is directed to the token contract. The contract’s code applies its rules to the request; the ERC-20 interface provides the common form of interaction.

This differs from sending a network’s native currency. A token transfer calls the token contract’s interface, while a native-currency transfer is a different kind of network transaction. The distinction matters when reading an application screen or transaction description: the fact that both actions can move value between addresses does not make their technical paths identical.

Consider a generic application flow. An application queries a token contract for the balance associated with an address, then offers an operation that requests a transfer to another address. The balance query and transfer are interface-level interactions. The specific contract determines how it processes those requests. This is an illustration of the general interface, not a promise that every contract, wallet, or application handles the flow in the same way.

A displayed balance should be interpreted narrowly: it is a quantity reported through the relevant contract and application. It does not, by itself, establish a market value, redemption right, reserve backing, or broader ownership claim. The ERC-20 interface does not supply those conclusions. Information about a particular token’s terms and surrounding arrangement must be considered separately.

## Allowances and delegated transfers

An allowance is a contract-recorded spending limit that permits another address to transfer tokens on an owner’s behalf, subject to the contract’s behavior. An approval sets or changes that authorization. A delegated transfer is a separate operation that can use the allowance; the approval itself is not the transfer of tokens.

This distinction helps explain why approval screens and transfer screens represent different actions. Approval concerns permission. A later delegated transfer concerns use of that permission. The common ERC-20 interface provides the operations for approvals, allowances, and transfers, but it does not decide whether a particular authorization is appropriate for a user or application.

Before interacting, readers should verify which contract and address are involved and what spending authorization is being requested. Compatibility alone cannot establish that an approval is safe, necessary, or limited as expected. The specific contract’s implementation and the details of the requested interaction matter. A familiar interface should not be treated as a substitute for examining the authorization itself.

For application builders, this means that showing an approval as though it were an ordinary transfer can obscure what the user is authorizing. The technical distinction is important even when both operations appear in the same workflow. The interface defines recognizable operations, while the application remains responsible for presenting the requested action clearly and the user must decide whether to authorize it.

## What ERC-20 compatibility does not guarantee

ERC-20 compatibility does not establish an issuance policy, backing, market value, compliance, or implementation safety. Nor does it establish liquidity, redemption availability, or the rights a token holder may have. The standard defines a common interface for token operations; it is not an evaluation or certification of every token that uses that interface.

A compatible interface also does not mean that all contracts behave identically in every respect. The standard supplies common operations and signals, while the implementation determines how a given contract processes them. Additional behavior or design choices cannot be inferred just from recognizing the standard interface. A technical assessment of a particular contract requires attention to that contract and relevant documentation, rather than relying on the ERC-20 label alone.

This boundary is especially useful when separating contract facts from asset claims. An interface can indicate how applications request a balance or transfer and how they observe approvals. It cannot, by itself, confirm that a token represents a particular external asset, that the external asset exists, or that a holder can enforce a stated claim. Those conclusions require evidence beyond the interface, and this explainer does not make claims about any particular token.

In short, ERC-20 answers a limited but practical technical question: does a token contract expose the common interface for supply, balances, transfers, spending permissions, and related events? It does not answer what the token is worth, what rights it represents, or whether its implementation or surrounding arrangements are safe or dependable. Keeping interface compatibility separate from those broader questions helps readers understand what the standard defines—and where its scope ends.

## Sources and references
