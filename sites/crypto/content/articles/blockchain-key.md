---
title: "Blockchain key: public and private keys explained"
description: "Learn what a blockchain key is, how public and private keys differ, and how cryptographic signatures authorize transactions without exposing a private key."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["wallets_custody"]
tags: ["key blockchain"]
author: "editorial_team"
primary_keyword: "blockchain key"
owned_question: "What is a blockchain key, and how do public and private keys support control and authorization in a crypto wallet?"
risk_level: "medium"
---

A blockchain key is cryptographic data used in a blockchain system to support actions such as authorizing a transaction. A private key is secret signing information; a corresponding public key can support verification. A key is not the wallet, the wallet address, or the digital asset itself, and the details differ across blockchain systems.

## What a blockchain key means

A key is information used by a cryptographic system. In a blockchain context, keys can support the authorization and verification of transactions. The blockchain is the shared ledger: it records transactions and uses network rules to maintain an agreed state. The key is not that record or the asset represented by it.

The word “blockchain” covers systems that differ in their participation, consensus, visibility, and execution models. As a result, key terminology and how keys relate to other identifiers can vary. This article describes the common public-key distinction without treating one chain’s implementation as universal.

A wallet is also a separate concept. It is a tool or service associated with managing or using keys and blockchain addresses; it is not itself a key. Likewise, an address is not necessarily identical to a public key. The relationship depends on the protocol and the way it represents or derives identifiers.

## How public and private keys differ

A private key is secret information used to create a cryptographic signature. A public key is information that a relevant system can use to verify a signature or, depending on the protocol, to derive a related identifier. The two have different roles: the private key is kept secret, while public information can be used for verification.

Do not assume that every address is simply a public key written in another format. In Ethereum’s externally owned account model, for example, an account is controlled by the private key corresponding to its cryptographic address. That example describes Ethereum’s account model; it should not be generalized into a claim that all blockchain addresses and public keys are identical.

A valid signature can support the conclusion that the signing key authorized a particular transaction under the applicable protocol. It does not, by itself, identify the person, organization, device, or service controlling that key. The cryptographic relationship is about keys and signatures, not a direct identification of a human being.

## How a private key authorizes a transaction

At a high level, a transaction is prepared as data, a signature is created using private-key material, and the network checks the signature according to its protocol rules. If the transaction passes the relevant checks and is accepted under the network’s process, it can become part of the ledger’s transaction history.

The signature allows the network to check authorization without the transaction publishing the private key itself. The key remains secret; the signature is the information used in the authorization check. The exact transaction fields and validation steps depend on the blockchain and transaction type.

A valid signature has a limited meaning. It supports key-control attribution for that transaction, but it does not prove who operated the key. Nor does signature validity alone establish that a transaction will be confirmed, that it is lawful, or that it can be reversed. Those questions involve network rules and circumstances beyond the signature’s cryptographic role.

## Keys, wallet addresses, and custody

Wallet software or a wallet service may manage or use key material and work with blockchain addresses. The interface a person sees is not itself the private key. Some systems also separate signing from broadcasting: the key-related operation authorizes data, while another component may submit it to a network. Which components perform these tasks depends on the particular wallet and service design.

In a self-managed arrangement, the user controls the key material needed to authorize activity. In a custodial arrangement, a third party may manage access to private keys on a customer’s behalf. These descriptions concern control arrangements, not a universal legal classification: custody structures and customer rights can vary by provider and jurisdiction.

A related example shows why “key” does not mean “complete access to everything.” Monero’s private view key can be shared to let another party identify incoming transactions for an account without granting the spend key. The documented view-key model does not reliably reveal all outgoing transactions, so it should not be treated as complete balance or activity proof. This is a protocol-specific visibility example, not a general rule for blockchain keys.

## What key control does—and does not—establish

Key control matters because a valid signature can show that the corresponding signing capability was used to authorize a transaction. But that fact should not be stretched into broader conclusions. A signature alone does not establish the key controller’s identity, prove legal ownership, or guarantee that assets can be recovered. The legal and operational effects depend on the arrangement and circumstances, not just on the cryptographic key.

The practical meaning of “control” also depends on the wallet and custody design. A person may interact with a wallet interface while a service administers the signing keys; another design may place key control with the user. Do not infer who controls the key solely from an address or an interface. The key distinction to remember is narrower: private keys are secret signing material, public information supports verification or related protocol functions, and a wallet is the system through which those keys may be managed or used.

## Sources and references

- [Ethereum accounts](https://ethereum.org/developers/docs/accounts/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [View Key](https://web.getmonero.org/resources/moneropedia/viewkey.html) — Monero Project documentation; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
