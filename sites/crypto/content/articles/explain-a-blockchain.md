---
title: "Explain a Blockchain: A Clear Definition and Basic Process"
description: "Explain a blockchain in plain language: learn what a shared ledger is, how transactions are checked and recorded, and what the basic definition leaves out."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "definition"
topics: ["blockchain_payment_foundations"]
tags: ["explain blockchain"]
author: "editorial_team"
primary_keyword: "explain a blockchain"
owned_question: "What does it mean to explain a blockchain: what it is, how it records and verifies transactions, and what its basic limits are?"
risk_level: "medium"
---

A blockchain is a shared digital ledger that participating computers update according to a network’s rules. Transactions are checked, accepted updates are linked into an ordered history, and participants consult or maintain ledger copies. The specific rules and participants vary by blockchain, so the term alone does not establish how open, decentralized, or secure a network is.

## What does “explain a blockchain” mean?

A blockchain is a kind of database for recording transactions. Its defining idea is not simply that data is stored online, but that participants follow a protocol—a set of rules—for proposing, checking, and agreeing on updates to a shared record. In Ethereum’s description, nodes use a consensus mechanism to agree on new blocks and the continuing chain. That is one concrete example; consensus mechanisms differ across networks. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The ledger is the recordkeeping system. It is distinct from digital assets or applications that may use the network. For example, an Ethereum smart contract can be part of an application that interacts with blockchain state, but the contract or application is not the ledger itself. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Blockchain designs also differ in who can participate and how agreement is reached. The word “blockchain” by itself does not mean every network is public, permissionless, or decentralized to the same degree. To describe a particular system, identify its participants and the rules by which it accepts updates rather than assuming those properties from the label.

## How a blockchain records a transaction

A basic transaction flow can be described in five steps. The details are system-specific, but the sequence helps explain the shared-ledger idea:

1. **A participant proposes an update.** A user or application submits a transaction for the network to consider. The network’s design determines how it is submitted and which participants handle it.
2. **The system checks it.** Relevant participants evaluate the transaction against that network’s rules and the ledger state they are using. In Ethereum, a full node independently verifies blocks and transactions against protocol rules rather than relying entirely on another node. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)
3. **Valid proposals are assembled into an update.** In many blockchain explanations, a group of transactions is described as a block. The exact construction and handling of proposed updates vary by protocol; this article does not prescribe one network’s procedure.
4. **Participants agree on the accepted history.** A consensus or approval process determines which update becomes part of the shared record. Ethereum nodes, for example, use a consensus mechanism to agree on new blocks and the continuing chain. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)
5. **Ledger copies reflect the accepted update.** Participants then consult or maintain records according to the system’s design. A blockchain node is a running instance of protocol client software connected to peers; its behavior depends on its software and configured mode. [source](<https://ethereum.org/developers/docs/nodes-and-clients>)

This flow distinguishes proposing a transaction from having it accepted into the network’s history. A submission is a request to update the record; whether and how it is accepted depends on the applicable validation and agreement rules.

## What makes blockchain records linked and verifiable?

In a blockchain, blocks commonly refer cryptographically to earlier blocks, creating an ordered chain. Ethereum’s block description provides one example: a block references its parent block cryptographically, linking it to the preceding network state. [source](<https://ethereum.org/developers/docs/scaling/>)

That link makes earlier changes detectable through the system’s verification rules: if data changes, the relationship between linked records may no longer validate. This is a tamper-evident structure, not a universal promise that records can never be changed or that every possible participant will detect every issue. The way a network validates updates and resolves competing histories depends on its protocol.

The distinction matters: cryptographic links help organize and check the record, while the network’s rules determine which updates participants accept. The presence of linked records alone does not tell a reader how a specific system handles disagreements or changes to its rules.

## What a blockchain explanation does—and does not—tell you

A basic definition explains a recordkeeping model, not every property of a particular network. The participants, validation rules, and consensus design determine how updates are proposed and accepted. Even the term “consensus mechanism” needs care: in Ethereum’s explanation, proof of work is a component used alongside validation, networking, incentives, and a fork-choice rule, rather than the entire agreement process by itself. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

So, calling something a blockchain does not by itself guarantee that its transactions are correct, that its records are private, that the system will always be available, or that recovery will work in a particular way. Nor does a shared ledger alone establish who governs the network or how governance decisions are made. Those questions require information about the specific system.

For an implementation-level decision, review the relevant network’s documentation and identify its participants, validation process, and method for accepting updates. The concise definition is: a blockchain is a shared ledger whose participants use system-specific rules to check and agree on updates, which are commonly linked into an ordered history.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients) — ethereum.org; retrieved 2026-10-18.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
