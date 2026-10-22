---
title: "Blockchain L1 L2: Roles, Differences, and Dependencies"
description: "Learn what blockchain L1 L2 mean, how base and scaling layers differ, and which functions to examine when assessing their relationship and dependencies."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["blockchain 1 2"]
author: "editorial_team"
primary_keyword: "blockchain l1 l2"
owned_question: "What do blockchain L1 and L2 mean, how do their roles differ, and how can an L2 depend on an L1?"
risk_level: "medium"
---

For readers encountering the terms in a network description, **Layer 1 (L1)** is the base blockchain in that architecture, while **Layer 2 (L2)** is a separate system designed to work with an L1. The labels identify roles, not a ranking of quality or a complete description of security. To understand the relationship, trace where execution, data availability, settlement, and security responsibilities lie—and what assumptions connect the layers.

## What L1 and L2 mean in blockchain

A blockchain is a database shared across networked computers. Blocks cryptographically reference earlier blocks, and nodes use consensus to agree on network state. In a layered architecture, **L1** refers to the base blockchain network and its protocol. **L2** refers to a separate system designed to handle activity in relation to that base. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The terms are relational: a component is described as an L2 in connection with a particular L1. The label alone does not tell you which transactions the system processes, which records it publishes, or what the L1 checks. Nor does it establish that the L2 has a particular security property. Those details come from the system’s design and its connection to the base chain.

It is therefore useful to read “L1” and “L2” as a first-pass map. The L1 is the base in the relationship being described; the L2 is a separate system built to work with it. Project terminology can vary, so the functions and dependencies matter more than the name. The question is not simply “Which layer is it?” but “What does this layer do, and which other layer does it rely on?”

## How an L1 and L2 divide responsibilities

A practical way to compare layers is to examine four functions: **execution, data availability, settlement, and consensus**. Execution is where transactions are processed and state changes are computed. Data availability concerns where the information needed to check those changes can be obtained. Settlement concerns where results are established or recorded for the architecture. Consensus is how participants agree on a network’s state.

These functions need not all be performed by one system. A modular blockchain model can assign execution, settlement, consensus, and data availability to specialized layers. By contrast, a monolithic base layer performs those functions together. Real architectures may also combine approaches, so these categories are a framework for asking questions rather than a rule that every system fits neatly. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>) [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

For a specific L1–L2 relationship, ask:

- **Execution:** Which system processes transactions and calculates the resulting state changes?
- **Data availability:** Where is the information needed to check those changes made available?
- **Settlement:** Which layer records or resolves the results the system treats as settled?
- **Consensus and security:** Which protocol rules support agreement on the relevant state, and what assumptions does the arrangement add?

The answers may point to different layers. An L2 can execute activity separately while depending on an L1 for one or more other functions. “The L2 uses the L1” is therefore incomplete unless the description says how: for example, whether it publishes information there, relies on it to establish results, or uses it in a dispute process. The function-by-function view prevents a reader from treating a single connection as proof that the two systems share every responsibility.

## How L2 systems depend on an L1

To understand dependence, follow the information and state changes between systems. Start by identifying where the L2 processes activity and maintains its state. Then look for what it sends or publishes to the L1. Finally, determine what the L1 does with that information and which mechanisms establish or challenge the L2’s reported outcomes. This sequence distinguishes a technical dependency from a general claim that two systems are connected.

An Ethereum Layer 2 is one example of a system that may derive some security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. The extent of that dependence is system-specific: it depends on the proof, data-availability, settlement, governance, and exit mechanisms involved. [source](<https://ethereum.org/developers/docs/scaling/>)

That qualification matters. Saying that an L2 derives some security from an L1 does not mean that it has identical security, that every operation is checked in the same way, or that additional assumptions disappear. The phrase “uses L1 security” is not a complete account of what the L1 guarantees. Readers need to identify the particular mechanism and the functions it covers before drawing conclusions.

A system can also rely on the L1 for one responsibility while handling others through its own components or different mechanisms. Thus, the dependency is not simply a question of whether the L2 has an L1 connection. It is a map of which layer supplies or verifies which function, and which trust assumptions remain elsewhere in the design. If documentation does not specify those handoffs, the label alone cannot fill in the missing details.

## What L1 and L2 do—and do not—tell you

The labels describe architectural roles. On their own, they do not establish comparative throughput, fees, decentralization, or security. Those are separate claims about a particular system and its conditions; they cannot be inferred just from the words “L1” or “L2.” A reader should look for the design details and evidence relevant to the specific comparison rather than treating the category as a measurement.

Nor is “L2” a single architecture. Systems can divide execution, settlement, consensus, and data availability differently, and modularity can be partial. The appropriate distinction depends on what functions the system performs and where. A label may be convenient shorthand, but it does not replace a description of the actual division of work. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>) [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

A maturity label or framework also has a defined scope. For example, the L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization. A higher stage is not a complete security score and does not establish that contracts, proof systems, bridges, or implementations are free of bugs. That framework illustrates why a narrow category should not be mistaken for a universal verdict on a system. [source](<https://l2beat.com/stages>)

For the same reason, avoid collapsing separate questions into one conclusion. A system’s use of an L1 does not by itself answer where data is available, what results are settled there, or which assumptions apply to the L2’s own operation. Similarly, a statement about one function should not be read as a statement about every other function. Each part of the architecture needs to be understood on its own terms.

## A practical checklist for reading L1 and L2 descriptions

When you see an L1 or L2 label, use the following sequence to clarify what it means in context:

1. **Identify the relationship.** Which blockchain is the stated L1, and which separate system is called its L2? Treat the labels as architecture-specific rather than as universal categories with guaranteed properties.
2. **Locate execution.** Find where transactions are processed and state changes are computed. If the description is unclear, the L2 label does not resolve that uncertainty.
3. **Locate data availability.** Determine where the information needed to check the changes can be obtained. Do not assume that execution and data availability occur in the same place.
4. **Locate settlement.** Ask which layer establishes or records the outcomes, and what the other layer contributes. Look for the actual mechanism rather than relying on general terms such as “anchored” or “secured.”
5. **Trace security dependencies.** Identify which L1 function the L2 depends on, how that function is used, and which assumptions remain outside it. The amount and form of security derived from an L1 vary by system.
6. **Separate role labels from claims.** Evaluate statements about fees, throughput, decentralization, or security as claims about a particular design—not as consequences of being called an L1 or L2.
7. **Check the documentation’s limits.** If project material does not describe the handoffs or relevant assumptions, mark the point as unknown rather than treating the layer label as a substitute for evidence.

The core distinction is straightforward: L1 names the base blockchain in a stated architecture, and L2 names a separate system designed to work with it. The useful technical explanation comes from tracing execution, data availability, settlement, and security dependencies between them. Those functions may be split in different ways, so the labels are a starting point for reading an architecture—not a complete account of how it works.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
