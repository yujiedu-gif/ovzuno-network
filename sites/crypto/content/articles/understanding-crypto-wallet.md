---
title: "Understanding crypto wallet: keys, addresses, and custody"
description: "Understanding crypto wallet basics: see how wallet software, keys, addresses, blockchain records, and custody relate, without confusing a wallet with stored coins."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["wallets_custody"]
tags: []
author: "editorial_team"
primary_keyword: "understanding crypto wallet"
owned_question: "What does a crypto wallet do, and how do keys, blockchain addresses, and custody relate to one another?"
risk_level: "medium"
---

A crypto wallet is software or a service that manages cryptographic keys and helps interact with blockchain networks; it does not generally store coins as files. Keys are used to authorize certain actions, while the blockchain records activity according to its own protocol. Who controls the keys—and how access or recovery works—depends on the custody arrangement.

## What a crypto wallet does

A wallet provides a way to manage or use cryptographic keys in connection with a blockchain. Its functions depend on the wallet’s design and the networks it supports. A wallet may help prepare an action, authorize it with a key, or display information associated with blockchain activity. Those functions do not mean that the wallet itself contains the digital assets.

A useful distinction is between the wallet interface and the underlying record. The wallet is the tool through which a person or service interacts with key material and network functions. The blockchain network maintains its own records under its protocol. The U.S. Securities and Exchange Commission’s educational explanation describes a crypto wallet as generally storing private keys or passcodes used to access and authorize crypto assets, rather than storing the assets themselves.

The word “wallet” can refer to different things in practice: an application, a service, or a broader arrangement involving key management. Those are not interchangeable with the keys themselves, the address associated with an account, or the blockchain record. Keeping these concepts separate helps avoid assuming that a screen showing an asset is where that asset is held.

## Understanding crypto wallet keys and addresses

A cryptographic key is information used in cryptographic operations. A **private key** is the secret part used to authorize an action in systems that rely on digital signatures. A corresponding public-facing identifier can be used by a network to associate activity with an account or address. The exact relationship depends on the blockchain’s design, so it is better not to treat every network’s address model as identical.

For example, in Ethereum’s externally owned account model, an account is controlled by the private key corresponding to its cryptographic address. A valid signature can support attribution of key control for a transaction, but it does not, by itself, identify the human, organization, device, or service controlling that key.

An address is therefore not the same thing as a wallet or a private key. It is a network-facing identifier used in the relevant blockchain’s account or transaction model. A wallet may manage keys associated with one or more addresses, depending on its design; the address alone is not the secret that authorizes a signed action.

This distinction also limits what can be inferred from a transaction. A cryptographic signature can show that the required signing key was used under the protocol. It does not establish who used it, why they acted, or whether the action was appropriate. Key control is a technical relationship, not a complete account of identity or intent.

## Where blockchain records fit

The blockchain is the network’s recordkeeping system, not a file cabinet inside the wallet. A blockchain can be described as a database shared and updated across networked computers, with nodes using consensus to agree on state. Designs differ in how they participate, reach agreement, expose data, and execute actions; a general explanation should not imply that every chain records or processes activity in exactly the same way.

In a digital-signature-based system, a wallet may use a private key to authorize a transaction. Bitcoin’s original design, for example, uses digital signatures to authorize transfers through a chain of signed ownership records. Signatures are one part of the mechanism: the network also needs rules for validating transactions and preventing the same digital unit from being spent more than once.

After an action is submitted, the wallet may present information about it, but the network’s records and protocol determine its status. What a wallet displays depends on the network data it receives and how its software interprets that data. A displayed balance or transaction summary is thus a user-facing representation, not the blockchain record itself. The wallet and the network have related but distinct roles: one manages or uses keys and presents information; the other maintains records under its rules.

## Who holds the keys: custody in context

**Custody** describes who controls access to the keys used to access or authorize activity involving crypto assets. In a self-custody arrangement, the user controls the private keys and recovery material needed to access the assets. In a third-party custody arrangement, a custodian manages access to private keys on customers’ behalf. These are different control models, not merely different-looking wallet screens.

The distinction matters because access and recovery depend on the specific arrangement. Key-management practices can cover generation, storage, distribution, use, recovery, revocation, and destruction of key material. But naming these functions does not establish what any particular wallet or custodian provides. The documented procedures, responsibilities, and terms of the arrangement determine what access and recovery options exist.

Neither model should be treated as a guarantee that access will always be secure or recoverable. A signature can establish key use under a protocol, but it cannot establish that the key holder is the rightful person or that the action can be reversed. Likewise, the presence of a wallet interface does not show who controls its keys. The relevant question is how the arrangement assigns control and what happens if access is lost or disputed.

## Questions to resolve before relying on a wallet

Use these questions to clarify the setup, rather than assuming that all wallets work alike:

- **What does the wallet support?** Check current documentation for the specific software or service and the networks and assets it supports. Support is product- and network-specific; do not infer that a wallet handles every asset or chain.
- **Who controls the keys?** Establish whether the user or a third party controls the keys, and distinguish that technical control from any separate claim about identity or ownership.
- **What access and recovery procedures are documented?** Look for the arrangement’s actual procedures and limits. The existence of a recovery function should not be assumed from the word “wallet.”
- **Which records come from the network, and which are wallet displays?** Separate the blockchain’s protocol-defined record from a wallet’s software-generated presentation of that information.
- **What other requirements apply?** Fees, taxes, legal obligations, security practices, and compliance requirements depend on the specific network, service, jurisdiction, and circumstances. This conceptual explanation does not establish those requirements; consult current authoritative information relevant to the situation.

The core model is straightforward: a wallet manages or uses keys, an address identifies an account or destination in a network-specific way, and the blockchain maintains records under its protocol. Custody identifies who controls the keys. Keeping those roles distinct makes it easier to understand what a wallet does without mistaking an interface for the asset or the ledger.

## Sources and references

- [Key Management Guidelines](https://csrc.nist.gov/Projects/Key-Management/Key-Management-Guidelines) — NIST Computer Security Resource Center; retrieved 2026-10-19.
- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
