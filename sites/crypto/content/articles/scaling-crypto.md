---
title: "Scaling crypto: What it means and how approaches differ"
description: "Learn what scaling crypto means, which parts of a blockchain system can change, and how capacity approaches involve trade-offs in verification and coordination."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "scaling crypto"
owned_question: "What does scaling crypto mean, which parts of a blockchain system can be scaled, and what trade-offs do different approaches involve?"
risk_level: "medium"
---

Scaling crypto means increasing a blockchain system’s capacity to handle more activity while pursuing its intended security and decentralization properties. It is a system-level design goal, not a single speed or fee number: capacity depends on which system functions change, what resources they require, and how participants verify the results. The goal of increasing transaction speed and throughput without sacrificing decentralization or security is an objective, not a guarantee that any particular approach achieves it. [source](<https://ethereum.org/developers/docs/scaling/>)

## What scaling crypto means

A scaling claim is useful only when it identifies what kind of capacity is increasing and under what conditions. Transaction throughput, time to a stated outcome, and cost describe different things; one does not automatically establish the others. A single throughput figure, for example, does not show what the system can sustain under other workloads or what participants must do to verify it.

It helps to distinguish capacity from observed performance. Capacity concerns the system’s ability to handle activity under stated design assumptions. Observed performance describes results under particular operating conditions. To interpret a reported result, look for the workload, measurement method, and conditions behind it. Without those details, a number may not support a useful comparison.

Scaling also concerns more than transaction processing in isolation. A system can distribute work among distinct functions or components, so a change that increases activity in one part may affect the demands placed on another. The central question is therefore not just how much activity a system reports handling, but what parts of the system do the work and what verification and coordination remain necessary.

## Where capacity constraints can arise

A useful conceptual map separates four functions: **execution**, which processes transactions and changes state; **data availability**, the question of whether relevant data can be accessed; **consensus**, through which a network agrees on blocks or state; and **settlement**, where an outcome is established on a system serving as the record for that activity. These functions can be assigned differently across system designs. The modular model described by Celestia, for example, treats execution, settlement, consensus, and data availability as functions that can be assigned to specialized layers.

Different resources can matter to different functions. Execution requires computation. Moving and publishing data depends on communication and data handling. Keeping ledger information involves storage, while checking outcomes requires participants to obtain relevant information and apply the system’s rules. The evidence available here does not establish one universal resource limit or a single formula for combining these constraints; their importance depends on the network and design being evaluated.

This is why improving one function may move a bottleneck rather than remove it. If a design changes where execution happens, for instance, the questions about data access, agreement, and settlement still need answers. Consider the full path: where activity is processed, what information is published, who can check the result, and which component establishes the relevant outcome.

## Broad ways crypto systems scale

One broad direction is to increase capacity within a base network. This focuses on having the base system handle more activity, but the category alone does not say which function changes, what resource demand rises, or how independently participants can verify the system. Those details must be assessed for the specific design.

A second direction is to process activity outside a base layer while using that layer for some other functions. In the rollup pattern, transactions execute outside Layer 1, while transaction data or commitments are posted to Layer 1 so batches can use it for consensus and settlement. This is an architectural pattern, not a universal performance result: publication formats and proof designs vary, and lower fees or higher throughput are not guaranteed for every transaction or operating condition. [source](<https://ethereum.org/developers/docs/scaling/>)

A third direction is to divide or specialize system functions. Rather than assigning every function to one layer, a design can assign different functions to specialized components. This can change where computation, data handling, or other responsibilities occur. Separation does not by itself establish that overall capacity increased or specify what security properties the system provides.

These approaches are broad, conceptual directions, not necessarily exclusive categories. A system may combine them. To understand what a proposal changes, examine the functions and dependencies rather than relying on a label.

## Trade-offs to examine

Start with verification. Ask what information participants need to check transactions or state changes and whether they can obtain it under the design. A capacity claim does not answer that question by itself. Also ask which participants are expected to verify results and what software or resources that task requires; the relevant requirements depend on the system.

Next, examine coordination and trust assumptions when activity spans layers or networks. Separate components must fit together for the system to operate as intended, but the architecture label does not explain who operates them or how they are governed. Participation models are also distinct: some networks are permissionless, while others restrict ledger maintenance to authorized users; access to read or submit transactions can also be restricted. Real systems can assign these rights separately or combine open submission with restricted validation. [source](<https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf>)

Consider whether the design’s stated capacity is theoretical or observed under operating conditions. A design objective is not a measurement. A reported result needs a defined workload and method to show what it represents. Likewise, security and decentralization implications depend on the architecture and evidence, not simply on whether a system is described as base-layer, multi-network, or modular.

Finally, look for work or responsibility that shifts to users, operators, or other components. A change may reduce demands on one part while increasing demands elsewhere. The useful question is whether the whole arrangement’s verification and coordination requirements are clear—not just whether one component reports higher capacity.

## A framework for evaluating a scaling claim

Use these questions to make a claim concrete:

1. **Which bottleneck is being addressed?** Identify the function or resource the proposal changes, such as execution, data handling, computation, or storage.
2. **What does the metric measure?** Check whether it concerns throughput, time to a specified outcome, or cost, and whether the workload, conditions, and method are stated.
3. **Who can verify the result?** Find out what information and capabilities participants need to check the relevant outcomes.
4. **What dependencies are introduced?** Identify which components must coordinate and what participation or operating assumptions the design relies on.
5. **Where does the work move?** Compare responsibilities across the system rather than treating a local capacity change as evidence of system-wide improvement.

This framework does not rank implementations or predict how a particular network will perform. It helps separate an architectural proposal from evidence about its operation. A well-scoped scaling claim identifies the function being changed, explains what its metric represents, and makes the remaining verification and coordination requirements visible. Without those details, a headline number or category name cannot show how the system handles more activity or what trade-offs accompany that change.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) — National Institute of Standards and Technology; retrieved 2026-10-19.
