---
title: "Examples of layer 2 crypto: networks and designs explained"
description: "Explore examples of layer 2 crypto, including representative networks, their underlying-chain relationships, and key design differences without rankings."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["examples layer 2 crypto"]
author: "editorial_team"
primary_keyword: "examples of layer 2 crypto"
owned_question: "What are representative examples of layer 2 crypto networks, and how can readers distinguish them by design and purpose?"
risk_level: "medium"
---

For builders, operators, and business decision-makers, examples of layer 2 crypto are easiest to understand by examining what each system relies on an underlying blockchain to do. The allowed evidence here supports describing rollup and bridge-related design boundaries, but it does not establish current network names or confirm which named projects meet a particular layer 2 definition. Rather than present an unverified project list, this explainer shows how to evaluate architecture claims and why labels alone are insufficient.

## What counts as a layer 2 crypto network?

A layer 2 is commonly discussed as a system that handles activity beyond a base blockchain while depending on that underlying chain for some functions. But “layer 2” is not a complete architecture specification. To classify a system, identify its relationship to the base chain: which activity occurs elsewhere, what information is published back, and what role the underlying chain plays.

A rollup is one specific design pattern. It separates transaction execution from the base layer while posting data to the underlying chain, where base-layer consensus establishes the published record. This gives readers a concrete architectural test: does the system execute transactions away from the base layer and publish data there? Even when that pattern applies, implementations can differ in proof systems, data formats, sequencing, upgrades, and bridge design. The shared label does not establish that these mechanisms are identical.

A system that connects to another blockchain is not automatically a rollup or a layer 2. Bridges coordinate token, message, data, or contract-call activity between otherwise isolated blockchain environments. A destination chain changes only after its bridge-side logic accepts the relevant cross-chain message or transfer condition. That connection describes a relationship between environments; it does not, by itself, show that one chain provides the other’s consensus or data availability.

Classification terms can vary among sources. One documented distinction reserves “rollup” for systems that use a base chain for consensus and data availability, while systems that publish data elsewhere add external data-availability assumptions and may be categorized differently. Since labels are not uniform, explain the architecture directly instead of relying on a name or marketing category.

## Examples of layer 2 crypto networks by design

A useful named-network reference list needs current technical documentation for each network, showing its underlying-chain relationship and relevant architecture. The allowed evidence for this article does not verify representative project names or their current classifications. Naming networks anyway would create a false impression that their status had been checked. The categories below therefore describe documented design patterns rather than a roster of projects.

- **Rollups:** These separate transaction execution from the base layer and publish data to the underlying chain, whose consensus establishes the published record. This is a broad architecture pattern, not a statement that all rollups implement the same proof, sequencing, upgrade, or bridge arrangements.
- **Systems that publish data elsewhere:** Under one classification approach, a system that relies on an external data-availability arrangement differs from a rollup that uses its base chain for data availability. The external arrangement introduces assumptions beyond the base-chain publication pattern. The label a source applies may therefore depend on its taxonomy.
- **Bridge-connected blockchain environments:** A bridge can coordinate activity across separate chains. The destination environment changes after its bridge-side logic accepts a cross-chain message or transfer condition. This describes how environments are connected, not proof that the destination is a rollup or inherits the other chain’s role.

These categories are not a substitute for a project-specific technical review. They should not be read as a ranking, endorsement, or claim about live fees, speed, throughput, confirmation times, or adoption. No network-specific performance or status conclusion follows from the general mechanisms described here.

## How rollup examples differ from other layer 2 designs

The key distinction is the relationship between off-base-layer activity and the underlying chain. In the rollup pattern described above, transactions execute outside the base layer, while data is posted to the underlying chain. The base chain’s consensus establishes the published record. That description helps identify the architecture, but it does not tell a reader every detail of a particular network’s implementation.

Data availability is one important classification question. It concerns where the data needed to support the system’s published activity is made available. A system that publishes data to its underlying chain has a different data-publication relationship from one that uses an external arrangement. Under the cited classification approach, the latter has additional external data-availability assumptions and may not be classified as a rollup. Treat this as a distinction about dependencies and terminology, not as a complete security assessment.

Bridges are another boundary to keep separate. They coordinate activity between otherwise isolated blockchain environments, but they do not collapse those environments into one chain. Since the destination changes only after its bridge-side logic accepts the message or transfer condition, a reviewer should identify that logic and its role rather than infer security properties from the word “bridge.” The evidence available here does not support a broader claim that any particular bridge-connected system inherits the security of another chain.

These architecture distinctions should also remain separate from operational measurements. The design descriptions do not establish a network’s current fees, throughput, or confirmation times. Such measurements are time-sensitive and require separate, dated evidence. They are not needed to answer the classification question: where does execution happen, where is data published, and what function does the underlying chain perform?

## What to verify before classifying a network as layer 2

When reviewing a named network, use its technical documentation to answer a set of specific questions. Record the date and scope of the documentation, because an architecture label is only as useful as the description behind it.

1. **What is the claimed underlying chain?** Identify the chain the project says it relies on, then look for the specific functions assigned to that chain. A vague statement that a network is “built on” another chain does not identify what is actually delegated to it.
2. **Where does transaction execution occur?** Check whether the documentation describes execution away from the base layer. If it does, identify what happens to the resulting state changes and how the system reports them to the underlying chain.
3. **Where is data published?** Distinguish publication to the underlying chain from reliance on an external data-availability arrangement. This is a key architectural distinction and may change how classification sources use the term “rollup.”
4. **What is the relationship to other chains?** If a bridge is involved, determine what the bridge-side logic accepts before the destination chain changes. A bridge connection alone does not establish that the destination system is a rollup.
5. **Which functions belong to which components?** Separate the role of the underlying blockchain from the roles of the layer 2 system and any bridge-side logic. Do not infer that the underlying chain operates every component merely because the project uses it as a base.
6. **What terminology does the source use?** If sources disagree, compare the described mechanisms rather than treating one label as definitive. State whether the classification depends on a particular definition, especially for systems with external data availability.
7. **Is the claim current and appropriately limited?** Use dated technical documentation for architecture-dependent statements. Keep those statements separate from live performance claims, which require their own evidence.

This process produces a more precise reference than a bare list of names. The evidence supplied for this article supports explaining rollup publication, external data-availability classification, and bridge relationships; it does not verify a current catalog of named layer 2 networks. A reader should therefore treat the design categories as a framework for evaluating project documentation, not as a project roster or a guarantee of equivalent security or decentralization.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
