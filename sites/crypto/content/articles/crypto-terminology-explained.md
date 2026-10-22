---
title: "Crypto terminology explained: a practical glossary of infrastructure terms"
description: "Crypto terminology explained through a practical glossary of assets, networks, protocols, and transactions, with context for interpreting ambiguous terms."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["crypto_assets_protocols"]
tags: ["crypto terminology"]
author: "editorial_team"
primary_keyword: "crypto terminology explained"
owned_question: "What do common crypto infrastructure terms mean, and how should readers distinguish terms that describe assets, networks, protocols, and transaction processes?"
risk_level: "medium"
---

Crypto terminology is easiest to interpret when you first identify what a word describes: an asset, a network, a protocol, a service, or a process. Then check whether the wording is a formal specification or an informal label, and use documentation for the specific system when the distinction matters. The same term can describe different designs in different networks, so a glossary gives orientation—not proof of an asset’s legal status, backing, safety, or recoverability.

## How to read crypto terminology in context

Start by locating a term’s role in the material. Is it naming something recorded, such as a balance or transfer? A system that communicates and agrees on records? A set of rules? Or a service that connects users to the system? These categories help prevent a description of one component from being mistaken for a claim about the entire arrangement.

Next, separate technical definitions from casual or promotional usage. A technical document may define a term narrowly for one protocol, while a business document may use it more broadly. Do not assume that a familiar label guarantees identical operation across networks.

When the meaning affects an integration, transaction, or operational decision, consult documentation for the named protocol and version. Look for what the system actually records, which participants perform each step, and what assumptions the design makes. If a document does not identify those details, treat the wording as ambiguous rather than filling in the gaps from the label alone.

## Asset and ledger terms in crypto terminology

A **ledger** is a record of activity or state. In an application, it is useful to distinguish the record from the thing a reader believes the record represents. A ledger entry may describe a transfer or an ownership association; that entry alone does not establish what rights exist outside the system.

An **account** is a system-specific way to represent a participant or its state. An **address** is an identifier used within a particular network or application. Do not assume that an address has the same role or format everywhere. For example, Monero’s stealth-address design lets a sender create a one-time destination address so incoming payments are not directly linked onchain to the recipient’s published address. This protocol-specific use illustrates why the word “address” needs context.

A **transaction** is an operation submitted to a system to request a change, such as transferring value or invoking a function. The word can also refer informally to a record showing that operation. In either usage, check which stage the document means: request, processing attempt, or recorded result. A transaction label by itself does not establish that a requested outcome has been completed.

The practical distinction is between an on-network record and the underlying asset, service, or claim being discussed. A ledger can record information about an arrangement, but the record’s meaning depends on that arrangement’s rules and surrounding systems. Avoid treating a technical label as evidence of legal ownership, redemption rights, or backing.

## Networks, protocols, and standards

A **network** is the set of connected participants and systems that exchange information or coordinate activity. A **node** is a running instance of protocol client software connected to peers; its behavior depends on its client and configured mode. This means the word “node” does not, by itself, specify every task that a particular machine performs.

A **protocol** is the rule set that defines how participating software communicates or behaves. A **consensus mechanism** refers to the system’s way of coordinating agreement about network updates, but the exact design is protocol-specific. These terms describe infrastructure rules; they do not tell you, without further detail, who operates a service or controls an application interface.

A **standard** or **interface** specifies conventions that compatible implementations can follow. It is not necessarily a complete application or a guarantee about how a particular service uses the interface. When a document cites a standard, check the implementation and deployment it refers to, rather than assuming every feature or operational responsibility is covered by the standard.

The distinction also matters when reading about scaling systems. A **rollup**, in one common Ethereum-oriented usage, separates transaction execution from the base layer while publishing data to Ethereum, where base-layer consensus establishes the published record. But terminology is not uniform: under L2BEAT’s terminology, a rollup uses Layer 1 for consensus and data availability, while systems publishing data elsewhere add external data-availability assumptions and are classified differently. When a source uses “Layer 2,” inspect the architecture it describes instead of relying on the label alone.

## Transaction processing and network operation

Transaction vocabulary often compresses several stages into one phrase. **Submission** means that an operation has been sent to a network or service. **Validation** refers to checking it against applicable rules. **Confirmation** is commonly used to describe its inclusion or continued recognition by a network, but the relevant convention depends on the system. **Settlement** refers to the point at which an obligation is treated as completed under the applicable process or policy.

These terms should not be treated as synonyms. A business workflow may require a particular network condition or an additional operational check before it regards a transaction as settled. Read the system’s documentation and the organization’s own process description to determine what evidence each stage requires.

Likewise, **finality** and **confirmation** do not have one universal definition or threshold across crypto systems. A term may refer to a protocol’s own treatment of recorded history, or to an application’s decision about when to act. If an important action depends on a transaction, identify which meaning the relevant documentation uses rather than assuming all systems use the same convention.

Fees, throughput, and availability are also operating conditions, not fixed definitions of a network. Their values and behavior depend on the network and circumstances. A glossary can explain what “fee” means in context, but it cannot supply a universal cost or performance expectation. Consult current, system-specific information for a live operational decision.

## Terms that require extra context before use

Some words carry technical, business, and legal meanings that should be kept separate:

- **Custody**: Ask who controls the relevant keys or access, and what the service arrangement says. The word alone does not establish a particular customer right or recovery outcome.
- **Bridge**: Identify which systems are connected and how the design verifies activity across them. “Bridge” names a category of cross-system mechanism, not one uniform architecture.
- **Stablecoin**: Treat the name as a description that needs an identified reference and stabilization mechanism, not proof of a particular backing arrangement or value.
- **Decentralization**: Ask which component is being described and who operates or controls it. A claim about one component should not be generalized to the whole system.

For each term, separate what the technology records or does from what a provider, application, operator, merchant, or user is responsible for. The protocol may define a transaction or verification rule; an application may decide how to present it; an organization may set its own operating threshold. Those are different claims and should be checked in the relevant materials.

Finally, technical descriptions do not settle legal, tax, or compliance interpretations. Those depend on jurisdiction and context. When such an interpretation matters, use current authoritative sources for the relevant jurisdiction and avoid treating a technical glossary entry as a legal conclusion. The most reliable reading method is simple: identify the component, find the system-specific definition, and confirm which responsibilities and assumptions the document actually assigns.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Stealth Address](https://web.getmonero.org/resources/moneropedia/stealthaddress.html) — Monero Project documentation; retrieved 2026-10-18.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients) — ethereum.org; retrieved 2026-10-18.
