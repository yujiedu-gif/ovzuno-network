---
title: "How to assess new layer 1 blockchain projects"
description: "Learn how to identify new layer 1 blockchain projects, verify their Layer 1 status, and assess architecture, scaling claims, and development evidence."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "new layer 1 blockchain projects"
owned_question: "How can readers identify and assess new Layer 1 blockchain projects by their scaling approach, architecture, and evidence of development?"
risk_level: "medium"
---

To assess new Layer 1 blockchain projects, first verify that a project describes a distinct base network and establish whether that network is proposed, in development, on a testnet, or operating on a mainnet. Then examine the documented scaling design against a defined use case, while separating implemented features from plans and measured outcomes. The evidence available for this guide does not verify named projects or their current development stages, so it supports a repeatable assessment method—not a current project list or project-specific conclusions.

## What qualifies as a new Layer 1 project?

“Layer 1” commonly refers to a base blockchain network and its protocol; it is common usage, not a separately standardized technical category. For a practical screen, look for a distinct network whose own protocol governs its shared transaction history and state. A blockchain can be described as a database shared across networked computers, where blocks cryptographically refer to earlier blocks and nodes use consensus to agree on state. This provides a starting definition, not proof that a particular project meets it. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

The central question is whether the candidate has a network of its own, rather than merely a token, application, or service associated with another network. A token issued on an existing chain is not, by itself, evidence of a new base network. Similarly, an application built on a blockchain and an infrastructure service supporting it should not be counted as separate Layer 1 networks without evidence of their own distinct protocol and network.

A Layer 2 is a particularly important boundary case. In an Ethereum rollup model, transaction execution is separated from the base layer while data is posted to Ethereum, where base-layer consensus establishes the published record. That is not the same classification as a new Layer 1. [source](<https://ethereum.org/developers/docs/scaling/>) Labels can vary in industry usage, so inspect the architecture rather than relying on a project’s label alone.

Keep network identity separate from development stage. A proposal, development network, testnet, and mainnet are not interchangeable descriptions. Assign a stage only when current project materials or network evidence support it. A roadmap can establish that a project states an intention; it does not, by itself, establish that the announced feature or network is operating. Record uncertainty rather than upgrading a plan into an implementation claim.

## How to find projects without treating a list as complete

Start with a defined scope: what kinds of networks you are considering, what time period the evidence covers, and what sources you will treat as sufficient. Those boundaries help readers understand what an eventual candidate set does and does not represent. A set assembled under a particular method should not be described as complete unless the evidence supports that conclusion.

For each candidate, check primary project materials for a distinct network description, a protocol or technical specification, and an explicit development-stage disclosure. Look for an explanation of how transactions are processed or validated, not just general language about speed, decentralization, or innovation. If the documentation does not make the network boundary clear, mark Layer 1 status as unverified and leave the candidate out of a confirmed set.

Keep project identity, network status, and feature status as separate records. The existence of a project page or a token reference does not establish that a base network is live. A specification can describe a design without showing that it has been implemented. A testnet observation, where one is documented, is evidence about that environment; do not describe it as proof of production-network behavior.

For each candidate, distinguish confirmed details from announcements. “The documentation proposes a sharding design” reports a stated plan. “The network uses sharding” asserts implementation and requires different evidence. If the evidence pack or current materials do not establish a claim, omit it or label it as unverified. Here, no project-specific materials are authorized, so naming examples would imply verification that this guide cannot support.

## Assess the scaling design behind each project

Begin by translating a broad scaling claim into a specific mechanism. Ask which protocol function is intended to change and what the project documentation says about how it changes. One useful architecture vocabulary separates execution, settlement, consensus, and data availability into functions that can be assigned to specialized layers. This vocabulary is an analytical framework, not proof that a particular project separates those functions. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

If a project claims parallel execution, examine what work it says can occur in parallel and what coordination or state constraints remain. If it describes sharding, determine what the design partitions and how the network accounts for the resulting state. For another claimed approach, require a technical description that explains the mechanism. Do not infer implementation from a name, roadmap, or general claim of higher capacity. The evidence available here does not establish that any named new Layer 1 uses these mechanisms.

Next, distinguish the proposed mechanism from a performance result. A claim about a design objective is not automatically a measurement of network behavior. For any performance figure, look for the workload, measurement method, network stage, operating conditions, and stated limitations. Without those details, a headline number does not establish how the network would behave for a particular application. Figures measured in materially different conditions should not be treated as directly comparable. If reproducible evidence is absent, describe the figure as unverified or omit it.

Examine dependencies as part of the scaling assessment. Ask which functions remain on the base network and which are delegated elsewhere. Identify what the project says participants or operators must do, what information is available for checking the network’s state, and which components are outside the protocol itself. These questions identify what needs verification; they do not justify assumptions about a project when its documentation is missing or unclear.

Avoid collapsing capacity, decentralization, and security into one verdict. A documented mechanism may support a specific technical claim, but it does not alone establish that the overall design is suitable for every workload or that its operational assumptions are acceptable. Record what the documentation establishes and what remains an open question.

## Verify architecture, status, and evidence

Maintain a claim-by-claim evidence record. For every material statement, capture the source, what it actually says, the network stage it describes, and whether the feature is proposed, implemented, or independently measurable. Keep a specification, a project announcement, a repository artifact, and an explorer observation distinct: each can support different kinds of statements, and none should be stretched beyond its scope.

Check that evidence refers to the same network and feature under review. A project may describe an intended architecture in one document and a separate development environment elsewhere. Do not assume the latter demonstrates every design element in the former. Where status or implementation is unclear, state that rather than inferring a result from an artifact’s existence.

Treat maturity labels cautiously and use only the framework they were designed to describe. The L2BEAT Stages Framework measures rollup maturity in decentralization and trust minimization; it is not a complete security score, and a higher stage does not by itself show that contracts, proof systems, bridges, or implementations are bug-free. It should not be transferred to Layer 1 projects as a general maturity rating. [source](<https://l2beat.com/stages>)

An audit announcement, roadmap, or isolated benchmark also has limited reach. Do not use any one of them as a substitute for evidence of production operation, reliability, security, or performance across workloads. If a claim concerns a security property, recovery process, or operational condition, it needs evidence specific to that claim and to the project being assessed. When suitable current evidence is not available, preserve the uncertainty in the assessment.

## Match project evidence to a defined use case

Before evaluating whether a project is relevant, write down the application requirements. Specify the execution needs, data-handling requirements, needed integrations, and operational constraints that matter to the intended use. This prevents a broad label such as “scalable” from standing in for evidence about a concrete requirement.

Map each requirement to the evidence that addresses it. A practical record can classify a capability as supported by current technical evidence, stated but not independently demonstrated, planned, or unknown. Add the source and any condition that limits the conclusion. If a requirement has no corresponding evidence, mark it unresolved rather than treating the project’s overall description as an answer.

This process can show where the evidence is relevant without producing a universal winner. Two projects may make claims using different mechanisms or measurement conditions, and the available material may not resolve which design better serves a specific application. In that case, report the unresolved comparison instead of forcing a ranking.

Finally, keep token availability, fees, yields, security, recovery, compliance, and local access as separate questions. They require current, suitable evidence and cannot be inferred from a network’s architecture or development stage. The result of this method is a bounded technical assessment: whether a candidate appears to be a distinct Layer 1, what it says about scaling, what is demonstrably implemented, and which assumptions remain to be checked—not investment advice or a recommendation.

## Sources and references

- [Stages Framework](https://l2beat.com/stages) — L2BEAT; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
