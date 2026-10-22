---
title: "Onchain data: What blockchain records show and what they do not"
description: "Learn what onchain data records, how it can describe blockchain activity, and why visible transactions do not by themselves establish identity, intent, or context."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["onchain_data_analytics"]
tags: []
author: "editorial_team"
primary_keyword: "onchain data"
owned_question: "What does onchain data represent, what can it reveal about blockchain activity, and what are its interpretive limits?"
risk_level: "medium"
---

Onchain data is information recorded in, or associated with, blockchain activity and state. It can describe what a network recorded, such as transactions or changes to contract data, but the record alone does not identify the people behind addresses, establish their intent, or explain the full real-world context. For builders, operators, and business decision-makers, the key is to separate protocol observations from conclusions that require evidence beyond the ledger.

## What onchain data means

A blockchain is a shared digital record maintained according to the network’s rules. In normal operation, a blockchain network enables a community to record transactions in a shared ledger whose published records cannot simply be changed. This describes how the ledger operates; it does not mean that every relevant fact about an event is recorded or that a ledger entry explains itself. ([source](<https://csrc.nist.gov/pubs/ir/8202/final>))

“Onchain data” is a broad term for information represented in a blockchain’s records and state. Protocol-recorded information concerns activity the network processes or stores. Offchain information concerns facts that are not established merely by a ledger entry—for example, who controlled an address, what an organization intended, or what agreement surrounded an action. A record and its real-world interpretation are related, but they are different kinds of evidence.

There is no single record format or visibility rule for all networks. Blockchain systems differ in participation, consensus, privacy, finality, and governance. Accordingly, what a reader can observe—and what a record means—depends on the particular network and its design. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

This distinction also helps prevent a common category error: treating everything associated with a blockchain as if it were written directly into the protocol record. A presentation may include decoded labels or other information that makes records easier to discuss, but the display is not automatically the same thing as the underlying protocol data. The relevant question is which parts are direct records and which parts have been organized or interpreted.

## What a blockchain record can contain

Transactions are one important kind of onchain information. Depending on the network and transaction type, records can represent actions such as sending value or invoking contract behavior. The fields and encodings are not identical across networks, so a description of one chain’s transaction structure should not be generalized to every blockchain.

On Ethereum, a transaction can include a sender-authorizing signature, a nonce, a destination, value or contract data, a gas limit, and fee parameters according to its transaction type. This is a network-specific example: it illustrates that records can carry multiple kinds of protocol information, not that every network stores the same fields or exposes them in the same form.

Smart contracts provide another example of how records can relate to network state. An Ethereum smart contract has persistent data and executable functions at an on-chain address, and it can emit events that applications process. That description is specific to Ethereum; other smart-contract platforms can use different execution and storage models. ([source](<https://ethereum.org/developers/docs/smart-contracts/anatomy/>))

Some datasets organize blockchain information into categories such as blocks, transactions, receipts, logs, decoded events, token transfers, traces, and selected account-state records. This provides an example of the range of record types represented in a documented Ethereum mainnet analytics dataset. It does not establish that every chain or dataset contains those categories, that fields are uniform, or that all activity is publicly readable. ([source](<https://docs.cloud.google.com/blockchain-analytics/docs/schema>))

A further distinction is between a protocol record and a derived presentation of it. For example, an application indexing layer can transform selected blockchain records and contract events into stored entities queried through a schema. Those entities can make selected information easier to work with, but they are an application-level representation, not a universal protocol-native description of all activity. ([source](<https://thegraph.com/docs/en/subgraphs/overview/>))

## What onchain data can help describe

Onchain records can describe activity the network recorded. At the simplest level, they can show that a transaction appears in the network’s history or that contract data changed. Looking across multiple records can support a description of activity over a chosen period, as long as the observation is tied to the records and definitions actually examined.

The scope of the statement matters. “These records show activity involving these addresses during the period examined” is a descriptive observation. It does not, without further evidence, establish who controlled the addresses, why the activity occurred, or what it meant outside the network. Nor does a past record, by itself, establish what will happen in the future.

Aggregation does not remove that boundary. A summary can describe a pattern in the records selected for it, but the summary depends on what was included and how the activity was categorized. If records are grouped or labeled, those choices belong to the analysis rather than becoming facts written into the protocol. A clear explanation should distinguish the underlying observations from the interpretation layered on top.

This distinction is useful when comparing a record with a claim about value or purpose. A transaction may contain a destination or contract data, but those details do not necessarily explain the commercial, personal, or operational reason for the action. Onchain information can provide evidence about network activity; it does not automatically supply an account of the surrounding event.

## What the records cannot establish on their own

A wallet or address does not, by itself, establish a person’s or organization’s identity. The address is part of the record; attributing it to a real-world actor is a separate conclusion that requires evidence beyond the address’s appearance onchain. A label attached to an address may communicate an interpretation, but readers should not mistake that label for a protocol fact unless its basis is established.

Likewise, a transaction record alone does not establish intent or the offchain purpose of a transfer. The record can document activity under the network’s rules, but it does not necessarily explain the circumstances, authority, or agreement around that activity. Those questions require additional context and appropriate supporting evidence.

Interpretation may also be complicated by shared custody, intermediaries, privacy features, or incomplete context. A visible transaction might reflect an arrangement that cannot be reconstructed from the transaction alone. Network differences further limit broad assumptions about what is observable. The available evidence supports caution, not a universal rule about what any particular address or pattern represents.

For the same reason, an observed pattern is not proof of wrongdoing and should not be presented as a reliable prediction. A record of network activity is not automatically proof of a real-world motive, business outcome, or future consequence. Conclusions should remain proportional to what the records and any additional evidence actually support.

## How to read onchain claims cautiously

When evaluating a claim based on onchain data, first identify the network and the kind of record being discussed. Ask what period was examined and what assumptions shaped the description. A claim about selected records on one network should not quietly become a claim about every blockchain or all activity.

Next, separate direct protocol observations from labels, estimates, and analyst interpretations. Ask whether a statement describes a field or state change in the record, or whether it assigns an identity, purpose, or significance to that observation. If the claim depends on grouping or labeling, the method and assumptions should be treated as part of the interpretation.

Finally, match the conclusion to the evidence. Onchain records can help describe activity recorded by a network. They do not, on their own, establish identity, intent, or the full offchain context. For conclusions that depend on those matters, seek independent and appropriate evidence rather than treating the ledger as a complete account of the real-world event. Keeping this boundary clear makes the record useful without asking it to prove more than it shows.

## Sources and references

- [Blockchain Analytics Dataset Schemas](https://docs.cloud.google.com/blockchain-analytics/docs/schema) — Google Cloud; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Anatomy of smart contracts](https://ethereum.org/developers/docs/smart-contracts/anatomy/) — ethereum.org; retrieved 2026-10-19.
- [Subgraphs](https://thegraph.com/docs/en/subgraphs/overview/) — The Graph Documentation; retrieved 2026-10-19.
