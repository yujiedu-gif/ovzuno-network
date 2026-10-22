---
title: "New l1 blockchain: how to assess its design and scaling claims"
description: "Learn how to assess a new l1 blockchain’s architecture, scaling approach, and operational evidence, while separating documented capabilities from unverified claims."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["new 1 blockchain"]
author: "editorial_team"
primary_keyword: "new l1 blockchain"
owned_question: "What distinguishes a new Layer 1 blockchain, and how can readers assess its architecture, scaling approach, and evidence of operation?"
risk_level: "medium"
---

A new Layer 1 blockchain is a proposed or operating base network that maintains shared ledger records under its own network rules. To assess one, distinguish its documented architecture from what has been demonstrated: identify how it organizes network functions, what its scaling statements actually measure, and what evidence shows about operation. The evidence available for this explainer does not establish any particular network’s launch status, performance, or security, so those conclusions require network-specific verification.

## What counts as a new l1 blockchain?

A Layer 1, or L1, is commonly used to mean a blockchain’s base network and its protocol. It is a general usage, not a separately standardized technical category. A blockchain can be characterized as a tamper-evident and tamper-resistant ledger implemented in a distributed fashion. Published records cannot simply be changed under normal operation, but that description does not establish that every recorded input is correct or that alteration is impossible in every circumstance. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

“New” describes neither a specific architecture nor a development status. It may refer to a proposed design, a test network, or a network presented as launched. These statuses call for different evidence. A document can describe intended protocol behavior; a claim of operation needs evidence about a running network and what it is doing. The evidence available here does not establish the status of any named network. Do not treat a project’s label or announcement alone as proof that its described architecture is operating.

The key distinction is what the base network itself does and what other systems handle. A useful assessment question is which functions are performed by the base network and which are assigned to external systems. This is a way to organize the inquiry, not a universal classification rule for every design.

For example, some Ethereum Layer 2 systems derive some security from Ethereum’s Layer 1 consensus. The precise guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. This example shows why a label alone does not identify where a system’s rules and assurances come from; it does not establish how a particular new L1 is designed. [source](<https://ethereum.org/developers/docs/scaling/>)

## Identify the network’s core design choices

Begin with primary technical documentation. Look for descriptions of how transactions are handled, how network participants agree on ledger updates, how data is made available, and who can participate in maintaining the ledger. These are questions to investigate, not facts to assume about a particular network. Record what the material states, what it leaves unspecified, and whether its statements concern an intended design or a running implementation.

Then ask whether the design presents its functions as integrated, separated, or delegated to other components. A system architecture can coordinate physical devices, communication and data handling, blockchain records, incentives, and application services. That is one example of a layered architecture, not a universal blueprint for Layer 1 blockchains. Use it as a prompt to locate responsibilities: which component does what, and where does the documentation say that function occurs? [source](<https://arxiv.org/abs/2406.02239>)

Participation claims also need careful reading. A distributed network may reduce the ability of one bad actor to affect consensus as independently operated nodes increase. But node count alone does not show whether operators are independent, geographically diverse, or using different software. It also does not establish who controls block production. Assess the evidence about operator independence and control rather than treating a node total as a complete description of decentralization. [source](<https://csrc.nist.gov/pubs/ir/8202/final>)

For each architectural statement, keep a short evidence record:

- **Claim:** Quote or summarize the specific design statement.
- **Evidence:** Identify the technical document or public record that supports it.
- **Scope:** Note whether it describes a proposed design, software behavior, or operation.
- **Gap:** Record what remains unclear and what evidence would address it.

If the material does not answer a question, mark it “not established.” A broad description such as “distributed” does not by itself explain who operates the components or how responsibilities are divided.

## Examine scaling claims against measurable evidence

Scaling is not one measurement. Throughput concerns how many transactions or operations a system handles over a period; latency concerns how long an operation takes; capacity concerns how much demand it can accommodate; and fees describe costs under specified conditions. A figure for one measure does not establish another. Keep each claim attached to the measure it actually addresses.

A design objective is different from demonstrated performance. Scaling work can seek to increase transaction speed and throughput without sacrificing decentralization or security. That is an objective, not a universal guarantee, a benchmark result, or a score showing that the goal has been achieved. [source](<https://ethereum.org/developers/docs/scaling/>)

Before interpreting a benchmark, look for its methodology and conditions. Check what workload was used, what network state was tested, how measurements were collected, and whether the result comes from a live network or a controlled test. Also determine whether the figure is an estimate, roadmap target, simulation, or observation. Those categories should not be blended into a single claim about present capability.

The evidence available for this explainer supplies no benchmark methodology, results, fee schedule, or operating conditions for a particular new L1. It therefore cannot support a network-specific performance conclusion. If a published number lacks enough detail to interpret it, describe it as an unverified claim, not as a demonstrated capability. If documentation gives a target, call it a target; do not recast it as observed throughput or a guarantee of future capacity.

## Check what is operating and independently verifiable

First establish what status the evidence supports: proposal, test network, or production operation. Seek materials appropriate to that claim. A specification may document intended rules, but it does not alone prove that a running network follows them. An operational claim should be connected to records or technical materials readers can inspect, not inferred from an announcement.

Next, keep three kinds of evidence distinct. Technical documentation can describe a design; operational records can show activity or behavior within their scope; and independent review can examine specified aspects of a system. Evidence in one category does not automatically establish conclusions in another. In particular, neither documentation nor evidence of operation alone demonstrates security.

For a specific network, readers can look for accessible technical specifications, software repositories, explorers, or other public records relevant to the claim being checked. Verify that the record is about the network in question and that it supports the particular statement being made. A public record may help establish that an activity occurred; it does not, by itself, establish that the architecture works as described under all conditions.

The evidence available here does not verify a specific network’s production status, public records, security reviews, or incident history. Those matters remain unestablished. Do not infer reliability or security from a project’s claimed launch, an apparent level of activity, or its description as distributed. Security conclusions require specific evidence and a clear statement of what that evidence covers.

## Separate technical assessment from adoption and risk decisions

Before drawing a conclusion, summarize what the documentation establishes and list unresolved questions. A bounded finding might say that a design document describes a proposed function, while available evidence does not establish live performance or production status. That is more precise than presenting a roadmap statement as an operating capability.

Apply the same evidence discipline to adoption, recovery, fees, and future performance. Each requires specific, current information about the network and the conditions involved. The claims available here do not establish those details for a particular project. Nor do they support a recommendation to use a network or acquire a token. This is an infrastructure-assessment framework, not investment, legal, or tax advice.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Blockchain Technology Overview (NIST IR 8202)](https://csrc.nist.gov/pubs/ir/8202/final) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Decentralized Physical Infrastructure Network (DePIN): Challenges and Opportunities](https://arxiv.org/abs/2406.02239) — arXiv; retrieved 2026-10-19.
