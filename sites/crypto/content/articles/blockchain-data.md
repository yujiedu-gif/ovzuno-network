---
title: "Blockchain data: what it includes and how to understand it"
description: "Learn what blockchain data includes, from transactions and events to state, and how recorded onchain information differs from decoded or interpreted data."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["onchain_data_analytics"]
tags: []
author: "editorial_team"
primary_keyword: "blockchain data"
owned_question: "What does blockchain data include, and how does it differ from indexed or interpreted data about blockchain activity?"
risk_level: "medium"
---

Blockchain data is information recorded by or made available through a blockchain network. It can include transactions, transaction-related fields, contract records, and changes to network state. The term also gets used for decoded, indexed, or interpreted versions of those records—but those are derived views, not necessarily data written in that form by the protocol.

## What blockchain data means

A blockchain can be described as a database shared across networked computers, where blocks cryptographically reference earlier blocks and nodes use consensus to agree on state. The records and rules that make up this shared history vary across blockchain designs, including their participation, consensus, data visibility, finality, and execution capabilities. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

In everyday usage, “blockchain data” may refer to several layers: protocol records, values obtained from those records, and conclusions drawn by software or people. The distinction matters because a transaction record is not the same thing as a human-readable label or an explanation of what the transaction means.

## What information can appear in blockchain data

Transactions are one central category. A transaction can carry information that a network uses to authorize and process an action. For example, an Ethereum transaction includes a sender-authorizing signature, nonce, destination, value or contract data, gas limit, and fee parameters according to its transaction type. Those fields describe Ethereum transactions; other networks use different formats and fields. [source](<https://ethereum.org/developers/docs/transactions/>)

Records can also refer to existing network objects. In Bitcoin, for example, an outpoint identifies a particular output from a prior transaction using that transaction’s hash and the output’s index. This is a Bitcoin-specific way to refer to an output, not a universal transaction format. [source](<https://developer.bitcoin.org/reference/transactions.html>)

Blockchain data may also be discussed in terms of state: information representing the network’s current condition, such as records associated with accounts or contracts. What that information looks like, and how the protocol exposes it, depends on the network. An application may also represent contract activity through events or other records, but the details should not be assumed to match across protocols.

The practical takeaway is that “blockchain data” is a broad category rather than one standardized dataset. A field, record type, or representation found on one network may have no direct equivalent on another.

## Recorded data is not the same as interpreted data

Protocol-level data consists of records and values defined by a network’s rules. Decoding translates a protocol-specific representation into a more readable form. Indexing organizes selected records so an application can query them. Interpretation goes further: it assigns a meaning, classification, or conclusion to those records.

For example, a Subgraph is an application indexing layer that extracts and processes blockchain data into stored entities that applications can query through GraphQL. Those entities form a derived view of selected records; they are not a universal protocol-native data format. [source](<https://thegraph.com/docs/en/subgraphs/overview/>)

Labels and behavioral conclusions require particular care. A record associated with an address does not, by itself, establish the real-world identity of whoever controls that address or their intent. A classification may depend on external information, analytical choices, or assumptions. Treat such conclusions as interpretations, and ask what evidence and method support them rather than treating them as protocol facts.

## How blockchain data is used as an input

Builders, analysts, and operators may use blockchain records as inputs to applications, research, reporting, or operational monitoring. The right representation depends on the question: a protocol record may be appropriate when checking what the network recorded, while a decoded or indexed view may be easier to use when an application needs a particular field or entity.

These layers should not be conflated. A decoded value depends on the decoder’s interpretation of a protocol format; an indexed dataset reflects the records selected and organized by its indexing system; and an analytical conclusion depends on the methods used to interpret that dataset. None should automatically be treated as a complete account of all network activity.

## Limits readers should keep in mind

Formats, available records, and network rules differ. Even where two systems expose information that appears similar, it may not have the same meaning or be directly comparable. The evidence here does not establish that any particular dataset is complete, current, or suitable for a specific decision, so verify those qualities for the network and use case at hand.

It also helps to ask where a statement sits in the data chain: Was it recorded by the protocol, decoded from a protocol-specific value, organized by an indexer, or inferred by an analytical method? That distinction clarifies what can be checked against network records and what depends on an external system or judgment.

Finally, blockchain records alone do not settle questions such as real-world identity, intent, legal or tax treatment, or compliance. Those questions require evidence and context beyond the general definition of blockchain data. For a closer look at collection and analysis, see *analytics on blockchain*; for indexing methods and query access, see *blockchain data indexing*.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Transactions Reference](https://developer.bitcoin.org/reference/transactions.html) — Bitcoin Developer Reference; retrieved 2026-10-19.
- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-18.
- [Subgraphs](https://thegraph.com/docs/en/subgraphs/overview/) — The Graph Documentation; retrieved 2026-10-19.
