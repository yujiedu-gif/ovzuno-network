---
title: "Level 1 blockchains: core functions and scaling"
description: "Learn what level 1 blockchains do, how they handle shared network functions, and why choices at the base layer shape blockchain scaling trade-offs."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "level 1 blockchains"
owned_question: "What are level 1 blockchains, which core functions do they perform, and how do they relate to scaling?"
risk_level: "medium"
---

A level 1 blockchain—usually called a Layer 1, or L1—is a base network that maintains its own record of transactions and state under its protocol rules. Its core responsibilities can include communicating transactions, organizing them into an ordered record, and supporting agreement on accepted updates. The particular functions and how they are implemented vary by network, so the label alone does not establish a capacity figure or performance guarantee.

## What “level 1 blockchain” means

“Level 1” is commonly used to mean “Layer 1” or “base layer.” The term describes the foundational blockchain network in its own architecture; it is common usage rather than a separately standardized technical category.

A blockchain is a shared database updated across networked computers. In Ethereum, for example, each block cryptographically references its parent block, creating an ordered chain of network state. Other networks may use different data structures and consensus rules.  [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The network itself is not the same thing as an application that uses it. Applications may provide interfaces or submit transactions, while the base network applies its own protocol rules to the records and state changes it accepts. A technical explanation should keep those responsibilities distinct: the Layer 1 label does not specify every application, service, or component connected to the network.

The same caution applies to architecture. Some descriptions treat a base layer as performing several functions together; other designs assign functions to specialized layers. One modular model separates execution, settlement, consensus, and data availability, but those categories are an architectural framework rather than a universal definition of every network. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

## Core functions of level 1 blockchains

A base network needs a way for proposed transactions to reach relevant participants, a set of rules for checking those transactions, and a mechanism for deciding which blocks or state updates become part of the recognized history. These functions are related but distinct. Communicating a transaction does not establish its validity, and validating it does not alone settle which competing history the network recognizes.

Bitcoin provides one specific example of transaction and block communication. Its full nodes use a peer-to-peer protocol to exchange transactions and blocks and synchronize validated chain data. Peer discovery, relay policy, and serving behavior depend on software and configuration, so this example should not be treated as a description of every L1. [source](<https://developer.bitcoin.org/devguide/p2p_network.html>)

Validation means applying the network’s rules to a proposed transaction or block. The checks, state changes, and data structures involved depend on the protocol. A block, in Ethereum’s case, links to its parent and contributes to an ordered chain of network state; this does not mean every blockchain uses Ethereum’s structure. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Consensus is the process by which participants coordinate on accepted blocks or state. Mechanisms differ among networks. In Bitcoin, nodes select the valid chain representing the greatest cumulative proof of work when histories compete. Proof of work does not make an invalid block valid: nodes also enforce transaction and block-validity rules. This is a Bitcoin-specific chain-selection description, not a universal rule for Layer 1 networks.

## How a base network maintains shared state

A useful conceptual sequence is: a transaction is submitted, communicated to participants, checked under the relevant protocol rules, and included in a proposed block or other network record. Participants then apply the network’s consensus and conflict-resolution rules to determine which record becomes part of the accepted history. The sequence is a high-level model; specific protocols define their own transaction lifecycle and acceptance conditions.

It also helps to distinguish protocol rules from the software and infrastructure used to carry them out. The protocol specifies what counts as valid and how competing records are handled. Client software implements those rules and communicates with peers; operators run and configure that software. Those roles can be organized differently across networks, so a description of one network’s node software should not be assumed to describe another network’s implementation.

A transaction’s submission or appearance in an interface should not automatically be described as inclusion in the network’s accepted record. The meaning of statuses such as “pending,” “included,” or “confirmed” depends on the network and the application displaying them. When reading a technical claim, check which event it refers to rather than treating communication, validation, inclusion, and acceptance as synonyms.

## Why Layer 1 design affects scaling

Scaling concerns how a network handles activity while continuing to perform the functions needed to maintain its record. Base-layer design can affect which work participants perform and how functions such as execution, consensus, and data handling are arranged. Because architectures vary, the label “Layer 1” by itself does not tell a reader how much activity a network can handle or how performance changes with a different workload.

Design choices can also change what participants are expected to check or coordinate. A description of capacity is therefore more informative when it identifies the relevant protocol behavior and workload, rather than presenting a number as an inherent property of all L1 networks. Claims about performance require transparent measurement methods and conditions; the evidence available here does not establish a universal throughput figure or a fixed scaling trade-off across networks.

Bitcoin offers an example of a protocol rule that should not be mistaken for a capacity measurement: its proof-of-work target is adjusted after each 2,016-block difficulty period using block-header timestamps and consensus rules. The exact behavior is defined by deployed network software. This describes a Bitcoin mechanism, not transaction speed, user experience, or a general feature of all base networks. [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

The distinction between functions and measurements matters. A headline figure might count submitted transactions, executed transactions, or transactions included in a record; those are not necessarily equivalent measures. A careful explanation states what is counted, the conditions under which it was measured, and which network or software version is in scope. Without those details, the number cannot be used to infer performance under every condition.

## What to check when evaluating a Layer 1 explanation

When a claim describes an L1’s operation or capacity, first check whether it names the network and, where relevant, the protocol or software version. Then look for the workload, metric, and measurement method. An advertised target, an observed result under specified conditions, and a user-facing status describe different things.

Next, identify the function being discussed. Does the claim concern transaction communication, rule-based validation, consensus, or the handling of network data? If it uses a broad term such as “processes,” check whether that means submission, execution, inclusion, or acceptance under consensus rules. Precise wording helps readers understand what the statement actually establishes.

Finally, look for assumptions and scope limits. Network architectures may combine or separate responsibilities, and a statement about Bitcoin or Ethereum should not be generalized to every Layer 1. A sound explanation makes the network and measurement conditions clear, distinguishes protocol behavior from application and operator roles, and does not turn one metric into a universal conclusion.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin Developer Documentation; retrieved 2026-10-18.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
