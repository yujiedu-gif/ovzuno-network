---
title: "Blockchain Layer 1 and Layer 2: How It Works"
description: "Understand Blockchain Layer 1 and Layer 2, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["blockchain layer 1 layer 2"]
author: "editorial_team"
primary_keyword: "blockchain layer 1 and layer 2"
owned_question: "How do Layer 1 and Layer 2 blockchains differ, and how do they work together to scale blockchain networks?"
risk_level: "medium"
---

# Blockchain Layer 1 and Layer 2: How It Works

Layer 1 and Layer 2 describe different roles in a blockchain system. A Layer 1 is the base network where its consensus process establishes an agreed record. A Layer 2 is a separate system that performs some work away from that base layer and may use it for particular functions, such as publishing data or settling outcomes. The labels do not by themselves specify how a system is secured, how users exit, or which operators control it.

Ethereum scaling documentation describes rollups as one Layer 2 approach: transactions execute outside Ethereum, while transaction data or commitments are posted to Ethereum. The rollup separates execution from the base layer, but uses the base layer’s consensus to establish the published record. The exact security guarantees depend on the rollup’s proof, data-availability, settlement, governance, and exit mechanisms. [claim_rollup_batching] [claim_rollup_separation] [claim_l2_derives_l1_security]

## What Blockchain Layer 1 and Layer 2 means

A Layer 1 is the base blockchain in the relationship being discussed. It provides the consensus layer against which published records can be established. A Layer 2 is not simply a faster mode of the Layer 1: it is an additional system that handles activity outside the base layer and connects back to it in defined ways.

The distinction is easiest to understand by separating four functions: execution, settlement, consensus, and data availability. Execution is where transactions are processed and state changes are computed. Settlement concerns how outcomes or claims are resolved against a base network. Consensus is the mechanism by which network participants establish an agreed record. Data availability concerns whether the information needed to inspect or reconstruct activity is accessible.

In a monolithic architecture, a base layer performs execution, settlement, consensus, and data availability together. A modular architecture can assign these functions to specialized layers. These categories are a useful model, not a universal naming rule: architecture literature may group functions differently, and real deployments may be only partly modular. [claim_integrated_separated]

“Scaling” describes a design objective, not a guaranteed performance result. Ethereum’s scaling overview frames the goal as increasing transaction speed and throughput without sacrificing decentralization or security, while recognizing that implementations make different architectural and trust trade-offs. The objective is therefore not proof that every design achieves all three properties equally. [claim_scaling_three_goals]

## Core components of Blockchain Layer 1 and Layer 2

A Layer 1 and Layer 2 arrangement can include the following components, although their implementation varies:

- **Base-layer consensus and record:** The Layer 1 network establishes consensus over the records published to it. In the Ethereum rollup model, this is where the published data or commitments become part of the base-layer record.
- **Layer 2 execution environment:** The Layer 2 processes transactions outside the base layer. Its execution rules and state are distinct from simply running each transaction directly on Layer 1.
- **Publication path:** A rollup posts transaction data or commitments to Layer 1. The publication format differs among rollups, so “posting” should not be assumed to mean identical or complete transaction information in every design.
- **Proof and settlement mechanisms:** A rollup’s proof design and settlement process affect how its claims are checked and resolved. The broad label “rollup” does not specify one proof system or one guarantee.
- **Data-availability arrangement:** The location and accessibility of data matter to what users or independent parties can verify. Data availability is one of the mechanisms that affects a system’s security, and it should be examined separately from execution speed.
- **Sequencing, governance, upgrades, and exit:** Rollups differ in sequencing, upgrade, governance, and bridge design. These operational and control components influence how the system behaves and how users can leave or respond to changes.

This list is a way to map responsibilities, not a claim that every Layer 2 uses identical components or assigns them to the same operators. The specific design must be established from its documentation and deployed implementation. [claim_rollup_separation] [claim_l2_derives_l1_security]

## How Blockchain Layer 1 and Layer 2 works

A simplified rollup workflow can be traced in stages:

1. **A user submits a transaction to the Layer 2.** The transaction is handled by the Layer 2 execution system rather than being executed directly on the base layer.
2. **The Layer 2 processes transactions.** Multiple transactions can be handled as a batch. The term “rollup” refers to an architecture that executes transactions outside Layer 1 and posts transaction data or commitments to Layer 1; the precise batch and publication format varies.
3. **The system publishes data or commitments to Layer 1.** This creates a connection between the Layer 2’s activity and the base network. A commitment is not interchangeable with all underlying transaction data, so readers should check what is actually published and what information remains available elsewhere.
4. **Layer 1 consensus establishes the published record.** For the described Ethereum rollup model, the base layer provides consensus and settlement functions for the published material. This does not mean that Layer 1 executes every Layer 2 transaction.
5. **The rollup’s proof and settlement design governs how outcomes are checked.** The relevant mechanisms vary. A general description of rollups cannot establish the precise validation, challenge, finality, or exit process of a particular deployment.
6. **Users and operators rely on the system’s exit and data mechanisms.** Whether users can independently verify activity or exit under particular conditions depends on the design, including data availability and bridge or exit mechanisms. Those details need system-specific verification.

Batching can allow many Layer 2 transactions to use the base layer for consensus and settlement, but it does not guarantee lower fees or higher throughput for every transaction or operating condition. Publication format and proof design differ among rollups. [claim_rollup_batching]

## Trust and control boundaries

A Layer 2 may derive some security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. “Some” is important: this does not mean that Layer 1 automatically protects every part of the Layer 2 or that every rollup has the same security profile. The exact guarantee depends on proof, data-availability, settlement, governance, and exit mechanisms. [claim_l2_derives_l1_security]

A practical trust analysis separates what the base layer does from what the Layer 2 must do. Layer 1 consensus can establish the published record, while the Layer 2 still has its own execution and operational design. Sequencing, upgrades, governance, proof verification, and exit arrangements should not be treated as interchangeable or inferred merely from the Layer 2 label. Rollups differ in these areas, as well as in data format and bridge design. [claim_rollup_separation]

The distinction also matters for custody and operations. The architecture alone does not establish who controls a user’s keys, which interfaces a user relies on, or whether a particular service can pause or alter access. Those are implementation- and service-specific questions. A technical review should therefore distinguish protocol-level mechanisms from the controls of wallets, bridges, sequencers, and other services involved in a deployment.

## Limitations and failure modes

Layer 2 is not a blanket guarantee of lower cost, greater capacity, or equivalent security. The accepted architecture claims support a narrower conclusion: rollups move execution outside Layer 1 and publish data or commitments to it, but their proof systems and publication formats vary, and fees or throughput are not guaranteed to improve for every transaction or condition. [claim_rollup_batching]

Potential weaknesses must be evaluated through the system’s actual dependencies. If data needed to inspect or reconstruct activity is not available as expected, the practical ability to verify or exit may be affected; the relevant data-availability and exit mechanisms are system-specific. Likewise, proof, settlement, governance, upgrade, sequencing, and bridge designs can change the trust assumptions. The general category does not establish how any particular failure is handled.

There is also no universal architecture score implied by the phrase “scaling.” Increasing speed and throughput while preserving decentralization and security is a design objective, and implementations make different trade-offs. A comparison should identify which properties are documented and which remain assumptions rather than treating the objective as a guaranteed outcome. [claim_scaling_three_goals]

## What teams should verify

Builders, operators, institutions, and technical decision-makers can use the following evidence checklist when assessing a Layer 1 and Layer 2 design:

1. **Map the functions.** Identify where execution, settlement, consensus, and data availability occur. Determine whether the architecture is monolithic, modular, or partly modular, using the deployment’s own technical documentation rather than assuming standard labels.
2. **Inspect what is published.** Confirm whether the Layer 2 posts transaction data, commitments, or another specified format to Layer 1. Identify what users or independent parties can obtain and what is not included in the published record.
3. **Trace the proof and settlement path.** Find the documented proof design and how claims are resolved against Layer 1. Do not infer a specific validation or finality guarantee from the word “rollup.”
4. **Check data availability.** Determine which system makes required data available, how that arrangement is verified, and what the documented consequences are if data cannot be obtained.
5. **Review exits and bridges.** Establish how users exit, what conditions apply, and which bridge mechanisms are involved. Confirm whether the documented process depends on particular operators or services.
6. **Identify control and upgrade authority.** Review sequencing, governance, and upgrade mechanisms. Record who or what can change the system and what constraints the documentation describes.
7. **Separate protocol from service dependencies.** Map wallets, interfaces, custody arrangements, and other operational services separately from the protocol’s consensus and settlement claims.
8. **Treat performance as conditional.** Check evidence for the actual workload and operating conditions of interest. Do not assume that batching ensures lower fees or higher throughput in every case.
9. **State the trust assumptions explicitly.** Describe which security properties come from Layer 1 consensus and which depend on Layer 2 proof, data, governance, settlement, or exit mechanisms.

The central distinction is functional: Layer 1 provides the base network, while a Layer 2 can execute activity separately and use the base layer for specified publication, consensus, or settlement roles. How well the combination scales—and what users must trust—depends on the architecture and its concrete mechanisms, not on the labels alone.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
