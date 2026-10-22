---
title: "Layer 1 Networks Crypto: Core Functions and How They Fit Into Blockchain Systems"
description: "Understand layer 1 networks crypto: what a base layer does, how it processes and records activity, and how it relates to Layer 2 systems."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["Layer 1 blockchain", "base layer", "consensus mechanism", "smart contract execution"]
author: "editorial_team"
primary_keyword: "layer 1 networks crypto"
owned_question: "What is a Layer 1 network in crypto, what functions does it perform, and how does it relate to Layer 2 networks?"
risk_level: "medium"
---

A Layer 1 network in crypto is the base blockchain and its protocol: the foundational network whose rules govern how its own activity is validated and how participants agree on the continuing record. It is not a universal design template. Consensus, node roles, and the work assigned to the base layer vary by network. Layer 2 systems handle some activity outside an underlying Layer 1, but their specific relationship with that base layer depends on their architecture. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>) [source](<https://ethereum.org/developers/docs/scaling/>)

## What “Layer 1” means in crypto

“Layer 1” is common terminology for a blockchain network’s underlying or base layer, rather than a separately standardized technical category. The term identifies a place in an architecture: the network and protocol on which other components may rely. It does not, by itself, specify a single set of technical features. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Keep the network distinct from its protocol, native currency, and applications. The protocol is the set of rules that network software follows. Nodes are running instances of software that participate in the network, while applications use network capabilities. A token associated with a network is not the network itself, and the Layer 1 label does not say what functions that token performs. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The phrase also does not guarantee that every network is open to the same participants, has the same consensus process, or supports the same application capabilities. For example, Ethereum documentation describes its nodes as using a consensus mechanism to agree on new blocks and the continuing chain. That describes Ethereum’s operation; it should not be treated as a universal specification for all Layer 1 networks. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

## The core functions of layer 1 networks crypto

At a high level, a Layer 1 provides rules for accepting activity into the network’s record. In Ethereum, full nodes independently check blocks and transactions against protocol rules rather than relying entirely on another node. This is one concrete example of a node’s validation role, not a claim that all networks use the same node design or assign validation identically. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

Validation and consensus are related but distinct. Validation means checking whether a block or transaction conforms to the applicable protocol rules. Consensus is the process by which participants coordinate around blocks and the continuing chain. Ethereum’s consensus documentation describes proof of work as one component: it provides Sybil resistance and a method for selecting block authors, alongside validation, networking, incentives, and a fork-choice rule. That distinction cautions against treating a consensus mechanism as the entire network protocol. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

A network also maintains a recognized record of activity and the state derived from it. The particulars of the state representation and the checks that govern updates depend on the protocol. For Ethereum, a node receiving a proposed block checks it and re-executes its transactions to verify the resulting state change before accepting it. This gives a specific example of how transaction execution and validation can be tied to an update, but it is not a description of every Layer 1.

Smart-contract execution is a capability of some Layer 1 designs, not a universal definition of the term. The label alone does not tell a reader whether a network supports contracts or what execution rules apply. For a particular network, consult its protocol documentation rather than inferring capabilities from the architectural name.

## How a Layer 1 reaches agreement and updates state

A simplified way to understand network activity is to follow the record it produces. A transaction is handled under the network’s rules; a block may contain activity to be recognized; and the network’s consensus process determines which blocks belong to its continuing chain. The exact processing path and acceptance criteria depend on the protocol, so this outline should not be read as a universal step-by-step implementation.

The division between checking and agreeing matters. A node’s validation role concerns whether the proposed block and its transactions follow protocol rules. Consensus concerns how the network coordinates on the accepted chain. In Ethereum, a full node independently verifies blocks and transactions, while Ethereum nodes use a consensus mechanism to agree on new blocks and the continuing chain. These are Ethereum-specific details and should not be generalized to networks with different designs. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>) [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

“Confirmation” and “finality” should also be read in the context of the named protocol. The Layer 1 label does not establish one universal confirmation threshold or finality rule. To understand what an accepted record means in a specific system, look for that network’s definitions and procedures in its documentation. Avoid substituting a wallet or application’s display status for the protocol’s own account of acceptance.

This is also where responsibility boundaries matter. The protocol defines network rules, and nodes running the relevant client software carry out their assigned functions. An application or other external component may provide a user-facing path into the network, but its interface does not itself define Layer 1 validation or consensus. When examining a system, separate what the protocol documents from what an application, provider, or other component supplies.

## Where Layer 2 fits—and where it does not

A Layer 2 is a system designed to handle some activity in connection with an underlying Layer 1. In Ethereum rollups, transaction execution is separated from the base layer while data is posted to Ethereum, where base-layer consensus establishes the published record. That is an Ethereum rollup pattern, not a universal description of every system called Layer 2. [source](<https://ethereum.org/developers/docs/scaling/>)

The distinction is functional: identify what work the Layer 2 performs and what role the Layer 1 retains. In the cited rollup model, execution is separated from the base layer, while Ethereum provides consensus over the data posted there. This does not mean every Layer 2 executes transactions the same way, publishes identical data, or relies on the same verification arrangement. [source](<https://ethereum.org/developers/docs/scaling/>)

For a specific Layer 2, check how its design handles data, state changes, and the relationship to the underlying network. The term alone does not specify those details. Keep the Layer 1’s documented responsibilities separate from the work performed by the Layer 2 or other components; do not assume that a function has moved merely because the system uses a layer label.

## A practical boundary for using the term

When a project calls a network Layer 1, treat that as an architectural description to investigate, not as a complete technical assessment. Begin with the protocol documentation and identify what it says about node roles, validation, consensus, transaction execution, and record updates. If it discusses a Layer 2 or another external system, record which functions are assigned there instead of attributing all activity to the base network.

For Ethereum, documentation describes full nodes as independently verifying blocks and transactions against protocol rules, and nodes as using consensus to agree on blocks and the continuing chain. Those facts can help explain Ethereum’s own architecture; they are not evidence that a differently designed network uses identical roles or rules. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>) [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

Treat other assertions—including claims about security, performance, availability, compliance, or recovery—as separate questions requiring evidence specific to the relevant network and system. A Layer 1 label does not establish those properties. Nor does a Layer 2 label, without details about its relationship to the base network, tell you how data, execution, or verification are handled.

The working definition is therefore simple but deliberately limited: a Layer 1 is a blockchain network and protocol serving as a base layer, with its own rules and design for network activity. Its functions must be established from that protocol, not inferred from the label. A Layer 2 may perform some activity separately while relying on a defined relationship with the base network; the details belong to the particular system’s architecture. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>) [source](<https://ethereum.org/developers/docs/scaling/>)

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
