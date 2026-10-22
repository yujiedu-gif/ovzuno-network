---
title: "Cryptocurrency terms explained: a practical crypto infrastructure glossary"
description: "Cryptocurrency terms explained with concise definitions of assets, networks, protocols, wallets, keys and transactions, plus distinctions among related concepts."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: ["cryptocurrency terms"]
author: "editorial_team"
primary_keyword: "cryptocurrency terms explained"
owned_question: "What do commonly used cryptocurrency terms mean, and how do the terms relate to crypto assets, networks, protocols, and transactions?"
risk_level: "medium"
---

Cryptocurrency terminology describes different parts of a system: the asset being used, the network that records activity, the rules that govern it, and the applications that interact with it. These terms are related, but they are not interchangeable; the precise meaning can depend on the protocol or operational context.

## Core cryptocurrency terms

A **crypto asset** is a digital asset used or represented in a cryptocurrency-related system. The label is broad: it does not, by itself, specify how the asset is issued, what rights it represents, or which network records it. “Cryptocurrency” is often used more narrowly for a digital unit transferred among users of a blockchain network, but everyday and technical usage can overlap.

A **digital asset** is a general description of an asset represented in digital form. It may be recorded on or interact with a blockchain or another kind of distributed ledger. The label alone does not establish that the asset is a cryptocurrency or explain its technical or legal status.

These are working technical distinctions, not universal legal definitions. In particular, the word “crypto” in a product name or conversation does not settle how an asset should be classified for a particular purpose.

## Networks, blockchains, and protocols

A **network** is the system of connected participants and software that communicate and coordinate activity. A blockchain network is one kind of network; its participants follow rules for handling transactions and agreeing on a shared history.

A **blockchain** is a ledger whose records are linked in an ordered sequence. On Ethereum, for example, each block references its parent cryptographically, creating an ordered chain of network state. Other systems may organize records and consensus differently, so this example should not be treated as a definition of every distributed ledger.

A **distributed ledger** is a shared record maintained across distributed participants. “Blockchain” is commonly used for a particular ledger structure, while “distributed ledger” is broader terminology. The exact participation, validation, and governance model varies between systems.

A **protocol** is the set of rules and specifications that describes how a system behaves. It is not the same thing as the network that runs those rules. A protocol can define how transactions are represented or validated; participating software implements those rules, and the network coordinates the activity. An **application** is another layer: it uses network or protocol capabilities to perform a user-facing or operational task.

This distinction helps when reading technical material. A protocol specification describes intended rules; a live network consists of participants running software; an application may rely on that network and on additional services. A statement about one layer does not automatically describe every other layer.

## Coins, tokens, and smart contracts

**Coin** and **token** are common terms for crypto assets, but their use is not uniform. In many discussions, “coin” refers to an asset native to a network, while “token” refers to an asset represented through a contract or another system on a network. Treat those as common conventions, not universal rules. The distinction is useful only when the speaker’s context makes it clear.

A **smart contract** is software deployed on a blockchain or other supported execution environment. On Ethereum, a smart contract has code and data at an on-chain address and can respond to transactions under its programmed rules. A contract is not the same as the protocol or network: it operates within the environment those systems provide.

An asset can be associated with a network and transferred according to rules implemented by that network or by a contract. The word “associated” matters: cross-network designs may coordinate records through different mechanisms, such as lock-and-mint, burn-and-mint, or asset swaps. Those mechanisms do not mean an asset is physically moved from one ledger to another; the representation and accounting path depend on the design.

A **stablecoin** is an asset designed to maintain a stable value relative to a specified asset, currency, or basket. “Stable” describes the objective and mechanism, not a guarantee that market value or redemption value will always match the reference.

## Wallets, keys, and addresses

A **wallet** is software or infrastructure used to generate, manage, store, or use cryptographic keys and blockchain addresses. The word can mislead: a wallet does not necessarily contain the digital assets themselves. It provides a way to interact with the system that records them.

A **public address** is an identifier that can be used as a destination or reference in network activity. A **private key** is secret cryptographic material used to authorize particular actions. An address alone does not demonstrate that someone controls the corresponding key, and a key-control signal does not necessarily identify the person or organization operating it.

A **recovery credential** is information or a mechanism used to regain access under a particular wallet or custody arrangement. Its meaning and recovery process are specific to that arrangement; the term does not imply that access can always be restored. For operational use, identify which wallet model is involved and consult its own recovery documentation rather than assuming that all wallets work alike.

## Transactions, fees, and confirmations

A **transaction** is an instruction submitted to a network for processing. Depending on the system, it may transfer an asset, invoke contract code, or request another state change. A transaction’s fields and processing rules are protocol-specific.

To **broadcast** a transaction is to send it to network participants for consideration. Broadcasting is not the same as confirming it. A **confirmation** generally refers to evidence that a transaction has been included in the accepted history, but the way systems define inclusion, finality, and confidence differs. An application or business may also use its own completion policy, so its status labels should not be assumed to match a protocol’s terminology.

A **transaction fee** is a charge associated with processing activity under a particular network’s rules. The calculation and terminology depend on the network and transaction type; there is no single general fee amount or formula that applies to all cryptocurrency systems.

For Ethereum-family token transfers, the sender must use the same network as the recipient and hold enough native ETH for the transaction fee unless a supported sponsored-fee mechanism applies. This is an Ethereum-family operational condition, not a rule for every network.

## Terms that need context

**Custody** describes an arrangement for managing access to assets or the keys used to control them. The term can refer to different operational models, so it is important to establish who controls the keys and what the arrangement actually does before relying on a label such as “custodial.” This is a technical distinction, not a legal conclusion.

**Decentralization** is also context-dependent. A system’s description may refer to one function, such as transaction validation or governance, rather than every component a user depends on. Ask which function is being described and which network, application, or time period is in view.

Finally, keep technical descriptions separate from legal, tax, or regulatory classifications. A glossary can explain how a term is commonly used, but it cannot determine the meaning that applies to a specific asset, service, transaction, or jurisdiction. For operational decisions, verify the relevant protocol documentation and the applicable context instead of treating a familiar label as a complete specification.

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
- [How to Use Ethereum Wallets](https://ethereum.org/guides/how-to-use-a-wallet) — ethereum.org; retrieved 2026-10-19.
- [Understanding Stablecoins](https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf) — International Monetary Fund; retrieved 2026-10-18.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
