---
title: "Layer 1 Blockchain Examples: How It Works"
description: "Understand Layer 1 Blockchain Examples, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification po."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 1 blockchain examples"
owned_question: "What are examples of Layer 1 blockchains, and how do their base-layer designs differ?"
risk_level: "medium"
---

# Layer 1 Blockchain Examples: How It Works

A Layer 1 blockchain is a base protocol that maintains its own shared ledger or state and uses its own consensus rules to order and validate updates. Examples include Bitcoin and Ethereum, whose original network designs illustrate different approaches to organizing and securing blockchain history. A Layer 1 may also provide a base for other systems, but the term does not imply that every network has the same architecture, purpose, or security properties.

The most useful comparison is not a simple list of names. It is a map of what each base layer does: how it represents history, how participants agree on updates, what execution or validation happens at the base layer, and what other systems depend on it. Those details are network-specific. The accepted examples here document Bitcoin’s original design and aspects of Ethereum’s block structure and scaling model; they do not establish a complete feature comparison across all Layer 1 networks.

## What Layer 1 Blockchain Examples means

“Layer 1” refers to the base blockchain in a system’s architecture. It is where that network’s own rules establish its canonical record. The label is often used when distinguishing a base network from a Layer 2 system, which is built to process or organize activity in relation to that base.

Bitcoin’s original network design links blocks using hashes and uses hash-based proof of work to order history. Replacing history requires renewed computational work under that design. This is one documented way a base layer can link records and make competing histories costly to establish.

Ethereum offers a different example of a programmable public blockchain. Its blocks reference parent blocks cryptographically, creating an ordered chain of network state. This describes Ethereum’s block structure, not a universal rule for every blockchain: other networks can use different data structures and consensus rules.

These examples show why “Layer 1” is a category, not a single technical blueprint. A comparison should specify which feature is being discussed—such as block structure, consensus, execution, or the role of the base layer—and avoid treating a characteristic of one network as a property of all networks.

## Core components of Layer 1 Blockchain Examples

A base-layer system can be understood through several interacting components. Their specific implementation varies, so the following framework is a way to organize verification rather than a claim that every network contains identical mechanisms.

- **Ledger or state representation:** The data structure that records the network’s history or current state. Ethereum’s documented block structure links each block to its parent cryptographically. Bitcoin’s original design also links blocks with hashes.
- **Consensus and ordering:** The rules and process by which a network’s participants establish which updates belong in the accepted history. Bitcoin’s original design uses hash-based proof of work to order history. The source material here does not provide a parallel, complete account of Ethereum’s consensus rules, so a specific comparison on that dimension requires further primary documentation.
- **Execution:** The processing of transactions or other operations that change state. In a modular blockchain model described by Celestia, execution is treated as a distinct function that can be assigned to a specialized layer. That is an architectural framing, not a universal naming convention.
- **Settlement:** The function of establishing or resolving outcomes against a base layer. Celestia’s modular model treats settlement as distinct from execution, consensus, and data availability. Implementations can assign these functions differently.
- **Data availability:** Whether the information needed to inspect or verify a published record is available to relevant participants. Celestia’s documentation describes data availability as a separate function in its modular model. The term alone does not specify a network’s precise mechanism or guarantee.
- **Interfaces and dependencies:** Users and applications may interact with a network through software, services, or other layers. A Layer 2 can depend on a Layer 1 for some properties, but its exact relationship must be checked system by system.

The modular model is useful for asking which component does what. Celestia’s documentation separates execution, settlement, consensus, and data availability into functions that can be assigned to specialized layers. Other researchers and protocols may group or name the functions differently, so teams should check each project’s own definitions before comparing architectures.

## How Layer 1 Blockchain Examples works

A general base-layer workflow can be described as a sequence of questions, but the exact steps and mechanisms depend on the protocol.

1. **An operation is submitted.** A user or application creates an operation intended to update network state. The sources in this article do not specify a common transaction format or submission path across Bitcoin, Ethereum, and other networks.
2. **The network evaluates it under protocol rules.** Participants or software determine whether the operation meets the relevant rules. Which actors perform this work, and what they check, depends on the particular network.
3. **Updates are ordered into a record.** Bitcoin’s original design uses hash-based proof of work to order history. Ethereum’s blocks reference their parent blocks cryptographically, preserving an ordered chain of network state. These statements describe different documented features; they are not a full consensus comparison.
4. **The resulting record becomes a reference point for dependent systems.** In an Ethereum rollup, transaction execution is separated from the base layer while data is posted to Ethereum, where base-layer consensus establishes the published record. That describes a relationship between a particular class of Layer 2 and Ethereum, not every Layer 2 or every base chain.
5. **Users or systems rely on the published result.** The extent to which they can independently verify it depends on the information and mechanisms available to them. A block being published does not by itself describe every security, availability, or recovery property of a wider system.

This sequence should be treated as a diagnostic outline, not a protocol specification. For an actual implementation, consult its primary documentation for transaction validation, consensus participation, data publication, finality or confirmation semantics, and the interfaces through which users and applications observe state.

## Trust and control boundaries

A Layer 1’s rules and consensus process establish its own record, but a system built around it may introduce additional components and assumptions. The distinction matters when evaluating a Layer 2, a bridge, an application, or a service that presents blockchain data to users.

For Ethereum scaling systems, some Layer 2 solutions derive some of their security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. The strength and scope of that relationship depend on the particular system’s proof, data-availability, settlement, governance, and exit mechanisms. “Uses Ethereum” is therefore not enough to establish what a specific system’s security depends on.

Ethereum rollups illustrate one specific division of work: execution is separated from the base layer, while data is posted to Ethereum and the base-layer consensus establishes the published record. Rollups differ in proof system, data format, sequencing, upgrade, and bridge design. Those differences affect what a team must inspect; the general label “rollup” does not settle them.

Operational interfaces also matter. A wallet, hosted endpoint, custodian, or application can shape how a user submits or observes activity, but the source pack does not establish the behavior or reliability of any particular service. Separate protocol-level claims from service-level claims, and verify the latter against current, product-specific documentation.

## Limitations and failure modes

A base-layer label does not guarantee a particular level of security, performance, availability, decentralization, or usability. The source material supports specific design descriptions, not universal rankings or outcome guarantees.

The Bitcoin claim is scoped to its original network design: hashes link blocks, and hash-based proof of work orders history so that replacement requires renewed computational work. It should not be generalized to other networks, which may use different consensus and data-commitment mechanisms. Nor does that description, by itself, answer every operational question about a specific deployment or user’s ability to verify history.

Likewise, Ethereum’s parent-linked block structure establishes an ordered chain of network state, but it does not by itself document every part of Ethereum’s execution, consensus, or operational behavior. A complete technical evaluation requires additional primary sources relevant to the specific question.

Layer 2 dependencies add further boundaries. For an Ethereum rollup, the publication of data to Ethereum and the role of base-layer consensus are important, but the rollup’s proof, data format, sequencing, upgrades, and bridge design differ across systems. A general statement about base-layer inheritance cannot replace a review of those mechanisms. The available claims also do not establish how any particular failure would be detected, recovered from, or resolved.

Finally, modular architecture is a way to allocate functions, not proof that a design is safer or more efficient. Celestia’s model separates execution, settlement, consensus, and data availability, but other protocols may define these functions differently. Any comparison should state whose model and terminology it uses.

## What teams should verify

Before building on, operating, or evaluating a Layer 1 or a dependent system, teams can use the following evidence-led checklist:

1. **Identify the system boundary.** Is the subject a base Layer 1, a Layer 2, an application, or a service? Record which network establishes the relevant base-layer history.
2. **Read the primary protocol documentation.** Confirm the documented block or state structure and the rules used to validate and order updates. Do not infer a network’s consensus mechanism from another network’s design.
3. **Trace the workflow.** Establish how operations are submitted, checked, ordered, published, and observed. Mark steps that depend on software, operators, or external services rather than treating them as protocol guarantees.
4. **Map architectural functions.** If a system uses a modular model, identify where execution, settlement, consensus, and data availability occur. Confirm how that project defines those terms; function labels can vary.
5. **Inspect Layer 2 dependencies individually.** For an Ethereum scaling system, check its proof, data-availability, settlement, governance, and exit mechanisms. For a rollup, also verify its data format, sequencing, upgrades, and bridge design rather than assuming uniform behavior.
6. **Separate documented facts from open questions.** Note the scope of each claim, including whether it applies to an original network design, a particular protocol class, or a named implementation. Seek current primary evidence where details are not established by the sources reviewed here.
7. **Verify operational interfaces separately.** If users rely on a wallet, endpoint, custodian, or application, review current documentation for that specific service. A protocol description alone does not establish a service’s availability or behavior.

The practical result is a comparison grounded in mechanisms: what the base layer records, how it orders updates, which functions it performs, and what dependent systems still require. Bitcoin’s original hash-linked, proof-of-work design and Ethereum’s parent-linked block structure are distinct Layer 1 examples. Their documented differences are useful starting points, but a system-level decision requires evidence about the particular protocol and its dependencies.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
