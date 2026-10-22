---
title: "Cryptocurrency concepts: a payment-focused glossary"
description: "Learn cryptocurrency concepts behind a digital-asset payment, from wallet control and transaction signing to network records, confirmation, and settlement."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["crypto_payments"]
tags: ["cryptocurrency concept"]
author: "editorial_team"
primary_keyword: "cryptocurrency concepts"
owned_question: "What core cryptocurrency concepts help explain how a digital-asset payment is represented, authorized, recorded, and settled?"
risk_level: "medium"
---

Cryptocurrency concepts help explain a digital-asset payment by separating who authorizes it, what instruction is sent, how a network records it, and when the relevant parties treat it as complete. The details differ by network, and a network record is not automatically the same thing as a business recognizing that it has received payment.

## What cryptocurrency concepts mean in a payment context

A payment can involve a digital asset, credentials used to authorize an action, a network that processes the instruction, and a sequence of transaction states. These are related components, not interchangeable terms. A wallet interface, for example, is not itself the network record, and a submitted instruction is not necessarily a completed payment.

The terms also depend on the network. Bitcoin, Ethereum, and other systems can represent and process transactions differently. A Bitcoin-specific detail should therefore be identified as such rather than treated as a universal cryptocurrency rule.

## Wallets, keys, addresses, and signing

A **wallet** is a tool or service for managing or using credentials to interact with digital assets. It is more accurate to think of it as a control interface than as a container holding coins. The credentials it uses can authorize actions, while the network maintains its own transaction records.

An **address** is a public-facing identifier used in network activity. In Ethereum’s account model, an externally owned account is controlled by the private key corresponding to its cryptographic address. But a valid signature supports key-control attribution for a transaction; it does not establish which person, organization, device, or service controls that key. ([source](<https://ethereum.org/developers/docs/accounts/>))

**Signing** means using cryptographic credentials to authorize a transaction or another message. Cryptography encompasses several information-security goals, including integrity and source authentication, but a specific cryptographic method usually serves only some of them. A signature is thus an authorization mechanism, not proof of the signer’s real-world identity or of the transaction’s business purpose. ([source](<https://csrc.nist.gov/glossary/term/cryptography>))

Wallets and signing workflows can be organized differently. In one documented EVM tutorial, wallet creation, transaction construction with a blockchain node, and transaction signing through a server-side software development kit are separate steps. That is an example of one provider-specific flow, not a universal wallet architecture. ([source](<https://developers.circle.com/wallets/sign-tx-evm>))

## Network, token, and transaction: the payment’s basic components

A **network** is the environment whose rules determine how transactions are processed and recorded. A **transaction** is an instruction formatted for that network. Its contents and validation rules depend on the system; the word does not imply one shared format across all cryptocurrencies.

A **coin** commonly refers to an asset native to a network, while a **token** refers to an asset represented through a network’s token system. These terms are useful distinctions, but the allowed evidence here does not establish one universal technical definition or a single format used by all networks. The same asset name or symbol, by itself, should not be treated as a complete description of the network representation involved.

In Bitcoin’s transaction model, an **outpoint** identifies a specific prior transaction output using the prior transaction’s hash and the output’s index. This is a Bitcoin-specific way of identifying an output being spent; other networks may use different transaction and state models. ([source](<https://developer.bitcoin.org/reference/transactions.html>))

The practical distinction is between the asset being referenced, the network rules under which it is represented, and the transaction instruction that asks the network to act. Knowing one of those terms does not establish every detail of the others.

## From submitted transaction to confirmation and settlement

**Submission** or **broadcast** means that a signed transaction has been sent into a network’s processing path. It does not, by itself, mean that the transaction has been recorded or that a merchant should treat an order as paid. In Ethereum’s transaction lifecycle, a state-changing interaction is broadcast, selected for a block, executed, and later gains stronger confirmation or finality. A receipt may report failed execution even when the transaction was included in a block. This description is specific to Ethereum’s lifecycle and should not be read as a universal sequence for every network. ([source](<https://ethereum.org/developers/docs/transactions/>))

**Confirmation** refers to recognition of a transaction under the relevant network’s rules. What counts as confirmation, and how the network describes finality, varies by network. The term alone does not specify how much assurance a particular payment requires; no universal threshold follows from this definition.

**Settlement** is a separate, practical concept: the point at which the parties treat the payment obligation as completed. That judgment can depend on business terms as well as network state. A transaction can be visible or included in a network record without that fact alone resolving whether a particular merchant’s conditions for recognizing payment have been met.

These terms mark different stages rather than synonyms: authorization concerns the signing credentials; submission sends an instruction for processing; confirmation concerns network recognition; settlement concerns completion of the obligation as treated by the relevant parties. The exact relationship among those stages depends on the network and the payment arrangement.

## What these concepts do—and do not—tell a payment operator

This vocabulary gives an operator a way to distinguish authorization, network processing, and business recognition. It can help clarify what someone means by “signed,” “broadcast,” “confirmed,” or “settled,” without assuming that those words describe the same event.

The definitions do not establish transaction fees, processing time, privacy, reversibility, compliance status, or suitability for a particular payment. Nor do they select a provider or prescribe an implementation. Those questions require separate, context-specific analysis; they cannot be answered by the glossary alone.

## Sources and references

- [Transactions Reference](https://developer.bitcoin.org/reference/transactions.html) — Bitcoin Developer Reference; retrieved 2026-10-19.
- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-19.
- [Ethereum accounts](https://ethereum.org/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-19.
- [Cryptography](https://csrc.nist.gov/glossary/term/cryptography) — National Institute of Standards and Technology; retrieved 2026-10-19.
- [Sign Transactions on EVM Chains](https://developers.circle.com/wallets/sign-tx-evm) — Circle; retrieved 2026-10-19.
