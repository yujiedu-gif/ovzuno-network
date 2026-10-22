---
title: "Layer 2 Solutions: How They Extend Blockchain Capacity"
description: "Learn what layer 2 solutions are, how they connect to a base blockchain, and which architecture, settlement, and security trade-offs to examine."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 solutions"
owned_question: "What are layer 2 solutions, how do they relate to an underlying blockchain, and what trade-offs should readers understand?"
risk_level: "medium"
---

Layer 2 solutions process some blockchain activity outside a base blockchain’s direct execution path, while using that underlying network for selected functions. Their designs differ in what information they publish, how results are checked, and which functions the base layer performs, so the term “layer 2” alone does not establish a system’s security or performance properties.

## What layer 2 solutions mean

A base blockchain, often called layer 1, is the underlying network to which a layer 2 design connects. A blockchain can be understood as a database updated and shared across networked computers: blocks cryptographically reference earlier blocks, and nodes use consensus to agree on state. The phrase “layer 2” describes an architecture built around a base network, not one standardized technology with identical rules in every implementation. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The broad purpose is to handle some activity away from direct execution on the base layer. Depending on the design, the base chain may then have a role in recording information, verifying a claim, or settling an outcome. The term does not mean that all activity is processed in the same way, nor does it by itself establish how much the system depends on the underlying chain.

A useful starting point is to distinguish a layer 2 architecture from an application that simply uses a blockchain. The key question is how the system’s processing and records relate to the base chain: which work happens outside it, what is sent back, and what the underlying network actually checks or records. The label alone cannot answer those questions.

## How activity connects to the base layer

To read an architecture, separate four functions: execution, settlement, consensus, and data availability. Execution processes transactions and determines resulting state changes. Settlement concerns how claims or outcomes are resolved against an underlying system. Consensus is the method participants use to agree on a record. Data availability concerns whether participants can obtain the transaction data needed to verify summarized state changes. An architecture can assign these functions to different places rather than treating them as one job. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A high-level lifecycle begins with activity being processed outside the base layer’s direct execution path. The layer 2 system then communicates selected information to the underlying network. What it sends depends on its design: documentation may describe transaction data, a summary or commitment, or a proof about a proposed state transition. The base layer’s role is determined by what it receives and what its protocol or contracts verify—not by the layer 2 label.

When examining a system, trace the activity through three questions. First, where are transactions executed? Second, what record, data, or proof is published to the base chain? Third, what does that chain independently record or verify? Then investigate where the information needed to check or reconstruct activity is available. Data availability is not simply another name for settlement: it addresses access to data needed for verification, while settlement concerns how outcomes are resolved.

This map also helps avoid overclaiming. A record being posted to a base chain does not, by itself, explain every offchain dependency or show that every element of the system is checked there. The architecture documentation should specify the boundary between layer 2 processing and the base layer’s contribution.

## Rollups and other design approaches

Rollups are a prominent architectural pattern. They separate transaction execution from the base layer while posting data to the underlying chain, where base-layer consensus establishes the published record. A rollup can execute activity in batches outside the base layer and post transaction data or commitments so the base layer can provide consensus and settlement functions. The exact publication format and proof design differ across rollups. [source](<https://ethereum.org/developers/docs/scaling/>)

Rollups also illustrate how verification approaches can differ. Some use an optimistic acceptance model: a state transition may be challenged during a challenge period through a fraud-proof process. Others use a validity-proof approach in which a base-layer verifier accepts a cryptographic proof for a proposed offchain state transition. These are distinct patterns, not interchangeable labels. Neither description alone proves that a particular deployment’s contracts, proof implementation, data handling, or operational controls are correct.

Other approaches may organize responsibilities differently. Architecture frameworks distinguish a monolithic arrangement, where a base layer performs execution, settlement, consensus, and data availability together, from a modular arrangement, where those functions can be assigned to specialized layers. These terms are useful for describing system structure, but the boundaries and dependencies must be checked in the implementation’s own documentation. A scaling approach should be assessed by its documented architecture rather than assumed to match rollups. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

## Trade-offs behind layer 2 designs

Moving some execution away from a base chain is an architectural choice, not a quantified promise. Throughput, latency, costs, and user experience cannot be inferred from the category name. To assess a specific performance claim, evidence needs to identify the system, the measurement being made, and the operating conditions. Without that scope, a broad comparison can imply more than the evidence establishes.

Security assumptions follow the division of responsibilities. A design may rely on a base layer for some functions while depending on separate components for others. Its documented proof or dispute process, data publication, and settlement path each address particular parts of the system; none should be treated as a complete security guarantee. A maturity framework, when one is used, can measure decentralization and trust minimization, but it is not a complete security score. [source](<https://l2beat.com/stages>)

Bridges require their own analysis when they coordinate activity across separate ledgers. They are not simply a continuation of one chain’s transaction process: the destination-side action depends on the bridge’s design and its handling of cross-chain information. For a system that relies on a bridge, investigate how source-chain activity is verified and which components or rules authorize the corresponding destination-side change. Do not assume that a general layer 2 description covers bridge behavior.

The division of work also raises operational questions. System-specific documentation should identify which components process or order activity, what is published to the base layer, and how the design handles verification and settlement. It should also explain its documented authority and recovery arrangements. The category name does not settle these questions, and this overview does not establish particular performance, security, fee, asset-support, or recovery characteristics for any network.

## Questions to investigate before evaluating a network

Use a system’s technical documentation to build a concrete map before drawing conclusions:

- **Map the functions:** locate execution, settlement, consensus, and data availability, and note where the system assigns each one.
- **Follow the information:** identify what activity or proof is published to the base layer and what that layer is specified to check or record.
- **Understand verification:** determine whether the documented design uses a dispute process, a validity proof, or another mechanism, and note what the mechanism does not establish.
- **Check operational roles:** identify which components process activity and what the documentation says about authority, system changes, and recovery.
- **Verify current operational details independently:** fees, supported assets, availability, and system-specific security claims are outside what the general term “layer 2” can establish. Confirm them using current evidence for the particular system.

The central distinction is that a layer 2 system processes some activity away from a base blockchain, while the underlying chain performs only the functions assigned to it by that architecture. The meaningful trade-offs depend on where execution, data availability, verification, consensus, and settlement occur—and on the specific assumptions documented for each component.

## Sources and references

- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
