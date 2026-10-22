---
title: "Layer1 blockchain list: networks and comparison criteria"
description: "Use this layer1 blockchain list to identify representative networks, understand what qualifies as Layer 1, and compare payment-relevant design features."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "layer1 blockchain list"
owned_question: "Which networks are Layer 1 blockchains, and how can readers compare their core architecture and payment-related capabilities?"
risk_level: "medium"
---

A Layer 1 blockchain is a base network that runs its own consensus and records or settles transactions under its own protocol rules. The evidence available for this article supports only a narrow list of architecture examples—not a current, exhaustive directory of named networks—so the entries below focus on what can be responsibly classified and compared without inferring unsupported payment performance or suitability.

## What qualifies as a Layer 1 blockchain?

For this list, “Layer 1” means a blockchain’s base layer: the network’s own rules and infrastructure establish the accepted transaction history. Consensus is the process by which the network agrees on that history; settlement is the recording of accepted transactions as part of it. These terms describe the base network, not every application or service that uses it.

A useful distinction is between a base layer and a Layer 2. A rollup, for example, separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. That dependence on another network’s consensus and data publication makes a rollup different from an independently classified base network in this comparison. The word “Layer 1” is therefore best applied by checking the architecture rather than relying on a project label alone.

The distinction does not mean that every service associated with a base network is itself part of that network. Wallets, applications, exchanges, and payment processors can provide separate functions, and their features should not be attributed to the underlying protocol without evidence.

## Layer 1 blockchain list: representative networks

This is an architecture reference, not an exhaustive inventory. The allowed evidence does not establish current network status, consensus design, or payment capabilities for a broad set of named Layer 1s. It supports the following carefully scoped examples:

- **Ethereum:** The evidence identifies Ethereum as a programmable public blockchain and describes its blocks as cryptographically referencing parent blocks, forming an ordered chain of network state. It also supports a separate distinction between Ethereum and rollups that post data to Ethereum. This establishes Ethereum as a base-layer example for this article, but does not by itself establish payment speed, capacity, fee levels, or recovery options.
- **Hyperledger Fabric:** Fabric is documented as a permissioned-network architecture organized around participating organizations, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. This is a distinct base-network model from an open public chain. The evidence does not establish that every Fabric deployment has identical permissions, settlement behavior, or payment features.

These entries are grouped by architecture rather than market value or popularity. The evidence available here does not support a broader network-by-network comparison, nor does it confirm a time-sensitive status for additional candidates. A list that added names without current, network-specific documentation would risk presenting an unverified label as a technical classification.

The list is illustrative and deliberately limited. It is not a recommendation, endorsement, or judgment about which network is more secure, reliable, active, or suitable for a particular payment flow.

## How to compare Layer 1 networks for payment use

Start with the settlement path: identify which network’s consensus establishes the transaction record, and whether another system is responsible for execution, messaging, or a later settlement step. For a base chain, inspect its own protocol documentation. For a rollup or other dependent system, identify what is posted to the underlying network and what that network actually establishes. Ethereum’s block structure, for example, links blocks into an ordered record; a rollup’s publication to Ethereum is a different architectural relationship, not proof that all rollup operations behave identically.

Next, separate protocol capabilities from application features. A network may support programmable transactions, but a payment application still determines how it constructs a transfer, presents transaction status, and handles exceptions. A wallet or service provider may add its own interface and operating rules. Do not treat those additions as universal protocol behavior.

For a practical comparison, collect evidence under these headings rather than relying on broad claims:

- **Consensus and settlement:** Which network rules determine the accepted history, and does the system depend on another chain for settlement?
- **Execution model:** Does the network support smart contracts or other programmable transaction behavior? Verify this for the specific network and version.
- **Payment flow:** Which steps occur on the base layer, and which are handled by a wallet, application, or service provider?
- **Finality and confirmation:** What does the network documentation say about inclusion, confirmation, or finality? Do not assume those terms mean the same thing across protocols.
- **Performance and fees:** Use current, network-specific evidence for any stated throughput or cost. The evidence for this list does not support numeric or comparative performance claims.

This framework helps readers ask comparable questions without declaring a winner. A technical feature documented for one network cannot be generalized to another, and an application’s user experience does not establish the base layer’s protocol guarantees.

## What a Layer 1 list cannot tell you

A category label alone does not establish security, reliability, adoption, or suitability. Even a documented architecture is not a guarantee that a particular deployment or application behaves as intended. Permission models, consensus, governance, and ledger access can differ between systems and deployments; the label “Layer 1” does not settle those questions.

Nor does inclusion establish that a network is inexpensive or fast for a particular transaction. The evidence available for this list does not support current fees, throughput figures, or comparative performance. Those claims require current, properly scoped documentation and should be assessed for the relevant network and transaction type.

A network list also says nothing by itself about token value, exchange availability, service terms, legal treatment, taxes, or compliance obligations. Those depend on facts beyond the architecture classification, including jurisdiction and the service or activity involved. This article makes no such determinations.

Finally, a protocol-level record should not be confused with a promise that a payment can be reversed or recovered. The available evidence does not establish recovery procedures for the networks listed. Any claim about reversals, custody, or customer support would need to be attributed to the relevant wallet, application, custodian, or other provider and supported separately.

## Evidence and checks before using a network

Before relying on a Layer 1 classification, check recent technical documentation that describes the network’s own consensus, execution, and settlement roles. Where a system depends on another chain, verify that relationship rather than assuming that its branding identifies its architectural layer. For a permissioned deployment, inspect the documented roles and access model for that particular network or implementation.

Treat claims about fees, yields, security, availability, or performance as separate claims requiring their own current evidence. An architecture description does not substantiate a numeric fee or a guarantee of safe operation. Likewise, do not infer that a protocol feature guarantees transaction reversal, recovery, or compliance.

For payments, map responsibilities before comparing options: the protocol determines network-level behavior; the wallet and application shape the user’s transaction flow; and any provider or merchant may set additional operational conditions. If a decision depends on jurisdiction, service availability, or a recovery process, seek evidence specific to that jurisdiction and responsible service. The result is a more useful Layer 1 comparison: clear about what the network does, careful about what it does not establish, and free of unsupported rankings.

## Sources and references

- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
