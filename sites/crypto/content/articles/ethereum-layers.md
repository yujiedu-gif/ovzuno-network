---
title: "Ethereum layers: how the architecture fits together"
description: "Learn what Ethereum layers mean, how core protocol functions differ from scaling designs, and why layer labels alone do not establish shared security."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "ethereum layers"
owned_question: "What does “Ethereum layers” mean, and how do the execution, consensus, and scaling layers relate to one another?"
risk_level: "medium"
---

Ethereum layers is a broad way to describe how technical responsibilities are divided between Ethereum’s core protocol and systems built around it. Execution and consensus are complementary parts of Ethereum’s core; scaling designs may move some activity elsewhere and connect back to Ethereum, but the word “layer” alone does not establish a system’s security or recovery properties.

## What “Ethereum layers” means

A layer is a useful architectural description of a component’s role in a larger system. It is not, by itself, proof that every project uses the same formal taxonomy or that components bearing the same label work alike. The practical question is what each part does and how it interacts with the others.

An Ethereum application stack can include blockchain nodes and smart contracts alongside client libraries, wallets, front-end interfaces, data indexing, storage, and other off-chain services. Those pieces may support one application, but they do not all perform the same function. A wallet, for example, is not the same component as the blockchain protocol, and an application interface is not the same component as an on-chain contract. A useful architecture description identifies these roles rather than grouping every dependency under a single label.

This distinction also helps clarify terms such as “base layer” and “scaling layer.” They can indicate a relationship in a particular design, but the label does not tell you exactly where transactions are processed, what information is available for verification, or which system determines a final result. Those details need to be established from the architecture of the specific system.

## Execution and consensus in Ethereum’s core protocol

Execution is the processing of transactions and their effects on blockchain state. Ethereum smart contracts, for example, are programs with code and data at network addresses that users can invoke by submitting transactions. When a transaction changes state, participating nodes must derive the same result under the network’s rules; execution results are then recorded on the blockchain. This deterministic behavior is part of how a shared state can be maintained across participants.

Consensus performs a different, connected job: coordinating agreement about the chain’s history. Ethereum nodes use a consensus mechanism to agree on new blocks and the continuing chain. Ethereum’s proof-of-stake design combines validator attestations, a fork-choice rule, and checkpoint finality under protocol-defined supermajority conditions. Those elements describe Ethereum’s own consensus design; they should not be assumed to describe every system that uses Ethereum or calls itself a layer.

Execution and consensus are not independent networks that a user selects between when interacting with Ethereum. Execution determines the effects of transactions under protocol rules; consensus coordinates which blocks and resulting history the network accepts. Keeping the functions distinct helps explain the protocol, while recognizing that they work together to maintain it.

The distinction between a protocol role and its implementation matters, too. Ethereum protocol change involves proposal, technical review, implementation, coordination, and adoption across network stakeholders. So an architectural diagram is not a complete account of the system: it describes technical responsibilities, while software and coordination processes are additional parts of how those responsibilities are carried out.

## How Ethereum layers relate to scaling designs

Scaling work seeks to increase transaction speed and throughput without sacrificing decentralization or security. That statement describes a design objective, not a result guaranteed for every system or operating condition. Scaling designs can handle some activity outside Ethereum and communicate relevant information or results back to it, but the details differ.

For example, a general zero-knowledge rollup pattern moves execution and state storage off-chain while submitting state-change summaries and cryptographic validity proofs to Ethereum. In that pattern, a base-layer verifier contract accepts a proof for a proposed state transition. This describes a technical pattern, not a conclusion that every system using the rollup label has identical properties or that the complete system is free of other assumptions.

Some Ethereum Layer 2 solutions derive some security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. The word “some” is important: the exact guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. A connection to Ethereum therefore does not, by itself, establish that all system functions rely on Ethereum or that its security properties match the base protocol’s.

Several design questions should be considered separately:

- **Execution:** Where are transactions processed, and which rules determine their effects?
- **Data availability:** Can network participants obtain the transaction data needed to independently verify summarized state changes, even if they do not process all data in the same way?
- **Settlement:** Where are results recorded or resolved, and what does that record establish?
- **Proof or dispute process:** How does the design check a proposed state change, or allow a claim to be challenged?

A particular architecture may assign these functions differently. Knowing that execution happens outside Ethereum, for instance, does not tell you where data is made available or how the system handles a disputed result. Each part needs to be checked independently against the system’s documentation.

## What a layer label does—and does not—tell you

A layer label alone does not establish decentralization, security, data availability, or withdrawal guarantees. Even a statement that a design derives some security from Ethereum is conditional on the specific mechanisms involved. Avoid extending a narrow claim about one proof or connection into a conclusion about the full system.

To interpret a design, first identify which functions Ethereum itself performs and which are handled elsewhere. Then examine the documented proof, data-availability, settlement, governance, and exit mechanisms. Ask what the evidence supports and what assumptions remain. A category name or general description of intent cannot substitute for that system-level account.

Claims about performance, fees, and availability also require evidence tied to the particular implementation and time period. They cannot be inferred from the term “layer” or from the general objective of scaling. This overview does not compare individual networks or provide current operating estimates.

## Questions to check before evaluating a specific design

A bounded technical review can start with these questions:

- Which functions does Ethereum perform, and which are assigned to another protocol, operator, or service?
- Where does execution occur, and what data, summaries, or proofs are submitted to Ethereum?
- What mechanism supports the stated security assumptions, and what does it leave dependent on other components?
- How does the documented design address data availability, settlement, and exit or recovery paths?
- Are claims about fees, performance, or availability supported by current evidence for that specific system?

Regulatory, tax, custody, and compliance conclusions are outside this technical overview. They require evidence appropriate to the relevant jurisdiction and arrangement; a technical layer label cannot answer them. The central point is to read “Ethereum layers” as a description of system roles, then examine the actual architecture to understand how those roles relate and which assumptions remain outside Ethereum’s core protocol.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to the Ethereum stack](https://ethereum.org/developers/docs/ethereum-stack/) — ethereum.org; retrieved 2026-10-19.
- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Smart contract - Glossary](https://csrc.nist.gov/glossary/term/Smart_contract) — National Institute of Standards and Technology; retrieved 2026-10-18.
